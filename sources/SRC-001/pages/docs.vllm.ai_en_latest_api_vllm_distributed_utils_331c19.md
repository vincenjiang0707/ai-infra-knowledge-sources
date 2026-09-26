source: https://docs.vllm.ai/en/latest/api/vllm/distributed/utils/
lastmod: 2026-09-24

#

`vllm.distributed.utils`

[¶](https://docs.vllm.ai#vllm.distributed.utils)

Classes:

-
–[StatelessProcessGroup](https://docs.vllm.ai#vllm.distributed.utils.StatelessProcessGroup)A dataclass to hold a metadata store, and the rank, world_size of the


Functions:

-
–[create_tcp_store](https://docs.vllm.ai#vllm.distributed.utils.create_tcp_store)Create a TCPStore, optionally taking ownership of

`listen_socket`

. -
–[divide](https://docs.vllm.ai#vllm.distributed.utils.divide)Ensure that numerator is divisible by the denominator and return

-
–[ensure_divisibility](https://docs.vllm.ai#vllm.distributed.utils.ensure_divisibility)Ensure that numerator is divisible by the denominator.

-
–[get_cached_tcp_store_client](https://docs.vllm.ai#vllm.distributed.utils.get_cached_tcp_store_client)Return a cached TCPStore client.

-
–[get_pp_indices](https://docs.vllm.ai#vllm.distributed.utils.get_pp_indices)Try to evenly distribute layers across partitions.

-
–[get_worker_rank_suffix](https://docs.vllm.ai#vllm.distributed.utils.get_worker_rank_suffix)Generate a descriptive rank suffix for worker identification.

-
–[init_gloo_process_group](https://docs.vllm.ai#vllm.distributed.utils.init_gloo_process_group)Stateless init ProcessGroup with gloo backend compatible with

-
–[is_weak_contiguous](https://docs.vllm.ai#vllm.distributed.utils.is_weak_contiguous)Check that

*inp*occupies a single contiguous block of memory. -
–[split_tensor_along_last_dim](https://docs.vllm.ai#vllm.distributed.utils.split_tensor_along_last_dim)Split a tensor along its last dimension.

-
–[stateless_destroy_torch_distributed_process_group](https://docs.vllm.ai#vllm.distributed.utils.stateless_destroy_torch_distributed_process_group)Destroy ProcessGroup returned by

-
–[stateless_init_torch_distributed_process_group](https://docs.vllm.ai#vllm.distributed.utils.stateless_init_torch_distributed_process_group)A replacement for

`torch.distributed.init_process_group`

that does not -
–[verify_group_size_divides_partition](https://docs.vllm.ai#vllm.distributed.utils.verify_group_size_divides_partition)Validate that a TP-sharded layer holds a whole number of quant groups.


##

`StatelessProcessGroup`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.utils.StatelessProcessGroup)

A dataclass to hold a metadata store, and the rank, world_size of the group. Only use it to communicate metadata between processes. For data-plane communication, create NCCL-related objects.

Methods:

-
–[all_gather_obj](https://docs.vllm.ai#vllm.distributed.utils.StatelessProcessGroup.all_gather_obj)All gather an object from all ranks.

-
–[all_reduce](https://docs.vllm.ai#vllm.distributed.utils.StatelessProcessGroup.all_reduce)All-reduce a tensor across all ranks.

-
–[barrier](https://docs.vllm.ai#vllm.distributed.utils.StatelessProcessGroup.barrier)A robust barrier to synchronize all ranks.

-
–[broadcast](https://docs.vllm.ai#vllm.distributed.utils.StatelessProcessGroup.broadcast)Broadcast a tensor from source rank to all other ranks.

-
–[broadcast_obj](https://docs.vllm.ai#vllm.distributed.utils.StatelessProcessGroup.broadcast_obj)Broadcast an object from a source rank to all other ranks.

-
–[create](https://docs.vllm.ai#vllm.distributed.utils.StatelessProcessGroup.create)A replacement for

`torch.distributed.init_process_group`

that does not -
–[expire_data](https://docs.vllm.ai#vllm.distributed.utils.StatelessProcessGroup.expire_data)Expire data that is older than

`data_expiration_seconds`

seconds. -
–[recv](https://docs.vllm.ai#vllm.distributed.utils.StatelessProcessGroup.recv)Receive a tensor from a source rank.

-
–[recv_obj](https://docs.vllm.ai#vllm.distributed.utils.StatelessProcessGroup.recv_obj)Receive an object from a source rank.

-
–[send](https://docs.vllm.ai#vllm.distributed.utils.StatelessProcessGroup.send)Send a tensor to a destination rank.

-
–[send_obj](https://docs.vllm.ai#vllm.distributed.utils.StatelessProcessGroup.send_obj)Send an object to a destination rank.


## Source code in `vllm/distributed/utils.py`


|
|

###

`all_gather_obj(obj)`

[¶](https://docs.vllm.ai#vllm.distributed.utils.StatelessProcessGroup.all_gather_obj)

All gather an object from all ranks.

## Source code in `vllm/distributed/utils.py`


###

`all_reduce(tensor, op=torch.distributed.ReduceOp.SUM)`

[¶](https://docs.vllm.ai#vllm.distributed.utils.StatelessProcessGroup.all_reduce)

All-reduce a tensor across all ranks.

## Source code in `vllm/distributed/utils.py`


###

`barrier(timeout=30.0)`

[¶](https://docs.vllm.ai#vllm.distributed.utils.StatelessProcessGroup.barrier)

A robust barrier to synchronize all ranks.

Uses a multi-phase approach to ensure all processes reach the barrier before proceeding:

-
Each process signals it has reached the barrier

-
Each process signals that it has confirmed the arrival of all other ranks.

-
Rank 0 waits for all other ranks to signal their departure to ensure that all ranks have departed the barrier first.


Parameters:

Raises:

-

–[RuntimeError](https://docs.python.org/3/builtins/exceptions.html#RuntimeError)If coordination fails or times out


## Source code in `vllm/distributed/utils.py`


|
|

###

`broadcast(tensor, src)`

[¶](https://docs.vllm.ai#vllm.distributed.utils.StatelessProcessGroup.broadcast)

Broadcast a tensor from source rank to all other ranks.

## Source code in `vllm/distributed/utils.py`


###

`broadcast_obj(obj, src)`

[¶](https://docs.vllm.ai#vllm.distributed.utils.StatelessProcessGroup.broadcast_obj)

Broadcast an object from a source rank to all other ranks. It does not clean up after all ranks have received the object. Use it for limited times, e.g., for initialization.

## Source code in `vllm/distributed/utils.py`


###

`create(host, port, rank, world_size, data_expiration_seconds=3600, store_timeout=300, listen_socket=None)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.distributed.utils.StatelessProcessGroup.create)

A replacement for `torch.distributed.init_process_group`

that does not pollute the global state.

If we have process A and process B called `torch.distributed.init_process_group`

to form a group, and then we want to form another group with process A, B, C, D, it is not possible in PyTorch, because process A and process B have already formed a group, and process C and process D cannot join that group. This function is a workaround for this issue.

`torch.distributed.init_process_group`

is a global call, while this function is a stateless call. It will return a `StatelessProcessGroup`

object that can be used for exchanging metadata. With this function, process A and process B can call `StatelessProcessGroup.create`

to form a group, and then process A, B, C, and D can call `StatelessProcessGroup.create`

to form another group.

## Source code in `vllm/distributed/utils.py`


###

`expire_data()`

[¶](https://docs.vllm.ai#vllm.distributed.utils.StatelessProcessGroup.expire_data)

Expire data that is older than `data_expiration_seconds`

seconds.

## Source code in `vllm/distributed/utils.py`


###

`recv(tensor, src)`

[¶](https://docs.vllm.ai#vllm.distributed.utils.StatelessProcessGroup.recv)

Receive a tensor from a source rank.

## Source code in `vllm/distributed/utils.py`


###

`recv_obj(src)`

[¶](https://docs.vllm.ai#vllm.distributed.utils.StatelessProcessGroup.recv_obj)

Receive an object from a source rank.

###

`send(tensor, dst)`

[¶](https://docs.vllm.ai#vllm.distributed.utils.StatelessProcessGroup.send)

Send a tensor to a destination rank.

## Source code in `vllm/distributed/utils.py`


###

`send_obj(obj, dst)`

[¶](https://docs.vllm.ai#vllm.distributed.utils.StatelessProcessGroup.send_obj)

Send an object to a destination rank.

## Source code in `vllm/distributed/utils.py`


##

`create_tcp_store(host, port, listen_socket=None, **kwargs)`

[¶](https://docs.vllm.ai#vllm.distributed.utils.create_tcp_store)

Create a TCPStore, optionally taking ownership of `listen_socket`

.

## Source code in `vllm/distributed/utils.py`


##

`divide(numerator, denominator)`

[¶](https://docs.vllm.ai#vllm.distributed.utils.divide)

Ensure that numerator is divisible by the denominator and return the division value.

##

`ensure_divisibility(numerator, denominator)`

[¶](https://docs.vllm.ai#vllm.distributed.utils.ensure_divisibility)

Ensure that numerator is divisible by the denominator.

##

`get_cached_tcp_store_client(host, port)`

`cached`

[¶](https://docs.vllm.ai#vllm.distributed.utils.get_cached_tcp_store_client)

Return a cached TCPStore client.

Cached so that every call with the same `(host, port)`

reuses the same connection. A new `(host, port)`

evicts the old entry.

## Source code in `vllm/distributed/utils.py`


##

`get_pp_indices(num_hidden_layers, pp_rank, pp_size)`

[¶](https://docs.vllm.ai#vllm.distributed.utils.get_pp_indices)

Try to evenly distribute layers across partitions.

If the number of layers is not divisible by the number of partitions, the remaining layers are evenly distributed across all but the last partition. The last partition is excluded because it often contains an additional norm layer and we are attempting to balance compute.

If `pp_size > 2`

and the number of remaining layers is `0 < x <= pp_size - 2`

then the remaining layers are evenly distributed across the middle partitions. The first and last partitions are excluded because they contain the input and output embeddings respectively and we are attempting to reduce maximum memory consumption across partitions.

## Source code in `vllm/distributed/utils.py`


##

`get_worker_rank_suffix(global_rank=None)`

[¶](https://docs.vllm.ai#vllm.distributed.utils.get_worker_rank_suffix)

Generate a descriptive rank suffix for worker identification.

Returns a string like 'dp0_pp0_tp0_dcp0_ep0_rank0' including all parallel dimensions: DP, PP, TP, DCP, EP.

Parameters:

-

(`global_rank`

[¶](https://docs.vllm.ai#vllm.distributed.utils.get_worker_rank_suffix(global_rank))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)| None`None`

) –Optional global rank to append. If not provided, only parallel dimension ranks are included.


Returns:

## Source code in `vllm/distributed/utils.py`


##

`init_gloo_process_group(prefix_store, group_rank, group_size, timeout)`

[¶](https://docs.vllm.ai#vllm.distributed.utils.init_gloo_process_group)

Stateless init ProcessGroup with gloo backend compatible with different torch versions.

## Source code in `vllm/distributed/utils.py`


##

`is_weak_contiguous(inp)`

[¶](https://docs.vllm.ai#vllm.distributed.utils.is_weak_contiguous)

Check that *inp* occupies a single contiguous block of memory.

Unlike `torch.Tensor.is_contiguous()`

, this also accepts tensors whose strides are not strictly C-contiguous (e.g. column-major) as long as the underlying storage from the tensor's offset onward is exactly `numel * element_size`

bytes.

## Source code in `vllm/distributed/utils.py`


##

`split_tensor_along_last_dim(tensor, num_partitions, contiguous_split_chunks=False)`

[¶](https://docs.vllm.ai#vllm.distributed.utils.split_tensor_along_last_dim)

Split a tensor along its last dimension.

Parameters:

-

(`tensor`

[¶](https://docs.vllm.ai#vllm.distributed.utils.split_tensor_along_last_dim(tensor))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)input tensor.

-

(`num_partitions`

[¶](https://docs.vllm.ai#vllm.distributed.utils.split_tensor_along_last_dim(num_partitions))

) –[int](https://docs.python.org/3/builtins/functions.html#int)number of partitions to split the tensor

-

(`contiguous_split_chunks`

[¶](https://docs.vllm.ai#vllm.distributed.utils.split_tensor_along_last_dim(contiguous_split_chunks))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –If True, make each chunk contiguous in memory.


Returns:

## Source code in `vllm/distributed/utils.py`


##

`stateless_destroy_torch_distributed_process_group(pg)`

[¶](https://docs.vllm.ai#vllm.distributed.utils.stateless_destroy_torch_distributed_process_group)

Destroy ProcessGroup returned by stateless_init_torch_distributed_process_group().

##

`stateless_init_torch_distributed_process_group(host, port, rank, world_size, backend, group_name=None, return_store=False, listen_socket=None)`

[¶](https://docs.vllm.ai#vllm.distributed.utils.stateless_init_torch_distributed_process_group)

A replacement for `torch.distributed.init_process_group`

that does not pollute the global state. The created ProcessGroup object can be used for some operations such as `allreduce`

, because it does not depend on the global rank. However, some operations such as `broadcast`

cannot be used because it depends on the global rank.

### TODO: ask for help from PyTorch team if we need the `broadcast`

operation.[¶](https://docs.vllm.ai#vllm.distributed.utils.stateless_init_torch_distributed_process_group--todo-ask-for-help-from-pytorch-team-if-we-need-the-broadcast-operation)

This function is useful when we are not sure about the total number of processes in the process group. For example, we may have process 1, 2, ..., 8 who want to communicate, and process 9 might be the same process as process 1, or it might be a different process; process 10 might be the same process as process 5, or it might be a different process. In this case, how can we reliably form a communication channel within process 9 and 10, without affecting the communication channel within process 1, 2, ..., 8?

One possible solution is to figure out if process 9 and 10 are the same as process 1 and 5 beforehand, and then form a communication channel based on the information, adjusting the ranks and world_size etc. However, figuring out the information is not always easy, and it will interfere with the main communication channel.

Our solution is to always form a communication channel with process 1, 2, ..., 8, and then use this function to form another communication channel with process 9 and 10. This way, regardless of whether process 9 and 10 are the same as process 1 and 5, the main communication channel is always formed with process 1, 2, ..., 8, and the additional communication channel is formed with process 9 and 10.

When *listen_socket* is provided, the rendezvous step is skipped and a `TCPStore`

server is created directly using the pre-bound socket. This is useful for eliminating TOCTOU races between port allocation and binding.

## Source code in `vllm/distributed/utils.py`


|
|

##

`verify_group_size_divides_partition(input_size_per_partition, group_size, layer_name=None, extra_suggestion='')`

[¶](https://docs.vllm.ai#vllm.distributed.utils.verify_group_size_divides_partition)

Validate that a TP-sharded layer holds a whole number of quant groups.