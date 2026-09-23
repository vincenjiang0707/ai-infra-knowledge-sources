source: https://docs.vllm.ai/en/latest/api/vllm/distributed/eplb/eplb_communicator/
lastmod: 2026-09-23

#

`vllm.distributed.eplb.eplb_communicator`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_communicator)

EPLB communicator implementations and factory.

Classes:

-
–[EplbCommunicator](https://docs.vllm.ai#vllm.distributed.eplb.eplb_communicator.EplbCommunicator)Abstract EPLB communicator for expert weight transfers.

-
–[NixlEplbCommunicator](https://docs.vllm.ai#vllm.distributed.eplb.eplb_communicator.NixlEplbCommunicator)EPLB communicator backed by NIXL READ transfers.

-
–[PyNcclEplbCommunicator](https://docs.vllm.ai#vllm.distributed.eplb.eplb_communicator.PyNcclEplbCommunicator)EPLB communicator backed by PyNcclCommunicator using ncclSend/ncclRecv.

-
–[TorchDistGlooStagedEplbCommunicator](https://docs.vllm.ai#vllm.distributed.eplb.eplb_communicator.TorchDistGlooStagedEplbCommunicator)EPLB communicator using gloo P2P with CPU staging.

-
–[TorchDistNcclEplbCommunicator](https://docs.vllm.ai#vllm.distributed.eplb.eplb_communicator.TorchDistNcclEplbCommunicator)EPLB communicator backed by torch.distributed isend/irecv.

-
–[TorchDistXCCLStagedEplbCommunicator](https://docs.vllm.ai#vllm.distributed.eplb.eplb_communicator.TorchDistXCCLStagedEplbCommunicator)EPLB communicator using XCCL device-to-device P2P on XPU.


Functions:

-
–[create_eplb_communicator](https://docs.vllm.ai#vllm.distributed.eplb.eplb_communicator.create_eplb_communicator)Create an EPLB communicator for the given backend.

-
–[has_nixl](https://docs.vllm.ai#vllm.distributed.eplb.eplb_communicator.has_nixl)Whether the optional NIXL package is available.


##

`EplbCommunicator`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_communicator.EplbCommunicator)

Bases: [ABC](https://docs.python.org/3/library/abc.html#abc.ABC)

Abstract EPLB communicator for expert weight transfers.

Methods:

-
–[execute](https://docs.vllm.ai#vllm.distributed.eplb.eplb_communicator.EplbCommunicator.execute)Complete all enqueued transfers.

-
–[set_transfer_context](https://docs.vllm.ai#vllm.distributed.eplb.eplb_communicator.EplbCommunicator.set_transfer_context)Pre-set layer context before add_recv calls.


Attributes:

-
([needs_profile_buffer_reservation](https://docs.vllm.ai#vllm.distributed.eplb.eplb_communicator.EplbCommunicator.needs_profile_buffer_reservation)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether the profile path must run a dummy collective operation to reserve


## Source code in `vllm/distributed/eplb/eplb_communicator.py`


###

`needs_profile_buffer_reservation`

`property`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_communicator.EplbCommunicator.needs_profile_buffer_reservation)

Whether the profile path must run a dummy collective operation to reserve communication buffers.

###

`execute()`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_communicator.EplbCommunicator.execute)

Complete all enqueued transfers.

Some backends perform communication here; others (e.g. NIXL) issue transfers eagerly in add_recv and only wait here. On return, all data is available in the destination buffers.

## Source code in `vllm/distributed/eplb/eplb_communicator.py`


###

`set_transfer_context(old_indices, layer_idx)`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_communicator.EplbCommunicator.set_transfer_context)

Pre-set layer context before add_recv calls.

Default is a no-op; overridden by backends (e.g. NIXL) that need layer-level context to issue transfers inside add_recv.

## Source code in `vllm/distributed/eplb/eplb_communicator.py`


##

`NixlEplbCommunicator`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_communicator.NixlEplbCommunicator)

Bases: [EplbCommunicator](https://docs.vllm.ai#vllm.distributed.eplb.eplb_communicator.EplbCommunicator)

EPLB communicator backed by NIXL READ transfers.

Methods:

-
–[__init__](https://docs.vllm.ai#vllm.distributed.eplb.eplb_communicator.NixlEplbCommunicator.__init__)Create a NIXL-backed EPLB communicator.


## Source code in `vllm/distributed/eplb/eplb_communicator.py`


|
|

###

`__init__(cpu_group, all_expert_weights, expert_buffer)`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_communicator.NixlEplbCommunicator.__init__)

Create a NIXL-backed EPLB communicator.

Parameters:

-

(`cpu_group`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_communicator.NixlEplbCommunicator.__init__(cpu_group))`ProcessGroup`

) –CPU process group for metadata exchange.

-

(`all_expert_weights`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_communicator.NixlEplbCommunicator.__init__(all_expert_weights))

) –[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]]Expert weight tensors for all MoE layers.

-

(`expert_buffer`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_communicator.NixlEplbCommunicator.__init__(expert_buffer))

) –[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]Pre-allocated receive buffer tensors.


## Source code in `vllm/distributed/eplb/eplb_communicator.py`


###

`_create_peer_xfer(src, local_descs, remote_descs)`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_communicator.NixlEplbCommunicator._create_peer_xfer)

Create a batched xfer for multiple descriptors from one peer.

Each element in *local_descs* / *remote_descs* is an `(address, size, device_id)`

tuple.

Returns `(local_dlist, remote_dlist, xfer_handle)`

.

## Source code in `vllm/distributed/eplb/eplb_communicator.py`


###

`_exchange_remote_send_meta()`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_communicator.NixlEplbCommunicator._exchange_remote_send_meta)

Exchange per-layer per-tensor metadata so receivers can compute remote RDMA addresses at transfer time.

## Source code in `vllm/distributed/eplb/eplb_communicator.py`


###

`_init_remote_state()`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_communicator.NixlEplbCommunicator._init_remote_state)

Exchange NIXL agent metadata and RDMA pointer info with all peers.

This is a collective operation (uses `all_gather_object`

twice).

## Source code in `vllm/distributed/eplb/eplb_communicator.py`


###

`_make_agent_name()`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_communicator.NixlEplbCommunicator._make_agent_name)

Build a deployment-unique nixl agent name.

## Source code in `vllm/distributed/eplb/eplb_communicator.py`


###

`_post_read_barrier()`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_communicator.NixlEplbCommunicator._post_read_barrier)

Correctness fence: prevents overwrite-while-remote-read race.

We avoid `torch.distributed.monitored_barrier`

because it calls `get_backend(group)`

which fails for stateless groups (elastic EP). An async `all_reduce`

+ `wait(timeout)`

works with both regular and stateless groups and provides equivalent timeout detection.

## Source code in `vllm/distributed/eplb/eplb_communicator.py`


##

`PyNcclEplbCommunicator`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_communicator.PyNcclEplbCommunicator)

Bases: [EplbCommunicator](https://docs.vllm.ai#vllm.distributed.eplb.eplb_communicator.EplbCommunicator)

EPLB communicator backed by PyNcclCommunicator using ncclSend/ncclRecv.

## Source code in `vllm/distributed/eplb/eplb_communicator.py`


##

`TorchDistGlooStagedEplbCommunicator`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_communicator.TorchDistGlooStagedEplbCommunicator)

Bases: [EplbCommunicator](https://docs.vllm.ai#vllm.distributed.eplb.eplb_communicator.EplbCommunicator)

EPLB communicator using gloo P2P with CPU staging.

## Source code in `vllm/distributed/eplb/eplb_communicator.py`


|
|

##

`TorchDistNcclEplbCommunicator`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_communicator.TorchDistNcclEplbCommunicator)

Bases: [EplbCommunicator](https://docs.vllm.ai#vllm.distributed.eplb.eplb_communicator.EplbCommunicator)

EPLB communicator backed by torch.distributed isend/irecv.

## Source code in `vllm/distributed/eplb/eplb_communicator.py`


##

`TorchDistXCCLStagedEplbCommunicator`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_communicator.TorchDistXCCLStagedEplbCommunicator)

Bases: [EplbCommunicator](https://docs.vllm.ai#vllm.distributed.eplb.eplb_communicator.EplbCommunicator)

EPLB communicator using XCCL device-to-device P2P on XPU.

## Source code in `vllm/distributed/eplb/eplb_communicator.py`


##

`create_eplb_communicator(group_coordinator, backend, expert_weights, expert_buffer)`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_communicator.create_eplb_communicator)

Create an EPLB communicator for the given backend.

Parameters:

-

(`group_coordinator`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_communicator.create_eplb_communicator(group_coordinator))

) –[GroupCoordinator](https://docs.vllm.ai/parallel_state/#vllm.distributed.parallel_state.GroupCoordinator)Process-group coordinator that provides the device and CPU communication groups.

-

(`backend`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_communicator.create_eplb_communicator(backend))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Communicator backend name (

`"torch_nccl"`

,`"torch_gloo"`

,`"pynccl"`

, or`"nixl"`

). Falls back to`"torch_nccl"`

when*None*. Stateless (elastic EP) groups support`"torch_nccl"`

,`"pynccl"`

, and`"nixl"`

;`"torch_nccl"`

is silently promoted to`"pynccl"`

. When tensors reside on CPU,`"torch_gloo"`

or`"torch_nccl"`

are used via the CPU process group. -

(`expert_weights`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_communicator.create_eplb_communicator(expert_weights))

) –[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]]Expert weight tensors for

*all*MoE layers. Shape`(num_layers)(num_tensors_per_layer)`

. NixlEplbCommunicator registers all layers with NIXL for zero-copy RDMA reads. -

(`expert_buffer`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_communicator.create_eplb_communicator(expert_buffer))

) –[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]Pre-allocated receive buffer tensors (one per weight tensor in a single layer).


## Source code in `vllm/distributed/eplb/eplb_communicator.py`


|
|