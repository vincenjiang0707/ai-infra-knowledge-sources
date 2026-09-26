source: https://docs.vllm.ai/en/latest/api/vllm/models/deepseek_v4/common/ops/cache_utils/
lastmod: 2026-09-24

#

`vllm.models.deepseek_v4.common.ops.cache_utils`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.ops.cache_utils)

Triton kernels for DeepseekV4 paged K-cache management and sparse-attention index preparation.

- quantize_and_insert_k_cache: quantize bf16 K to UE8M0 FP8 and insert into the paged cache.
- dequantize_and_gather_k_cache: gather and dequantize FP8 K from the paged cache for sparse/SWA prefill.
- compute_global_topk_indices_and_lens: map local topk indices to global KV cache slots and count valid entries.
- combine_topk_swa_indices: concatenate topk compressed indices with SWA window indices for sparse prefill.

Functions:

-
–[build_flashinfer_mixed_sparse_indices](https://docs.vllm.ai#vllm.models.deepseek_v4.common.ops.cache_utils.build_flashinfer_mixed_sparse_indices)Build the FlashInfer DSV4 sparse-index matrix for decode-first batches.

-
–[compute_global_topk_indices_and_lens](https://docs.vllm.ai#vllm.models.deepseek_v4.common.ops.cache_utils.compute_global_topk_indices_and_lens)Map local topk indices to global KV cache slots and count valid entries.

-
–[dequantize_and_gather_k_cache](https://docs.vllm.ai#vllm.models.deepseek_v4.common.ops.cache_utils.dequantize_and_gather_k_cache)Dequantize and gather a paged DSv4 K cache.

-
–[quantize_and_insert_k_cache](https://docs.vllm.ai#vllm.models.deepseek_v4.common.ops.cache_utils.quantize_and_insert_k_cache)Quantize K tensor and insert into paged K cache.

-
–[quantize_and_insert_k_kernel](https://docs.vllm.ai#vllm.models.deepseek_v4.common.ops.cache_utils.quantize_and_insert_k_kernel)Quantize K tensor and insert into paged K cache.


##

`build_flashinfer_mixed_sparse_indices(decode_swa_indices, decode_compressed_indices, decode_compressed_topk_lens, prefill_topk_indices, query_start_loc, seq_lens, token_to_req_indices, swa_block_table, swa_block_size, compressed_block_table, compressed_block_size, window_size, compress_ratio, topk, decode_compressed_indices_are_local=False, decode_is_valid_token=None, swa_block_span=None, compressed_block_span=None, prefill_left_visible=None, prefill_right_visible=None, max_image_tokens=0)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.ops.cache_utils.build_flashinfer_mixed_sparse_indices)

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

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.ops.cache_utils.compute_global_topk_indices_and_lens)

Map local topk indices to global KV cache slots and count valid entries.

Fuses three operations into a single kernel: 1. Block-table lookup (local index → global slot id) 2. Valid-entry counting (topk_lens per token) 3. Masking padding tokens to length 0

## Source code in `vllm/models/deepseek_v4/common/ops/cache_utils.py`


##

`dequantize_and_gather_k_cache(out, k_cache, seq_lens, gather_lens, block_table, block_size, offset, use_fnuz=False)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.ops.cache_utils.dequantize_and_gather_k_cache)

Dequantize and gather a paged DSv4 K cache.

`use_fnuz`

MUST match the encoder of the specific cache being read: `False`

for `compressed_k_cache`

(Triton encoder is OCP everywhere), `current_platform.is_fp8_fnuz()`

for `swa_k_cache`

(C++ encoder writes FNUZ on gfx942 and OCP on gfx950).

## Source code in `vllm/models/deepseek_v4/common/ops/cache_utils.py`


##

`quantize_and_insert_k_cache(k, k_cache, slot_mapping, block_size=64, is_ue8m0=True, use_fnuz=False)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.ops.cache_utils.quantize_and_insert_k_cache)

Quantize K tensor and insert into paged K cache.

K Cache block layout (block_size=64 tokens): - First 64 * 576 = 36864 bytes: Token data - Each token: 448 bytes (fp8) + 128 bytes (bf16) - Next 64 * 8 = 512 bytes: Scales - Each token: 8 bytes (uint8 scales, 7 real + 1 padding) - Padded to multiple of 576

`use_fnuz=True`

selects FNUZ E4M3 cache encoding and is only valid on platforms whose FP8 format is FNUZ. `use_fnuz=False`

selects OCP E4M3, which is used by OCP-encoded caches even on gfx942.

## Source code in `vllm/models/deepseek_v4/common/ops/cache_utils.py`


##

`quantize_and_insert_k_kernel(k_ptr, slot_mapping_ptr, k_cache_ptr, num_tokens, input_dim, fp8_dim, bf16_dim, scale_dim, quant_block, cache_block_size, token_data_size, block_stride, fp8_max, n_quant_blocks, use_fnuz=False)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.ops.cache_utils.quantize_and_insert_k_kernel)

Quantize K tensor and insert into paged K cache.

K Cache block layout (block_size=64 tokens): - [0, 64*576): Token data, each token has 448 fp8 + 128 bf16 - [64*576, 64*576 + 64*8): Scales, each token has 8 uint8 scales - [64*576 + 64*8, block_stride): Padding

One program per token.

`use_fnuz=True`

selects FNUZ (`tl.float8e4b8`

); default OCP (`tl.float8e4nv`

) matches every production caller.

## Source code in `vllm/models/deepseek_v4/common/ops/cache_utils.py`


|
|