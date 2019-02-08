"""Python wrappers around TensorFlow ops.

This file is MACHINE GENERATED! Do not edit.
Original C++ source file: reduce_slice_ops.cc
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


def reduce_slice_max(data, indices, axis, name=None):
  r"""Dynamically compute the maximum over the first dimension of a tensor according

  to start and end indices specified at "indices".

  For example:

  ```prettyprint
  # if 'data' is [[   1,  20,   3]
                  [ 400,   5,  60]
                  [  70,   8, 900]
                  [1000,2000,3000]],

  and 'indices' is [[0,1]
                    [1,1]
                    [0,2]],

  the the output will be [[          1,         20,          3]
                          [ -BIG_VALUE, -BIG_VALUE, -BIG_VALUE]
                          [        400,         20,         60]].
  ```

  The data must be at least rank 1. The indices can be of shape (?,2) where the
  first column is start indices and the second column is end indices. The end indices
  are not included in the reduce operation, which means, if you want to do a reduce
  over indices 0,1,2, then you should have start index 0 and end index 3. If end
  index is smaller than or equal to start, the result will be 1. If end index is
  out of bounds, then the reduce operation will automatically stop at the bound, so
  feel free to put a large number as your end of your index if you want to do the
  reduction until the bound. The indices can also be of shape (?), in this case, the
  start index of i will be the element at i, then end index of i will be the element
  at i+1. That is:

  ```prettyprint
  indices = [0,5,11,115]

  is equivalent to

  indices = [ [0,5],
              [5,11],
              [11,115]]
  ```

  Args:
    data: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int64`, `int32`, `uint8`, `uint16`, `int16`, `int8`, `complex64`, `complex128`, `qint8`, `quint8`, `qint32`, `half`.
      The source of data where the computation will be taken from.
    indices: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      start, end indices that controls which part to be included.
    axis: A `Tensor` of type `int64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `data`. the computed product values.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "ReduceSliceMax", data=data, indices=indices, axis=axis, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("T", _op.get_attr("T"), "Tindices", _op.get_attr("Tindices"))
  else:
    _attr_T, (data,) = _execute.args_to_matching_eager([data], _ctx)
    _attr_T = _attr_T.as_datatype_enum
    _attr_Tindices, (indices,) = _execute.args_to_matching_eager([indices], _ctx)
    _attr_Tindices = _attr_Tindices.as_datatype_enum
    axis = _ops.convert_to_tensor(axis, _dtypes.int64)
    _inputs_flat = [data, indices, axis]
    _attrs = ("T", _attr_T, "Tindices", _attr_Tindices)
    _result = _execute.execute(b"ReduceSliceMax", 1, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "ReduceSliceMax", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result

_ops.RegisterShape("ReduceSliceMax")(None)


def reduce_slice_min(data, indices, axis, name=None):
  r"""Dynamically compute the minimum over the first dimension of a tensor according

  to start and end indices specified at 'indices'.

  For example:

  ```prettyprint
  # if 'data' is [[   1,  20,   3]
                  [ 400,   5,  60]
                  [  70,   8, 900]
                  [1000,2000,3000]],

  and 'indices' is [[0,1]
                    [1,1]
                    [0,2]],

  the the output will be [[          1,         20,          3]
                          [ +BIG_VALUE, +BIG_VALUE, +BIG_VALUE]
                          [          1,          5,          3]].
  ```

  The data must be at least rank 1. The indices can be of shape (?,2) where the
  first column is start indices and the second column is end indices. The end indices
  are not included in the reduce operation, which means, if you want to do a reduce
  over indices 0,1,2, then you should have start index 0 and end index 3. If end
  index is smaller than or equal to start, the result will be 1. If end index is
  out of bounds, then the reduce operation will automatically stop at the bound, so
  feel free to put a large number as your end of your index if you want to do the
  reduction until the bound. The indices can also be of shape (?), in this case, the
  start index of i will be the element at i, then end index of i will be the element
  at i+1. That is:

  ```prettyprint
  indices = [0,5,11,115]

  is equivalent to

  indices = [ [0,5],
              [5,11],
              [11,115]]
  ```

  Args:
    data: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int64`, `int32`, `uint8`, `uint16`, `int16`, `int8`, `complex64`, `complex128`, `qint8`, `quint8`, `qint32`, `half`.
      The source of data where the computation will be taken from.
    indices: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      start, end indices that controls which part to be included.
    axis: A `Tensor` of type `int64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `data`. the computed product values.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "ReduceSliceMin", data=data, indices=indices, axis=axis, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("T", _op.get_attr("T"), "Tindices", _op.get_attr("Tindices"))
  else:
    _attr_T, (data,) = _execute.args_to_matching_eager([data], _ctx)
    _attr_T = _attr_T.as_datatype_enum
    _attr_Tindices, (indices,) = _execute.args_to_matching_eager([indices], _ctx)
    _attr_Tindices = _attr_Tindices.as_datatype_enum
    axis = _ops.convert_to_tensor(axis, _dtypes.int64)
    _inputs_flat = [data, indices, axis]
    _attrs = ("T", _attr_T, "Tindices", _attr_Tindices)
    _result = _execute.execute(b"ReduceSliceMin", 1, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "ReduceSliceMin", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result

_ops.RegisterShape("ReduceSliceMin")(None)


def reduce_slice_prod(data, indices, axis, name=None):
  r"""Dynamically compute the product over the first dimension of a tensor according

  to start and end indices specified at 'indices'.

  For example:

  ```prettyprint
  # if 'data' is [[   1,   2,   3]
                  [  40,  50,  60]
                  [ 700, 800, 900]
                  [1000,2000,3000]],

  and 'indices' is [[0,1]
                    [1,1]
                    [0,2]],

  the the output will be [[ 1,  2,  3]
                          [ 1,  1,  1]
                          [40,100,180]].
  ```

  The data must be at least rank 1. The indices can be of shape (?,2) where the
  first column is start indices and the second column is end indices. The end indices
  are not included in the reduce operation, which means, if you want to do a reduce
  over indices 0,1,2, then you should have start index 0 and end index 3. If end
  index is smaller than or equal to start, the result will be 1. If end index is
  out of bounds, then the reduce operation will automatically stop at the bound, so
  feel free to put a large number as your end of your index if you want to do the
  reduction until the bound. The indices can also be of shape (?), in this case, the
  start index of i will be the element at i, then end index of i will be the element
  at i+1. That is:

  ```prettyprint
  indices = [0,5,11,115]

  is equivalent to

  indices = [ [0,5],
              [5,11],
              [11,115]]
  ```

  Args:
    data: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int64`, `int32`, `uint8`, `uint16`, `int16`, `int8`, `complex64`, `complex128`, `qint8`, `quint8`, `qint32`, `half`.
      The source of data where the computation will be taken from.
    indices: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      start, end indices that controls which part to be included.
    axis: A `Tensor` of type `int64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `data`. the computed product values.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "ReduceSliceProd", data=data, indices=indices, axis=axis, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("T", _op.get_attr("T"), "Tindices", _op.get_attr("Tindices"))
  else:
    _attr_T, (data,) = _execute.args_to_matching_eager([data], _ctx)
    _attr_T = _attr_T.as_datatype_enum
    _attr_Tindices, (indices,) = _execute.args_to_matching_eager([indices], _ctx)
    _attr_Tindices = _attr_Tindices.as_datatype_enum
    axis = _ops.convert_to_tensor(axis, _dtypes.int64)
    _inputs_flat = [data, indices, axis]
    _attrs = ("T", _attr_T, "Tindices", _attr_Tindices)
    _result = _execute.execute(b"ReduceSliceProd", 1, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "ReduceSliceProd", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result

_ops.RegisterShape("ReduceSliceProd")(None)


def reduce_slice_sum(data, indices, axis, name=None):
  r"""Dynamically sum over the first dimension of a tensor according to start and end

  indices specified at 'index'.

  For example:

  ```prettyprint
  # if 'data' is [[   1,   2,   3]
                  [  40,  50,  60]
                  [ 700, 800, 900]
                  [1000,2000,3000]],

  and 'indices' is [[0,1]
                    [1,1]
                    [0,2]],

  the the output will be [[ 1, 2, 3]
                          [ 0, 0, 0]
                          [41,52,63]].
  ```

  The data must be at least rank 1. The indices must be of shape (?,2) where the
  first column is start indices and the second column is end indices. The end indices
  are not included in the reduce operation, which means, if you want to do a reduce
  over indices 0,1,2, then you should have start index 0 and end index 3. If end
  index is smaller than or equal to start, the result will be zero. If end index is
  out of bounds, then the reduce operation will automatically stop at the bound, so
  feel free to put a large number as your end of your index if you want to do the
  reduction until the bound.

  Args:
    data: A `Tensor`. Must be one of the following types: `float32`, `float64`, `int64`, `int32`, `uint8`, `uint16`, `int16`, `int8`, `complex64`, `complex128`, `qint8`, `quint8`, `qint32`, `half`.
      The source of data where the computation will be taken from.
    indices: A `Tensor`. Must be one of the following types: `int32`, `int64`.
      start, end indices that controls which part to be included.
    axis: A `Tensor` of type `int64`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `data`. the computed sum values.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "ReduceSliceSum", data=data, indices=indices, axis=axis, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("T", _op.get_attr("T"), "Tindices", _op.get_attr("Tindices"))
  else:
    _attr_T, (data,) = _execute.args_to_matching_eager([data], _ctx)
    _attr_T = _attr_T.as_datatype_enum
    _attr_Tindices, (indices,) = _execute.args_to_matching_eager([indices], _ctx)
    _attr_Tindices = _attr_Tindices.as_datatype_enum
    axis = _ops.convert_to_tensor(axis, _dtypes.int64)
    _inputs_flat = [data, indices, axis]
    _attrs = ("T", _attr_T, "Tindices", _attr_Tindices)
    _result = _execute.execute(b"ReduceSliceSum", 1, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "ReduceSliceSum", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result

_ops.RegisterShape("ReduceSliceSum")(None)

def _InitOpDefLibrary(op_list_proto_bytes):
  op_list = _op_def_pb2.OpList()
  op_list.ParseFromString(op_list_proto_bytes)
  _op_def_registry.register_op_list(op_list)
  op_def_lib = _op_def_library.OpDefLibrary()
  op_def_lib.add_op_list(op_list)
  return op_def_lib
# op {
#   name: "ReduceSliceMax"
#   input_arg {
#     name: "data"
#     type_attr: "T"
#   }
#   input_arg {
#     name: "indices"
#     type_attr: "Tindices"
#   }
#   input_arg {
#     name: "axis"
#     type: DT_INT64
#   }
#   output_arg {
#     name: "output"
#     type_attr: "T"
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
# }
# op {
#   name: "ReduceSliceMin"
#   input_arg {
#     name: "data"
#     type_attr: "T"
#   }
#   input_arg {
#     name: "indices"
#     type_attr: "Tindices"
#   }
#   input_arg {
#     name: "axis"
#     type: DT_INT64
#   }
#   output_arg {
#     name: "output"
#     type_attr: "T"
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
# }
# op {
#   name: "ReduceSliceProd"
#   input_arg {
#     name: "data"
#     type_attr: "T"
#   }
#   input_arg {
#     name: "indices"
#     type_attr: "Tindices"
#   }
#   input_arg {
#     name: "axis"
#     type: DT_INT64
#   }
#   output_arg {
#     name: "output"
#     type_attr: "T"
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
# }
# op {
#   name: "ReduceSliceSum"
#   input_arg {
#     name: "data"
#     type_attr: "T"
#   }
#   input_arg {
#     name: "indices"
#     type_attr: "Tindices"
#   }
#   input_arg {
#     name: "axis"
#     type: DT_INT64
#   }
#   output_arg {
#     name: "output"
#     type_attr: "T"
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
# }
_op_def_lib = _InitOpDefLibrary(b"\n\200\001\n\016ReduceSliceMax\022\t\n\004data\"\001T\022\023\n\007indices\"\010Tindices\022\010\n\004axis\030\t\032\013\n\006output\"\001T\"\035\n\001T\022\004type:\022\n\0202\016\001\002\t\003\004\021\005\006\010\022\013\014\r\023\"\030\n\010Tindices\022\004type:\006\n\0042\002\003\t\n\200\001\n\016ReduceSliceMin\022\t\n\004data\"\001T\022\023\n\007indices\"\010Tindices\022\010\n\004axis\030\t\032\013\n\006output\"\001T\"\035\n\001T\022\004type:\022\n\0202\016\001\002\t\003\004\021\005\006\010\022\013\014\r\023\"\030\n\010Tindices\022\004type:\006\n\0042\002\003\t\n\201\001\n\017ReduceSliceProd\022\t\n\004data\"\001T\022\023\n\007indices\"\010Tindices\022\010\n\004axis\030\t\032\013\n\006output\"\001T\"\035\n\001T\022\004type:\022\n\0202\016\001\002\t\003\004\021\005\006\010\022\013\014\r\023\"\030\n\010Tindices\022\004type:\006\n\0042\002\003\t\n\200\001\n\016ReduceSliceSum\022\t\n\004data\"\001T\022\023\n\007indices\"\010Tindices\022\010\n\004axis\030\t\032\013\n\006output\"\001T\"\035\n\001T\022\004type:\022\n\0202\016\001\002\t\003\004\021\005\006\010\022\013\014\r\023\"\030\n\010Tindices\022\004type:\006\n\0042\002\003\t")
