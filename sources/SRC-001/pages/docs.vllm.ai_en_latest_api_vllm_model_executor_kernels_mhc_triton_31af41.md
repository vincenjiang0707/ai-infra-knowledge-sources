source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/kernels/mhc/triton/
lastmod: 2026-09-24

#

`vllm.model_executor.kernels.mhc.triton`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.triton)

Functions:

-
–[hc_collapse_triton](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.triton.hc_collapse_triton)Collapse BF16 residual streams with FP32 pre-mix coefficients.

-
–[mhc_pre_mix_triton](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.triton.mhc_pre_mix_triton)Pre-mix gate for the delayed mHC pre, from AITER's split-k GEMM output.

-
–[rmsnorm_nw](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.triton.rmsnorm_nw)Weight-free RMSNorm over the last dimension.


##

`_hc_head_triton(hs_flat, fn, hc_scale, hc_base, out, hidden_size, rms_eps, hc_eps, hc_mult)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.triton._hc_head_triton)

Fill pre-allocated `out`

(T, H) in-place with the hc_head result.

## Source code in `vllm/model_executor/kernels/mhc/triton.py`


##

`_mhc_pre_mix_kernel(gemm_ptr, sqrsum_ptr, hc_scale_ptr, hc_base_ptr, out_ptr, splitk, hc_mult, gemm_stride_k, gemm_stride_t, gemm_stride_j, sqrsum_stride_k, sqrsum_stride_t, out_stride_t, out_stride_j, inv_hc_hidden, rms_eps, hc_pre_eps, SPLITK_BLOCK, HC_BLOCK)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.triton._mhc_pre_mix_kernel)

Recover the pre-mix gate from a split-k mHC pre GEMM output.

## Source code in `vllm/model_executor/kernels/mhc/triton.py`


##

`_rmsnorm_nw_kernel(x_ptr, out_ptr, stride_row, D, eps, RBLOCK)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.triton._rmsnorm_nw_kernel)

Weight-free RMSNorm Triton kernel: out = x * rsqrt(mean(x², -1) + eps).

## Source code in `vllm/model_executor/kernels/mhc/triton.py`


##

`hc_collapse_triton(x, pre_mix)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.triton.hc_collapse_triton)

Collapse BF16 residual streams with FP32 pre-mix coefficients.

## Source code in `vllm/model_executor/kernels/mhc/triton.py`


##

`mhc_pre_mix_triton(gemm_out, sqrsum, hc_scale, hc_base, hc_mult, hc_hidden_size, rms_eps, hc_pre_eps)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.triton.mhc_pre_mix_triton)

Pre-mix gate for the delayed mHC pre, from AITER's split-k GEMM output.

AITER's `mhc_pre_big_fuse`

consumes the unreduced `[splitk, tokens, hc_mult3]`

GEMM output and the matching row square-sums, but only returns the post and comb gates. The delayed formulation also needs the pre gate, to carry into the next sublayer seam. It is the same slice of the same numbers, so recover it here rather than repeating the projection.

## Source code in `vllm/model_executor/kernels/mhc/triton.py`


##

`rmsnorm_nw(x, eps)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.mhc.triton.rmsnorm_nw)

Weight-free RMSNorm over the last dimension.

Treats *x* as `[num_rows, D]`

where `num_rows = product(shape[:-1])`

. Returns a contiguous tensor with the same shape and dtype as *x*.