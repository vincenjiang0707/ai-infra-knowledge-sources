source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/experts/batched_deep_gemm_moe/
lastmod: 2026-09-23

#

`vllm.model_executor.layers.fused_moe.experts.batched_deep_gemm_moe`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.batched_deep_gemm_moe)

Classes:

Functions:

-
–[persistent_masked_m_silu_mul_quant](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.batched_deep_gemm_moe.persistent_masked_m_silu_mul_quant)Quantize silu(y[..., :H]) * y[..., H:] to FP8 with group per-token scales


##

`BatchedDeepGemmExperts`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.batched_deep_gemm_moe.BatchedDeepGemmExperts)

Bases: [FusedMoEExpertsModular](https://docs.vllm.ai/modular_kernel/#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExpertsModular)

Methods:

-
–[__init__](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.batched_deep_gemm_moe.BatchedDeepGemmExperts.__init__)max_num_tokens: Maximum number of tokens from a DP Rank

-
–[supports_packed_ue8m0_act_scales](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.batched_deep_gemm_moe.BatchedDeepGemmExperts.supports_packed_ue8m0_act_scales)DeepGemm supports packed ue8m0 activation scales on Blackwell-family


## Source code in `vllm/model_executor/layers/fused_moe/experts/batched_deep_gemm_moe.py`


|
|

###

`__init__(moe_config, quant_config, max_num_tokens, num_dispatchers)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.batched_deep_gemm_moe.BatchedDeepGemmExperts.__init__)

max_num_tokens: Maximum number of tokens from a DP Rank num_dispatchers: The number of DP dispatchers. quant_config: Quantization configuration

## Source code in `vllm/model_executor/layers/fused_moe/experts/batched_deep_gemm_moe.py`


###

`supports_packed_ue8m0_act_scales()`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.batched_deep_gemm_moe.BatchedDeepGemmExperts.supports_packed_ue8m0_act_scales)

DeepGemm supports packed ue8m0 activation scales on Blackwell-family GPUs (SM100 datacenter and SM120 consumer).

## Source code in `vllm/model_executor/layers/fused_moe/experts/batched_deep_gemm_moe.py`


##

`persistent_masked_m_silu_mul_quant(y, tokens_per_expert, num_parallel_tokens=16, group_size=128, quant_scale_fmt=DeepGemmQuantScaleFMT.FLOAT32)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.batched_deep_gemm_moe.persistent_masked_m_silu_mul_quant)

Quantize silu(y[..., :H]) * y[..., H:] to FP8 with group per-token scales y has shape (E, T, 2*H). The first half of the last dimension is silu-activated, multiplied by the second half, then quantized into FP8. We launch a fixed grid of threads to accommodate CUDA graphs. Let `P2`

be a parallelization factor for persistent_masked_m_silu_mul_quant over the hidden dimension.

Let `expert_offsets = [0] + [num_tokens.cumsum()]`

and `total_tokens = expert_offsets[-1]`

. persistent_masked_m_silu_mul_quant launches `total_tokens x P2`

number of thread blocks. Each thread block contains `NUM_WARPS`

warps.

Every thread block needs to find it's corresponding expert by warp-parallel scanning over the `expert_offsets`

array.

The i-th warp in the first thread block processes `[i * warp_chunk_size, (i + 1) * warp_chunk_size]`

groups sequentially, where `warp_chunk_size = ((H / GROUP_SIZE) / P2) / NUM_WARPS`

, pipelining loads and computes.

The shared memory layout for 4 warps with a 2-stage pipeline for SiLU V2 can is visualized like so:

```
stage0 stage1
```


┌─────┬───┬─────┬───┬─────┬───┬─────┬───┬─────┬───┬─────┬───┬─────┬───┬─────┬───┐ │gate0│up0│gate1│up1│gate2│up2│gate3│up3│gate0│up0│gate1│up1│gate2│up2│gate3│up3│ └─────┴───┴─────┴───┴─────┴───┴─────┴───┴─────┴───┴─────┴───┴─────┴───┴─────┴───┘

with the main difference between V1 and V2 being the global load stride between warps, and between half-warps. Regarding the latter stride, we assign the first half warp of every warp for `gate`

loads and the second half-warp to `up`

loads.

Returns `(y_q, y_s)`

where * `y_q`

: FP8 tensor, shape (E, T, H), same layout as y[..., :H] * `y_s`

depends on quant_scale_fmt, - quant_scale_fmt == FLOAT32, `y_s`

: FP32 tensor, shape (E, T, H // group_size), strides (T*G, 1, T) - quant_scale_fmt == E8M0, y_s: Int32 tensor, shape (E, T, H // group_size // 4), strides (T*G, 1, T) - quant_scale_fmt == E8M0_FLOAT32_SPARSE

`y_s`

: FP32 tensor, shape (E, T, H // group_size), strides (T*G, 1, T) Let NUM_WARPS be the number of warps in a single thread block and `GROUP_SIZE = 128`

be the size of the quantization group.## Source code in `vllm/model_executor/layers/fused_moe/experts/batched_deep_gemm_moe.py`


|
|