source: https://docs.vllm.ai/en/latest/api/vllm/models/deepseek_v41/common/ops/
lastmod: 2026-09-24

#

`vllm.models.deepseek_v41.common.ops`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops)

DeepSeek V4.1 fused ops.

Single bridging point for the kernels V4.1 shares verbatim with V4: the re-exports below are the only place this package reaches into `vllm.models.deepseek_v4`

, so submodules import them from `.`

instead of naming the V4 path themselves. Keep these imports above the `.`

-relative ones — `indexer_k_store`

reads them off this partially-initialized module.

Modules:

-
–[cache_utils](https://docs.vllm.ai/cache_utils/#vllm.models.deepseek_v41.common.ops.cache_utils)Triton kernels for DeepseekV4 paged K-cache management and sparse-attention index

-
–[fused_compress_quant_cache](https://docs.vllm.ai/fused_compress_quant_cache/#vllm.models.deepseek_v41.common.ops.fused_compress_quant_cache)V4.1 state saving/compression and independently schedulable cache insertion.

-
–[fused_layout](https://docs.vllm.ai/fused_layout/#vllm.models.deepseek_v41.common.ops.fused_layout)Weight permutations for FlashMLA's mega-attention kernel.

-
–[indexer_k_store](https://docs.vllm.ai/indexer_k_store/#vllm.models.deepseek_v41.common.ops.indexer_k_store)Indexer K production for DeepSeek V4.1 kv-source layers.

-
–[query_quant](https://docs.vllm.ai/query_quant/#vllm.models.deepseek_v41.common.ops.query_quant)

Functions:

-
–[build_flashinfer_mixed_sparse_indices](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.build_flashinfer_mixed_sparse_indices)Build the FlashInfer DSV4 sparse-index matrix for decode-first batches.

-
–[compute_global_topk_indices_and_lens](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.compute_global_topk_indices_and_lens)Map local topk indices to global KV cache slots and count valid entries.

-
–[dequantize_and_gather_k_cache](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.dequantize_and_gather_k_cache)Dequantize and gather a paged DSv4 K cache.

-
–[fused_indexer_q_rope_quant](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.fused_indexer_q_rope_quant)Fused RoPE + quantize Q for the sparse indexer.

-
–[fused_inv_rope_fp8_quant](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.fused_inv_rope_fp8_quant)Fused inverse RoPE + block-scaled FP8 quantization.

-
–[indexer_k_norm_rope_store](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.indexer_k_norm_rope_store)k_norm → RoPE → quant → paged store for indexer keys.

-
–[quantize_and_insert_k_cache](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.quantize_and_insert_k_cache)Quantize K tensor and insert into paged K cache.


##

`build_flashinfer_mixed_sparse_indices(decode_swa_indices, decode_compressed_indices, decode_compressed_topk_lens, prefill_topk_indices, query_start_loc, seq_lens, token_to_req_indices, swa_block_table, swa_block_size, compressed_block_table, compressed_block_size, window_size, compress_ratio, topk, decode_compressed_indices_are_local=False, decode_is_valid_token=None, swa_block_span=None, compressed_block_span=None, *, replay_start)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.build_flashinfer_mixed_sparse_indices)

Build the FlashInfer DSV4 sparse-index matrix for decode-first batches.

Produces `sparse_indices`

of shape `[num_tokens, swa_total_width + padded_topk]`

(the first `swa_total_width`

columns are SWA slot ids, the rest are compressed/top-k slot ids) and `sparse_topk_lens`

(active length per token). Decode tokens read precomputed SWA/compressed indices; prefill tokens derive their SWA window from the position and translate local compressed indices to global slots via the block tables.

`replay_start`

([num_reqs], SWA bounded replay) lower-bounds every prefill token's window: positions below it hold no window KV.

## Source code in `vllm/models/deepseek_v41/common/ops/cache_utils.py`


|
|

##

`compute_global_topk_indices_and_lens(topk_indices, token_to_req_indices, block_table, block_size, is_valid_token)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.compute_global_topk_indices_and_lens)

Map local topk indices to global KV cache slots and count valid entries.

Fuses three operations into a single kernel: 1. Block-table lookup (local index → global slot id) 2. Valid-entry counting (topk_lens per token) 3. Masking padding tokens to length 0

## Source code in `vllm/models/deepseek_v41/common/ops/cache_utils.py`


##

`dequantize_and_gather_k_cache(out, k_cache, seq_lens, gather_lens, block_table, block_size, offset, use_fnuz=False)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.dequantize_and_gather_k_cache)

Dequantize and gather a paged DSv4 K cache.

The record is read off `k_cache.shape[-1]`

; see the module header. Only the fp8 records have a CuteDSL gather, so NVFP4 always takes the Triton path.

`use_fnuz`

MUST match the encoder of the specific cache being read: `False`

for `compressed_k_cache`

(Triton encoder is OCP everywhere), `current_platform.is_fp8_fnuz()`

for `swa_k_cache`

(C++ encoder writes FNUZ on gfx942 and OCP on gfx950).

## Source code in `vllm/models/deepseek_v41/common/ops/cache_utils.py`


##

`fused_indexer_q_rope_quant(positions, index_q, index_q_cos_sin_cache, index_weights, index_weights_softmax_scale, index_weights_head_scale, use_fp4=False, weights_out_dtype=torch.float32)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.fused_indexer_q_rope_quant)

Fused RoPE + quantize Q for the sparse indexer.

`weights_out_dtype`

is the dtype the downstream scoring kernel takes: fp32 for the dense MQA-logits kernels, bf16 for DeepGEMM's sparse MQA-logits kernels (CUDA MXFP4 path only).

Weight-fold semantics (important — the two paths differ):

FP8 path (use_fp4=False, default): q_fp8 : (T, H, HEAD_DIM) platform fp8 (e4m3fnuz on gfx942, e4m3fn elsewhere); per-token-per-head scalar scale (NOT stored — folded into weights below) weights_out = weights * q_scale * softmax_scale * head_scale Rationale: a single per-token q_scale is a scalar the downstream FP8 logits kernel would otherwise multiply in. Folding it into `weights`

avoids emitting a separate tensor and is free for the logits kernel.

MXFP4 path (use_fp4=True): q_packed : (T, H, HEAD_DIM // 2) uint8 (2 E2M1 nibbles per byte) q_scale : (T, H, HEAD_DIM // MXFP4_BLOCK_SIZE) uint8 ue8m0 bytes weights_out = weights * softmax_scale * head_scale Rationale: MXFP4 has PER-BLOCK (32-element) scales that live with the Q values — they cannot be folded into a per-token weight scalar, so `weights`

carries only the softmax and head scales.

Returns (q_quant, weights_out) where q_quant is either a Tensor (FP8) or a (values, scales) tuple (MXFP4). This matches the union type accepted by `SparseAttnIndexer.forward_*`

.

## Source code in `vllm/models/deepseek_v4/common/ops/fused_indexer_q.py`


|
|

##

`fused_inv_rope_fp8_quant(o, positions, cos_sin_cache, n_groups, heads_per_group, nope_dim=448, rope_dim=64, quant_group_size=128, tma_aligned_scales=False, quantize=True)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.fused_inv_rope_fp8_quant)

Fused inverse RoPE + block-scaled FP8 quantization.

Parameters:

-

(`o`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.fused_inv_rope_fp8_quant(o))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Attention output [num_tokens, num_heads, head_dim] bf16.

-

(`positions`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.fused_inv_rope_fp8_quant(positions))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Token positions [num_tokens] int64.

-

(`cos_sin_cache`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.fused_inv_rope_fp8_quant(cos_sin_cache))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Precomputed [max_pos, rope_dim] with cos||sin.

-

(`n_groups`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.fused_inv_rope_fp8_quant(n_groups))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of output groups.

-

(`heads_per_group`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.fused_inv_rope_fp8_quant(heads_per_group))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Heads per group.

-

(`nope_dim`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.fused_inv_rope_fp8_quant(nope_dim))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`448`

) –Non-RoPE dimensions per head (default 448).

-

(`rope_dim`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.fused_inv_rope_fp8_quant(rope_dim))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`64`

) –RoPE dimensions per head (default 64).

-

(`quant_group_size`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.fused_inv_rope_fp8_quant(quant_group_size))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`128`

) –FP8 quantization block size (default 128).

-

(`tma_aligned_scales`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.fused_inv_rope_fp8_quant(tma_aligned_scales))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –Output INT32 packed UE8M0 for SM100 (True) or FP32 for SM90 (False).

-

(`quantize`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.fused_inv_rope_fp8_quant(quantize))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`True`

) –Quantize the rotated output to FP8 and return its scales.


Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Rotated output in [T, G, D] and its FP8 scales. The scale tensor is

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)empty when quantization is disabled.


## Source code in `vllm/models/deepseek_v4/common/ops/fused_inv_rope_fp8_quant.py`


|
|

##

`indexer_k_norm_rope_store(k_pre, positions, cos_sin_cache, rms_norm_weight, rms_norm_eps, k_cache, kv_slot_mapping, compress_ratio, use_fp4_cache)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.indexer_k_norm_rope_store)

k_norm → RoPE → quant → paged store for indexer keys.

Parameters:

-

(`k_pre`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.indexer_k_norm_rope_store(k_pre))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[num_tokens, 128] bf16, the

`wk(latent)`

projection. Only group-boundary rows are read. -

(`positions`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.indexer_k_norm_rope_store(positions))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[num_tokens] int64 token positions.

-

(`cos_sin_cache`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.indexer_k_norm_rope_store(cos_sin_cache))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[max_pos, rope_head_dim] GPT-J layout (cos half, then sin half), from the layer's compress-RoPE instance.

-

(`rms_norm_weight`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.indexer_k_norm_rope_store(rms_norm_weight))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[128] k_norm weight.

-

(`rms_norm_eps`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.indexer_k_norm_rope_store(rms_norm_eps))

) –[float](https://docs.python.org/3/builtins/functions.html#float)Epsilon of the k_norm RMSNorm.

-

(`k_cache`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.indexer_k_norm_rope_store(k_cache))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)uint8 paged indexer cache [num_blocks, block_size, row_bytes].

-

(`kv_slot_mapping`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.indexer_k_norm_rope_store(kv_slot_mapping))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[num_tokens] slots in the indexer cache (-1 = skip).

-

(`compress_ratio`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.indexer_k_norm_rope_store(compress_ratio))

) –[int](https://docs.python.org/3/builtins/functions.html#int)group size; keys are emitted at group boundaries.

-

(`use_fp4_cache`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.indexer_k_norm_rope_store(use_fp4_cache))

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)MXFP4 (2 nibbles/byte + ue8m0 per 32) when True, else per-token FP8 with a single fp32 scale.


## Source code in `vllm/models/deepseek_v41/common/ops/indexer_k_store.py`


##

`quantize_and_insert_k_cache(k, k_cache, slot_mapping, block_size=64, is_ue8m0=True, use_fnuz=False, bytes_per_token=V4_BYTES_PER_TOKEN)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.quantize_and_insert_k_cache)

Quantize K tensor and insert into paged K cache.

`bytes_per_token`

picks the record (see the module header): the V4 one, or V4.1's all-dims MXFP8 one.

`use_fnuz=True`

selects FNUZ E4M3 cache encoding and is only valid on platforms whose FP8 format is FNUZ. `use_fnuz=False`

selects OCP E4M3, which is used by OCP-encoded caches even on gfx942.

## Source code in `vllm/models/deepseek_v41/common/ops/cache_utils.py`


|
|