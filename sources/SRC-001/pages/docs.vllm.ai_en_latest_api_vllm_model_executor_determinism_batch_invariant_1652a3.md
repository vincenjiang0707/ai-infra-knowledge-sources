source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/determinism/batch_invariant/
lastmod: 2026-09-23

#

`vllm.model_executor.determinism.batch_invariant`

[¶](https://docs.vllm.ai#vllm.model_executor.determinism.batch_invariant)

Functions:

-
–[bmm_kernel](https://docs.vllm.ai#vllm.model_executor.determinism.batch_invariant.bmm_kernel)Batched GEMM: (B, M, K) x (B, K, N) -> (B, M, N).

-
–[log_softmax](https://docs.vllm.ai#vllm.model_executor.determinism.batch_invariant.log_softmax)Compute log_softmax using Triton kernel.

-
–[matmul_descriptor_persistent](https://docs.vllm.ai#vllm.model_executor.determinism.batch_invariant.matmul_descriptor_persistent)Persistent matmul using tensor descriptors (Intel XPU fast path).

-
–[matmul_kernel_descriptor_persistent](https://docs.vllm.ai#vllm.model_executor.determinism.batch_invariant.matmul_kernel_descriptor_persistent)Persistent matmul using tensor descriptors for 2D block I/O.

-
–[mean_dim](https://docs.vllm.ai#vllm.model_executor.determinism.batch_invariant.mean_dim)Triton implementation of torch.mean with single dimension reduction.

-
–[mean_kernel](https://docs.vllm.ai#vllm.model_executor.determinism.batch_invariant.mean_kernel)Kernel for computing mean along a single dimension.

-
–[rms_norm_batch_invariant](https://docs.vllm.ai#vllm.model_executor.determinism.batch_invariant.rms_norm_batch_invariant)Compute RMS normalization using Triton kernel.


##

`_log_softmax_kernel(input_ptr, output_ptr, input_row_stride, output_row_stride, n_cols, BLOCK_SIZE)`

[¶](https://docs.vllm.ai#vllm.model_executor.determinism.batch_invariant._log_softmax_kernel)

Compute log_softmax along the last dimension of a 2D tensor. Each block handles one row of the input tensor.

## Source code in `vllm/model_executor/determinism/batch_invariant.py`


##

`_rms_norm_kernel(input_ptr, weight_ptr, output_ptr, input_row_stride, output_row_stride, n_cols, eps, BLOCK_SIZE, HAS_WEIGHT)`

[¶](https://docs.vllm.ai#vllm.model_executor.determinism.batch_invariant._rms_norm_kernel)

Compute RMS normalization along the last dimension of a 2D tensor. RMS Norm: y = x / sqrt(mean(x^2) + eps) * weight Each block handles one row of the input tensor.

## Source code in `vllm/model_executor/determinism/batch_invariant.py`


##

`bmm_kernel(a_ptr, b_ptr, c_ptr, B, M, N, K, stride_ab, stride_am, stride_ak, stride_bb, stride_bk, stride_bn, stride_cb, stride_cm, stride_cn, BLOCK_SIZE_M, BLOCK_SIZE_N, BLOCK_SIZE_K, A_LARGE, B_LARGE, C_LARGE)`

[¶](https://docs.vllm.ai#vllm.model_executor.determinism.batch_invariant.bmm_kernel)

Batched GEMM: (B, M, K) x (B, K, N) -> (B, M, N).

Each program computes one (batch_idx, tile_m, tile_n) tile, accumulating along K in a fixed order to preserve batch invariance.

## Source code in `vllm/model_executor/determinism/batch_invariant.py`


|
|

##

`log_softmax(input, dim=-1)`

[¶](https://docs.vllm.ai#vllm.model_executor.determinism.batch_invariant.log_softmax)

Compute log_softmax using Triton kernel.

Parameters:

-

(`input`

[¶](https://docs.vllm.ai#vllm.model_executor.determinism.batch_invariant.log_softmax(input))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Input tensor

-

(`dim`

[¶](https://docs.vllm.ai#vllm.model_executor.determinism.batch_invariant.log_softmax(dim))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`-1`

) –Dimension along which to compute log_softmax (only -1 or last dim supported)


Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Tensor with log_softmax applied along the specified dimension


## Source code in `vllm/model_executor/determinism/batch_invariant.py`


##

`matmul_descriptor_persistent(a, b, bias=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.determinism.batch_invariant.matmul_descriptor_persistent)

Persistent matmul using tensor descriptors (Intel XPU fast path).

Parameters:

-

(`a`

[¶](https://docs.vllm.ai#vllm.model_executor.determinism.batch_invariant.matmul_descriptor_persistent(a))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Input matrix [M, K], must be contiguous.

-

(`b`

[¶](https://docs.vllm.ai#vllm.model_executor.determinism.batch_invariant.matmul_descriptor_persistent(b))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Weight matrix [K, N] (standard layout — transposed internally).

-

(`bias`

[¶](https://docs.vllm.ai#vllm.model_executor.determinism.batch_invariant.matmul_descriptor_persistent(bias))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –Optional 1D bias vector [N].


Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Output matrix [M, N] with dtype matching the inputs.


## Source code in `vllm/model_executor/determinism/batch_invariant.py`


##

`matmul_kernel_descriptor_persistent(a_ptr, b_ptr, c_ptr, bias_ptr, M, N, K, BLOCK_SIZE_M, BLOCK_SIZE_N, BLOCK_SIZE_K, GROUP_SIZE_M, NUM_SMS, HAS_BIAS)`

[¶](https://docs.vllm.ai#vllm.model_executor.determinism.batch_invariant.matmul_kernel_descriptor_persistent)

Persistent matmul using tensor descriptors for 2D block I/O.

Expects b_ptr to point to a transposed B matrix of shape [N, K] with row-major (K-contiguous) layout. The dot product transposes each loaded B-tile back: dot(A_tile, B_tile.T).

~3x faster than the pointer-based persistent kernel on Intel XPU because tensor descriptors leverage hardware 2D block load/store with automatic bounds checking (no explicit masks needed).

## Source code in `vllm/model_executor/determinism/batch_invariant.py`


|
|

##

`mean_dim(input, dim, keepdim=False, dtype=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.determinism.batch_invariant.mean_dim)

Triton implementation of torch.mean with single dimension reduction.

Parameters:

-

(`input`

[¶](https://docs.vllm.ai#vllm.model_executor.determinism.batch_invariant.mean_dim(input))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Input tensor

-

(`dim`

[¶](https://docs.vllm.ai#vllm.model_executor.determinism.batch_invariant.mean_dim(dim))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Single dimension along which to compute mean

-

(`keepdim`

[¶](https://docs.vllm.ai#vllm.model_executor.determinism.batch_invariant.mean_dim(keepdim))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –Whether to keep the reduced dimension

-

(`dtype`

[¶](https://docs.vllm.ai#vllm.model_executor.determinism.batch_invariant.mean_dim(dtype))

, default:[dtype](https://pytorch.org/docs/stable/tensor_attributes.html#torch.dtype)| None`None`

) –Output dtype. If None, uses input dtype (or float32 for integer inputs)


Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Tensor with mean values along specified dimension


## Source code in `vllm/model_executor/determinism/batch_invariant.py`


|
|

##

`mean_kernel(input_ptr, output_ptr, input_stride0, input_stride1, input_stride2, output_stride0, output_stride1, M, N, K, BLOCK_SIZE)`

[¶](https://docs.vllm.ai#vllm.model_executor.determinism.batch_invariant.mean_kernel)

Kernel for computing mean along a single dimension. Input is viewed as (M, N, K) where N is the dimension being reduced.

## Source code in `vllm/model_executor/determinism/batch_invariant.py`


##

`rms_norm_batch_invariant(input, weight, eps=1e-06, residual=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.determinism.batch_invariant.rms_norm_batch_invariant)

Compute RMS normalization using Triton kernel.

Parameters:

-

(`input`

[¶](https://docs.vllm.ai#vllm.model_executor.determinism.batch_invariant.rms_norm_batch_invariant(input))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Input tensor of shape (..., hidden_size)

-

(`weight`

[¶](https://docs.vllm.ai#vllm.model_executor.determinism.batch_invariant.rms_norm_batch_invariant(weight))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| NoneWeight tensor of shape (hidden_size,), or None to skip the per-channel multiply (

`RMSNorm(has_weight=False)`

) -

(`eps`

[¶](https://docs.vllm.ai#vllm.model_executor.determinism.batch_invariant.rms_norm_batch_invariant(eps))

, default:[float](https://docs.python.org/3/builtins/functions.html#float)`1e-06`

) –Small constant for numerical stability

-

(`residual`

[¶](https://docs.vllm.ai#vllm.model_executor.determinism.batch_invariant.rms_norm_batch_invariant(residual))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –Optional residual tensor fused into the normalization path


Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)|[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor),[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]RMS normalized tensor, or

`(output, residual_out)`

when`residual`

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)|[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor),[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]is provided