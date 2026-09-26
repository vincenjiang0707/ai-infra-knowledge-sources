source: https://docs.vllm.ai/en/latest/api/vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/worker/
lastmod: 2026-09-24

#

`vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.worker`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.worker)

Worker-side logic for MooncakeStoreConnector.

Includes the store worker, transfer threads, lookup server, and MooncakeDistributedStore integration.

Classes:

-
–[KVCacheStoreRecvingThread](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.worker.KVCacheStoreRecvingThread)Background thread for loading KV cache blocks from the store.

-
–[KVCacheStoreSendingThread](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.worker.KVCacheStoreSendingThread)Background thread for storing KV cache blocks to the store.

-
–[KVTransferThread](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.worker.KVTransferThread)Base class for async KV cache transfer threads.

-
–[LookupKeyClient](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.worker.LookupKeyClient)ZMQ client for the LookupKey admin channel.

-
–[LookupKeyServer](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.worker.LookupKeyServer)ZMQ server on worker rank 0 for the LookupKey admin channel.

-
–[MooncakeStoreWorker](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.worker.MooncakeStoreWorker)Worker-side component for MooncakeStoreConnector.


Functions:

-
–[get_zmq_rpc_path_lookup](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.worker.get_zmq_rpc_path_lookup)Construct IPC path for ZMQ lookup socket.

-
–[resolve_store_tp_size](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.worker.resolve_store_tp_size)Resolve the common Store TP requested by connector config.


##

`KVCacheStoreRecvingThread`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.worker.KVCacheStoreRecvingThread)

Bases: [KVTransferThread](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.worker.KVTransferThread)

Background thread for loading KV cache blocks from the store.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/worker.py`


|
|

##

`KVCacheStoreSendingThread`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.worker.KVCacheStoreSendingThread)

Bases: [KVTransferThread](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.worker.KVTransferThread)

Background thread for storing KV cache blocks to the store.

Methods:

-
–[finish_store_job](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.worker.KVCacheStoreSendingThread.finish_store_job)Retire a job from the ledger and report its blocks as no longer read.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/worker.py`


|
|

###

`_boundary_snapshot_puts(req_meta, entries)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.worker.KVCacheStoreSendingThread._boundary_snapshot_puts)

Puts for committed mamba "align" boundary-state snapshots.

These are block-aligned boundaries, i.e. exactly what the normal save would key — but `store_mask`

masks mamba groups out of it entirely, so this is their *only* writer. The exclusion is not an optimization: the normal save resolves a chunk's address as `req_meta.block_ids[g][start // block_size]`

, and `block_ids`

is the connector's append-only mirror of the core's per-group table. An align-mode table is mutated in place (a superseded state block is freed and nulled; speculative blocks relocate), and the connector is never told, so a stale mirror entry is indistinguishable from a live one — a retry of a failed or pressure-skipped chunk would read a block that now belongs to another request.

Each entry's handed-off block *is* the boundary state and is pinned by the core, so it is uploaded under its boundary-end hash key and never resolved positionally.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/worker.py`


###

`_get_retry_token_ids(req_meta)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.worker.KVCacheStoreSendingThread._get_retry_token_ids)

Return retry state only if this store job is still live.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/worker.py`


###

`_maybe_offload_boundary_states(req_meta)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.worker.KVCacheStoreSendingThread._maybe_offload_boundary_states)

Persist connector-pinned mamba "align" boundary states handed off for this request, deduped against the store.

This is every mamba key the connector writes — `store_mask`

excludes mamba groups from the positional normal save, aligned boundaries included (see :meth:`_boundary_snapshot_puts`

).

The two entry kinds are keyed and sourced differently, so they are prepared separately and put in one batch:

- block-aligned for its group: a committed boundary-state snapshot, the handed-off block itself;
- not block-aligned: the sub-block CoW partial tail, which also has to cover the other groups' blocks in the normal save's lcm gap.

Returns:

-

–[bool](https://docs.python.org/3/builtins/functions.html#bool)True when no put is needed or every put succeeds, False otherwise.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/worker.py`


|
|

###

`_sub_block_tail_puts(req_meta, entries)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.worker.KVCacheStoreSendingThread._sub_block_tail_puts)

Puts for the request's sub-block partial tail (its last prompt hash boundary), so a later request can hit the sub-block prefix.

Covers every group's blocks from the normal save's lcm floor to the boundary: the normal save floors to `lcm_block_size`

, so a smaller-block group's full blocks in that gap are never persisted elsewhere, and the consumer's lookup needs every group at every probed boundary. Full blocks are keyed by their block-end hash and the partial boundary block by the boundary sub-hash; a mamba "align" group contributes only its boundary block, from the core-provided CoW block.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/worker.py`


###

`_update_retry_token_ids(req_meta, save_completed, token_ids_start, event_token_ids)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.worker.KVCacheStoreSendingThread._update_retry_token_ids)

Update retry state without letting a stale job touch a reused ID.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/worker.py`


###

`finish_store_job(req_meta)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.worker.KVCacheStoreSendingThread.finish_store_job)

Retire a job from the ledger and report its blocks as no longer read.

Every path out of a job must reach this, skips and failures included: a job that never reports leaves its blocks referenced for the rest of the run. The discard is a no-op for a job whose generation already retired.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/worker.py`


##

`KVTransferThread`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.worker.KVTransferThread)

Bases: [Thread](https://docs.python.org/3/library/threading.html#threading.Thread)

Base class for async KV cache transfer threads.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/worker.py`


|
|

##

`LookupKeyClient`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.worker.LookupKeyClient)

ZMQ client for the LookupKey admin channel.

Routes both prefix-cache lookups and admin commands (currently: `reset`

) to `LookupKeyServer`

on worker rank 0. The first frame of every request is a named tag from `protocol.py`

.

Methods:

-
–[discard](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.worker.LookupKeyClient.discard)Drop any cached/in-flight lookup for

`req_id`

(e.g. on abort). -
–[lookup](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.worker.LookupKeyClient.lookup)If non_block is True, will return None until the result is ready,


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/worker.py`


|
|

###

`_reset()`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.worker.LookupKeyClient._reset)

Trigger `store.remove_all(force=True)`

on worker rank 0.

Ordering assumption: caller MUST ensure no in-flight Mooncake lookups or transfers when invoking reset. In RL workflows this holds naturally at the step boundary after weight updates and rollout drain. Returns True on ACK, False on NACK.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/worker.py`


###

`discard(req_id)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.worker.LookupKeyClient.discard)

Drop any cached/in-flight lookup for `req_id`

(e.g. on abort).

###

`lookup(req_id, num_tokens, block_hashes, non_block=False)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.worker.LookupKeyClient.lookup)

If non_block is True, will return None until the result is ready, so the caller retries on a later step.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/worker.py`


##

`LookupKeyServer`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.worker.LookupKeyServer)

ZMQ server on worker rank 0 for the LookupKey admin channel.

Handles two request types, tagged at frame 0: - `LOOKUP_MSG`

: prefix-cache hit query, returns its load plan. - `RESET_MSG`

: drains the send thread queue, then runs `store.remove_all(force=True)`

. Caller must have paused the scheduler first.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/worker.py`


|
|

##

`MooncakeStoreWorker`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.worker.MooncakeStoreWorker)

Worker-side component for MooncakeStoreConnector.

Methods:

-
–[close](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.worker.MooncakeStoreWorker.close)Release the MooncakeDistributedStore handle on teardown.

-
–[get_finished](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.worker.MooncakeStoreWorker.get_finished)Get completed send/recv request IDs.

-
–[get_transfer_results](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.worker.MooncakeStoreWorker.get_transfer_results)Get completed sends/recvs plus requests whose remote KV load failed.

-
–[lookup](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.worker.MooncakeStoreWorker.lookup)Check how many prefix tokens exist in the store.

-
–[register_kv_caches](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.worker.MooncakeStoreWorker.register_kv_caches)Register KV cache tensors and start transfer threads.

-
–[start_load_kv](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.worker.MooncakeStoreWorker.start_load_kv)Issue async loads.

-
–[wait_for_save](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.worker.MooncakeStoreWorker.wait_for_save)Issue async stores with CUDA event synchronization.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/worker.py`


|
|

###

`_build_token_databases(metadata, layout_cls)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.worker.MooncakeStoreWorker._build_token_databases)

Construct token databases and their Store layouts.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/worker.py`


###

`_close_ended_store_requests(finished_req_ids, meta)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.worker.MooncakeStoreWorker._close_ended_store_requests)

Retire the ledger entries of requests that finished or were preempted.

An entry may only go once its jobs have drained, because they still read the resume offset it owns; a request that comes back after preemption then saves from the start rather than from where the last attempt got to.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/worker.py`


###

`_compute_group_tp_replication_factors()`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.worker.MooncakeStoreWorker._compute_group_tp_replication_factors)

Return the number of byte-identical TP replicas per cache group.

DCP and Mamba use 1; MLA uses `tp_size`

; GQA uses `tp_size // num_kv_head`

.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/worker.py`


###

`_select_store_layout(extra_config)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.worker.MooncakeStoreWorker._select_store_layout)

Select the opt-in TP layout and its Store namespace.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/worker.py`


|
|

###

`_tail_key_boundaries(block_hashes, hit_length, cached_block_pool)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.worker.MooncakeStoreWorker._tail_key_boundaries)

Return the hash boundary used to store each group's tail block.

With fine-grained prefix matching, `hit_length`

may fall within a physical cache block and may not align with the hash boundary used to store that block. For each KV-cache group, return the token boundary whose hash was used as the store key.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/worker.py`


###

`close()`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.worker.MooncakeStoreWorker.close)

Release the MooncakeDistributedStore handle on teardown.

Closing the store frees its TransferEngine, the registered RDMA buffers, and the connection to the master server. Idempotent so it is safe to call from both the explicit shutdown path and `__del__`

.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/worker.py`


###

`get_finished(finished_req_ids, meta)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.worker.MooncakeStoreWorker.get_finished)

Get completed send/recv request IDs.

Loads are issued in start_load_kv() and stores in wait_for_save().

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/worker.py`


###

`get_transfer_results(finished_req_ids, meta)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.worker.MooncakeStoreWorker.get_transfer_results)

Get completed sends/recvs plus requests whose remote KV load failed.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/worker.py`


###

`lookup(num_tokens, block_hashes)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.worker.MooncakeStoreWorker.lookup)

Check how many prefix tokens exist in the store.

Checks across all rank-specific key namespaces that may be loaded. A hit covering all `num_tokens`

is re-derived below the request end so the last token is recomputed for sampling.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/worker.py`


|
|

###

`register_kv_caches(kv_caches)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.worker.MooncakeStoreWorker.register_kv_caches)

Register KV cache tensors and start transfer threads.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/worker.py`


|
|

###

`start_load_kv(metadata)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.worker.MooncakeStoreWorker.start_load_kv)

Issue async loads.

Runs after the forward launch on steps without sync loads (SchedulerOutput.has_sync_kv_loads), keeping load submission off the critical path while preserving compute-I/O overlap.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/worker.py`


###

`wait_for_save(metadata)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.worker.MooncakeStoreWorker.wait_for_save)

Issue async stores with CUDA event synchronization.

Runs after the forward launch for compute-I/O overlap.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/worker.py`


##

`_split_disk_offload_load_batches(keys, addrs, sizes, usable_budget_bytes, raw_budget_bytes)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.worker._split_disk_offload_load_batches)

Split a GET into sub-batches that fit the owner's staging buffer.

`addrs[i]`

/ `sizes[i]`

are scatter-gather lists (K/V or multi-layer segments) for key `i`

. `usable_budget_bytes`

caps a multi-key batch; `raw_budget_bytes`

is the hard per-key cap.

Returns `(batches, oversize_key)`

. Aborts with `([], key)`

if any single key exceeds `raw_budget_bytes`

; otherwise `oversize_key`

is `None`

.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/worker.py`


##

`get_zmq_rpc_path_lookup(vllm_config)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.worker.get_zmq_rpc_path_lookup)

Construct IPC path for ZMQ lookup socket.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/worker.py`


##

`resolve_store_tp_size(extra_config)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.mooncake.store.worker.resolve_store_tp_size)

Resolve the common Store TP requested by connector config.