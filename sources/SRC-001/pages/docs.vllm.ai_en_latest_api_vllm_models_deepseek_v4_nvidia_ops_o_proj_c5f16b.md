source: https://docs.vllm.ai/en/latest/api/vllm/models/deepseek_v4/nvidia/ops/o_proj/
lastmod: 2026-09-24

#

`vllm.models.deepseek_v4.nvidia.ops.o_proj`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.nvidia.ops.o_proj)

Functions:

-
–[compute_fp8_einsum_recipe](https://docs.vllm.ai#vllm.models.deepseek_v4.nvidia.ops.o_proj.compute_fp8_einsum_recipe)fp8_einsum recipe + scale layout for the current GPU arch.

-
–[deep_gemm_fp8_o_proj](https://docs.vllm.ai#vllm.models.deepseek_v4.nvidia.ops.o_proj.deep_gemm_fp8_o_proj)O projection: inverse RoPE + grouped wo_a + wo_b.


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