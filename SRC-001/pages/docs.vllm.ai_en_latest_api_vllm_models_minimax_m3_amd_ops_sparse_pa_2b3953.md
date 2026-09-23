source: https://docs.vllm.ai/en/latest/api/vllm/models/minimax_m3/amd/ops/sparse_pa/
lastmod: 2026-09-23

#

`vllm.models.minimax_m3.amd.ops.sparse_pa`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.amd.ops.sparse_pa)

AITER page-16 sparse paged-attention helpers for MiniMax-M3 on ROCm.

Functions:

-
–[minimax_m3_build_sparse_block_table_decode](https://docs.vllm.ai#vllm.models.minimax_m3.amd.ops.sparse_pa.minimax_m3_build_sparse_block_table_decode)Build one page-16 sparse block table row per decode query token.

-
–[minimax_m3_build_sparse_block_table_prefill](https://docs.vllm.ai#vllm.models.minimax_m3.amd.ops.sparse_pa.minimax_m3_build_sparse_block_table_prefill)Build one page-16 sparse block table row per prefill query token.

-
–[minimax_m3_insert_index_cache](https://docs.vllm.ai#vllm.models.minimax_m3.amd.ops.sparse_pa.minimax_m3_insert_index_cache)Scatter index keys into MiniMax-M3's key-only side cache.

-
–[minimax_m3_rebase_block_table_to_page16](https://docs.vllm.ai#vllm.models.minimax_m3.amd.ops.sparse_pa.minimax_m3_rebase_block_table_to_page16)Rebase a logical page table onto AITER's page-16 page numbering.

-
–[minimax_m3_sparse_block_page_stride](https://docs.vllm.ai#vllm.models.minimax_m3.amd.ops.sparse_pa.minimax_m3_sparse_block_page_stride)How many page ids one sparse block spans.


##

`_sides_are_packed(k_cache, v_cache)`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.amd.ops.sparse_pa._sides_are_packed)

Whether a block holds both its K and V pages instead of one side.

##

`_write_sparse_block_table_row_from_values(blk, bt_row, sbt_row, ctx_ptr, abs_pos, max_topk, SPARSE_BLOCK_SIZE_C, PAGES_PER_BLOCK, BLOCK_PAGE_STRIDE, BLOCK_SIZE_T)`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.amd.ops.sparse_pa._write_sparse_block_table_row_from_values)

Compact one query's selected logical blocks into physical page-16 ids.

`BLOCK_PAGE_STRIDE`

is how many page ids a block spans, which is `PAGES_PER_BLOCK`

when each K/V side is its own dense plane and twice that when both sides share a block. Padded rows carry a negative `abs_pos`

, which clamps the causal range to empty.

## Source code in `vllm/models/minimax_m3/amd/ops/sparse_pa.py`


##

`minimax_m3_build_sparse_block_table_decode(topk_idx, block_table, seq_lens, decode_query_len=1, block_page_stride=PAGES_PER_SPARSE_BLOCK)`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.amd.ops.sparse_pa.minimax_m3_build_sparse_block_table_decode)

Build one page-16 sparse block table row per decode query token.

## Source code in `vllm/models/minimax_m3/amd/ops/sparse_pa.py`


##

`minimax_m3_build_sparse_block_table_prefill(topk_idx, block_table, query_req_id, query_abs_pos, block_page_stride=PAGES_PER_SPARSE_BLOCK)`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.amd.ops.sparse_pa.minimax_m3_build_sparse_block_table_prefill)

Build one page-16 sparse block table row per prefill query token.

## Source code in `vllm/models/minimax_m3/amd/ops/sparse_pa.py`


##

`minimax_m3_insert_index_cache(index_k, index_cache, index_slot_mapping)`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.amd.ops.sparse_pa.minimax_m3_insert_index_cache)

Scatter index keys into MiniMax-M3's key-only side cache.

## Source code in `vllm/models/minimax_m3/amd/ops/sparse_pa.py`


##

`minimax_m3_rebase_block_table_to_page16(block_table, out=None)`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.amd.ops.sparse_pa.minimax_m3_rebase_block_table_to_page16)

Rebase a logical page table onto AITER's page-16 page numbering.

The page ids AITER's top-k emits for the attend are `block_table[blk] * pages_per_block + j`

, and `pages_per_block`

is fixed at AITER build time to one side's pages. An interleaved block spans both sides, so the only way to reach its pages through that kernel is to hand it a table already scaled to the wider stride. The caller does this once per step, since every sparse layer resolves its selection through the same table.

## Source code in `vllm/models/minimax_m3/amd/ops/sparse_pa.py`


##

`minimax_m3_sparse_block_page_stride(k_cache, v_cache)`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.amd.ops.sparse_pa.minimax_m3_sparse_block_page_stride)

How many page ids one sparse block spans.

Each side owns `PAGES_PER_SPARSE_BLOCK`

pages. When the sides are dense planes a block is exactly that wide; when they interleave, a block covers both sides' pages and V is reached from the same page id at a fixed offset.