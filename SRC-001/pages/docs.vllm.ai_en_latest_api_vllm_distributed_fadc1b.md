source: https://docs.vllm.ai/en/latest/api/vllm/distributed/
lastmod: 2026-09-23

#

`vllm.distributed`

[¶](https://docs.vllm.ai#vllm.distributed)

Modules:

-
–[aux_output_connector](https://docs.vllm.ai/aux_output_connector/#vllm.distributed.aux_output_connector) -
–[communication_op](https://docs.vllm.ai/communication_op/#vllm.distributed.communication_op) -
–[device_communicators](https://docs.vllm.ai/device_communicators/#vllm.distributed.device_communicators) -
–[ec_transfer](https://docs.vllm.ai/ec_transfer/#vllm.distributed.ec_transfer) -
–[elastic_ep](https://docs.vllm.ai/elastic_ep/#vllm.distributed.elastic_ep) -
–[envs](https://docs.vllm.ai/envs/#vllm.envs) -
–[eplb](https://docs.vllm.ai/eplb/#vllm.distributed.eplb)Expert parallelism load balancer (EPLB).

-
–[kv_events](https://docs.vllm.ai/kv_events/#vllm.distributed.kv_events) -
–[kv_transfer](https://docs.vllm.ai/kv_transfer/#vllm.distributed.kv_transfer) -
–[mooncake_store](https://docs.vllm.ai/mooncake_store/#vllm.distributed.mooncake_store)Shared configuration and setup for EC and KV Mooncake Store clients.

-
–[nixl_utils](https://docs.vllm.ai/nixl_utils/#vllm.distributed.nixl_utils) -
–[parallel_state](https://docs.vllm.ai/parallel_state/#vllm.distributed.parallel_state)vLLM distributed state.

-
–[stateless_coordinator](https://docs.vllm.ai/stateless_coordinator/#vllm.distributed.stateless_coordinator) -
–[utils](https://docs.vllm.ai/utils/#vllm.distributed.utils) -
–[weight_transfer](https://docs.vllm.ai/weight_transfer/#vllm.distributed.weight_transfer)Weight transfer engines for syncing model weights from trainers


Classes:

-
–[DeviceCommunicatorBase](https://docs.vllm.ai#vllm.distributed.DeviceCommunicatorBase)Base class for device-specific communicator.

-
–[GroupCoordinator](https://docs.vllm.ai#vllm.distributed.GroupCoordinator)PyTorch ProcessGroup wrapper for a group of processes.

-
–[Handle](https://docs.vllm.ai#vllm.distributed.Handle)Minimal async work handle used by P2P send/recv methods.

-
–[StatelessProcessGroup](https://docs.vllm.ai#vllm.distributed.StatelessProcessGroup)A dataclass to hold a metadata store, and the rank, world_size of the


Functions:

-
–[checkpoint_prepare_distributed_state](https://docs.vllm.ai#vllm.distributed.checkpoint_prepare_distributed_state)Prepare every device communicator for a process checkpoint.

-
–[checkpoint_restore_distributed_state](https://docs.vllm.ai#vllm.distributed.checkpoint_restore_distributed_state)Restore every device communicator after a process checkpoint.

-
–[create_tcp_store](https://docs.vllm.ai#vllm.distributed.create_tcp_store)Create a TCPStore, optionally taking ownership of

`listen_socket`

. -
–[destroy_model_parallel](https://docs.vllm.ai#vllm.distributed.destroy_model_parallel)Set the groups to none and destroy them.

-
–[direct_register_custom_op](https://docs.vllm.ai#vllm.distributed.direct_register_custom_op)`torch.library.custom_op`

can have significant overhead because it -
–[divide](https://docs.vllm.ai#vllm.distributed.divide)Ensure that numerator is divisible by the denominator and return

-
–[ensure_divisibility](https://docs.vllm.ai#vllm.distributed.ensure_divisibility)Ensure that numerator is divisible by the denominator.

-
–[ensure_model_parallel_initialized](https://docs.vllm.ai#vllm.distributed.ensure_model_parallel_initialized)Helper to initialize model parallel groups if they are not initialized,

-
–[get_cached_tcp_store_client](https://docs.vllm.ai#vllm.distributed.get_cached_tcp_store_client)Return a cached TCPStore client.

-
–[get_engram_dp_group](https://docs.vllm.ai#vllm.distributed.get_engram_dp_group)Return the DP replicas that share one engram embedding table.

-
–[get_engram_dp_size](https://docs.vllm.ai#vllm.distributed.get_engram_dp_size)Number of DP replicas one engram embedding table is sharded over.

-
–[get_etp_group](https://docs.vllm.ai#vllm.distributed.get_etp_group)Return the Engram Tensor Parallel (ETP) group that shards one embedding table.

-
–[get_node_count](https://docs.vllm.ai#vllm.distributed.get_node_count)Return the total number of nodes in the distributed environment.

-
–[get_pp_indices](https://docs.vllm.ai#vllm.distributed.get_pp_indices)Try to evenly distribute layers across partitions.

-
–[get_tensor_model_parallel_rank](https://docs.vllm.ai#vllm.distributed.get_tensor_model_parallel_rank)Return my rank for the tensor model parallel group.

-
–[get_tensor_model_parallel_world_size](https://docs.vllm.ai#vllm.distributed.get_tensor_model_parallel_world_size)Return world size for the tensor model parallel group.

-
–[get_worker_rank_suffix](https://docs.vllm.ai#vllm.distributed.get_worker_rank_suffix)Generate a descriptive rank suffix for worker identification.

-
–[graph_capture](https://docs.vllm.ai#vllm.distributed.graph_capture)`graph_capture`

is a context manager which should surround the code that -
–[in_the_same_node_as](https://docs.vllm.ai#vllm.distributed.in_the_same_node_as)This is a collective operation that returns if each rank is in the same node

-
–[init_gloo_process_group](https://docs.vllm.ai#vllm.distributed.init_gloo_process_group)Stateless init ProcessGroup with gloo backend compatible with

-
–[init_logger](https://docs.vllm.ai#vllm.distributed.init_logger)The main purpose of this function is to ensure that loggers are

-
–[initialize_model_parallel](https://docs.vllm.ai#vllm.distributed.initialize_model_parallel)Initialize model parallel groups.

-
–[is_global_first_rank](https://docs.vllm.ai#vllm.distributed.is_global_first_rank)Check if the current process is the first rank globally across all

-
–[is_local_first_rank](https://docs.vllm.ai#vllm.distributed.is_local_first_rank)Check if the current process is the first local rank (rank 0 on its node).

-
–[is_weak_contiguous](https://docs.vllm.ai#vllm.distributed.is_weak_contiguous)Check that

*inp*occupies a single contiguous block of memory. -
–[model_parallel_is_initialized](https://docs.vllm.ai#vllm.distributed.model_parallel_is_initialized)Check if tensor and pipeline parallel groups are initialized.

-
–[resolve_obj_by_qualname](https://docs.vllm.ai#vllm.distributed.resolve_obj_by_qualname)Resolve an object by its fully-qualified class name.

-
–[resume_device_comms](https://docs.vllm.ai#vllm.distributed.resume_device_comms)Restore suspended device communicators (collective).

-
–[split_tensor_along_last_dim](https://docs.vllm.ai#vllm.distributed.split_tensor_along_last_dim)Split a tensor along its last dimension.

-
–[stateless_destroy_torch_distributed_process_group](https://docs.vllm.ai#vllm.distributed.stateless_destroy_torch_distributed_process_group)Destroy ProcessGroup returned by

-
–[stateless_init_torch_distributed_process_group](https://docs.vllm.ai#vllm.distributed.stateless_init_torch_distributed_process_group)A replacement for

`torch.distributed.init_process_group`

that does not -
–[suppress_stdout](https://docs.vllm.ai#vllm.distributed.suppress_stdout)Suppress stdout from C libraries at the file descriptor level.

-
–[suspend_device_comms](https://docs.vllm.ai#vllm.distributed.suspend_device_comms)Release device communicator memory (collective; comms must be idle).

-
–[tensor_model_parallel_all_gather](https://docs.vllm.ai#vllm.distributed.tensor_model_parallel_all_gather)All-gather the input tensor across model parallel group.

-
–[tensor_model_parallel_all_reduce](https://docs.vllm.ai#vllm.distributed.tensor_model_parallel_all_reduce)All-reduce the input tensor across model parallel group.

-
–[tensor_model_parallel_gather](https://docs.vllm.ai#vllm.distributed.tensor_model_parallel_gather)Gather the input tensor across model parallel group.

-
–[tensor_model_parallel_reduce_scatter](https://docs.vllm.ai#vllm.distributed.tensor_model_parallel_reduce_scatter)Reduce-Scatter the input tensor across model parallel group.

-
–[verify_group_size_divides_partition](https://docs.vllm.ai#vllm.distributed.verify_group_size_divides_partition)Validate that a TP-sharded layer holds a whole number of quant groups.


##

`DeviceCommunicatorBase`

[¶](https://docs.vllm.ai#vllm.distributed.DeviceCommunicatorBase)

Base class for device-specific communicator. It can use the `cpu_group`

to initialize the communicator. If the device has PyTorch integration (PyTorch can recognize its communication backend), the `device_group`

will also be given.

Methods:

-
–[broadcast](https://docs.vllm.ai#vllm.distributed.DeviceCommunicatorBase.broadcast)Broadcast a tensor from source rank to all ranks.

-
–[checkpoint_prepare](https://docs.vllm.ai#vllm.distributed.DeviceCommunicatorBase.checkpoint_prepare)Prepare reclaimable communicator state for checkpoint (default: no-op).

-
–[checkpoint_restore](https://docs.vllm.ai#vllm.distributed.DeviceCommunicatorBase.checkpoint_restore)Restore communicator state after checkpoint (default: no-op).

-
–[combine](https://docs.vllm.ai#vllm.distributed.DeviceCommunicatorBase.combine)Combine the hidden states and router logits from the appropriate device.

-
–[dispatch](https://docs.vllm.ai#vllm.distributed.DeviceCommunicatorBase.dispatch)Dispatch the hidden states and topk weights/ids to the appropriate device.

-
–[dispatch_router_logits](https://docs.vllm.ai#vllm.distributed.DeviceCommunicatorBase.dispatch_router_logits)Dispatch the hidden states and router logits to the appropriate device.

-
–[gather](https://docs.vllm.ai#vllm.distributed.DeviceCommunicatorBase.gather)NOTE: We assume that the input tensor is on the same device across

-
–[recv](https://docs.vllm.ai#vllm.distributed.DeviceCommunicatorBase.recv)Receives a tensor from the source rank.

-
–[resume](https://docs.vllm.ai#vllm.distributed.DeviceCommunicatorBase.resume)Restore memory released by

`suspend`

(default: no-op). -
–[send](https://docs.vllm.ai#vllm.distributed.DeviceCommunicatorBase.send)Sends a tensor to the destination rank in a blocking way.

-
–[suspend](https://docs.vllm.ai#vllm.distributed.DeviceCommunicatorBase.suspend)Release reclaimable communicator memory (default: no-op).


## Source code in `vllm/distributed/device_communicators/base_device_communicator.py`


|
|

###

`broadcast(tensor, src=0)`

[¶](https://docs.vllm.ai#vllm.distributed.DeviceCommunicatorBase.broadcast)

Broadcast a tensor from source rank to all ranks.

## Source code in `vllm/distributed/device_communicators/base_device_communicator.py`


###

`checkpoint_prepare()`

[¶](https://docs.vllm.ai#vllm.distributed.DeviceCommunicatorBase.checkpoint_prepare)

###

`checkpoint_restore()`

[¶](https://docs.vllm.ai#vllm.distributed.DeviceCommunicatorBase.checkpoint_restore)

###

`combine(hidden_states, is_sequence_parallel=False)`

[¶](https://docs.vllm.ai#vllm.distributed.DeviceCommunicatorBase.combine)

Combine the hidden states and router logits from the appropriate device. This is a no-op in the base class.

## Source code in `vllm/distributed/device_communicators/base_device_communicator.py`


###

`dispatch(hidden_states, topk_weights, topk_ids, is_sequence_parallel=False, extra_tensors=None)`

[¶](https://docs.vllm.ai#vllm.distributed.DeviceCommunicatorBase.dispatch)

Dispatch the hidden states and topk weights/ids to the appropriate device. This is a no-op in the base class.

## Source code in `vllm/distributed/device_communicators/base_device_communicator.py`


###

`dispatch_router_logits(hidden_states, router_logits, is_sequence_parallel=False, extra_tensors=None)`

[¶](https://docs.vllm.ai#vllm.distributed.DeviceCommunicatorBase.dispatch_router_logits)

Dispatch the hidden states and router logits to the appropriate device. This is a no-op in the base class.

## Source code in `vllm/distributed/device_communicators/base_device_communicator.py`


###

`gather(input_, dst=0, dim=-1)`

[¶](https://docs.vllm.ai#vllm.distributed.DeviceCommunicatorBase.gather)

NOTE: We assume that the input tensor is on the same device across all the ranks. NOTE: `dst`

is the local rank of the destination rank.

## Source code in `vllm/distributed/device_communicators/base_device_communicator.py`


###

`recv(size, dtype, src=None)`

[¶](https://docs.vllm.ai#vllm.distributed.DeviceCommunicatorBase.recv)

Receives a tensor from the source rank.

## Source code in `vllm/distributed/device_communicators/base_device_communicator.py`


###

`resume()`

[¶](https://docs.vllm.ai#vllm.distributed.DeviceCommunicatorBase.resume)

###

`send(tensor, dst=None)`

[¶](https://docs.vllm.ai#vllm.distributed.DeviceCommunicatorBase.send)

Sends a tensor to the destination rank in a blocking way.

## Source code in `vllm/distributed/device_communicators/base_device_communicator.py`


##

`GroupCoordinator`

[¶](https://docs.vllm.ai#vllm.distributed.GroupCoordinator)

PyTorch ProcessGroup wrapper for a group of processes. PyTorch ProcessGroup is bound to one specific communication backend, e.g. NCCL, Gloo, MPI, etc. GroupCoordinator takes charge of all the communication operations among the processes in the group. It manages both CPU and device communication.

Methods:

-
–[all_reduce](https://docs.vllm.ai#vllm.distributed.GroupCoordinator.all_reduce)User-facing all-reduce function before we actually call the

-
–[barrier](https://docs.vllm.ai#vllm.distributed.GroupCoordinator.barrier)Barrier synchronization among the group.

-
–[broadcast](https://docs.vllm.ai#vllm.distributed.GroupCoordinator.broadcast)Broadcast the input tensor.

-
–[broadcast_object](https://docs.vllm.ai#vllm.distributed.GroupCoordinator.broadcast_object)Broadcast the input object.

-
–[broadcast_object_list](https://docs.vllm.ai#vllm.distributed.GroupCoordinator.broadcast_object_list)Broadcast the input object list.

-
–[broadcast_tensor_dict](https://docs.vllm.ai#vllm.distributed.GroupCoordinator.broadcast_tensor_dict)Broadcast the input tensor dictionary.

-
–[gather](https://docs.vllm.ai#vllm.distributed.GroupCoordinator.gather)NOTE: We assume that the input tensor is on the same device across

-
–[isend_object](https://docs.vllm.ai#vllm.distributed.GroupCoordinator.isend_object)Non-blocking

`send_object`

: isend size + pickled object on the -
–[isend_tensor_dict](https://docs.vllm.ai#vllm.distributed.GroupCoordinator.isend_tensor_dict)Send the input tensor dictionary asynchronously.

-
–[make_sibling_device_group](https://docs.vllm.ai#vllm.distributed.GroupCoordinator.make_sibling_device_group)Create a new device-side ProcessGroup with the same per-rank membership

-
–[recv](https://docs.vllm.ai#vllm.distributed.GroupCoordinator.recv)Receives a tensor from the source rank.

-
–[recv_object](https://docs.vllm.ai#vllm.distributed.GroupCoordinator.recv_object)Receive the input object list from the source rank.

-
–[recv_tensor_dict](https://docs.vllm.ai#vllm.distributed.GroupCoordinator.recv_tensor_dict)Recv the input tensor dictionary.

-
–[send](https://docs.vllm.ai#vllm.distributed.GroupCoordinator.send)Sends a tensor to the destination rank in a blocking way.

-
–[send_object](https://docs.vllm.ai#vllm.distributed.GroupCoordinator.send_object)Send the input object list to the destination rank.

-
–[send_tensor_dict](https://docs.vllm.ai#vllm.distributed.GroupCoordinator.send_tensor_dict)Send the input tensor dictionary.


Attributes:

-
–[first_rank](https://docs.vllm.ai#vllm.distributed.GroupCoordinator.first_rank)Return the global rank of the first process in the group.

-
–[is_first_rank](https://docs.vllm.ai#vllm.distributed.GroupCoordinator.is_first_rank)Return whether the caller is the first process in the group.

-
–[is_last_rank](https://docs.vllm.ai#vllm.distributed.GroupCoordinator.is_last_rank)Return whether the caller is the last process in the group.

-
–[last_rank](https://docs.vllm.ai#vllm.distributed.GroupCoordinator.last_rank)Return the global rank of the last process in the group.

-
–[next_rank](https://docs.vllm.ai#vllm.distributed.GroupCoordinator.next_rank)Return the global rank of the process that follows the caller.

-
–[prev_rank](https://docs.vllm.ai#vllm.distributed.GroupCoordinator.prev_rank)Return the global rank of the process that precedes the caller.


## Source code in `vllm/distributed/parallel_state.py`


|
|

###

`first_rank`

`property`

[¶](https://docs.vllm.ai#vllm.distributed.GroupCoordinator.first_rank)

Return the global rank of the first process in the group.

###

`is_first_rank`

`property`

[¶](https://docs.vllm.ai#vllm.distributed.GroupCoordinator.is_first_rank)

Return whether the caller is the first process in the group.

###

`is_last_rank`

`property`

[¶](https://docs.vllm.ai#vllm.distributed.GroupCoordinator.is_last_rank)

Return whether the caller is the last process in the group.

###

`last_rank`

`property`

[¶](https://docs.vllm.ai#vllm.distributed.GroupCoordinator.last_rank)

Return the global rank of the last process in the group.

###

`next_rank`

`property`

[¶](https://docs.vllm.ai#vllm.distributed.GroupCoordinator.next_rank)

Return the global rank of the process that follows the caller.

###

`prev_rank`

`property`

[¶](https://docs.vllm.ai#vllm.distributed.GroupCoordinator.prev_rank)

Return the global rank of the process that precedes the caller.

###

`_reap_completed_isends()`

[¶](https://docs.vllm.ai#vllm.distributed.GroupCoordinator._reap_completed_isends)

Lazily drop self-retained `isend_tensor_dict`

entries that have completed, oldest first (FIFO).

gloo `Work.is_completed()`

is unreliable (it can report completion before the background copy of the source buffer finishes), so the metadata handle (`handles[0]`

, a gloo-backed `_RetainedHandle`

) is never used as the completion gate. Instead we gate on the tensor-send handles (`handles[1:]`

), which run on the device backend where `is_completed()`

is reliable. Once all tensor sends are done the peer must already have posted the matching tensor recvs — and since the receiver ingests metadata before tensors, the gloo metadata send is then guaranteed complete, so `wait()`

on it is ~instant and only serves to drop the retained refs.

Metadata-only entries (`handles[1:]`

empty, e.g. an empty `IntermediateTensors`

) have no reliable completion signal; drop them best-effort without blocking on the gloo metadata wait.

## Source code in `vllm/distributed/parallel_state.py`


###

`all_reduce(input_)`

[¶](https://docs.vllm.ai#vllm.distributed.GroupCoordinator.all_reduce)

User-facing all-reduce function before we actually call the all-reduce operation.

We need this because Dynamo does not support passing an arbitrary object (`self`

in this case) to a custom op. We need to pass the group name as a string, and then look up the group coordinator from the group name, dispatch the all-reduce operation to the group coordinator.

In addition, PyTorch custom ops do not support mutation or returning a new tensor in the same op. So we always make the all-reduce operation out-of-place.

## Source code in `vllm/distributed/parallel_state.py`


###

`barrier()`

[¶](https://docs.vllm.ai#vllm.distributed.GroupCoordinator.barrier)

Barrier synchronization among the group. NOTE: don't use `device_group`

here! `barrier`

in NCCL is terrible because it is internally a broadcast operation with secretly created GPU tensors. It is easy to mess up the current device. Use the CPU group instead.

## Source code in `vllm/distributed/parallel_state.py`


###

`broadcast(input_, src=0)`

[¶](https://docs.vllm.ai#vllm.distributed.GroupCoordinator.broadcast)

Broadcast the input tensor. NOTE: `src`

is the local rank of the source rank.

## Source code in `vllm/distributed/parallel_state.py`


###

`broadcast_object(obj=None, src=0)`

[¶](https://docs.vllm.ai#vllm.distributed.GroupCoordinator.broadcast_object)

Broadcast the input object. NOTE: `src`

is the local rank of the source rank.

## Source code in `vllm/distributed/parallel_state.py`


###

`broadcast_object_list(obj_list, src=0, group=None)`

[¶](https://docs.vllm.ai#vllm.distributed.GroupCoordinator.broadcast_object_list)

Broadcast the input object list. NOTE: `src`

is the local rank of the source rank.

## Source code in `vllm/distributed/parallel_state.py`


###

`broadcast_tensor_dict(tensor_dict=None, src=0, group=None, metadata_group=None)`

[¶](https://docs.vllm.ai#vllm.distributed.GroupCoordinator.broadcast_tensor_dict)

Broadcast the input tensor dictionary. NOTE: `src`

is the local rank of the source rank.

## Source code in `vllm/distributed/parallel_state.py`


|
|

###

`gather(input_, dst=0, dim=-1)`

[¶](https://docs.vllm.ai#vllm.distributed.GroupCoordinator.gather)

NOTE: We assume that the input tensor is on the same device across all the ranks. NOTE: `dst`

is the local rank of the destination rank.

## Source code in `vllm/distributed/parallel_state.py`


###

`isend_object(obj, dst)`

[¶](https://docs.vllm.ai#vllm.distributed.GroupCoordinator.isend_object)

Non-blocking `send_object`

: isend size + pickled object on the CPU group. Returns a handle that retains the serialized source tensors until `wait`

drains both sends.

## Source code in `vllm/distributed/parallel_state.py`


###

`isend_tensor_dict(tensor_dict, dst=None, all_gather_group=None, all_gather_tensors=None)`

[¶](https://docs.vllm.ai#vllm.distributed.GroupCoordinator.isend_tensor_dict)

Send the input tensor dictionary asynchronously.

The returned handles are additionally self-retained in `self._pending_isends`

(together with the sent source tensors) and reaped lazily on subsequent calls, so fire-and-forget callers that drop the handles cannot free or overwrite the send buffers while the sends are still in flight. Callers that do keep the handles may `wait()`

them as before; the retention entry is dropped on reap either way.

## Source code in `vllm/distributed/parallel_state.py`


|
|

###

`make_sibling_device_group(group_desc=None)`

[¶](https://docs.vllm.ai#vllm.distributed.GroupCoordinator.make_sibling_device_group)

Create a new device-side ProcessGroup with the same per-rank membership as this coordinator's `device_group`

, but backed by a distinct communicator. This is a collective call: every world rank must invoke it. Used where we want to issue ops that can run concurrently with ops on `device_group`

.

## Source code in `vllm/distributed/parallel_state.py`


###

`recv(size, dtype, src=None)`

[¶](https://docs.vllm.ai#vllm.distributed.GroupCoordinator.recv)

Receives a tensor from the source rank.

## Source code in `vllm/distributed/parallel_state.py`


###

`recv_object(src)`

[¶](https://docs.vllm.ai#vllm.distributed.GroupCoordinator.recv_object)

Receive the input object list from the source rank.

## Source code in `vllm/distributed/parallel_state.py`


###

`recv_tensor_dict(src=None, all_gather_group=None, all_gather_tensors=None)`

[¶](https://docs.vllm.ai#vllm.distributed.GroupCoordinator.recv_tensor_dict)

Recv the input tensor dictionary. NOTE: `src`

is the local rank of the source rank.

## The group for the all-gather operation. If provided,

an optimization is enabled where each rank in the group sends a slice of a tensor and the receiver reconstructs it using an all-gather, which can improve performance. This is typically the tensor-parallel group.

all_gather_tensors: A dictionary to specify which tensors should use the all-gather optimization, which is only effective when `all_gather_group`

is provided. By default, this optimization is on for any tensor whose size is divisible by the `all_gather_group`

's world size. However, it should be disabled for tensors that are not fully replicated across the group (e.g., the residual tensor when sequence parallelism is enabled). This dictionary allows overriding the default behavior on a per-tensor basis.

## Source code in `vllm/distributed/parallel_state.py`


###

`send(tensor, dst=None)`

[¶](https://docs.vllm.ai#vllm.distributed.GroupCoordinator.send)

Sends a tensor to the destination rank in a blocking way.

## Source code in `vllm/distributed/parallel_state.py`


###

`send_object(obj, dst)`

[¶](https://docs.vllm.ai#vllm.distributed.GroupCoordinator.send_object)

Send the input object list to the destination rank.

## Source code in `vllm/distributed/parallel_state.py`


###

`send_tensor_dict(tensor_dict, dst=None, all_gather_group=None, all_gather_tensors=None)`

[¶](https://docs.vllm.ai#vllm.distributed.GroupCoordinator.send_tensor_dict)

Send the input tensor dictionary. NOTE: `dst`

is the local rank of the source rank.

## The group for the all-gather operation. If provided,

an optimization is enabled where each rank in the group sends a slice of a tensor and the receiver reconstructs it using an all-gather, which can improve performance. This is typically the tensor-parallel group.

all_gather_tensors: A dictionary to specify which tensors should use the all-gather optimization, which is only effective when `all_gather_group`

is provided. By default, this optimization is on for any tensor whose size is divisible by the `all_gather_group`

's world size. However, it should be disabled for tensors that are not fully replicated across the group (e.g., the residual tensor when sequence parallelism is enabled). This dictionary allows overriding the default behavior on a per-tensor basis.

## Source code in `vllm/distributed/parallel_state.py`


##

`Handle`

[¶](https://docs.vllm.ai#vllm.distributed.Handle)

##

`StatelessProcessGroup`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.StatelessProcessGroup)

A dataclass to hold a metadata store, and the rank, world_size of the group. Only use it to communicate metadata between processes. For data-plane communication, create NCCL-related objects.

Methods:

-
–[all_gather_obj](https://docs.vllm.ai#vllm.distributed.StatelessProcessGroup.all_gather_obj)All gather an object from all ranks.

-
–[all_reduce](https://docs.vllm.ai#vllm.distributed.StatelessProcessGroup.all_reduce)All-reduce a tensor across all ranks.

-
–[barrier](https://docs.vllm.ai#vllm.distributed.StatelessProcessGroup.barrier)A robust barrier to synchronize all ranks.

-
–[broadcast](https://docs.vllm.ai#vllm.distributed.StatelessProcessGroup.broadcast)Broadcast a tensor from source rank to all other ranks.

-
–[broadcast_obj](https://docs.vllm.ai#vllm.distributed.StatelessProcessGroup.broadcast_obj)Broadcast an object from a source rank to all other ranks.

-
–[create](https://docs.vllm.ai#vllm.distributed.StatelessProcessGroup.create)A replacement for

`torch.distributed.init_process_group`

that does not -
–[expire_data](https://docs.vllm.ai#vllm.distributed.StatelessProcessGroup.expire_data)Expire data that is older than

`data_expiration_seconds`

seconds. -
–[recv](https://docs.vllm.ai#vllm.distributed.StatelessProcessGroup.recv)Receive a tensor from a source rank.

-
–[recv_obj](https://docs.vllm.ai#vllm.distributed.StatelessProcessGroup.recv_obj)Receive an object from a source rank.

-
–[send](https://docs.vllm.ai#vllm.distributed.StatelessProcessGroup.send)Send a tensor to a destination rank.

-
–[send_obj](https://docs.vllm.ai#vllm.distributed.StatelessProcessGroup.send_obj)Send an object to a destination rank.


## Source code in `vllm/distributed/utils.py`


|
|

###

`all_gather_obj(obj)`

[¶](https://docs.vllm.ai#vllm.distributed.StatelessProcessGroup.all_gather_obj)

All gather an object from all ranks.

## Source code in `vllm/distributed/utils.py`


###

`all_reduce(tensor, op=torch.distributed.ReduceOp.SUM)`

[¶](https://docs.vllm.ai#vllm.distributed.StatelessProcessGroup.all_reduce)

All-reduce a tensor across all ranks.

## Source code in `vllm/distributed/utils.py`


###

`barrier(timeout=30.0)`

[¶](https://docs.vllm.ai#vllm.distributed.StatelessProcessGroup.barrier)

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

[¶](https://docs.vllm.ai#vllm.distributed.StatelessProcessGroup.broadcast)

Broadcast a tensor from source rank to all other ranks.

## Source code in `vllm/distributed/utils.py`


###

`broadcast_obj(obj, src)`

[¶](https://docs.vllm.ai#vllm.distributed.StatelessProcessGroup.broadcast_obj)

Broadcast an object from a source rank to all other ranks. It does not clean up after all ranks have received the object. Use it for limited times, e.g., for initialization.

## Source code in `vllm/distributed/utils.py`


###

`create(host, port, rank, world_size, data_expiration_seconds=3600, store_timeout=300, listen_socket=None)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.distributed.StatelessProcessGroup.create)

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

[¶](https://docs.vllm.ai#vllm.distributed.StatelessProcessGroup.expire_data)

Expire data that is older than `data_expiration_seconds`

seconds.

## Source code in `vllm/distributed/utils.py`


###

`recv(tensor, src)`

[¶](https://docs.vllm.ai#vllm.distributed.StatelessProcessGroup.recv)

Receive a tensor from a source rank.

## Source code in `vllm/distributed/utils.py`


###

`recv_obj(src)`

[¶](https://docs.vllm.ai#vllm.distributed.StatelessProcessGroup.recv_obj)

Receive an object from a source rank.

###

`send(tensor, dst)`

[¶](https://docs.vllm.ai#vllm.distributed.StatelessProcessGroup.send)

Send a tensor to a destination rank.

## Source code in `vllm/distributed/utils.py`


###

`send_obj(obj, dst)`

[¶](https://docs.vllm.ai#vllm.distributed.StatelessProcessGroup.send_obj)

Send an object to a destination rank.

## Source code in `vllm/distributed/utils.py`


##

`checkpoint_prepare_distributed_state()`

[¶](https://docs.vllm.ai#vllm.distributed.checkpoint_prepare_distributed_state)

Prepare every device communicator for a process checkpoint.

## Source code in `vllm/distributed/parallel_state.py`


##

`checkpoint_restore_distributed_state()`

[¶](https://docs.vllm.ai#vllm.distributed.checkpoint_restore_distributed_state)

Restore every device communicator after a process checkpoint.

## Source code in `vllm/distributed/parallel_state.py`


##

`create_tcp_store(host, port, listen_socket=None, **kwargs)`

[¶](https://docs.vllm.ai#vllm.distributed.create_tcp_store)

Create a TCPStore, optionally taking ownership of `listen_socket`

.

## Source code in `vllm/distributed/utils.py`


##

`destroy_model_parallel()`

[¶](https://docs.vllm.ai#vllm.distributed.destroy_model_parallel)

Set the groups to none and destroy them.

## Source code in `vllm/distributed/parallel_state.py`


##

`direct_register_custom_op(op_name, op_func, mutates_args=None, fake_impl=None, target_lib=None, dispatch_key=None, tags=())`

[¶](https://docs.vllm.ai#vllm.distributed.direct_register_custom_op)

`torch.library.custom_op`

can have significant overhead because it needs to consider complicated dispatching logic. This function directly registers a custom op and dispatches it to the CUDA backend. See https://gist.github.com/youkaichao/ecbea9ec9fc79a45d2adce1784d7a9a5 for more details.

By default, the custom op is registered to the vLLM library. If you want to register it to a different library, you can pass the library object to the `target_lib`

argument.

IMPORTANT: the lifetime of the operator is tied to the lifetime of the library object. If you want to bind the operator to a different library, make sure the library object is alive when the operator is used.

## Source code in `vllm/utils/torch_utils.py`


##

`divide(numerator, denominator)`

[¶](https://docs.vllm.ai#vllm.distributed.divide)

Ensure that numerator is divisible by the denominator and return the division value.

##

`ensure_divisibility(numerator, denominator)`

[¶](https://docs.vllm.ai#vllm.distributed.ensure_divisibility)

Ensure that numerator is divisible by the denominator.

##

`ensure_model_parallel_initialized(tensor_model_parallel_size, pipeline_model_parallel_size, prefill_context_model_parallel_size=1, decode_context_model_parallel_size=1, backend=None)`

[¶](https://docs.vllm.ai#vllm.distributed.ensure_model_parallel_initialized)

Helper to initialize model parallel groups if they are not initialized, or ensure tensor-parallel and pipeline-parallel sizes are equal to expected values if the model parallel groups are initialized.

## Source code in `vllm/distributed/parallel_state.py`


##

`get_cached_tcp_store_client(host, port)`

`cached`

[¶](https://docs.vllm.ai#vllm.distributed.get_cached_tcp_store_client)

Return a cached TCPStore client.

Cached so that every call with the same `(host, port)`

reuses the same connection. A new `(host, port)`

evicts the old entry.

## Source code in `vllm/distributed/utils.py`


##

`get_engram_dp_group()`

[¶](https://docs.vllm.ai#vllm.distributed.get_engram_dp_group)

Return the DP replicas that share one engram embedding table.

None when every replica holds a full (TP-sharded) copy, which is the case for models without engram layers and for replicas that span nodes.

## Source code in `vllm/distributed/parallel_state.py`


##

`get_engram_dp_size()`

[¶](https://docs.vllm.ai#vllm.distributed.get_engram_dp_size)

##

`get_etp_group()`

[¶](https://docs.vllm.ai#vllm.distributed.get_etp_group)

Return the Engram Tensor Parallel (ETP) group that shards one embedding table.

##

`get_node_count()`

[¶](https://docs.vllm.ai#vllm.distributed.get_node_count)

Return the total number of nodes in the distributed environment.

##

`get_pp_indices(num_hidden_layers, pp_rank, pp_size)`

[¶](https://docs.vllm.ai#vllm.distributed.get_pp_indices)

Try to evenly distribute layers across partitions.

If the number of layers is not divisible by the number of partitions, the remaining layers are evenly distributed across all but the last partition. The last partition is excluded because it often contains an additional norm layer and we are attempting to balance compute.

If `pp_size > 2`

and the number of remaining layers is `0 < x <= pp_size - 2`

then the remaining layers are evenly distributed across the middle partitions. The first and last partitions are excluded because they contain the input and output embeddings respectively and we are attempting to reduce maximum memory consumption across partitions.

## Source code in `vllm/distributed/utils.py`


##

`get_tensor_model_parallel_rank()`

[¶](https://docs.vllm.ai#vllm.distributed.get_tensor_model_parallel_rank)

##

`get_tensor_model_parallel_world_size()`

[¶](https://docs.vllm.ai#vllm.distributed.get_tensor_model_parallel_world_size)

##

`get_worker_rank_suffix(global_rank=None)`

[¶](https://docs.vllm.ai#vllm.distributed.get_worker_rank_suffix)

Generate a descriptive rank suffix for worker identification.

Returns a string like 'dp0_pp0_tp0_dcp0_ep0_rank0' including all parallel dimensions: DP, PP, TP, DCP, EP.

Parameters:

-

(`global_rank`

[¶](https://docs.vllm.ai#vllm.distributed.get_worker_rank_suffix(global_rank))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)| None`None`

) –Optional global rank to append. If not provided, only parallel dimension ranks are included.


Returns:

## Source code in `vllm/distributed/utils.py`


##

`graph_capture(device)`

[¶](https://docs.vllm.ai#vllm.distributed.graph_capture)

`graph_capture`

is a context manager which should surround the code that is capturing the CUDA graph. Its main purpose is to ensure that some operations will be run after the graph is captured, before the graph is replayed. It returns a `GraphCaptureContext`

object which contains the necessary data for the graph capture. Currently, it only contains the stream that the graph capture is running on. This stream is set to the current CUDA stream when the context manager is entered and reset to the default stream when the context manager is exited. This is to ensure that the graph capture is running on a separate stream from the default stream, in order to explicitly distinguish the kernels to capture from other kernels possibly launched on background in the default stream.

## Source code in `vllm/distributed/parallel_state.py`


##

`in_the_same_node_as(pg, source_rank=0)`

[¶](https://docs.vllm.ai#vllm.distributed.in_the_same_node_as)

This is a collective operation that returns if each rank is in the same node as the source rank. It tests if processes are attached to the same memory system (shared access to shared memory).

## Source code in `vllm/distributed/parallel_state.py`


|
|

##

`init_gloo_process_group(prefix_store, group_rank, group_size, timeout)`

[¶](https://docs.vllm.ai#vllm.distributed.init_gloo_process_group)

Stateless init ProcessGroup with gloo backend compatible with different torch versions.

## Source code in `vllm/distributed/utils.py`


##

`init_logger(name)`

[¶](https://docs.vllm.ai#vllm.distributed.init_logger)

The main purpose of this function is to ensure that loggers are retrieved in such a way that we can be sure the root vllm logger has already been configured.

## Source code in `vllm/logger.py`


##

`initialize_model_parallel(tensor_model_parallel_size=1, pipeline_model_parallel_size=1, prefill_context_model_parallel_size=1, decode_context_model_parallel_size=1, backend=None)`

[¶](https://docs.vllm.ai#vllm.distributed.initialize_model_parallel)

Initialize model parallel groups.

Parameters:

-

(`tensor_model_parallel_size`

[¶](https://docs.vllm.ai#vllm.distributed.initialize_model_parallel(tensor_model_parallel_size))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`1`

) –number of GPUs used for tensor model parallelism.

-

(`pipeline_model_parallel_size`

[¶](https://docs.vllm.ai#vllm.distributed.initialize_model_parallel(pipeline_model_parallel_size))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`1`

) –number of GPUs used for pipeline model parallelism.

-

(`prefill_context_model_parallel_size`

[¶](https://docs.vllm.ai#vllm.distributed.initialize_model_parallel(prefill_context_model_parallel_size))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`1`

) –number of GPUs used for context parallelism during prefill.

-

(`decode_context_model_parallel_size`

[¶](https://docs.vllm.ai#vllm.distributed.initialize_model_parallel(decode_context_model_parallel_size))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)| None`1`

) –number of GPUs used for context parallelism during decode.

-

(`backend`

[¶](https://docs.vllm.ai#vllm.distributed.initialize_model_parallel(backend))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)| None`None`

) –name of torch distributed communication backend.


Let's say we have a total of 8 GPUs denoted by g0 ... g7 and we use 2 GPUs to parallelize the model tensor, and 4 GPUs to parallelize the model pipeline. The present function will create 4 tensor model-parallel groups and 2 pipeline model-parallel groups: 4 tensor model-parallel groups: [g0, g1], [g2, g3], [g4, g5], [g6, g7] 2 pipeline model-parallel groups: [g0, g2, g4, g6], [g1, g3, g5, g7] Note that for efficiency, the caller should make sure adjacent ranks are on the same DGX box. For example if we are using 2 DGX-1 boxes with a total of 16 GPUs, rank 0 to 7 belong to the first box and ranks 8 to 15 belong to the second box.

## Source code in `vllm/distributed/parallel_state.py`


|
|

##

`is_global_first_rank()`

[¶](https://docs.vllm.ai#vllm.distributed.is_global_first_rank)

Check if the current process is the first rank globally across all parallelism strategies (PP, TP, DP, EP, etc.).

Unlike group-specific checks like `get_tensor_model_parallel_rank() == 0`

or `get_pp_group().is_first_rank`

, this function checks the global rank across all parallelism dimensions.

Returns:

-
(`bool`


) –[bool](https://docs.python.org/3/builtins/functions.html#bool)True if this is the global first rank (rank 0), False otherwise. Returns True if distributed is not initialized (single process).


## Source code in `vllm/distributed/parallel_state.py`


##

`is_local_first_rank()`

[¶](https://docs.vllm.ai#vllm.distributed.is_local_first_rank)

Check if the current process is the first local rank (rank 0 on its node).

## Source code in `vllm/distributed/parallel_state.py`


##

`is_weak_contiguous(inp)`

[¶](https://docs.vllm.ai#vllm.distributed.is_weak_contiguous)

Check that *inp* occupies a single contiguous block of memory.

Unlike `torch.Tensor.is_contiguous()`

, this also accepts tensors whose strides are not strictly C-contiguous (e.g. column-major) as long as the underlying storage from the tensor's offset onward is exactly `numel * element_size`

bytes.

## Source code in `vllm/distributed/utils.py`


##

`model_parallel_is_initialized()`

[¶](https://docs.vllm.ai#vllm.distributed.model_parallel_is_initialized)

##

`resolve_obj_by_qualname(qualname)`

[¶](https://docs.vllm.ai#vllm.distributed.resolve_obj_by_qualname)

Resolve an object by its fully-qualified class name.

##

`resume_device_comms()`

[¶](https://docs.vllm.ai#vllm.distributed.resume_device_comms)

##

`split_tensor_along_last_dim(tensor, num_partitions, contiguous_split_chunks=False)`

[¶](https://docs.vllm.ai#vllm.distributed.split_tensor_along_last_dim)

Split a tensor along its last dimension.

Parameters:

-

(`tensor`

[¶](https://docs.vllm.ai#vllm.distributed.split_tensor_along_last_dim(tensor))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)input tensor.

-

(`num_partitions`

[¶](https://docs.vllm.ai#vllm.distributed.split_tensor_along_last_dim(num_partitions))

) –[int](https://docs.python.org/3/builtins/functions.html#int)number of partitions to split the tensor

-

(`contiguous_split_chunks`

[¶](https://docs.vllm.ai#vllm.distributed.split_tensor_along_last_dim(contiguous_split_chunks))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –If True, make each chunk contiguous in memory.


Returns:

## Source code in `vllm/distributed/utils.py`


##

`stateless_destroy_torch_distributed_process_group(pg)`

[¶](https://docs.vllm.ai#vllm.distributed.stateless_destroy_torch_distributed_process_group)

Destroy ProcessGroup returned by stateless_init_torch_distributed_process_group().

##

`stateless_init_torch_distributed_process_group(host, port, rank, world_size, backend, group_name=None, return_store=False, listen_socket=None)`

[¶](https://docs.vllm.ai#vllm.distributed.stateless_init_torch_distributed_process_group)

A replacement for `torch.distributed.init_process_group`

that does not pollute the global state. The created ProcessGroup object can be used for some operations such as `allreduce`

, because it does not depend on the global rank. However, some operations such as `broadcast`

cannot be used because it depends on the global rank.

### TODO: ask for help from PyTorch team if we need the `broadcast`

operation.[¶](https://docs.vllm.ai#vllm.distributed.stateless_init_torch_distributed_process_group--todo-ask-for-help-from-pytorch-team-if-we-need-the-broadcast-operation)

This function is useful when we are not sure about the total number of processes in the process group. For example, we may have process 1, 2, ..., 8 who want to communicate, and process 9 might be the same process as process 1, or it might be a different process; process 10 might be the same process as process 5, or it might be a different process. In this case, how can we reliably form a communication channel within process 9 and 10, without affecting the communication channel within process 1, 2, ..., 8?

One possible solution is to figure out if process 9 and 10 are the same as process 1 and 5 beforehand, and then form a communication channel based on the information, adjusting the ranks and world_size etc. However, figuring out the information is not always easy, and it will interfere with the main communication channel.

Our solution is to always form a communication channel with process 1, 2, ..., 8, and then use this function to form another communication channel with process 9 and 10. This way, regardless of whether process 9 and 10 are the same as process 1 and 5, the main communication channel is always formed with process 1, 2, ..., 8, and the additional communication channel is formed with process 9 and 10.

When *listen_socket* is provided, the rendezvous step is skipped and a `TCPStore`

server is created directly using the pre-bound socket. This is useful for eliminating TOCTOU races between port allocation and binding.

## Source code in `vllm/distributed/utils.py`


|
|

##

`suppress_stdout()`

[¶](https://docs.vllm.ai#vllm.distributed.suppress_stdout)

Suppress stdout from C libraries at the file descriptor level.

Only suppresses stdout, not stderr, to preserve error messages. Suppression is disabled when VLLM_LOGGING_LEVEL is set to DEBUG.

## Example

with suppress_stdout(): # C library calls that would normally print to stdout torch.distributed.new_group(ranks, backend="gloo")

## Source code in `vllm/utils/system_utils.py`


##

`suspend_device_comms()`

[¶](https://docs.vllm.ai#vllm.distributed.suspend_device_comms)

##

`tensor_model_parallel_all_gather(input_, dim=-1)`

[¶](https://docs.vllm.ai#vllm.distributed.tensor_model_parallel_all_gather)

All-gather the input tensor across model parallel group.

##

`tensor_model_parallel_all_reduce(input_)`

[¶](https://docs.vllm.ai#vllm.distributed.tensor_model_parallel_all_reduce)

##

`tensor_model_parallel_gather(input_, dst=0, dim=-1)`

[¶](https://docs.vllm.ai#vllm.distributed.tensor_model_parallel_gather)

Gather the input tensor across model parallel group.

##

`tensor_model_parallel_reduce_scatter(input_, dim=-1)`

[¶](https://docs.vllm.ai#vllm.distributed.tensor_model_parallel_reduce_scatter)

Reduce-Scatter the input tensor across model parallel group.

##

`verify_group_size_divides_partition(input_size_per_partition, group_size, layer_name=None, extra_suggestion='')`

[¶](https://docs.vllm.ai#vllm.distributed.verify_group_size_divides_partition)

Validate that a TP-sharded layer holds a whole number of quant groups.