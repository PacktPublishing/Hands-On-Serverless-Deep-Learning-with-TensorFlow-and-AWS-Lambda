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
"""Operations for linear algebra."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow.python.framework import ops
from tensorflow.python.ops import array_ops
from tensorflow.python.ops import gen_linalg_ops
from tensorflow.python.ops import math_ops


def logdet(matrix, name=None):
  """Computes log of the determinant of a hermitian positive definite matrix.

  ```python
  # Compute the determinant of a matrix while reducing the chance of over- or
  underflow:
  A = ... # shape 10 x 10
  det = tf.exp(tf.logdet(A))  # scalar
  ```

  Args:
    matrix:  A `Tensor`. Must be `float32`, `float64`, `complex64`, or
      `complex128` with shape `[..., M, M]`.
    name:  A name to give this `Op`.  Defaults to `logdet`.

  Returns:
    The natural log of the determinant of `matrix`.

  @compatibility(numpy)
  Equivalent to numpy.linalg.slogdet, although no sign is returned since only
  hermitian positive definite matrices are supported.
  @end_compatibility
  """
  # This uses the property that the log det(A) = 2*sum(log(real(diag(C))))
  # where C is the cholesky decomposition of A.
  with ops.name_scope(name, 'logdet', [matrix]):
    chol = gen_linalg_ops.cholesky(matrix)
    return 2.0 * math_ops.reduce_sum(
        math_ops.log(math_ops.real(array_ops.matrix_diag_part(chol))),
        reduction_indices=[-1])
