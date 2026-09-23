source: https://docs.vllm.ai/en/latest/api/vllm/distributed/weight_transfer/sparse_nccl_engine/
lastmod: 2026-09-23

#

`vllm.distributed.weight_transfer.sparse_nccl_engine`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sparse_nccl_engine)

Sparse NCCL weight transfer engine.

Sparse patches use checkpoint names, shapes, and flat indices. The model's native weight loader maps them to rank-local runtime parameters, including TP shards and packed parameters.

Classes:

-
–[SparseNCCLTrainerInitInfo](https://docs.vllm.ai#vllm.distributed.weight_transfer.sparse_nccl_engine.SparseNCCLTrainerInitInfo)Trainer-side init info for the sparse NCCL weight transfer backend.

-
–[SparseNCCLTrainerWeightTransferEngine](https://docs.vllm.ai#vllm.distributed.weight_transfer.sparse_nccl_engine.SparseNCCLTrainerWeightTransferEngine)Trainer-side sparse NCCL weight transfer engine.

-
–[SparseNCCLWeightTransferEngine](https://docs.vllm.ai#vllm.distributed.weight_transfer.sparse_nccl_engine.SparseNCCLWeightTransferEngine)Sparse weight transfer engine using NCCL.

-
–[SparseNCCLWeightTransferUpdateInfo](https://docs.vllm.ai#vllm.distributed.weight_transfer.sparse_nccl_engine.SparseNCCLWeightTransferUpdateInfo)Update info for the sparse NCCL weight transfer backend.

-
–[SparseWeightPatch](https://docs.vllm.ai#vllm.distributed.weight_transfer.sparse_nccl_engine.SparseWeightPatch)A sparse patch in checkpoint coordinates.


##

`SparseNCCLTrainerInitInfo`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sparse_nccl_engine.SparseNCCLTrainerInitInfo)

Bases: [TrainerInitInfo](https://docs.vllm.ai/base/#vllm.distributed.weight_transfer.base.TrainerInitInfo)

Trainer-side init info for the sparse NCCL weight transfer backend.

Same rendezvous shape as the dense NCCL backend (the sender opens its endpoint as NCCL rank 0), but with no packed wire params: sparse transfers are never packed. `backend`

is the factory dispatch key.

## Source code in `vllm/distributed/weight_transfer/sparse_nccl_engine.py`


##

`SparseNCCLTrainerWeightTransferEngine`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sparse_nccl_engine.SparseNCCLTrainerWeightTransferEngine)

Bases: [TrainerWeightTransferEngine](https://docs.vllm.ai/base/#vllm.distributed.weight_transfer.base.TrainerWeightTransferEngine)[[SparseNCCLTrainerInitInfo](https://docs.vllm.ai#vllm.distributed.weight_transfer.sparse_nccl_engine.SparseNCCLTrainerInitInfo)]

Trainer-side sparse NCCL weight transfer engine.

Broadcasts flat-index (indices, values) patches from NCCL rank 0 while the inference-side `update_weights`

runs concurrently on a side thread (the worker's recvs rendezvous inside the same NCCL broadcasts). `send_weights`

owns a complete one-shot lifecycle. RL infrastructure that owns the generic client lifecycle can call `send_weight_chunk`

between one start and finish.

Sparse patches differ every round, so they are not a stable `WeightSource`

: the engine takes no `source`

, and patches are passed directly to the send methods. An empty patch list is a no-op.

Only the designated trainer sender joins the transfer group; other trainer ranks skip sparse sends.

Methods:

-
–[send_weight_chunk](https://docs.vllm.ai#vllm.distributed.weight_transfer.sparse_nccl_engine.SparseNCCLTrainerWeightTransferEngine.send_weight_chunk)Broadcast one chunk inside a caller-owned weight update lifecycle.

-
–[send_weights](https://docs.vllm.ai#vllm.distributed.weight_transfer.sparse_nccl_engine.SparseNCCLTrainerWeightTransferEngine.send_weights)Broadcast one sparse update through a one-shot lifecycle.


## Source code in `vllm/distributed/weight_transfer/sparse_nccl_engine.py`


|
|

###

`_post_send_sync()`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sparse_nccl_engine.SparseNCCLTrainerWeightTransferEngine._post_send_sync)

Wait for the broadcasts to land before returning, so a caller may rebuild or free the patch tensors as soon as a send method returns rather than relying on same-stream ordering. See `NCCLTrainerWeightTransferEngine._post_send_sync`

for why there is no cross-rank barrier.

## Source code in `vllm/distributed/weight_transfer/sparse_nccl_engine.py`


###

`_validate_patch(patch)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sparse_nccl_engine.SparseNCCLTrainerWeightTransferEngine._validate_patch)

Reject a malformed patch before starting the NCCL transfer.

## Source code in `vllm/distributed/weight_transfer/sparse_nccl_engine.py`


###

`send_weight_chunk(patches=None)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sparse_nccl_engine.SparseNCCLTrainerWeightTransferEngine.send_weight_chunk)

Broadcast one chunk inside a caller-owned weight update lifecycle.

## Source code in `vllm/distributed/weight_transfer/sparse_nccl_engine.py`


###

`send_weights(patches=None)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sparse_nccl_engine.SparseNCCLTrainerWeightTransferEngine.send_weights)

Broadcast one sparse update through a one-shot lifecycle.

## Source code in `vllm/distributed/weight_transfer/sparse_nccl_engine.py`


##

`SparseNCCLWeightTransferEngine`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sparse_nccl_engine.SparseNCCLWeightTransferEngine)

Bases: [WeightTransferEngine](https://docs.vllm.ai/base/#vllm.distributed.weight_transfer.base.WeightTransferEngine)[[NCCLWeightTransferInitInfo](https://docs.vllm.ai/nccl_common/#vllm.distributed.weight_transfer.nccl_common.NCCLWeightTransferInitInfo), [SparseNCCLWeightTransferUpdateInfo](https://docs.vllm.ai#vllm.distributed.weight_transfer.sparse_nccl_engine.SparseNCCLWeightTransferUpdateInfo)]

Sparse weight transfer engine using NCCL.

Receives checkpoint-coordinate patches broadcast from the trainer and applies them through the model's native weight loader. Sparse updates modify initialized model tensors in place, so the layerwise reload lifecycle is not used.

Methods:

-
–[finish_weight_update](https://docs.vllm.ai#vllm.distributed.weight_transfer.sparse_nccl_engine.SparseNCCLWeightTransferEngine.finish_weight_update)No-op: sparse patches are applied in place, no layerwise reload.

-
–[init_transfer_engine](https://docs.vllm.ai#vllm.distributed.weight_transfer.sparse_nccl_engine.SparseNCCLWeightTransferEngine.init_transfer_engine)Initialize the NCCL process group with the trainer.

-
–[receive_weights](https://docs.vllm.ai#vllm.distributed.weight_transfer.sparse_nccl_engine.SparseNCCLWeightTransferEngine.receive_weights)Receive sparse flat-index patches from the trainer and apply them.

-
–[start_weight_update](https://docs.vllm.ai#vllm.distributed.weight_transfer.sparse_nccl_engine.SparseNCCLWeightTransferEngine.start_weight_update)No-op: sparse patches are applied in place, no layerwise reload.


## Source code in `vllm/distributed/weight_transfer/sparse_nccl_engine.py`


|
|

###

`finish_weight_update()`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sparse_nccl_engine.SparseNCCLWeightTransferEngine.finish_weight_update)

###

`init_transfer_engine(init_info)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sparse_nccl_engine.SparseNCCLWeightTransferEngine.init_transfer_engine)

Initialize the NCCL process group with the trainer.

## Source code in `vllm/distributed/weight_transfer/sparse_nccl_engine.py`


###

`receive_weights(update_info)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sparse_nccl_engine.SparseNCCLWeightTransferEngine.receive_weights)

Receive sparse flat-index patches from the trainer and apply them.

## Source code in `vllm/distributed/weight_transfer/sparse_nccl_engine.py`


##

`SparseNCCLWeightTransferUpdateInfo`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sparse_nccl_engine.SparseNCCLWeightTransferUpdateInfo)

Bases: [WeightTransferUpdateInfo](https://docs.vllm.ai/base/#vllm.distributed.weight_transfer.base.WeightTransferUpdateInfo)

Update info for the sparse NCCL weight transfer backend.

Attributes:

-
([num_updates_list](https://docs.vllm.ai#vllm.distributed.weight_transfer.sparse_nccl_engine.SparseNCCLWeightTransferUpdateInfo.num_updates_list)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]Number of sparse entries to receive for each parameter in

`names`

.

## Source code in `vllm/distributed/weight_transfer/sparse_nccl_engine.py`


###

`num_updates_list`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sparse_nccl_engine.SparseNCCLWeightTransferUpdateInfo.num_updates_list)

Number of sparse entries to receive for each parameter in `names`

.

##

`SparseWeightPatch`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sparse_nccl_engine.SparseWeightPatch)

A sparse patch in checkpoint coordinates.

Attributes:

-
([full_shape](https://docs.vllm.ai#vllm.distributed.weight_transfer.sparse_nccl_engine.SparseWeightPatch.full_shape)

) –[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[int](https://docs.python.org/3/builtins/functions.html#int), ...]Full checkpoint shape.


## Source code in `vllm/distributed/weight_transfer/sparse_nccl_engine.py`


###

`full_shape`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.sparse_nccl_engine.SparseWeightPatch.full_shape)

Full checkpoint shape.