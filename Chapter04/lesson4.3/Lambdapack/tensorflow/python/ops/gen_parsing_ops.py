"""Python wrappers around TensorFlow ops.

This file is MACHINE GENERATED! Do not edit.
Original C++ source file: parsing_ops.cc
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


def _decode_csv(records, record_defaults, field_delim=",", use_quote_delim=True, na_value="", name=None):
  r"""Convert CSV records to tensors. Each column maps to one tensor.

  RFC 4180 format is expected for the CSV records.
  (https://tools.ietf.org/html/rfc4180)
  Note that we allow leading and trailing spaces with int or float field.

  Args:
    records: A `Tensor` of type `string`.
      Each string is a record/row in the csv and all records should have
      the same format.
    record_defaults: A list of `Tensor` objects with types from: `float32`, `int32`, `int64`, `string`.
      One tensor per column of the input record, with either a
      scalar default value for that column or empty if the column is required.
    field_delim: An optional `string`. Defaults to `","`.
      char delimiter to separate fields in a record.
    use_quote_delim: An optional `bool`. Defaults to `True`.
      If false, treats double quotation marks as regular
      characters inside of the string fields (ignoring RFC 4180, Section 2,
      Bullet 5).
    na_value: An optional `string`. Defaults to `""`.
      Additional string to recognize as NA/NaN.
    name: A name for the operation (optional).

  Returns:
    A list of `Tensor` objects. Has the same type as `record_defaults`.
    Each tensor will have the same shape as records.
  """
  if field_delim is None:
    field_delim = ","
  field_delim = _execute.make_str(field_delim, "field_delim")
  if use_quote_delim is None:
    use_quote_delim = True
  use_quote_delim = _execute.make_bool(use_quote_delim, "use_quote_delim")
  if na_value is None:
    na_value = ""
  na_value = _execute.make_str(na_value, "na_value")
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "DecodeCSV", records=records, record_defaults=record_defaults,
        field_delim=field_delim, use_quote_delim=use_quote_delim,
        na_value=na_value, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("OUT_TYPE", _op.get_attr("OUT_TYPE"), "field_delim",
              _op.get_attr("field_delim"), "use_quote_delim",
              _op.get_attr("use_quote_delim"), "na_value",
              _op.get_attr("na_value"))
  else:
    _attr_OUT_TYPE, record_defaults = _execute.convert_to_mixed_eager_tensors(record_defaults, _ctx)
    _attr_OUT_TYPE = [_t.as_datatype_enum for _t in _attr_OUT_TYPE]
    records = _ops.convert_to_tensor(records, _dtypes.string)
    _inputs_flat = [records] + list(record_defaults)
    _attrs = ("OUT_TYPE", _attr_OUT_TYPE, "field_delim", field_delim,
              "use_quote_delim", use_quote_delim, "na_value", na_value)
    _result = _execute.execute(b"DecodeCSV", len(record_defaults),
                               inputs=_inputs_flat, attrs=_attrs, ctx=_ctx,
                               name=name)
  _execute.record_gradient(
      "DecodeCSV", _inputs_flat, _attrs, _result, name)
  return _result


def decode_json_example(json_examples, name=None):
  r"""Convert JSON-encoded Example records to binary protocol buffer strings.

  This op translates a tensor containing Example records, encoded using
  the [standard JSON
  mapping](https://developers.google.com/protocol-buffers/docs/proto3#json),
  into a tensor containing the same records encoded as binary protocol
  buffers. The resulting tensor can then be fed to any of the other
  Example-parsing ops.

  Args:
    json_examples: A `Tensor` of type `string`.
      Each string is a JSON object serialized according to the JSON
      mapping of the Example proto.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `string`.
    Each string is a binary Example protocol buffer corresponding
    to the respective element of `json_examples`.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "DecodeJSONExample", json_examples=json_examples, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = None
  else:
    json_examples = _ops.convert_to_tensor(json_examples, _dtypes.string)
    _inputs_flat = [json_examples]
    _attrs = None
    _result = _execute.execute(b"DecodeJSONExample", 1, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "DecodeJSONExample", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result


def decode_raw(bytes, out_type, little_endian=True, name=None):
  r"""Reinterpret the bytes of a string as a vector of numbers.

  Args:
    bytes: A `Tensor` of type `string`.
      All the elements must have the same length.
    out_type: A `tf.DType` from: `tf.half, tf.float32, tf.float64, tf.int32, tf.uint16, tf.uint8, tf.int16, tf.int8, tf.int64`.
    little_endian: An optional `bool`. Defaults to `True`.
      Whether the input `bytes` are in little-endian order.
      Ignored for `out_type` values that are stored in a single byte like
      `uint8`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `out_type`.
    A Tensor with one more dimension than the input `bytes`.  The
    added dimension will have size equal to the length of the elements
    of `bytes` divided by the number of bytes to represent `out_type`.
  """
  out_type = _execute.make_type(out_type, "out_type")
  if little_endian is None:
    little_endian = True
  little_endian = _execute.make_bool(little_endian, "little_endian")
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "DecodeRaw", bytes=bytes, out_type=out_type,
        little_endian=little_endian, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("out_type", _op.get_attr("out_type"), "little_endian",
              _op.get_attr("little_endian"))
  else:
    bytes = _ops.convert_to_tensor(bytes, _dtypes.string)
    _inputs_flat = [bytes]
    _attrs = ("out_type", out_type, "little_endian", little_endian)
    _result = _execute.execute(b"DecodeRaw", 1, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "DecodeRaw", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result


__parse_example_outputs = ["sparse_indices", "sparse_values", "sparse_shapes",
                          "dense_values"]
_ParseExampleOutput = _collections.namedtuple(
    "ParseExample", __parse_example_outputs)


def _parse_example(serialized, names, sparse_keys, dense_keys, dense_defaults, sparse_types, dense_shapes, name=None):
  r"""Transforms a vector of brain.Example protos (as strings) into typed tensors.

  Args:
    serialized: A `Tensor` of type `string`.
      A vector containing a batch of binary serialized Example protos.
    names: A `Tensor` of type `string`.
      A vector containing the names of the serialized protos.
      May contain, for example, table key (descriptive) names for the
      corresponding serialized protos.  These are purely useful for debugging
      purposes, and the presence of values here has no effect on the output.
      May also be an empty vector if no names are available.
      If non-empty, this vector must be the same length as "serialized".
    sparse_keys: A list of `Tensor` objects with type `string`.
      A list of Nsparse string Tensors (scalars).
      The keys expected in the Examples' features associated with sparse values.
    dense_keys: A list of `Tensor` objects with type `string`.
      A list of Ndense string Tensors (scalars).
      The keys expected in the Examples' features associated with dense values.
    dense_defaults: A list of `Tensor` objects with types from: `float32`, `int64`, `string`.
      A list of Ndense Tensors (some may be empty).
      dense_defaults[j] provides default values
      when the example's feature_map lacks dense_key[j].  If an empty Tensor is
      provided for dense_defaults[j], then the Feature dense_keys[j] is required.
      The input type is inferred from dense_defaults[j], even when it's empty.
      If dense_defaults[j] is not empty, and dense_shapes[j] is fully defined,
      then the shape of dense_defaults[j] must match that of dense_shapes[j].
      If dense_shapes[j] has an undefined major dimension (variable strides dense
      feature), dense_defaults[j] must contain a single element:
      the padding element.
    sparse_types: A list of `tf.DTypes` from: `tf.float32, tf.int64, tf.string`.
      A list of Nsparse types; the data types of data in each Feature
      given in sparse_keys.
      Currently the ParseExample supports DT_FLOAT (FloatList),
      DT_INT64 (Int64List), and DT_STRING (BytesList).
    dense_shapes: A list of shapes (each a `tf.TensorShape` or list of `ints`).
      A list of Ndense shapes; the shapes of data in each Feature
      given in dense_keys.
      The number of elements in the Feature corresponding to dense_key[j]
      must always equal dense_shapes[j].NumEntries().
      If dense_shapes[j] == (D0, D1, ..., DN) then the shape of output
      Tensor dense_values[j] will be (|serialized|, D0, D1, ..., DN):
      The dense outputs are just the inputs row-stacked by batch.
      This works for dense_shapes[j] = (-1, D1, ..., DN).  In this case
      the shape of the output Tensor dense_values[j] will be
      (|serialized|, M, D1, .., DN), where M is the maximum number of blocks
      of elements of length D1 * .... * DN, across all minibatch entries
      in the input.  Any minibatch entry with less than M blocks of elements of
      length D1 * ... * DN will be padded with the corresponding default_value
      scalar element along the second dimension.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (sparse_indices, sparse_values, sparse_shapes, dense_values).

    sparse_indices: A list with the same length as `sparse_keys` of `Tensor` objects with type `int64`.
    sparse_values: A list of `Tensor` objects of type `sparse_types`.
    sparse_shapes: A list with the same length as `sparse_keys` of `Tensor` objects with type `int64`.
    dense_values: A list of `Tensor` objects. Has the same type as `dense_defaults`.
  """
  if not isinstance(sparse_keys, (list, tuple)):
    raise TypeError(
        "Expected list for 'sparse_keys' argument to "
        "'parse_example' Op, not %r." % sparse_keys)
  _attr_Nsparse = len(sparse_keys)
  if not isinstance(dense_keys, (list, tuple)):
    raise TypeError(
        "Expected list for 'dense_keys' argument to "
        "'parse_example' Op, not %r." % dense_keys)
  _attr_Ndense = len(dense_keys)
  if not isinstance(sparse_types, (list, tuple)):
    raise TypeError(
        "Expected list for 'sparse_types' argument to "
        "'parse_example' Op, not %r." % sparse_types)
  sparse_types = [_execute.make_type(_t, "sparse_types") for _t in sparse_types]
  if not isinstance(dense_shapes, (list, tuple)):
    raise TypeError(
        "Expected list for 'dense_shapes' argument to "
        "'parse_example' Op, not %r." % dense_shapes)
  dense_shapes = [_execute.make_shape(_s, "dense_shapes") for _s in dense_shapes]
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "ParseExample", serialized=serialized, names=names,
        sparse_keys=sparse_keys, dense_keys=dense_keys,
        dense_defaults=dense_defaults, sparse_types=sparse_types,
        dense_shapes=dense_shapes, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("Nsparse", _op.get_attr("Nsparse"), "Ndense",
              _op.get_attr("Ndense"), "sparse_types",
              _op.get_attr("sparse_types"), "Tdense", _op.get_attr("Tdense"),
              "dense_shapes", _op.get_attr("dense_shapes"))
  else:
    _attr_Tdense, dense_defaults = _execute.convert_to_mixed_eager_tensors(dense_defaults, _ctx)
    _attr_Tdense = [_t.as_datatype_enum for _t in _attr_Tdense]
    serialized = _ops.convert_to_tensor(serialized, _dtypes.string)
    names = _ops.convert_to_tensor(names, _dtypes.string)
    sparse_keys = _ops.convert_n_to_tensor(sparse_keys, _dtypes.string)
    dense_keys = _ops.convert_n_to_tensor(dense_keys, _dtypes.string)
    _inputs_flat = [serialized, names] + list(sparse_keys) + list(dense_keys) + list(dense_defaults)
    _attrs = ("Nsparse", _attr_Nsparse, "Ndense", _attr_Ndense,
              "sparse_types", sparse_types, "Tdense", _attr_Tdense,
              "dense_shapes", dense_shapes)
    _result = _execute.execute(b"ParseExample", _attr_Nsparse +
                               len(sparse_types) + _attr_Nsparse +
                               len(dense_defaults), inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "ParseExample", _inputs_flat, _attrs, _result, name)
  _result = [_result[:_attr_Nsparse]] + _result[_attr_Nsparse:]
  _result = _result[:1] + [_result[1:1 + len(sparse_types)]] + _result[1 + len(sparse_types):]
  _result = _result[:2] + [_result[2:2 + _attr_Nsparse]] + _result[2 + _attr_Nsparse:]
  _result = _result[:3] + [_result[3:]]
  _result = _ParseExampleOutput._make(_result)
  return _result


__parse_single_sequence_example_outputs = ["context_sparse_indices",
                                          "context_sparse_values",
                                          "context_sparse_shapes",
                                          "context_dense_values",
                                          "feature_list_sparse_indices",
                                          "feature_list_sparse_values",
                                          "feature_list_sparse_shapes",
                                          "feature_list_dense_values"]
_ParseSingleSequenceExampleOutput = _collections.namedtuple(
    "ParseSingleSequenceExample", __parse_single_sequence_example_outputs)


def _parse_single_sequence_example(serialized, feature_list_dense_missing_assumed_empty, context_sparse_keys, context_dense_keys, feature_list_sparse_keys, feature_list_dense_keys, context_dense_defaults, debug_name, context_sparse_types=[], feature_list_dense_types=[], context_dense_shapes=[], feature_list_sparse_types=[], feature_list_dense_shapes=[], name=None):
  r"""Transforms a scalar brain.SequenceExample proto (as strings) into typed tensors.

  Args:
    serialized: A `Tensor` of type `string`.
      A scalar containing a binary serialized SequenceExample proto.
    feature_list_dense_missing_assumed_empty: A `Tensor` of type `string`.
      A vector listing the
      FeatureList keys which may be missing from the SequenceExample.  If the
      associated FeatureList is missing, it is treated as empty.  By default,
      any FeatureList not listed in this vector must exist in the SequenceExample.
    context_sparse_keys: A list of `Tensor` objects with type `string`.
      A list of Ncontext_sparse string Tensors (scalars).
      The keys expected in the Examples' features associated with context_sparse
      values.
    context_dense_keys: A list of `Tensor` objects with type `string`.
      A list of Ncontext_dense string Tensors (scalars).
      The keys expected in the SequenceExamples' context features associated with
      dense values.
    feature_list_sparse_keys: A list of `Tensor` objects with type `string`.
      A list of Nfeature_list_sparse string Tensors
      (scalars).  The keys expected in the FeatureLists associated with sparse
      values.
    feature_list_dense_keys: A list of `Tensor` objects with type `string`.
      A list of Nfeature_list_dense string Tensors (scalars).
      The keys expected in the SequenceExamples' feature_lists associated
      with lists of dense values.
    context_dense_defaults: A list of `Tensor` objects with types from: `float32`, `int64`, `string`.
      A list of Ncontext_dense Tensors (some may be empty).
      context_dense_defaults[j] provides default values
      when the SequenceExample's context map lacks context_dense_key[j].
      If an empty Tensor is provided for context_dense_defaults[j],
      then the Feature context_dense_keys[j] is required.
      The input type is inferred from context_dense_defaults[j], even when it's
      empty.  If context_dense_defaults[j] is not empty, its shape must match
      context_dense_shapes[j].
    debug_name: A `Tensor` of type `string`.
      A scalar containing the name of the serialized proto.
      May contain, for example, table key (descriptive) name for the
      corresponding serialized proto.  This is purely useful for debugging
      purposes, and the presence of values here has no effect on the output.
      May also be an empty scalar if no name is available.
    context_sparse_types: An optional list of `tf.DTypes` from: `tf.float32, tf.int64, tf.string`. Defaults to `[]`.
      A list of Ncontext_sparse types; the data types of data in
      each context Feature given in context_sparse_keys.
      Currently the ParseSingleSequenceExample supports DT_FLOAT (FloatList),
      DT_INT64 (Int64List), and DT_STRING (BytesList).
    feature_list_dense_types: An optional list of `tf.DTypes` from: `tf.float32, tf.int64, tf.string`. Defaults to `[]`.
    context_dense_shapes: An optional list of shapes (each a `tf.TensorShape` or list of `ints`). Defaults to `[]`.
      A list of Ncontext_dense shapes; the shapes of data in
      each context Feature given in context_dense_keys.
      The number of elements in the Feature corresponding to context_dense_key[j]
      must always equal context_dense_shapes[j].NumEntries().
      The shape of context_dense_values[j] will match context_dense_shapes[j].
    feature_list_sparse_types: An optional list of `tf.DTypes` from: `tf.float32, tf.int64, tf.string`. Defaults to `[]`.
      A list of Nfeature_list_sparse types; the data types
      of data in each FeatureList given in feature_list_sparse_keys.
      Currently the ParseSingleSequenceExample supports DT_FLOAT (FloatList),
      DT_INT64 (Int64List), and DT_STRING (BytesList).
    feature_list_dense_shapes: An optional list of shapes (each a `tf.TensorShape` or list of `ints`). Defaults to `[]`.
      A list of Nfeature_list_dense shapes; the shapes of
      data in each FeatureList given in feature_list_dense_keys.
      The shape of each Feature in the FeatureList corresponding to
      feature_list_dense_key[j] must always equal
      feature_list_dense_shapes[j].NumEntries().
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (context_sparse_indices, context_sparse_values, context_sparse_shapes, context_dense_values, feature_list_sparse_indices, feature_list_sparse_values, feature_list_sparse_shapes, feature_list_dense_values).

    context_sparse_indices: A list with the same length as `context_sparse_keys` of `Tensor` objects with type `int64`.
    context_sparse_values: A list of `Tensor` objects of type `context_sparse_types`.
    context_sparse_shapes: A list with the same length as `context_sparse_keys` of `Tensor` objects with type `int64`.
    context_dense_values: A list of `Tensor` objects. Has the same type as `context_dense_defaults`.
    feature_list_sparse_indices: A list with the same length as `feature_list_sparse_keys` of `Tensor` objects with type `int64`.
    feature_list_sparse_values: A list of `Tensor` objects of type `feature_list_sparse_types`.
    feature_list_sparse_shapes: A list with the same length as `feature_list_sparse_keys` of `Tensor` objects with type `int64`.
    feature_list_dense_values: A list of `Tensor` objects of type `feature_list_dense_types`.
  """
  if not isinstance(context_sparse_keys, (list, tuple)):
    raise TypeError(
        "Expected list for 'context_sparse_keys' argument to "
        "'parse_single_sequence_example' Op, not %r." % context_sparse_keys)
  _attr_Ncontext_sparse = len(context_sparse_keys)
  if not isinstance(context_dense_keys, (list, tuple)):
    raise TypeError(
        "Expected list for 'context_dense_keys' argument to "
        "'parse_single_sequence_example' Op, not %r." % context_dense_keys)
  _attr_Ncontext_dense = len(context_dense_keys)
  if not isinstance(feature_list_sparse_keys, (list, tuple)):
    raise TypeError(
        "Expected list for 'feature_list_sparse_keys' argument to "
        "'parse_single_sequence_example' Op, not %r." % feature_list_sparse_keys)
  _attr_Nfeature_list_sparse = len(feature_list_sparse_keys)
  if not isinstance(feature_list_dense_keys, (list, tuple)):
    raise TypeError(
        "Expected list for 'feature_list_dense_keys' argument to "
        "'parse_single_sequence_example' Op, not %r." % feature_list_dense_keys)
  _attr_Nfeature_list_dense = len(feature_list_dense_keys)
  if context_sparse_types is None:
    context_sparse_types = []
  if not isinstance(context_sparse_types, (list, tuple)):
    raise TypeError(
        "Expected list for 'context_sparse_types' argument to "
        "'parse_single_sequence_example' Op, not %r." % context_sparse_types)
  context_sparse_types = [_execute.make_type(_t, "context_sparse_types") for _t in context_sparse_types]
  if feature_list_dense_types is None:
    feature_list_dense_types = []
  if not isinstance(feature_list_dense_types, (list, tuple)):
    raise TypeError(
        "Expected list for 'feature_list_dense_types' argument to "
        "'parse_single_sequence_example' Op, not %r." % feature_list_dense_types)
  feature_list_dense_types = [_execute.make_type(_t, "feature_list_dense_types") for _t in feature_list_dense_types]
  if context_dense_shapes is None:
    context_dense_shapes = []
  if not isinstance(context_dense_shapes, (list, tuple)):
    raise TypeError(
        "Expected list for 'context_dense_shapes' argument to "
        "'parse_single_sequence_example' Op, not %r." % context_dense_shapes)
  context_dense_shapes = [_execute.make_shape(_s, "context_dense_shapes") for _s in context_dense_shapes]
  if feature_list_sparse_types is None:
    feature_list_sparse_types = []
  if not isinstance(feature_list_sparse_types, (list, tuple)):
    raise TypeError(
        "Expected list for 'feature_list_sparse_types' argument to "
        "'parse_single_sequence_example' Op, not %r." % feature_list_sparse_types)
  feature_list_sparse_types = [_execute.make_type(_t, "feature_list_sparse_types") for _t in feature_list_sparse_types]
  if feature_list_dense_shapes is None:
    feature_list_dense_shapes = []
  if not isinstance(feature_list_dense_shapes, (list, tuple)):
    raise TypeError(
        "Expected list for 'feature_list_dense_shapes' argument to "
        "'parse_single_sequence_example' Op, not %r." % feature_list_dense_shapes)
  feature_list_dense_shapes = [_execute.make_shape(_s, "feature_list_dense_shapes") for _s in feature_list_dense_shapes]
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "ParseSingleSequenceExample", serialized=serialized,
        feature_list_dense_missing_assumed_empty=feature_list_dense_missing_assumed_empty,
        context_sparse_keys=context_sparse_keys,
        context_dense_keys=context_dense_keys,
        feature_list_sparse_keys=feature_list_sparse_keys,
        feature_list_dense_keys=feature_list_dense_keys,
        context_dense_defaults=context_dense_defaults, debug_name=debug_name,
        context_sparse_types=context_sparse_types,
        feature_list_dense_types=feature_list_dense_types,
        context_dense_shapes=context_dense_shapes,
        feature_list_sparse_types=feature_list_sparse_types,
        feature_list_dense_shapes=feature_list_dense_shapes, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("Ncontext_sparse", _op.get_attr("Ncontext_sparse"),
              "Ncontext_dense", _op.get_attr("Ncontext_dense"),
              "Nfeature_list_sparse", _op.get_attr("Nfeature_list_sparse"),
              "Nfeature_list_dense", _op.get_attr("Nfeature_list_dense"),
              "context_sparse_types", _op.get_attr("context_sparse_types"),
              "Tcontext_dense", _op.get_attr("Tcontext_dense"),
              "feature_list_dense_types",
              _op.get_attr("feature_list_dense_types"),
              "context_dense_shapes", _op.get_attr("context_dense_shapes"),
              "feature_list_sparse_types",
              _op.get_attr("feature_list_sparse_types"),
              "feature_list_dense_shapes",
              _op.get_attr("feature_list_dense_shapes"))
  else:
    _attr_Tcontext_dense, context_dense_defaults = _execute.convert_to_mixed_eager_tensors(context_dense_defaults, _ctx)
    _attr_Tcontext_dense = [_t.as_datatype_enum for _t in _attr_Tcontext_dense]
    serialized = _ops.convert_to_tensor(serialized, _dtypes.string)
    feature_list_dense_missing_assumed_empty = _ops.convert_to_tensor(feature_list_dense_missing_assumed_empty, _dtypes.string)
    context_sparse_keys = _ops.convert_n_to_tensor(context_sparse_keys, _dtypes.string)
    context_dense_keys = _ops.convert_n_to_tensor(context_dense_keys, _dtypes.string)
    feature_list_sparse_keys = _ops.convert_n_to_tensor(feature_list_sparse_keys, _dtypes.string)
    feature_list_dense_keys = _ops.convert_n_to_tensor(feature_list_dense_keys, _dtypes.string)
    debug_name = _ops.convert_to_tensor(debug_name, _dtypes.string)
    _inputs_flat = [serialized, feature_list_dense_missing_assumed_empty] + list(context_sparse_keys) + list(context_dense_keys) + list(feature_list_sparse_keys) + list(feature_list_dense_keys) + list(context_dense_defaults) + [debug_name]
    _attrs = ("Ncontext_sparse", _attr_Ncontext_sparse, "Ncontext_dense",
              _attr_Ncontext_dense, "Nfeature_list_sparse",
              _attr_Nfeature_list_sparse, "Nfeature_list_dense",
              _attr_Nfeature_list_dense, "context_sparse_types",
              context_sparse_types, "Tcontext_dense", _attr_Tcontext_dense,
              "feature_list_dense_types", feature_list_dense_types,
              "context_dense_shapes", context_dense_shapes,
              "feature_list_sparse_types", feature_list_sparse_types,
              "feature_list_dense_shapes", feature_list_dense_shapes)
    _result = _execute.execute(b"ParseSingleSequenceExample",
                               _attr_Ncontext_sparse +
                               len(context_sparse_types) +
                               _attr_Ncontext_sparse +
                               len(context_dense_defaults) +
                               _attr_Nfeature_list_sparse +
                               len(feature_list_sparse_types) +
                               _attr_Nfeature_list_sparse +
                               len(feature_list_dense_types),
                               inputs=_inputs_flat, attrs=_attrs, ctx=_ctx,
                               name=name)
  _execute.record_gradient(
      "ParseSingleSequenceExample", _inputs_flat, _attrs, _result, name)
  _result = [_result[:_attr_Ncontext_sparse]] + _result[_attr_Ncontext_sparse:]
  _result = _result[:1] + [_result[1:1 + len(context_sparse_types)]] + _result[1 + len(context_sparse_types):]
  _result = _result[:2] + [_result[2:2 + _attr_Ncontext_sparse]] + _result[2 + _attr_Ncontext_sparse:]
  _result = _result[:3] + [_result[3:3 + len(context_dense_defaults)]] + _result[3 + len(context_dense_defaults):]
  _result = _result[:4] + [_result[4:4 + _attr_Nfeature_list_sparse]] + _result[4 + _attr_Nfeature_list_sparse:]
  _result = _result[:5] + [_result[5:5 + len(feature_list_sparse_types)]] + _result[5 + len(feature_list_sparse_types):]
  _result = _result[:6] + [_result[6:6 + _attr_Nfeature_list_sparse]] + _result[6 + _attr_Nfeature_list_sparse:]
  _result = _result[:7] + [_result[7:]]
  _result = _ParseSingleSequenceExampleOutput._make(_result)
  return _result


def parse_tensor(serialized, out_type, name=None):
  r"""Transforms a serialized tensorflow.TensorProto proto into a Tensor.

  Args:
    serialized: A `Tensor` of type `string`.
      A scalar string containing a serialized TensorProto proto.
    out_type: A `tf.DType`.
      The type of the serialized tensor.  The provided type must match the
      type of the serialized tensor and no implicit conversion will take place.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `out_type`. A Tensor of type `out_type`.
  """
  out_type = _execute.make_type(out_type, "out_type")
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "ParseTensor", serialized=serialized, out_type=out_type, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("out_type", _op.get_attr("out_type"))
  else:
    serialized = _ops.convert_to_tensor(serialized, _dtypes.string)
    _inputs_flat = [serialized]
    _attrs = ("out_type", out_type)
    _result = _execute.execute(b"ParseTensor", 1, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "ParseTensor", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result


def serialize_tensor(tensor, name=None):
  r"""Transforms a Tensor into a serialized TensorProto proto.

  Args:
    tensor: A `Tensor`. A Tensor of type `T`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `string`.
    A serialized TensorProto proto of the input tensor.
  """
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "SerializeTensor", tensor=tensor, name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("T", _op.get_attr("T"))
  else:
    _attr_T, (tensor,) = _execute.args_to_matching_eager([tensor], _ctx)
    _attr_T = _attr_T.as_datatype_enum
    _inputs_flat = [tensor]
    _attrs = ("T", _attr_T)
    _result = _execute.execute(b"SerializeTensor", 1, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "SerializeTensor", _inputs_flat, _attrs, _result, name)
  _result, = _result
  return _result


def string_to_number(string_tensor, out_type=_dtypes.float32, name=None):
  r"""Converts each string in the input Tensor to the specified numeric type.

  (Note that int32 overflow results in an error while float overflow
  results in a rounded value.)

  Args:
    string_tensor: A `Tensor` of type `string`.
    out_type: An optional `tf.DType` from: `tf.float32, tf.float64, tf.int32, tf.int64`. Defaults to `tf.float32`.
      The numeric type to interpret each string in `string_tensor` as.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of type `out_type`.
    A Tensor of the same shape as the input `string_tensor`.
  """
  if out_type is None:
    out_type = _dtypes.float32
  out_type = _execute.make_type(out_type, "out_type")
  _ctx = _context.context()
  if _ctx.in_graph_mode():
    _, _, _op = _op_def_lib._apply_op_helper(
        "StringToNumber", string_tensor=string_tensor, out_type=out_type,
        name=name)
    _result = _op.outputs[:]
    _inputs_flat = _op.inputs
    _attrs = ("out_type", _op.get_attr("out_type"))
  else:
    string_tensor = _ops.convert_to_tensor(string_tensor, _dtypes.string)
    _inputs_flat = [string_tensor]
    _attrs = ("out_type", out_type)
    _result = _execute.execute(b"StringToNumber", 1, inputs=_inputs_flat,
                               attrs=_attrs, ctx=_ctx, name=name)
  _execute.record_gradient(
      "StringToNumber", _inputs_flat, _attrs, _result, name)
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
#   name: "DecodeCSV"
#   input_arg {
#     name: "records"
#     type: DT_STRING
#   }
#   input_arg {
#     name: "record_defaults"
#     type_list_attr: "OUT_TYPE"
#   }
#   output_arg {
#     name: "output"
#     type_list_attr: "OUT_TYPE"
#   }
#   attr {
#     name: "OUT_TYPE"
#     type: "list(type)"
#     has_minimum: true
#     minimum: 1
#     allowed_values {
#       list {
#         type: DT_FLOAT
#         type: DT_INT32
#         type: DT_INT64
#         type: DT_STRING
#       }
#     }
#   }
#   attr {
#     name: "field_delim"
#     type: "string"
#     default_value {
#       s: ","
#     }
#   }
#   attr {
#     name: "use_quote_delim"
#     type: "bool"
#     default_value {
#       b: true
#     }
#   }
#   attr {
#     name: "na_value"
#     type: "string"
#     default_value {
#       s: ""
#     }
#   }
# }
# op {
#   name: "DecodeJSONExample"
#   input_arg {
#     name: "json_examples"
#     type: DT_STRING
#   }
#   output_arg {
#     name: "binary_examples"
#     type: DT_STRING
#   }
# }
# op {
#   name: "DecodeRaw"
#   input_arg {
#     name: "bytes"
#     type: DT_STRING
#   }
#   output_arg {
#     name: "output"
#     type_attr: "out_type"
#   }
#   attr {
#     name: "out_type"
#     type: "type"
#     allowed_values {
#       list {
#         type: DT_HALF
#         type: DT_FLOAT
#         type: DT_DOUBLE
#         type: DT_INT32
#         type: DT_UINT16
#         type: DT_UINT8
#         type: DT_INT16
#         type: DT_INT8
#         type: DT_INT64
#       }
#     }
#   }
#   attr {
#     name: "little_endian"
#     type: "bool"
#     default_value {
#       b: true
#     }
#   }
# }
# op {
#   name: "ParseExample"
#   input_arg {
#     name: "serialized"
#     type: DT_STRING
#   }
#   input_arg {
#     name: "names"
#     type: DT_STRING
#   }
#   input_arg {
#     name: "sparse_keys"
#     type: DT_STRING
#     number_attr: "Nsparse"
#   }
#   input_arg {
#     name: "dense_keys"
#     type: DT_STRING
#     number_attr: "Ndense"
#   }
#   input_arg {
#     name: "dense_defaults"
#     type_list_attr: "Tdense"
#   }
#   output_arg {
#     name: "sparse_indices"
#     type: DT_INT64
#     number_attr: "Nsparse"
#   }
#   output_arg {
#     name: "sparse_values"
#     type_list_attr: "sparse_types"
#   }
#   output_arg {
#     name: "sparse_shapes"
#     type: DT_INT64
#     number_attr: "Nsparse"
#   }
#   output_arg {
#     name: "dense_values"
#     type_list_attr: "Tdense"
#   }
#   attr {
#     name: "Nsparse"
#     type: "int"
#     has_minimum: true
#   }
#   attr {
#     name: "Ndense"
#     type: "int"
#     has_minimum: true
#   }
#   attr {
#     name: "sparse_types"
#     type: "list(type)"
#     has_minimum: true
#     allowed_values {
#       list {
#         type: DT_FLOAT
#         type: DT_INT64
#         type: DT_STRING
#       }
#     }
#   }
#   attr {
#     name: "Tdense"
#     type: "list(type)"
#     has_minimum: true
#     allowed_values {
#       list {
#         type: DT_FLOAT
#         type: DT_INT64
#         type: DT_STRING
#       }
#     }
#   }
#   attr {
#     name: "dense_shapes"
#     type: "list(shape)"
#     has_minimum: true
#   }
# }
# op {
#   name: "ParseSingleSequenceExample"
#   input_arg {
#     name: "serialized"
#     type: DT_STRING
#   }
#   input_arg {
#     name: "feature_list_dense_missing_assumed_empty"
#     type: DT_STRING
#   }
#   input_arg {
#     name: "context_sparse_keys"
#     type: DT_STRING
#     number_attr: "Ncontext_sparse"
#   }
#   input_arg {
#     name: "context_dense_keys"
#     type: DT_STRING
#     number_attr: "Ncontext_dense"
#   }
#   input_arg {
#     name: "feature_list_sparse_keys"
#     type: DT_STRING
#     number_attr: "Nfeature_list_sparse"
#   }
#   input_arg {
#     name: "feature_list_dense_keys"
#     type: DT_STRING
#     number_attr: "Nfeature_list_dense"
#   }
#   input_arg {
#     name: "context_dense_defaults"
#     type_list_attr: "Tcontext_dense"
#   }
#   input_arg {
#     name: "debug_name"
#     type: DT_STRING
#   }
#   output_arg {
#     name: "context_sparse_indices"
#     type: DT_INT64
#     number_attr: "Ncontext_sparse"
#   }
#   output_arg {
#     name: "context_sparse_values"
#     type_list_attr: "context_sparse_types"
#   }
#   output_arg {
#     name: "context_sparse_shapes"
#     type: DT_INT64
#     number_attr: "Ncontext_sparse"
#   }
#   output_arg {
#     name: "context_dense_values"
#     type_list_attr: "Tcontext_dense"
#   }
#   output_arg {
#     name: "feature_list_sparse_indices"
#     type: DT_INT64
#     number_attr: "Nfeature_list_sparse"
#   }
#   output_arg {
#     name: "feature_list_sparse_values"
#     type_list_attr: "feature_list_sparse_types"
#   }
#   output_arg {
#     name: "feature_list_sparse_shapes"
#     type: DT_INT64
#     number_attr: "Nfeature_list_sparse"
#   }
#   output_arg {
#     name: "feature_list_dense_values"
#     type_list_attr: "feature_list_dense_types"
#   }
#   attr {
#     name: "Ncontext_sparse"
#     type: "int"
#     default_value {
#       i: 0
#     }
#     has_minimum: true
#   }
#   attr {
#     name: "Ncontext_dense"
#     type: "int"
#     default_value {
#       i: 0
#     }
#     has_minimum: true
#   }
#   attr {
#     name: "Nfeature_list_sparse"
#     type: "int"
#     default_value {
#       i: 0
#     }
#     has_minimum: true
#   }
#   attr {
#     name: "Nfeature_list_dense"
#     type: "int"
#     default_value {
#       i: 0
#     }
#     has_minimum: true
#   }
#   attr {
#     name: "context_sparse_types"
#     type: "list(type)"
#     default_value {
#       list {
#       }
#     }
#     has_minimum: true
#     allowed_values {
#       list {
#         type: DT_FLOAT
#         type: DT_INT64
#         type: DT_STRING
#       }
#     }
#   }
#   attr {
#     name: "Tcontext_dense"
#     type: "list(type)"
#     default_value {
#       list {
#       }
#     }
#     has_minimum: true
#     allowed_values {
#       list {
#         type: DT_FLOAT
#         type: DT_INT64
#         type: DT_STRING
#       }
#     }
#   }
#   attr {
#     name: "feature_list_dense_types"
#     type: "list(type)"
#     default_value {
#       list {
#       }
#     }
#     has_minimum: true
#     allowed_values {
#       list {
#         type: DT_FLOAT
#         type: DT_INT64
#         type: DT_STRING
#       }
#     }
#   }
#   attr {
#     name: "context_dense_shapes"
#     type: "list(shape)"
#     default_value {
#       list {
#       }
#     }
#     has_minimum: true
#   }
#   attr {
#     name: "feature_list_sparse_types"
#     type: "list(type)"
#     default_value {
#       list {
#       }
#     }
#     has_minimum: true
#     allowed_values {
#       list {
#         type: DT_FLOAT
#         type: DT_INT64
#         type: DT_STRING
#       }
#     }
#   }
#   attr {
#     name: "feature_list_dense_shapes"
#     type: "list(shape)"
#     default_value {
#       list {
#       }
#     }
#     has_minimum: true
#   }
# }
# op {
#   name: "ParseTensor"
#   input_arg {
#     name: "serialized"
#     type: DT_STRING
#   }
#   output_arg {
#     name: "output"
#     type_attr: "out_type"
#   }
#   attr {
#     name: "out_type"
#     type: "type"
#   }
# }
# op {
#   name: "SerializeTensor"
#   input_arg {
#     name: "tensor"
#     type_attr: "T"
#   }
#   output_arg {
#     name: "serialized"
#     type: DT_STRING
#   }
#   attr {
#     name: "T"
#     type: "type"
#   }
# }
# op {
#   name: "StringToNumber"
#   input_arg {
#     name: "string_tensor"
#     type: DT_STRING
#   }
#   output_arg {
#     name: "output"
#     type_attr: "out_type"
#   }
#   attr {
#     name: "out_type"
#     type: "type"
#     default_value {
#       type: DT_FLOAT
#     }
#     allowed_values {
#       list {
#         type: DT_FLOAT
#         type: DT_DOUBLE
#         type: DT_INT32
#         type: DT_INT64
#       }
#     }
#   }
# }
_op_def_lib = _InitOpDefLibrary(b"\n\300\001\n\tDecodeCSV\022\013\n\007records\030\007\022\033\n\017record_defaults2\010OUT_TYPE\032\022\n\006output2\010OUT_TYPE\"$\n\010OUT_TYPE\022\nlist(type)(\0010\001:\010\n\0062\004\001\003\t\007\"\032\n\013field_delim\022\006string\032\003\022\001,\"\033\n\017use_quote_delim\022\004bool\032\002(\001\"\026\n\010na_value\022\006string\032\002\022\000\n;\n\021DecodeJSONExample\022\021\n\rjson_examples\030\007\032\023\n\017binary_examples\030\007\nf\n\tDecodeRaw\022\t\n\005bytes\030\007\032\022\n\006output\"\010out_type\"\037\n\010out_type\022\004type:\r\n\0132\t\023\001\002\003\021\004\005\006\t\"\031\n\rlittle_endian\022\004bool\032\002(\001\n\357\002\n\014ParseExample\022\016\n\nserialized\030\007\022\t\n\005names\030\007\022\030\n\013sparse_keys\030\007*\007Nsparse\022\026\n\ndense_keys\030\007*\006Ndense\022\030\n\016dense_defaults2\006Tdense\032\033\n\016sparse_indices\030\t*\007Nsparse\032\035\n\rsparse_values2\014sparse_types\032\032\n\rsparse_shapes\030\t*\007Nsparse\032\026\n\014dense_values2\006Tdense\"\020\n\007Nsparse\022\003int(\001\"\017\n\006Ndense\022\003int(\001\"%\n\014sparse_types\022\nlist(type)(\001:\007\n\0052\003\001\t\007\"\037\n\006Tdense\022\nlist(type)(\001:\007\n\0052\003\001\t\007\"\035\n\014dense_shapes\022\013list(shape)(\001\n\203\t\n\032ParseSingleSequenceExample\022\016\n\nserialized\030\007\022,\n(feature_list_dense_missing_assumed_empty\030\007\022(\n\023context_sparse_keys\030\007*\017Ncontext_sparse\022&\n\022context_dense_keys\030\007*\016Ncontext_dense\0222\n\030feature_list_sparse_keys\030\007*\024Nfeature_list_sparse\0220\n\027feature_list_dense_keys\030\007*\023Nfeature_list_dense\022(\n\026context_dense_defaults2\016Tcontext_dense\022\016\n\ndebug_name\030\007\032+\n\026context_sparse_indices\030\t*\017Ncontext_sparse\032-\n\025context_sparse_values2\024context_sparse_types\032*\n\025context_sparse_shapes\030\t*\017Ncontext_sparse\032&\n\024context_dense_values2\016Tcontext_dense\0325\n\033feature_list_sparse_indices\030\t*\024Nfeature_list_sparse\0327\n\032feature_list_sparse_values2\031feature_list_sparse_types\0324\n\032feature_list_sparse_shapes\030\t*\024Nfeature_list_sparse\0325\n\031feature_list_dense_values2\030feature_list_dense_types\"\034\n\017Ncontext_sparse\022\003int\032\002\030\000(\001\"\033\n\016Ncontext_dense\022\003int\032\002\030\000(\001\"!\n\024Nfeature_list_sparse\022\003int\032\002\030\000(\001\" \n\023Nfeature_list_dense\022\003int\032\002\030\000(\001\"1\n\024context_sparse_types\022\nlist(type)\032\002\n\000(\001:\007\n\0052\003\001\t\007\"+\n\016Tcontext_dense\022\nlist(type)\032\002\n\000(\001:\007\n\0052\003\001\t\007\"5\n\030feature_list_dense_types\022\nlist(type)\032\002\n\000(\001:\007\n\0052\003\001\t\007\")\n\024context_dense_shapes\022\013list(shape)\032\002\n\000(\001\"6\n\031feature_list_sparse_types\022\nlist(type)\032\002\n\000(\001:\007\n\0052\003\001\t\007\".\n\031feature_list_dense_shapes\022\013list(shape)\032\002\n\000(\001\nC\n\013ParseTensor\022\016\n\nserialized\030\007\032\022\n\006output\"\010out_type\"\020\n\010out_type\022\004type\n9\n\017SerializeTensor\022\013\n\006tensor\"\001T\032\016\n\nserialized\030\007\"\t\n\001T\022\004type\nW\n\016StringToNumber\022\021\n\rstring_tensor\030\007\032\022\n\006output\"\010out_type\"\036\n\010out_type\022\004type\032\0020\001:\010\n\0062\004\001\002\003\t")
