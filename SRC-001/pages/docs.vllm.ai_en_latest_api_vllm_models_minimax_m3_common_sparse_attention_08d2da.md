source: https://docs.vllm.ai/en/latest/api/vllm/models/minimax_m3/common/sparse_attention/
lastmod: 2026-09-23

#

`vllm.models.minimax_m3.common.sparse_attention`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.common.sparse_attention)

Main block-sparse GQA attention for MiniMax M3 sparse layers.

The lightning indexer (`indexer.py`

) selects the top-k KV blocks (written into the shared `layer.topk_indices_buffer`

); this module holds the main attention that attends only to those blocks: the paged K/V cache backend, its metadata + builder, and the impl that reads the indexer's top-k from that buffer. The Triton attend kernel lives here; the SM100 (MSA) `build_k2q_csr`

+ `sparse_atten_func`

attend lives in `nvidia/sparse_attention_msa.py`

.

`MiniMaxM3SparseBackend`

and `MiniMaxM3SparseMetadata`

are referenced by the attention-backend registry (by dotted path) and by spec-decode, so they must keep these names and stay in this module.

Classes:

-
–[MiniMaxM3SparseBackend](https://docs.vllm.ai#vllm.models.minimax_m3.common.sparse_attention.MiniMaxM3SparseBackend)Block-sparse GQA backend for MiniMax M3 sparse attention layers.

-
–[MiniMaxM3SparseDecodeMetadata](https://docs.vllm.ai#vllm.models.minimax_m3.common.sparse_attention.MiniMaxM3SparseDecodeMetadata)Per-decode state (cudagraph-safe).

`decode_query_len`

is the uniform -
–[MiniMaxM3SparseImpl](https://docs.vllm.ai#vllm.models.minimax_m3.common.sparse_attention.MiniMaxM3SparseImpl)Abstract base for block-sparse GQA over the indexer-selected blocks.

-
–[MiniMaxM3SparseMetadata](https://docs.vllm.ai#vllm.models.minimax_m3.common.sparse_attention.MiniMaxM3SparseMetadata)Sparse-attention metadata, split into prefill and decode sub-metadata.

-
–[MiniMaxM3SparsePrefillMetadata](https://docs.vllm.ai#vllm.models.minimax_m3.common.sparse_attention.MiniMaxM3SparsePrefillMetadata)Per-prefill state;

`cu_seqlens_k`

/`total_kv_blocks`

feed the MSA CSR. -
–[MiniMaxM3SparseTritonImpl](https://docs.vllm.ai#vllm.models.minimax_m3.common.sparse_attention.MiniMaxM3SparseTritonImpl)Triton block-sparse attend (

`minimax_m3_sparse_attn`

) + Triton decode.

Functions:

-
–[minimax_m3_query_token_positions](https://docs.vllm.ai#vllm.models.minimax_m3.common.sparse_attention.minimax_m3_query_token_positions)Map each prefill query token to its request id and absolute KV position.

-
–[minimax_m3_rebase_slots_to_page16](https://docs.vllm.ai#vllm.models.minimax_m3.common.sparse_attention.minimax_m3_rebase_slots_to_page16)Rebase a token slot mapping onto AITER's page-16 page numbering.

-
–[minimax_m3_use_aiter_sparse_pa](https://docs.vllm.ai#vllm.models.minimax_m3.common.sparse_attention.minimax_m3_use_aiter_sparse_pa)Whether to use the ROCm AITER page-16 sparse PA prototype.

-
–[select_main_backend_and_impl_cls](https://docs.vllm.ai#vllm.models.minimax_m3.common.sparse_attention.select_main_backend_and_impl_cls)Pick the main attention backend and implementation.

-
–[select_main_impl_cls](https://docs.vllm.ai#vllm.models.minimax_m3.common.sparse_attention.select_main_impl_cls)Backward-compatible implementation-only selector.


##

`MiniMaxM3SparseBackend`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.common.sparse_attention.MiniMaxM3SparseBackend)

Bases: [AttentionBackend](https://docs.vllm.ai/v1/attention/backend/#vllm.v1.attention.backend.AttentionBackend)

Block-sparse GQA backend for MiniMax M3 sparse attention layers.

## Source code in `vllm/models/minimax_m3/common/sparse_attention.py`


##

`MiniMaxM3SparseDecodeMetadata`

`dataclass`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.common.sparse_attention.MiniMaxM3SparseDecodeMetadata)

Per-decode state (cudagraph-safe). `decode_query_len`

is the uniform per-request query length (1, or 1 + num_speculative_tokens).

## Source code in `vllm/models/minimax_m3/common/sparse_attention.py`


##

`MiniMaxM3SparseImpl`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.common.sparse_attention.MiniMaxM3SparseImpl)

Bases: [AttentionImplBase](https://docs.vllm.ai/v1/attention/backend/#vllm.v1.attention.backend.AttentionImplBase)[[MiniMaxM3SparseMetadata](https://docs.vllm.ai#vllm.models.minimax_m3.common.sparse_attention.MiniMaxM3SparseMetadata)]

Abstract base for block-sparse GQA over the indexer-selected blocks.

Inherits `AttentionImplBase`

for a custom forward signature (the layer pre-inserts K/V and runs the indexer, which writes the selected blocks into the shared `layer.topk_indices_buffer`

; the attend reads them back from there). The Triton and MSA subclasses each own a full `forward`

-- no shared forward code.

Methods:

-
–[forward](https://docs.vllm.ai#vllm.models.minimax_m3.common.sparse_attention.MiniMaxM3SparseImpl.forward)Attend the queries to the indexer-selected blocks. Per kernel.


## Source code in `vllm/models/minimax_m3/common/sparse_attention.py`


###

`forward(layer, query, kv_cache, output, *, query_fp8=None)`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.common.sparse_attention.MiniMaxM3SparseImpl.forward)

Attend the queries to the indexer-selected blocks. Per kernel.

The indexer has already written the top-k block ids into `layer.topk_indices_buffer`

(decode at `[:, :nd]`

, prefill at `[:, nd:num_tokens]`

); the attend reads them from there.

## Source code in `vllm/models/minimax_m3/common/sparse_attention.py`


##

`MiniMaxM3SparseMetadata`

`dataclass`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.common.sparse_attention.MiniMaxM3SparseMetadata)

Bases: `AttentionMetadata`


Sparse-attention metadata, split into prefill and decode sub-metadata.

## Source code in `vllm/models/minimax_m3/common/sparse_attention.py`


##

`MiniMaxM3SparsePrefillMetadata`

`dataclass`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.common.sparse_attention.MiniMaxM3SparsePrefillMetadata)

Per-prefill state; `cu_seqlens_k`

/`total_kv_blocks`

feed the MSA CSR.

## Source code in `vllm/models/minimax_m3/common/sparse_attention.py`


##

`MiniMaxM3SparseTritonImpl`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.common.sparse_attention.MiniMaxM3SparseTritonImpl)

Bases: [MiniMaxM3SparseImpl](https://docs.vllm.ai#vllm.models.minimax_m3.common.sparse_attention.MiniMaxM3SparseImpl)

Triton block-sparse attend (`minimax_m3_sparse_attn`

) + Triton decode.

## Source code in `vllm/models/minimax_m3/common/sparse_attention.py`


|
|

##

`minimax_m3_query_token_positions(cu_seqlens_q, prefix_lens, total_q)`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.common.sparse_attention.minimax_m3_query_token_positions)

Map each prefill query token to its request id and absolute KV position.

Both tensors are the same for every sparse layer in a step, so the AITER sparse PA block-table builder reads them from the metadata instead of rebuilding them once per layer.

## Source code in `vllm/models/minimax_m3/common/sparse_attention.py`


##

`minimax_m3_rebase_slots_to_page16(slot_mapping, block_size, out=None)`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.common.sparse_attention.minimax_m3_rebase_slots_to_page16)

Rebase a token slot mapping onto AITER's page-16 page numbering.

AITER's KV writer derives the destination page from `slot // 16`

and assumes pages are numbered consecutively. When the resolved layout stores both K/V sides inside a block, a block spans twice as many pages, so only the block component of the slot doubles -- the offset within the page must not move. Clamping before the division leaves padding slots at their negative sentinel, which is what tells the writer to skip them.

## Source code in `vllm/models/minimax_m3/common/sparse_attention.py`


##

`minimax_m3_use_aiter_sparse_pa(num_kv_heads, *, emits_sparse_block_table=False)`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.common.sparse_attention.minimax_m3_use_aiter_sparse_pa)

Whether to use the ROCm AITER page-16 sparse PA prototype.

More than one KV head per rank is only served when the layer's indexer emits the attend's page table itself, since the Triton builders this path otherwise falls back to address one head's cache. Whether an indexer does that is a ROCm-side fact, so its caller passes it in.

## Source code in `vllm/models/minimax_m3/common/sparse_attention.py`


##

`select_main_backend_and_impl_cls(*, topk_blocks, kv_cache_dtype, num_kv_heads, emits_sparse_block_table=False)`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.common.sparse_attention.select_main_backend_and_impl_cls)

Pick the main attention backend and implementation.

Blackwell (SM100) uses the MSA attend for supported top-k block counts when the KV cache is BF16 or FP8 E4M3; MI355 uses AITER sparse PA with shuffle KV cache layout; Other platforms and FP8 E5M2 fall back to Triton. The MSA modules are imported lazily to avoid import errors on unsupported platforms.

## Source code in `vllm/models/minimax_m3/common/sparse_attention.py`


##

`select_main_impl_cls(*, topk_blocks, kv_cache_dtype, num_kv_heads, emits_sparse_block_table=False)`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.common.sparse_attention.select_main_impl_cls)

Backward-compatible implementation-only selector.