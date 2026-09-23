source: https://docs.vllm.ai/en/latest/api/vllm/distributed/weight_transfer/nccl_common/
lastmod: 2026-09-23

#

`vllm.distributed.weight_transfer.nccl_common`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.nccl_common)

Shared NCCL initialization helpers for weight transfer engines.

The dense (`NCCLWeightTransferEngine`

) and sparse (`SparseNCCLWeightTransferEngine`

) backends are independent engines that share *only* their process-group initialization. That common logic lives here so the sparse engine does not have to subclass the dense one.

Classes:

-
–[NCCLRendezvous](https://docs.vllm.ai#vllm.distributed.weight_transfer.nccl_common.NCCLRendezvous)The TCP rendezvous fields

`trainer_init`

needs. -
–[NCCLWeightTransferInitInfo](https://docs.vllm.ai#vllm.distributed.weight_transfer.nccl_common.NCCLWeightTransferInitInfo)Worker-side initialization info for NCCL-based weight transfer backends.


Functions:

-
–[decode_nccl_unique_id](https://docs.vllm.ai#vllm.distributed.weight_transfer.nccl_common.decode_nccl_unique_id)Validate the rendezvous mode and decode a pre-shared unique id.

-
–[stateless_init_process_group](https://docs.vllm.ai#vllm.distributed.weight_transfer.nccl_common.stateless_init_process_group)VLLM provides

`StatelessProcessGroup`

to create a process group -
–[trainer_init](https://docs.vllm.ai#vllm.distributed.weight_transfer.nccl_common.trainer_init)Initialize NCCL process group for trainer-side weight transfer.

-
–[uid_init_process_group](https://docs.vllm.ai#vllm.distributed.weight_transfer.nccl_common.uid_init_process_group)Join the NCCL group from pre-shared

`ncclUniqueId`

bytes. -
–[worker_init_payload](https://docs.vllm.ai#vllm.distributed.weight_transfer.nccl_common.worker_init_payload)Serialize a worker init info for

`init_weight_transfer_engine`

, dropping -
–[worker_init_process_group](https://docs.vllm.ai#vllm.distributed.weight_transfer.nccl_common.worker_init_process_group)Create the trainer<->worker NCCL group on an inference worker.


##

`NCCLRendezvous`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.nccl_common.NCCLRendezvous)

Bases: [Protocol](https://docs.python.org/3/library/typing.html#typing.Protocol)

The TCP rendezvous fields `trainer_init`

needs.

Structural so each backend can keep its own trainer init info next to its engine (dense `NCCLTrainerInitInfo`

, `SparseNCCLTrainerInitInfo`

) without this shared module importing either.

## Source code in `vllm/distributed/weight_transfer/nccl_common.py`


##

`NCCLWeightTransferInitInfo`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.nccl_common.NCCLWeightTransferInitInfo)

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

`decode_nccl_unique_id(*, master_address, master_port, nccl_unique_id_b64, ctx)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.nccl_common.decode_nccl_unique_id)

Validate the rendezvous mode and decode a pre-shared unique id.

## Source code in `vllm/distributed/weight_transfer/nccl_common.py`


##

`stateless_init_process_group(master_address, master_port, rank, world_size, device)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.nccl_common.stateless_init_process_group)

VLLM provides `StatelessProcessGroup`

to create a process group without considering the global process group in torch.distributed. It is recommended to create `StatelessProcessGroup`

, and then initialize the data-plane communication (NCCL) between external (train processes) and vLLM workers.

## Source code in `vllm/distributed/weight_transfer/nccl_common.py`


##

`trainer_init(init_info)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.nccl_common.trainer_init)

Initialize NCCL process group for trainer-side weight transfer.

The trainer is always rank 0 in the process group. Uses the current CUDA device (torch.accelerator.current_device_index()).

Parameters:

-

(`init_info`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.nccl_common.trainer_init(init_info))

) –[NCCLRendezvous](https://docs.vllm.ai#vllm.distributed.weight_transfer.nccl_common.NCCLRendezvous)|[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)Any object carrying the

`NCCLRendezvous`

fields (a trainer or worker NCCL init info), or a dict with keys: - master_address: str - master_port: int - world_size: int

Returns:

-

–[PyNcclCommunicator](https://docs.vllm.ai/device_communicators/pynccl/#vllm.distributed.device_communicators.pynccl.PyNcclCommunicator)PyNcclCommunicator for weight transfer.


## Source code in `vllm/distributed/weight_transfer/nccl_common.py`


##

`uid_init_process_group(nccl_unique_id_bytes, rank, world_size, device)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.nccl_common.uid_init_process_group)

Join the NCCL group from pre-shared `ncclUniqueId`

bytes.

The torch-free rendezvous alternative to `stateless_init_process_group`

: no TCPStore, and therefore no barrier -- every rank must enter concurrently.

## Source code in `vllm/distributed/weight_transfer/nccl_common.py`


##

`worker_init_payload(init_info)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.nccl_common.worker_init_payload)

Serialize a worker init info for `init_weight_transfer_engine`

, dropping the unset rendezvous field (the UID in TCP mode) so the wire payload carries only the mode actually in use. Shared by the dense and sparse trainer engines so the two cannot drift.

## Source code in `vllm/distributed/weight_transfer/nccl_common.py`


##

`worker_init_process_group(init_info, parallel_config)`

[¶](https://docs.vllm.ai#vllm.distributed.weight_transfer.nccl_common.worker_init_process_group)

Create the trainer<->worker NCCL group on an inference worker.

Computes a unique rank for this worker across all data-parallel groups and joins the trainer via whichever rendezvous mode `init_info`

carries.