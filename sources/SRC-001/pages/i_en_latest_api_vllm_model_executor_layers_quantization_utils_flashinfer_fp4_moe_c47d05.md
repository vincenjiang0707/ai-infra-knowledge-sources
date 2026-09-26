source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/utils/flashinfer_fp4_moe/
lastmod: 2026-09-24

#

`vllm.model_executor.layers.quantization.utils.flashinfer_fp4_moe`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.flashinfer_fp4_moe)

Utility helpers for NVFP4 + FlashInfer fused-MoE path.

Functions:

-
–[reorder_w1w3_to_w3w1](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.flashinfer_fp4_moe.reorder_w1w3_to_w3w1)Re-order concatenated

`[w1, w3]`

tensors to`[w3, w1]`

in-place.

##

`interleave_linear_and_gate(x, group_size=64, dim=-1)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.flashinfer_fp4_moe.interleave_linear_and_gate)

Interleave gate and linear weight rows for CuteDSL wrapper.

## Source code in `vllm/model_executor/layers/quantization/utils/flashinfer_fp4_moe.py`


##

`nvfp4_swizzled_scale_to_cutedsl_mma_view(scale)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.flashinfer_fp4_moe.nvfp4_swizzled_scale_to_cutedsl_mma_view)

View a swizzled (E, M_padded, K_sf_padded) block-scale tensor in the MMA layout expected by the CuteDSL MoE kernel.

The returned tensor aliases `scale`

's storage, so in-place updates of the registered Parameter (weight reloads, EPLB rearrangement) are visible to the kernel with no extra bookkeeping.

## Source code in `vllm/model_executor/layers/quantization/utils/flashinfer_fp4_moe.py`


##

`prepare_nvfp4_moe_layer_for_flashinfer_cutedsl(layer, w13, w13_scale, w13_scale_2, a13_scale, w2, w2_scale, w2_scale_2, a2_scale)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.flashinfer_fp4_moe.prepare_nvfp4_moe_layer_for_flashinfer_cutedsl)

Prepare weights for the CuteDSL wrapper-based NvFP4 MoE backend.

Converts weight scale factors to MMA layout expected by CuteDslMoEWrapper, and interleaves w13 gate/linear rows for gated activations. Non-gated activations use a single w13 projection and keep its row order unchanged.

## Source code in `vllm/model_executor/layers/quantization/utils/flashinfer_fp4_moe.py`


##

`prepare_static_weights_for_trtllm_fp4_moe(gemm1_weights, gemm2_weights, gemm1_scales_linear_fp4_bytes, gemm2_scales_linear_fp4_bytes, hidden_size, intermediate_size, num_experts, is_gated_activation)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.flashinfer_fp4_moe.prepare_static_weights_for_trtllm_fp4_moe)

Shuffle NVFP4 weights into the FlashInfer TRT-LLM layout.

## Source code in `vllm/model_executor/layers/quantization/utils/flashinfer_fp4_moe.py`


|
|

##

`reorder_w13_to_w31_for_flashinfer_cutedsl(activation, w13, w13_scale)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.flashinfer_fp4_moe.reorder_w13_to_w31_for_flashinfer_cutedsl)

Normalize gated w13 rows to the [up; gate] order used by FlashInfer.

## Source code in `vllm/model_executor/layers/quantization/utils/flashinfer_fp4_moe.py`


##

`reorder_w1w3_to_w3w1(weight, scale, dim=-2)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.utils.flashinfer_fp4_moe.reorder_w1w3_to_w3w1)

Re-order concatenated `[w1, w3]`

tensors to `[w3, w1]`

in-place.

`weight`

and `scale`

must be contiguous; they remain contiguous on return.