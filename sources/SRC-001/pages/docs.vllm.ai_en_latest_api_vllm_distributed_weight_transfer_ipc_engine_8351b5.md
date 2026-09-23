source: https://docs.vllm.ai/en/latest/api/vllm/distributed/weight_transfer/ipc_engine/
lastmod: 2026-09-23

#

`vllm.distributed.weight_transfer.ipc_engine`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.ipc_engine)

IPC-based weight transfer engine using CUDA IPC for communication.

Classes:

-
–[IPCTrainerInitInfo](https://docs.vllm.ai#vllm.distributed.weight_transfer.ipc_engine.IPCTrainerInitInfo)Trainer-side init info for IPC weight transfer. No rendezvous needed;

-
–[IPCTrainerWeightTransferEngine](https://docs.vllm.ai#vllm.distributed.weight_transfer.ipc_engine.IPCTrainerWeightTransferEngine)Trainer-side CUDA IPC weight transfer engine.

-
–[IPCWeightTransferEngine](https://docs.vllm.ai#vllm.distributed.weight_transfer.ipc_engine.IPCWeightTransferEngine)Weight transfer engine using CUDA IPC between trainer and workers.

-
–[IPCWeightTransferInitInfo](https://docs.vllm.ai#vllm.distributed.weight_transfer.ipc_engine.IPCWeightTransferInitInfo)Worker-side init info for IPC weight transfer. No rendezvous needed.

-
–[IPCWeightTransferUpdateInfo](https://docs.vllm.ai#vllm.distributed.weight_transfer.ipc_engine.IPCWeightTransferUpdateInfo)Per-round update info for the IPC weight transfer backend.


##

`IPCTrainerInitInfo`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.ipc_engine.IPCTrainerInitInfo)

Bases: [TrainerInitInfo](https://docs.vllm.ai/base/#vllm.distributed.weight_transfer.base.TrainerInitInfo)

Trainer-side init info for IPC weight transfer. No rendezvous needed; `rank`

(from `TrainerInitInfo`

) identifies this trainer process — rank 0 ships the merged IPC handles. All ranks still join the handle all-gather.

`packed`

/ `packed_buffer_size_bytes`

are the transfer's wire params. The trainer propagates `packed`

to the worker at `trainer_init`

so the two sides cannot disagree. `backend`

is the factory dispatch key.

## Source code in `vllm/distributed/weight_transfer/ipc_engine.py`


##

`IPCTrainerWeightTransferEngine`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.ipc_engine.IPCTrainerWeightTransferEngine)

Bases: [TrainerWeightTransferEngine](https://docs.vllm.ai/base/#vllm.distributed.weight_transfer.base.TrainerWeightTransferEngine)[[IPCTrainerInitInfo](https://docs.vllm.ai#vllm.distributed.weight_transfer.ipc_engine.IPCTrainerInitInfo)]

Trainer-side CUDA IPC weight transfer engine.

Called on every trainer rank. For multi-rank (e.g. FSDP) trainers all ranks iterate the source (materializing each tensor) and contribute to the IPC-handle all-gather; only the sender (rank 0) ships the merged handles to the inference side. IPC transfer is straight-line (no concurrent broadcast like NCCL): `update_weights`

*is* the transfer, and it rides the client, so it no-ops on non-senders.

`packed`

/ `packed_buffer_size_bytes`

come from `IPCTrainerInitInfo`

; the sender propagates `packed`

to the worker at `trainer_init`

.

## Source code in `vllm/distributed/weight_transfer/ipc_engine.py`


|
|

###

`_all_gather_and_merge_handles(handles)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.ipc_engine.IPCTrainerWeightTransferEngine._all_gather_and_merge_handles)

All-gather and merge IPC handle dicts across ranks in one call.

Each rank contributes a list of {gpu_uuid: ipc_args} dicts (one per parameter or one per chunk). A single all_gather_object collects every rank's full list, then the sender merges per-index so each dict maps every GPU UUID to its args.

The all-gather runs over the *default* process group; this assumes the default group is exactly the set of colocated trainer ranks and that the sender is a member. No-op (returns handles unchanged) when no distributed group exists.

## Source code in `vllm/distributed/weight_transfer/ipc_engine.py`


###

`_do_send(names, dtype_names, shapes, ipc_handles, tensor_sizes=None)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.ipc_engine.IPCTrainerWeightTransferEngine._do_send)

Build one update payload and ship it via the client. Only the sender ships (non-sender ranks already contributed to the handle all-gather).

Emits raw `ipc_handles`

; transports that cannot carry them natively (HTTP/JSON) pickle them in their client (see `HTTPVLLMWeightSyncClient`

).

## Source code in `vllm/distributed/weight_transfer/ipc_engine.py`


###

`_post_send_sync()`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.ipc_engine.IPCTrainerWeightTransferEngine._post_send_sync)

Barrier + ipc_collect after a send; no-op if single-GPU.

## Source code in `vllm/distributed/weight_transfer/ipc_engine.py`


###

`_send_packed(source)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.ipc_engine.IPCTrainerWeightTransferEngine._send_packed)

Send weights in bounded-memory chunks (packed mode).

## Source code in `vllm/distributed/weight_transfer/ipc_engine.py`


###

`_send_unpacked(source)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.ipc_engine.IPCTrainerWeightTransferEngine._send_unpacked)

Iterate the source, build one IPC handle per param, all-gather the handles across ranks, and (sender) ship them in one update call.

Returns the strong refs to every contiguous copy. reduce_tensor's args do NOT keep storage alive, and non-contiguous inputs allocate fresh storage in .contiguous(); the caller must keep these alive until the post-send barrier (past `finish`

) so the consumer's IPC views stay valid.

## Source code in `vllm/distributed/weight_transfer/ipc_engine.py`


##

`IPCWeightTransferEngine`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.ipc_engine.IPCWeightTransferEngine)

Bases: [WeightTransferEngine](https://docs.vllm.ai/base/#vllm.distributed.weight_transfer.base.WeightTransferEngine)[[IPCWeightTransferInitInfo](https://docs.vllm.ai#vllm.distributed.weight_transfer.ipc_engine.IPCWeightTransferInitInfo), [IPCWeightTransferUpdateInfo](https://docs.vllm.ai#vllm.distributed.weight_transfer.ipc_engine.IPCWeightTransferUpdateInfo)]

Weight transfer engine using CUDA IPC between trainer and workers.

This implementation uses CUDA IPC to transfer weights from the trainer (rank 0) to all inference workers in a process group. IPC handles are used to share memory between processes on the same node.

Methods:

-
–[finish_weight_update](https://docs.vllm.ai#vllm.distributed.weight_transfer.ipc_engine.IPCWeightTransferEngine.finish_weight_update)Finalize layerwise reloading after all weights have been received.

-
–[init_transfer_engine](https://docs.vllm.ai#vllm.distributed.weight_transfer.ipc_engine.IPCWeightTransferEngine.init_transfer_engine)Initialize the weight transfer mechanism. No data-plane rendezvous is

-
–[receive_weights](https://docs.vllm.ai#vllm.distributed.weight_transfer.ipc_engine.IPCWeightTransferEngine.receive_weights)Receive weights from the trainer via CUDA IPC handles and load them.

-
–[start_weight_update](https://docs.vllm.ai#vllm.distributed.weight_transfer.ipc_engine.IPCWeightTransferEngine.start_weight_update)Initialize layerwise reloading for the incoming checkpoint weights.


## Source code in `vllm/distributed/weight_transfer/ipc_engine.py`


|
|

###

`finish_weight_update()`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.ipc_engine.IPCWeightTransferEngine.finish_weight_update)

Finalize layerwise reloading after all weights have been received.

## Source code in `vllm/distributed/weight_transfer/ipc_engine.py`


###

`init_transfer_engine(init_info)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.ipc_engine.IPCWeightTransferEngine.init_transfer_engine)

Initialize the weight transfer mechanism. No data-plane rendezvous is needed for IPC; this just records the trainer-supplied wire params so the worker decodes exactly as the trainer encoded.

Parameters:

-

(`init_info`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.ipc_engine.IPCWeightTransferEngine.init_transfer_engine(init_info))

) –[IPCWeightTransferInitInfo](https://docs.vllm.ai#vllm.distributed.weight_transfer.ipc_engine.IPCWeightTransferInitInfo)IPC initialization info (carries

`packed`

).

## Source code in `vllm/distributed/weight_transfer/ipc_engine.py`


###

`receive_weights(update_info)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.ipc_engine.IPCWeightTransferEngine.receive_weights)

Receive weights from the trainer via CUDA IPC handles and load them.

Whether the transfer is packed is read from `self.packed`

, set at the init handshake from the trainer's init info, so it is guaranteed to match how the trainer encoded.

Parameters:

-

(`update_info`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.ipc_engine.IPCWeightTransferEngine.receive_weights(update_info))

) –[IPCWeightTransferUpdateInfo](https://docs.vllm.ai#vllm.distributed.weight_transfer.ipc_engine.IPCWeightTransferUpdateInfo)IPC update info containing parameter names, dtypes, shapes, and IPC handles. Each IPC handle is a mapping between physical GPU UUID and the rebuild_cuda_tensor args tuple.


## Source code in `vllm/distributed/weight_transfer/ipc_engine.py`


###

`start_weight_update()`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.ipc_engine.IPCWeightTransferEngine.start_weight_update)

Initialize layerwise reloading for the incoming checkpoint weights.

## Source code in `vllm/distributed/weight_transfer/ipc_engine.py`


##

`IPCWeightTransferInitInfo`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.ipc_engine.IPCWeightTransferInitInfo)

Bases: [WeightTransferInitInfo](https://docs.vllm.ai/base/#vllm.distributed.weight_transfer.base.WeightTransferInitInfo)

Worker-side init info for IPC weight transfer. No rendezvous needed.

`packed`

is a must-agree wire param: the trainer ships it here at the init handshake so the worker decodes with the same setting the trainer encoded with. The consumer rebuilds from the IPC handle + `tensor_sizes`

, so it does not need the buffer size (producer-only).

## Source code in `vllm/distributed/weight_transfer/ipc_engine.py`


##

`IPCWeightTransferUpdateInfo`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.ipc_engine.IPCWeightTransferUpdateInfo)

Bases: [WeightTransferUpdateInfo](https://docs.vllm.ai/base/#vllm.distributed.weight_transfer.base.WeightTransferUpdateInfo)

Per-round update info for the IPC weight transfer backend.

Attributes:

-
([ipc_handles](https://docs.vllm.ai#vllm.distributed.weight_transfer.ipc_engine.IPCWeightTransferUpdateInfo.ipc_handles)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)]] |[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)] | NoneIPC handles mapping physical GPU UUID to rebuild_cuda_tensor args.

-
([ipc_handles_pickled](https://docs.vllm.ai#vllm.distributed.weight_transfer.ipc_engine.IPCWeightTransferUpdateInfo.ipc_handles_pickled)

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneBase64-encoded pickled IPC handles, used for HTTP transport.

-
([tensor_sizes](https://docs.vllm.ai#vllm.distributed.weight_transfer.ipc_engine.IPCWeightTransferUpdateInfo.tensor_sizes)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)] | NonePer-parameter sizes in bytes within the packed buffer.


## Source code in `vllm/distributed/weight_transfer/ipc_engine.py`


###

`ipc_handles = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.ipc_engine.IPCWeightTransferUpdateInfo.ipc_handles)

IPC handles mapping physical GPU UUID to rebuild_cuda_tensor args. For non-packed mode: list of per-parameter handle dicts. For packed mode: single handle dict for the packed buffer.

###

`ipc_handles_pickled = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.ipc_engine.IPCWeightTransferUpdateInfo.ipc_handles_pickled)

Base64-encoded pickled IPC handles, used for HTTP transport.

###

`tensor_sizes = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.ipc_engine.IPCWeightTransferUpdateInfo.tensor_sizes)

Per-parameter sizes in bytes within the packed buffer. Required when packed=True, unused otherwise.