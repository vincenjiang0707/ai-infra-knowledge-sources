source: https://docs.vllm.ai/en/latest/api/vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/data/
lastmod: 2026-09-23

#

`vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data)

Data classes for MooncakeStoreConnector.

Classes:

-
–[BlobBlockHashes](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data.BlobBlockHashes)Lazy view over a flat buffer of fixed-size block hashes to avoid the overhead

-
–[ChunkedTokenDatabase](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data.ChunkedTokenDatabase)Enumerates logical token chunks and their hashes.

-
–[KeyMetadata](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data.KeyMetadata)Metadata for constructing pool keys.

-
–[LBHNCStoreLayout](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data.LBHNCStoreLayout)Native head-major layout shared by divisible TP sizes.

-
–[LBNHCStoreLayout](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data.LBNHCStoreLayout)Native token-major layout shared by divisible TP sizes.

-
–[LoadSpec](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data.LoadSpec)Specification for loading KV cache from external store.

-
–[MooncakeLookupResult](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data.MooncakeLookupResult)Lookup result used to build the subsequent load request.

-
–[MooncakeStoreConnectorMetadata](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data.MooncakeStoreConnectorMetadata)Metadata passed from scheduler to worker.

-
–[MooncakeStoreWorkerMetadata](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data.MooncakeStoreWorkerMetadata)Maps

`ReqMeta.store_job_id`

to the number of ranks done with that job. -
–[PoolKey](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data.PoolKey)Key for addressing KV cache blocks in the distributed store.

-
–[RankLocalStoreLayout](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data.RankLocalStoreLayout)Historical rank-local Store payload layout.

-
–[ReqMeta](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data.ReqMeta)Per-request metadata for store put/get operations.

-
–[RequestTracker](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data.RequestTracker)Tracks per-request state across scheduler ticks.

-
–[StoreLayout](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data.StoreLayout)Store payload layout for one KV-cache group on one local TP rank.

-
–[TPShardedStoreLayout](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data.TPShardedStoreLayout)Store layout shared by divisible TP sizes.

-
–[TailKeyBoundary](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data.TailKeyBoundary)Hash boundary used to key a group's tail block in the store.


Functions:

-
–[chunk_hashes_for_block_size](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data.chunk_hashes_for_block_size)Map

`hash_block_size`

-granular block hashes to one compact hash per

##

`BlobBlockHashes`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data.BlobBlockHashes)

Bases: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[BlockHash]

Lazy view over a flat buffer of fixed-size block hashes to avoid the overhead of materializing all hashes upfront.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/data.py`


##

`ChunkedTokenDatabase`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data.ChunkedTokenDatabase)

Enumerates logical token chunks and their hashes.

Methods:

-
–[prepare_value_for_block](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data.ChunkedTokenDatabase.prepare_value_for_block)Return addresses and sizes for one physical block slot.

-
–[process_tokens](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data.ChunkedTokenDatabase.process_tokens)Process tokens and yield (start_idx, end_idx, block_hash) tuples.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/data.py`


|
|

###

`prepare_value_for_block(block_id)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data.ChunkedTokenDatabase.prepare_value_for_block)

Return addresses and sizes for one physical block slot.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/data.py`


###

`process_tokens(token_len, block_hashes, mask_num=0, *, chunk_mask=None, put_step=1, put_step_rank=0)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data.ChunkedTokenDatabase.process_tokens)

Process tokens and yield (start_idx, end_idx, block_hash) tuples.

When there are fewer KV heads than TP ranks, chunks are distributed across TP ranks to avoid duplicate load/store. The assignment keys off the absolute `chunk_id`

so a given chunk always lands on the same rank regardless of where the processed suffix begins.

Parameters:

-

(`token_len`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data.ChunkedTokenDatabase.process_tokens(token_len))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Total number of tokens. Must be hash-block aligned and covered by

`block_hashes`

when hashes are present. -

(`block_hashes`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data.ChunkedTokenDatabase.process_tokens(block_hashes))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[BlockHash]Block hashes computed at

`hash_block_size`

granularity. When`block_size > hash_block_size`

each group's`block_size`

chunk is keyed by its last sub-hash via`chunk_hashes_for_block_size`

. -

(`mask_num`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data.ChunkedTokenDatabase.process_tokens(mask_num))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`0`

) –Number of tokens to skip from the beginning.

-

(`chunk_mask`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data.ChunkedTokenDatabase.process_tokens(chunk_mask))

, default:[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[bool](https://docs.python.org/3/builtins/functions.html#bool)] | None`None`

) –Optional mask relative to the first chunk after

`mask_num`

. False entries are skipped before hash access. -

(`put_step`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data.ChunkedTokenDatabase.process_tokens(put_step))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`1`

) –Stride for distributing chunks across ranks.

-

(`put_step_rank`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data.ChunkedTokenDatabase.process_tokens(put_step_rank))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`0`

) –`chunk_id % put_step`

value this rank stores.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/data.py`


##

`KeyMetadata`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data.KeyMetadata)

Metadata for constructing pool keys.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/data.py`


##

`LBHNCStoreLayout`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data.LBHNCStoreLayout)

Bases: [TPShardedStoreLayout](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data.TPShardedStoreLayout)

Native head-major layout shared by divisible TP sizes.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/data.py`


##

`LBNHCStoreLayout`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data.LBNHCStoreLayout)

Bases: [TPShardedStoreLayout](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data.TPShardedStoreLayout)

Native token-major layout shared by divisible TP sizes.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/data.py`


##

`LoadSpec`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data.LoadSpec)

Specification for loading KV cache from external store.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/data.py`


##

`MooncakeLookupResult`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data.MooncakeLookupResult)

Lookup result used to build the subsequent load request.

Attributes:

-
(`hit_length`


) –[int](https://docs.python.org/3/builtins/functions.html#int)Longest prefix that every KV-cache group can reuse after their individual cache hits converge.

-
(`tail_key_boundaries`


) –[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[TailKeyBoundary](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data.TailKeyBoundary), ...]Hash boundary used to store each cache group's tail block when

`hit_length`

does not identify its store key. There is one entry per group for every nonzero hit.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/data.py`


##

`MooncakeStoreConnectorMetadata`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data.MooncakeStoreConnectorMetadata)

Bases: [KVConnectorMetadata](https://docs.vllm.ai/base/#vllm.distributed.kv_transfer.kv_connector.v1.base.KVConnectorMetadata)

Metadata passed from scheduler to worker.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/data.py`


##

`MooncakeStoreWorkerMetadata`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data.MooncakeStoreWorkerMetadata)

Bases: [KVConnectorWorkerMetadata](https://docs.vllm.ai/base/#vllm.distributed.kv_transfer.kv_connector.v1.base.KVConnectorWorkerMetadata)

Maps `ReqMeta.store_job_id`

to the number of ranks done with that job.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/data.py`


##

`PoolKey`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data.PoolKey)

Key for addressing KV cache blocks in the distributed store.

Methods:

-
–[build_prefix](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data.PoolKey.build_prefix)Return the stable prefix for a Mooncake pool key.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/data.py`


###

`build_prefix(key_metadata, *, tp_rank=None, pcp_rank=None, dcp_rank=None, pp_rank=None)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data.PoolKey.build_prefix)

Return the stable prefix for a Mooncake pool key.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/data.py`


##

`RankLocalStoreLayout`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data.RankLocalStoreLayout)

Bases: [StoreLayout](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data.StoreLayout)

Historical rank-local Store payload layout.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/data.py`


|
|

##

`ReqMeta`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data.ReqMeta)

Per-request metadata for store put/get operations.

Methods:

-
–[from_request_tracker](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data.ReqMeta.from_request_tracker)Create ReqMeta from a RequestTracker.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/data.py`


|
|

###

`from_request_tracker(tracker, block_size, load_spec=None, skip_save=False, block_hashes=None)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data.ReqMeta.from_request_tracker)

Create ReqMeta from a RequestTracker.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/data.py`


##

`RequestTracker`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data.RequestTracker)

Tracks per-request state across scheduler ticks.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/data.py`


##

`StoreLayout`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data.StoreLayout)

Store payload layout for one KV-cache group on one local TP rank.

Methods:

-
–[lookup_key_prefixes](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data.StoreLayout.lookup_key_prefixes)Prefixes that must exist for a logical block to be reusable.

-
–[prepare_values](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data.StoreLayout.prepare_values)Build Store multi-buffer descriptors for logical chunks.

-
–[register_kv_caches](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data.StoreLayout.register_kv_caches)Build descriptors from the local KV cache tensors.


Attributes:

-
([local_shard_ids](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data.StoreLayout.local_shard_ids)

) –[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[StoreShardId, ...]Store objects contributed or consumed by this local rank.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/data.py`


###

`local_shard_ids`

`property`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data.StoreLayout.local_shard_ids)

Store objects contributed or consumed by this local rank.

###

`lookup_key_prefixes(rank_namespaces)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data.StoreLayout.lookup_key_prefixes)

Prefixes that must exist for a logical block to be reusable.

###

`prepare_values(chunks, block_ids, shard_ids)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data.StoreLayout.prepare_values)

Build Store multi-buffer descriptors for logical chunks.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/data.py`


###

`register_kv_caches(kv_caches, num_blocks)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data.StoreLayout.register_kv_caches)

Build descriptors from the local KV cache tensors.

##

`TPShardedStoreLayout`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data.TPShardedStoreLayout)

Bases: [StoreLayout](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data.StoreLayout)

Store layout shared by divisible TP sizes.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/data.py`


|
|

##

`TailKeyBoundary`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data.TailKeyBoundary)

Hash boundary used to key a group's tail block in the store.

Attributes:

-
(`group_id`


) –[int](https://docs.python.org/3/builtins/functions.html#int)KV-cache group containing the tail block.

-
(`num_tokens`


) –[int](https://docs.python.org/3/builtins/functions.html#int)Token boundary whose prefix hash identifies the matched stored block. The loader uses

`block_hashes[num_tokens // hash_block_size - 1]`

instead of the hash implied by`MooncakeLookupResult.hit_length`

. This changes only the load key, not the reusable prefix.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/data.py`


##

`_CompactChunkHashList`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data._CompactChunkHashList)

Bases: [BlockHashListWithBlockSize](https://docs.vllm.ai/v1/core/kv_cache_utils/#vllm.v1.core.kv_cache_utils.BlockHashListWithBlockSize)

View that keys each `block_size`

chunk by the last constituent `hash_block_size`

hash instead of concatenating all of them.

The engine chains block hashes (each hash folds in the previous one), so the final sub-block hash of a chunk already uniquely identifies the whole chunk and its prefix. Using it keeps a Mooncake key at a single hash digest regardless of the `block_size`

/ `hash_block_size`

ratio, instead of growing the key linearly with it (e.g. 64x for `block_size=256`

, `hash_block_size=4`

).

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/data.py`


##

`chunk_hashes_for_block_size(block_hashes, hash_block_size, block_size)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.data.chunk_hashes_for_block_size)

Map `hash_block_size`

-granular block hashes to one compact hash per `block_size`

chunk (the chunk's last sub-hash). Returns `block_hashes`

unchanged when the two sizes are equal.