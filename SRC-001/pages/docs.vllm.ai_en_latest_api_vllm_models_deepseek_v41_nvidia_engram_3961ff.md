source: https://docs.vllm.ai/en/latest/api/vllm/models/deepseek_v41/nvidia/engram/
lastmod: 2026-09-23

#

`vllm.models.deepseek_v41.nvidia.engram`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.nvidia.engram)

NVIDIA Engram DP sharding, shared host storage, and asynchronous prefetch.

Classes:

-
–[DPSharedEngramStorage](https://docs.vllm.ai#vllm.models.deepseek_v41.nvidia.engram.DPSharedEngramStorage)Registered host weights shared by a node-local DP group with one writer.

-
–[Engram](https://docs.vllm.ai#vllm.models.deepseek_v41.nvidia.engram.Engram)NVIDIA Engram with asynchronous offload and node-local DP lookup.

-
–[ParallelEngramEmbedding](https://docs.vllm.ai#vllm.models.deepseek_v41.nvidia.engram.ParallelEngramEmbedding)Extend TP lookup with DP head sharding or shared, CPU-offloaded TP slices.


Functions:

-
–[can_share_engram_tables](https://docs.vllm.ai#vllm.models.deepseek_v41.nvidia.engram.can_share_engram_tables)Whether co-located DP replicas exist and /dev/shm can hold the full tables.

-
–[engram_gathered_num_tokens](https://docs.vllm.ai#vllm.models.deepseek_v41.nvidia.engram.engram_gathered_num_tokens)Per-replica token slot for the node-local Engram DP group.

-
–[engram_head_shard_rank](https://docs.vllm.ai#vllm.models.deepseek_v41.nvidia.engram.engram_head_shard_rank)This rank's slot among the hash-head shards of one engram table.

-
–[gather_engram_hashes](https://docs.vllm.ai#vllm.models.deepseek_v41.nvidia.engram.gather_engram_hashes)Collect the n-gram ids of every DP replica sharing one table.


##

`DPSharedEngramStorage`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.nvidia.engram.DPSharedEngramStorage)

Registered host weights shared by a node-local DP group with one writer.

## Source code in `vllm/models/deepseek_v41/nvidia/engram.py`


|
|

###

`_allocate(num_bytes)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.nvidia.engram.DPSharedEngramStorage._allocate)

Map and register one physical allocation across a node-local DP group.

## Source code in `vllm/models/deepseek_v41/nvidia/engram.py`


##

`Engram`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.nvidia.engram.Engram)

Bases: [Engram](https://docs.vllm.ai/common/engram/#vllm.models.deepseek_v41.common.engram.Engram)

NVIDIA Engram with asynchronous offload and node-local DP lookup.

Methods:

-
–[prepare_embeddings](https://docs.vllm.ai#vllm.models.deepseek_v41.nvidia.engram.Engram.prepare_embeddings)Prefetch local shared rows or the DP group's gathered hash IDs.


## Source code in `vllm/models/deepseek_v41/nvidia/engram.py`


###

`prepare_embeddings(hash_ids)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.nvidia.engram.Engram.prepare_embeddings)

Prefetch local shared rows or the DP group's gathered hash IDs.

## Source code in `vllm/models/deepseek_v41/nvidia/engram.py`


##

`ParallelEngramEmbedding`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.nvidia.engram.ParallelEngramEmbedding)

Bases: [ParallelEngramEmbedding](https://docs.vllm.ai/common/engram/#vllm.models.deepseek_v41.common.engram.ParallelEngramEmbedding)

Extend TP lookup with DP head sharding or shared, CPU-offloaded TP slices.

## Source code in `vllm/models/deepseek_v41/nvidia/engram.py`


|
|

##

`_gather_engram_rows(staged, num_tokens)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.nvidia.engram._gather_engram_rows)

Exchange DP tokens for heads, retaining only this replica's tokens.

## Source code in `vllm/models/deepseek_v41/nvidia/engram.py`


##

`can_share_engram_tables(layout, block_size=32)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.nvidia.engram.can_share_engram_tables)

Whether co-located DP replicas exist and /dev/shm can hold the full tables.

## Source code in `vllm/models/deepseek_v41/nvidia/engram.py`


##

`engram_gathered_num_tokens()`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.nvidia.engram.engram_gathered_num_tokens)

Per-replica token slot for the node-local Engram DP group.

## Source code in `vllm/models/deepseek_v41/nvidia/engram.py`


##

`engram_head_shard_rank()`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.nvidia.engram.engram_head_shard_rank)

This rank's slot among the hash-head shards of one engram table.

TP-major, so the shards a DP gather brings in are contiguous heads and the following TP gather completes the head order.

## Source code in `vllm/models/deepseek_v41/nvidia/engram.py`


##

`gather_engram_hashes(hash_ids, *, dp_shared_memory=False)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.nvidia.engram.gather_engram_hashes)

Collect the n-gram ids of every DP replica sharing one table.

Replicas are padded to a common token slot, so the gathered shape is static under CUDA graph capture (where DP already pads alike).