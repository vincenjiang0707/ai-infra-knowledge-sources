source: https://docs.vllm.ai/en/latest/api/vllm/distributed/weight_transfer/sharded_rdt_engine/
lastmod: 2026-09-23

#

`vllm.distributed.weight_transfer.sharded_rdt_engine`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine)

Sharded Ray Direct Transport (RDT) weight transfer engine (consumer side).

Pulls only the slice each vLLM worker consumes under tensor/expert parallelism, not the full HF-format tensor.

Two phases. BAKE, once at `init_transfer_engine`

: drive `model.load_weights`

against `FakeRDTTensor`

placeholders and record, per leaf module, how each destination slice is fetched (an op chain) and where it lands (an `as_strided`

descriptor). REPLAY, every sync: no `load_weights`

, no `FakeRDTTensor`

dispatch, no discovery — pull the recorded slices in packed chunks over a ring of receive buffers, scatter them into freshly materialized params, then quant and kernel-copy. A live name with no recorded plan fails the plan build: there is no fallback load.

Weights arrive in checkpoint format: the engine drives layerwise reload itself, in `start_weight_update`

/ `finish_weight_update`

.

### Data flow[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine--data-flow)

One thing at four resolutions, over three lifetimes. `FetchKey`

-- `(name, op_chain)`

, "which slice of which trainer tensor" -- is the atom; everything else is bookkeeping around it.

```
BAKE once at init, kept for the engine's life
FakeRDTTensor intercepts the model's loaders; each copy_ records a
_Scatter (sharded_rdt_fake): src FetchKey, owning layer, the destination
as_strided region, and the produced dtype/nbytes.
-> _name_to_plan: name -> that module's scatter list
PLAN once, cached, _build_call_plan
_Chunk one packed pull: its scatters, deduped keys, the byte-exact
pack_layout, which producer serves it, and what to run after
(materialize / quant / free). One per (group, owner class).
_CallPlan all chunks + pre_free.
RUN per chunk, per sync, _run_chunk_pipeline
_Chunk -> _PendingPull issued, not yet landed: Ray ref, buffer views,
ring slot. [RPC thread]
-> _ProcItem chunk + results + slot. [hand-off to the
background scatter thread]
```


The RUN pair stays split on purpose: it is the thread boundary, and only `targets`

should outlive the get -- carrying the Ray ref and the whole-buffer blob into the queue would keep both alive for the scatter's lifetime.

See docs/training/weight_transfer/sharded_rdt.md for the design and the measured results behind the choices here.

Classes:

-
–[ShardedRDTWeightTransferEngine](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferEngine)Pull-based RDT/NIXL backend that transports only the slice each worker

-
–[ShardedRDTWeightTransferInitInfo](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferInitInfo)Initialization info for the sharded RDT backend.

-
–[ShardedRDTWeightTransferUpdateInfo](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferUpdateInfo)Update info for the sharded RDT backend: intentionally EMPTY.


##

`ShardedRDTWeightTransferEngine`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferEngine)

Bases: [WeightTransferEngine](https://docs.vllm.ai/base/#vllm.distributed.weight_transfer.base.WeightTransferEngine)[[ShardedRDTWeightTransferInitInfo](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferInitInfo), [ShardedRDTWeightTransferUpdateInfo](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferUpdateInfo)]

Pull-based RDT/NIXL backend that transports only the slice each worker consumes.

Requires `distributed_executor_backend="ray"`

, `nixl`

in the shared env, a named trainer actor exposing a `@ray.method(tensor_transport="nixl")`

producer, and weight loaders that stay inside `SUPPORTED_OPS`

— anything needing real data (`.to`

, `.item`

, arithmetic, bool-mask indexing) raises during the bake.

The plan is baked once at `init_transfer_engine`

into one scatter list per fully-loaded leaf module, indexed by source name; every `update_weights`

replays the modules its gathered names cover.

Methods:

-
–[drain_pending](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferEngine.drain_pending)Block until the background thread has processed every queued item and

-
–[finish_weight_update](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferEngine.finish_weight_update)Drain the deferred pull/process pipeline (so every layer is fully

-
–[init_transfer_engine](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferEngine.init_transfer_engine)Configure the ring, bind the producers, bake the replay plan, and

-
–[receive_weights](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferEngine.receive_weights)Pull + replay the baked leaf modules the sync covers.

-
–[start_weight_update](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferEngine.start_weight_update)Put the model's params on meta so layerwise reload streams them in

-
–[update_weights](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferEngine.update_weights)Receive one update. Unlike the base, does NOT issue a per-update


## Source code in `vllm/distributed/weight_transfer/sharded_rdt_engine.py`


|
|

###

`_bake(init_info)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferEngine._bake)

Bake the replay plan once, as a self-driven meta dry run.

Puts the params on meta, then drives `model.load_weights`

over `init_info.names`

through the model's ORIGINAL loaders (the stamps bypass `online_process_loader`

, so `_layerwise_process`

is never in the path). Nothing materializes or pulls; the fake's `copy_`

records the source op chain and the meta destination's geometry. Afterwards one scatter list per fully-loaded leaf module (copied numel == loadable size) is indexed by source name; a partial or unrecordable module fails the plan build. The model is restored.

This leans on layerwise internals a public API should expose first-class: a currently-loading hook instead of monkeypatched stamps, a dry-run mode instead of bypassing `online_process_loader`

, and an `abort_layerwise_reload`

instead of `_restore_after_dry_run`

.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_engine.py`


|
|

###

`_build_call_plan(names, group_lens)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferEngine._build_call_plan)

Build the STATIC plan for one whole-sync call.

Pure — no pulls, no engine state touched — so the result is cached and reused every sync. Three passes: 1. Split `names`

into gather groups, one chunk per owner class present in this worker's baked copies, recording each group's last chunk for its `free_group`

signal (or `pre_free`

when this worker pulls nothing from it). Every group is signaled exactly once by construction. The stream has no per-group call boundaries, so group L+1's first chunk issues while L's still stream. 2. Per leaf module, find its FIRST and LAST chunk — materialize on the first, quant/kernel/reset on the last, correct by construction instead of by runtime counters. 3. Assemble `_Chunk`

s: dedup keys and precompute the packed layout.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_engine.py`


|
|

###

`_build_fake_weights(names, sink, device)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferEngine._build_fake_weights)

Zero-storage lazies for `names`

, dtype/shape from the init metadata, all feeding the bake's recording sink.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_engine.py`


###

`_build_static_plan(init_info)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferEngine._build_static_plan)

Build the chunk/free plan once. It never changes across syncs, so `update_weights`

needs no per-sync names.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_engine.py`


###

`_chunk_module_scatters(modules)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferEngine._chunk_module_scatters)

Cut the modules' copies into one chunk per distinct owner class present, ascending by class index, as `(class_idx, scatters)`

pairs.

A chunk is one packed pull, so every name in it must share a producer — which is exactly what an owner class is. The cut is a pure function of the bake and the ownership table. Copy order within a chunk is bake order, and a module's copies may span chunks (materialize/quant fire on its first/last chunk; see `_build_call_plan`

).

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_engine.py`


###

`_complete_pull(pending)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferEngine._complete_pull)

Blocking half of a pull: the NIXL read lands during this `ray.get`

.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_engine.py`


###

`_configure_ring(init_info)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferEngine._configure_ring)

Ring depth K.

Must run before `_ensure_proc_worker`

creates the per-slot events and counters, and before any buffer is grown (both happen on the first pull).

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_engine.py`


###

`_dispatch_item(item)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferEngine._dispatch_item)

Hand one chunk item to the background scatter thread.

Counts the item against its slot BEFORE dispatch: the next pull into that slot must wait until the background thread has processed (and RECORDED the read-done event for) every item ever queued on it.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_engine.py`


###

`_ensure_proc_worker()`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferEngine._ensure_proc_worker)

Lazily create the per-slot events, the background CUDA stream, the work queue, and the single processing thread. Idempotent.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_engine.py`


###

`_global_worker_index()`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferEngine._global_worker_index)

This worker's stable, distinct global index across the inference fleet: `data_parallel_index * world_size + rank`

over the TP*PP world.

`data_parallel_index`

, not `data_parallel_rank`

: vLLM resets the latter to 0 in a dense worker but keeps the former as the distinct global DP rank. Same formula as the sibling `nccl_engine`

, so dense-via-TP and MoE-via-DP+EP both yield distinct 0..C-1.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_engine.py`


###

`_install_recording_stamps(model, recorder)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferEngine._install_recording_stamps)

Wrap each loadable param's `weight_loader`

to stamp `recorder.current = (leaf_module, param_name)`

before delegating to the original loader, so the fake's `copy_`

can attribute each recorded copy. `functools.wraps`

keeps the loader's real signature (so vLLM's `_layerwise_process`

`param`

redirect still works if a stamp leaks), and `_rdt_stamp_inner`

tags it so `_restore_after_dry_run`

can unwrap it.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_engine.py`


###

`_issue_pull(chunk, slot)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferEngine._issue_pull)

Reserve `slot`

, lay the targets out in its buffer, dispatch the produce RPC and point the transfer at the buffer — WITHOUT the blocking `ray.get`

(that is `_complete_pull`

). The chunked pipeline issues chunk i+1 before completing chunk i, so the producer serves the next chunk while the in-flight RDMA streams.

Slot-reuse guard, both stages required: a generation wait (the CUDA event binds only to its LAST record, so synchronizing before the background thread recorded this item's event passes silently — observed as nondeterministic weight corruption), then the event synchronize. It must precede `set_target_for_ref`

, not just the get: the transfer may start any time after the metadata push. See the doc's "slot generation handshake".

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_engine.py`


###

`_mark_slot_done(slot)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferEngine._mark_slot_done)

Publish that a queued item's read-done event has been recorded (or the item failed) so a pull waiting to reuse `slot`

can proceed to its CUDA-event synchronize.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_engine.py`


###

`_num_consumers()`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferEngine._num_consumers)

Total inference-worker count. Prefers the driver-supplied `init_info.num_consumers`

(authoritative -- the driver knows the whole fleet); else `world_size_across_dp`

, the same stride `_global_worker_index`

indexes with, so the two agree at any pp.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_engine.py`


###

`_preregister_at_init()`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferEngine._preregister_at_init)

Register every NIXL buffer this worker will use at init, before any transfer runs, so nothing registers during the sync-0 RDMA churn.

Both sides are sized from the static plan: receive buffers are `ring_depth`

slots at the largest chunk's `pack_bytes`

, and each bound producer is asked to pre-register a serve ring at the max bytes this consumer will pull from it. A no-op when this worker has no chunks.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_engine.py`


###

`_proc_worker_loop()`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferEngine._proc_worker_loop)

Single persistent thread: run each queued item's process phase on the background stream. Exits on the `None`

sentinel (shutdown). An item that raises is recorded in `_proc_error`

and re-raised on the RPC thread / at drain, so a failed sync fails loudly rather than corrupting silently.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_engine.py`


###

`_process_item(item)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferEngine._process_item)

Scatter-thread half: materialize this chunk's first-seen modules, scatter its slices on the process stream, publish the slot, then hand the modules it COMPLETES to the quant thread.

Mirrors `_layerwise_process`

minus the loader replay. Once every scatter reading `item.slot`

is enqueued, records the slot's read-done event so the RPC thread can block on it before overwriting the slot.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_engine.py`


|
|

###

`_pull_targets(chunk, slot, buffer)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferEngine._pull_targets)

Per-key dtype views into `slot`

's buffer.

The packed layout is static, so the views are built once per (chunk, slot) rather than once per pull -- rebuilding them cost ~1150 Python ops per pull at 235B. Keyed on the buffer pointer as well, so a regrow invalidates instead of handing back views into a freed buffer.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_engine.py`


###

`_quant_worker_loop()`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferEngine._quant_worker_loop)

Dedicated quant thread: drains (completed_modules, scatter-done event) batches. Errors surface via _proc_error like the scatter thread's.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_engine.py`


###

`_raise_proc_error()`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferEngine._raise_proc_error)

Re-raise (once) any error captured by the background thread.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_engine.py`


###

`_resolve_consumer_id(init_info)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferEngine._resolve_consumer_id)

This worker's DISTINCT index in 0..C-1 across the whole fleet.

Within one engine that is `_global_worker_index()`

. But a fleet of INDEPENDENT engines (each with its own parallel config) restarts that index at 0 per engine, so each engine offsets into its own range using `replica_rank`

: with a uniform fleet, `workers_per_replica = C // num_replicas`

. `num_replicas`

defaults to 1 (offset 0), preserving single-engine and single-DP-deployment behaviour.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_engine.py`


###

`_resolve_producers(init_info)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferEngine._resolve_producers)

Work out this worker's consumer identity, build the router, and bind EVERY producer actor.

Pull routing is M:N: each chunk goes to ONE producer holding every name in it (see `RdtRouter`

), so one producer serves a whole pull. All producers are bound regardless, because the per-group `free_group`

signal fans out to every owner of a group, including producers this worker never pulls from.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_engine.py`


|
|

###

`_restore_after_dry_run(model)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferEngine._restore_after_dry_run)

Restore each layerwise layer's saved kernel tensors without pulling (a real `finalize_layerwise_reload`

would materialize/load) and reset its info. Also unwrap any recording `stamp`

left on the params, since a leaked stamp would sit under the next sync's `online_process_loader`

and silently break `_layerwise_process`

's `param`

redirect.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_engine.py`


###

`_run_chunk_pipeline(plan)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferEngine._run_chunk_pipeline)

Pipelined chunk pulls over the ring of receive slots.

Issues up to `ring_depth`

produce RPCs ahead of the blocking gets, so while chunk i's RDMA streams the producer serves i+1 into its own ring slot and the background thread scatters i-1 out of another. Reads stay serialized on the shared NIC — the bandwidth floor, not a loss.

Slot safety rests on two arguments spelled out in the doc: the producer's ring is no shallower than this one and drain-before-issue orders its reuse; the consumer's slots are held by `_issue_pull`

's generation handshake.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_engine.py`


###

`_run_quant(layers, ready)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferEngine._run_quant)

Quant/kernel-copy/reset the given COMPLETED leaf modules, exactly as _layerwise_process. Runs on the quant thread's own stream, ordered after the modules' scatters via `ready`

; touches only the scattered params (never a receive slot), so it can overlap subsequent chunks' RDMA and scatters. `info.reset()`

is what makes finalize skip the layer — drain_pending joins the quant queue before finalize runs.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_engine.py`


###

`_signal_group_done(group_idx)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferEngine._signal_group_done)

Fire-and-forget `free_group`

signal at EVERY owner of the group.

The per-group barrier: each owner counts one signal per live consumer and frees the group (releasing its lookahead credit) on the last one, so every owner must hear from every consumer — including owners this worker pulls nothing from. Refs are held and drained in `drain_pending`

so every signal has EXECUTED before the sync ends: `begin_sync`

resets the counters, and a straggler landing in the next sync would credit a group it does not belong to.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_engine.py`


###

`_workers_per_replica(init_info)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferEngine._workers_per_replica)

Consumers per inference deployment, assuming a uniform fleet.

Read by this worker's consumer id and by the router's block carve, which must not disagree, so it is derived once here.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_engine.py`


###

`drain_pending()`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferEngine.drain_pending)

Block until the background thread has processed every queued item and its stream work is complete, then re-raise any error it hit. Called from the worker's `finish_weight_update`

before `finalize_layerwise_reload`

so every baked layer is fully loaded (and `info.reset()`

-ed) first.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_engine.py`


###

`finish_weight_update()`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferEngine.finish_weight_update)

Drain the deferred pull/process pipeline (so every layer is fully loaded) before finalizing the layerwise reload.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_engine.py`


###

`init_transfer_engine(init_info)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferEngine.init_transfer_engine)

Configure the ring, bind the producers, bake the replay plan, and pre-register every NIXL buffer -- in that order, because each step depends on the previous one.

The bake drives `model.load_weights`

and the pre-registration blocks on RPCs to the producers, so this is a heavyweight one-off; every later `update_weights`

is pure replay.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_engine.py`


###

`receive_weights(update_info)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferEngine.receive_weights)

Pull + replay the baked leaf modules the sync covers.

The chunk/free plan is STATIC across syncs — a pure function of the baked plan and the driver's group partition — so it was built once at init and every sync just re-runs the pipeline over its self-describing chunks, with no per-sync bookkeeping and an empty `update_info`

.

Assumes each baked module's source names fall within one gather group, which the per-layer / pre / post partition guarantees (a leaf module's sources all live in one decoder layer). A module that did span groups would be planned once per group and could pull a name whose group the pipeline already freed, which parks the pull until the producer's stall watchdog fires.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_engine.py`


###

`start_weight_update()`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferEngine.start_weight_update)

Put the model's params on meta so layerwise reload streams them in as each layer's slices land. Baked replay uses checkpoint format.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_engine.py`


###

`update_weights(update_info)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferEngine.update_weights)

Receive one update. Unlike the base, does NOT issue a per-update device sync: post-processing is deferred to background threads and a sync here would block on them and serialize the pull/process pipeline. Completion is guaranteed by `drain_pending`

in `finish_weight_update`

.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_engine.py`


##

`ShardedRDTWeightTransferInitInfo`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferInitInfo)

Bases: [WeightTransferInitInfo](https://docs.vllm.ai/base/#vllm.distributed.weight_transfer.base.WeightTransferInitInfo)

Initialization info for the sharded RDT backend.

Attributes:

-
([buffer_presize_gb](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferInitInfo.buffer_presize_gb)

) –[float](https://docs.python.org/3/builtins/functions.html#float)Pre-size each packed receive-buffer slot to this many GiB

-
([dtype_names](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferInitInfo.dtype_names)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]Dtype name (e.g. 'bfloat16') for each entry of

`names`

. -
([group_lens](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferInitInfo.group_lens)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]Partition of

`names`

into gather groups, in the SAME order the trainers -
([name_owner_class](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferInitInfo.name_owner_class)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]Per-name index into

`owner_sets`

, parallel to`names`

: which producers -
([names](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferInitInfo.names)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]The trainer's complete, flat param name list. The bake drives

-
([num_consumers](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferInitInfo.num_consumers)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Total consumer count across the fleet, for M:N routing. Authoritative when

-
([num_rdt_buffers](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferInitInfo.num_rdt_buffers)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Depth of the consumer receive-buffer ring. Must match the

-
([num_replicas](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferInitInfo.num_replicas)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of independent inference engines in the fleet. Default 1 => the

-
([owner_sets](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferInitInfo.owner_sets)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]]The distinct producer sets that occur, each a sorted list of trainer ranks

-
([produce_method_name](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferInitInfo.produce_method_name)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Name of the trainer-side producer method. It and the rest of the serve

-
([replica_rank](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferInitInfo.replica_rank)

) –[int](https://docs.python.org/3/builtins/functions.html#int)This inference engine's ordinal in the fleet (0..

`num_replicas`

-1). -
([shapes](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferInitInfo.shapes)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]]Full HF shape for each entry of

`names`

. -
([trainer_actor_names](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferInitInfo.trainer_actor_names)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]Names of all trainer Ray actors exposing the producer method (set via

-
([trainer_actor_namespace](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferInitInfo.trainer_actor_namespace)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneOptional Ray namespace the trainer actor(s) live in.


## Source code in `vllm/distributed/weight_transfer/sharded_rdt_engine.py`


|
|

###

`buffer_presize_gb = 0.0`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferInitInfo.buffer_presize_gb)

Pre-size each packed receive-buffer slot to this many GiB (0 = size to the first chunk + coarse 256MB round-up). Set it to cover the model's largest atomic chunk (e.g. an untied lm_head). Sizing buffers ONCE matters beyond perf -- see the doc's "Sizing buffers once matters beyond throughput".

###

`dtype_names = field(default_factory=list)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferInitInfo.dtype_names)

Dtype name (e.g. 'bfloat16') for each entry of `names`

.

###

`group_lens = field(default_factory=list)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferInitInfo.group_lens)

Partition of `names`

into gather groups, in the SAME order the trainers gather and publish them (group-major; `sum(group_lens) == len(names)`

, and `names`

must be ordered to match). Required: the engine pre-builds the whole static chunk/signal plan from it at init, and fires `free_group`

at every owner as each group's last chunk completes.

###

`name_owner_class = field(default_factory=list)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferInitInfo.name_owner_class)

Per-name index into `owner_sets`

, parallel to `names`

: which producers hold each name. Empty means every producer holds every name.

This one table expresses every layout the trainer can have — pipeline stages (the names of these groups have this owner set), expert parallelism (this expert name has this one-rank owner set), and combinations of the two — so the engine cuts each group's baked copies into one chunk per distinct class present and routes each chunk to that class's owner. Derived by the trainer from `WeightSource.held_names()`

.

###

`names = field(default_factory=list)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferInitInfo.names)

The trainer's complete, flat param name list. The bake drives `model.load_weights`

over all of them once and keys the plan by source name.

###

`num_consumers = 0`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferInitInfo.num_consumers)

Total consumer count across the fleet, for M:N routing. Authoritative when

0; at 0 the engine infers it from

`parallel_config`

, which is correct for the supported serving modes but worth setting explicitly under M:N. Each worker's distinct index comes from`_global_worker_index`

.

###

`num_rdt_buffers = 2`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferInitInfo.num_rdt_buffers)

Depth of the consumer receive-buffer ring. Must match the producer's — `_run_chunk_pipeline`

's slot-safety argument rests on it. 2 = double buffer: chunk i+1's serve overlaps chunk i's RDMA, and scatter(i-1) overlaps RDMA(i) in the other slot. Keep depth x chunk_bytes under the fabric's address-translation reach (~2-3 GB/flow on the reference 8xB200 RoCE cluster, where K=3 measurably hurt).

###

`num_replicas = 1`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferInitInfo.num_replicas)

Number of independent inference engines in the fleet. Default 1 => the per-replica offset is 0 and consumer identity is exactly `_global_worker_index`

(preserves single-engine and single-DP-deployment behavior). When > 1, `workers_per_replica = num_consumers // num_replicas`

and this engine's consumers occupy `replica_rank * workers_per_replica + _global_worker_index()`

. Assumes a uniform fleet (every replica has the same worker count). Set alongside `replica_rank`

, by the driver.

###

`owner_sets = field(default_factory=list)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferInitInfo.owner_sets)

The distinct producer sets that occur, each a sorted list of trainer ranks (indices into `trainer_actor_names`

). Indexed by `name_owner_class`

. Empty means every producer holds every name.

###

`produce_method_name = 'rdt_produce_weights_batched'`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferInitInfo.produce_method_name)

Name of the trainer-side producer method. It and the rest of the serve surface (`free_group`

, `reserve_serve_buffer`

) are documented where they are implemented, on `_RDTProducerServer`

in `sharded_rdt_trainer.py`

.

###

`replica_rank = 0`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferInitInfo.replica_rank)

This inference engine's ordinal in the fleet (0..`num_replicas`

-1).

Multi-engine deployments run several INDEPENDENT inference engines, each with its own self-contained parallel config, so every engine's `_global_worker_index`

restarts at 0 and would collide across engines. The driver gives each engine a distinct `replica_rank`

(with identical `num_replicas`

) so the engine offsets its consumers into a globally distinct range for the M:N block assignment.Default 0/1 (single engine) needs no override.

###

`shapes = field(default_factory=list)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferInitInfo.shapes)

Full HF shape for each entry of `names`

.

###

`trainer_actor_names = field(default_factory=list)`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferInitInfo.trainer_actor_names)

Names of all trainer Ray actors exposing the producer method (set via `.options(name=...)`

), ordered by trainer rank. `RdtRouter`

picks one of them per pull, out of the name's owner set. Every actor is bound regardless, because `free_group`

fans out to every owner. Must be non-empty; a single-producer trainer passes a one-element list.

###

`trainer_actor_namespace = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferInitInfo.trainer_actor_namespace)

Optional Ray namespace the trainer actor(s) live in.

##

`ShardedRDTWeightTransferUpdateInfo`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine.ShardedRDTWeightTransferUpdateInfo)

Bases: [WeightTransferUpdateInfo](https://docs.vllm.ai/base/#vllm.distributed.weight_transfer.base.WeightTransferUpdateInfo)

Update info for the sharded RDT backend: intentionally EMPTY.

The chunk/free plan is a pure function of the baked plan and the driver's gather-group partition, both fixed for the engine's lifetime, so it is built once at `init_transfer_engine`

from `ShardedRDTWeightTransferInitInfo`

's `names`

+ `group_lens`

. ONE `update_weights`

per sync then just re-runs that plan; there is nothing per-sync to carry.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_engine.py`


##

`_CallPlan`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine._CallPlan)

The static plan for one sync (see Data flow). Pure, so it is built once and reused; runtime is then execution only.

`pre_free`

= groups with NO chunk on this worker, signaled at sync start (owners tolerate a signal preceding its publish). With the last-chunk signals this keeps the completeness invariant consumer-local: every group is signaled exactly once.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_engine.py`


##

`_Chunk`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine._Chunk)

One packed pull plus its post-processing (see Data flow).

A module's copies span chunks when its experts sit in several owner classes, so `materialize`

fires on its FIRST chunk and `quant`

on its LAST -- materialize-once by construction, not by a runtime counter. `pack_layout`

mirrors the producer's rule byte-exactly.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_engine.py`


##

`_PendingPull`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine._PendingPull)

A dispatched pull whose blocking `ray.get`

has not run (see Data flow).

`targets`

/`blob`

must stay strongly referenced until it completes: `set_target_for_ref`

stores WEAKREFS, so dropping them silently reroutes the transfer into a fallback buffer.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_engine.py`


##

`_ProcItem`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine._ProcItem)

A landed pull handed to the background scatter thread (see Data flow).

`results`

alias the ring buffer `slot`

, held as strong refs so they outlive the RPC-thread frame until the scatter consumes them.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_engine.py`


##

`_dtype_from_name(name)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine._dtype_from_name)

Resolve a string like 'bfloat16' to torch.bfloat16.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_engine.py`


##

`_plan_digest(keys_per_chunk)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_engine._plan_digest)

Digest of the chunks one consumer pulls from one producer, in pull order.

Two consumers a producer serves out of ONE shared serve ring must agree on this, since sharing rests on their plans being identical; the producer compares it at init. Over the whole (name, op-chain) list rather than the names, because the chains decide the bytes each pull returns.