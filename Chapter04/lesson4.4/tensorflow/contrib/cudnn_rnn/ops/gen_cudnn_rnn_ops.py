"""Python wrappers around TensorFlow ops.

This file is MACHINE GENERATED! Do not edit.
Original C++ source file: cudnn_rnn_ops.cc
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


_cudnn_rnn_outputs = ["output", "output_h", "output_c", "reserve_space"]
_CudnnRNNOutput = _collections.namedtuple(
    "CudnnRNN", _cudnn_rnn_outputs)


def cudnn_rnn(input, input_h, input_c, params, rnn_mode="lstm", input_mode="linear_input", direction="unidirectional", dropout=0, seed=0, seed2=0, is_training=True, name=None):
  r"""Computes the RNN from the input and initial states, with respect to the params

  buffer.

  Args:
    input: A `Tensor`. Must be one of the following types: `float32`, `float64`.
      a 3-D tensor with the shape of [seq_length, batch_size, input_size].
    input_h: A `Tensor`. Must have the same type as `input`.
      a 3-D tensor with the shape of [num_layer * dir, batch_size,
      num_units].
    input_c: A `Tensor`. Must have the same type as `input`.
      For LSTM, a 3-D tensor with the shape of
      [num_layer * dir, batch, num_units]. For other models, it is ignored.
    params: A `Tensor`. Must have the same type as `input`.
      a 1-D tensor that contains the weights and biases in an opaque layout.
      The size must be created through CudnnRNNParamsSize, and initialized
      separately. Note that they might not be compatible across different
      generations. So it is a good idea to save and restore
    rnn_mode: An optional `string` from: `"rnn_relu", "rnn_tanh", "lstm", "gru"`. Defaults to `"lstm"`.
      Indicates the type of the RNN model.
    input_mode: An optional `string` from: `"linear_input", "skip_input", "auto_select"`. Defaults to `"linear_input"`.
      Indicate whether there is a linear projection between the input and
      The actual computation before the first layer. 'skip_input' is only allowed
      when input_size == num_units; 'auto_select' implies 'skip_input' when
      input_size == num_units; otherwise, it implies 'linear_input'.
    direction: An optional `string` from: `"unidirectional", "bidirectional"`. Defaults to `"unidirectional"`.
      Indicates whether a bidirectional model will be used.
      dir = (direction == bidirectional) ? 2 : 1
    dropout: An optional `float`. Defaults to `0`.
      dropout probability. When set to 0., dropout is disabled.
    seed: An optional `int`. Defaults to `0`.
      the 1st part of a seed to initialize dropout.
    seed2: An optional `int`. Defaults to `0`.
      the 2nd part of a seed to initialize dropout.
    is_training: An optional `bool`. Defaults to `True`.
      Indicates whether this operation is used for inferenece or
      training.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (output, output_h, output_c, reserve_space).

    output: A `Tensor`. Has the same type as `input`. a 3-D tensor with the shape of [seq_length, batch_size,
      dir * num_units].
    output_h: A `Tensor`. Has the same type as `input`. the same shape has input_h.
    output_c: A `Tensor`. Has the same type as `input`. the same shape as input_c for LSTM. An empty tensor for other models.
    reserve_space: A `Tensor`. Has the same type as `input`. an opaque tensor that can be used in backprop calculation. It
      is only produced if is_training is false.
  """
  if rnn_mode is None:
    rnn_mode = "lstm"
  rnn_mode = _execute.make_str(rnn_mode, "rnn_mode")
  if input_mode is None:
    input_mode = "linear_input"
  input_mode = _execute.make_str(input_mode, "input_mode")
  if direction is None:
    direction = "unidirectional"
  direction = _execute.make_str(direction, "direction")
  if dropout is None:
    dropout = 0
  dropout = _execute.make_float(dropout, "dropout")
  if seed is None:
    seed = 0
  seed = _execute.make_int(seed, "seed")
  if seed2 is None:
    seed2 = 0
  seed2 = _execute.make_int(seed2, "seed2")
  if is_training is None:
    is_training = True
  is_training = _execute.make_bool(is_training, "is_training")
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "CudnnRNN", input=input, input_h=input_h, input_c=input_c,
        params=params, rnn_mode=rnn_mode, input_mode=input_mode,
        direction=direction, dropout=dropout, seed=seed, seed2=seed2,
        is_training=is_training, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("T", _op.get_attr("T"), "rnn_mode", _op.get_attr("rnn_mode"),
              "input_mode", _op.get_attr("input_mode"), "direction",
              _op.get_attr("direction"), "dropout", _op.get_attr("dropout"),
              "seed", _op.get_attr("seed"), "seed2", _op.get_attr("seed2"),
              "is_training", _op.get_attr("is_training"))
  else:
    _attr_T, _inputs_T = _execute.args_to_matching_eager([input, input_h, input_c, params], _ctx)
    (input, input_h, input_c, params) = _inputs_T
    _attr_T = _attr_T.as_datatype_enum
    _inputs_flat = [input, input_h, input_c, params]
    _attrs = ("T", _attr_T, "rnn_mode", rnn_mode, "input_mode", input_mode,
              "direction", direction, "dropout", dropout, "seed", seed,
              "seed2", seed2, "is_training", is_training)
    _result = _execute.execute(b"CudnnRNN", 4, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "CudnnRNN", _inputs_flat, _attrs, _result, name)
  _result = _CudnnRNNOutput._make(_result)
  return _result

_ops.RegisterShape("CudnnRNN")(None)


_cudnn_rnn_backprop_outputs = ["input_backprop", "input_h_backprop",
                              "input_c_backprop", "params_backprop"]
_CudnnRNNBackpropOutput = _collections.namedtuple(
    "CudnnRNNBackprop", _cudnn_rnn_backprop_outputs)


def cudnn_rnn_backprop(input, input_h, input_c, params, output, output_h, output_c, output_backprop, output_h_backprop, output_c_backprop, reserve_space, rnn_mode="lstm", input_mode="linear_input", direction="unidirectional", dropout=0, seed=0, seed2=0, name=None):
  r"""Compute the backprop of both data and weights in a RNN.

  Args:
    input: A `Tensor`. Must be one of the following types: `float32`, `float64`.
      a 3-D tensor with the shape of [seq_length, batch_size, input_size].
    input_h: A `Tensor`. Must have the same type as `input`.
      a 3-D tensor with the shape of [num_layer * dir, batch_size,
      num_units].
    input_c: A `Tensor`. Must have the same type as `input`.
      For LSTM, a 3-D tensor with the shape of
      [num_layer * dir, batch, num_units]. For other models, it is ignored.
    params: A `Tensor`. Must have the same type as `input`.
      a 1-D tensor that contains the weights and biases in an opaque layout.
      The size must be created through CudnnRNNParamsSize, and initialized
      separately. Note that they might not be compatible across different
      generations. So it is a good idea to save and restore
    output: A `Tensor`. Must have the same type as `input`.
      a 3-D tensor with the shape of [seq_length, batch_size,
      dir * num_units].
    output_h: A `Tensor`. Must have the same type as `input`.
      the same shape has input_h.
    output_c: A `Tensor`. Must have the same type as `input`.
      the same shape as input_c for LSTM. An empty tensor for other models.
    output_backprop: A `Tensor`. Must have the same type as `input`.
      A 3-D tensor with the same shape as output in the forward pass.
    output_h_backprop: A `Tensor`. Must have the same type as `input`.
      A 3-D tensor with the same shape as output_h in the forward
      pass.
    output_c_backprop: A `Tensor`. Must have the same type as `input`.
      A 3-D tensor with the same shape as output_c in the forward
      pass.
    reserve_space: A `Tensor`. Must have the same type as `input`.
      The same reserve_space produced in for forward operation.
    rnn_mode: An optional `string` from: `"rnn_relu", "rnn_tanh", "lstm", "gru"`. Defaults to `"lstm"`.
      Indicates the type of the RNN model.
    input_mode: An optional `string` from: `"linear_input", "skip_input", "auto_select"`. Defaults to `"linear_input"`.
      Indicate whether there is a linear projection between the input and
      The actual computation before the first layer. 'skip_input' is only allowed
      when input_size == num_units; 'auto_select' implies 'skip_input' when
      input_size == num_units; otherwise, it implies 'linear_input'.
    direction: An optional `string` from: `"unidirectional", "bidirectional"`. Defaults to `"unidirectional"`.
      Indicates whether a bidirectional model will be used.
      dir = (direction == bidirectional) ? 2 : 1
    dropout: An optional `float`. Defaults to `0`.
      dropout probability. When set to 0., dropout is disabled.
    seed: An optional `int`. Defaults to `0`.
      the 1st part of a seed to initialize dropout.
    seed2: An optional `int`. Defaults to `0`.
      the 2nd part of a seed to initialize dropout.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (input_backprop, input_h_backprop, input_c_backprop, params_backprop).

    input_backprop: A `Tensor`. Has the same type as `input`. The backprop to input in the forward pass. Has the same shape
      as input.
    input_h_backprop: A `Tensor`. Has the same type as `input`. The backprop to input_h in the forward pass. Has the same
      shape as input_h.
    input_c_backprop: A `Tensor`. Has the same type as `input`. The backprop to input_c in the forward pass. Has the same
      shape as input_c.
    params_backprop: A `Tensor`. Has the same type as `input`. The backprop to the params buffer in the forward pass. Has the
      same shape as params.
  """
  if rnn_mode is None:
    rnn_mode = "lstm"
  rnn_mode = _execute.make_str(rnn_mode, "rnn_mode")
  if input_mode is None:
    input_mode = "linear_input"
  input_mode = _execute.make_str(input_mode, "input_mode")
  if direction is None:
    direction = "unidirectional"
  direction = _execute.make_str(direction, "direction")
  if dropout is None:
    dropout = 0
  dropout = _execute.make_float(dropout, "dropout")
  if seed is None:
    seed = 0
  seed = _execute.make_int(seed, "seed")
  if seed2 is None:
    seed2 = 0
  seed2 = _execute.make_int(seed2, "seed2")
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "CudnnRNNBackprop", input=input, input_h=input_h, input_c=input_c,
        params=params, output=output, output_h=output_h, output_c=output_c,
        output_backprop=output_backprop, output_h_backprop=output_h_backprop,
        output_c_backprop=output_c_backprop, reserve_space=reserve_space,
        rnn_mode=rnn_mode, input_mode=input_mode, direction=direction,
        dropout=dropout, seed=seed, seed2=seed2, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("T", _op.get_attr("T"), "rnn_mode", _op.get_attr("rnn_mode"),
              "input_mode", _op.get_attr("input_mode"), "direction",
              _op.get_attr("direction"), "dropout", _op.get_attr("dropout"),
              "seed", _op.get_attr("seed"), "seed2", _op.get_attr("seed2"))
  else:
    _attr_T, _inputs_T = _execute.args_to_matching_eager([input, input_h, input_c, params, output, output_h, output_c, output_backprop, output_h_backprop, output_c_backprop, reserve_space], _ctx)
    (input, input_h, input_c, params, output, output_h, output_c, output_backprop, output_h_backprop, output_c_backprop, reserve_space) = _inputs_T
    _attr_T = _attr_T.as_datatype_enum
    _inputs_flat = [input, input_h, input_c, params, output, output_h, output_c, output_backprop, output_h_backprop, output_c_backprop, reserve_space]
    _attrs = ("T", _attr_T, "rnn_mode", rnn_mode, "input_mode", input_mode,
              "direction", direction, "dropout", dropout, "seed", seed,
              "seed2", seed2)
    _result = _execute.execute(b"CudnnRNNBackprop", 4, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "CudnnRNNBackprop", _inputs_flat, _attrs, _result, name)
  _result = _CudnnRNNBackpropOutput._make(_result)
  return _result

_ops.RegisterShape("CudnnRNNBackprop")(None)


def cudnn_rnn_canonical_to_params(num_layers, num_units, input_size, weights, biases, rnn_mode="lstm", input_mode="linear_input", direction="unidirectional", dropout=0, seed=0, seed2=0, name=None):
  r"""Writes a set of weights into the opaque params buffer so they can be used in

  upcoming training or inferences.

  Args:
    num_layers: A `Tensor` of type `int32`.
      Specifies the number of layers in the RNN model.
    num_units: A `Tensor` of type `int32`.
      Specifies the size of the hidden state.
    input_size: A `Tensor` of type `int32`.
      Specifies the size of the input state.
    weights: A list of at least 1 `Tensor` objects with the same type in: `float32`, `float64`.
      the canonical form of weights that can be used for saving
      and restoration. They are more likely to be compatible across different
      generations.
    biases: A list with the same length as `weights` of `Tensor` objects with the same type as `weights`.
      the canonical form of biases that can be used for saving
          and restoration. They are more likely to be compatible across different
          generations.

      Note that the params buffer may not be compatible across different GPUs. So any
      save and restoration should be converted to and from the canonical weights and
      biases.
    rnn_mode: An optional `string` from: `"rnn_relu", "rnn_tanh", "lstm", "gru"`. Defaults to `"lstm"`.
      Indicates the type of the RNN model.
    input_mode: An optional `string` from: `"linear_input", "skip_input", "auto_select"`. Defaults to `"linear_input"`.
      Indicate whether there is a linear projection between the input and
      The actual computation before the first layer. 'skip_input' is only allowed
      when input_size == num_units; 'auto_select' implies 'skip_input' when
      input_size == num_units; otherwise, it implies 'linear_input'.
    direction: An optional `string` from: `"unidirectional", "bidirectional"`. Defaults to `"unidirectional"`.
      Indicates whether a bidirectional model will be used.
      dir = (direction == bidirectional) ? 2 : 1
    dropout: An optional `float`. Defaults to `0`.
      dropout probability. When set to 0., dropout is disabled.
    seed: An optional `int`. Defaults to `0`.
      the 1st part of a seed to initialize dropout.
    seed2: An optional `int`. Defaults to `0`.
      the 2nd part of a seed to initialize dropout.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `weights`.
  """
  if not isinstance(weights, (list, tuple)):
    raise TypeError(
        "Expected list for 'weights' argument to "
        "'cudnn_rnn_canonical_to_params' Op, not %r." % weights)
  _attr_num_params = len(weights)
  if not isinstance(biases, (list, tuple)):
    raise TypeError(
        "Expected list for 'biases' argument to "
        "'cudnn_rnn_canonical_to_params' Op, not %r." % biases)
  if len(biases) != _attr_num_params:
    raise ValueError(
        "List argument 'biases' to 'cudnn_rnn_canonical_to_params' Op with length %d "
        "must match length %d of argument 'weights'." %
        (len(biases), _attr_num_params))
  if rnn_mode is None:
    rnn_mode = "lstm"
  rnn_mode = _execute.make_str(rnn_mode, "rnn_mode")
  if input_mode is None:
    input_mode = "linear_input"
  input_mode = _execute.make_str(input_mode, "input_mode")
  if direction is None:
    direction = "unidirectional"
  direction = _execute.make_str(direction, "direction")
  if dropout is None:
    dropout = 0
  dropout = _execute.make_float(dropout, "dropout")
  if seed is None:
    seed = 0
  seed = _execute.make_int(seed, "seed")
  if seed2 is None:
    seed2 = 0
  seed2 = _execute.make_int(seed2, "seed2")
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "CudnnRNNCanonicalToParams", num_layers=num_layers,
        num_units=num_units, input_size=input_size, weights=weights,
        biases=biases, rnn_mode=rnn_mode, input_mode=input_mode,
        direction=direction, dropout=dropout, seed=seed, seed2=seed2,
        name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("T", _op.get_attr("T"), "num_params",
              _op.get_attr("num_params"), "rnn_mode",
              _op.get_attr("rnn_mode"), "input_mode",
              _op.get_attr("input_mode"), "direction",
              _op.get_attr("direction"), "dropout", _op.get_attr("dropout"),
              "seed", _op.get_attr("seed"), "seed2", _op.get_attr("seed2"))
  else:
    _attr_T, _inputs_T = _execute.args_to_matching_eager(list(weights) + list(biases), _ctx)
    _inputs_T = [_inputs_T[:_attr_num_params]] + _inputs_T[_attr_num_params:]
    _inputs_T = _inputs_T[:1] + [_inputs_T[1:]]
    (weights, biases) = _inputs_T
    _attr_T = _attr_T.as_datatype_enum
    num_layers = _ops.convert_to_tensor(num_layers, _dtypes.int32)
    num_units = _ops.convert_to_tensor(num_units, _dtypes.int32)
    input_size = _ops.convert_to_tensor(input_size, _dtypes.int32)
    _inputs_flat = [num_layers, num_units, input_size] + list(weights) + list(biases)
    _attrs = ("T", _attr_T, "num_params", _attr_num_params, "rnn_mode",
              rnn_mode, "input_mode", input_mode, "direction", direction,
              "dropout", dropout, "seed", seed, "seed2", seed2)
    _result = _execute.execute(b"CudnnRNNCanonicalToParams", 1,
                               inputs=_inputs_flat, attrs=_attrs, ctx=_ctx,
                               name=name)
  _execute.record_gradient(
      "CudnnRNNCanonicalToParams", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result

_ops.RegisterShape("CudnnRNNCanonicalToParams")(None)


def cudnn_rnn_params_size(num_layers, num_units, input_size, T, S, rnn_mode="lstm", input_mode="linear_input", direction="unidirectional", dropout=0, seed=0, seed2=0, name=None):
  r"""Return the params size that can be used by the Cudnn RNN model. Subsequent

  weight allocation and initialization should use this size.

  Args:
    num_layers: A `Tensor` of type `int32`.
      Specifies the number of layers in the RNN model.
    num_units: A `Tensor` of type `int32`.
      Specifies the size of the hidden state.
    input_size: A `Tensor` of type `int32`.
      Specifies the size of the input state.
    T: A `tf.DType` from: `tf.float32, tf.float64`.
    S: A `tf.DType` from: `tf.int32, tf.int64`.
    rnn_mode: An optional `string` from: `"rnn_relu", "rnn_tanh", "lstm", "gru"`. Defaults to `"lstm"`.
      Indicates the type of the RNN model.
    input_mode: An optional `string` from: `"linear_input", "skip_input", "auto_select"`. Defaults to `"linear_input"`.
      Indicate whether there is a linear projection between the input and
      The actual computation before the first layer. 'skip_input' is only allowed
      when input_size == num_units; 'auto_select' implies 'skip_input' when
      input_size == num_units; otherwise, it implies 'linear_input'.
    direction: An optional `string` from: `"unidirectional", "bidirectional"`. Defaults to `"unidirectional"`.
      Indicates whether a bidirectional model will be used.
      dir = (direction == bidirectional) ? 2 : 1
    dropout: An optional `float`. Defaults to `0`.
      dropout probability. When set to 0., dropout is disabled.
    seed: An optional `int`. Defaults to `0`.
      the 1st part of a seed to initialize dropout.
    seed2: An optional `int`. Defaults to `0`.
      the 2nd part of a seed to initialize dropout.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `S`.
    The size of the params buffer that should be allocated and
        initialized for this RNN model. Note that this params buffer may not be
        compatible across GPUs. Please use CudnnRNNParamsWeights and
        CudnnRNNParamsBiases to save and restore them in a way that is compatible
        across different runs.

    Note that the params buffer may not be compatible across different GPUs. So any
    save and restoration should be converted to and from the canonical weights and
    biases.
  """
  T = _execute.make_type(T, "T")
  S = _execute.make_type(S, "S")
  if rnn_mode is None:
    rnn_mode = "lstm"
  rnn_mode = _execute.make_str(rnn_mode, "rnn_mode")
  if input_mode is None:
    input_mode = "linear_input"
  input_mode = _execute.make_str(input_mode, "input_mode")
  if direction is None:
    direction = "unidirectional"
  direction = _execute.make_str(direction, "direction")
  if dropout is None:
    dropout = 0
  dropout = _execute.make_float(dropout, "dropout")
  if seed is None:
    seed = 0
  seed = _execute.make_int(seed, "seed")
  if seed2 is None:
    seed2 = 0
  seed2 = _execute.make_int(seed2, "seed2")
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "CudnnRNNParamsSize", num_layers=num_layers, num_units=num_units,
        input_size=input_size, T=T, S=S, rnn_mode=rnn_mode,
        input_mode=input_mode, direction=direction, dropout=dropout,
        seed=seed, seed2=seed2, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("T", _op.get_attr("T"), "S", _op.get_attr("S"), "rnn_mode",
              _op.get_attr("rnn_mode"), "input_mode",
              _op.get_attr("input_mode"), "direction",
              _op.get_attr("direction"), "dropout", _op.get_attr("dropout"),
              "seed", _op.get_attr("seed"), "seed2", _op.get_attr("seed2"))
  else:
    num_layers = _ops.convert_to_tensor(num_layers, _dtypes.int32)
    num_units = _ops.convert_to_tensor(num_units, _dtypes.int32)
    input_size = _ops.convert_to_tensor(input_size, _dtypes.int32)
    _inputs_flat = [num_layers, num_units, input_size]
    _attrs = ("T", T, "S", S, "rnn_mode", rnn_mode, "input_mode", input_mode,
              "direction", direction, "dropout", dropout, "seed", seed,
              "seed2", seed2)
    _result = _execute.execute(b"CudnnRNNParamsSize", 1, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "CudnnRNNParamsSize", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result

_ops.RegisterShape("CudnnRNNParamsSize")(None)


_cudnn_rnn_params_to_canonical_outputs = ["weights", "biases"]
_CudnnRNNParamsToCanonicalOutput = _collections.namedtuple(
    "CudnnRNNParamsToCanonical", _cudnn_rnn_params_to_canonical_outputs)


def cudnn_rnn_params_to_canonical(num_layers, num_units, input_size, params, num_params, rnn_mode="lstm", input_mode="linear_input", direction="unidirectional", dropout=0, seed=0, seed2=0, name=None):
  r"""Retrieves a set of weights from the opaque params buffer that can be saved and

  restored in a way compatible with future runs.

  Args:
    num_layers: A `Tensor` of type `int32`.
      Specifies the number of layers in the RNN model.
    num_units: A `Tensor` of type `int32`.
      Specifies the size of the hidden state.
    input_size: A `Tensor` of type `int32`.
      Specifies the size of the input state.

      Note that the params buffer may not be compatible across different GPUs. So any
      save and restoration should be converted to and from the canonical weights and
      biases.
    params: A `Tensor`. Must be one of the following types: `float32`, `float64`.
    num_params: An `int` that is `>= 1`.
      number of parameter sets for all layers.
      Each layer may contain multiple parameter sets, with each set consisting of
      a weight matrix and a bias vector.
    rnn_mode: An optional `string` from: `"rnn_relu", "rnn_tanh", "lstm", "gru"`. Defaults to `"lstm"`.
      Indicates the type of the RNN model.
    input_mode: An optional `string` from: `"linear_input", "skip_input", "auto_select"`. Defaults to `"linear_input"`.
      Indicate whether there is a linear projection between the input and
      The actual computation before the first layer. 'skip_input' is only allowed
      when input_size == num_units; 'auto_select' implies 'skip_input' when
      input_size == num_units; otherwise, it implies 'linear_input'.
    direction: An optional `string` from: `"unidirectional", "bidirectional"`. Defaults to `"unidirectional"`.
      Indicates whether a bidirectional model will be used.
      dir = (direction == bidirectional) ? 2 : 1
    dropout: An optional `float`. Defaults to `0`.
      dropout probability. When set to 0., dropout is disabled.
    seed: An optional `int`. Defaults to `0`.
      the 1st part of a seed to initialize dropout.
    seed2: An optional `int`. Defaults to `0`.
      the 2nd part of a seed to initialize dropout.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (weights, biases).

    weights: A list of `num_params` `Tensor` objects with the same type as `params`. the canonical form of weights that can be used for saving
      and restoration. They are more likely to be compatible across different
      generations.
    biases: A list of `num_params` `Tensor` objects with the same type as `params`. the canonical form of biases that can be used for saving
      and restoration. They are more likely to be compatible across different
      generations.
  """
  num_params = _execute.make_int(num_params, "num_params")
  if rnn_mode is None:
    rnn_mode = "lstm"
  rnn_mode = _execute.make_str(rnn_mode, "rnn_mode")
  if input_mode is None:
    input_mode = "linear_input"
  input_mode = _execute.make_str(input_mode, "input_mode")
  if direction is None:
    direction = "unidirectional"
  direction = _execute.make_str(direction, "direction")
  if dropout is None:
    dropout = 0
  dropout = _execute.make_float(dropout, "dropout")
  if seed is None:
    seed = 0
  seed = _execute.make_int(seed, "seed")
  if seed2 is None:
    seed2 = 0
  seed2 = _execute.make_int(seed2, "seed2")
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "CudnnRNNParamsToCanonical", num_layers=num_layers,
        num_units=num_units, input_size=input_size, params=params,
        num_params=num_params, rnn_mode=rnn_mode, input_mode=input_mode,
        direction=direction, dropout=dropout, seed=seed, seed2=seed2,
        name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("T", _op.get_attr("T"), "num_params",
              _op.get_attr("num_params"), "rnn_mode",
              _op.get_attr("rnn_mode"), "input_mode",
              _op.get_attr("input_mode"), "direction",
              _op.get_attr("direction"), "dropout", _op.get_attr("dropout"),
              "seed", _op.get_attr("seed"), "seed2", _op.get_attr("seed2"))
  else:
    _attr_T, (params,) = _execute.args_to_matching_eager([params], _ctx)
    _attr_T = _attr_T.as_datatype_enum
    num_layers = _ops.convert_to_tensor(num_layers, _dtypes.int32)
    num_units = _ops.convert_to_tensor(num_units, _dtypes.int32)
    input_size = _ops.convert_to_tensor(input_size, _dtypes.int32)
    _inputs_flat = [num_layers, num_units, input_size, params]
    _attrs = ("T", _attr_T, "num_params", num_params, "rnn_mode", rnn_mode,
              "input_mode", input_mode, "direction", direction, "dropout",
              dropout, "seed", seed, "seed2", seed2)
    _result = _execute.execute(b"CudnnRNNParamsToCanonical", num_params +
                               num_params, inputs=_inputs_flat, attrs=_attrs,
                               ctx=_ctx, name=name)
  _execute.record_gradient(
      "CudnnRNNParamsToCanonical", _inputs_flat, _attrs, _result, name)
  _result = [_result[:num_params]] + _result[num_params:]
  _result = _result[:1] + [_result[1:]]
  _result = _CudnnRNNParamsToCanonicalOutput._make(_result)
  return _result

_ops.RegisterShape("CudnnRNNParamsToCanonical")(None)

def _InitOpDefLibrary(op_list_proto_bytes):
  op_list = _op_def_pb2.OpList()
  op_list.ParseFromString(op_list_proto_bytes)
  _op_def_registry.register_op_list(op_list)
  op_def_lib = _op_def_library.OpDefLibrary()
  op_def_lib.add_op_list(op_list)
  return op_def_lib
# op {
#   name: "CudnnRNN"
#   input_arg {
#     name: "input"
#     type_attr: "T"
#   }
#   input_arg {
#     name: "input_h"
#     type_attr: "T"
#   }
#   input_arg {
#     name: "input_c"
#     type_attr: "T"
#   }
#   input_arg {
#     name: "params"
#     type_attr: "T"
#   }
#   output_arg {
#     name: "output"
#     type_attr: "T"
#   }
#   output_arg {
#     name: "output_h"
#     type_attr: "T"
#   }
#   output_arg {
#     name: "output_c"
#     type_attr: "T"
#   }
#   output_arg {
#     name: "reserve_space"
#     type_attr: "T"
#   }
#   attr {
#     name: "T"
#     type: "type"
#     allowed_values {
#       list {
#         type: DT_FLOAT
#         type: DT_DOUBLE
#       }
#     }
#   }
#   attr {
#     name: "rnn_mode"
#     type: "string"
#     default_value {
#       s: "lstm"
#     }
#     allowed_values {
#       list {
#         s: "rnn_relu"
#         s: "rnn_tanh"
#         s: "lstm"
#         s: "gru"
#       }
#     }
#   }
#   attr {
#     name: "input_mode"
#     type: "string"
#     default_value {
#       s: "linear_input"
#     }
#     allowed_values {
#       list {
#         s: "linear_input"
#         s: "skip_input"
#         s: "auto_select"
#       }
#     }
#   }
#   attr {
#     name: "direction"
#     type: "string"
#     default_value {
#       s: "unidirectional"
#     }
#     allowed_values {
#       list {
#         s: "unidirectional"
#         s: "bidirectional"
#       }
#     }
#   }
#   attr {
#     name: "dropout"
#     type: "float"
#     default_value {
#       f: 0
#     }
#   }
#   attr {
#     name: "seed"
#     type: "int"
#     default_value {
#       i: 0
#     }
#   }
#   attr {
#     name: "seed2"
#     type: "int"
#     default_value {
#       i: 0
#     }
#   }
#   attr {
#     name: "is_training"
#     type: "bool"
#     default_value {
#       b: true
#     }
#   }
#   is_stateful: true
# }
# op {
#   name: "CudnnRNNBackprop"
#   input_arg {
#     name: "input"
#     type_attr: "T"
#   }
#   input_arg {
#     name: "input_h"
#     type_attr: "T"
#   }
#   input_arg {
#     name: "input_c"
#     type_attr: "T"
#   }
#   input_arg {
#     name: "params"
#     type_attr: "T"
#   }
#   input_arg {
#     name: "output"
#     type_attr: "T"
#   }
#   input_arg {
#     name: "output_h"
#     type_attr: "T"
#   }
#   input_arg {
#     name: "output_c"
#     type_attr: "T"
#   }
#   input_arg {
#     name: "output_backprop"
#     type_attr: "T"
#   }
#   input_arg {
#     name: "output_h_backprop"
#     type_attr: "T"
#   }
#   input_arg {
#     name: "output_c_backprop"
#     type_attr: "T"
#   }
#   input_arg {
#     name: "reserve_space"
#     type_attr: "T"
#   }
#   output_arg {
#     name: "input_backprop"
#     type_attr: "T"
#   }
#   output_arg {
#     name: "input_h_backprop"
#     type_attr: "T"
#   }
#   output_arg {
#     name: "input_c_backprop"
#     type_attr: "T"
#   }
#   output_arg {
#     name: "params_backprop"
#     type_attr: "T"
#   }
#   attr {
#     name: "T"
#     type: "type"
#     allowed_values {
#       list {
#         type: DT_FLOAT
#         type: DT_DOUBLE
#       }
#     }
#   }
#   attr {
#     name: "rnn_mode"
#     type: "string"
#     default_value {
#       s: "lstm"
#     }
#     allowed_values {
#       list {
#         s: "rnn_relu"
#         s: "rnn_tanh"
#         s: "lstm"
#         s: "gru"
#       }
#     }
#   }
#   attr {
#     name: "input_mode"
#     type: "string"
#     default_value {
#       s: "linear_input"
#     }
#     allowed_values {
#       list {
#         s: "linear_input"
#         s: "skip_input"
#         s: "auto_select"
#       }
#     }
#   }
#   attr {
#     name: "direction"
#     type: "string"
#     default_value {
#       s: "unidirectional"
#     }
#     allowed_values {
#       list {
#         s: "unidirectional"
#         s: "bidirectional"
#       }
#     }
#   }
#   attr {
#     name: "dropout"
#     type: "float"
#     default_value {
#       f: 0
#     }
#   }
#   attr {
#     name: "seed"
#     type: "int"
#     default_value {
#       i: 0
#     }
#   }
#   attr {
#     name: "seed2"
#     type: "int"
#     default_value {
#       i: 0
#     }
#   }
#   is_stateful: true
# }
# op {
#   name: "CudnnRNNCanonicalToParams"
#   input_arg {
#     name: "num_layers"
#     type: DT_INT32
#   }
#   input_arg {
#     name: "num_units"
#     type: DT_INT32
#   }
#   input_arg {
#     name: "input_size"
#     type: DT_INT32
#   }
#   input_arg {
#     name: "weights"
#     type_attr: "T"
#     number_attr: "num_params"
#   }
#   input_arg {
#     name: "biases"
#     type_attr: "T"
#     number_attr: "num_params"
#   }
#   output_arg {
#     name: "params"
#     type_attr: "T"
#   }
#   attr {
#     name: "T"
#     type: "type"
#     allowed_values {
#       list {
#         type: DT_FLOAT
#         type: DT_DOUBLE
#       }
#     }
#   }
#   attr {
#     name: "num_params"
#     type: "int"
#     has_minimum: true
#     minimum: 1
#   }
#   attr {
#     name: "rnn_mode"
#     type: "string"
#     default_value {
#       s: "lstm"
#     }
#     allowed_values {
#       list {
#         s: "rnn_relu"
#         s: "rnn_tanh"
#         s: "lstm"
#         s: "gru"
#       }
#     }
#   }
#   attr {
#     name: "input_mode"
#     type: "string"
#     default_value {
#       s: "linear_input"
#     }
#     allowed_values {
#       list {
#         s: "linear_input"
#         s: "skip_input"
#         s: "auto_select"
#       }
#     }
#   }
#   attr {
#     name: "direction"
#     type: "string"
#     default_value {
#       s: "unidirectional"
#     }
#     allowed_values {
#       list {
#         s: "unidirectional"
#         s: "bidirectional"
#       }
#     }
#   }
#   attr {
#     name: "dropout"
#     type: "float"
#     default_value {
#       f: 0
#     }
#   }
#   attr {
#     name: "seed"
#     type: "int"
#     default_value {
#       i: 0
#     }
#   }
#   attr {
#     name: "seed2"
#     type: "int"
#     default_value {
#       i: 0
#     }
#   }
# }
# op {
#   name: "CudnnRNNParamsSize"
#   input_arg {
#     name: "num_layers"
#     type: DT_INT32
#   }
#   input_arg {
#     name: "num_units"
#     type: DT_INT32
#   }
#   input_arg {
#     name: "input_size"
#     type: DT_INT32
#   }
#   output_arg {
#     name: "params_size"
#     type_attr: "S"
#   }
#   attr {
#     name: "T"
#     type: "type"
#     allowed_values {
#       list {
#         type: DT_FLOAT
#         type: DT_DOUBLE
#       }
#     }
#   }
#   attr {
#     name: "S"
#     type: "type"
#     allowed_values {
#       list {
#         type: DT_INT32
#         type: DT_INT64
#       }
#     }
#   }
#   attr {
#     name: "rnn_mode"
#     type: "string"
#     default_value {
#       s: "lstm"
#     }
#     allowed_values {
#       list {
#         s: "rnn_relu"
#         s: "rnn_tanh"
#         s: "lstm"
#         s: "gru"
#       }
#     }
#   }
#   attr {
#     name: "input_mode"
#     type: "string"
#     default_value {
#       s: "linear_input"
#     }
#     allowed_values {
#       list {
#         s: "linear_input"
#         s: "skip_input"
#         s: "auto_select"
#       }
#     }
#   }
#   attr {
#     name: "direction"
#     type: "string"
#     default_value {
#       s: "unidirectional"
#     }
#     allowed_values {
#       list {
#         s: "unidirectional"
#         s: "bidirectional"
#       }
#     }
#   }
#   attr {
#     name: "dropout"
#     type: "float"
#     default_value {
#       f: 0
#     }
#   }
#   attr {
#     name: "seed"
#     type: "int"
#     default_value {
#       i: 0
#     }
#   }
#   attr {
#     name: "seed2"
#     type: "int"
#     default_value {
#       i: 0
#     }
#   }
# }
# op {
#   name: "CudnnRNNParamsToCanonical"
#   input_arg {
#     name: "num_layers"
#     type: DT_INT32
#   }
#   input_arg {
#     name: "num_units"
#     type: DT_INT32
#   }
#   input_arg {
#     name: "input_size"
#     type: DT_INT32
#   }
#   input_arg {
#     name: "params"
#     type_attr: "T"
#   }
#   output_arg {
#     name: "weights"
#     type_attr: "T"
#     number_attr: "num_params"
#   }
#   output_arg {
#     name: "biases"
#     type_attr: "T"
#     number_attr: "num_params"
#   }
#   attr {
#     name: "T"
#     type: "type"
#     allowed_values {
#       list {
#         type: DT_FLOAT
#         type: DT_DOUBLE
#       }
#     }
#   }
#   attr {
#     name: "num_params"
#     type: "int"
#     has_minimum: true
#     minimum: 1
#   }
#   attr {
#     name: "rnn_mode"
#     type: "string"
#     default_value {
#       s: "lstm"
#     }
#     allowed_values {
#       list {
#         s: "rnn_relu"
#         s: "rnn_tanh"
#         s: "lstm"
#         s: "gru"
#       }
#     }
#   }
#   attr {
#     name: "input_mode"
#     type: "string"
#     default_value {
#       s: "linear_input"
#     }
#     allowed_values {
#       list {
#         s: "linear_input"
#         s: "skip_input"
#         s: "auto_select"
#       }
#     }
#   }
#   attr {
#     name: "direction"
#     type: "string"
#     default_value {
#       s: "unidirectional"
#     }
#     allowed_values {
#       list {
#         s: "unidirectional"
#         s: "bidirectional"
#       }
#     }
#   }
#   attr {
#     name: "dropout"
#     type: "float"
#     default_value {
#       f: 0
#     }
#   }
#   attr {
#     name: "seed"
#     type: "int"
#     default_value {
#       i: 0
#     }
#   }
#   attr {
#     name: "seed2"
#     type: "int"
#     default_value {
#       i: 0
#     }
#   }
# }
_op_def_lib = _InitOpDefLibrary(b"\n\303\003\n\010CudnnRNN\022\n\n\005input\"\001T\022\014\n\007input_h\"\001T\022\014\n\007input_c\"\001T\022\013\n\006params\"\001T\032\013\n\006output\"\001T\032\r\n\010output_h\"\001T\032\r\n\010output_c\"\001T\032\022\n\rreserve_space\"\001T\"\021\n\001T\022\004type:\006\n\0042\002\001\002\"=\n\010rnn_mode\022\006string\032\006\022\004lstm:!\n\037\022\010rnn_relu\022\010rnn_tanh\022\004lstm\022\003gru\"O\n\ninput_mode\022\006string\032\016\022\014linear_input:)\n\'\022\014linear_input\022\nskip_input\022\013auto_select\"H\n\tdirection\022\006string\032\020\022\016unidirectional:!\n\037\022\016unidirectional\022\rbidirectional\"\027\n\007dropout\022\005float\032\005%\000\000\000\000\"\017\n\004seed\022\003int\032\002\030\000\"\020\n\005seed2\022\003int\032\002\030\000\"\027\n\013is_training\022\004bool\032\002(\001\210\001\001\n\321\004\n\020CudnnRNNBackprop\022\n\n\005input\"\001T\022\014\n\007input_h\"\001T\022\014\n\007input_c\"\001T\022\013\n\006params\"\001T\022\013\n\006output\"\001T\022\r\n\010output_h\"\001T\022\r\n\010output_c\"\001T\022\024\n\017output_backprop\"\001T\022\026\n\021output_h_backprop\"\001T\022\026\n\021output_c_backprop\"\001T\022\022\n\rreserve_space\"\001T\032\023\n\016input_backprop\"\001T\032\025\n\020input_h_backprop\"\001T\032\025\n\020input_c_backprop\"\001T\032\024\n\017params_backprop\"\001T\"\021\n\001T\022\004type:\006\n\0042\002\001\002\"=\n\010rnn_mode\022\006string\032\006\022\004lstm:!\n\037\022\010rnn_relu\022\010rnn_tanh\022\004lstm\022\003gru\"O\n\ninput_mode\022\006string\032\016\022\014linear_input:)\n\'\022\014linear_input\022\nskip_input\022\013auto_select\"H\n\tdirection\022\006string\032\020\022\016unidirectional:!\n\037\022\016unidirectional\022\rbidirectional\"\027\n\007dropout\022\005float\032\005%\000\000\000\000\"\017\n\004seed\022\003int\032\002\030\000\"\020\n\005seed2\022\003int\032\002\030\000\210\001\001\n\312\003\n\031CudnnRNNCanonicalToParams\022\016\n\nnum_layers\030\003\022\r\n\tnum_units\030\003\022\016\n\ninput_size\030\003\022\030\n\007weights\"\001T*\nnum_params\022\027\n\006biases\"\001T*\nnum_params\032\013\n\006params\"\001T\"\021\n\001T\022\004type:\006\n\0042\002\001\002\"\025\n\nnum_params\022\003int(\0010\001\"=\n\010rnn_mode\022\006string\032\006\022\004lstm:!\n\037\022\010rnn_relu\022\010rnn_tanh\022\004lstm\022\003gru\"O\n\ninput_mode\022\006string\032\016\022\014linear_input:)\n\'\022\014linear_input\022\nskip_input\022\013auto_select\"H\n\tdirection\022\006string\032\020\022\016unidirectional:!\n\037\022\016unidirectional\022\rbidirectional\"\027\n\007dropout\022\005float\032\005%\000\000\000\000\"\017\n\004seed\022\003int\032\002\030\000\"\020\n\005seed2\022\003int\032\002\030\000\n\221\003\n\022CudnnRNNParamsSize\022\016\n\nnum_layers\030\003\022\r\n\tnum_units\030\003\022\016\n\ninput_size\030\003\032\020\n\013params_size\"\001S\"\021\n\001T\022\004type:\006\n\0042\002\001\002\"\021\n\001S\022\004type:\006\n\0042\002\003\t\"=\n\010rnn_mode\022\006string\032\006\022\004lstm:!\n\037\022\010rnn_relu\022\010rnn_tanh\022\004lstm\022\003gru\"O\n\ninput_mode\022\006string\032\016\022\014linear_input:)\n\'\022\014linear_input\022\nskip_input\022\013auto_select\"H\n\tdirection\022\006string\032\020\022\016unidirectional:!\n\037\022\016unidirectional\022\rbidirectional\"\027\n\007dropout\022\005float\032\005%\000\000\000\000\"\017\n\004seed\022\003int\032\002\030\000\"\020\n\005seed2\022\003int\032\002\030\000\n\312\003\n\031CudnnRNNParamsToCanonical\022\016\n\nnum_layers\030\003\022\r\n\tnum_units\030\003\022\016\n\ninput_size\030\003\022\013\n\006params\"\001T\032\030\n\007weights\"\001T*\nnum_params\032\027\n\006biases\"\001T*\nnum_params\"\021\n\001T\022\004type:\006\n\0042\002\001\002\"\025\n\nnum_params\022\003int(\0010\001\"=\n\010rnn_mode\022\006string\032\006\022\004lstm:!\n\037\022\010rnn_relu\022\010rnn_tanh\022\004lstm\022\003gru\"O\n\ninput_mode\022\006string\032\016\022\014linear_input:)\n\'\022\014linear_input\022\nskip_input\022\013auto_select\"H\n\tdirection\022\006string\032\020\022\016unidirectional:!\n\037\022\016unidirectional\022\rbidirectional\"\027\n\007dropout\022\005float\032\005%\000\000\000\000\"\017\n\004seed\022\003int\032\002\030\000\"\020\n\005seed2\022\003int\032\002\030\000")
