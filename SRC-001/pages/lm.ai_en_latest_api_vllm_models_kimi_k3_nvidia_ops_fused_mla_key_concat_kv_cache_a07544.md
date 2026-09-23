source: https://docs.vllm.ai/en/latest/api/vllm/models/kimi_k3/nvidia/ops/fused_mla_key_concat_kv_cache/
lastmod: 2026-09-23

#

`vllm.models.kimi_k3.nvidia.ops.fused_mla_key_concat_kv_cache`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.fused_mla_key_concat_kv_cache)

Fused MLA prefill and decode epilogues for Kimi-K3.

Thin wrappers over the CUDA ops in `csrc/libtorch_stable/fused_kimi_k3_mla_key_concat_kv_cache_kernel.cu`

, which mirror `fused_deepseek_v4_qnorm_rope_kv_rope_full_cache_{bf16,fp8}_insert`

.

`fused_mla_key_concat_kv_cache_insert`

(bf16): optionally apply RoPE, concat the full per-head key`[k_nope | k_pe]`

into`k_out`

, and insert the latent`[kv_c_normed | k_pe]`

into the paged cache.`fused_mla_qkv_quant_kv_cache_fp8_insert`

(fp8): additionally quantize`q`

/`k`

/`v`

to E4M3 with`q_scale`

/`k_scale`

/`v_scale`

(the cache shares`k_scale`

, as in`concat_and_cache_mla`

).`fused_mla_kv_concat`

/`fused_mla_kv_concat_quant_fp8`

(chunked context): the same K concat (plus the fp8 K/V cast) without the cache insert, for context chunks whose latent was gathered back out of the paged cache.

The optional `positions`

/ `cos_sin_cache`

pair enables GPT-J-style RoPE inside the epilogue. Omitting both keeps the K3 NoPE fast path. The kernels use Programmatic Dependent Launch to overlap the tail of the producing GEMMs on sm_90+.

Functions:

-
–[fused_mla_decode_q_concat_kv_cache_insert](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.fused_mla_key_concat_kv_cache.fused_mla_decode_q_concat_kv_cache_insert)Concat the latent decode query

`mqa_q = [ql_nope | q_pe]`

and insert the -
–[fused_mla_key_concat_ds_mla_insert](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.fused_mla_key_concat_kv_cache.fused_mla_key_concat_ds_mla_insert)Concat full K (bf16) and insert the latent in the fp8_ds_mla layout.

-
–[fused_mla_key_concat_kv_cache_insert](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.fused_mla_key_concat_kv_cache.fused_mla_key_concat_kv_cache_insert)Apply optional RoPE, concat K, and insert the paged latent (bf16).

-
–[fused_mla_kv_concat](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.fused_mla_key_concat_kv_cache.fused_mla_kv_concat)Concat

`k = [k_nope | k_pe]`

into a contiguous key, in one launch. -
–[fused_mla_kv_concat_quant_fp8](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.fused_mla_key_concat_kv_cache.fused_mla_kv_concat_quant_fp8)`fused_mla_kv_concat`

plus an fp8 cast of the key and of`v`

. -
–[fused_mla_qkv_quant_kv_cache_fp8_insert](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.fused_mla_key_concat_kv_cache.fused_mla_qkv_quant_kv_cache_fp8_insert)Quantize q/k/v to fp8 and insert the fp8 latent into the paged cache.


##

`fused_mla_decode_q_concat_kv_cache_insert(ql_nope, q_pe, kv_c_normed, k_pe, kv_cache, slot_mapping, *, ds_mla=False, q_scale_inv=None, cache_scale_inv=None, positions=None, cos_sin_cache=None)`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.fused_mla_key_concat_kv_cache.fused_mla_decode_q_concat_kv_cache_insert)

Concat the latent decode query `mqa_q = [ql_nope | q_pe]`

and insert the latent `[kv_c_normed | k_pe]`

into the paged cache, in one launch (runs right before `forward_mqa`

).

## Dispatched by cache format

- bf16 -> bf16 mqa_q, bf16 cache
- plain fp8 -> fp8 mqa_q (q_scale_inv), fp8 cache (cache_scale_inv)
- fp8_ds_mla -> bf16 mqa_q, 656B block-scaled cache

Returns `mqa_q`

of shape `[B, H, kv_lora_rank + qk_rope_head_dim]`

; writes `kv_cache`

in place.

## Source code in `vllm/models/kimi_k3/nvidia/ops/fused_mla_key_concat_kv_cache.py`


|
|

##

`fused_mla_key_concat_ds_mla_insert(q, k_nope, k_pe, kv_c_normed, kv_cache, slot_mapping, positions=None, cos_sin_cache=None)`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.fused_mla_key_concat_kv_cache.fused_mla_key_concat_ds_mla_insert)

Concat full K (bf16) and insert the latent in the fp8_ds_mla layout.

The cache uses DeepSeek's 656-byte block-scaled layout (NoPE in 4 tiles of 128 with per-tile power-of-two scales stored as float32, RoPE as bf16) -- self-scaling, so no scale argument. Returns the bf16 full key; optionally rotates `q`

and writes `kv_cache`

in place.

## Source code in `vllm/models/kimi_k3/nvidia/ops/fused_mla_key_concat_kv_cache.py`


##

`fused_mla_key_concat_kv_cache_insert(q, k_nope, k_pe, kv_c_normed, kv_cache, slot_mapping, positions=None, cos_sin_cache=None)`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.fused_mla_key_concat_kv_cache.fused_mla_key_concat_kv_cache_insert)

Apply optional RoPE, concat K, and insert the paged latent (bf16).

Returns the full key `[Tp, H, qk_nope_head_dim + qk_rope_head_dim]`

; optionally rotates `q`

and writes `kv_cache`

in place.

## Source code in `vllm/models/kimi_k3/nvidia/ops/fused_mla_key_concat_kv_cache.py`


##

`fused_mla_kv_concat(k_nope, k_pe)`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.fused_mla_key_concat_kv_cache.fused_mla_kv_concat)

Concat `k = [k_nope | k_pe]`

into a contiguous key, in one launch.

The chunked-context counterpart of `fused_mla_key_concat_kv_cache_insert`

: no query, no cache insert and no RoPE (the gathered `k_pe`

is already rotated). `k_nope`

is a strided half of one `kv_b_proj`

output and `k_pe`

a strided view of the gather workspace, so neither has to be made contiguous first.

## Source code in `vllm/models/kimi_k3/nvidia/ops/fused_mla_key_concat_kv_cache.py`


##

`fused_mla_kv_concat_quant_fp8(k_nope, k_pe, v)`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.fused_mla_key_concat_kv_cache.fused_mla_kv_concat_quant_fp8)

`fused_mla_kv_concat`

plus an fp8 cast of the key and of `v`

.

`k_pe`

may already be fp8: a plain fp8 cache is gathered without dequantizing, and those bytes are copied through as-is.

Returns contiguous `(k_fp8, v_fp8)`

.

## Source code in `vllm/models/kimi_k3/nvidia/ops/fused_mla_key_concat_kv_cache.py`


##

`fused_mla_qkv_quant_kv_cache_fp8_insert(q, k_nope, k_pe, kv_c_normed, v, kv_cache, slot_mapping, q_scale_inv, k_scale_inv, v_scale_inv, cache_scale_inv, positions=None, cos_sin_cache=None)`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.fused_mla_key_concat_kv_cache.fused_mla_qkv_quant_kv_cache_fp8_insert)

Quantize q/k/v to fp8 and insert the fp8 latent into the paged cache.

The attention key `k_fp8`

and the cache latent use *separate* scales (`k_scale_inv`

vs `cache_scale_inv`

): the cache must be quantized with `_k_scale`

(read back by decode / context), while the prefill attention q/k/v currently stay unscaled (the prefill flash path does not dequantize).

Returns `(q_fp8, k_fp8, v_fp8)`

; writes the fp8 `kv_cache`

in place.