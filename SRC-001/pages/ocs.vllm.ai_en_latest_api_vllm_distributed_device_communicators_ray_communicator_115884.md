source: https://docs.vllm.ai/en/latest/api/vllm/distributed/device_communicators/ray_communicator/
lastmod: 2026-09-23

#

`vllm.distributed.device_communicators.ray_communicator`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.ray_communicator)

Classes:

-
–[RayPPCommunicator](https://docs.vllm.ai#vllm.distributed.device_communicators.ray_communicator.RayPPCommunicator)Communicator to be used for pipeline parallelism in Ray Compiled Graph.


##

`RayPPCommunicator`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.ray_communicator.RayPPCommunicator)

Bases: `Communicator`


Communicator to be used for pipeline parallelism in Ray Compiled Graph. This is wraps around the vLLM _PP GroupCoordinator.

This class is not thread-safe.

Methods:

-
–[__init__](https://docs.vllm.ai#vllm.distributed.device_communicators.ray_communicator.RayPPCommunicator.__init__)Initialize a RayPPCommunicator that can be used to communicate with

-
–[get_rank](https://docs.vllm.ai#vllm.distributed.device_communicators.ray_communicator.RayPPCommunicator.get_rank)Return the given actor's rank using device communicator collective ops.

-
–[get_self_rank](https://docs.vllm.ai#vllm.distributed.device_communicators.ray_communicator.RayPPCommunicator.get_self_rank)Return this actor's rank.

-
–[get_world_size](https://docs.vllm.ai#vllm.distributed.device_communicators.ray_communicator.RayPPCommunicator.get_world_size)Return the number of ranks in the RayPPCommunicator group.

-
–[recv](https://docs.vllm.ai#vllm.distributed.device_communicators.ray_communicator.RayPPCommunicator.recv)Receive a torch.Tensor from a peer and synchronize the current stream.

-
–[send](https://docs.vllm.ai#vllm.distributed.device_communicators.ray_communicator.RayPPCommunicator.send)Send a torch.Tensor to a peer.


## Source code in `vllm/distributed/device_communicators/ray_communicator.py`


|
|

###

`__init__(world_size, comm_id, rank, actor_handles, cuda_stream, use_communication_streams=False)`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.ray_communicator.RayPPCommunicator.__init__)

Initialize a RayPPCommunicator that can be used to communicate with other Ray Compiled Graph actors for pipeline parallelism.

Parameters:

-

(`world_size`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.ray_communicator.RayPPCommunicator.__init__(world_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)The number of participating actors.

-

(`comm_id`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.ray_communicator.RayPPCommunicator.__init__(comm_id))

) –[Any](https://docs.python.org/3/library/typing.html#typing.Any)A unique communicator ID. This is just to conform with the Ray Communicator API and is not used.

-

(`rank`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.ray_communicator.RayPPCommunicator.__init__(rank))

) –[int](https://docs.python.org/3/builtins/functions.html#int)| NoneThe rank of this actor. If None, then the caller is not a participant of the RayPPCommunicator group (e.g., the Ray driver).

-

(`actor_handles`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.ray_communicator.RayPPCommunicator.__init__(actor_handles))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[ActorHandle]A list of actor handles.

-

(`cuda_stream`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.ray_communicator.RayPPCommunicator.__init__(cuda_stream))

) –[Stream](https://pytorch.org/docs/stable/generated/torch.cuda.Stream_class.html#torch.cuda.Stream)| NoneA CUDA stream to dispatch communication ops to. This is not supported.

-

(`use_communication_streams`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.ray_communicator.RayPPCommunicator.__init__(use_communication_streams))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –Whether to use communication streams. This is not supported.


## Source code in `vllm/distributed/device_communicators/ray_communicator.py`


###

`_build_actor_rank_mapping()`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.ray_communicator.RayPPCommunicator._build_actor_rank_mapping)

Use collective communication to build a mapping from actor IDs to ranks. This should be called once during initialization.

## Source code in `vllm/distributed/device_communicators/ray_communicator.py`


###

`get_rank(actor)`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.ray_communicator.RayPPCommunicator.get_rank)

Return the given actor's rank using device communicator collective ops.

## Source code in `vllm/distributed/device_communicators/ray_communicator.py`


###

`get_self_rank()`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.ray_communicator.RayPPCommunicator.get_self_rank)

###

`get_world_size()`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.ray_communicator.RayPPCommunicator.get_world_size)

###

`recv(shape, dtype, peer_rank, allocator)`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.ray_communicator.RayPPCommunicator.recv)

Receive a torch.Tensor from a peer and synchronize the current stream.

After this call returns, the receive buffer is safe to read from any stream. An RayChannelError will be raised if an error occurred (e.g., remote actor died), and the buffer is not safe to read.

Parameters:

-

(`shape`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.ray_communicator.RayPPCommunicator.recv(shape))

) –[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[int](https://docs.python.org/3/builtins/functions.html#int), ...]The shape of the tensor to receive.

-

(`dtype`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.ray_communicator.RayPPCommunicator.recv(dtype))

) –[dtype](https://pytorch.org/docs/stable/tensor_attributes.html#torch.dtype)The dtype of the tensor to receive.

-

(`peer_rank`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.ray_communicator.RayPPCommunicator.recv(peer_rank))

) –[int](https://docs.python.org/3/builtins/functions.html#int)The rank of the actor to receive from.

-

(`allocator`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.ray_communicator.RayPPCommunicator.recv(allocator))`TorchTensorAllocator`

) –The allocator to use to create the received tensor. This is ignored for this implementation.


## Source code in `vllm/distributed/device_communicators/ray_communicator.py`


###

`send(buf, peer_rank)`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.ray_communicator.RayPPCommunicator.send)

Send a torch.Tensor to a peer.

This returns when the send kernel has been queued, but the kernel may not have completed. Therefore, the caller should ensure that there are no concurrent writes to the sent `buf`

until the send has finished. That is, either all writes should be submitted on the current stream (self._cuda_stream) or, if on a different stream, that stream should synchronize with the current stream.

Parameters:

-

(`buf`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.ray_communicator.RayPPCommunicator.send(buf))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)The torch.Tensor to send. It should already be on this actor's default device.

-

(`peer_rank`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.ray_communicator.RayPPCommunicator.send(peer_rank))

) –[int](https://docs.python.org/3/builtins/functions.html#int)The rank of the actor to send to.