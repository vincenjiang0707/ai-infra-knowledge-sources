source: https://docs.vllm.ai/en/latest/api/vllm/distributed/eplb/rebalance_execute/
lastmod: 2026-09-23

#

`vllm.distributed.eplb.rebalance_execute`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute)

The actual execution of the rearrangement.

This involves the exchange of expert weights between GPUs.

Classes:

-
–[TransferMetadata](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.TransferMetadata)Metadata describing a completed EPLB buffer transfer.


Functions:

-
–[move_from_buffer](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.move_from_buffer)Copies expert weights from communication buffers back to the target weight

-
–[transfer_layer](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.transfer_layer)Rearranges the expert weights in place according to the new expert indices.


##

`AsyncEplbLayerResult`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.AsyncEplbLayerResult)

The result of one completed async EPLB layer transfer.

Attributes:

-
([consumed_event](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.AsyncEplbLayerResult.consumed_event)

) –[CpuGpuEvent](https://docs.vllm.ai/eplb_utils/#vllm.distributed.eplb.eplb_utils.CpuGpuEvent)Event used to synchronize access to the intermediate buffer. The async worker calls

-
([layer_idx](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.AsyncEplbLayerResult.layer_idx)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Index of the MoE layer that was transferred.

-
([new_physical_to_logical_map](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.AsyncEplbLayerResult.new_physical_to_logical_map)

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)New physical→logical mapping for layers_idx, on CPU.

-
([transfer_metadata](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.AsyncEplbLayerResult.transfer_metadata)

) –[TransferMetadata](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.TransferMetadata)Metadata describing what was received during transfer_layer.


## Source code in `vllm/distributed/eplb/rebalance_execute.py`


###

`consumed_event`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.AsyncEplbLayerResult.consumed_event)

Event used to synchronize access to the intermediate buffer. The async worker calls wait() after it finishes transferring weights to the intermediate buffer. The main thread calls record() after it finishes transferring weights out of the intermediate buffer in _move_to_workspace()

###

`layer_idx`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.AsyncEplbLayerResult.layer_idx)

Index of the MoE layer that was transferred.

###

`new_physical_to_logical_map`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.AsyncEplbLayerResult.new_physical_to_logical_map)

New physical→logical mapping for layers_idx, on CPU. Shape: (num_physical_experts)

###

`transfer_metadata`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.AsyncEplbLayerResult.transfer_metadata)

Metadata describing what was received during transfer_layer.

##

`TransferMetadata`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.TransferMetadata)

Metadata describing a completed EPLB buffer transfer.

Attributes:

-
([is_received_locally](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.TransferMetadata.is_received_locally)

) –[ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray)Mask of (num_local_experts,) indicating experts received from local data.

-
([is_unchanged](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.TransferMetadata.is_unchanged)

) –[ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray)Mask of (num_local_experts,) indicating experts unchanged after rebalance.

-
([recv_count](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.TransferMetadata.recv_count)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of received experts for the layer.

-
([recv_dst_rows](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.TransferMetadata.recv_dst_rows)

) –[ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray)Target expert indices (num_local_experts,) in local tensors to send.

-
([recv_expert_ids](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.TransferMetadata.recv_expert_ids)

) –[ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray)Expert ids (num_local_experts,) of remote primary experts.

-
([recv_primary_mask](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.TransferMetadata.recv_primary_mask)

) –[ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray)Mask of (num_local_experts,) indicating primary experts received.


## Source code in `vllm/distributed/eplb/rebalance_execute.py`


###

`is_received_locally`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.TransferMetadata.is_received_locally)

Mask of (num_local_experts,) indicating experts received from local data.

###

`is_unchanged`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.TransferMetadata.is_unchanged)

Mask of (num_local_experts,) indicating experts unchanged after rebalance.

###

`recv_count`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.TransferMetadata.recv_count)

Number of received experts for the layer.

###

`recv_dst_rows`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.TransferMetadata.recv_dst_rows)

Target expert indices (num_local_experts,) in local tensors to send.

###

`recv_expert_ids`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.TransferMetadata.recv_expert_ids)

Expert ids (num_local_experts,) of remote primary experts.

###

`recv_primary_mask`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.TransferMetadata.recv_primary_mask)

Mask of (num_local_experts,) indicating primary experts received.

##

`_map_old_expert_indices_with_rank_mapping(old_global_expert_indices, rank_mapping, new_ep_size)`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute._map_old_expert_indices_with_rank_mapping)

Map the old global expert indices to the new global expert indices.

Parameters:

-

(`old_global_expert_indices`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute._map_old_expert_indices_with_rank_mapping(old_global_expert_indices))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Shape (num_layers, old_ep_size * num_local_physical_experts).

-

(`rank_mapping`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute._map_old_expert_indices_with_rank_mapping(rank_mapping))

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[int](https://docs.python.org/3/builtins/functions.html#int),[int](https://docs.python.org/3/builtins/functions.html#int)]Mapping from old rank to new rank.

-

(`new_ep_size`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute._map_old_expert_indices_with_rank_mapping(new_ep_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)New expert parallelism size.


Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Mapped expert indices with shape

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)(num_layers, new_ep_size * num_local_physical_experts).


## Source code in `vllm/distributed/eplb/rebalance_execute.py`


##

`get_ep_ranks_with_experts_batch(expert_ids, num_local_experts, old_indices, new_indices)`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.get_ep_ranks_with_experts_batch)

Get the ranks of the experts that need to be exchanged.

Parameters:

-

(`expert_ids`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.get_ep_ranks_with_experts_batch(expert_ids))

) –[ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray)1D array of expert indices to query.

-

(`num_local_experts`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.get_ep_ranks_with_experts_batch(num_local_experts))

) –[int](https://docs.python.org/3/builtins/functions.html#int)The number of local experts.

-

(`old_indices`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.get_ep_ranks_with_experts_batch(old_indices))

) –[ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray)The old indices of the experts.

-

(`new_indices`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.get_ep_ranks_with_experts_batch(new_indices))

) –[ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray)The new indices of the experts.


Returns:

-

–[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[int](https://docs.python.org/3/builtins/functions.html#int),[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]]A tuple of two dictionaries mapping expert_id to:

-

–[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[int](https://docs.python.org/3/builtins/functions.html#int),[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]]- ranks_to_send: The ranks that have this expert and need to send.

-

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[int](https://docs.python.org/3/builtins/functions.html#int),[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]],[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[int](https://docs.python.org/3/builtins/functions.html#int),[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]]]- ranks_to_recv: The ranks that need to receive this expert.


## Source code in `vllm/distributed/eplb/rebalance_execute.py`


|
|

##

`move_from_buffer(expert_weights, expert_weights_buffers, transfer_metadata, new_indices, ep_rank)`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.move_from_buffer)

Copies expert weights from communication buffers back to the target weight tensors after EPLB rebalancing.

Parameters:

-

(`expert_weights`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.move_from_buffer(expert_weights))

) –[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]List of the actual MoE layer weights used in the execution.

-

(`expert_weights_buffers`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.move_from_buffer(expert_weights_buffers))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]Intermediate buffers containing the experts weights after the transfer is completed.

-

(`transfer_metadata`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.move_from_buffer(transfer_metadata))

) –[TransferMetadata](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.TransferMetadata)TransferMetadata containing transfer metadata.

-

(`new_indices`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.move_from_buffer(new_indices))

) –[ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray)(num_experts_total,) mapping from local rows to desired (possibly global) expert id, after rebalance.

-

(`ep_rank`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.move_from_buffer(ep_rank))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Rank of the process in the expert parallel group.


## Source code in `vllm/distributed/eplb/rebalance_execute.py`


##

`move_to_buffer(num_local_experts, old_indices, new_indices, expert_weights, expert_weights_buffers, stream, ep_rank, communicator, layer_idx=0)`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.move_to_buffer)

Rearranges expert weights during EPLB rebalancing.

Parameters:

-

(`num_local_experts`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.move_to_buffer(num_local_experts))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of local experts.

-

(`old_indices`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.move_to_buffer(old_indices))

) –[ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray)(num_experts_total,) ndarray of current (old) global-to-locals expert assignments.

-

(`new_indices`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.move_to_buffer(new_indices))

) –[ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray)(num_experts_total,) ndarray of desired (new) global-to-local assignments after rebalance.

-

(`expert_weights`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.move_to_buffer(expert_weights))

) –[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]Original expert weights for the layer.

-

(`expert_weights_buffers`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.move_to_buffer(expert_weights_buffers))

) –[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]Intermediate buffers (one per tensor).

-

(`stream`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.move_to_buffer(stream))

) –[Stream](https://pytorch.org/docs/stable/generated/torch.Stream.html#torch.Stream)| NoneCUDA/XPU stream for async copies (can be None for sync mode).

-

(`ep_rank`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.move_to_buffer(ep_rank))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Rank of this process in expert parallel group.

-

(`communicator`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.move_to_buffer(communicator))

) –[EplbCommunicator](https://docs.vllm.ai/eplb_communicator/#vllm.distributed.eplb.eplb_communicator.EplbCommunicator)EplbCommunicator instance for P2P communication.

-

(`layer_idx`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.move_to_buffer(layer_idx))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`0`

) –Index of the MoE layer being transferred.


Returns:

-
(`TransferMetadata`


) –[TransferMetadata](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.TransferMetadata)Metadata needed for completing remote weight transfers.


## Source code in `vllm/distributed/eplb/rebalance_execute.py`


|
|

##

`rearrange_expert_weights_inplace(old_global_expert_indices, new_global_expert_indices, expert_weights, expert_buffer, ep_group, communicator, is_profile=False, rank_mapping=None)`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.rearrange_expert_weights_inplace)

Rearranges the expert weights in place according to the new expert indices.

The value of the indices arguments are logical indices of the experts, while keys are physical.

Parameters:

-

(`old_global_expert_indices`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.rearrange_expert_weights_inplace(old_global_expert_indices))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Shape (num_moe_layers, num_physical_experts).

-

(`new_global_expert_indices`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.rearrange_expert_weights_inplace(new_global_expert_indices))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Shape (num_moe_layers, num_physical_experts).

-

(`expert_weights`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.rearrange_expert_weights_inplace(expert_weights))

) –[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]]A sequence of shape (num_moe_layers)(weight_count) of tensors of shape (num_local_physical_experts, hidden_size_i). For example, a linear layer may have up and down projection, so weight_count = 2. Each weight's hidden size can be different.

-

(`expert_buffer`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.rearrange_expert_weights_inplace(expert_buffer))

) –[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]Pre-allocated receive buffer tensors (one per weight tensor in a single layer).

-

(`ep_group`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.rearrange_expert_weights_inplace(ep_group))`ProcessGroup`

) –The device process group for expert parallelism.

-

(`communicator`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.rearrange_expert_weights_inplace(communicator))

) –[EplbCommunicator](https://docs.vllm.ai/eplb_communicator/#vllm.distributed.eplb.eplb_communicator.EplbCommunicator)EplbCommunicator instance for P2P communication.

-

(`is_profile`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.rearrange_expert_weights_inplace(is_profile))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –If

`True`

, do not perform any actual weight copy. This is used during profile run, where we only perform dummy communications to reserve enough memory for the buffers. -

(`rank_mapping`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.rearrange_expert_weights_inplace(rank_mapping))

, default:[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[int](https://docs.python.org/3/builtins/functions.html#int),[int](https://docs.python.org/3/builtins/functions.html#int)] | None`None`

) –A dictionary mapping old rank to new rank.


## Source code in `vllm/distributed/eplb/rebalance_execute.py`


|
|

##

`transfer_layer(old_layer_indices, new_layer_indices, expert_weights, expert_weights_buffer, ep_group, communicator, is_profile=False, stream=None, rank_mapping=None, layer_idx=0)`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.transfer_layer)

Rearranges the expert weights in place according to the new expert indices.

The value of the indices arguments are logical indices of the experts, while keys are physical.

Parameters:

-

(`old_layer_indices`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.transfer_layer(old_layer_indices))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Shape (num_physical_experts,).

-

(`new_layer_indices`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.transfer_layer(new_layer_indices))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Shape (num_physical_experts,).

-

(`expert_weights`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.transfer_layer(expert_weights))

) –[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]Iterable of weight tensors for this layer, each with shape (num_local_physical_experts, hidden_size_i). For example, a linear layer may have up and down projection.

-

(`expert_weights_buffer`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.transfer_layer(expert_weights_buffer))

) –[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]Intermediate buffers (one per weight tensor).

-

(`ep_group`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.transfer_layer(ep_group))`ProcessGroup`

) –The device process group for expert parallelism.

-

(`communicator`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.transfer_layer(communicator))

) –[EplbCommunicator](https://docs.vllm.ai/eplb_communicator/#vllm.distributed.eplb.eplb_communicator.EplbCommunicator)EplbCommunicator instance for P2P communication.

-

(`is_profile`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.transfer_layer(is_profile))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –If

`True`

, do not perform any actual weight copy. This is used during profile run, where we only perform dummy communications to reserve enough memory for the buffers. -

(`stream`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.transfer_layer(stream))

, default:[Stream](https://pytorch.org/docs/stable/generated/torch.Stream.html#torch.Stream)| None`None`

) –CUDA stream for async copies (can be None for sync mode).

-

(`rank_mapping`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.transfer_layer(rank_mapping))

, default:[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[int](https://docs.python.org/3/builtins/functions.html#int),[int](https://docs.python.org/3/builtins/functions.html#int)] | None`None`

) –Optional rank mapping for elastic expert parallelism.

-

(`layer_idx`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.transfer_layer(layer_idx))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`0`

) –Index of the MoE layer being transferred.


Returns:

-
(`TransferMetadata`


) –[TransferMetadata](https://docs.vllm.ai#vllm.distributed.eplb.rebalance_execute.TransferMetadata)Metadata needed for completing remote weight transfers, including is_unchanged and is_received_locally masks.


## Source code in `vllm/distributed/eplb/rebalance_execute.py`


|
|