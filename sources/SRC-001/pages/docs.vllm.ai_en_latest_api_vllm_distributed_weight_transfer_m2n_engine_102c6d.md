source: https://docs.vllm.ai/en/latest/api/vllm/distributed/weight_transfer/m2n_engine/
lastmod: 2026-09-27

#

`vllm.distributed.weight_transfer.m2n_engine`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_engine)

Inference-side weight transfer engine built on NCCL M2N (`nccl_m2n`

).

The trainer and the inference workers share one NCCL communicator: trainer ranks occupy `[0, T)`

, workers `[T, T + N)`

. Each parameter is moved with a single `nccl.m2n.reshard`

, which redistributes it from the trainer's layout (FSDP / EP / arbitrary DTensor sharding) to the inference layout — so the trainer sends its local shards and never all-gathers a full tensor, which is what the broadcast NCCL backend forces it to do.

When an incoming checkpoint parameter maps directly to a live vLLM parameter, M2N reshards into that worker's local model storage. Parameters whose names or layouts cannot be resolved receive a full tensor and fall back to `load_weights`

, preserving the existing backend's loading behavior.

Both meshes participate in every reshard, in the same order, so this backend has the same concurrency shape as the broadcast NCCL backend: the worker must be inside `receive_weights`

while the trainer is sending. Driving that from the trainer is the trainer engine's job.

Classes:

-
–[M2NWeightTransferEngine](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_engine.M2NWeightTransferEngine)Inference-side engine: receives each parameter with one reshard.

-
–[M2NWeightTransferInitInfo](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_engine.M2NWeightTransferInitInfo)Worker-side init info: the rendezvous plus the full transfer plan.

-
–[M2NWeightTransferUpdateInfo](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_engine.M2NWeightTransferUpdateInfo)Per-round update info: which parameters this chunk carries, in order.


##

`M2NWeightTransferEngine`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_engine.M2NWeightTransferEngine)

Bases: [WeightTransferEngine](https://docs.vllm.ai/base/#vllm.distributed.weight_transfer.base.WeightTransferEngine)[[M2NWeightTransferInitInfo](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_engine.M2NWeightTransferInitInfo), [M2NWeightTransferUpdateInfo](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_engine.M2NWeightTransferUpdateInfo)]

Inference-side engine: receives each parameter with one reshard.

Resolvable parameters are resharded from the trainer layout directly into each worker's live local model storage. Unresolvable parameters receive a full tensor and use `load_weights`

. In both cases, the trainer sends its local shards without materializing a full tensor.

Methods:

-
–[finish_weight_update](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_engine.M2NWeightTransferEngine.finish_weight_update)Finalize layerwise reloading when the plan uses fallback entries.

-
–[init_transfer_engine](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_engine.M2NWeightTransferEngine.init_transfer_engine)Join the trainer's communicator and rebuild the transfer plan.

-
–[receive_weights](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_engine.M2NWeightTransferEngine.receive_weights)Receive each requested parameter using its initialization-time plan.

-
–[shutdown](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_engine.M2NWeightTransferEngine.shutdown)Finish pending GPU work and release M2N communication state.

-
–[start_weight_update](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_engine.M2NWeightTransferEngine.start_weight_update)Set up layerwise reloading, but only if some parameter needs it.


## Source code in `vllm/distributed/weight_transfer/m2n_engine.py`


|
|

###

`_reshard(comm, stream, src_meta, dst_placements, dst_buffer)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_engine.M2NWeightTransferEngine._reshard)

Reshard one parameter from its trainer layout into a worker buffer.

`dst_placements`

describes the buffer's logical placement over the worker mesh; `dst_buffer`

is this rank's physical storage.

## Source code in `vllm/distributed/weight_transfer/m2n_engine.py`


###

`finish_weight_update()`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_engine.M2NWeightTransferEngine.finish_weight_update)

Finalize layerwise reloading when the plan uses fallback entries.

## Source code in `vllm/distributed/weight_transfer/m2n_engine.py`


###

`init_transfer_engine(init_info)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_engine.M2NWeightTransferEngine.init_transfer_engine)

Join the trainer's communicator and rebuild the transfer plan.

Every precondition (dtype, tensor rank, divisibility) is checked here so a bad plan fails the init RPC instead of hanging the first collective.

## Source code in `vllm/distributed/weight_transfer/m2n_engine.py`


|
|

###

`receive_weights(update_info)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_engine.M2NWeightTransferEngine.receive_weights)

Receive each requested parameter using its initialization-time plan.

## Source code in `vllm/distributed/weight_transfer/m2n_engine.py`


###

`shutdown()`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_engine.M2NWeightTransferEngine.shutdown)

Finish pending GPU work and release M2N communication state.

## Source code in `vllm/distributed/weight_transfer/m2n_engine.py`


###

`start_weight_update()`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_engine.M2NWeightTransferEngine.start_weight_update)

Set up layerwise reloading, but only if some parameter needs it.

Directly-resharded parameters are written in place and never go through `load_weights`

, so a plan with no fallback entries has nothing to reload.

## Source code in `vllm/distributed/weight_transfer/m2n_engine.py`


##

`M2NWeightTransferInitInfo`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_engine.M2NWeightTransferInitInfo)

Bases: [WeightTransferInitInfo](https://docs.vllm.ai/base/#vllm.distributed.weight_transfer.base.WeightTransferInitInfo)

Worker-side init info: the rendezvous plus the full transfer plan.

Layouts are static for the whole run, so they ride the one-time init handshake and the per-round update info stays a list of names. Everything is plain JSON so the HTTP control plane carries it unchanged.

Attributes:

-
([dst_mesh_dims](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_engine.M2NWeightTransferInitInfo.dst_mesh_dims)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]The inference mesh, starting at

`rank_offset`

. Declared rather than -
([rank_offset](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_engine.M2NWeightTransferInitInfo.rank_offset)

) –[int](https://docs.python.org/3/builtins/functions.html#int)First worker rank, i.e. the number of trainer ranks.

-
([src_mesh_dims](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_engine.M2NWeightTransferInitInfo.src_mesh_dims)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]The trainer's mesh, shared by every parameter (

`start_rank`

is 0: the -
([src_placements](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_engine.M2NWeightTransferInitInfo.src_placements)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)] | None]Per parameter, relative to

`src_mesh_dims`

;`None`

means replicated. -
([world_size](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_engine.M2NWeightTransferInitInfo.world_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Trainer ranks + all inference workers.


## Source code in `vllm/distributed/weight_transfer/m2n_engine.py`


###

`dst_mesh_dims`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_engine.M2NWeightTransferInitInfo.dst_mesh_dims)

The inference mesh, starting at `rank_offset`

. Declared rather than derived so both sides describe the destination identically.

###

`rank_offset`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_engine.M2NWeightTransferInitInfo.rank_offset)

First worker rank, i.e. the number of trainer ranks.

###

`src_mesh_dims`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_engine.M2NWeightTransferInitInfo.src_mesh_dims)

The trainer's mesh, shared by every parameter (`start_rank`

is 0: the trainer occupies the front of the communicator).

###

`src_placements`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_engine.M2NWeightTransferInitInfo.src_placements)

Per parameter, relative to `src_mesh_dims`

; `None`

means replicated.

###

`world_size`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_engine.M2NWeightTransferInitInfo.world_size)

Trainer ranks + all inference workers.

##

`M2NWeightTransferUpdateInfo`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_engine.M2NWeightTransferUpdateInfo)

Bases: [WeightTransferUpdateInfo](https://docs.vllm.ai/base/#vllm.distributed.weight_transfer.base.WeightTransferUpdateInfo)

Per-round update info: which parameters this chunk carries, in order.

Shapes, dtypes and layouts were fixed at init, so a round only needs to say what is coming and in what order — both sides must issue their reshards in exactly that order.