# Copyright 2017 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Experimental API for TensorFlow's "Eager" mode of execution."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import contextlib
import copy
import threading

from tensorflow.python import pywrap_tensorflow
from tensorflow.python.framework import device as pydev
from tensorflow.python.framework import errors
from tensorflow.python.platform import app
from tensorflow.python.util import compat
from tensorflow.python.util import tf_contextlib
from tensorflow.python.util import tf_inspect

GRAPH_MODE = 0
EAGER_MODE = 1

# Default execution mode.
_default_mode = GRAPH_MODE

# Cache from (old_device_name, partial_new_device_name) -> (new_device_name,
# new_device_spec).
# Note that we do not protect this with a lock and instead rely on python's GIL
# and the idempotent nature of writes to provide thread safety.
_device_parsing_cache = {}


# TODO(agarwal): better name ?
class _EagerContext(threading.local):
  """Thread local eager context."""

  def __init__(self):
    super(_EagerContext, self).__init__()
    self.device_spec = pydev.DeviceSpec.from_string("")
    self.device_name = self.device_spec.to_string()
    self.mode = _default_mode
    self.scope_name = ""
    self.recording_summaries = False
    self.scalar_cache = {}


# TODO(agarwal): rename to EagerContext / EagerRuntime ?
# TODO(agarwal): consider keeping the corresponding Graph here.
class Context(object):
  """Environment in which eager operations execute."""

  def __init__(self, config=None):
    """Creates a new Context.

    Args:
      config: (Optional.) A `ConfigProto` protocol buffer with configuration
      options for the Context. Note that a lot of these options may be
      currently unimplemented or irrelevant for EAGER mode.
    """
    self._eager_context = _EagerContext()
    self._context_handle = None
    self._context_devices = None
    self._summary_writer_resource = None
    self._post_execution_callbacks = []
    self._config = config
    self._initialize_lock = threading.Lock()

  def _initialize_handle_and_devices(self):
    """Initialize handle and devices."""
    with self._initialize_lock:
      if self._context_handle is not None:
        return
      assert self._context_devices is None
      opts = pywrap_tensorflow.TF_NewSessionOptions(
          target=compat.as_bytes(""), config=self._config)
      with errors.raise_exception_on_not_ok_status() as status:
        self._context_handle = pywrap_tensorflow.TFE_NewContext(opts, status)
        pywrap_tensorflow.TF_DeleteSessionOptions(opts)
      # Store list of devices
      self._context_devices = []
      with errors.raise_exception_on_not_ok_status() as status:
        device_list = pywrap_tensorflow.TFE_ContextListDevices(
            self._context_handle, status)
      try:
        for i in range(pywrap_tensorflow.TF_DeviceListCount(device_list)):
          with errors.raise_exception_on_not_ok_status() as status:
            dev_name = pywrap_tensorflow.TF_DeviceListName(
                device_list, i, status)
          self._context_devices.append(pydev.canonical_name(dev_name))
      finally:
        pywrap_tensorflow.TF_DeleteDeviceList(device_list)

  @property
  def _handle(self):
    ctx = self._context_handle
    if ctx is None:
      self._initialize_handle_and_devices()
      return self._context_handle
    else:
      return ctx

  @property
  def _devices(self):
    devices = self._context_devices
    if devices is None:
      self._initialize_handle_and_devices()
      return self._context_devices
    else:
      return devices

  def __str__(self):
    if self._context_handle is None:
      return "Eager TensorFlow Context. Devices currently uninitialized."
    else:
      devices = self._devices
      lines = ["Eager TensorFlow Context with %d devices" % (len(devices))]
      for i, d in enumerate(devices):
        lines.append("   Device %d: %s" % (i, d))
      return "\n".join(lines)

  @tf_contextlib.contextmanager
  def _mode(self, mode):
    ctx = self._eager_context
    old_mode = ctx.mode
    ctx.mode = mode
    try:
      yield
    finally:
      ctx.mode = old_mode

  def in_graph_mode(self):
    """Returns True if current thread is in GRAPH mode."""
    return self._eager_context.mode == GRAPH_MODE

  def in_eager_mode(self):
    """Returns True if current thread is in EAGER mode."""
    return self._eager_context.mode == EAGER_MODE

  def scalar_cache(self):
    """Per-device cache for scalars."""
    return self._eager_context.scalar_cache

  @property
  def scope_name(self):
    """Returns scope name for the current thread."""
    return self._eager_context.scope_name

  @scope_name.setter
  def scope_name(self, s):
    """Sets scope name for the current thread."""
    self._eager_context.scope_name = s

  @property
  def summary_writer_resource(self):
    """Returns summary writer resource."""
    return self._summary_writer_resource

  @summary_writer_resource.setter
  def summary_writer_resource(self, resource):
    """Sets summary writer resource."""
    self._summary_writer_resource = resource

  @property
  def device_name(self):
    """Returns the device name for the current thread."""
    return self._eager_context.device_name

  @property
  def device_spec(self):
    """Returns the device spec for the current thread."""
    return self._eager_context.device_spec

  @tf_contextlib.contextmanager
  def device(self, name):
    """Context-manager to force placement of operations and Tensors on a device.

    Args:
      name: Name of the device or None to get default placement.

    Yields:
      Nothing.

    Raises:
      ValueError: If name is not a string or is an invalid device name.
    """
    eager_context = self._eager_context
    old_device_name = eager_context.device_name
    old_device_spec = eager_context.device_spec
    cache_key = (old_device_name, name)
    try:
      new_device_name, new_device_spec = _device_parsing_cache[cache_key]
    except TypeError:
      # Error while trying to compute the cache key.
      raise ValueError("Expecting a string device name. Got %s(%s)" %
                       (type(name), name))
    except KeyError:
      # Handle a cache miss.
      if name is not None:
        if not isinstance(name, str):
          raise ValueError("Expecting a string device name. Got %s(%s)" %
                           (type(name), name))
        device_spec = pydev.DeviceSpec.from_string(name)
        if old_device_name:
          new_device_spec = copy.copy(old_device_spec)
        else:
          new_device_spec = pydev.DeviceSpec.from_string(
              "/job:localhost/replica:0/task:0/device:CPU:0")
        new_device_spec.merge_from(device_spec)
      else:
        new_device_spec = pydev.DeviceSpec.from_string("")
      new_device_name = new_device_spec.to_string()
      _device_parsing_cache[cache_key] = (new_device_name, new_device_spec)

    try:
      eager_context.device_name = new_device_name
      eager_context.device_spec = new_device_spec
      yield
    finally:
      eager_context.device_name = old_device_name
      eager_context.device_spec = old_device_spec

  def devices(self):
    """List of the names of devices available to execute operations."""
    return self._devices

  def num_gpus(self):
    """The number of GPUs available to execute operations."""
    # TODO(ashankar): Use TF_DeviceListType to count GPU devices.
    return len(self._devices) - 1

  def add_function_def(self, fdef):
    """Add a function definition to the context.

    Once added, the function (identified by its name) can be executed like any
    other operation.

    Args:
      fdef: A FunctionDef protocol buffer message.
    """
    fdef_string = fdef.SerializeToString()
    with errors.raise_exception_on_not_ok_status() as status:
      pywrap_tensorflow.TFE_ContextAddFunctionDef(
          self._handle,  # pylint: disable=protected-access
          fdef_string,
          len(fdef_string),
          status)

  def add_post_execution_callback(self, callback):
    """Add a post-execution callback to the context.

    A post-execution callback is invoked immediately after an eager operation or
    function has finished execution, providing access to the op's type, name
    input and output tensors. Multiple execution callbacks can be added, in
    which case the callbacks will be invoked in the order in which they are
    added.

    Args:
      callback: a callable of the signature
      `f(op_type, op_name, attrs, inputs, outputs)`.
      `op_type` is the type of the operation that was just executed (e.g.,
        `MatMul`).
      `op_name` is the name of the operation that has was just executed. This
        name is set by the client who created the operation and can be `None` if
        it is unset.
      `attrs` contains the attributes of the operation as a `tuple` of
        alternating attribute names and attribute values.
      `inputs` is the `list` of input `Tensor`(s) to the op.
      `outputs` is the `list` of output `Tensor`(s) from the op.
       Return value(s) from the callback are ignored.
    """
    # TODO(cais): (b/64674139) Allow access to function-internal operations.
    self._post_execution_callbacks.append(callback)

  def clear_post_execution_callbacks(self):
    """Clear all post-execution callbacks added to the context."""
    del self._post_execution_callbacks[:]

  @property
  def post_execution_callbacks(self):
    """Get the list of post-execution callbacks added to the context."""
    return self._post_execution_callbacks

_context = None
_context_lock = threading.Lock()


def _initialize_context():
  global _context
  with _context_lock:
    if _context is None:
      _context = Context()


def context():
  """Returns a singleton context object."""
  if _context is None:
    _initialize_context()
  return _context


# TODO(agarwal): remove this.
def get_default_context():
  """Same as context."""
  if _context is None:
    _initialize_context()
  return _context


def in_graph_mode():
  """Returns True if current thread is in GRAPH mode for default context."""
  return context().in_graph_mode()


def in_eager_mode():
  """Returns True if current thread is in EAGER mode for default context."""
  return context().in_eager_mode()


def graph_mode():
  """Context-manager to enable GRAPH mode for current thread."""
  return context()._mode(GRAPH_MODE)  # pylint: disable=protected-access


def eager_mode():
  """Context-manager to enable EAGER mode for current thread."""
  return context()._mode(EAGER_MODE)  # pylint: disable=protected-access


# TODO(agarwal): get rid of this and use ops.name_scope instead.
@contextlib.contextmanager
def namescope(name):
  """ContextManager for creating hierarchical name scopes."""
  ctx = context()
  old_name = ctx.scope_name
  ctx.scope_name = "%s/%s" % (old_name, name) if old_name else name
  try:
    yield
  finally:
    ctx.scope_name = old_name


def scope_name():
  """Name of the current scope."""
  return context().scope_name


def device(name):
  """Context-manager to force placement of operations and Tensors on a device.

  Example:
  ```python
  with tfe.device('gpu:0'):
    with tfe.device('cpu:0'):
      shape = tf.constant([], dtype=tf.int32)
    x = tf.truncated_normal(shape, tf.float32)
  ```
  will ensure that the `shape` Tensor is on CPU but the `truncated_normal`
  operation runs on GPU 0.

  Args:
    name: Name of the device (see context().devices()), or None to
      perform automatic placement.

  Returns:
    Context manager for setting the device.
  """
  return context().device(name)


def run(main=None, argv=None):
  """Runs the program with an optional main function and argv list.

  The program will run with eager execution enabled.

  Example:
  ```python
  import tensorflow as tf
  # Import subject to future changes:
  from tensorflow.contrib.eager.python import tfe

  def main(_):
    u = tf.constant(6.0)
    v = tf.constant(7.0)
    print(u * v)

  if __name__ == "__main__":
    tfe.run()
  ```

  Args:
    main: the main function to run.
    argv: the arguments to pass to it.
  """
  enable_eager_execution()
  app.run(main, argv)


# TODO(apassos): This should not be a part of the public API.
def enable_eager_execution():
  """Enables, for the rest of the lifetime of this program, eager execution.

  If not called immediately on startup risks creating breakage and bugs. Calling
  this method more than once in the same process will lead to an exception.

  Example:
  ```python
  # Before eager execution is enabled, `Tensor`s are symbolic and do not hold
  # concrete values (they are to be executed in a `tf.Session`).
  assert not hasattr(tf.multiply(6, 7), "numpy")

  tfe.enable_eager_execution()

  # After eager execution is enabled, operations are executed as they are
  # defined and `Tensor`s hold concrete values, which can be accessed as
  # `numpy.ndarray`s through the `numpy()` method.
  assert tf.multiply(6, 7).numpy() == 42
  ```

  Raises:
    ValueError: If this method has already been invoked in the current process.
  """
  global _default_mode
  if _default_mode == EAGER_MODE:
    func_name = (
        "tfe." + tf_inspect.getframeinfo(tf_inspect.currentframe()).function)
    raise ValueError(
        "Do not call %s more than once in the same process. Note eager-mode "
        "methods such as tfe.run() also call %s." % (func_name, func_name))
  _default_mode = EAGER_MODE


def list_devices():
  """List the names of the available devices.

  Returns:
    Names of the available devices, as a `list`.
  """
  return context().devices()


def num_gpus():
  """Get the number of available GPU devices.

  Returns:
    The number of available GPU devices.
  """
  return context().num_gpus()
