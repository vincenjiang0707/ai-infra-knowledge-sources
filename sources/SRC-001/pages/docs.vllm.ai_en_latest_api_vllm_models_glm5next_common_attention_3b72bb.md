source: https://docs.vllm.ai/en/latest/api/vllm/models/glm5next/common/attention/
lastmod: 2026-09-24

#

`vllm.models.glm5next.common.attention`

[¶](https://docs.vllm.ai#vllm.models.glm5next.common.attention)

Classes:

-
–[Glm5NextIndexerCache](https://docs.vllm.ai#vllm.models.glm5next.common.attention.Glm5NextIndexerCache)Indexer K cache that stores kpool-compressed entries.

-
–[Glm5NextTailCache](https://docs.vllm.ai#vllm.models.glm5next.common.attention.Glm5NextTailCache)Paged circular buffer for the kpool indexer's in-progress (tail) pool.


##

`Glm5NextIndexerCache`

[¶](https://docs.vllm.ai#vllm.models.glm5next.common.attention.Glm5NextIndexerCache)

Bases: [DeepseekV32IndexerCache](https://docs.vllm.ai/model_executor/models/deepseek_v2/#vllm.model_executor.models.deepseek_v2.DeepseekV32IndexerCache)

Indexer K cache that stores kpool-compressed entries.

Setting `tokens_per_state = index_kpool`

on the KV cache spec makes vLLM's indexer metadata builder emit pool-granular `slot_mapping`

/ `seq_lens`

/ `cu_seq_lens`

/ `page_table`

for free, and shrinks the cache allocation store one state per `index_kpool`

tokens. The pool *content* (softmax-weighted sum vs keep-every-Nth) is computed by the kpool compress kernel inside the indexer op — the cache only provides the addressing, which is identical for both schemes.

The indexer shares one block with the co-located MLA (a single `MLAAttentionSpec`

/ block_table), so `block_size`

is the model-wide `cache_config.block_size`

. DeepGEMM's paged-MQA kernel (`csrc/apis/attention.hpp`

) requires `block_kv`

to be exactly 32 or 64, so the storage block is virtually split into pool pages of the largest such size that tiles it (`storage_kernel_block_size`

); this needs `block_size`

to be a multiple of `index_kpool * 32`

(512 for `index_kpool = 16`

). A smaller block (e.g. the default 64) silently collapses `storage_block_size`

(64 // 16 = 4) and only fails later at the opaque C++ assert; `get_kv_cache_spec`

guards this up front instead.

## Source code in `vllm/models/glm5next/common/attention.py`


##

`Glm5NextTailCache`

[¶](https://docs.vllm.ai#vllm.models.glm5next.common.attention.Glm5NextTailCache)

Bases: [DeepseekV32IndexerCache](https://docs.vllm.ai/model_executor/models/deepseek_v2/#vllm.model_executor.models.deepseek_v2.DeepseekV32IndexerCache)

Paged circular buffer for the kpool indexer's in-progress (tail) pool.

Holds the trailing incomplete pool's raw K + gate score: one block of `index_kpool`

slots per request, overwritten in place by `pos % kpool`

as decode/spec-decode advances. Prefill seeds it (instead of discarding the tail raw K+gate); the connector transfers it across PD; decode reads it to compress the boundary pool correctly. `KpoolTailSpec`

/ `KpoolTailManager`

provide the no-prune, 1-block/req allocation that lets the in-progress pool survive across steps and across transfer.

Stores raw bf16 K (`head_dim`

) as the "K" half of each block and the bf16 gate score (`head_dim`

) as the "V" half -- not the fp8-compressed entry, which lives in `Glm5NextIndexerCache`

.