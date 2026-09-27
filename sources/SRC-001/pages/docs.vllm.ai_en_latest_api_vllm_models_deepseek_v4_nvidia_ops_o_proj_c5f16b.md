source: https://docs.vllm.ai/en/latest/api/vllm/models/deepseek_v4/nvidia/ops/o_proj/
lastmod: 2026-09-27

#

`vllm.models.deepseek_v4.nvidia.ops.o_proj`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.nvidia.ops.o_proj)

Functions:

-
–[compute_fp8_einsum_recipe](https://docs.vllm.ai#vllm.models.deepseek_v4.nvidia.ops.o_proj.compute_fp8_einsum_recipe)fp8_einsum recipe + scale layout for the current GPU arch.

-
–[deep_gemm_fp8_o_proj](https://docs.vllm.ai#vllm.models.deepseek_v4.nvidia.ops.o_proj.deep_gemm_fp8_o_proj)O projection: inverse RoPE + grouped wo_a + wo_b.

-
–[rope_quant_attn_out](https://docs.vllm.ai#vllm.models.deepseek_v4.nvidia.ops.o_proj.rope_quant_attn_out)Allocate the output pair the RopeQuant kernel writes.

-
–[rope_quant_unsupported_reason](https://docs.vllm.ai#vllm.models.deepseek_v4.nvidia.ops.o_proj.rope_quant_unsupported_reason)Why

`layer`

cannot take FlashInfer's fused inverse RoPE + FP8 output.

##

`compute_fp8_einsum_recipe(block_size=128)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.nvidia.ops.o_proj.compute_fp8_einsum_recipe)

fp8_einsum recipe + scale layout for the current GPU arch.

SM90 keeps block-row FP32 scales. SM100 uses packed per-row E8M0 scales.

Returns `(einsum_recipe, tma_aligned_scales)`

for `deep_gemm_fp8_o_proj`

.

## Source code in `vllm/models/deepseek_v4/nvidia/ops/o_proj.py`


##

`deep_gemm_fp8_o_proj(o, positions, cos_sin_cache, wo_a, wo_b, *, n_groups, heads_per_group, nope_dim, rope_dim, o_lora_rank, einsum_recipe, tma_aligned_scales)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.nvidia.ops.o_proj.deep_gemm_fp8_o_proj)

O projection: inverse RoPE + grouped wo_a + wo_b.

Shared by the FlashMLA and FlashInfer CUDA backends. The attention layer selects the recipe at initialization. `wo_b`

is any callable over the flattened `z`

: the projection module itself, or a wrapper that also reduce-scatters its output (DeepSeek-V4.1 GEMM-RS).

A QuantizedActivation `o`

was already rotated and cast by the attention kernel, one `wo_a`

group per slot with the live groups first, so only the padding groups are sliced off.

## Source code in `vllm/models/deepseek_v4/nvidia/ops/o_proj.py`


##

`rope_quant_attn_out(num_tokens, device)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.nvidia.ops.o_proj.rope_quant_attn_out)

Allocate the output pair the RopeQuant kernel writes.

Values are group-major, `[num_tokens, 16, 8 * 512]`

over physical `[group, token, K]`

. Scales are MN-major packed UE8M0, one int32 per head over its four 128-wide blocks. Both are what `fp8_einsum`

consumes.

## Source code in `vllm/models/deepseek_v4/nvidia/ops/o_proj.py`


##

`rope_quant_unsupported_reason(layer)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.nvidia.ops.o_proj.rope_quant_unsupported_reason)

Why `layer`

cannot take FlashInfer's fused inverse RoPE + FP8 output.

DSv4 always has 8 heads per `wo_a`

group at any TP size, and the rest of the kernel's fixed shape (head/RoPE dims, per-128 einsum scales, FP32 RoPE cache) is what the SM100 layer uses anyway. What varies is the local head count and the configs the layer also serves unquantized.