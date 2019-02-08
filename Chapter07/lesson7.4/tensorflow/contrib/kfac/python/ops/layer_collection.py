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
"""Registry for layers and their parameters/variables.

This represents the collection of all layers in the approximate Fisher
information matrix to which a particular FisherBlock may belong. That is, we
might have several layer collections for one TF graph (if we have multiple K-FAC
optimizers being used, for example.)
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from collections import defaultdict
from collections import OrderedDict

from tensorflow.contrib.kfac.python.ops import fisher_blocks as fb
from tensorflow.contrib.kfac.python.ops import loss_functions as lf
from tensorflow.contrib.kfac.python.ops import utils
from tensorflow.python.framework import ops
from tensorflow.python.ops import math_ops
from tensorflow.python.ops import variable_scope
from tensorflow.python.platform import tf_logging as logging
from tensorflow.python.util import nest


APPROX_KRONECKER_NAME = "kron"
APPROX_DIAGONAL_NAME = "diagonal"
APPROX_FULL_NAME = "full"

# TODO(jamesmartens): need to add find_canonical_output back into this somewhere


class LayerParametersDict(OrderedDict):
  """An OrderedDict where keys are Tensors or tuples of Tensors.

  Ensures that no Tensor is associated with two different keys.
  """

  def __init__(self, *args, **kwargs):
    self._tensors = set()
    super(LayerParametersDict, self).__init__(*args, **kwargs)

  def __setitem__(self, key, value):
    tensors = key if isinstance(key, (tuple, list)) else (key,)
    key_collisions = self._tensors.intersection(tensors)
    if key_collisions:
      raise ValueError("Key(s) already present: {}".format(key_collisions))
    self._tensors.update(tensors)
    super(LayerParametersDict, self).__setitem__(key, value)

  def __delitem__(self, key):
    self._tensors.remove(key)
    super(LayerParametersDict, self).__delitem__(key)


# TODO(duckworthd): add capability for LayerCollection to be "finalized"
# and do this when it gets used by FisherEstimator / KfacOptimizer


class LayerCollection(object):
  """Registry of information about layers and losses.

  Note that you need to create a new one of these for each MatrixEstimator or
  KfacOptimizer.

  Attributes:
    fisher_blocks: a LayersParamsDict (subclass of OrderedDict) mapping layer
        parameters (Tensors or tuples of Tensors) to FisherBlock instances.
    fisher_factors: an OrderedDict mapping tuples to FisherFactor instances.
    generic_registrations: a list of variables registered via a generic layer
        registration. Generic registrations handle any and all of the ways a
        variable is used in the graph, which means we don't need to check
        their registration when verifying the correctness of the graph.
    losses: a list of LossFunction objects. The loss to be optimized is their
        sum.
  """

  def __init__(self, graph=None, name="LayerCollection"):
    self.fisher_blocks = LayerParametersDict()
    self.fisher_factors = OrderedDict()
    self._generic_registrations = set()
    self._graph = graph or ops.get_default_graph()
    self.losses = []
    self._subgraph = None

    with variable_scope.variable_scope(None, default_name=name) as scope:
      self._var_scope = scope.name

  reset_internals = __init__

  def register_block(self, layer_key, fisher_block):
    """Validates and registers the layer_key associated with the fisher_block.

    Validation consists of checking whether the key was already registered or
    if any of the elements of layer_key (if it's a tuple) were already
    registered as part of another tuple (throws an error if so). If any of the
    elements were registered by themselves, or as part of tuples that are
    subsets of this layer_key, those registrations are first removed.

    If the layer_key is a subset of an existing registration, registration of
    the new, smaller layer_key is skipped.

    e.g. If registrations include {'a': foo, ('b', 'c'): bar}, then
      - register_layer('a', baz) -> ValueError
      - register_layer(('b', 'c', 'd'), baz) ->
        {'a': foo, ('b', 'c', 'd'): baz}
      - register_layer('b', baz) ->
        {'a': foo, ('b', 'c'): bar} (No change)
      - register_layer(('a', 'd'), baz) ->
        {('a', 'd'): baz, ('b', 'c'): bar}
      - register_layer(('b', 'd'), baz) -> ValueError

    Args:
      layer_key: The key to check for in existing registrations and to register
          if valid.
      fisher_block: The associated fisher block.

    Raises:
      ValueError: If the layer_key was already registered, or if a subset of the
          layer_key has already been registered as part of a different tuple.
    """
    if layer_key in self.fisher_blocks:
      raise ValueError("Duplicate registration: {}".format(layer_key))
    if isinstance(layer_key, (tuple, list)):
      self._register_block_with_sequence_key(layer_key, fisher_block)
    else:
      self._register_block_with_nonsequence_key(layer_key, fisher_block)

  def _register_block_with_sequence_key(self, layer_key, fisher_block):
    """Validates and registers the layer_key if it's a sequence."""
    inclusions = {
        fisher_elt
        for layer_elt in layer_key for fisher_elt in self.fisher_blocks
        if self._equal_or_subset(layer_elt, fisher_elt)
    }

    if not inclusions:
      self.fisher_blocks[layer_key] = fisher_block
      return

    for key in inclusions:
      fisher_block_key = key if isinstance(key, (tuple, list)) else (key,)
      if set(layer_key).issubset(fisher_block_key):
        logging.warning("Graph Registration Warning: tried to register "
                        "a subset ({}) of an already registered tuple "
                        "({}), skipping".format(layer_key, fisher_block_key))
        return
      if not set(fisher_block_key).issubset(layer_key):
        raise ValueError(
            "Inconsistent registration, expected new key to be a subset or "
            "superset of the existing key: existing is {}, new is {}".format(
                key, layer_key))
      else:
        self.fisher_blocks.pop(key)

    self.fisher_blocks[layer_key] = fisher_block

  def _register_block_with_nonsequence_key(self, layer_key, fisher_block):
    """Validates and registers the layer_key if it's not a sequence."""
    inclusions = {
        fisher_elt
        for fisher_elt in self.fisher_blocks
        if self._equal_or_subset(layer_key, fisher_elt)
    }

    if not inclusions:
      self.fisher_blocks[layer_key] = fisher_block
    else:
      logging.warning("Graph Registration Warning: tried to register "
                      "variable ({}) but a containing tuple was already "
                      "registered ({}), skipping".format(layer_key, inclusions))

  def _equal_or_subset(self, elt1, elt2):
    """Checks if the elements are equal or one is contained in the other."""
    return (elt1 == elt2 or (isinstance(elt1,
                                        (tuple, list)) and elt2 in elt1) or
            (isinstance(elt2, (tuple, list)) and elt1 in elt2))

  def get_use_count_map(self):
    """Returns a dict of variables to their number of registrations."""
    vars_to_uses = defaultdict(int)
    for key in self.fisher_blocks.keys():
      key = key if isinstance(key, (tuple, list)) else (key,)
      for k in key:
        vars_to_uses[k] += 1
    return vars_to_uses

  def get_blocks(self):
    return self.fisher_blocks.values()

  def get_factors(self):
    return self.fisher_factors.values()

  @property
  def generic_registrations(self):
    return self._generic_registrations

  @property
  def graph(self):
    return self._graph

  @property
  def subgraph(self):
    return self._subgraph

  def create_subgraph(self):
    if not self.losses:
      raise ValueError("Must have at least one registered loss.")
    inputs_to_losses = nest.flatten(tuple(loss.inputs for loss in self.losses))
    self._subgraph = utils.SubGraph(inputs_to_losses)

  def total_loss(self):
    return math_ops.add_n(tuple(loss.evaluate() for loss in self.losses))

  def total_sampled_loss(self):
    return math_ops.add_n(
        tuple(loss.evaluate_on_sample() for loss in self.losses))

  def register_fully_connected(self,
                               params,
                               inputs,
                               outputs,
                               approx=APPROX_KRONECKER_NAME):
    has_bias = isinstance(params, (tuple, list))
    if approx == APPROX_KRONECKER_NAME:
      self.register_block(params,
                          fb.FullyConnectedKFACBasicFB(self, inputs, outputs,
                                                       has_bias))
    elif approx == APPROX_DIAGONAL_NAME:
      self.register_block(params,
                          fb.FullyConnectedDiagonalFB(self, inputs, outputs,
                                                      has_bias))
    else:
      raise ValueError("Bad value {} for approx.".format(approx))

  def register_conv2d(self, params, strides, padding, inputs, outputs,
                      approx=APPROX_KRONECKER_NAME):

    if approx == APPROX_KRONECKER_NAME:
      self.register_block(params,
                          fb.ConvKFCBasicFB(self, params, inputs, outputs,
                                            strides, padding))
    elif approx == APPROX_DIAGONAL_NAME:
      self.register_block(params,
                          fb.ConvDiagonalFB(self, params, inputs, outputs,
                                            strides, padding))

  def register_generic(self, params, batch_size, approx=APPROX_DIAGONAL_NAME):
    params = params if isinstance(params, (tuple, list)) else (params,)
    self._generic_registrations |= set(params)

    # Generic registrations do not need special registration rules because we do
    # not care about multiple generic registrations. Add them to the
    # fisher_block dictionary manually rather than going through the logic in
    # self.register_block.
    if approx == APPROX_FULL_NAME:
      self.fisher_blocks[params] = fb.FullFB(self, params, batch_size)
    elif approx == APPROX_DIAGONAL_NAME:
      self.fisher_blocks[params] = fb.NaiveDiagonalFB(self, params, batch_size)
    else:
      raise ValueError("Bad value {} for approx.".format(approx))

  def register_categorical_predictive_distribution(self,
                                                   logits,
                                                   seed=None,
                                                   targets=None):
    """Registers a categorical predictive distribution.

    Args:
      logits: The logits of the distribution (i.e. its parameters).
      seed: The seed for the RNG (for debugging) (Default: None)
      targets: (OPTIONAL) The targets for the loss function.  Only required if
        one wants to call total_loss() instead of total_sampled_loss().
        total_loss() is required, for example, to estimate the
        "empirical Fisher" (instead of the true Fisher).
        (Default: None)
    """
    loss = lf.CategoricalLogitsNegativeLogProbLoss(
        logits, targets=targets, seed=seed)
    self.losses.append(loss)

  def register_normal_predictive_distribution(self,
                                              mean,
                                              var=0.5,
                                              seed=None,
                                              targets=None):
    """Registers a normal predictive distribution.

    Args:
      mean: The mean vector defining the distribution.
      var: The variance (must be a scalar).  Note that the default value of
        0.5 corresponds to a standard squared error loss (target -
        prediction)**2. If your squared error loss is of the form
        0.5*(target - prediction)**2 you should use var=1.0. (Default: 0.5)
      seed: The seed for the RNG (for debugging) (Default: None)
      targets: (OPTIONAL) The targets for the loss function.  Only required if
        one wants to call total_loss() instead of total_sampled_loss().
        total_loss() is required, for example, to estimate the
        "empirical Fisher" (instead of the true Fisher).
        (Default: None)
    """
    loss = lf.NormalMeanNegativeLogProbLoss(
        mean, var, targets=targets, seed=seed)
    self.losses.append(loss)

  def register_multi_bernoulli_predictive_distribution(self,
                                                       logits,
                                                       seed=None,
                                                       targets=None):
    """Registers a multi-Bernoulli predictive distribution.

    Args:
      logits: The logits of the distribution (i.e. its parameters).
      seed: The seed for the RNG (for debugging) (Default: None)
      targets: (OPTIONAL) The targets for the loss function.  Only required if
        one wants to call total_loss() instead of total_sampled_loss().
        total_loss() is required, for example, to estimate the
        "empirical Fisher" (instead of the true Fisher).
        (Default: None)
    """
    loss = lf.MultiBernoulliNegativeLogProbLoss(
        logits, targets=targets, seed=seed)
    self.losses.append(loss)

  def make_or_get_factor(self, cls, args):
    with variable_scope.variable_scope(self._var_scope):
      return utils.setdefault(self.fisher_factors, (cls, args),
                              lambda: cls(*args))
