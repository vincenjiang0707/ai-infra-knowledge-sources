source: https://docs.vllm.ai/en/latest/api/vllm/models/minimax_m3/common/indexer/
lastmod: 2026-09-24

#

`vllm.models.minimax_m3.common.indexer`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.common.indexer)

MiniMax M3 lightning indexer: side cache, metadata, and impl.

The indexer scores KV blocks with the index heads and selects the top-k blocks (plus fixed init/local blocks) that the main block-sparse attention (`sparse_attention.py`

) then attends to. It owns its own side cache (`MiniMaxM3IndexerCache`

, one index-key vector per token), metadata, and metadata builder, mirroring how DeepSeek V4 keeps the indexer separate from the main attention.

`MiniMaxM3Indexer`

is the `nn.Module`

the attention layer holds (like `DeepseekV4Indexer`

); it picks a kernel impl in `__init__`

(via `select_indexer_impl_cls`

) and delegates `forward`

to it.

Classes:

-
–[MiniMaxM3Indexer](https://docs.vllm.ai#vllm.models.minimax_m3.common.indexer.MiniMaxM3Indexer)Indexer module held by the attention layer (like

`DeepseekV4Indexer`

). -
–[MiniMaxM3IndexerBackend](https://docs.vllm.ai#vllm.models.minimax_m3.common.indexer.MiniMaxM3IndexerBackend)Indexer side-cache backend (key-only).

-
–[MiniMaxM3IndexerCache](https://docs.vllm.ai#vllm.models.minimax_m3.common.indexer.MiniMaxM3IndexerCache)Side KV cache for the indexer's per-token index keys (key-only).

-
–[MiniMaxM3IndexerDecodeMetadata](https://docs.vllm.ai#vllm.models.minimax_m3.common.indexer.MiniMaxM3IndexerDecodeMetadata)Per-decode state (cudagraph-safe).

`decode_query_len`

is the uniform -
–[MiniMaxM3IndexerImpl](https://docs.vllm.ai#vllm.models.minimax_m3.common.indexer.MiniMaxM3IndexerImpl)Abstract base for the indexer kernel impls.

-
–[MiniMaxM3IndexerMetadata](https://docs.vllm.ai#vllm.models.minimax_m3.common.indexer.MiniMaxM3IndexerMetadata)Indexer metadata, split into prefill and decode sub-metadata.

-
–[MiniMaxM3IndexerMetadataBuilder](https://docs.vllm.ai#vllm.models.minimax_m3.common.indexer.MiniMaxM3IndexerMetadataBuilder)Abstract base: shared setup only. The Triton and MSA builders are

-
–[MiniMaxM3IndexerPrefillMetadata](https://docs.vllm.ai#vllm.models.minimax_m3.common.indexer.MiniMaxM3IndexerPrefillMetadata)Per-prefill index-scoring state.

-
–[MiniMaxM3IndexerTritonImpl](https://docs.vllm.ai#vllm.models.minimax_m3.common.indexer.MiniMaxM3IndexerTritonImpl)Triton indexer score + top-k for both prefill and decode.

-
–[MiniMaxM3IndexerTritonMetadataBuilder](https://docs.vllm.ai#vllm.models.minimax_m3.common.indexer.MiniMaxM3IndexerTritonMetadataBuilder)Triton indexer metadata: no SM100 fmha_sm100 plan.


Functions:

-
–[select_indexer_impl_cls](https://docs.vllm.ai#vllm.models.minimax_m3.common.indexer.select_indexer_impl_cls)Pick the indexer impl off the platform, top-k count, and cache dtype.


##

`MiniMaxM3Indexer`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.common.indexer.MiniMaxM3Indexer)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Indexer module held by the attention layer (like `DeepseekV4Indexer`

).

Picks the kernel impl in `__init__`

(`select_indexer_impl_cls`

) and delegates `forward`

; exposes the impl's side cache via `index_cache`

.

## Source code in `vllm/models/minimax_m3/common/indexer.py`


|
|

##

`MiniMaxM3IndexerBackend`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.common.indexer.MiniMaxM3IndexerBackend)

Bases: [AttentionBackend](https://docs.vllm.ai/v1/attention/backend/#vllm.v1.attention.backend.AttentionBackend)

Indexer side-cache backend (key-only).

## Source code in `vllm/models/minimax_m3/common/indexer.py`


##

`MiniMaxM3IndexerCache`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.common.indexer.MiniMaxM3IndexerCache)

Bases:

, [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)[AttentionLayerBase](https://docs.vllm.ai/model_executor/layers/attention_layer_base/#vllm.model_executor.layers.attention_layer_base.AttentionLayerBase)

Side KV cache for the indexer's per-token index keys (key-only).

Registers itself in the static forward context so the KV-cache manager allocates it (like `DeepseekV32IndexerCache`

).

## Source code in `vllm/models/minimax_m3/common/indexer.py`


##

`MiniMaxM3IndexerDecodeMetadata`

`dataclass`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.common.indexer.MiniMaxM3IndexerDecodeMetadata)

Per-decode state (cudagraph-safe). `decode_query_len`

is the uniform per-request query length (1, or 1 + num_speculative_tokens).

## Source code in `vllm/models/minimax_m3/common/indexer.py`


##

`MiniMaxM3IndexerImpl`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.common.indexer.MiniMaxM3IndexerImpl)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Abstract base for the indexer kernel impls.

Each impl owns its side cache and reports its backend via `indexer_backend_cls`

(so each gets its own builder). The Triton and MSA subclasses each own a full `forward`

returning `(decode_topk, prefill_topk)`

-- no shared forward code.

Methods:

-
–[forward](https://docs.vllm.ai#vllm.models.minimax_m3.common.indexer.MiniMaxM3IndexerImpl.forward)Return

`(decode_topk, prefill_topk)`

; implemented per kernel impl.

## Source code in `vllm/models/minimax_m3/common/indexer.py`


###

`forward(index_query)`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.common.indexer.MiniMaxM3IndexerImpl.forward)

Return `(decode_topk, prefill_topk)`

; implemented per kernel impl.

##

`MiniMaxM3IndexerMetadata`

`dataclass`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.common.indexer.MiniMaxM3IndexerMetadata)

Bases: `AttentionMetadata`


Indexer metadata, split into prefill and decode sub-metadata.

## Source code in `vllm/models/minimax_m3/common/indexer.py`


##

`MiniMaxM3IndexerMetadataBuilder`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.common.indexer.MiniMaxM3IndexerMetadataBuilder)

Bases: [AttentionMetadataBuilder](https://docs.vllm.ai/v1/attention/backend/#vllm.v1.attention.backend.AttentionMetadataBuilder)[[MiniMaxM3IndexerMetadata](https://docs.vllm.ai#vllm.models.minimax_m3.common.indexer.MiniMaxM3IndexerMetadata)]

Abstract base: shared setup only. The Triton and MSA builders are parallel subclasses that each own their full `build`

(no shared code).

## Source code in `vllm/models/minimax_m3/common/indexer.py`


##

`MiniMaxM3IndexerPrefillMetadata`

`dataclass`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.common.indexer.MiniMaxM3IndexerPrefillMetadata)

Per-prefill index-scoring state.

## Source code in `vllm/models/minimax_m3/common/indexer.py`


##

`MiniMaxM3IndexerTritonImpl`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.common.indexer.MiniMaxM3IndexerTritonImpl)

Bases: [MiniMaxM3IndexerImpl](https://docs.vllm.ai#vllm.models.minimax_m3.common.indexer.MiniMaxM3IndexerImpl)

Triton indexer score + top-k for both prefill and decode.

## Source code in `vllm/models/minimax_m3/common/indexer.py`


|
|

##

`MiniMaxM3IndexerTritonMetadataBuilder`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.common.indexer.MiniMaxM3IndexerTritonMetadataBuilder)

Bases: [MiniMaxM3IndexerMetadataBuilder](https://docs.vllm.ai#vllm.models.minimax_m3.common.indexer.MiniMaxM3IndexerMetadataBuilder)

Triton indexer metadata: no SM100 fmha_sm100 plan.

## Source code in `vllm/models/minimax_m3/common/indexer.py`


##

`select_indexer_impl_cls(*, topk_blocks, indexer_kv_dtype='bf16')`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.common.indexer.select_indexer_impl_cls)

Pick the indexer impl off the platform, top-k count, and cache dtype.

On Blackwell (SM100) with `topk_blocks == 16`

(the only width fmha_sm100's `sparse_topk_select`

kernel supports), the fmha_sm100 score + top-k path is used for both bf16 and fp8 index caches. Everything else falls back to the Triton indexer (bf16 only).