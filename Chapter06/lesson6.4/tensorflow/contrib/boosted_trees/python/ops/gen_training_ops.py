"""Python wrappers around TensorFlow ops.

This file is MACHINE GENERATED! Do not edit.
Original C++ source file: gen_training_ops_py.cc
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


def center_tree_ensemble_bias(tree_ensemble_handle, stamp_token, next_stamp_token, delta_updates, learner_config, centering_epsilon=0.01, name=None):
  r"""Centers the tree ensemble bias before adding trees based on feature splits.

  Args:
    tree_ensemble_handle: A `Tensor` of type `resource`.
      Handle to the ensemble variable.
    stamp_token: A `Tensor` of type `int64`.
      Stamp token for validating operation consistency.
    next_stamp_token: A `Tensor` of type `int64`.
      Stamp token to be used for the next iteration.
    delta_updates: A `Tensor` of type `float32`.
      Rank 1 Tensor containing delta updates per bias dimension.
    learner_config: A `string`.
      Config for the learner of type LearnerConfig proto.
    centering_epsilon: An optional `float`. Defaults to `0.01`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `bool`.
    Scalar indicating whether more centering is needed.
  """
  learner_config = _execute.make_str(learner_config, "learner_config")
  if centering_epsilon is None:
    centering_epsilon = 0.01
  centering_epsilon = _execute.make_float(centering_epsilon, "centering_epsilon")
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "CenterTreeEnsembleBias", tree_ensemble_handle=tree_ensemble_handle,
        stamp_token=stamp_token, next_stamp_token=next_stamp_token,
        delta_updates=delta_updates, learner_config=learner_config,
        centering_epsilon=centering_epsilon, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("learner_config", _op.get_attr("learner_config"),
              "centering_epsilon", _op.get_attr("centering_epsilon"))
  else:
    tree_ensemble_handle = _ops.convert_to_tensor(tree_ensemble_handle, _dtypes.resource)
    stamp_token = _ops.convert_to_tensor(stamp_token, _dtypes.int64)
    next_stamp_token = _ops.convert_to_tensor(next_stamp_token, _dtypes.int64)
    delta_updates = _ops.convert_to_tensor(delta_updates, _dtypes.float32)
    _inputs_flat = [tree_ensemble_handle, stamp_token, next_stamp_token, delta_updates]
    _attrs = ("learner_config", learner_config, "centering_epsilon",
              centering_epsilon)
    _result = _execute.execute(b"CenterTreeEnsembleBias", 1,
                               inputs=_inputs_flat, attrs=_attrs, ctx=_ctx,
                               name=name)
  _execute.record_gradient(
      "CenterTreeEnsembleBias", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result

_ops.RegisterShape("CenterTreeEnsembleBias")(None)


def grow_tree_ensemble(tree_ensemble_handle, stamp_token, next_stamp_token, learning_rate, dropout_seed, partition_ids, gains, splits, learner_config, center_bias, name=None):
  r"""Grows the tree ensemble by either adding a layer to the last tree being grown

  or by starting a new tree.

  Args:
    tree_ensemble_handle: A `Tensor` of type `resource`.
      Handle to the ensemble variable.
    stamp_token: A `Tensor` of type `int64`.
      Stamp token for validating operation consistency.
    next_stamp_token: A `Tensor` of type `int64`.
      Stamp token to be used for the next iteration.
    learning_rate: A `Tensor` of type `float32`. Scalar learning rate.
    dropout_seed: A `Tensor` of type `int64`.
    partition_ids: A list of `Tensor` objects with type `int32`.
      List of Rank 1 Tensors containing partition Id per candidate.
    gains: A list with the same length as `partition_ids` of `Tensor` objects with type `float32`.
      List of Rank 1 Tensors containing gains per candidate.
    splits: A list with the same length as `partition_ids` of `Tensor` objects with type `string`.
      List of Rank 1 Tensors containing serialized SplitInfo protos per candidate.
    learner_config: A `string`.
      Config for the learner of type LearnerConfig proto.
    center_bias: A `bool`.
    name: A name for the operation (optional).

  Returns:
    The created Operation.
  """
  if not isinstance(partition_ids, (list, tuple)):
    raise TypeError(
        "Expected list for 'partition_ids' argument to "
        "'grow_tree_ensemble' Op, not %r." % partition_ids)
  _attr_num_handlers = len(partition_ids)
  if not isinstance(gains, (list, tuple)):
    raise TypeError(
        "Expected list for 'gains' argument to "
        "'grow_tree_ensemble' Op, not %r." % gains)
  if len(gains) != _attr_num_handlers:
    raise ValueError(
        "List argument 'gains' to 'grow_tree_ensemble' Op with length %d "
        "must match length %d of argument 'partition_ids'." %
        (len(gains), _attr_num_handlers))
  if not isinstance(splits, (list, tuple)):
    raise TypeError(
        "Expected list for 'splits' argument to "
        "'grow_tree_ensemble' Op, not %r." % splits)
  if len(splits) != _attr_num_handlers:
    raise ValueError(
        "List argument 'splits' to 'grow_tree_ensemble' Op with length %d "
        "must match length %d of argument 'partition_ids'." %
        (len(splits), _attr_num_handlers))
  learner_config = _execute.make_str(learner_config, "learner_config")
  center_bias = _execute.make_bool(center_bias, "center_bias")
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "GrowTreeEnsemble", tree_ensemble_handle=tree_ensemble_handle,
        stamp_token=stamp_token, next_stamp_token=next_stamp_token,
        learning_rate=learning_rate, dropout_seed=dropout_seed,
        partition_ids=partition_ids, gains=gains, splits=splits,
        learner_config=learner_config, center_bias=center_bias, name=name)
    return _op
  else:
    tree_ensemble_handle = _ops.convert_to_tensor(tree_ensemble_handle, _dtypes.resource)
    stamp_token = _ops.convert_to_tensor(stamp_token, _dtypes.int64)
    next_stamp_token = _ops.convert_to_tensor(next_stamp_token, _dtypes.int64)
    learning_rate = _ops.convert_to_tensor(learning_rate, _dtypes.float32)
    dropout_seed = _ops.convert_to_tensor(dropout_seed, _dtypes.int64)
    partition_ids = _ops.convert_n_to_tensor(partition_ids, _dtypes.int32)
    gains = _ops.convert_n_to_tensor(gains, _dtypes.float32)
    splits = _ops.convert_n_to_tensor(splits, _dtypes.string)
    _inputs_flat = [tree_ensemble_handle, stamp_token, next_stamp_token, learning_rate, dropout_seed] + list(partition_ids) + list(gains) + list(splits)
    _attrs = ("learner_config", learner_config, "num_handlers",
              _attr_num_handlers, "center_bias", center_bias)
    _result = _execute.execute(b"GrowTreeEnsemble", 0, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
  return _result

_ops.RegisterShape("GrowTreeEnsemble")(None)


_tree_ensemble_stats_outputs = ["num_trees", "num_layers", "active_tree",
                               "active_layer", "attempted_trees",
                               "attempted_layers"]
_TreeEnsembleStatsOutput = _collections.namedtuple(
    "TreeEnsembleStats", _tree_ensemble_stats_outputs)


def tree_ensemble_stats(tree_ensemble_handle, stamp_token, name=None):
  r"""Retrieves stats related to the tree ensemble.

  Args:
    tree_ensemble_handle: A `Tensor` of type `resource`.
      Handle to the ensemble variable.
    stamp_token: A `Tensor` of type `int64`.
      Stamp token for validating operation consistency.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (num_trees, num_layers, active_tree, active_layer, attempted_trees, attempted_layers).

    num_trees: A `Tensor` of type `int64`. Scalar indicating the number of finalized trees in the ensemble.
    num_layers: A `Tensor` of type `int64`. Scalar indicating the number of layers in the ensemble.
    active_tree: A `Tensor` of type `int64`. Scalar indicating the active tree being trained.
    active_layer: A `Tensor` of type `int64`. Scalar indicating the active layer being trained.
    attempted_trees: A `Tensor` of type `int64`.
    attempted_layers: A `Tensor` of type `int64`.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "TreeEnsembleStats", tree_ensemble_handle=tree_ensemble_handle,
        stamp_token=stamp_token, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = None
  else:
    tree_ensemble_handle = _ops.convert_to_tensor(tree_ensemble_handle, _dtypes.resource)
    stamp_token = _ops.convert_to_tensor(stamp_token, _dtypes.int64)
    _inputs_flat = [tree_ensemble_handle, stamp_token]
    _attrs = None
    _result = _execute.execute(b"TreeEnsembleStats", 6, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "TreeEnsembleStats", _inputs_flat, _attrs, _result, name)
  _result = _TreeEnsembleStatsOutput._make(_result)
  return _result

_ops.RegisterShape("TreeEnsembleStats")(None)

def _InitOpDefLibrary(op_list_proto_bytes):
  op_list = _op_def_pb2.OpList()
  op_list.ParseFromString(op_list_proto_bytes)
  _op_def_registry.register_op_list(op_list)
  op_def_lib = _op_def_library.OpDefLibrary()
  op_def_lib.add_op_list(op_list)
  return op_def_lib
# op {
#   name: "CenterTreeEnsembleBias"
#   input_arg {
#     name: "tree_ensemble_handle"
#     type: DT_RESOURCE
#   }
#   input_arg {
#     name: "stamp_token"
#     type: DT_INT64
#   }
#   input_arg {
#     name: "next_stamp_token"
#     type: DT_INT64
#   }
#   input_arg {
#     name: "delta_updates"
#     type: DT_FLOAT
#   }
#   output_arg {
#     name: "continue_centering"
#     type: DT_BOOL
#   }
#   attr {
#     name: "learner_config"
#     type: "string"
#   }
#   attr {
#     name: "centering_epsilon"
#     type: "float"
#     default_value {
#       f: 0.01
#     }
#   }
#   is_stateful: true
# }
# op {
#   name: "GrowTreeEnsemble"
#   input_arg {
#     name: "tree_ensemble_handle"
#     type: DT_RESOURCE
#   }
#   input_arg {
#     name: "stamp_token"
#     type: DT_INT64
#   }
#   input_arg {
#     name: "next_stamp_token"
#     type: DT_INT64
#   }
#   input_arg {
#     name: "learning_rate"
#     type: DT_FLOAT
#   }
#   input_arg {
#     name: "dropout_seed"
#     type: DT_INT64
#   }
#   input_arg {
#     name: "partition_ids"
#     type: DT_INT32
#     number_attr: "num_handlers"
#   }
#   input_arg {
#     name: "gains"
#     type: DT_FLOAT
#     number_attr: "num_handlers"
#   }
#   input_arg {
#     name: "splits"
#     type: DT_STRING
#     number_attr: "num_handlers"
#   }
#   attr {
#     name: "learner_config"
#     type: "string"
#   }
#   attr {
#     name: "num_handlers"
#     type: "int"
#     has_minimum: true
#   }
#   attr {
#     name: "center_bias"
#     type: "bool"
#   }
#   is_stateful: true
# }
# op {
#   name: "TreeEnsembleStats"
#   input_arg {
#     name: "tree_ensemble_handle"
#     type: DT_RESOURCE
#   }
#   input_arg {
#     name: "stamp_token"
#     type: DT_INT64
#   }
#   output_arg {
#     name: "num_trees"
#     type: DT_INT64
#   }
#   output_arg {
#     name: "num_layers"
#     type: DT_INT64
#   }
#   output_arg {
#     name: "active_tree"
#     type: DT_INT64
#   }
#   output_arg {
#     name: "active_layer"
#     type: DT_INT64
#   }
#   output_arg {
#     name: "attempted_trees"
#     type: DT_INT64
#   }
#   output_arg {
#     name: "attempted_layers"
#     type: DT_INT64
#   }
#   is_stateful: true
# }
_op_def_lib = _InitOpDefLibrary(b"\n\304\001\n\026CenterTreeEnsembleBias\022\030\n\024tree_ensemble_handle\030\024\022\017\n\013stamp_token\030\t\022\024\n\020next_stamp_token\030\t\022\021\n\rdelta_updates\030\001\032\026\n\022continue_centering\030\n\"\030\n\016learner_config\022\006string\"!\n\021centering_epsilon\022\005float\032\005%\n\327#<\210\001\001\n\225\002\n\020GrowTreeEnsemble\022\030\n\024tree_ensemble_handle\030\024\022\017\n\013stamp_token\030\t\022\024\n\020next_stamp_token\030\t\022\021\n\rlearning_rate\030\001\022\020\n\014dropout_seed\030\t\022\037\n\rpartition_ids\030\003*\014num_handlers\022\027\n\005gains\030\001*\014num_handlers\022\030\n\006splits\030\007*\014num_handlers\"\030\n\016learner_config\022\006string\"\025\n\014num_handlers\022\003int(\001\"\023\n\013center_bias\022\004bool\210\001\001\n\256\001\n\021TreeEnsembleStats\022\030\n\024tree_ensemble_handle\030\024\022\017\n\013stamp_token\030\t\032\r\n\tnum_trees\030\t\032\016\n\nnum_layers\030\t\032\017\n\013active_tree\030\t\032\020\n\014active_layer\030\t\032\023\n\017attempted_trees\030\t\032\024\n\020attempted_layers\030\t\210\001\001")
