source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/kernels/linear/scaled_mm/xpu/
lastmod: 2026-09-23

#

`vllm.model_executor.kernels.linear.scaled_mm.xpu`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.xpu)

Classes:

##

`XPUFp8BlockScaledMMKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.xpu.XPUFp8BlockScaledMMKernel)

Bases: `Fp8BlockScaledMMLinearKernel`


## Source code in `vllm/model_executor/kernels/linear/scaled_mm/xpu.py`


|
|

###

`_prepare_bmm_params(layer, scale_kn)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.xpu.XPUFp8BlockScaledMMKernel._prepare_bmm_params)

Precompute batched weight and scale for grouped fp8_bmm (e.g. wo_a).

Splits scale [k_blocks, n_blocks] into [G, k_blocks, n_blocks_per_group] and weight [N_total, K] into [G, K, N_per_group] for batch GEMM.

## Source code in `vllm/model_executor/kernels/linear/scaled_mm/xpu.py`


##

`XPUW8A8FP8LinearKernel`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.xpu.XPUW8A8FP8LinearKernel)

Bases: `FP8ScaledMMLinearKernel`


Methods:

-
–[process_weights_after_loading](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.xpu.XPUW8A8FP8LinearKernel.process_weights_after_loading)Ensure weight is stored as C-contiguous [K, N] (KN layout).


## Source code in `vllm/model_executor/kernels/linear/scaled_mm/xpu.py`


|
|

###

`process_weights_after_loading(layer)`

[¶](https://docs.vllm.ai#vllm.model_executor.kernels.linear.scaled_mm.xpu.XPUW8A8FP8LinearKernel.process_weights_after_loading)

Ensure weight is stored as C-contiguous [K, N] (KN layout).

Checkpoints store weight as [N, K]; fp8_gemm requires [K, N], C-contiguous. Three incoming layouts are possible: • [N, K] C-contiguous ← direct checkpoint → .t().contiguous() • [K, N] Fortran-order ← fp8.py's weight.t() → .contiguous() • [K, N] C-contiguous ← already correct → no-op

For square weights (K == N) the shape is ambiguous; contiguity is used as a proxy: C-contiguous ≡ checkpoint [N, K] (needs transpose); Fortran-order ≡ fp8.py already transposed (needs only contiguous).