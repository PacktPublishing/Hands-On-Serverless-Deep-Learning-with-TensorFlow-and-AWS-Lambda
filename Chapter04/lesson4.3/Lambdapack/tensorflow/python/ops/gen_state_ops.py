"""Python wrappers around TensorFlow ops.

This file is MACHINE GENERATED! Do not edit.
Original C++ source file: state_ops.cc
"""

import collections as _collections

from tensorflow.python.eager import execute as _execute
from tensorflow.python.eager import context as _context
from tensorflow.python.eager import core as _core
from tensorflow.python.framework import dtypes as _dtypes
from tensorflow.python.framework import tensor_shape as _tensor_shape

from tensorflow.core.framework import op_def_pb2 as _op_def_pb2
# Needed to trigger the call to _set_call_cpp_shape_fn.
from tensorflow.python.framework import common_shapes as _common_shapes
from tensorflow.python.framework import op_def_registry as _op_def_registry
from tensorflow.python.framework import ops as _ops
from tensorflow.python.framework import op_def_library as _op_def_library


def assign(ref, value, validate_shape=True, use_locking=True, name=None):
  r"""Update 'ref' by assigning 'value' to it.

  This operation outputs "ref" after the assignment is done.
  This makes it easier to chain operations that need to use the reset value.

  Args:
    ref: A mutable `Tensor`.
      Should be from a `Variable` node. May be uninitialized.
    value: A `Tensor`. Must have the same type as `ref`.
      The value to be assigned to the variable.
    validate_shape: An optional `bool`. Defaults to `True`.
      If true, the operation will validate that the shape
      of 'value' matches the shape of the Tensor being assigned to.  If false,
      'ref' will take on the shape of 'value'.
    use_locking: An optional `bool`. Defaults to `True`.
      If True, the assignment will be protected by a lock;
      otherwise the behavior is undefined, but may exhibit less contention.
    name: A name for the operation (optional).

  Returns:
    Same as "ref".  Returned as a convenience for operations that want
    to use the new value after the variable has been reset.
  """
  if validate_shape is None:
    validate_shape = True
  validate_shape = _execute.make_bool(validate_shape, "validate_shape")
  if use_locking is None:
    use_locking = True
  use_locking = _execute.make_bool(use_locking, "use_locking")
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "Assign", ref=ref, value=value, validate_shape=validate_shape,
        use_locking=use_locking, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("T", _op.get_attr("T"), "validate_shape",
              _op.get_attr("validate_shape"), "use_locking",
              _op.get_attr("use_locking"))
  else:
    raise RuntimeError(
        "assign op does not support eager execution. Arg 'output_ref'' is a ref.")
  _execute.record_gradient(
      "Assign", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result


def assign_add(ref, value, use_locking=False, name=None):
  r"""Update 'ref' by adding 'value' to it.

  This operation outputs "ref" after the update is done.
  This makes it easier to chain operations that need to use the reset value.

  Args:
    ref: A mutable `Tensor`. Must be one of the following types: `float32`, `float64`, `int64`, `int32`, `uint8`, `uint16`, `int16`, `int8`, `complex64`, `complex128`, `qint8`, `quint8`, `qint32`, `half`.
      Should be from a `Variable` node.
    value: A `Tensor`. Must have the same type as `ref`.
      The value to be added to the variable.
    use_locking: An optional `bool`. Defaults to `False`.
      If True, the addition will be protected by a lock;
      otherwise the behavior is undefined, but may exhibit less contention.
    name: A name for the operation (optional).

  Returns:
    Same as "ref".  Returned as a convenience for operations that want
    to use the new value after the variable has been updated.
  """
  if use_locking is None:
    use_locking = False
  use_locking = _execute.make_bool(use_locking, "use_locking")
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "AssignAdd", ref=ref, value=value, use_locking=use_locking, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("T", _op.get_attr("T"), "use_locking",
              _op.get_attr("use_locking"))
  else:
    raise RuntimeError(
        "assign_add op does not support eager execution. Arg 'output_ref'' is a ref.")
  _execute.record_gradient(
      "AssignAdd", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result


def assign_sub(ref, value, use_locking=False, name=None):
  r"""Update 'ref' by subtracting 'value' from it.

  This operation outputs "ref" after the update is done.
  This makes it easier to chain operations that need to use the reset value.

  Args:
    ref: A mutable `Tensor`. Must be one of the following types: `float32`, `float64`, `int64`, `int32`, `uint8`, `uint16`, `int16`, `int8`, `complex64`, `complex128`, `qint8`, `quint8`, `qint32`, `half`.
      Should be from a `Variable` node.
    value: A `Tensor`. Must have the same type as `ref`.
      The value to be subtracted to the variable.
    use_locking: An optional `bool`. Defaults to `False`.
      If True, the subtraction will be protected by a lock;
      otherwise the behavior is undefined, but may exhibit less contention.
    name: A name for the operation (optional).

  Returns:
    Same as "ref".  Returned as a convenience for operations that want
    to use the new value after the variable has been updated.
  """
  if use_locking is None:
    use_locking = False
  use_locking = _execute.make_bool(use_locking, "use_locking")
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "AssignSub", ref=ref, value=value, use_locking=use_locking, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("T", _op.get_attr("T"), "use_locking",
              _op.get_attr("use_locking"))
  else:
    raise RuntimeError(
        "assign_sub op does not support eager execution. Arg 'output_ref'' is a ref.")
  _execute.record_gradient(
      "AssignSub", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result


def count_up_to(ref, limit, name=None):
  r"""Increments 'ref' until it reaches 'limit'.

  Args:
    ref: A mutable `Tensor`. Must be one of the following types: `int32`, `int64`.
      Should be from a scalar `Variable` node.
    limit: An `int`.
      If incrementing ref would bring it above limit, instead generates an
      'OutOfRange' error.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `ref`.
    A copy of the input before increment. If nothing else modifies the
    input, the values produced will all be distinct.
  """
  limit = _execute.make_int(limit, "limit")
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "CountUpTo", ref=ref, limit=limit, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("limit", _op.get_attr("limit"), "T", _op.get_attr("T"))
  else:
    raise RuntimeError(
        "count_up_to op does not support eager execution. Arg 'ref'' is a ref.")
  _execute.record_gradient(
      "CountUpTo", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result


def _destroy_temporary_variable(ref, var_name, name=None):
  r"""Destroys the temporary variable and returns its final value.

  Sets output to the value of the Tensor pointed to by 'ref', then destroys
  the temporary variable called 'var_name'.
  All other uses of 'ref' *must* have executed before this op.
  This is typically achieved by chaining the ref through each assign op, or by
  using control dependencies.

  Outputs the final value of the tensor pointed to by 'ref'.

  Args:
    ref: A mutable `Tensor`. A reference to the temporary variable tensor.
    var_name: A `string`.
      Name of the temporary variable, usually the name of the matching
      'TemporaryVariable' op.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `ref`.
  """
  var_name = _execute.make_str(var_name, "var_name")
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "DestroyTemporaryVariable", ref=ref, var_name=var_name, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("T", _op.get_attr("T"), "var_name", _op.get_attr("var_name"))
  else:
    raise RuntimeError(
        "destroy_temporary_variable op does not support eager execution. Arg 'ref'' is a ref.")
  _execute.record_gradient(
      "DestroyTemporaryVariable", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result


def is_variable_initialized(ref, name=None):
  r"""Checks whether a tensor has been initialized.

  Outputs boolean scalar indicating whether the tensor has been initialized.

  Args:
    ref: A mutable `Tensor`.
      Should be from a `Variable` node. May be uninitialized.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `bool`.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "IsVariableInitialized", ref=ref, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("dtype", _op.get_attr("dtype"))
  else:
    raise RuntimeError(
        "is_variable_initialized op does not support eager execution. Arg 'ref'' is a ref.")
  _execute.record_gradient(
      "IsVariableInitialized", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result


def scatter_add(ref, indices, updates, use_locking=False, name=None):
  r"""Adds sparse updates to a variable reference.

  This operation computes

      # Scalar indices
      ref[indices, ...] += updates[...]

      # Vector indices (for each i)
      ref[indices[i], ...] += updates[i, ...]

      # High rank indices (for each i, ..., j)
      ref[indices[i, ..., j], ...] += updates[i, ..., j, ...]

  This operation outputs `ref` after the update is done.
  This makes it easier to chain operations that need to use the reset value.

  Duplicate entries are handled correctly: if multiple `indices` reference
  the same location, their contributions add.

  Requires `updates.shape = indices.shape + ref.shape[1:]`.

  <div style="width:70%; margin:auto; margin-bottom:10px; margin-top:20px;">
  <img style="width:100%" src="https://www.tensorflow.org/images/ScatterAdd.png" alt>
  </div>

  Args:
    ref: A mutable `Tensor`. Must be one of the following types: `float32`, `float64`, `int64`, `int32`, `uint8`, `uint16`, `int16`, `int8`, `complex64`, `complex128`, `qint8`, `quint8`, `qint32`, `half`.
      Should be from a `Variable` node.
    indices: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      A tensor of indices into the first dimension of `ref`.
    updates: A `Tensor`. Must have the same type as `ref`.
      A tensor of updated values to add to `ref`.
    use_locking: An optional `bool`. Defaults to `False`.
      If True, the addition will be protected by a lock;
      otherwise the behavior is undefined, but may exhibit less contention.
    name: A name for the operation (optional).

  Returns:
    Same as `ref`.  Returned as a convenience for operations that want
    to use the updated values after the update is done.
  """
  if use_locking is None:
    use_locking = False
  use_locking = _execute.make_bool(use_locking, "use_locking")
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "ScatterAdd", ref=ref, indices=indices, updates=updates,
        use_locking=use_locking, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("T", _op.get_attr("T"), "Tindices", _op.get_attr("Tindices"),
              "use_locking", _op.get_attr("use_locking"))
  else:
    raise RuntimeError(
        "scatter_add op does not support eager execution. Arg 'output_ref'' is a ref.")
  _execute.record_gradient(
      "ScatterAdd", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result


def scatter_div(ref, indices, updates, use_locking=False, name=None):
  r"""Divides a variable reference by sparse updates.

  This operation computes

  ```python
      # Scalar indices
      ref[indices, ...] /= updates[...]

      # Vector indices (for each i)
      ref[indices[i], ...] /= updates[i, ...]

      # High rank indices (for each i, ..., j)
      ref[indices[i, ..., j], ...] /= updates[i, ..., j, ...]
  ```

  This operation outputs `ref` after the update is done.
  This makes it easier to chain operations that need to use the reset value.

  Duplicate entries are handled correctly: if multiple `indices` reference
  the same location, their contributions divide.

  Requires `updates.shape = indices.shape + ref.shape[1:]`.

  Args:
    ref: A mutable `Tensor`. Must be one of the following types: `float32`, `float64`, `int64`, `int32`, `uint8`, `uint16`, `int16`, `int8`, `complex64`, `complex128`, `qint8`, `quint8`, `qint32`, `half`.
      Should be from a `Variable` node.
    indices: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      A tensor of indices into the first dimension of `ref`.
    updates: A `Tensor`. Must have the same type as `ref`.
      A tensor of values that `ref` is divided by.
    use_locking: An optional `bool`. Defaults to `False`.
      If True, the operation will be protected by a lock;
      otherwise the behavior is undefined, but may exhibit less contention.
    name: A name for the operation (optional).

  Returns:
    Same as `ref`.  Returned as a convenience for operations that want
    to use the updated values after the update is done.
  """
  if use_locking is None:
    use_locking = False
  use_locking = _execute.make_bool(use_locking, "use_locking")
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "ScatterDiv", ref=ref, indices=indices, updates=updates,
        use_locking=use_locking, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("T", _op.get_attr("T"), "Tindices", _op.get_attr("Tindices"),
              "use_locking", _op.get_attr("use_locking"))
  else:
    raise RuntimeError(
        "scatter_div op does not support eager execution. Arg 'output_ref'' is a ref.")
  _execute.record_gradient(
      "ScatterDiv", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result


def scatter_mul(ref, indices, updates, use_locking=False, name=None):
  r"""Multiplies sparse updates into a variable reference.

  This operation computes

  ```python
      # Scalar indices
      ref[indices, ...] *= updates[...]

      # Vector indices (for each i)
      ref[indices[i], ...] *= updates[i, ...]

      # High rank indices (for each i, ..., j)
      ref[indices[i, ..., j], ...] *= updates[i, ..., j, ...]
  ```

  This operation outputs `ref` after the update is done.
  This makes it easier to chain operations that need to use the reset value.

  Duplicate entries are handled correctly: if multiple `indices` reference
  the same location, their contributions multiply.

  Requires `updates.shape = indices.shape + ref.shape[1:]`.

  Args:
    ref: A mutable `Tensor`. Must be one of the following types: `float32`, `float64`, `int64`, `int32`, `uint8`, `uint16`, `int16`, `int8`, `complex64`, `complex128`, `qint8`, `quint8`, `qint32`, `half`.
      Should be from a `Variable` node.
    indices: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      A tensor of indices into the first dimension of `ref`.
    updates: A `Tensor`. Must have the same type as `ref`.
      A tensor of updated values to multiply to `ref`.
    use_locking: An optional `bool`. Defaults to `False`.
      If True, the operation will be protected by a lock;
      otherwise the behavior is undefined, but may exhibit less contention.
    name: A name for the operation (optional).

  Returns:
    Same as `ref`.  Returned as a convenience for operations that want
    to use the updated values after the update is done.
  """
  if use_locking is None:
    use_locking = False
  use_locking = _execute.make_bool(use_locking, "use_locking")
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "ScatterMul", ref=ref, indices=indices, updates=updates,
        use_locking=use_locking, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("T", _op.get_attr("T"), "Tindices", _op.get_attr("Tindices"),
              "use_locking", _op.get_attr("use_locking"))
  else:
    raise RuntimeError(
        "scatter_mul op does not support eager execution. Arg 'output_ref'' is a ref.")
  _execute.record_gradient(
      "ScatterMul", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result


def scatter_nd_add(ref, indices, updates, use_locking=False, name=None):
  r"""Applies sparse addition between `updates` and individual values or slices

  within a given variable according to `indices`.

  `ref` is a `Tensor` with rank `P` and `indices` is a `Tensor` of rank `Q`.

  `indices` must be integer tensor, containing indices into `ref`.
  It must be shape `[d_0, ..., d_{Q-2}, K]` where `0 < K <= P`.

  The innermost dimension of `indices` (with length `K`) corresponds to
  indices into elements (if `K = P`) or slices (if `K < P`) along the `K`th
  dimension of `ref`.

  `updates` is `Tensor` of rank `Q-1+P-K` with shape:

  ```
  [d_0, ..., d_{Q-2}, ref.shape[K], ..., ref.shape[P-1]].
  ```

  For example, say we want to add 4 scattered elements to a rank-1 tensor to 8
  elements. In Python, that addition would look like this:

      ref = tf.Variable([1, 2, 3, 4, 5, 6, 7, 8])
      indices = tf.constant([[4], [3], [1], [7]])
      updates = tf.constant([9, 10, 11, 12])
      add = tf.scatter_nd_add(ref, indices, updates)
      with tf.Session() as sess:
        print sess.run(add)

  The resulting update to ref would look like this:

      [1, 13, 3, 14, 14, 6, 7, 20]

  See @{tf.scatter_nd} for more details about how to make updates to
  slices.

  Args:
    ref: A mutable `Tensor`. Must be one of the following types: `float32`, `float64`, `int64`, `int32`, `uint8`, `uint16`, `int16`, `int8`, `complex64`, `complex128`, `qint8`, `quint8`, `qint32`, `half`.
      A mutable Tensor. Should be from a Variable node.
    indices: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      A Tensor. Must be one of the following types: int32, int64.
      A tensor of indices into ref.
    updates: A `Tensor`. Must have the same type as `ref`.
      A Tensor. Must have the same type as ref. A tensor of updated values
      to add to ref.
    use_locking: An optional `bool`. Defaults to `False`.
      An optional bool. Defaults to True. If True, the assignment will
      be protected by a lock; otherwise the behavior is undefined,
      but may exhibit less contention.
    name: A name for the operation (optional).

  Returns:
    A mutable `Tensor`. Has the same type as `ref`.
    Same as ref. Returned as a convenience for operations that want
    to use the updated values after the update is done.
  """
  if use_locking is None:
    use_locking = False
  use_locking = _execute.make_bool(use_locking, "use_locking")
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "ScatterNdAdd", ref=ref, indices=indices, updates=updates,
        use_locking=use_locking, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("T", _op.get_attr("T"), "Tindices", _op.get_attr("Tindices"),
              "use_locking", _op.get_attr("use_locking"))
  else:
    raise RuntimeError(
        "scatter_nd_add op does not support eager execution. Arg 'output_ref'' is a ref.")
  _execute.record_gradient(
      "ScatterNdAdd", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result


def scatter_nd_sub(ref, indices, updates, use_locking=False, name=None):
  r"""Applies sparse subtraction between `updates` and individual values or slices

  within a given variable according to `indices`.

  `ref` is a `Tensor` with rank `P` and `indices` is a `Tensor` of rank `Q`.

  `indices` must be integer tensor, containing indices into `ref`.
  It must be shape `[d_0, ..., d_{Q-2}, K]` where `0 < K <= P`.

  The innermost dimension of `indices` (with length `K`) corresponds to
  indices into elements (if `K = P`) or slices (if `K < P`) along the `K`th
  dimension of `ref`.

  `updates` is `Tensor` of rank `Q-1+P-K` with shape:

  ```
  [d_0, ..., d_{Q-2}, ref.shape[K], ..., ref.shape[P-1]].
  ```

  For example, say we want to subtract 4 scattered elements from a rank-1 tensor
  with 8 elements. In Python, that subtraction would look like this:

      ref = tf.Variable([1, 2, 3, 4, 5, 6, 7, 8])
      indices = tf.constant([[4], [3], [1], [7]])
      updates = tf.constant([9, 10, 11, 12])
      sub = tf.scatter_nd_sub(ref, indices, updates)
      with tf.Session() as sess:
        print sess.run(sub)

  The resulting update to ref would look like this:

      [1, -9, 3, -6, -4, 6, 7, -4]

  See @{tf.scatter_nd} for more details about how to make updates to
  slices.

  Args:
    ref: A mutable `Tensor`. Must be one of the following types: `float32`, `float64`, `int64`, `int32`, `uint8`, `uint16`, `int16`, `int8`, `complex64`, `complex128`, `qint8`, `quint8`, `qint32`, `half`.
      A mutable Tensor. Should be from a Variable node.
    indices: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      A Tensor. Must be one of the following types: int32, int64.
      A tensor of indices into ref.
    updates: A `Tensor`. Must have the same type as `ref`.
      A Tensor. Must have the same type as ref. A tensor of updated values
      to subtract from ref.
    use_locking: An optional `bool`. Defaults to `False`.
      An optional bool. Defaults to True. If True, the assignment will
      be protected by a lock; otherwise the behavior is undefined,
      but may exhibit less contention.
    name: A name for the operation (optional).

  Returns:
    A mutable `Tensor`. Has the same type as `ref`.
    Same as ref. Returned as a convenience for operations that want
    to use the updated values after the update is done.
  """
  if use_locking is None:
    use_locking = False
  use_locking = _execute.make_bool(use_locking, "use_locking")
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "ScatterNdSub", ref=ref, indices=indices, updates=updates,
        use_locking=use_locking, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("T", _op.get_attr("T"), "Tindices", _op.get_attr("Tindices"),
              "use_locking", _op.get_attr("use_locking"))
  else:
    raise RuntimeError(
        "scatter_nd_sub op does not support eager execution. Arg 'output_ref'' is a ref.")
  _execute.record_gradient(
      "ScatterNdSub", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result


def scatter_nd_update(ref, indices, updates, use_locking=True, name=None):
  r"""Applies sparse `updates` to individual values or slices within a given

  variable according to `indices`.

  `ref` is a `Tensor` with rank `P` and `indices` is a `Tensor` of rank `Q`.

  `indices` must be integer tensor, containing indices into `ref`.
  It must be shape `[d_0, ..., d_{Q-2}, K]` where `0 < K <= P`.

  The innermost dimension of `indices` (with length `K`) corresponds to
  indices into elements (if `K = P`) or slices (if `K < P`) along the `K`th
  dimension of `ref`.

  `updates` is `Tensor` of rank `Q-1+P-K` with shape:

  ```
  [d_0, ..., d_{Q-2}, ref.shape[K], ..., ref.shape[P-1]].
  ```

  For example, say we want to update 4 scattered elements to a rank-1 tensor to
  8 elements. In Python, that update would look like this:

  ```python
      ref = tf.Variable([1, 2, 3, 4, 5, 6, 7, 8])
      indices = tf.constant([[4], [3], [1] ,[7]])
      updates = tf.constant([9, 10, 11, 12])
      update = tf.scatter_nd_update(ref, indices, updates)
      with tf.Session() as sess:
        print sess.run(update)
  ```

  The resulting update to ref would look like this:

      [1, 11, 3, 10, 9, 6, 7, 12]

  See @{tf.scatter_nd} for more details about how to make updates to
  slices.

  Args:
    ref: A mutable `Tensor`. A mutable Tensor. Should be from a Variable node.
    indices: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      A Tensor. Must be one of the following types: int32, int64.
      A tensor of indices into ref.
    updates: A `Tensor`. Must have the same type as `ref`.
      A Tensor. Must have the same type as ref. A tensor of updated
      values to add to ref.
    use_locking: An optional `bool`. Defaults to `True`.
      An optional bool. Defaults to True. If True, the assignment will
      be protected by a lock; otherwise the behavior is undefined,
      but may exhibit less contention.
    name: A name for the operation (optional).

  Returns:
    A mutable `Tensor`. Has the same type as `ref`.
    Same as ref. Returned as a convenience for operations that want to
    use the updated values after the update is done.
  """
  if use_locking is None:
    use_locking = True
  use_locking = _execute.make_bool(use_locking, "use_locking")
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "ScatterNdUpdate", ref=ref, indices=indices, updates=updates,
        use_locking=use_locking, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("T", _op.get_attr("T"), "Tindices", _op.get_attr("Tindices"),
              "use_locking", _op.get_attr("use_locking"))
  else:
    raise RuntimeError(
        "scatter_nd_update op does not support eager execution. Arg 'output_ref'' is a ref.")
  _execute.record_gradient(
      "ScatterNdUpdate", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result


def scatter_sub(ref, indices, updates, use_locking=False, name=None):
  r"""Subtracts sparse updates to a variable reference.

  ```python
      # Scalar indices
      ref[indices, ...] -= updates[...]

      # Vector indices (for each i)
      ref[indices[i], ...] -= updates[i, ...]

      # High rank indices (for each i, ..., j)
      ref[indices[i, ..., j], ...] -= updates[i, ..., j, ...]
  ```

  This operation outputs `ref` after the update is done.
  This makes it easier to chain operations that need to use the reset value.

  Duplicate entries are handled correctly: if multiple `indices` reference
  the same location, their (negated) contributions add.

  Requires `updates.shape = indices.shape + ref.shape[1:]`.

  <div style="width:70%; margin:auto; margin-bottom:10px; margin-top:20px;">
  <img style="width:100%" src="https://www.tensorflow.org/images/ScatterSub.png" alt>
  </div>

  Args:
    ref: A mutable `Tensor`. Must be one of the following types: `float32`, `float64`, `int64`, `int32`, `uint8`, `uint16`, `int16`, `int8`, `complex64`, `complex128`, `qint8`, `quint8`, `qint32`, `half`.
      Should be from a `Variable` node.
    indices: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      A tensor of indices into the first dimension of `ref`.
    updates: A `Tensor`. Must have the same type as `ref`.
      A tensor of updated values to subtract from `ref`.
    use_locking: An optional `bool`. Defaults to `False`.
      If True, the subtraction will be protected by a lock;
      otherwise the behavior is undefined, but may exhibit less contention.
    name: A name for the operation (optional).

  Returns:
    Same as `ref`.  Returned as a convenience for operations that want
    to use the updated values after the update is done.
  """
  if use_locking is None:
    use_locking = False
  use_locking = _execute.make_bool(use_locking, "use_locking")
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "ScatterSub", ref=ref, indices=indices, updates=updates,
        use_locking=use_locking, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("T", _op.get_attr("T"), "Tindices", _op.get_attr("Tindices"),
              "use_locking", _op.get_attr("use_locking"))
  else:
    raise RuntimeError(
        "scatter_sub op does not support eager execution. Arg 'output_ref'' is a ref.")
  _execute.record_gradient(
      "ScatterSub", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result


def scatter_update(ref, indices, updates, use_locking=True, name=None):
  r"""Applies sparse updates to a variable reference.

  This operation computes

  ```python
      # Scalar indices
      ref[indices, ...] = updates[...]

      # Vector indices (for each i)
      ref[indices[i], ...] = updates[i, ...]

      # High rank indices (for each i, ..., j)
      ref[indices[i, ..., j], ...] = updates[i, ..., j, ...]
  ```

  This operation outputs `ref` after the update is done.
  This makes it easier to chain operations that need to use the reset value.

  If values in `ref` is to be updated more than once, because there are
  duplicate entries in `indices`, the order at which the updates happen
  for each value is undefined.

  Requires `updates.shape = indices.shape + ref.shape[1:]`.

  <div style="width:70%; margin:auto; margin-bottom:10px; margin-top:20px;">
  <img style="width:100%" src="https://www.tensorflow.org/images/ScatterUpdate.png" alt>
  </div>

  Args:
    ref: A mutable `Tensor`. Should be from a `Variable` node.
    indices: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      A tensor of indices into the first dimension of `ref`.
    updates: A `Tensor`. Must have the same type as `ref`.
      A tensor of updated values to store in `ref`.
    use_locking: An optional `bool`. Defaults to `True`.
      If True, the assignment will be protected by a lock;
      otherwise the behavior is undefined, but may exhibit less contention.
    name: A name for the operation (optional).

  Returns:
    Same as `ref`.  Returned as a convenience for operations that want
    to use the updated values after the update is done.
  """
  if use_locking is None:
    use_locking = True
  use_locking = _execute.make_bool(use_locking, "use_locking")
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "ScatterUpdate", ref=ref, indices=indices, updates=updates,
        use_locking=use_locking, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("T", _op.get_attr("T"), "Tindices", _op.get_attr("Tindices"),
              "use_locking", _op.get_attr("use_locking"))
  else:
    raise RuntimeError(
        "scatter_update op does not support eager execution. Arg 'output_ref'' is a ref.")
  _execute.record_gradient(
      "ScatterUpdate", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result


def _temporary_variable(shape, dtype, var_name="", name=None):
  r"""Returns a tensor that may be mutated, but only persists within a single step.

  This is an experimental op for internal use only and it is possible to use this
  op in unsafe ways.  DO NOT USE unless you fully understand the risks.

  It is the caller's responsibility to ensure that 'ref' is eventually passed to a
  matching 'DestroyTemporaryVariable' op after all other uses have completed.

  Outputs a ref to the tensor state so it may be read or modified.

    E.g.
        var = state_ops._temporary_variable([1, 2], types.float_)
        var_name = var.op.name
        var = state_ops.assign(var, [[4.0, 5.0]])
        var = state_ops.assign_add(var, [[6.0, 7.0]])
        final = state_ops._destroy_temporary_variable(var, var_name=var_name)

  Args:
    shape: A `tf.TensorShape` or list of `ints`.
      The shape of the variable tensor.
    dtype: A `tf.DType`. The type of elements in the variable tensor.
    var_name: An optional `string`. Defaults to `""`.
      Overrides the name used for the temporary variable resource. Default
      value is the name of the 'TemporaryVariable' op (which is guaranteed unique).
    name: A name for the operation (optional).

  Returns:
    A mutable `Tensor` of type `dtype`. A reference to the variable tensor.
  """
  shape = _execute.make_shape(shape, "shape")
  dtype = _execute.make_type(dtype, "dtype")
  if var_name is None:
    var_name = ""
  var_name = _execute.make_str(var_name, "var_name")
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "TemporaryVariable", shape=shape, dtype=dtype, var_name=var_name,
        name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("shape", _op.get_attr("shape"), "dtype", _op.get_attr("dtype"),
              "var_name", _op.get_attr("var_name"))
  else:
    raise RuntimeError(
        "temporary_variable op does not support eager execution. Arg 'ref'' is a ref.")
  _execute.record_gradient(
      "TemporaryVariable", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result


def _variable(shape, dtype, container="", shared_name="", name=None):
  r"""Use VariableV2 instead.

  Args:
    shape: A `tf.TensorShape` or list of `ints`.
    dtype: A `tf.DType`.
    container: An optional `string`. Defaults to `""`.
    shared_name: An optional `string`. Defaults to `""`.
    name: A name for the operation (optional).

  Returns:
    A mutable `Tensor` of type `dtype`.
  """
  shape = _execute.make_shape(shape, "shape")
  dtype = _execute.make_type(dtype, "dtype")
  if container is None:
    container = ""
  container = _execute.make_str(container, "container")
  if shared_name is None:
    shared_name = ""
  shared_name = _execute.make_str(shared_name, "shared_name")
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "Variable", shape=shape, dtype=dtype, container=container,
        shared_name=shared_name, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("shape", _op.get_attr("shape"), "dtype", _op.get_attr("dtype"),
              "container", _op.get_attr("container"), "shared_name",
              _op.get_attr("shared_name"))
  else:
    raise RuntimeError(
        "variable op does not support eager execution. Arg 'ref'' is a ref.")
  _execute.record_gradient(
      "Variable", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result


def _variable_v2(shape, dtype, container="", shared_name="", name=None):
  r"""Holds state in the form of a tensor that persists across steps.

  Outputs a ref to the tensor state so it may be read or modified.
  TODO(zhifengc/mrry): Adds a pointer to a more detail document
  about sharing states in tensorflow.

  Args:
    shape: A `tf.TensorShape` or list of `ints`.
      The shape of the variable tensor.
    dtype: A `tf.DType`. The type of elements in the variable tensor.
    container: An optional `string`. Defaults to `""`.
      If non-empty, this variable is placed in the given container.
      Otherwise, a default container is used.
    shared_name: An optional `string`. Defaults to `""`.
      If non-empty, this variable is named in the given bucket
      with this shared_name. Otherwise, the node name is used instead.
    name: A name for the operation (optional).

  Returns:
    A mutable `Tensor` of type `dtype`. A reference to the variable tensor.
  """
  shape = _execute.make_shape(shape, "shape")
  dtype = _execute.make_type(dtype, "dtype")
  if container is None:
    container = ""
  container = _execute.make_str(container, "container")
  if shared_name is None:
    shared_name = ""
  shared_name = _execute.make_str(shared_name, "shared_name")
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "VariableV2", shape=shape, dtype=dtype, container=container,
        shared_name=shared_name, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("shape", _op.get_attr("shape"), "dtype", _op.get_attr("dtype"),
              "container", _op.get_attr("container"), "shared_name",
              _op.get_attr("shared_name"))
  else:
    raise RuntimeError(
        "variable_v2 op does not support eager execution. Arg 'ref'' is a ref.")
  _execute.record_gradient(
      "VariableV2", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result

def _InitOpDefLibrary(op_list_proto_bytes):
  op_list = _op_def_pb2.OpList()
  op_list.ParseFromString(op_list_proto_bytes)
  _op_def_registry.register_op_list(op_list)
  op_def_lib = _op_def_library.OpDefLibrary()
  op_def_lib.add_op_list(op_list)
  return op_def_lib
# op {
#   name: "Assign"
#   input_arg {
#     name: "ref"
#     type_attr: "T"
#     is_ref: true
#   }
#   input_arg {
#     name: "value"
#     type_attr: "T"
#   }
#   output_arg {
#     name: "output_ref"
#     type_attr: "T"
#     is_ref: true
#   }
#   attr {
#     name: "T"
#     type: "type"
#   }
#   attr {
#     name: "validate_shape"
#     type: "bool"
#     default_value {
#       b: true
#     }
#   }
#   attr {
#     name: "use_locking"
#     type: "bool"
#     default_value {
#       b: true
#     }
#   }
#   allows_uninitialized_input: true
# }
# op {
#   name: "AssignAdd"
#   input_arg {
#     name: "ref"
#     type_attr: "T"
#     is_ref: true
#   }
#   input_arg {
#     name: "value"
#     type_attr: "T"
#   }
#   output_arg {
#     name: "output_ref"
#     type_attr: "T"
#     is_ref: true
#   }
#   attr {
#     name: "T"
#     type: "type"
#     allowed_values {
#       list {
#         type: DT_FLOAT
#         type: DT_DOUBLE
#         type: DT_INT64
#         type: DT_INT32
#         type: DT_UINT8
#         type: DT_UINT16
#         type: DT_INT16
#         type: DT_INT8
#         type: DT_COMPLEX64
#         type: DT_COMPLEX128
#         type: DT_QINT8
#         type: DT_QUINT8
#         type: DT_QINT32
#         type: DT_HALF
#       }
#     }
#   }
#   attr {
#     name: "use_locking"
#     type: "bool"
#     default_value {
#       b: false
#     }
#   }
# }
# op {
#   name: "AssignSub"
#   input_arg {
#     name: "ref"
#     type_attr: "T"
#     is_ref: true
#   }
#   input_arg {
#     name: "value"
#     type_attr: "T"
#   }
#   output_arg {
#     name: "output_ref"
#     type_attr: "T"
#     is_ref: true
#   }
#   attr {
#     name: "T"
#     type: "type"
#     allowed_values {
#       list {
#         type: DT_FLOAT
#         type: DT_DOUBLE
#         type: DT_INT64
#         type: DT_INT32
#         type: DT_UINT8
#         type: DT_UINT16
#         type: DT_INT16
#         type: DT_INT8
#         type: DT_COMPLEX64
#         type: DT_COMPLEX128
#         type: DT_QINT8
#         type: DT_QUINT8
#         type: DT_QINT32
#         type: DT_HALF
#       }
#     }
#   }
#   attr {
#     name: "use_locking"
#     type: "bool"
#     default_value {
#       b: false
#     }
#   }
# }
# op {
#   name: "CountUpTo"
#   input_arg {
#     name: "ref"
#     type_attr: "T"
#     is_ref: true
#   }
#   output_arg {
#     name: "output"
#     type_attr: "T"
#   }
#   attr {
#     name: "limit"
#     type: "int"
#   }
#   attr {
#     name: "T"
#     type: "type"
#     allowed_values {
#       list {
#         type: DT_INT32
#         type: DT_INT64
#       }
#     }
#   }
# }
# op {
#   name: "DestroyTemporaryVariable"
#   input_arg {
#     name: "ref"
#     type_attr: "T"
#     is_ref: true
#   }
#   output_arg {
#     name: "value"
#     type_attr: "T"
#   }
#   attr {
#     name: "T"
#     type: "type"
#   }
#   attr {
#     name: "var_name"
#     type: "string"
#   }
# }
# op {
#   name: "IsVariableInitialized"
#   input_arg {
#     name: "ref"
#     type_attr: "dtype"
#     is_ref: true
#   }
#   output_arg {
#     name: "is_initialized"
#     type: DT_BOOL
#   }
#   attr {
#     name: "dtype"
#     type: "type"
#   }
#   allows_uninitialized_input: true
# }
# op {
#   name: "ScatterAdd"
#   input_arg {
#     name: "ref"
#     type_attr: "T"
#     is_ref: true
#   }
#   input_arg {
#     name: "indices"
#     type_attr: "Tindices"
#   }
#   input_arg {
#     name: "updates"
#     type_attr: "T"
#   }
#   output_arg {
#     name: "output_ref"
#     type_attr: "T"
#     is_ref: true
#   }
#   attr {
#     name: "T"
#     type: "type"
#     allowed_values {
#       list {
#         type: DT_FLOAT
#         type: DT_DOUBLE
#         type: DT_INT64
#         type: DT_INT32
#         type: DT_UINT8
#         type: DT_UINT16
#         type: DT_INT16
#         type: DT_INT8
#         type: DT_COMPLEX64
#         type: DT_COMPLEX128
#         type: DT_QINT8
#         type: DT_QUINT8
#         type: DT_QINT32
#         type: DT_HALF
#       }
#     }
#   }
#   attr {
#     name: "Tindices"
#     type: "type"
#     allowed_values {
#       list {
#         type: DT_INT32
#         type: DT_INT64
#       }
#     }
#   }
#   attr {
#     name: "use_locking"
#     type: "bool"
#     default_value {
#       b: false
#     }
#   }
# }
# op {
#   name: "ScatterDiv"
#   input_arg {
#     name: "ref"
#     type_attr: "T"
#     is_ref: true
#   }
#   input_arg {
#     name: "indices"
#     type_attr: "Tindices"
#   }
#   input_arg {
#     name: "updates"
#     type_attr: "T"
#   }
#   output_arg {
#     name: "output_ref"
#     type_attr: "T"
#     is_ref: true
#   }
#   attr {
#     name: "T"
#     type: "type"
#     allowed_values {
#       list {
#         type: DT_FLOAT
#         type: DT_DOUBLE
#         type: DT_INT64
#         type: DT_INT32
#         type: DT_UINT8
#         type: DT_UINT16
#         type: DT_INT16
#         type: DT_INT8
#         type: DT_COMPLEX64
#         type: DT_COMPLEX128
#         type: DT_QINT8
#         type: DT_QUINT8
#         type: DT_QINT32
#         type: DT_HALF
#       }
#     }
#   }
#   attr {
#     name: "Tindices"
#     type: "type"
#     allowed_values {
#       list {
#         type: DT_INT32
#         type: DT_INT64
#       }
#     }
#   }
#   attr {
#     name: "use_locking"
#     type: "bool"
#     default_value {
#       b: false
#     }
#   }
# }
# op {
#   name: "ScatterMul"
#   input_arg {
#     name: "ref"
#     type_attr: "T"
#     is_ref: true
#   }
#   input_arg {
#     name: "indices"
#     type_attr: "Tindices"
#   }
#   input_arg {
#     name: "updates"
#     type_attr: "T"
#   }
#   output_arg {
#     name: "output_ref"
#     type_attr: "T"
#     is_ref: true
#   }
#   attr {
#     name: "T"
#     type: "type"
#     allowed_values {
#       list {
#         type: DT_FLOAT
#         type: DT_DOUBLE
#         type: DT_INT64
#         type: DT_INT32
#         type: DT_UINT8
#         type: DT_UINT16
#         type: DT_INT16
#         type: DT_INT8
#         type: DT_COMPLEX64
#         type: DT_COMPLEX128
#         type: DT_QINT8
#         type: DT_QUINT8
#         type: DT_QINT32
#         type: DT_HALF
#       }
#     }
#   }
#   attr {
#     name: "Tindices"
#     type: "type"
#     allowed_values {
#       list {
#         type: DT_INT32
#         type: DT_INT64
#       }
#     }
#   }
#   attr {
#     name: "use_locking"
#     type: "bool"
#     default_value {
#       b: false
#     }
#   }
# }
# op {
#   name: "ScatterNdAdd"
#   input_arg {
#     name: "ref"
#     type_attr: "T"
#     is_ref: true
#   }
#   input_arg {
#     name: "indices"
#     type_attr: "Tindices"
#   }
#   input_arg {
#     name: "updates"
#     type_attr: "T"
#   }
#   output_arg {
#     name: "output_ref"
#     type_attr: "T"
#     is_ref: true
#   }
#   attr {
#     name: "T"
#     type: "type"
#     allowed_values {
#       list {
#         type: DT_FLOAT
#         type: DT_DOUBLE
#         type: DT_INT64
#         type: DT_INT32
#         type: DT_UINT8
#         type: DT_UINT16
#         type: DT_INT16
#         type: DT_INT8
#         type: DT_COMPLEX64
#         type: DT_COMPLEX128
#         type: DT_QINT8
#         type: DT_QUINT8
#         type: DT_QINT32
#         type: DT_HALF
#       }
#     }
#   }
#   attr {
#     name: "Tindices"
#     type: "type"
#     allowed_values {
#       list {
#         type: DT_INT32
#         type: DT_INT64
#       }
#     }
#   }
#   attr {
#     name: "use_locking"
#     type: "bool"
#     default_value {
#       b: false
#     }
#   }
# }
# op {
#   name: "ScatterNdSub"
#   input_arg {
#     name: "ref"
#     type_attr: "T"
#     is_ref: true
#   }
#   input_arg {
#     name: "indices"
#     type_attr: "Tindices"
#   }
#   input_arg {
#     name: "updates"
#     type_attr: "T"
#   }
#   output_arg {
#     name: "output_ref"
#     type_attr: "T"
#     is_ref: true
#   }
#   attr {
#     name: "T"
#     type: "type"
#     allowed_values {
#       list {
#         type: DT_FLOAT
#         type: DT_DOUBLE
#         type: DT_INT64
#         type: DT_INT32
#         type: DT_UINT8
#         type: DT_UINT16
#         type: DT_INT16
#         type: DT_INT8
#         type: DT_COMPLEX64
#         type: DT_COMPLEX128
#         type: DT_QINT8
#         type: DT_QUINT8
#         type: DT_QINT32
#         type: DT_HALF
#       }
#     }
#   }
#   attr {
#     name: "Tindices"
#     type: "type"
#     allowed_values {
#       list {
#         type: DT_INT32
#         type: DT_INT64
#       }
#     }
#   }
#   attr {
#     name: "use_locking"
#     type: "bool"
#     default_value {
#       b: false
#     }
#   }
# }
# op {
#   name: "ScatterNdUpdate"
#   input_arg {
#     name: "ref"
#     type_attr: "T"
#     is_ref: true
#   }
#   input_arg {
#     name: "indices"
#     type_attr: "Tindices"
#   }
#   input_arg {
#     name: "updates"
#     type_attr: "T"
#   }
#   output_arg {
#     name: "output_ref"
#     type_attr: "T"
#     is_ref: true
#   }
#   attr {
#     name: "T"
#     type: "type"
#   }
#   attr {
#     name: "Tindices"
#     type: "type"
#     allowed_values {
#       list {
#         type: DT_INT32
#         type: DT_INT64
#       }
#     }
#   }
#   attr {
#     name: "use_locking"
#     type: "bool"
#     default_value {
#       b: true
#     }
#   }
# }
# op {
#   name: "ScatterSub"
#   input_arg {
#     name: "ref"
#     type_attr: "T"
#     is_ref: true
#   }
#   input_arg {
#     name: "indices"
#     type_attr: "Tindices"
#   }
#   input_arg {
#     name: "updates"
#     type_attr: "T"
#   }
#   output_arg {
#     name: "output_ref"
#     type_attr: "T"
#     is_ref: true
#   }
#   attr {
#     name: "T"
#     type: "type"
#     allowed_values {
#       list {
#         type: DT_FLOAT
#         type: DT_DOUBLE
#         type: DT_INT64
#         type: DT_INT32
#         type: DT_UINT8
#         type: DT_UINT16
#         type: DT_INT16
#         type: DT_INT8
#         type: DT_COMPLEX64
#         type: DT_COMPLEX128
#         type: DT_QINT8
#         type: DT_QUINT8
#         type: DT_QINT32
#         type: DT_HALF
#       }
#     }
#   }
#   attr {
#     name: "Tindices"
#     type: "type"
#     allowed_values {
#       list {
#         type: DT_INT32
#         type: DT_INT64
#       }
#     }
#   }
#   attr {
#     name: "use_locking"
#     type: "bool"
#     default_value {
#       b: false
#     }
#   }
# }
# op {
#   name: "ScatterUpdate"
#   input_arg {
#     name: "ref"
#     type_attr: "T"
#     is_ref: true
#   }
#   input_arg {
#     name: "indices"
#     type_attr: "Tindices"
#   }
#   input_arg {
#     name: "updates"
#     type_attr: "T"
#   }
#   output_arg {
#     name: "output_ref"
#     type_attr: "T"
#     is_ref: true
#   }
#   attr {
#     name: "T"
#     type: "type"
#   }
#   attr {
#     name: "Tindices"
#     type: "type"
#     allowed_values {
#       list {
#         type: DT_INT32
#         type: DT_INT64
#       }
#     }
#   }
#   attr {
#     name: "use_locking"
#     type: "bool"
#     default_value {
#       b: true
#     }
#   }
# }
# op {
#   name: "TemporaryVariable"
#   output_arg {
#     name: "ref"
#     type_attr: "dtype"
#     is_ref: true
#   }
#   attr {
#     name: "shape"
#     type: "shape"
#   }
#   attr {
#     name: "dtype"
#     type: "type"
#   }
#   attr {
#     name: "var_name"
#     type: "string"
#     default_value {
#       s: ""
#     }
#   }
#   is_stateful: true
# }
# op {
#   name: "Variable"
#   output_arg {
#     name: "ref"
#     type_attr: "dtype"
#     is_ref: true
#   }
#   attr {
#     name: "shape"
#     type: "shape"
#   }
#   attr {
#     name: "dtype"
#     type: "type"
#   }
#   attr {
#     name: "container"
#     type: "string"
#     default_value {
#       s: ""
#     }
#   }
#   attr {
#     name: "shared_name"
#     type: "string"
#     default_value {
#       s: ""
#     }
#   }
#   is_stateful: true
# }
# op {
#   name: "VariableV2"
#   output_arg {
#     name: "ref"
#     type_attr: "dtype"
#     is_ref: true
#   }
#   attr {
#     name: "shape"
#     type: "shape"
#   }
#   attr {
#     name: "dtype"
#     type: "type"
#   }
#   attr {
#     name: "container"
#     type: "string"
#     default_value {
#       s: ""
#     }
#   }
#   attr {
#     name: "shared_name"
#     type: "string"
#     default_value {
#       s: ""
#     }
#   }
#   is_stateful: true
# }
_op_def_lib = _InitOpDefLibrary(b"\nx\n\006Assign\022\013\n\003ref\"\001T\200\001\001\022\n\n\005value\"\001T\032\022\n\noutput_ref\"\001T\200\001\001\"\t\n\001T\022\004type\"\032\n\016validate_shape\022\004bool\032\002(\001\"\027\n\013use_locking\022\004bool\032\002(\001\230\001\001\np\n\tAssignAdd\022\013\n\003ref\"\001T\200\001\001\022\n\n\005value\"\001T\032\022\n\noutput_ref\"\001T\200\001\001\"\035\n\001T\022\004type:\022\n\0202\016\001\002\t\003\004\021\005\006\010\022\013\014\r\023\"\027\n\013use_locking\022\004bool\032\002(\000\np\n\tAssignSub\022\013\n\003ref\"\001T\200\001\001\022\n\n\005value\"\001T\032\022\n\noutput_ref\"\001T\200\001\001\"\035\n\001T\022\004type:\022\n\0202\016\001\002\t\003\004\021\005\006\010\022\013\014\r\023\"\027\n\013use_locking\022\004bool\032\002(\000\nF\n\tCountUpTo\022\013\n\003ref\"\001T\200\001\001\032\013\n\006output\"\001T\"\014\n\005limit\022\003int\"\021\n\001T\022\004type:\006\n\0042\002\003\t\nR\n\030DestroyTemporaryVariable\022\013\n\003ref\"\001T\200\001\001\032\n\n\005value\"\001T\"\t\n\001T\022\004type\"\022\n\010var_name\022\006string\nN\n\025IsVariableInitialized\022\017\n\003ref\"\005dtype\200\001\001\032\022\n\016is_initialized\030\n\"\r\n\005dtype\022\004type\230\001\001\n\242\001\n\nScatterAdd\022\013\n\003ref\"\001T\200\001\001\022\023\n\007indices\"\010Tindices\022\014\n\007updates\"\001T\032\022\n\noutput_ref\"\001T\200\001\001\"\035\n\001T\022\004type:\022\n\0202\016\001\002\t\003\004\021\005\006\010\022\013\014\r\023\"\030\n\010Tindices\022\004type:\006\n\0042\002\003\t\"\027\n\013use_locking\022\004bool\032\002(\000\n\242\001\n\nScatterDiv\022\013\n\003ref\"\001T\200\001\001\022\023\n\007indices\"\010Tindices\022\014\n\007updates\"\001T\032\022\n\noutput_ref\"\001T\200\001\001\"\035\n\001T\022\004type:\022\n\0202\016\001\002\t\003\004\021\005\006\010\022\013\014\r\023\"\030\n\010Tindices\022\004type:\006\n\0042\002\003\t\"\027\n\013use_locking\022\004bool\032\002(\000\n\242\001\n\nScatterMul\022\013\n\003ref\"\001T\200\001\001\022\023\n\007indices\"\010Tindices\022\014\n\007updates\"\001T\032\022\n\noutput_ref\"\001T\200\001\001\"\035\n\001T\022\004type:\022\n\0202\016\001\002\t\003\004\021\005\006\010\022\013\014\r\023\"\030\n\010Tindices\022\004type:\006\n\0042\002\003\t\"\027\n\013use_locking\022\004bool\032\002(\000\n\244\001\n\014ScatterNdAdd\022\013\n\003ref\"\001T\200\001\001\022\023\n\007indices\"\010Tindices\022\014\n\007updates\"\001T\032\022\n\noutput_ref\"\001T\200\001\001\"\035\n\001T\022\004type:\022\n\0202\016\001\002\t\003\004\021\005\006\010\022\013\014\r\023\"\030\n\010Tindices\022\004type:\006\n\0042\002\003\t\"\027\n\013use_locking\022\004bool\032\002(\000\n\244\001\n\014ScatterNdSub\022\013\n\003ref\"\001T\200\001\001\022\023\n\007indices\"\010Tindices\022\014\n\007updates\"\001T\032\022\n\noutput_ref\"\001T\200\001\001\"\035\n\001T\022\004type:\022\n\0202\016\001\002\t\003\004\021\005\006\010\022\013\014\r\023\"\030\n\010Tindices\022\004type:\006\n\0042\002\003\t\"\027\n\013use_locking\022\004bool\032\002(\000\n\223\001\n\017ScatterNdUpdate\022\013\n\003ref\"\001T\200\001\001\022\023\n\007indices\"\010Tindices\022\014\n\007updates\"\001T\032\022\n\noutput_ref\"\001T\200\001\001\"\t\n\001T\022\004type\"\030\n\010Tindices\022\004type:\006\n\0042\002\003\t\"\027\n\013use_locking\022\004bool\032\002(\001\n\242\001\n\nScatterSub\022\013\n\003ref\"\001T\200\001\001\022\023\n\007indices\"\010Tindices\022\014\n\007updates\"\001T\032\022\n\noutput_ref\"\001T\200\001\001\"\035\n\001T\022\004type:\022\n\0202\016\001\002\t\003\004\021\005\006\010\022\013\014\r\023\"\030\n\010Tindices\022\004type:\006\n\0042\002\003\t\"\027\n\013use_locking\022\004bool\032\002(\000\n\221\001\n\rScatterUpdate\022\013\n\003ref\"\001T\200\001\001\022\023\n\007indices\"\010Tindices\022\014\n\007updates\"\001T\032\022\n\noutput_ref\"\001T\200\001\001\"\t\n\001T\022\004type\"\030\n\010Tindices\022\004type:\006\n\0042\002\003\t\"\027\n\013use_locking\022\004bool\032\002(\001\n^\n\021TemporaryVariable\032\017\n\003ref\"\005dtype\200\001\001\"\016\n\005shape\022\005shape\"\r\n\005dtype\022\004type\"\026\n\010var_name\022\006string\032\002\022\000\210\001\001\nq\n\010Variable\032\017\n\003ref\"\005dtype\200\001\001\"\016\n\005shape\022\005shape\"\r\n\005dtype\022\004type\"\027\n\tcontainer\022\006string\032\002\022\000\"\031\n\013shared_name\022\006string\032\002\022\000\210\001\001\ns\n\nVariableV2\032\017\n\003ref\"\005dtype\200\001\001\"\016\n\005shape\022\005shape\"\r\n\005dtype\022\004type\"\027\n\tcontainer\022\006string\032\002\022\000\"\031\n\013shared_name\022\006string\032\002\022\000\210\001\001")
