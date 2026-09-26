source: https://docs.vllm.ai/en/latest/api/vllm/models/deepseek_v4/common/ops/fused_compress_quant_cache/
lastmod: 2026-09-24

#

`vllm.models.deepseek_v4.common.ops.fused_compress_quant_cache`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.ops.fused_compress_quant_cache)

Fused compressor + FP8/MXFP4 UE8M0 quantization + KV cache insert kernels.

## Three specialized kernels

- _fused_kv_compress_norm_rope_insert_sparse_attn: head=512, nope=448 FP8 + rope=64 bf16
- _fused_kv_compress_norm_rope_insert_indexer_attn: head=128, all FP8, 1 block/token
- _fused_kv_compress_norm_rope_insert_indexer_mxfp4_attn: head=128, MXFP4 (block=32), 4 ue8m0 bytes

RoPE is register-based via tl.reshape -> tl.split -> tl.interleave (or the even/odd halves are consumed directly for MXFP4, no interleave needed). FP8 UE8M0 quant uses tl.reshape to tile [N_QUANT_BLOCKS, QUANT_BLOCK] for per-block absmax entirely in registers. MXFP4 does the same tiling on the even/odd halves, producing (N_QUANT_BLOCKS, MXFP4_BLOCK/2) packed nibbles and N_QUANT_BLOCKS ue8m0 bytes.

Functions:

-
–[compress_norm_rope_store_triton](https://docs.vllm.ai#vllm.models.deepseek_v4.common.ops.fused_compress_quant_cache.compress_norm_rope_store_triton)Shared triton launcher for the fused compress+norm+RoPE+insert path.

-
–[compress_norm_rope_store_two_stage_triton](https://docs.vllm.ai#vllm.models.deepseek_v4.common.ops.fused_compress_quant_cache.compress_norm_rope_store_two_stage_triton)Two-stage split compressor dispatch for head=512 cr>=128 (no-overlap).


##

`_compress_gather_split_sparse_attn(state_cache_ptr, state_cache_stride0, state_cache_stride1, positions_ptr, slot_mapping_ptr, token_to_req_indices_ptr, block_table_ptr, block_table_stride, block_size, scratch_ptr, scratch_stride, HEAD_SIZE, STATE_WIDTH, COMPRESS_RATIO, NUM_SPLITS, HEAD_TILE)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.ops.fused_compress_quant_cache._compress_gather_split_sparse_attn)

Stage 1: per-(token, head-split) compress gather, write to fp32 scratch.

No-overlap gather (cr>=128) on rows [0, COMPRESS_RATIO)

## Source code in `vllm/models/deepseek_v4/common/ops/fused_compress_quant_cache.py`


##

`_finalize_norm_rope_quant_store_sparse_attn(scratch_ptr, scratch_stride, positions_ptr, slot_mapping_ptr, rms_norm_weight_ptr, rms_norm_eps, cos_sin_cache_ptr, cos_sin_stride, k_cache_ptr, kv_slot_mapping_ptr, kv_cache_block_size, HEAD_SIZE, TRITON_BLOCK_SIZE, COMPRESS_RATIO, ROPE_HEAD_DIM, FP8_MAX, QUANT_BLOCK, TOKEN_STRIDE, SCALE_DIM, KV_BLOCK_STRIDE, SANITIZE_CACHE_NANS)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.ops.fused_compress_quant_cache._finalize_norm_rope_quant_store_sparse_attn)

Stage 2: read compressed_kv[512] from scratch buffer, then RMSNorm + FP8 quant (nope) + RoPE + bf16 store

## Source code in `vllm/models/deepseek_v4/common/ops/fused_compress_quant_cache.py`


|
|

##

`_fused_kv_compress_norm_rope_insert_indexer_attn(state_cache_ptr, state_cache_stride0, state_cache_stride1, token_to_req_indices_ptr, positions_ptr, slot_mapping_ptr, block_table_ptr, block_table_stride, block_size, rms_norm_weight_ptr, rms_norm_eps, cos_sin_cache_ptr, cos_sin_stride, k_cache_ptr, kv_slot_mapping_ptr, kv_cache_block_size, HEAD_SIZE, TRITON_BLOCK_SIZE, STATE_WIDTH, COMPRESS_RATIO, OVERLAP, ROPE_HEAD_DIM, FP8_MAX, QUANT_BLOCK, TOKEN_STRIDE, SCALE_DIM, KV_BLOCK_STRIDE)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.ops.fused_compress_quant_cache._fused_kv_compress_norm_rope_insert_indexer_attn)

Fused compress → RMSNorm → RoPE → FP8 quant → store.

One program per token; early-exits for non-boundary positions.

## Cache block layout

[0, bs*128): FP8 data (128 bytes/token) [bs*128, +bs*4): float32 scales (4 bytes/token)

For head_dim=128 we have exactly one quant block, so we skip the [N_QUANT_BLOCKS, QUANT_BLOCK] reshape entirely and use a flat `tl.max`

reduction.

## Source code in `vllm/models/deepseek_v4/common/ops/fused_compress_quant_cache.py`


|
|

##

`_fused_kv_compress_norm_rope_insert_indexer_mxfp4_attn(state_cache_ptr, state_cache_stride0, state_cache_stride1, token_to_req_indices_ptr, positions_ptr, slot_mapping_ptr, block_table_ptr, block_table_stride, block_size, rms_norm_weight_ptr, rms_norm_eps, cos_sin_cache_ptr, cos_sin_stride, k_cache_ptr, kv_slot_mapping_ptr, kv_cache_block_size, HEAD_SIZE, TRITON_BLOCK_SIZE, STATE_WIDTH, COMPRESS_RATIO, OVERLAP, ROPE_HEAD_DIM, FP8_MAX, QUANT_BLOCK, TOKEN_STRIDE, SCALE_DIM, KV_BLOCK_STRIDE)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.ops.fused_compress_quant_cache._fused_kv_compress_norm_rope_insert_indexer_mxfp4_attn)

Fused compress → RMSNorm → RoPE → MXFP4 quant → store.

One program per token; early-exits for non-boundary positions.

Cache block layout (`block_size`

tokens per cache block): [0, bs*TOKEN_STRIDE): packed MXFP4 nibbles (2 values/byte) [bs*TOKEN_STRIDE, +bs*SCALE_DIM): ue8m0 scale bytes (one per 32-elem block)

## MXFP4 format

- E2M1 4-bit values packed two per byte (low nibble first, then high).
- Per-32-element block scale = 2^ceil(log2(amax / 6.0)), stored ue8m0 (byte = exponent + 127).
- Max representable magnitude = 6.0.

## Source code in `vllm/models/deepseek_v4/common/ops/fused_compress_quant_cache.py`


|
|

##

`_fused_kv_compress_norm_rope_insert_sparse_attn(state_cache_ptr, state_cache_stride0, state_cache_stride1, token_to_req_indices_ptr, positions_ptr, slot_mapping_ptr, block_table_ptr, block_table_stride, block_size, rms_norm_weight_ptr, rms_norm_eps, cos_sin_cache_ptr, cos_sin_stride, k_cache_ptr, kv_slot_mapping_ptr, kv_cache_block_size, HEAD_SIZE, TRITON_BLOCK_SIZE, STATE_WIDTH, COMPRESS_RATIO, OVERLAP, ROPE_HEAD_DIM, FP8_MAX, QUANT_BLOCK, TOKEN_STRIDE, SCALE_DIM, KV_BLOCK_STRIDE, SANITIZE_CACHE_NANS)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.ops.fused_compress_quant_cache._fused_kv_compress_norm_rope_insert_sparse_attn)

Fused compress → RMSNorm → FP8 quant (nope) → RoPE → bf16 store (rope).

One program per token; early-exits for non-boundary positions.

Cache block layout (`block_size`

tokens): [0, bs*576): token data (448 fp8 + 128 bf16 each) [bs*576, +bs*8): uint8 UE8M0 scales (7 real + 1 pad each)

## Source code in `vllm/models/deepseek_v4/common/ops/fused_compress_quant_cache.py`


|
|

##

`_pick_compress_num_splits(num_actual, compress_ratio, head_dim)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.ops.fused_compress_quant_cache._pick_compress_num_splits)

Occupancy-targeted column splits for the cr>=128 head=512 compressor.

Sizes the per-token fan-out so (estimated computing tokens) * num_splits ~

### CU, capped by head tiling at a 32-wide min tile, as a power-of-2 divisor of[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.ops.fused_compress_quant_cache._pick_compress_num_splits--cu-capped-by-head-tiling-at-a-32-wide-min-tile-as-a-power-of-2-divisor-of)

head_dim.

## Source code in `vllm/models/deepseek_v4/common/ops/fused_compress_quant_cache.py`


##

`compress_norm_rope_store_triton(state_cache, num_actual, token_to_req_indices, positions, slot_mapping, block_table, block_size, state_width, cos_sin_cache, kv_cache, k_cache_metadata, pdl_kwargs, head_dim, rope_head_dim, compress_ratio, overlap, use_fp4_cache, rms_norm_weight, rms_norm_eps, quant_block, token_stride, scale_dim)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.ops.fused_compress_quant_cache.compress_norm_rope_store_triton)

Shared triton launcher for the fused compress+norm+RoPE+insert path.

Picks one of the three kernels in this module based on `head_dim`

and `use_fp4_cache`

. Identical launch signature for all three.

## Source code in `vllm/models/deepseek_v4/common/ops/fused_compress_quant_cache.py`


|
|

##

`compress_norm_rope_store_two_stage_triton(state_cache, num_actual, token_to_req_indices, positions, slot_mapping, block_table, block_size, state_width, cos_sin_cache, kv_cache, k_cache_metadata, pdl_kwargs, head_dim, rope_head_dim, compress_ratio, overlap, use_fp4_cache, rms_norm_weight, rms_norm_eps, quant_block, token_stride, scale_dim, num_decode_tokens, compress_scratch)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.ops.fused_compress_quant_cache.compress_norm_rope_store_two_stage_triton)

Two-stage split compressor dispatch for head=512 cr>=128 (no-overlap).

Run the occupancy-fanned two-stage split for prefill [num_decodee_tokens:] to fill the CUs, and use the original single-pass launcher for decode [0, num_decode_tokens)

## Source code in `vllm/models/deepseek_v4/common/ops/fused_compress_quant_cache.py`


|
|