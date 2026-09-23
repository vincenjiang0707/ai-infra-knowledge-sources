source: https://docs.vllm.ai/en/latest/api/vllm/models/deepseek_v4/common/ops/
lastmod: 2026-09-23

#

`vllm.models.deepseek_v4.common.ops`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.ops)

Modules:

-
–[cache_utils](https://docs.vllm.ai/cache_utils/#vllm.models.deepseek_v4.common.ops.cache_utils)Triton kernels for DeepseekV4 paged K-cache management and sparse-attention index

-
–[fused_compress_quant_cache](https://docs.vllm.ai/fused_compress_quant_cache/#vllm.models.deepseek_v4.common.ops.fused_compress_quant_cache)Fused compressor + FP8/MXFP4 UE8M0 quantization + KV cache insert kernels.

-
–[fused_indexer_q](https://docs.vllm.ai/fused_indexer_q/#vllm.models.deepseek_v4.common.ops.fused_indexer_q) -
–[fused_inv_rope_fp8_quant](https://docs.vllm.ai/fused_inv_rope_fp8_quant/#vllm.models.deepseek_v4.common.ops.fused_inv_rope_fp8_quant)Fused inverse RoPE + block-scaled FP8 quantization kernel for DeepseekV4 attention.

-
–[fused_mtp_input_rmsnorm](https://docs.vllm.ai/fused_mtp_input_rmsnorm/#vllm.models.deepseek_v4.common.ops.fused_mtp_input_rmsnorm)Fused MTP-input RMSNorm: enorm (with mask-zero at position 0) + hnorm.

-
–[save_partial_states](https://docs.vllm.ai/save_partial_states/#vllm.models.deepseek_v4.common.ops.save_partial_states)

Functions:

-
–[build_flashinfer_mixed_sparse_indices](https://docs.vllm.ai#vllm.models.deepseek_v4.common.ops.build_flashinfer_mixed_sparse_indices)Build the FlashInfer DSV4 sparse-index matrix for decode-first batches.

-
–[compute_global_topk_indices_and_lens](https://docs.vllm.ai#vllm.models.deepseek_v4.common.ops.compute_global_topk_indices_and_lens)Map local topk indices to global KV cache slots and count valid entries.

-
–[dequantize_and_gather_k_cache](https://docs.vllm.ai#vllm.models.deepseek_v4.common.ops.dequantize_and_gather_k_cache)Dequantize and gather a paged DSv4 K cache.

-
–[fused_indexer_q_rope_quant](https://docs.vllm.ai#vllm.models.deepseek_v4.common.ops.fused_indexer_q_rope_quant)Fused RoPE + quantize Q for the sparse indexer.

-
–[quantize_and_insert_k_cache](https://docs.vllm.ai#vllm.models.deepseek_v4.common.ops.quantize_and_insert_k_cache)Quantize K tensor and insert into paged K cache.


##

`build_flashinfer_mixed_sparse_indices(decode_swa_indices, decode_compressed_indices, decode_compressed_topk_lens, prefill_topk_indices, query_start_loc, seq_lens, token_to_req_indices, swa_block_table, swa_block_size, compressed_block_table, compressed_block_size, window_size, compress_ratio, topk, decode_compressed_indices_are_local=False, decode_is_valid_token=None, swa_block_span=None, compressed_block_span=None, prefill_left_visible=None, prefill_right_visible=None, max_image_tokens=0)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.ops.build_flashinfer_mixed_sparse_indices)

Build the FlashInfer DSV4 sparse-index matrix for decode-first batches.

Produces `sparse_indices`

of shape `[num_tokens, swa_total_width + padded_topk]`

(the first `swa_total_width`

columns are SWA slot ids, the rest are compressed/top-k slot ids) and `sparse_topk_lens`

(active length per token). Decode tokens read precomputed SWA/compressed indices; prefill tokens derive their SWA window from the position and translate local compressed indices to global slots via the block tables.

When `prefill_left_visible`

/`prefill_right_visible`

are given (vision variant), the SWA column region widens by `max_image_tokens`

and prefill tokens inside an image span get a bidirectionally widened window; decode rows are padded with -1 across the extra columns.

## Source code in `vllm/models/deepseek_v4/common/ops/cache_utils.py`


|
|

##

`compute_global_topk_indices_and_lens(topk_indices, token_to_req_indices, block_table, block_size, is_valid_token)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.ops.compute_global_topk_indices_and_lens)

Map local topk indices to global KV cache slots and count valid entries.

Fuses three operations into a single kernel: 1. Block-table lookup (local index → global slot id) 2. Valid-entry counting (topk_lens per token) 3. Masking padding tokens to length 0

## Source code in `vllm/models/deepseek_v4/common/ops/cache_utils.py`


##

`dequantize_and_gather_k_cache(out, k_cache, seq_lens, gather_lens, block_table, block_size, offset, use_fnuz=False)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.ops.dequantize_and_gather_k_cache)

Dequantize and gather a paged DSv4 K cache.

`use_fnuz`

MUST match the encoder of the specific cache being read: `False`

for `compressed_k_cache`

(Triton encoder is OCP everywhere), `current_platform.is_fp8_fnuz()`

for `swa_k_cache`

(C++ encoder writes FNUZ on gfx942 and OCP on gfx950).

## Source code in `vllm/models/deepseek_v4/common/ops/cache_utils.py`


##

`fused_indexer_q_rope_quant(positions, index_q, index_q_cos_sin_cache, index_weights, index_weights_softmax_scale, index_weights_head_scale, use_fp4=False, weights_out_dtype=torch.float32)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.ops.fused_indexer_q_rope_quant)

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

`quantize_and_insert_k_cache(k, k_cache, slot_mapping, block_size=64, is_ue8m0=True, use_fnuz=False)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.ops.quantize_and_insert_k_cache)

Quantize K tensor and insert into paged K cache.

K Cache block layout (block_size=64 tokens): - First 64 * 576 = 36864 bytes: Token data - Each token: 448 bytes (fp8) + 128 bytes (bf16) - Next 64 * 8 = 512 bytes: Scales - Each token: 8 bytes (uint8 scales, 7 real + 1 padding) - Padded to multiple of 576

`use_fnuz=True`

selects FNUZ E4M3 cache encoding and is only valid on platforms whose FP8 format is FNUZ. `use_fnuz=False`

selects OCP E4M3, which is used by OCP-encoded caches even on gfx942.