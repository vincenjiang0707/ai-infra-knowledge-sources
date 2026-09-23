source: https://docs.vllm.ai/en/latest/api/vllm/models/minimax_m3/nvidia/indexer_msa/
lastmod: 2026-09-23

#

`vllm.models.minimax_m3.nvidia.indexer_msa`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.nvidia.indexer_msa)

MSA (SM100/Blackwell) indexer impl for MiniMax M3.

Both sides write block scores into one unified token-major buffer `[total_q, H, max_k_tiles]`

, then a single `fmha_sm100.sparse_topk_select`

selects the top-k blocks for the whole batch (decode `[:nd]`

+ prefill `[nd:]`

) into the shared `topk_indices_buffer`

. It bounds each row by its causal page count and force-includes the init/local blocks, so the unwritten tail of the buffer is pre-filled with `-inf`

.

Prefill scores with `fmha_sm100`

's score-only (`OnlyScore`

) path (much faster than Triton for the wide prefill score, benchmarked ~3-5x), writing its `max_score`

straight into the buffer's prefill region (stride-aware, no copy).

Decode scores with CuteDSL when the flattened query tile is supported and fall back to Triton otherwise, writing into the decode region. Only the top-k is shared with prefill.

`fmha_sm100`

imports are function-local so this module is import-safe on AMD / non-SM100.

Classes:

-
–[MiniMaxM3IndexerMSABackend](https://docs.vllm.ai#vllm.models.minimax_m3.nvidia.indexer_msa.MiniMaxM3IndexerMSABackend)Indexer side-cache backend selecting the MSA builder.

-
–[MiniMaxM3IndexerMSAImpl](https://docs.vllm.ai#vllm.models.minimax_m3.nvidia.indexer_msa.MiniMaxM3IndexerMSAImpl)Decode: CuteDSL/Triton score. Prefill: fmha_sm100 OnlyScore + top-k.

-
–[MiniMaxM3IndexerMSAMetadata](https://docs.vllm.ai#vllm.models.minimax_m3.nvidia.indexer_msa.MiniMaxM3IndexerMSAMetadata)Decode reuses the inherited base

`decode`

field (the Triton decode -
–[MiniMaxM3IndexerMSAMetadataBuilder](https://docs.vllm.ai#vllm.models.minimax_m3.nvidia.indexer_msa.MiniMaxM3IndexerMSAMetadataBuilder)Decode metadata is the cudagraph-safe Triton decode metadata; the prefill

-
–[MiniMaxM3IndexerMSAPrefillMetadata](https://docs.vllm.ai#vllm.models.minimax_m3.nvidia.indexer_msa.MiniMaxM3IndexerMSAPrefillMetadata)fmha score plan + Triton top-k inputs for the prefill side (eager).


##

`MiniMaxM3IndexerMSABackend`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.nvidia.indexer_msa.MiniMaxM3IndexerMSABackend)

Bases: [MiniMaxM3IndexerBackend](https://docs.vllm.ai/common/indexer/#vllm.models.minimax_m3.common.indexer.MiniMaxM3IndexerBackend)

Indexer side-cache backend selecting the MSA builder.

## Source code in `vllm/models/minimax_m3/nvidia/indexer_msa.py`


##

`MiniMaxM3IndexerMSAImpl`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.nvidia.indexer_msa.MiniMaxM3IndexerMSAImpl)

Bases: [MiniMaxM3IndexerImpl](https://docs.vllm.ai/common/indexer/#vllm.models.minimax_m3.common.indexer.MiniMaxM3IndexerImpl)

Decode: CuteDSL/Triton score. Prefill: fmha_sm100 OnlyScore + top-k.

## Source code in `vllm/models/minimax_m3/nvidia/indexer_msa.py`


|
|

##

`MiniMaxM3IndexerMSAMetadata`

`dataclass`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.nvidia.indexer_msa.MiniMaxM3IndexerMSAMetadata)

Bases: [MiniMaxM3IndexerMetadata](https://docs.vllm.ai/common/indexer/#vllm.models.minimax_m3.common.indexer.MiniMaxM3IndexerMetadata)

Decode reuses the inherited base `decode`

field (the Triton decode metadata); `prefill_msa`

carries the fmha score plan for the prefill side (the base `prefill`

field is unused on this path).

## Source code in `vllm/models/minimax_m3/nvidia/indexer_msa.py`


##

`MiniMaxM3IndexerMSAMetadataBuilder`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.nvidia.indexer_msa.MiniMaxM3IndexerMSAMetadataBuilder)

Bases: [MiniMaxM3IndexerMetadataBuilder](https://docs.vllm.ai/common/indexer/#vllm.models.minimax_m3.common.indexer.MiniMaxM3IndexerMetadataBuilder)

Decode metadata is the cudagraph-safe Triton decode metadata; the prefill fmha plan is built eagerly (prefill batches are not captured).

## Source code in `vllm/models/minimax_m3/nvidia/indexer_msa.py`


|
|

##

`MiniMaxM3IndexerMSAPrefillMetadata`

`dataclass`

[¶](https://docs.vllm.ai#vllm.models.minimax_m3.nvidia.indexer_msa.MiniMaxM3IndexerMSAPrefillMetadata)

fmha score plan + Triton top-k inputs for the prefill side (eager).