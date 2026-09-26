source: https://docs.vllm.ai/en/latest/api/vllm/distributed/weight_transfer/nccl_engine/
lastmod: 2026-09-24

#

`vllm.distributed.weight_transfer.nccl_engine`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.nccl_engine)

NCCL-based (dense) weight transfer engine.

Classes:

-
–[NCCLTrainerInitInfo](https://docs.vllm.ai#vllm.distributed.weight_transfer.nccl_engine.NCCLTrainerInitInfo)Trainer-side init info for the dense NCCL weight transfer backend.

-
–[NCCLTrainerWeightTransferEngine](https://docs.vllm.ai#vllm.distributed.weight_transfer.nccl_engine.NCCLTrainerWeightTransferEngine)Trainer-side NCCL weight transfer engine.

-
–[NCCLWeightTransferEngine](https://docs.vllm.ai#vllm.distributed.weight_transfer.nccl_engine.NCCLWeightTransferEngine)Weight transfer engine using NCCL for communication between trainer and workers.

-
–[NCCLWeightTransferInitInfo](https://docs.vllm.ai#vllm.distributed.weight_transfer.nccl_engine.NCCLWeightTransferInitInfo)Worker-side initialization info for NCCL-based weight transfer backends.

-
–[NCCLWeightTransferUpdateInfo](https://docs.vllm.ai#vllm.distributed.weight_transfer.nccl_engine.NCCLWeightTransferUpdateInfo)Per-round update info for the dense NCCL weight transfer backend.


##

`NCCLTrainerInitInfo`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.nccl_engine.NCCLTrainerInitInfo)

Bases: [TrainerInitInfo](https://docs.vllm.ai/base/#vllm.distributed.weight_transfer.base.TrainerInitInfo)

Trainer-side init info for the dense NCCL weight transfer backend.

The sender opens its endpoint as NCCL rank 0, so it needs no `rank_offset`

. `world_size`

is the full trainer+worker NCCL group size. `rank`

(from `TrainerInitInfo`

) identifies this trainer process; rank 0 is the sender.

The trainer joins over a TCPStore rendezvous (`master_address`

+ `master_port`

). Torch-free trainers (e.g. JAX) that cannot join a TCPStore mint an `ncclUniqueId`

themselves and drive rank 0 out of band; they ship a `nccl_unique_id_b64`

payload straight to the inference workers' `init_weight_transfer_engine`

(see `NCCLWeightTransferInitInfo`

) rather than going through this engine.

`packed`

/ buffer sizes are the transfer's wire params. The trainer propagates them to the worker at `trainer_init`

so the two sides cannot disagree. Note this defaults to packed, unlike the worker-side `NCCLWeightTransferInitInfo`

, whose default only applies when no trainer ships a value. `backend`

is the factory dispatch key.

## Source code in `vllm/distributed/weight_transfer/nccl_engine.py`


##

`NCCLTrainerWeightTransferEngine`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.nccl_engine.NCCLTrainerWeightTransferEngine)

Bases: [TrainerWeightTransferEngine](https://docs.vllm.ai/base/#vllm.distributed.weight_transfer.base.TrainerWeightTransferEngine)[[NCCLTrainerInitInfo](https://docs.vllm.ai#vllm.distributed.weight_transfer.nccl_engine.NCCLTrainerInitInfo)]

Trainer-side NCCL weight transfer engine.

On the sender (rank 0) holds the NCCL communicator and drives the full update round trip: it runs the inference-side `update_weights`

concurrently with the trainer-side broadcast (both rendezvous inside the same NCCL calls), then finishes the update. Non-sender trainer ranks hold no communicator; they only iterate the source to stay in the trainer-side collective (e.g. FSDP `full_tensor()`

) and skip the client RPCs and the broadcast (all guarded on `is_sender`

).

`packed`

/ buffer sizes come from `NCCLTrainerInitInfo`

; the sender propagates them to the worker at `trainer_init`

(on the worker-side init info), so per-round payloads carry only parameter metadata.

## Source code in `vllm/distributed/weight_transfer/nccl_engine.py`


|
|

###

`_broadcast(source, meta)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.nccl_engine.NCCLTrainerWeightTransferEngine._broadcast)

Iterate the source (materializing each tensor — a collective on all ranks) and, on the sender, broadcast from rank 0, packed or one-by-one. Non-sender ranks only replay the iteration to stay in the collective.

## Source code in `vllm/distributed/weight_transfer/nccl_engine.py`


###

`_checked_iter(source, meta)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.nccl_engine.NCCLTrainerWeightTransferEngine._checked_iter)

Yield the source's pairs, checking each against what the worker was told to expect.

The worker sizes its receive buffers — and in packed mode cuts its chunk boundaries — from the update info, which is built from `metadata()`

. If iteration disagrees with it, the two sides split the stream differently and the transfer hangs in NCCL or loads garbage. Checking here costs one comparison per parameter and turns that into an error naming the first divergent parameter. Sender-only: under pipeline parallelism a non-sender's yielded tensor is not meaningful.

## Source code in `vllm/distributed/weight_transfer/nccl_engine.py`


###

`_post_send_sync()`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.nccl_engine.NCCLTrainerWeightTransferEngine._post_send_sync)

Wait for this rank's transfer work to land before returning.

Broadcasts are only *enqueued* by `send_weights`

: the unpacked path on the current stream, the packed path on the producer's own streams (which it drains itself). Waiting here lets a caller mutate parameters, or start the next step on another stream, as soon as `send_weights`

returns, instead of silently depending on same-stream ordering. Every rank waits: a non-sender's `full_tensor()`

gathers feed the sender's broadcast, so they must have landed before it may touch its shards.

Unlike IPC there is no cross-rank barrier here. Nothing in this backend outlives the collective it travelled in (IPC's barrier keeps shared buffers alive until every consumer has opened them), so a barrier would only add a dependency on the default process group that this backend otherwise does not have.

## Source code in `vllm/distributed/weight_transfer/nccl_engine.py`


##

`NCCLWeightTransferEngine`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.nccl_engine.NCCLWeightTransferEngine)

Bases: [WeightTransferEngine](https://docs.vllm.ai/base/#vllm.distributed.weight_transfer.base.WeightTransferEngine)[[NCCLWeightTransferInitInfo](https://docs.vllm.ai/nccl_common/#vllm.distributed.weight_transfer.nccl_common.NCCLWeightTransferInitInfo), [NCCLWeightTransferUpdateInfo](https://docs.vllm.ai#vllm.distributed.weight_transfer.nccl_engine.NCCLWeightTransferUpdateInfo)]

Weight transfer engine using NCCL for communication between trainer and workers.

This implementation uses NCCL broadcast operations to transfer dense checkpoint-format weights from the trainer (rank 0) to all inference workers in a process group. Received weights are loaded via the model's `load_weights`

using the layerwise reload lifecycle.

Methods:

-
–[finish_weight_update](https://docs.vllm.ai#vllm.distributed.weight_transfer.nccl_engine.NCCLWeightTransferEngine.finish_weight_update)Finalize layerwise reloading after all weights have been received.

-
–[init_transfer_engine](https://docs.vllm.ai#vllm.distributed.weight_transfer.nccl_engine.NCCLWeightTransferEngine.init_transfer_engine)Initialize NCCL process group with the trainer and record the

-
–[receive_weights](https://docs.vllm.ai#vllm.distributed.weight_transfer.nccl_engine.NCCLWeightTransferEngine.receive_weights)Receive weights from trainer via NCCL broadcast.

-
–[start_weight_update](https://docs.vllm.ai#vllm.distributed.weight_transfer.nccl_engine.NCCLWeightTransferEngine.start_weight_update)Initialize layerwise reloading for the incoming checkpoint weights.


## Source code in `vllm/distributed/weight_transfer/nccl_engine.py`


|
|

###

`finish_weight_update()`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.nccl_engine.NCCLWeightTransferEngine.finish_weight_update)

Finalize layerwise reloading after all weights have been received.

## Source code in `vllm/distributed/weight_transfer/nccl_engine.py`


###

`init_transfer_engine(init_info)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.nccl_engine.NCCLWeightTransferEngine.init_transfer_engine)

Initialize NCCL process group with the trainer and record the trainer-supplied wire params so the worker decodes exactly as the trainer encodes.

Parameters:

-

(`init_info`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.nccl_engine.NCCLWeightTransferEngine.init_transfer_engine(init_info))

) –[NCCLWeightTransferInitInfo](https://docs.vllm.ai/nccl_common/#vllm.distributed.weight_transfer.nccl_common.NCCLWeightTransferInitInfo)NCCL initialization info containing master address, port, rank offset, world size, and the packed wire params


## Source code in `vllm/distributed/weight_transfer/nccl_engine.py`


###

`receive_weights(update_info)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.nccl_engine.NCCLWeightTransferEngine.receive_weights)

Receive weights from trainer via NCCL broadcast.

Whether to use packed broadcasting (and the buffer geometry) is read from `self.packed`

/ `self.packed_*`

, set at the init handshake from the trainer's init info, so it is guaranteed to match how the trainer encoded.

Parameters:

-

(`update_info`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.nccl_engine.NCCLWeightTransferEngine.receive_weights(update_info))

) –[NCCLWeightTransferUpdateInfo](https://docs.vllm.ai#vllm.distributed.weight_transfer.nccl_engine.NCCLWeightTransferUpdateInfo)NCCL update info containing parameter names, dtypes, and shapes


## Source code in `vllm/distributed/weight_transfer/nccl_engine.py`


###

`start_weight_update()`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.nccl_engine.NCCLWeightTransferEngine.start_weight_update)

Initialize layerwise reloading for the incoming checkpoint weights.

## Source code in `vllm/distributed/weight_transfer/nccl_engine.py`


##

`NCCLWeightTransferInitInfo`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.nccl_engine.NCCLWeightTransferInitInfo)

Bases: [WeightTransferInitInfo](https://docs.vllm.ai/base/#vllm.distributed.weight_transfer.base.WeightTransferInitInfo)

Worker-side initialization info for NCCL-based weight transfer backends.

Keyword-only (`kw_only`

): adding the optional `nccl_unique_id_b64`

field means the rendezvous fields can no longer keep a fixed positional slot, so a stale positional call fails loudly instead of silently swapping arguments.

Provide exactly one rendezvous mode:

`master_address`

+`master_port`

-- TCPStore /`StatelessProcessGroup`

rendezvous (requires torch on every rank, including the trainer), or`nccl_unique_id_b64`

-- standard (RFC 4648,*not*URL-safe) base64 of the 128 raw bytes from`ncclGetUniqueId`

, for torch-free trainers (e.g. JAX) that mint the unique id out of band and share it (over HTTP, etc.). Note a JAX peer must use`base64.b64encode`

, not`urlsafe_b64encode`

.

On the unique-id path all ranks must enter init concurrently (there is no store barrier), and every peer must honor the warm-up handshake: the worker's communicator issues a one-element `all_reduce`

immediately after `ncclCommInitRank`

(see `PyNcclCommunicator.from_unique_id_bytes`

), so a foreign peer must issue a matching one-element `all_reduce`

before any other collective or all ranks deadlock.

## Source code in `vllm/distributed/weight_transfer/nccl_common.py`


##

`NCCLWeightTransferUpdateInfo`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.nccl_engine.NCCLWeightTransferUpdateInfo)

Bases: [WeightTransferUpdateInfo](https://docs.vllm.ai/base/#vllm.distributed.weight_transfer.base.WeightTransferUpdateInfo)

Per-round update info for the dense NCCL weight transfer backend.

Whether the transfer is packed (and the buffer geometry) is a must-agree wire param carried on the init info (`NCCLTrainerInitInfo`

/ `NCCLWeightTransferInitInfo`

), not here; this carries only the per-round parameter metadata.

Methods:

-
–[__post_init__](https://docs.vllm.ai#vllm.distributed.weight_transfer.nccl_engine.NCCLWeightTransferUpdateInfo.__post_init__)Validate that all lists have the same length.


## Source code in `vllm/distributed/weight_transfer/nccl_engine.py`


###

`__post_init__()`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.nccl_engine.NCCLWeightTransferUpdateInfo.__post_init__)

Validate that all lists have the same length.