source: https://docs.vllm.ai/en/latest/api/vllm/distributed/weight_transfer/sharded_rdt_trainer/
lastmod: 2026-09-24

#

`vllm.distributed.weight_transfer.sharded_rdt_trainer`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer)

Trainer-side engine for the sharded-RDT (pull-based NIXL) backend.

RDT is pull-based, so unlike NCCL this engine broadcasts nothing. It owns a per-rank producer server (an internal Ray actor exposing the NIXL serve surface the worker engine dials by name), and on each `send_weights`

gathers this rank's weights group-by-group from the `WeightSource`

, shares each group into the server over CUDA IPC, and — on the sender — drives the inference-side start/update/finish handshake, whose single empty `update_weights`

unblocks the workers to pull.

All serve-side state lives on the server actor, so trainer processes need no mixin, no named actors and no special actor options.

See docs/training/weight_transfer/sharded_rdt.md for the publish -> serve -> free_group -> release lifecycle and the ownership model.

Classes:

-
–[ShardedRDTTrainerInitInfo](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer.ShardedRDTTrainerInitInfo)Trainer init info for the sharded-RDT backend.

-
–[ShardedRDTTrainerWeightTransferEngine](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer.ShardedRDTTrainerWeightTransferEngine)Trainer-side engine for the pull-based sharded-RDT backend.


##

`ShardedRDTTrainerInitInfo`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer.ShardedRDTTrainerInitInfo)

Bases: [TrainerInitInfo](https://docs.vllm.ai/base/#vllm.distributed.weight_transfer.base.TrainerInitInfo)

Trainer init info for the sharded-RDT backend.

Identical on every rank except `rank`

(rank 0 is the sender). Carries only the must-agree wire params; the sender forwards them verbatim onto the worker-side init info so the two cannot drift. Server-actor names are generated per rank and all-gathered by the engine, not supplied here.

Attributes:

-
([buffer_presize_gb](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer.ShardedRDTTrainerInitInfo.buffer_presize_gb)

) –[float](https://docs.python.org/3/builtins/functions.html#float)Serve-buffer pre-size floor in GiB (avoids NIXL desc-cache churn).

-
([gather_lookahead](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer.ShardedRDTTrainerInitInfo.gather_lookahead)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Gathered-but-unfreed groups the gather loop may run ahead by. Bounds

-
([num_consumers](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer.ShardedRDTTrainerInitInfo.num_consumers)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Total inference-worker (consumer) count across the whole fleet

-
([num_rdt_buffers](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer.ShardedRDTTrainerInitInfo.num_rdt_buffers)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Serve/receive ring depth K (must match the worker).

-
([stall_timeout_s](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer.ShardedRDTTrainerInitInfo.stall_timeout_s)

) –[float](https://docs.python.org/3/builtins/functions.html#float)Seconds of no publish/serve/free progress before the producer fails the

-
([trainer_actor_namespace](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer.ShardedRDTTrainerInitInfo.trainer_actor_namespace)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneRay namespace the engine spawns its serve actors in. The inference

-
([workers_per_replica](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer.ShardedRDTTrainerInitInfo.workers_per_replica)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Consumers per inference DEPLOYMENT (

`num_consumers // num_replicas`

).

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_trainer.py`


###

`buffer_presize_gb = 0.0`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer.ShardedRDTTrainerInitInfo.buffer_presize_gb)

Serve-buffer pre-size floor in GiB (avoids NIXL desc-cache churn).

###

`gather_lookahead = DEFAULT_GATHER_LOOKAHEAD`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer.ShardedRDTTrainerInitInfo.gather_lookahead)

Gathered-but-unfreed groups the gather loop may run ahead by. Bounds trainer-resident memory at `gather_lookahead + 1`

groups.

###

`num_consumers`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer.ShardedRDTTrainerInitInfo.num_consumers)

Total inference-worker (consumer) count across the whole fleet (DP*TP*PP*PCP), for the M:N block assignment / free ref-count.

###

`num_rdt_buffers = 2`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer.ShardedRDTTrainerInitInfo.num_rdt_buffers)

Serve/receive ring depth K (must match the worker).

###

`stall_timeout_s = DEFAULT_STALL_TIMEOUT_S`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer.ShardedRDTTrainerInitInfo.stall_timeout_s)

Seconds of no publish/serve/free progress before the producer fails the sync (see `DEFAULT_STALL_TIMEOUT_S`

).

###

`trainer_actor_namespace = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer.ShardedRDTTrainerInitInfo.trainer_actor_namespace)

Ray namespace the engine spawns its serve actors in. The inference workers (which run in their own EngineCore subprocess with its own `ray.init`

) resolve those actors by name, so this must be the namespace they can see. Forwarded to the worker-side init info.

###

`workers_per_replica = 0`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer.ShardedRDTTrainerInitInfo.workers_per_replica)

Consumers per inference DEPLOYMENT (`num_consumers // num_replicas`

).

Fixes the slot-sharing groups: consumers whose ids differ by a multiple of this are the same worker of different deployments, so they bake identical plans and pull byte-identical chunks, and ONE registered serve slot can serve all of them. 0 disables sharing, and so does the single-deployment value `num_consumers`

, which makes every group a singleton and the serve path identical to the unshared one.

##

`ShardedRDTTrainerWeightTransferEngine`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer.ShardedRDTTrainerWeightTransferEngine)

Bases: [TrainerWeightTransferEngine](https://docs.vllm.ai/base/#vllm.distributed.weight_transfer.base.TrainerWeightTransferEngine)[[ShardedRDTTrainerInitInfo](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer.ShardedRDTTrainerInitInfo)]

Trainer-side engine for the pull-based sharded-RDT backend.

Lives on every trainer rank. Owns a per-rank `_RDTProducerServer`

actor (the NIXL serve surface). `send_weights`

gathers this rank's weights group-by-group from the `WeightSource`

, shares each group into the server over CUDA IPC, and — on the sender — drives the inference-side handshake so the workers pull. Non-sender ranks only gather (staying in the collective).

Methods:

-
–[get_worker_init_payload](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer.ShardedRDTTrainerWeightTransferEngine.get_worker_init_payload)The consumer-side init payload, rebuilt on demand. Pure — no collective.

-
–[send_weights](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer.ShardedRDTTrainerWeightTransferEngine.send_weights)Gather this rank's weights and publish them for the consumers to pull.


## Source code in `vllm/distributed/weight_transfer/sharded_rdt_trainer.py`


|
|

###

`_all_gather_owned(world, mine)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer.ShardedRDTTrainerWeightTransferEngine._all_gather_owned)

All-gather each rank's (metadata digest, held-name bitmask).

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_trainer.py`


###

`_await_publish(ref)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer.ShardedRDTTrainerWeightTransferEngine._await_publish)

Resolve one async publish so a server-side rebuild error surfaces at window depth instead of at end_sync. Publishes carry nothing back — freed groups flow only through wait_freed/end_sync (one channel; see publish_group).

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_trainer.py`


###

`_drop_inflight(freed_keys)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer.ShardedRDTTrainerWeightTransferEngine._drop_inflight)

Release a freed group's refs and return its export-ring slot.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_trainer.py`


###

`_meta_digest()`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer.ShardedRDTTrainerWeightTransferEngine._meta_digest)

Stable digest of this rank's metadata (name order + count).

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_trainer.py`


###

`_pack_group_for_export(held, slot_idx)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer.ShardedRDTTrainerWeightTransferEngine._pack_group_for_export)

Copy `held`

into ring slot `slot_idx`

; return `(storages, views, refs)`

in the same shape the per-storage path returns, but with ONE storage. Views are built exactly as `publish_group`

rebuilds them, so the two sides cannot disagree about layout.

Slot safety is not the credit gate alone: that bounds how MANY groups are unfreed, not the order they free in, and barriers do complete out of order. The caller takes `slot_idx`

from a pool keyed by live group (`_slot_of_group`

/ `_free_slots`

); `_drop_inflight`

returns a slot only once its group is freed everywhere.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_trainer.py`


###

`_publish_async(group_idx, entries)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer.ShardedRDTTrainerWeightTransferEngine._publish_async)

Fire publish_group WITHOUT waiting on the RPC (the gather loop overlaps the publish's server-side rebuild with the next group's gather) and return a handle that `_await_publish`

resolves. Ray actor handle in production; a plain (non-Ray) fake server runs inline.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_trainer.py`


###

`_resolve_ownership(world, rank)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer.ShardedRDTTrainerWeightTransferEngine._resolve_ownership)

Resolve which rank holds which name, and this rank's publish plan.

A source may hold only part of the model — pipeline stages, expert parallelism, or any mix — so each rank declares its held names and the fleet all-gathers them. The consumers route per name, so the wire carries the transposed result: the distinct owner sets, and a per-name index into them.

The masks are positional over metadata order, which is why the metadata digest is checked first: a rank whose names disagree would transpose into the wrong owners entirely.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_trainer.py`


|
|

###

`_rpc(method, *args)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer.ShardedRDTTrainerWeightTransferEngine._rpc)

Call one of the server actor's methods and block for the result. The single seam through which the engine talks to its server, so tests can inject a local (non-Ray) fake server.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_trainer.py`


###

`_run_gather_loop(update_future, live_count, live_ids=None)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer.ShardedRDTTrainerWeightTransferEngine._run_gather_loop)

Gather this rank's weights group-by-group and publish each into the server over CUDA IPC. A gathered group is published — serveable — immediately; the loop gates BEFORE the next gather while more than `gather_lookahead`

groups are unfreed (the per-group free barrier: a credit releases when every live consumer has signaled the group). So the loop self-paces to the consumers' pull rate with at most `gather_lookahead + 1`

groups resident. Runs on every rank; only the sender has an `update_future`

to fail fast on.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_trainer.py`


|
|

###

`_validate_held_yields(gi, names, tensors)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer.ShardedRDTTrainerWeightTransferEngine._validate_held_yields)

Check `held_names()`

against what the source actually yields — the one place both sit side by side.

Without it, a source that claims a name but yields `None`

for it dies by stall watchdog 300s later: consumers route pulls here, the pull passes the served-names guard, and the cache wait never completes. With it, that is an immediate error naming the weight. One set lookup per name per sync.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_trainer.py`


###

`get_worker_init_payload()`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer.ShardedRDTTrainerWeightTransferEngine.get_worker_init_payload)

The consumer-side init payload, rebuilt on demand. Pure — no collective.

Reads only retained state, so a restarted inference engine can rejoin at a sync boundary: the driver can ask any time, including mid-run with every rank in its own training step. A collective here would deadlock, since the ranks are not at a matching one.

Raises:

-

–[RuntimeError](https://docs.python.org/3/builtins/exceptions.html#RuntimeError)called before

`trainer_init`

cached the server names.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_trainer.py`


###

`send_weights(live_consumer_ids=None)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer.ShardedRDTTrainerWeightTransferEngine.send_weights)

Gather this rank's weights and publish them for the consumers to pull.

`live_consumer_ids`

restricts the sync to the consumers still alive; `None`

serves the whole provisioned set. The provisioned geometry is FROZEN for the run — a degraded sync only lowers the live count handed to `begin_sync`

. Every rank must get the SAME live set, since they share the gather collectives, so the caller computes it once for all of them.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_trainer.py`


##

`_RDTProducerServer`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer._RDTProducerServer)

Per-rank NIXL serve surface: an internal Ray actor sharing the trainer rank's GPU over CUDA IPC. Holds the gather cache, per-consumer serve rings, the per-group free barrier and the packed serve. The engine feeds it with `publish_group`

; workers pull with `rdt_produce_weights_batched`

and signal with `free_group`

.

A plain class — the engine wraps it with `ray.remote(...)`

at spawn so the actor options live in one place.

Methods:

-
–[begin_sync](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer._RDTProducerServer.begin_sync)Reset per-sync free/backpressure state and set this sync's barrier

-
–[end_sync](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer._RDTProducerServer.end_sync)Block until every published group has been freed by its consumers;

-
–[free_group](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer._RDTProducerServer.free_group)Consumer back-edge: one consumer is done with group

`group_idx`

, -
–[publish_group](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer._RDTProducerServer.publish_group)Rebuild one gather group's CUDA-IPC tensors into the serve cache.

-
–[rdt_produce_weights_batched](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer._RDTProducerServer.rdt_produce_weights_batched)Serve one batched slice request over NIXL.

-
–[reserve_serve_buffer](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer._RDTProducerServer.reserve_serve_buffer)Pre-allocate + NIXL-register this consumer's serve ring before any

-
–[set_gather_error](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer._RDTProducerServer.set_gather_error)Record a trainer-side gather failure so blocked serves / publishes

-
–[wait_freed](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer._RDTProducerServer.wait_freed)Block until at least one published group has been freed; return and

-
–[warmup_nixl](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer._RDTProducerServer.warmup_nixl)Create this server's NIXL agent now, while the rank's GPU is quiet.


## Source code in `vllm/distributed/weight_transfer/sharded_rdt_trainer.py`


|
|

###

`_await_shared_pack(gen)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer._RDTProducerServer._await_shared_pack)

Block until this generation's packer published its blob, and return it. A failed pack is re-raised here, so every sharer of a bad pack fails instead of reading a half-written slot.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_trainer.py`


###

`_fail_shared_pack(gen, exc)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer._RDTProducerServer._fail_shared_pack)

Publish a pack failure so waiting sharers raise instead of hanging on a generation that will never complete.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_trainer.py`


###

`_join_share_group(consumer_id, seq)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer._RDTProducerServer._join_share_group)

Register this call's arrival in its group's rendezvous for `seq`

and return `(generation, is_packer)`

.

Exactly one caller per generation gets `is_packer=True`

, whichever completes the arrival set, and it is the only one that touches the GPU. The slot is `seq % nring`

: fixed by the consumers' issue order, so it needs no release accounting on this side.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_trainer.py`


###

`_new_serve_buffer(nbytes)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer._RDTProducerServer._new_serve_buffer)

Allocate + NIXL-register one serve slot: the single allocation seam, so registration cannot be skipped on either of the two paths that make buffers (the init-time reservation and the serve-path backstop).

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_trainer.py`


###

`_note_progress_locked()`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer._RDTProducerServer._note_progress_locked)

###

`_pack_shared(gen, specs)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer._RDTProducerServer._pack_shared)

Replay the op chains into this generation's slot and publish the blob to the sharers waiting on it.

Runs on exactly one call per generation and OUTSIDE `_cache_cond`

: the pack is GPU work and must not block publishes, frees or other groups.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_trainer.py`


###

`_release_group_locked(group_idx)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer._RDTProducerServer._release_group_locked)

Drop a freed group's cache entries and queue it for the engine (whose gather-credit gate blocks in `wait_freed`

on exactly this).

Shared by the last `free_group`

and by `publish_group`

completing an early-signaled group. Caller must hold `_cache_cond`

.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_trainer.py`


###

`_serve_slot(sg, idx, need)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer._RDTProducerServer._serve_slot)

Group `sg`

's ring slot `idx`

, grown if this chunk outgrew the reservation. Growing registers memory while the fabric is busy, the hazard `reserve_serve_buffer`

exists to avoid, so it is a backstop: the reservation is sized from the same static plan as this pack.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_trainer.py`


###

`_share_group(consumer_id)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer._RDTProducerServer._share_group)

The slot-sharing group `consumer_id`

belongs to: its index within its own deployment, since that is what fixes the plan. Without a width the group is the consumer itself and nothing is shared.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_trainer.py`


###

`_sharers_of(sg)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer._RDTProducerServer._sharers_of)

The LIVE consumers of group `sg`

: the rendezvous width. Derived from `begin_sync`

's live set, so a degraded sync narrows the barrier instead of waiting forever on a dead deployment. Caller holds `_cache_cond`

.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_trainer.py`


###

`_wait_for(blocked, what)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer._RDTProducerServer._wait_for)

`_cache_cond.wait()`

with a liveness bound.

Waits while `blocked()`

holds, returning early on a gather error. If nothing on this producer progresses for `_stall_timeout`

, self-fires `set_gather_error`

, which every waiter here already checks — so the rank unwinds through one path and the driver gets a real exception.

The progress stamp is global to the producer, not per-waiter: a merely slow waiter is kept alive by its peers' progress. Caller holds `_cache_cond`

.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_trainer.py`


###

`begin_sync(live_count, live_consumer_ids=None)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer._RDTProducerServer.begin_sync)

Reset per-sync free/backpressure state and set this sync's barrier target.

`live_count`

is how many consumers take part in THIS sync. Required, no default: a forgotten argument silently targeting 1 would free groups after the FIRST signal while others still pull — use-after-free, not an error. The driver awaits the previous sync's finish before the next begins, so nothing is in flight; a straggler signal would otherwise credit the wrong sync, which is why the consumer drains its signals before finishing.

`live_consumer_ids`

is that same live set enumerated, which is what sizes each slot-sharing group's rendezvous; a count cannot, since a group is a specific set of ids. `None`

leaves every group a singleton.

The packed-destination cache deliberately survives: the layout repeats every sync. So does `_plan_digests`

, which is init-time state.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_trainer.py`


###

`end_sync()`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer._RDTProducerServer.end_sync)

Block until every published group has been freed by its consumers; return the remaining freed keys so the engine drops its last refs.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_trainer.py`


###

`free_group(group_idx)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer._RDTProducerServer.free_group)

Consumer back-edge: one consumer is done with group `group_idx`

, either because its last chunk landed or because it had nothing to pull.

The per-group barrier counts one signal per live consumer against the `begin_sync`

count; every consumer signals every owner, so the target is the same integer everywhere. The last signal drops the cache entries and queues the group as gather credit for `wait_freed`

. A signal arriving before its publish is only counted — `publish_group`

completes it.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_trainer.py`


###

`publish_group(group_idx, entries)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer._RDTProducerServer.publish_group)

Rebuild one gather group's CUDA-IPC tensors into the serve cache.

NEVER blocks: a gathered group is serveable immediately. The memory bound lives in the engine's gather loop, which stops GATHERING (not publishing) past `gather_lookahead`

unfreed groups.

`entries`

is `(storages, views)`

: one CUDA-IPC export per storage, plus per-name `(sid, dtype_name, shape, stride, storage_offset)`

rebuilt here as `as_strided`

views.

Signals can arrive BEFORE their publish — a consumer pulling nothing of a group signals it as its plan starts — so a group whose barrier is already satisfied is released here. Freed groups reach the engine only through `wait_freed`

/ `end_sync`

: a freed notice riding an unharvested async publish result would wedge the loop.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_trainer.py`


###

`rdt_produce_weights_batched(specs, consumer_id=0, seq=-1)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer._RDTProducerServer.rdt_produce_weights_batched)

Serve one batched slice request over NIXL.

Waits until the specs' names are cached, then rendezvouses with the other live sharers of this consumer's slot-sharing group. The last to arrive replays each spec's op chain (pure views into cached tensors, guarded by ALLOWED_OPS) and byte-packs the slices 16B-aligned into the group's ring slot `seq % nring`

, mirroring the consumer's identical layout; every sharer then returns that one packed blob, so R deployments cost one pack and one slot instead of R. With a single deployment every group is a singleton, so the arriving call is always its own packer and this is the unshared serve path exactly.

`seq`

is the caller's index in its pull stream to this producer, which is what fixes the slot. Callers that want a single slice pass one spec and read the blob back with that slice's dtype/shape.

Raises:

-

–[ValueError](https://docs.python.org/3/builtins/exceptions.html#ValueError)`seq`

was not supplied.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_trainer.py`


###

`reserve_serve_buffer(consumer_id, nbytes, plan_digest=None)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer._RDTProducerServer.reserve_serve_buffer)

Pre-allocate + NIXL-register this consumer's serve ring before any pull, while the fabric is idle (avoids registration races during the sync-0 RDMA churn under M:N fan-in). Idempotent; grows only if needed.

The ring is keyed by SLOT-SHARING GROUP, so the sharers of one group reserve ONE ring between them. They all call this, same group and same size, so the whole body runs under `_serve_lock`

, or two concurrent first-callers would each allocate a ring and one would be dropped while still registered.

`plan_digest`

is the caller's ordered chunk plan for THIS producer. Sharers must agree on it, and this is where a disagreement is caught rather than at serve time, where it is a rendezvous nobody completes.

Raises:

-

–[RuntimeError](https://docs.python.org/3/builtins/exceptions.html#RuntimeError)two consumers of one sharing group disagree on the chunks they pull from this producer.


## Source code in `vllm/distributed/weight_transfer/sharded_rdt_trainer.py`


###

`set_gather_error(message)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer._RDTProducerServer.set_gather_error)

Record a trainer-side gather failure so blocked serves / publishes stop waiting and surface it.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_trainer.py`


###

`wait_freed()`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer._RDTProducerServer.wait_freed)

Block until at least one published group has been freed; return and clear the freed backlog. The engine's gather-credit gate calls this once its loop is `gather_lookahead`

groups ahead, so this wait is where the trainer paces to the consumers' pull rate.

Raises rather than returning empty when the sync errors or stalls: the engine is blocked here inside its gather loop, and an empty return would spin it straight back in.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_trainer.py`


###

`warmup_nixl()`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer._RDTProducerServer.warmup_nixl)

Create this server's NIXL agent now, while the rank's GPU is quiet.

Called at spawn, before the server-name all-gather, so no rank can be spinning in a collective. Creating the agent lazily instead deadlocks on EFA-class fabrics (see "warmup_nixl breaks a startup deadlock" in the doc). The warmup buffer stays registered so the agent's CUDA-HMEM path stays initialized.

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_trainer.py`


##

`_SharedPack`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer._SharedPack)

One generation of one slot-sharing group: the rendezvous state for a single chunk, identified by the consumers' issue index.

Attributes:

## Source code in `vllm/distributed/weight_transfer/sharded_rdt_trainer.py`


###

`slot`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sharded_rdt_trainer._SharedPack.slot)

`seq % ring_depth`

. Fixed at creation, so slot reuse follows the consumers' issue order rather than this side's execution order.