source: https://docs.vllm.ai/en/latest/api/vllm/distributed/weight_transfer/m2n_trainer/
lastmod: 2026-09-27

#

`vllm.distributed.weight_transfer.m2n_trainer`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_trainer)

Trainer-side weight transfer engine for the NCCL M2N backend.

Symmetric to `M2NWeightTransferEngine`

but in the training process. Every trainer rank joins the shared communicator and runs every reshard, sending its own local shard; only rank 0 touches the inference control plane.

Workers join the communicator during init and run reshard from inside `update_weights`

, so those two RPCs overlap with work on this side. Both run on a helper thread and are joined afterwards, which keeps that overlap inside the engine -- where the `TrainerWeightTransferEngine`

contract puts it -- rather than in every caller.

Classes:

-
–[M2NTrainerInitInfo](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_trainer.M2NTrainerInitInfo)Trainer-side init info for nccl_m2n.

-
–[M2NTrainerWeightTransferEngine](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_trainer.M2NTrainerWeightTransferEngine)Trainer-side engine: sends every rank's local shard, once per parameter.


##

`M2NTrainerInitInfo`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_trainer.M2NTrainerInitInfo)

Bases: [TrainerInitInfo](https://docs.vllm.ai/base/#vllm.distributed.weight_transfer.base.TrainerInitInfo)

Trainer-side init info for nccl_m2n.

`rank`

(from `TrainerInitInfo`

) is this trainer process's rank; it is also its rank in the shared communicator, since the trainer occupies `[0, num_trainer_ranks)`

. Rank 0 drives the control plane.

Methods:

-
–[__post_init__](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_trainer.M2NTrainerInitInfo.__post_init__)Reject rank counts or destination meshes that cannot form a group.


Attributes:

-
([destination_mesh_dims](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_trainer.M2NTrainerInitInfo.destination_mesh_dims)

) –[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[int](https://docs.python.org/3/builtins/functions.html#int),[int](https://docs.python.org/3/builtins/functions.html#int)]`dst_mesh_dims`

, or a flat mesh over every inference worker. -
([dst_mesh_dims](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_trainer.M2NTrainerInitInfo.dst_mesh_dims)

) –[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[int](https://docs.python.org/3/builtins/functions.html#int),[int](https://docs.python.org/3/builtins/functions.html#int)] | NoneHow the inference ranks are laid out: axis 0 replicates and axis 1

-
([world_size](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_trainer.M2NTrainerInitInfo.world_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Trainer ranks + all inference workers.


## Source code in `vllm/distributed/weight_transfer/m2n_trainer.py`


###

`destination_mesh_dims`

`property`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_trainer.M2NTrainerInitInfo.destination_mesh_dims)

`dst_mesh_dims`

, or a flat mesh over every inference worker.

###

`dst_mesh_dims = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_trainer.M2NTrainerInitInfo.dst_mesh_dims)

How the inference ranks are laid out: axis 0 replicates and axis 1 shards. The trainer declares it so both sides describe the destination identically; defaults to a flat `(num_workers, 1)`

, which is all a replicated destination needs.

###

`world_size`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_trainer.M2NTrainerInitInfo.world_size)

Trainer ranks + all inference workers.

###

`__post_init__()`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_trainer.M2NTrainerInitInfo.__post_init__)

Reject rank counts or destination meshes that cannot form a group.

## Source code in `vllm/distributed/weight_transfer/m2n_trainer.py`


##

`M2NTrainerWeightTransferEngine`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_trainer.M2NTrainerWeightTransferEngine)

Bases: [TrainerWeightTransferEngine](https://docs.vllm.ai/base/#vllm.distributed.weight_transfer.base.TrainerWeightTransferEngine)[[M2NTrainerInitInfo](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_trainer.M2NTrainerInitInfo)]

Trainer-side engine: sends every rank's local shard, once per parameter.

Called on every trainer rank. All ranks join the communicator and run every reshard; only rank 0 touches the control plane.

Methods:

-
–[__init__](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_trainer.M2NTrainerWeightTransferEngine.__init__)Hold the client and source;

`trainer_init`

fills in the group. -
–[send_weights](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_trainer.M2NTrainerWeightTransferEngine.send_weights)Drive one update round: start, reshard concurrently, then finish.

-
–[shutdown](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_trainer.M2NTrainerWeightTransferEngine.shutdown)Destroy the m2n handle, join the helper thread, and drop the group.

-
–[trainer_init](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_trainer.M2NTrainerWeightTransferEngine.trainer_init)Build the engine and rendezvous with the inference side.


## Source code in `vllm/distributed/weight_transfer/m2n_trainer.py`


|
|

###

`__init__(*, client, source, is_controller, num_trainer_ranks)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_trainer.M2NTrainerWeightTransferEngine.__init__)

Hold the client and source; `trainer_init`

fills in the group.

## Source code in `vllm/distributed/weight_transfer/m2n_trainer.py`


###

`_receive_destination_plan(first_worker_rank)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_trainer.M2NTrainerWeightTransferEngine._receive_destination_plan)

Receive and validate the inference-side per-parameter placements.

## Source code in `vllm/distributed/weight_transfer/m2n_trainer.py`


###

`_send()`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_trainer.M2NTrainerWeightTransferEngine._send)

Reshard each local shard into its worker-planned destination.

## Source code in `vllm/distributed/weight_transfer/m2n_trainer.py`


###

`_worker_init_info(init_info)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_trainer.M2NTrainerWeightTransferEngine._worker_init_info)

Handshake payload: rendezvous, both meshes, and the transfer plan.

## Source code in `vllm/distributed/weight_transfer/m2n_trainer.py`


###

`send_weights()`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_trainer.M2NTrainerWeightTransferEngine.send_weights)

Drive one update round: start, reshard concurrently, then finish.

## Source code in `vllm/distributed/weight_transfer/m2n_trainer.py`


###

`shutdown()`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_trainer.M2NTrainerWeightTransferEngine.shutdown)

Destroy the m2n handle, join the helper thread, and drop the group.

## Source code in `vllm/distributed/weight_transfer/m2n_trainer.py`


###

`trainer_init(init_info, *, client, source=None)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.m2n_trainer.M2NTrainerWeightTransferEngine.trainer_init)

Build the engine and rendezvous with the inference side.

Runs on *every* trainer rank. Rank 0 additionally ships the transfer plan to the workers and drives the control plane; the other ranks only build local state and join the communicator. Every rank participates in every reshard and sends its local shard.

The ordering here is not arbitrary -- see the comments inline. In short: validate before anything blocks; start the init RPC without waiting (workers join the communicator inside that RPC, so it cannot return until this side has joined too); then join the NCCL communicator; then create the M2N handle; and only then wait for the RPC to finish.

## Source code in `vllm/distributed/weight_transfer/m2n_trainer.py`


|
|