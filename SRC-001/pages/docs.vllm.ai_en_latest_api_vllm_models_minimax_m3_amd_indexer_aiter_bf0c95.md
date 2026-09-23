source: https://docs.vllm.ai/en/latest/api/vllm/models/minimax_m3/amd/indexer_aiter/
lastmod: 2026-09-23

#

`vllm.models.minimax_m3.amd.indexer_aiter`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.amd.indexer_aiter)

AITER (ROCm) indexer impl for MiniMax M3.

Scores index blocks and selects the top-k with AITER's fp8 MFMA kernels on both sides of the batch: `pa_sparse_block_score_decode`

for the uniform-query-length decode rows and `pa_sparse_block_score_prefill`

for the ragged prefill rows, then `pa_sparse_block_topk`

for each. The two scoring passes share one tile body in AITER, so they agree block for block, and both encode the forced init/local blocks as the same sentinel scores the Triton indexer uses.

The top-k also emits the attend's page table. The winners are already in its workgroup's LDS, so resolving them through the block table there costs one wave and replaces the separate Triton pass in `ops.sparse_pa`

; the rows it writes are one per (token, kv head) with the page ids folded head-minor, which is the layout `pa_decode_gluon`

reads after it flattens the cache.

The score kernels are built on `v_mfma_f32_16x16x32_fp8_fp8`

, so this impl requires an fp8 (e4m3) index cache and an fp8 index query -- the fused QK-norm/RoPE kernel emits both directly when the index cache is e4m3. See `aiter_indexer_unsupported_reason`

for the full set of limits; `select_aiter_indexer_impl_cls`

refuses to pick this impl unless they all hold, and the model falls back to the platform-neutral `MiniMaxM3Indexer`

.

Classes:

-
–[MiniMaxM3AiterIndexer](https://docs.vllm.ai#vllm.models.minimax_m3.amd.indexer_aiter.MiniMaxM3AiterIndexer)`MiniMaxM3Indexer`

's surface over the AITER impl. -
–[MiniMaxM3IndexerAiterBackend](https://docs.vllm.ai#vllm.models.minimax_m3.amd.indexer_aiter.MiniMaxM3IndexerAiterBackend)Indexer side-cache backend selecting the AITER builder.

-
–[MiniMaxM3IndexerAiterImpl](https://docs.vllm.ai#vllm.models.minimax_m3.amd.indexer_aiter.MiniMaxM3IndexerAiterImpl)AITER fp8 score + top-k for both prefill and decode.

-
–[MiniMaxM3IndexerAiterMetadata](https://docs.vllm.ai#vllm.models.minimax_m3.amd.indexer_aiter.MiniMaxM3IndexerAiterMetadata)Adds the per-row shape the ragged top-k needs.

-
–[MiniMaxM3IndexerAiterMetadataBuilder](https://docs.vllm.ai#vllm.models.minimax_m3.amd.indexer_aiter.MiniMaxM3IndexerAiterMetadataBuilder)The Triton indexer's metadata plus the prefill rows' causal shape.


Functions:

-
–[aiter_indexer_max_decode_query_len](https://docs.vllm.ai#vllm.models.minimax_m3.amd.indexer_aiter.aiter_indexer_max_decode_query_len)Longest query a decode row can carry, which spec decode is what sets.

-
–[aiter_indexer_unsupported_reason](https://docs.vllm.ai#vllm.models.minimax_m3.amd.indexer_aiter.aiter_indexer_unsupported_reason)Return why this config cannot use the AITER indexer, or None if it can.

-
–[aiter_msa_kernels_unavailable_reason](https://docs.vllm.ai#vllm.models.minimax_m3.amd.indexer_aiter.aiter_msa_kernels_unavailable_reason)Return why the AITER MSA score/top-k ops cannot be imported, or None.

-
–[score_block_width](https://docs.vllm.ai#vllm.models.minimax_m3.amd.indexer_aiter.score_block_width)Block-axis width the top-k requires of the score buffer.

-
–[select_aiter_indexer_impl_cls](https://docs.vllm.ai#vllm.models.minimax_m3.amd.indexer_aiter.select_aiter_indexer_impl_cls)The AITER indexer impl if this config can use it, else None.


##

`MiniMaxM3AiterIndexer`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.amd.indexer_aiter.MiniMaxM3AiterIndexer)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

`MiniMaxM3Indexer`

's surface over the AITER impl.

The platform-neutral wrapper picks its impl through `common`

's selector and forwards a Triton-only set of fused-table arguments, neither of which can reach this impl without editing `common`

. This holds the same three members the attention layer uses -- `impl`

, `index_cache`

, `num_index_heads`

-- and forwards the one argument AITER needs instead.

## Source code in `vllm/models/minimax_m3/amd/indexer_aiter.py`


##

`MiniMaxM3IndexerAiterBackend`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.amd.indexer_aiter.MiniMaxM3IndexerAiterBackend)

Bases: [MiniMaxM3IndexerBackend](https://docs.vllm.ai/common/indexer/#vllm.models.minimax_m3.common.indexer.MiniMaxM3IndexerBackend)

Indexer side-cache backend selecting the AITER builder.

## Source code in `vllm/models/minimax_m3/amd/indexer_aiter.py`


##

`MiniMaxM3IndexerAiterImpl`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.amd.indexer_aiter.MiniMaxM3IndexerAiterImpl)

Bases: [MiniMaxM3IndexerImpl](https://docs.vllm.ai/common/indexer/#vllm.models.minimax_m3.common.indexer.MiniMaxM3IndexerImpl)

AITER fp8 score + top-k for both prefill and decode.

Attributes:

-
([pages_per_block](https://docs.vllm.ai#vllm.models.minimax_m3.amd.indexer_aiter.MiniMaxM3IndexerAiterImpl.pages_per_block)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Physical pages one selected block expands into for the attend.


## Source code in `vllm/models/minimax_m3/amd/indexer_aiter.py`


|
|

###

`pages_per_block`

`property`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.amd.indexer_aiter.MiniMaxM3IndexerAiterImpl.pages_per_block)

Physical pages one selected block expands into for the attend.

###

`_new_score(rows, max_seq_len)`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.amd.indexer_aiter.MiniMaxM3IndexerAiterImpl._new_score)

Score buffer for `rows`

query rows.

Left uninitialized on purpose: the score pass writes every block up to the longest row it covers, and the top-k reads only the blocks its own row can see, so nothing downstream observes the padded tail. Filling it would cost a write over the whole [H, rows, width] extent, which at long context is the largest tensor in the indexer.

## Source code in `vllm/models/minimax_m3/amd/indexer_aiter.py`


###

`_table_rows(lo, hi)`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.amd.indexer_aiter.MiniMaxM3IndexerAiterImpl._table_rows)

The page table and context rows covering score rows `[lo, hi)`

.

One table row per (token, kv head), head minor, which is the order `pa_decode_gluon`

reads once it flattens the cache. Slices of the shared buffers rather than copies, so the attend sees the writes; a model that reserved no buffers gets throwaway ones, and the attend rebuilds the table itself in that case.

## Source code in `vllm/models/minimax_m3/amd/indexer_aiter.py`


##

`MiniMaxM3IndexerAiterMetadata`

`dataclass`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.amd.indexer_aiter.MiniMaxM3IndexerAiterMetadata)

Bases: [MiniMaxM3IndexerMetadata](https://docs.vllm.ai/common/indexer/#vllm.models.minimax_m3.common.indexer.MiniMaxM3IndexerMetadata)

Adds the per-row shape the ragged top-k needs.

The uniform decode rows are recovered inside the kernel from `seq_lens`

and the shared query length, which also clamps cudagraph padding rows to nothing. Prefill rows have no such shape, so it is materialized here once per forward and shared by every layer -- which is also where the emitted page table's tail block comes from, since a block count alone does not say how many tokens the last block holds.

## Source code in `vllm/models/minimax_m3/amd/indexer_aiter.py`


##

`MiniMaxM3IndexerAiterMetadataBuilder`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.amd.indexer_aiter.MiniMaxM3IndexerAiterMetadataBuilder)

Bases: [MiniMaxM3IndexerMetadataBuilder](https://docs.vllm.ai/common/indexer/#vllm.models.minimax_m3.common.indexer.MiniMaxM3IndexerMetadataBuilder)

The Triton indexer's metadata plus the prefill rows' causal shape.

## Source code in `vllm/models/minimax_m3/amd/indexer_aiter.py`


|
|

##

`aiter_indexer_max_decode_query_len(vllm_config)`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.amd.indexer_aiter.aiter_indexer_max_decode_query_len)

Longest query a decode row can carry, which spec decode is what sets.

Mirrors `_init_reorder_batch_threshold(1, supports_spec_as_decode=True)`

, since that is what the builder splits the batch on and therefore what the decode kernel will actually be handed.

## Source code in `vllm/models/minimax_m3/amd/indexer_aiter.py`


##

`aiter_indexer_unsupported_reason(*, topk_blocks, sparse_block_size, num_index_heads, index_head_dim, indexer_kv_dtype, max_model_len, max_decode_query_len=1, score_type='max')`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.amd.indexer_aiter.aiter_indexer_unsupported_reason)

Return why this config cannot use the AITER indexer, or None if it can.

Checks platform (ROCm/gfx950), the AITER sparse PA attend, index-cache dtype, the compiled score/top-k contract, MFMA column limits, max context in blocks, and whether AITER exposes the MSA kernels. `select_aiter_indexer_impl_cls`

logs the string and falls back when it is not None.

## Source code in `vllm/models/minimax_m3/amd/indexer_aiter.py`


##

`aiter_msa_kernels_unavailable_reason()`

`cached`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.amd.indexer_aiter.aiter_msa_kernels_unavailable_reason)

Return why the AITER MSA score/top-k ops cannot be imported, or None.

They are a recent addition, so an AITER that predates them imports fine while these three names do not exist, and the failure would otherwise surface as an ImportError from the middle of a forward. `compile_ops`

binds them lazily, so this costs the module import only -- the kernel build itself still happens on the first call.

## Source code in `vllm/models/minimax_m3/amd/indexer_aiter.py`


##

`score_block_width(max_seq_len, block_size)`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.amd.indexer_aiter.score_block_width)

Block-axis width the top-k requires of the score buffer.

Lanes read whole wave-wide strips with no tail guard and each holds a power-of-two count of them, so the axis is padded past the block count.

## Source code in `vllm/models/minimax_m3/amd/indexer_aiter.py`


##

`select_aiter_indexer_impl_cls(*, topk_blocks, sparse_block_size, num_index_heads, index_head_dim, indexer_kv_dtype, score_type='max')`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.amd.indexer_aiter.select_aiter_indexer_impl_cls)

The AITER indexer impl if this config can use it, else None.

`None`

sends the caller to the platform-neutral `MiniMaxM3Indexer`

, which on ROCm means the Triton indexer -- and a bf16-only one, so an fp8 index cache that lands here has nowhere to go.