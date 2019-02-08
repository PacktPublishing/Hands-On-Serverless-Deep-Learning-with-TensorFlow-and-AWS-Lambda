"""Python wrappers around TensorFlow ops.

This file is MACHINE GENERATED! Do not edit.
Original C++ source file: spectral_ops.cc
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


def _batch_fft(input, name=None):
  r"""TODO: add doc.

  Args:
    input: A `Tensor` of type `complex64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `complex64`.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "BatchFFT", input=input, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = None
  else:
    input = _ops.convert_to_tensor(input, _dtypes.complex64)
    _inputs_flat = [input]
    _attrs = None
    _result = _execute.execute(b"BatchFFT", 1, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "BatchFFT", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result


def _batch_fft2d(input, name=None):
  r"""TODO: add doc.

  Args:
    input: A `Tensor` of type `complex64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `complex64`.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "BatchFFT2D", input=input, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = None
  else:
    input = _ops.convert_to_tensor(input, _dtypes.complex64)
    _inputs_flat = [input]
    _attrs = None
    _result = _execute.execute(b"BatchFFT2D", 1, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "BatchFFT2D", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result


def _batch_fft3d(input, name=None):
  r"""TODO: add doc.

  Args:
    input: A `Tensor` of type `complex64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `complex64`.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "BatchFFT3D", input=input, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = None
  else:
    input = _ops.convert_to_tensor(input, _dtypes.complex64)
    _inputs_flat = [input]
    _attrs = None
    _result = _execute.execute(b"BatchFFT3D", 1, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "BatchFFT3D", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result


def _batch_ifft(input, name=None):
  r"""TODO: add doc.

  Args:
    input: A `Tensor` of type `complex64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `complex64`.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "BatchIFFT", input=input, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = None
  else:
    input = _ops.convert_to_tensor(input, _dtypes.complex64)
    _inputs_flat = [input]
    _attrs = None
    _result = _execute.execute(b"BatchIFFT", 1, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "BatchIFFT", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result


def _batch_ifft2d(input, name=None):
  r"""TODO: add doc.

  Args:
    input: A `Tensor` of type `complex64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `complex64`.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "BatchIFFT2D", input=input, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = None
  else:
    input = _ops.convert_to_tensor(input, _dtypes.complex64)
    _inputs_flat = [input]
    _attrs = None
    _result = _execute.execute(b"BatchIFFT2D", 1, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "BatchIFFT2D", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result


def _batch_ifft3d(input, name=None):
  r"""TODO: add doc.

  Args:
    input: A `Tensor` of type `complex64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `complex64`.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "BatchIFFT3D", input=input, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = None
  else:
    input = _ops.convert_to_tensor(input, _dtypes.complex64)
    _inputs_flat = [input]
    _attrs = None
    _result = _execute.execute(b"BatchIFFT3D", 1, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "BatchIFFT3D", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result


def fft(input, name=None):
  r"""Fast Fourier transform.

  Computes the 1-dimensional discrete Fourier transform over the inner-most
  dimension of `input`.

  Args:
    input: A `Tensor` of type `complex64`. A complex64 tensor.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `complex64`.
    A complex64 tensor of the same shape as `input`. The inner-most
      dimension of `input` is replaced with its 1D Fourier transform.

    @compatibility(numpy)
    Equivalent to np.fft.fft
    @end_compatibility
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "FFT", input=input, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = None
  else:
    input = _ops.convert_to_tensor(input, _dtypes.complex64)
    _inputs_flat = [input]
    _attrs = None
    _result = _execute.execute(b"FFT", 1, inputs=_inputs_flat, attrs=_attrs,
                               ctx=_ctx, name=name)
  _execute.record_gradient(
      "FFT", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result


def fft2d(input, name=None):
  r"""2D fast Fourier transform.

  Computes the 2-dimensional discrete Fourier transform over the inner-most
  2 dimensions of `input`.

  Args:
    input: A `Tensor` of type `complex64`. A complex64 tensor.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `complex64`.
    A complex64 tensor of the same shape as `input`. The inner-most 2
      dimensions of `input` are replaced with their 2D Fourier transform.

    @compatibility(numpy)
    Equivalent to np.fft.fft2
    @end_compatibility
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "FFT2D", input=input, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = None
  else:
    input = _ops.convert_to_tensor(input, _dtypes.complex64)
    _inputs_flat = [input]
    _attrs = None
    _result = _execute.execute(b"FFT2D", 1, inputs=_inputs_flat, attrs=_attrs,
                               ctx=_ctx, name=name)
  _execute.record_gradient(
      "FFT2D", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result


def fft3d(input, name=None):
  r"""3D fast Fourier transform.

  Computes the 3-dimensional discrete Fourier transform over the inner-most 3
  dimensions of `input`.

  Args:
    input: A `Tensor` of type `complex64`. A complex64 tensor.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `complex64`.
    A complex64 tensor of the same shape as `input`. The inner-most 3
      dimensions of `input` are replaced with their 3D Fourier transform.

    @compatibility(numpy)
    Equivalent to np.fft.fftn with 3 dimensions.
    @end_compatibility
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "FFT3D", input=input, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = None
  else:
    input = _ops.convert_to_tensor(input, _dtypes.complex64)
    _inputs_flat = [input]
    _attrs = None
    _result = _execute.execute(b"FFT3D", 1, inputs=_inputs_flat, attrs=_attrs,
                               ctx=_ctx, name=name)
  _execute.record_gradient(
      "FFT3D", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result


def ifft(input, name=None):
  r"""Inverse fast Fourier transform.

  Computes the inverse 1-dimensional discrete Fourier transform over the
  inner-most dimension of `input`.

  Args:
    input: A `Tensor` of type `complex64`. A complex64 tensor.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `complex64`.
    A complex64 tensor of the same shape as `input`. The inner-most
      dimension of `input` is replaced with its inverse 1D Fourier transform.

    @compatibility(numpy)
    Equivalent to np.fft.ifft
    @end_compatibility
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "IFFT", input=input, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = None
  else:
    input = _ops.convert_to_tensor(input, _dtypes.complex64)
    _inputs_flat = [input]
    _attrs = None
    _result = _execute.execute(b"IFFT", 1, inputs=_inputs_flat, attrs=_attrs,
                               ctx=_ctx, name=name)
  _execute.record_gradient(
      "IFFT", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result


def ifft2d(input, name=None):
  r"""Inverse 2D fast Fourier transform.

  Computes the inverse 2-dimensional discrete Fourier transform over the
  inner-most 2 dimensions of `input`.

  Args:
    input: A `Tensor` of type `complex64`. A complex64 tensor.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `complex64`.
    A complex64 tensor of the same shape as `input`. The inner-most 2
      dimensions of `input` are replaced with their inverse 2D Fourier transform.

    @compatibility(numpy)
    Equivalent to np.fft.ifft2
    @end_compatibility
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "IFFT2D", input=input, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = None
  else:
    input = _ops.convert_to_tensor(input, _dtypes.complex64)
    _inputs_flat = [input]
    _attrs = None
    _result = _execute.execute(b"IFFT2D", 1, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "IFFT2D", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result


def ifft3d(input, name=None):
  r"""Inverse 3D fast Fourier transform.

  Computes the inverse 3-dimensional discrete Fourier transform over the
  inner-most 3 dimensions of `input`.

  Args:
    input: A `Tensor` of type `complex64`. A complex64 tensor.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `complex64`.
    A complex64 tensor of the same shape as `input`. The inner-most 3
      dimensions of `input` are replaced with their inverse 3D Fourier transform.

    @compatibility(numpy)
    Equivalent to np.fft.ifftn with 3 dimensions.
    @end_compatibility
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "IFFT3D", input=input, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = None
  else:
    input = _ops.convert_to_tensor(input, _dtypes.complex64)
    _inputs_flat = [input]
    _attrs = None
    _result = _execute.execute(b"IFFT3D", 1, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "IFFT3D", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result


def irfft(input, fft_length, name=None):
  r"""Inverse real-valued fast Fourier transform.

  Computes the inverse 1-dimensional discrete Fourier transform of a real-valued
  signal over the inner-most dimension of `input`.

  The inner-most dimension of `input` is assumed to be the result of `RFFT`: the
  `fft_length / 2 + 1` unique components of the DFT of a real-valued signal. If
  `fft_length` is not provided, it is computed from the size of the inner-most
  dimension of `input` (`fft_length = 2 * (inner - 1)`). If the FFT length used to
  compute `input` is odd, it should be provided since it cannot be inferred
  properly.

  Along the axis `IRFFT` is computed on, if `fft_length / 2 + 1` is smaller
  than the corresponding dimension of `input`, the dimension is cropped. If it is
  larger, the dimension is padded with zeros.

  Args:
    input: A `Tensor` of type `complex64`. A complex64 tensor.
    fft_length: A `Tensor` of type `int32`.
      An int32 tensor of shape [1]. The FFT length.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `float32`.
    A float32 tensor of the same rank as `input`. The inner-most
      dimension of `input` is replaced with the `fft_length` samples of its inverse
      1D Fourier transform.

    @compatibility(numpy)
    Equivalent to np.fft.irfft
    @end_compatibility
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "IRFFT", input=input, fft_length=fft_length, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = None
  else:
    input = _ops.convert_to_tensor(input, _dtypes.complex64)
    fft_length = _ops.convert_to_tensor(fft_length, _dtypes.int32)
    _inputs_flat = [input, fft_length]
    _attrs = None
    _result = _execute.execute(b"IRFFT", 1, inputs=_inputs_flat, attrs=_attrs,
                               ctx=_ctx, name=name)
  _execute.record_gradient(
      "IRFFT", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result


def irfft2d(input, fft_length, name=None):
  r"""Inverse 2D real-valued fast Fourier transform.

  Computes the inverse 2-dimensional discrete Fourier transform of a real-valued
  signal over the inner-most 2 dimensions of `input`.

  The inner-most 2 dimensions of `input` are assumed to be the result of `RFFT2D`:
  The inner-most dimension contains the `fft_length / 2 + 1` unique components of
  the DFT of a real-valued signal. If `fft_length` is not provided, it is computed
  from the size of the inner-most 2 dimensions of `input`. If the FFT length used
  to compute `input` is odd, it should be provided since it cannot be inferred
  properly.

  Along each axis `IRFFT2D` is computed on, if `fft_length` (or
  `fft_length / 2 + 1` for the inner-most dimension) is smaller than the
  corresponding dimension of `input`, the dimension is cropped. If it is larger,
  the dimension is padded with zeros.

  Args:
    input: A `Tensor` of type `complex64`. A complex64 tensor.
    fft_length: A `Tensor` of type `int32`.
      An int32 tensor of shape [2]. The FFT length for each dimension.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `float32`.
    A float32 tensor of the same rank as `input`. The inner-most 2
      dimensions of `input` are replaced with the `fft_length` samples of their
      inverse 2D Fourier transform.

    @compatibility(numpy)
    Equivalent to np.fft.irfft2
    @end_compatibility
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "IRFFT2D", input=input, fft_length=fft_length, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = None
  else:
    input = _ops.convert_to_tensor(input, _dtypes.complex64)
    fft_length = _ops.convert_to_tensor(fft_length, _dtypes.int32)
    _inputs_flat = [input, fft_length]
    _attrs = None
    _result = _execute.execute(b"IRFFT2D", 1, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "IRFFT2D", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result


def irfft3d(input, fft_length, name=None):
  r"""Inverse 3D real-valued fast Fourier transform.

  Computes the inverse 3-dimensional discrete Fourier transform of a real-valued
  signal over the inner-most 3 dimensions of `input`.

  The inner-most 3 dimensions of `input` are assumed to be the result of `RFFT3D`:
  The inner-most dimension contains the `fft_length / 2 + 1` unique components of
  the DFT of a real-valued signal. If `fft_length` is not provided, it is computed
  from the size of the inner-most 3 dimensions of `input`. If the FFT length used
  to compute `input` is odd, it should be provided since it cannot be inferred
  properly.

  Along each axis `IRFFT3D` is computed on, if `fft_length` (or
  `fft_length / 2 + 1` for the inner-most dimension) is smaller than the
  corresponding dimension of `input`, the dimension is cropped. If it is larger,
  the dimension is padded with zeros.

  Args:
    input: A `Tensor` of type `complex64`. A complex64 tensor.
    fft_length: A `Tensor` of type `int32`.
      An int32 tensor of shape [3]. The FFT length for each dimension.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `float32`.
    A float32 tensor of the same rank as `input`. The inner-most 3
      dimensions of `input` are replaced with the `fft_length` samples of their
      inverse 3D real Fourier transform.

    @compatibility(numpy)
    Equivalent to np.irfftn with 3 dimensions.
    @end_compatibility
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "IRFFT3D", input=input, fft_length=fft_length, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = None
  else:
    input = _ops.convert_to_tensor(input, _dtypes.complex64)
    fft_length = _ops.convert_to_tensor(fft_length, _dtypes.int32)
    _inputs_flat = [input, fft_length]
    _attrs = None
    _result = _execute.execute(b"IRFFT3D", 1, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "IRFFT3D", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result


def rfft(input, fft_length, name=None):
  r"""Real-valued fast Fourier transform.

  Computes the 1-dimensional discrete Fourier transform of a real-valued signal
  over the inner-most dimension of `input`.

  Since the DFT of a real signal is Hermitian-symmetric, `RFFT` only returns the
  `fft_length / 2 + 1` unique components of the FFT: the zero-frequency term,
  followed by the `fft_length / 2` positive-frequency terms.

  Along the axis `RFFT` is computed on, if `fft_length` is smaller than the
  corresponding dimension of `input`, the dimension is cropped. If it is larger,
  the dimension is padded with zeros.

  Args:
    input: A `Tensor` of type `float32`. A float32 tensor.
    fft_length: A `Tensor` of type `int32`.
      An int32 tensor of shape [1]. The FFT length.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `complex64`.
    A complex64 tensor of the same rank as `input`. The inner-most
      dimension of `input` is replaced with the `fft_length / 2 + 1` unique
      frequency components of its 1D Fourier transform.

    @compatibility(numpy)
    Equivalent to np.fft.rfft
    @end_compatibility
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "RFFT", input=input, fft_length=fft_length, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = None
  else:
    input = _ops.convert_to_tensor(input, _dtypes.float32)
    fft_length = _ops.convert_to_tensor(fft_length, _dtypes.int32)
    _inputs_flat = [input, fft_length]
    _attrs = None
    _result = _execute.execute(b"RFFT", 1, inputs=_inputs_flat, attrs=_attrs,
                               ctx=_ctx, name=name)
  _execute.record_gradient(
      "RFFT", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result


def rfft2d(input, fft_length, name=None):
  r"""2D real-valued fast Fourier transform.

  Computes the 2-dimensional discrete Fourier transform of a real-valued signal
  over the inner-most 2 dimensions of `input`.

  Since the DFT of a real signal is Hermitian-symmetric, `RFFT2D` only returns the
  `fft_length / 2 + 1` unique components of the FFT for the inner-most dimension
  of `output`: the zero-frequency term, followed by the `fft_length / 2`
  positive-frequency terms.

  Along each axis `RFFT2D` is computed on, if `fft_length` is smaller than the
  corresponding dimension of `input`, the dimension is cropped. If it is larger,
  the dimension is padded with zeros.

  Args:
    input: A `Tensor` of type `float32`. A float32 tensor.
    fft_length: A `Tensor` of type `int32`.
      An int32 tensor of shape [2]. The FFT length for each dimension.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `complex64`.
    A complex64 tensor of the same rank as `input`. The inner-most 2
      dimensions of `input` are replaced with their 2D Fourier transform. The
      inner-most dimension contains `fft_length / 2 + 1` unique frequency
      components.

    @compatibility(numpy)
    Equivalent to np.fft.rfft2
    @end_compatibility
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "RFFT2D", input=input, fft_length=fft_length, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = None
  else:
    input = _ops.convert_to_tensor(input, _dtypes.float32)
    fft_length = _ops.convert_to_tensor(fft_length, _dtypes.int32)
    _inputs_flat = [input, fft_length]
    _attrs = None
    _result = _execute.execute(b"RFFT2D", 1, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "RFFT2D", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result


def rfft3d(input, fft_length, name=None):
  r"""3D real-valued fast Fourier transform.

  Computes the 3-dimensional discrete Fourier transform of a real-valued signal
  over the inner-most 3 dimensions of `input`.

  Since the DFT of a real signal is Hermitian-symmetric, `RFFT3D` only returns the
  `fft_length / 2 + 1` unique components of the FFT for the inner-most dimension
  of `output`: the zero-frequency term, followed by the `fft_length / 2`
  positive-frequency terms.

  Along each axis `RFFT3D` is computed on, if `fft_length` is smaller than the
  corresponding dimension of `input`, the dimension is cropped. If it is larger,
  the dimension is padded with zeros.

  Args:
    input: A `Tensor` of type `float32`. A float32 tensor.
    fft_length: A `Tensor` of type `int32`.
      An int32 tensor of shape [3]. The FFT length for each dimension.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `complex64`.
    A complex64 tensor of the same rank as `input`. The inner-most 3
      dimensions of `input` are replaced with the their 3D Fourier transform. The
      inner-most dimension contains `fft_length / 2 + 1` unique frequency
      components.

    @compatibility(numpy)
    Equivalent to np.fft.rfftn with 3 dimensions.
    @end_compatibility
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "RFFT3D", input=input, fft_length=fft_length, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = None
  else:
    input = _ops.convert_to_tensor(input, _dtypes.float32)
    fft_length = _ops.convert_to_tensor(fft_length, _dtypes.int32)
    _inputs_flat = [input, fft_length]
    _attrs = None
    _result = _execute.execute(b"RFFT3D", 1, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "RFFT3D", _inputs_flat, _attrs, _result, name)
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
#   name: "BatchFFT"
#   input_arg {
#     name: "input"
#     type: DT_COMPLEX64
#   }
#   output_arg {
#     name: "output"
#     type: DT_COMPLEX64
#   }
#   deprecation {
#     version: 15
#     explanation: "Use FFT"
#   }
# }
# op {
#   name: "BatchFFT2D"
#   input_arg {
#     name: "input"
#     type: DT_COMPLEX64
#   }
#   output_arg {
#     name: "output"
#     type: DT_COMPLEX64
#   }
#   deprecation {
#     version: 15
#     explanation: "Use FFT2D"
#   }
# }
# op {
#   name: "BatchFFT3D"
#   input_arg {
#     name: "input"
#     type: DT_COMPLEX64
#   }
#   output_arg {
#     name: "output"
#     type: DT_COMPLEX64
#   }
#   deprecation {
#     version: 15
#     explanation: "Use FFT3D"
#   }
# }
# op {
#   name: "BatchIFFT"
#   input_arg {
#     name: "input"
#     type: DT_COMPLEX64
#   }
#   output_arg {
#     name: "output"
#     type: DT_COMPLEX64
#   }
#   deprecation {
#     version: 15
#     explanation: "Use IFFT"
#   }
# }
# op {
#   name: "BatchIFFT2D"
#   input_arg {
#     name: "input"
#     type: DT_COMPLEX64
#   }
#   output_arg {
#     name: "output"
#     type: DT_COMPLEX64
#   }
#   deprecation {
#     version: 15
#     explanation: "Use IFFT2D"
#   }
# }
# op {
#   name: "BatchIFFT3D"
#   input_arg {
#     name: "input"
#     type: DT_COMPLEX64
#   }
#   output_arg {
#     name: "output"
#     type: DT_COMPLEX64
#   }
#   deprecation {
#     version: 15
#     explanation: "Use IFFT3D"
#   }
# }
# op {
#   name: "FFT"
#   input_arg {
#     name: "input"
#     type: DT_COMPLEX64
#   }
#   output_arg {
#     name: "output"
#     type: DT_COMPLEX64
#   }
# }
# op {
#   name: "FFT2D"
#   input_arg {
#     name: "input"
#     type: DT_COMPLEX64
#   }
#   output_arg {
#     name: "output"
#     type: DT_COMPLEX64
#   }
# }
# op {
#   name: "FFT3D"
#   input_arg {
#     name: "input"
#     type: DT_COMPLEX64
#   }
#   output_arg {
#     name: "output"
#     type: DT_COMPLEX64
#   }
# }
# op {
#   name: "IFFT"
#   input_arg {
#     name: "input"
#     type: DT_COMPLEX64
#   }
#   output_arg {
#     name: "output"
#     type: DT_COMPLEX64
#   }
# }
# op {
#   name: "IFFT2D"
#   input_arg {
#     name: "input"
#     type: DT_COMPLEX64
#   }
#   output_arg {
#     name: "output"
#     type: DT_COMPLEX64
#   }
# }
# op {
#   name: "IFFT3D"
#   input_arg {
#     name: "input"
#     type: DT_COMPLEX64
#   }
#   output_arg {
#     name: "output"
#     type: DT_COMPLEX64
#   }
# }
# op {
#   name: "IRFFT"
#   input_arg {
#     name: "input"
#     type: DT_COMPLEX64
#   }
#   input_arg {
#     name: "fft_length"
#     type: DT_INT32
#   }
#   output_arg {
#     name: "output"
#     type: DT_FLOAT
#   }
# }
# op {
#   name: "IRFFT2D"
#   input_arg {
#     name: "input"
#     type: DT_COMPLEX64
#   }
#   input_arg {
#     name: "fft_length"
#     type: DT_INT32
#   }
#   output_arg {
#     name: "output"
#     type: DT_FLOAT
#   }
# }
# op {
#   name: "IRFFT3D"
#   input_arg {
#     name: "input"
#     type: DT_COMPLEX64
#   }
#   input_arg {
#     name: "fft_length"
#     type: DT_INT32
#   }
#   output_arg {
#     name: "output"
#     type: DT_FLOAT
#   }
# }
# op {
#   name: "RFFT"
#   input_arg {
#     name: "input"
#     type: DT_FLOAT
#   }
#   input_arg {
#     name: "fft_length"
#     type: DT_INT32
#   }
#   output_arg {
#     name: "output"
#     type: DT_COMPLEX64
#   }
# }
# op {
#   name: "RFFT2D"
#   input_arg {
#     name: "input"
#     type: DT_FLOAT
#   }
#   input_arg {
#     name: "fft_length"
#     type: DT_INT32
#   }
#   output_arg {
#     name: "output"
#     type: DT_COMPLEX64
#   }
# }
# op {
#   name: "RFFT3D"
#   input_arg {
#     name: "input"
#     type: DT_FLOAT
#   }
#   input_arg {
#     name: "fft_length"
#     type: DT_INT32
#   }
#   output_arg {
#     name: "output"
#     type: DT_COMPLEX64
#   }
# }
_op_def_lib = _InitOpDefLibrary(b"\n.\n\010BatchFFT\022\t\n\005input\030\010\032\n\n\006output\030\010B\013\010\017\022\007Use FFT\n2\n\nBatchFFT2D\022\t\n\005input\030\010\032\n\n\006output\030\010B\r\010\017\022\tUse FFT2D\n2\n\nBatchFFT3D\022\t\n\005input\030\010\032\n\n\006output\030\010B\r\010\017\022\tUse FFT3D\n0\n\tBatchIFFT\022\t\n\005input\030\010\032\n\n\006output\030\010B\014\010\017\022\010Use IFFT\n4\n\013BatchIFFT2D\022\t\n\005input\030\010\032\n\n\006output\030\010B\016\010\017\022\nUse IFFT2D\n4\n\013BatchIFFT3D\022\t\n\005input\030\010\032\n\n\006output\030\010B\016\010\017\022\nUse IFFT3D\n\034\n\003FFT\022\t\n\005input\030\010\032\n\n\006output\030\010\n\036\n\005FFT2D\022\t\n\005input\030\010\032\n\n\006output\030\010\n\036\n\005FFT3D\022\t\n\005input\030\010\032\n\n\006output\030\010\n\035\n\004IFFT\022\t\n\005input\030\010\032\n\n\006output\030\010\n\037\n\006IFFT2D\022\t\n\005input\030\010\032\n\n\006output\030\010\n\037\n\006IFFT3D\022\t\n\005input\030\010\032\n\n\006output\030\010\n.\n\005IRFFT\022\t\n\005input\030\010\022\016\n\nfft_length\030\003\032\n\n\006output\030\001\n0\n\007IRFFT2D\022\t\n\005input\030\010\022\016\n\nfft_length\030\003\032\n\n\006output\030\001\n0\n\007IRFFT3D\022\t\n\005input\030\010\022\016\n\nfft_length\030\003\032\n\n\006output\030\001\n-\n\004RFFT\022\t\n\005input\030\001\022\016\n\nfft_length\030\003\032\n\n\006output\030\010\n/\n\006RFFT2D\022\t\n\005input\030\001\022\016\n\nfft_length\030\003\032\n\n\006output\030\010\n/\n\006RFFT3D\022\t\n\005input\030\001\022\016\n\nfft_length\030\003\032\n\n\006output\030\010")
