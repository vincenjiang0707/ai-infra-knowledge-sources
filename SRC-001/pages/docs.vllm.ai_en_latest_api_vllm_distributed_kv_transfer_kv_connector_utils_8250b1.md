source: https://docs.vllm.ai/en/latest/api/vllm/distributed/kv_transfer/kv_connector/utils/
lastmod: 2026-09-23

#

`vllm.distributed.kv_transfer.kv_connector.utils`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.utils)

KV cache helper for store.

Classes:

-
–[EngineTransferInfo](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.utils.EngineTransferInfo)Common per-remote-engine transfer state, computed at handshake.

-
–[KVOutputAggregator](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.utils.KVOutputAggregator)Utility class to aggregate the output of all workers into a single

-
–[TransferTopology](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.utils.TransferTopology)Single source of truth for local TP identity and per-engine remote info.


Functions:

-
–[copy_kv_blocks](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.utils.copy_kv_blocks)Copy kv blocks between different buffers.

-
–[get_current_attn_backend](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.utils.get_current_attn_backend)Get the first attention backend for the given layers.

-
–[get_current_attn_backends](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.utils.get_current_attn_backends)Get all distinct attention backends for the given layers.

-
–[kv_postprocess_blksize_and_layout_on_receive](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.utils.kv_postprocess_blksize_and_layout_on_receive)Transforms the layout of received KV cache to the local block_size and LBHNC.

-
–[kv_postprocess_blksize_on_receive](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.utils.kv_postprocess_blksize_on_receive)Transforms the layout of received KV cache blocks to the local block_size.

-
–[kv_postprocess_layout_on_receive](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.utils.kv_postprocess_layout_on_receive)Transforms the layout of received KV cache blocks to the local format.

-
–[yield_req_data](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.utils.yield_req_data)Yields:


##

`EngineTransferInfo`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.utils.EngineTransferInfo)

Common per-remote-engine transfer state, computed at handshake.

Stored per `(engine_id, pp_rank)`

inside `TransferTopology._engines`

.

Attributes:

-
([end_layer](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.utils.EngineTransferInfo.end_layer)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Exclusive global index after the last layer owned by this PP rank.

-
([remote_block_len](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.utils.EngineTransferInfo.remote_block_len)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Block length (bytes)

-
([remote_block_size](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.utils.EngineTransferInfo.remote_block_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Tokens per block.

-
([remote_dcp_size](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.utils.EngineTransferInfo.remote_dcp_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Remote decode context parallel size.

-
([remote_physical_blocks_per_logical](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.utils.EngineTransferInfo.remote_physical_blocks_per_logical)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Physical blocks per logical block.

-
([remote_pp_rank](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.utils.EngineTransferInfo.remote_pp_rank)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Remote producer PP rank for this engine.

-
([start_layer](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.utils.EngineTransferInfo.start_layer)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Global index of the first layer owned by this PP rank.


## Source code in `vllm/distributed/kv_transfer/kv_connector/utils.py`


###

`end_layer = 0`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.utils.EngineTransferInfo.end_layer)

Exclusive global index after the last layer owned by this PP rank.

###

`remote_block_len`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.utils.EngineTransferInfo.remote_block_len)

Block length (bytes)

###

`remote_block_size`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.utils.EngineTransferInfo.remote_block_size)

Tokens per block.

###

`remote_dcp_size = 1`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.utils.EngineTransferInfo.remote_dcp_size)

Remote decode context parallel size.

###

`remote_physical_blocks_per_logical`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.utils.EngineTransferInfo.remote_physical_blocks_per_logical)

Physical blocks per logical block.

###

`remote_pp_rank = 0`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.utils.EngineTransferInfo.remote_pp_rank)

Remote producer PP rank for this engine.

###

`start_layer = 0`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.utils.EngineTransferInfo.start_layer)

Global index of the first layer owned by this PP rank.

##

`KVOutputAggregator`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.utils.KVOutputAggregator)

Utility class to aggregate the output of all workers into a single output corresponding to Rank 0 for scheduler.

## Source code in `vllm/distributed/kv_transfer/kv_connector/utils.py`


|
|

##

`TransferTopology`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.utils.TransferTopology)

Single source of truth for local TP identity and per-engine remote info.

Methods:

-
–[block_size_ratio](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.utils.TransferTopology.block_size_ratio)Calculate the block size ratio between local and remote.

-
–[dcp_consumer_count](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.utils.TransferTopology.dcp_consumer_count)How many local ranks (in aggregate) read from a given remote rank.

-
–[dcp_source_ranks](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.utils.TransferTopology.dcp_source_ranks)Remote ranks whose DCP slice overlaps mine (MLA,

`remote_dcp_size > 1`

). -
–[describe](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.utils.TransferTopology.describe)One-line summary of transfer config for logging.

-
–[handshake_target_ranks](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.utils.TransferTopology.handshake_target_ranks)Pre-registration: compute which remote TP ranks to handshake with.

-
–[is_kv_replicated](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.utils.TransferTopology.is_kv_replicated)Whether the KV cache is replicated across TP workers due to the

-
–[register_remote_engine](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.utils.TransferTopology.register_remote_engine)Register a remote engine, unifying worker dicts state.

-
–[target_remote_ranks](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.utils.TransferTopology.target_remote_ranks)Get the remote TP rank(s) that the current local TP rank will

-
–[tp_ratio](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.utils.TransferTopology.tp_ratio)Calculate the tensor parallel ratio between local and remote TP.


Attributes:

-
([dcp_rank](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.utils.TransferTopology.dcp_rank)

) –[int](https://docs.python.org/3/builtins/functions.html#int)This rank's DCP coverage rank.

-
([local_replicates_kv_cache](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.utils.TransferTopology.local_replicates_kv_cache)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether the local engine's KV cache is replicated.


## Source code in `vllm/distributed/kv_transfer/kv_connector/utils.py`


|
|

###

`dcp_rank`

`property`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.utils.TransferTopology.dcp_rank)

This rank's DCP coverage rank.

with `dcp_size in (1, tp_size)`

enforced at the connector boundary, a rank's DCP identity is always exactly `tp_rank % dcp_size`

.

###

`local_replicates_kv_cache`

`property`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.utils.TransferTopology.local_replicates_kv_cache)

Whether the local engine's KV cache is replicated.

###

`block_size_ratio(remote_block_size)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.utils.TransferTopology.block_size_ratio)

Calculate the block size ratio between local and remote.

## Source code in `vllm/distributed/kv_transfer/kv_connector/utils.py`


###

`dcp_consumer_count(remote_tp_size, remote_dcp_size)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.utils.TransferTopology.dcp_consumer_count)

How many local ranks (in aggregate) read from a given remote rank.

Used by the producer side to know how many reader notifications to wait for before freeing a request's blocks. Reuses `tp_ratio`

whenever the remote isn't sharded — a sharded local side already has `tp_size == dcp_size`

, so the existing TP-ratio formula is already correct there unmodified.

## Source code in `vllm/distributed/kv_transfer/kv_connector/utils.py`


###

`dcp_source_ranks(remote_tp_size, remote_dcp_size)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.utils.TransferTopology.dcp_source_ranks)

Remote ranks whose DCP slice overlaps mine (MLA, `remote_dcp_size > 1`

).

Shared by `handshake_target_ranks`

(who to query metadata from) and `compute_tp_mapping`

(who to actually read from) — for MLA the two questions have the identical answer, since DCP sharding is the only thing keeping a remote rank from being interchangeable with any other.

## Source code in `vllm/distributed/kv_transfer/kv_connector/utils.py`


###

`describe(remote_engine_id, remote_pp_rank=0)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.utils.TransferTopology.describe)

One-line summary of transfer config for logging.

## Source code in `vllm/distributed/kv_transfer/kv_connector/utils.py`


###

`handshake_target_ranks(remote_tp_size, remote_dcp_size=1)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.utils.TransferTopology.handshake_target_ranks)

Pre-registration: compute which remote TP ranks to handshake with.

Pure math based on local/remote TP (and DCP, when the remote shards its KV cache) sizes — does not require the remote engine to be registered yet.

DCP support is scoped to `dcp_size in (1, tp_size)`

on each side and DCP sizes that divide one another: neither side ever has a partially-duplicated, partially-sharded KV cache. When the remote is not sharded (`remote_dcp_size == 1`

) this reduces exactly to the DTP>=PTP case, since a sharded local side already has `tp_size == dcp_size`

.

## Source code in `vllm/distributed/kv_transfer/kv_connector/utils.py`


###

`is_kv_replicated(remote_engine_id, remote_pp_rank=0)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.utils.TransferTopology.is_kv_replicated)

Whether the KV cache is replicated across TP workers due to the number of TP workers being greater than the number of KV heads.

## Source code in `vllm/distributed/kv_transfer/kv_connector/utils.py`


###

`register_remote_engine(remote_engine_id, info)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.utils.TransferTopology.register_remote_engine)

Register a remote engine, unifying worker dicts state.

The caller (worker) is responsible for computing the info via the transfer policy. This method only stores and deduplicates.

## Source code in `vllm/distributed/kv_transfer/kv_connector/utils.py`


###

`target_remote_ranks(remote_engine_id, remote_pp_rank=0)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.utils.TransferTopology.target_remote_ranks)

Get the remote TP rank(s) that the current local TP rank will read from. When remote tp_size > local tp_size, reads from multiple remote ranks.

## Source code in `vllm/distributed/kv_transfer/kv_connector/utils.py`


###

`tp_ratio(remote_tp_size)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.utils.TransferTopology.tp_ratio)

Calculate the tensor parallel ratio between local and remote TP.

Positive when local_tp >= remote_tp (local workers read from the same remote worker in groups of size `tp_ratio`

). Negative when remote_tp > local_tp (ratio is flipped).

## Source code in `vllm/distributed/kv_transfer/kv_connector/utils.py`


##

`copy_kv_blocks(src_kv_caches, dst_kv_caches, src_block_ids, dst_block_ids, direction)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.utils.copy_kv_blocks)

Copy kv blocks between different buffers.

## Source code in `vllm/distributed/kv_transfer/kv_connector/utils.py`


##

`get_current_attn_backend(vllm_config, layer_names=None)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.utils.get_current_attn_backend)

Get the first attention backend for the given layers.

## Source code in `vllm/distributed/kv_transfer/kv_connector/utils.py`


##

`get_current_attn_backends(vllm_config, layer_names=None)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.utils.get_current_attn_backends)

Get all distinct attention backends for the given layers.

Parameters:

-

(`vllm_config`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.utils.get_current_attn_backends(vllm_config))

) –[VllmConfig](https://docs.vllm.ai/config/#vllm.config.VllmConfig)The current vLLM configuration.

-

(`layer_names`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.utils.get_current_attn_backends(layer_names))

, default:[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)] | None`None`

) –Optional list of layer names to scope the lookup. When None, all attention layers are considered.


Returns:

-

–[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[type](https://docs.python.org/3/builtins/functions.html#type)[[AttentionBackend](https://docs.vllm.ai/v1/attention/backend/#vllm.v1.attention.backend.AttentionBackend)]]Deduplicated list of attention backend classes.


## Source code in `vllm/distributed/kv_transfer/kv_connector/utils.py`


##

`kv_postprocess_blksize_and_layout_on_receive(cache, indices, block_size_ratio)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.utils.kv_postprocess_blksize_and_layout_on_receive)

Transforms the layout of received KV cache to the local block_size and LBHNC. (Only works for local blocksize > remote blocksize)

prefill is LBHNC, smaller block_size decode(local) is LBNHC, larger block_size

## Source code in `vllm/distributed/kv_transfer/kv_connector/utils.py`


##

`kv_postprocess_blksize_on_receive(cache, indices, block_size_ratio)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.utils.kv_postprocess_blksize_on_receive)

Transforms the layout of received KV cache blocks to the local block_size. (Only works for local blocksize > remote blocksize)

Example: local blocksize = 16 tokens, remote blocksize = 4 tokens local block[0] = remote block[0, 1, 2, 3] remote is |h0-b0|h1-b0|h2-b0|h3-b0|h0-b1|h1-b1|h2-b1|h3-b1|... local is |h0-b0..................|h1-b0..................|... permute is to: 1. view => view remote as n_blocks * remote_shape(H,remoteN,D) 2. permute => (H, nblocks, remoteN, D) 3. flatten => (H, localN, D)

## Source code in `vllm/distributed/kv_transfer/kv_connector/utils.py`


##

`kv_postprocess_layout_on_receive(cache, indices)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.utils.kv_postprocess_layout_on_receive)

Transforms the layout of received KV cache blocks to the local format.

This method corrects layout mismatches from direct memory copies by permuting the tensor dimensions.

4D cache: - **Source Layout:** `[num_blocks, n_kv_head, block_size, head_dim]`

- **Target Layout:** `[num_blocks, block_size, n_kv_head, head_dim]`

5D cache: - **Source Layout:** `[num_blocks, kv_dim, n_kv_head, block_size, head_dim]`

- **Target Layout:** `[num_blocks, kv_dim, block_size, n_kv_head, head_dim]`


Implementation: - x = blocks_to_update.reshape(src_shape) # view local kv with sender layout - permuted_blocks = x.permute(*inv_order) # transpose n_kv_heads, block_size - cache.index_copy_(0, indices, permuted_blocks) # copy permuted kv back

## Source code in `vllm/distributed/kv_transfer/kv_connector/utils.py`


##

`yield_req_data(scheduler_output)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.utils.yield_req_data)

Yields: (req_id, new_block_id_groups, preempted)