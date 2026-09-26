source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/experts/nvfp4_emulation_moe/
lastmod: 2026-09-24

#

`vllm.model_executor.layers.fused_moe.experts.nvfp4_emulation_moe`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.nvfp4_emulation_moe)

NVFP4 quantization emulation for MoE.

This file implements NVFP4 emulation for NVFP4 MOE in case the hardware used does not natively support NVFP4 MOE.

Weights are dequantized on the fly during each forward, we fall back to calling `TritonExperts`

using BF16, and fake NVFP4 quantize-dequantize is applied on `a13`

, `a2`

.

Classes:

-
–[Nvfp4QuantizationEmulationTritonExperts](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.nvfp4_emulation_moe.Nvfp4QuantizationEmulationTritonExperts)Extension of TritonExperts to support emulated NVFP4 MoE experts.


Functions:

-
–[fused_moe_nvfp4_emulation_kernel](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.nvfp4_emulation_moe.fused_moe_nvfp4_emulation_kernel)Fused MoE kernel for emulated NVFP4 weight-only dequantization + GEMM.

-
–[invoke_fused_moe_nvfp4_emulation_kernel](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.nvfp4_emulation_moe.invoke_fused_moe_nvfp4_emulation_kernel)Launch the fused NVFP4 emulation MoE kernel.


##

`Nvfp4QuantizationEmulationTritonExperts`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.nvfp4_emulation_moe.Nvfp4QuantizationEmulationTritonExperts)

Bases: [TritonExperts](https://docs.vllm.ai/triton_moe/#vllm.model_executor.layers.fused_moe.experts.triton_moe.TritonExperts)

Extension of TritonExperts to support emulated NVFP4 MoE experts.

It may be used for NVFP4 models when the device does not have native support for this dtype.

Methods:

-
–[apply](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.nvfp4_emulation_moe.Nvfp4QuantizationEmulationTritonExperts.apply)Apply emulated quantized MoE computation.


## Source code in `vllm/model_executor/layers/fused_moe/experts/nvfp4_emulation_moe.py`


|
|

###

`apply(output, hidden_states, w1, w2, topk_weights, topk_ids, activation, global_num_experts, expert_map, a1q_scale, a2_scale, workspace13, workspace2, expert_tokens_meta, apply_router_weight_on_input)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.nvfp4_emulation_moe.Nvfp4QuantizationEmulationTritonExperts.apply)

Apply emulated quantized MoE computation.

This dequantizes the weights on the fly and calls fused_experts_impl with activation quantization support.

## Source code in `vllm/model_executor/layers/fused_moe/experts/nvfp4_emulation_moe.py`


|
|

##

`fused_moe_nvfp4_emulation_kernel(a_ptr, b_ptr, c_ptr, b_scale_ptr, w_global_scale_ptr, topk_weights_ptr, sorted_token_ids_ptr, expert_ids_ptr, num_tokens_post_padded_ptr, N, K, EM, num_valid_tokens, stride_am, stride_ak, stride_be, stride_bk, stride_bn, stride_cm, stride_cn, stride_bse, stride_bsk, stride_bsn, block_k_diviable, BLOCK_SIZE_M, BLOCK_SIZE_N, BLOCK_SIZE_K, GROUP_SIZE_M, MUL_ROUTED_WEIGHT, top_k, compute_type, group_size)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.nvfp4_emulation_moe.fused_moe_nvfp4_emulation_kernel)

Fused MoE kernel for emulated NVFP4 weight-only dequantization + GEMM.

Activations A are BF16 (already QDQ'd externally). Weights B are packed uint8 NVFP4 [E, N, K//2] — two FP4 values per byte along the K dimension. B_scale holds per-block FP8-E4M3 scales [E, N, K // group_size]. w_global_scale is a per-expert scalar global scale.

## The dequantization formula per element is

w_float = e2m1_decode(nibble) * (block_scale_fp8 * global_scale)

Weight loading optimization: each packed byte is loaded exactly once as a [BLOCK_SIZE_N, BLOCK_SIZE_K // 2] tile (N-major), both nibbles are extracted, decoded and scaled, then tl.interleave produces the [BLOCK_SIZE_N, BLOCK_SIZE_K] dequantized tile which is transposed to [BLOCK_SIZE_K, BLOCK_SIZE_N] for tl.dot.

## Source code in `vllm/model_executor/layers/fused_moe/experts/nvfp4_emulation_moe.py`


|
|

##

`invoke_fused_moe_nvfp4_emulation_kernel(A, B, C, B_scale, act_global_scale, w_global_scale, topk_weights, sorted_token_ids, expert_ids, num_tokens_post_padded, mul_routed_weight, top_k, config, compute_type)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.nvfp4_emulation_moe.invoke_fused_moe_nvfp4_emulation_kernel)

Launch the fused NVFP4 emulation MoE kernel.

B has shape [E, N, K_packed] where K_packed = K // 2 (two FP4 per byte). B_scale has shape [E, N, K // group_size] in FP8-E4M3 (stored as uint8). w_global_scale has shape [E] (per-expert scalar).

## Source code in `vllm/model_executor/layers/fused_moe/experts/nvfp4_emulation_moe.py`


|
|