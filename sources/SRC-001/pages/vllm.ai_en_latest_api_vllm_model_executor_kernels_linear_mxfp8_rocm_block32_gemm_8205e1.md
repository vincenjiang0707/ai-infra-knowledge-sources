source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/kernels/linear/mxfp8/rocm_block32_gemm/
lastmod: 2026-09-27

#

`vllm.model_executor.kernels.linear.mxfp8.rocm_block32_gemm`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mxfp8.rocm_block32_gemm)

MXFP8 GEMM on 32x32 block-scaled weights for gfx950 (`tl.dot_scaled`

).

`y = x @ w.T`

with an MXFP8 activation (e4m3 values, one E8M0 scale per row and 32 K, `[M, K / 32]`

) and an e4m3 weight whose E8M0 scales stay in the checkpoint's 32x32 blocks, `[N / 32, K / 32]`

, instead of being expanded to every row. Each weight scale byte is then read once per 32 output rows, and small-M shapes can use the packed kernel below.

Two kernels, picked per shape from a table tuned on MI355X:

- a tiled kernel for larger M;
- a packed kernel for small M, which fills the MFMA's rows with K panels instead of tokens and keeps only the matching-panel (block-diagonal) products, so a handful of tokens still streams the weight at full width.

Either can split K. The partials are normally summed in the same launch by the last program of each output tile to finish, in split order, so the result does not depend on scheduling. Otherwise a second launch reduces them.

The packed kernel and the in-launch split-K reduction on one XCD (`_split_tile`

, `_sum_splits`

, `_split_counters`

, `_k_partition`

) are adapted from the group32 GEMM in ROCm/aiter#5750.

Functions:

-
–[rocm_mxfp8_block32_gemm](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mxfp8.rocm_block32_gemm.rocm_mxfp8_block32_gemm)`x @ weight.T`

for MXFP8`x`

and a 32x32 block-scaled MXFP8 weight.

##

`_default_config(M, N, K)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mxfp8.rocm_block32_gemm._default_config)

Untuned shapes: the tiers most tuned shapes settle on.

## Source code in `vllm/model_executor/kernels/linear/mxfp8/rocm_block32_gemm.py`


##

`_k_partition(K, splits, step)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mxfp8.rocm_block32_gemm._k_partition)

K per split, rounded up to whole steps, and the number of non-empty splits.

## Source code in `vllm/model_executor/kernels/linear/mxfp8/rocm_block32_gemm.py`


##

`_split_counters(device)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mxfp8.rocm_block32_gemm._split_counters)

Zeroed arrival counters, one set per stream so concurrent launches never share a tile's counter. Each launch leaves the counters it used at zero.

None when a stream first needs them inside a CUDA graph capture: that allocation would come from the graph's pool, where it can take the address of an intermediate that every replay overwrites. vLLM warms up on its capture streams first, so this only affects captures without a warmup.

## Source code in `vllm/model_executor/kernels/linear/mxfp8/rocm_block32_gemm.py`


##

`_split_tile(N, BLOCK_N, SPLITS)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mxfp8.rocm_block32_gemm._split_tile)

(pid_m, pid_n, tile, split) of a 1D grid that keeps a tile's splits on one XCD, so they meet in that XCD's L2.

## Source code in `vllm/model_executor/kernels/linear/mxfp8/rocm_block32_gemm.py`


##

`_sum_splits(acc, out_ptrs, out_mask, slot_ptr, count_ptr, split, SPLITS)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mxfp8.rocm_block32_gemm._sum_splits)

Publish this split's partial; the tile's last arrival sums all of them in split order and re-arms the counter.

## Source code in `vllm/model_executor/kernels/linear/mxfp8/rocm_block32_gemm.py`


##

`rocm_mxfp8_block32_gemm(x, x_scale, weight, weight_scale, out_dtype)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mxfp8.rocm_block32_gemm.rocm_mxfp8_block32_gemm)

`x @ weight.T`

for MXFP8 `x`

and a 32x32 block-scaled MXFP8 weight.

Parameters:

-

(`x`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mxfp8.rocm_block32_gemm.rocm_mxfp8_block32_gemm(x))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[M, K] e4m3 activation, contiguous.

-

(`x_scale`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mxfp8.rocm_block32_gemm.rocm_mxfp8_block32_gemm(x_scale))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[M, K / 32] E8M0 (uint8) activation scales.

-

(`weight`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mxfp8.rocm_block32_gemm.rocm_mxfp8_block32_gemm(weight))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[N, K] e4m3 weight, contiguous.

-

(`weight_scale`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mxfp8.rocm_block32_gemm.rocm_mxfp8_block32_gemm(weight_scale))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[ceil(N / 32), K / 32] E8M0 (uint8) weight block scales.

-

(`out_dtype`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.mxfp8.rocm_block32_gemm.rocm_mxfp8_block32_gemm(out_dtype))

) –[dtype](https://pytorch.org/docs/stable/tensor_attributes.html#torch.dtype)Output dtype.


Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)The [M, N] product.