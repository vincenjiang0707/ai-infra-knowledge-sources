source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/experts/cutlass_moe/
lastmod: 2026-09-24

#

`vllm.model_executor.layers.fused_moe.experts.cutlass_moe`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cutlass_moe)

CUTLASS based Fused MoE kernels.

Classes:

-
–[CutlassBatchedExpertsFp8](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cutlass_moe.CutlassBatchedExpertsFp8)Batched CUTLASS FP8 fused MoE expert implementation.

-
–[CutlassExpertsFp4](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cutlass_moe.CutlassExpertsFp4)CUTLASS FP4 fused MoE expert implementation.

-
–[CutlassExpertsFp8](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cutlass_moe.CutlassExpertsFp8)CUTLASS FP8 fused MoE expert implementation.

-
–[CutlassExpertsMxfp4](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cutlass_moe.CutlassExpertsMxfp4)CUTLASS MXFP4 x MXFP4 fused MoE expert implementation.


Functions:

-
–[run_cutlass_moe_fp4](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cutlass_moe.run_cutlass_moe_fp4)MoE implementation for FP4 Inputs.

-
–[run_cutlass_moe_mxfp4](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cutlass_moe.run_cutlass_moe_mxfp4)MXFP4 x MXFP4 MoE implementation using CUTLASS grouped GEMM.

-
–[swizzle_mxfp4_scales](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cutlass_moe.swizzle_mxfp4_scales)Swizzle flat [N, K//32] E8M0 scales to CUTLASS tiled layout.


##

`CutlassBatchedExpertsFp8`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cutlass_moe.CutlassBatchedExpertsFp8)

Bases: `CutlassExpertsFp8Base`


Batched CUTLASS FP8 fused MoE expert implementation.

## Source code in `vllm/model_executor/layers/fused_moe/experts/cutlass_moe.py`


##

`CutlassExpertsFp4`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cutlass_moe.CutlassExpertsFp4)

Bases: [FusedMoEExpertsModular](https://docs.vllm.ai/modular_kernel/#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExpertsModular)

CUTLASS FP4 fused MoE expert implementation.

## Source code in `vllm/model_executor/layers/fused_moe/experts/cutlass_moe.py`


|
|

##

`CutlassExpertsFp8`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cutlass_moe.CutlassExpertsFp8)

Bases: `CutlassExpertsFp8Base`


CUTLASS FP8 fused MoE expert implementation.

## Source code in `vllm/model_executor/layers/fused_moe/experts/cutlass_moe.py`


##

`CutlassExpertsMxfp4`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cutlass_moe.CutlassExpertsMxfp4)

Bases: [FusedMoEExpertsModular](https://docs.vllm.ai/modular_kernel/#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExpertsModular)

CUTLASS MXFP4 x MXFP4 fused MoE expert implementation.

## Source code in `vllm/model_executor/layers/fused_moe/experts/cutlass_moe.py`


|
|

##

`run_cutlass_moe_fp4(output, a, a1_gscale, w1_fp4, w1_blockscale, w1_alphas, a2_gscale, w2_fp4, w2_blockscale, w2_alphas, topk_weights, topk_ids, activation, workspace13, workspace2, m, n, k, e, device, apply_router_weight_on_input=False, *, activation_config=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cutlass_moe.run_cutlass_moe_fp4)

MoE implementation for FP4 Inputs.

### Gemm 1[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cutlass_moe.run_cutlass_moe_fp4--gemm-1)

a: Input tensor: [m, k] (half/bfloat16) a1_gscale: Activation scale per expert: [e] (float32) w1 (not an argument to cutlass_moe_fp4): [e, w1_n, k] w1_fp4: [e, w1_n, k // 2], dtype: torch.uint8 (stacked fp4: E2M1) where w1_n = 2*n for gated activations (gate+up), n for non-gated (up only). (Note: `n`

is the up projection output dim, `k`

is the input dim in full precision) w1_blockscale: [e, w1_n, k // block_size] (float8_e4m3) (Block size = 16 for NVFP4)

### Gemm 2[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cutlass_moe.run_cutlass_moe_fp4--gemm-2)

a2_gscale: Activation scale per expert: [e] w2(down projection) (not an argument to cutlass_moe_fp4): [e, k, n] w2_fp4: [e, k, n // 2], dtype: torch.uint8 (stacked E2M1) w2_blockscale: [e, k, n // block_size], dtype: float8_e4m3

topk_weights: [m, topk] dtype: float8 topk_ids: [m, topk] dtype: float8

m, n, k: Unquantized weight shapes, dtype: int e: number of experts, dtype: int

assumes that topk < k < n to satisfy - up/down projection expectations.

## Source code in `vllm/model_executor/layers/fused_moe/experts/cutlass_moe.py`


|
|

##

`run_cutlass_moe_mxfp4(output, a, w1_fp4, w1_blockscale, w2_fp4, w2_blockscale, topk_weights, topk_ids, activation, workspace13, workspace2, m, n, k, e, device, apply_router_weight_on_input=False, *, activation_config=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cutlass_moe.run_cutlass_moe_mxfp4)

MXFP4 x MXFP4 MoE implementation using CUTLASS grouped GEMM.

## Source code in `vllm/model_executor/layers/fused_moe/experts/cutlass_moe.py`


|
|

##

`swizzle_mxfp4_scales(scales, N, K)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cutlass_moe.swizzle_mxfp4_scales)

Swizzle flat [N, K//32] E8M0 scales to CUTLASS tiled layout.

## CUTLASS expects MX scale factors in a tiled layout

[numMTiles, numKTiles, 32, 4, 4]

where numMTiles = ceil(N/128), numKTiles = ceil(K/128), and the inner dimensions correspond to the swizzle pattern: mTileIdx = mIdx / 128 outerMIdx = mIdx % 32 innerMIdx = (mIdx / 32) % 4 kTileIdx = kIdx / 4 innerKIdx = kIdx % 4 with kIdx = col_in_scale_space (i.e., index into K//32).