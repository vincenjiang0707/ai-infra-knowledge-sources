source: https://docs.vllm.ai/en/latest/api/vllm/models/deepseek_v4/xpu/xpu_qnorm_rope_kv_fp8_insert/
lastmod: 2026-09-24

#

`vllm.models.deepseek_v4.xpu.xpu_qnorm_rope_kv_fp8_insert`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.xpu.xpu_qnorm_rope_kv_fp8_insert)

XPU Triton replacement for fused_deepseek_v4_qnorm_rope_kv_rope_quant_insert.

Does: Q per-head RMSNorm + GPT-J RoPE, KV GPT-J RoPE + UE8M0 FP8 quant + insert. Uses the existing quantize_and_insert_k_cache for the FP8 portion.

Functions:

-
–[xpu_qnorm_rope_kv_fp8_insert](https://docs.vllm.ai#vllm.models.deepseek_v4.xpu.xpu_qnorm_rope_kv_fp8_insert.xpu_qnorm_rope_kv_fp8_insert)XPU Triton: qnorm+rope on Q, rope on KV, then FP8 UE8M0 quant+insert.


##

`_xpu_qnorm_rope_kernel(q_ptr, kv_ptr, kv_out_ptr, position_ids_ptr, cos_sin_cache_ptr, eps, num_tokens, num_heads, HEAD_DIM, ROPE_DIM, NOPE_DIM, HALF_ROPE)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.xpu.xpu_qnorm_rope_kv_fp8_insert._xpu_qnorm_rope_kernel)

Apply per-head RMSNorm + GPT-J RoPE on Q, GPT-J RoPE on KV.

GPT-J interleaved format: pairs are (data[2i], data[2i+1]). cos_sin_cache layout: [max_pos, ROPE_DIM] with first HALF_ROPE=cos, second HALF_ROPE=sin.

## Source code in `vllm/models/deepseek_v4/xpu/xpu_qnorm_rope_kv_fp8_insert.py`


##

`xpu_qnorm_rope_kv_fp8_insert(q, kv, swa_kv_cache, slot_mapping, positions, cos_sin_cache, eps, block_size)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.xpu.xpu_qnorm_rope_kv_fp8_insert.xpu_qnorm_rope_kv_fp8_insert)

XPU Triton: qnorm+rope on Q, rope on KV, then FP8 UE8M0 quant+insert.