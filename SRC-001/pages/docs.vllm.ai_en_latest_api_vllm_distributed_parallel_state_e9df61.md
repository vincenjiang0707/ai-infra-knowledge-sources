source: https://docs.vllm.ai/en/latest/api/vllm/distributed/parallel_state/
lastmod: 2026-09-23

#

`vllm.distributed.parallel_state`

[¶](https://docs.vllm.ai#vllm.distributed.parallel_state)

vLLM distributed state. It takes over the control of the distributed environment from PyTorch. The typical workflow is:

- call
`init_distributed_environment`

to initialize the distributed environment. -
call

`initialize_model_parallel`

or`ensure_model_parallel_initialized`

to initialize the model parallel groups. -
any code dealing with the distributed stuff

-
call

`destroy_model_parallel`

to destroy the model parallel groups. - call
`destroy_distributed_environment`

to destroy the distributed environment.

If you only need to use the distributed environment without model/pipeline parallelism, you can skip the model parallel initialization and destruction steps.

Classes:

-
–[GroupCoordinator](https://docs.vllm.ai#vllm.distributed.parallel_state.GroupCoordinator)PyTorch ProcessGroup wrapper for a group of processes.

-
–[Handle](https://docs.vllm.ai#vllm.distributed.parallel_state.Handle)Minimal async work handle used by P2P send/recv methods.


Functions:

-
–[checkpoint_prepare_distributed_state](https://docs.vllm.ai#vllm.distributed.parallel_state.checkpoint_prepare_distributed_state)Prepare every device communicator for a process checkpoint.

-
–[checkpoint_restore_distributed_state](https://docs.vllm.ai#vllm.distributed.parallel_state.checkpoint_restore_distributed_state)Restore every device communicator after a process checkpoint.

-
–[destroy_model_parallel](https://docs.vllm.ai#vllm.distributed.parallel_state.destroy_model_parallel)Set the groups to none and destroy them.

-
–[ensure_model_parallel_initialized](https://docs.vllm.ai#vllm.distributed.parallel_state.ensure_model_parallel_initialized)Helper to initialize model parallel groups if they are not initialized,

-
–[get_engram_dp_group](https://docs.vllm.ai#vllm.distributed.parallel_state.get_engram_dp_group)Return the DP replicas that share one engram embedding table.

-
–[get_engram_dp_size](https://docs.vllm.ai#vllm.distributed.parallel_state.get_engram_dp_size)Number of DP replicas one engram embedding table is sharded over.

-
–[get_etp_group](https://docs.vllm.ai#vllm.distributed.parallel_state.get_etp_group)Return the Engram Tensor Parallel (ETP) group that shards one embedding table.

-
–[get_node_count](https://docs.vllm.ai#vllm.distributed.parallel_state.get_node_count)Return the total number of nodes in the distributed environment.

-
–[get_tensor_model_parallel_rank](https://docs.vllm.ai#vllm.distributed.parallel_state.get_tensor_model_parallel_rank)Return my rank for the tensor model parallel group.

-
–[get_tensor_model_parallel_world_size](https://docs.vllm.ai#vllm.distributed.parallel_state.get_tensor_model_parallel_world_size)Return world size for the tensor model parallel group.

-
–[graph_capture](https://docs.vllm.ai#vllm.distributed.parallel_state.graph_capture)`graph_capture`

is a context manager which should surround the code that -
–[in_the_same_node_as](https://docs.vllm.ai#vllm.distributed.parallel_state.in_the_same_node_as)This is a collective operation that returns if each rank is in the same node

-
–[initialize_model_parallel](https://docs.vllm.ai#vllm.distributed.parallel_state.initialize_model_parallel)Initialize model parallel groups.

-
–[is_global_first_rank](https://docs.vllm.ai#vllm.distributed.parallel_state.is_global_first_rank)Check if the current process is the first rank globally across all

-
–[is_local_first_rank](https://docs.vllm.ai#vllm.distributed.parallel_state.is_local_first_rank)Check if the current process is the first local rank (rank 0 on its node).

-
–[model_parallel_is_initialized](https://docs.vllm.ai#vllm.distributed.parallel_state.model_parallel_is_initialized)Check if tensor and pipeline parallel groups are initialized.

-
–[resume_device_comms](https://docs.vllm.ai#vllm.distributed.parallel_state.resume_device_comms)Restore suspended device communicators (collective).

-
–[suspend_device_comms](https://docs.vllm.ai#vllm.distributed.parallel_state.suspend_device_comms)Release device communicator memory (collective; comms must be idle).


##

`GroupCoordinator`

[¶](https://docs.vllm.ai#vllm.distributed.parallel_state.GroupCoordinator)

PyTorch ProcessGroup wrapper for a group of processes. PyTorch ProcessGroup is bound to one specific communication backend, e.g. NCCL, Gloo, MPI, etc. GroupCoordinator takes charge of all the communication operations among the processes in the group. It manages both CPU and device communication.

Methods:

-
–[all_reduce](https://docs.vllm.ai#vllm.distributed.parallel_state.GroupCoordinator.all_reduce)User-facing all-reduce function before we actually call the

-
–[barrier](https://docs.vllm.ai#vllm.distributed.parallel_state.GroupCoordinator.barrier)Barrier synchronization among the group.

-
–[broadcast](https://docs.vllm.ai#vllm.distributed.parallel_state.GroupCoordinator.broadcast)Broadcast the input tensor.

-
–[broadcast_object](https://docs.vllm.ai#vllm.distributed.parallel_state.GroupCoordinator.broadcast_object)Broadcast the input object.

-
–[broadcast_object_list](https://docs.vllm.ai#vllm.distributed.parallel_state.GroupCoordinator.broadcast_object_list)Broadcast the input object list.

-
–[broadcast_tensor_dict](https://docs.vllm.ai#vllm.distributed.parallel_state.GroupCoordinator.broadcast_tensor_dict)Broadcast the input tensor dictionary.

-
–[gather](https://docs.vllm.ai#vllm.distributed.parallel_state.GroupCoordinator.gather)NOTE: We assume that the input tensor is on the same device across

-
–[isend_object](https://docs.vllm.ai#vllm.distributed.parallel_state.GroupCoordinator.isend_object)Non-blocking

`send_object`

: isend size + pickled object on the -
–[isend_tensor_dict](https://docs.vllm.ai#vllm.distributed.parallel_state.GroupCoordinator.isend_tensor_dict)Send the input tensor dictionary asynchronously.

-
–[make_sibling_device_group](https://docs.vllm.ai#vllm.distributed.parallel_state.GroupCoordinator.make_sibling_device_group)Create a new device-side ProcessGroup with the same per-rank membership

-
–[recv](https://docs.vllm.ai#vllm.distributed.parallel_state.GroupCoordinator.recv)Receives a tensor from the source rank.

-
–[recv_object](https://docs.vllm.ai#vllm.distributed.parallel_state.GroupCoordinator.recv_object)Receive the input object list from the source rank.

-
–[recv_tensor_dict](https://docs.vllm.ai#vllm.distributed.parallel_state.GroupCoordinator.recv_tensor_dict)Recv the input tensor dictionary.

-
–[send](https://docs.vllm.ai#vllm.distributed.parallel_state.GroupCoordinator.send)Sends a tensor to the destination rank in a blocking way.

-
–[send_object](https://docs.vllm.ai#vllm.distributed.parallel_state.GroupCoordinator.send_object)Send the input object list to the destination rank.

-
–[send_tensor_dict](https://docs.vllm.ai#vllm.distributed.parallel_state.GroupCoordinator.send_tensor_dict)Send the input tensor dictionary.


Attributes:

-
–[first_rank](https://docs.vllm.ai#vllm.distributed.parallel_state.GroupCoordinator.first_rank)Return the global rank of the first process in the group.

-
–[is_first_rank](https://docs.vllm.ai#vllm.distributed.parallel_state.GroupCoordinator.is_first_rank)Return whether the caller is the first process in the group.

-
–[is_last_rank](https://docs.vllm.ai#vllm.distributed.parallel_state.GroupCoordinator.is_last_rank)Return whether the caller is the last process in the group.

-
–[last_rank](https://docs.vllm.ai#vllm.distributed.parallel_state.GroupCoordinator.last_rank)Return the global rank of the last process in the group.

-
–[next_rank](https://docs.vllm.ai#vllm.distributed.parallel_state.GroupCoordinator.next_rank)Return the global rank of the process that follows the caller.

-
–[prev_rank](https://docs.vllm.ai#vllm.distributed.parallel_state.GroupCoordinator.prev_rank)Return the global rank of the process that precedes the caller.


## Source code in `vllm/distributed/parallel_state.py`


|
|

###

`first_rank`

`property`

[¶](https://docs.vllm.ai#vllm.distributed.parallel_state.GroupCoordinator.first_rank)

Return the global rank of the first process in the group.

###

`is_first_rank`

`property`

[¶](https://docs.vllm.ai#vllm.distributed.parallel_state.GroupCoordinator.is_first_rank)

Return whether the caller is the first process in the group.

###

`is_last_rank`

`property`

[¶](https://docs.vllm.ai#vllm.distributed.parallel_state.GroupCoordinator.is_last_rank)

Return whether the caller is the last process in the group.

###

`last_rank`

`property`

[¶](https://docs.vllm.ai#vllm.distributed.parallel_state.GroupCoordinator.last_rank)

Return the global rank of the last process in the group.

###

`next_rank`

`property`

[¶](https://docs.vllm.ai#vllm.distributed.parallel_state.GroupCoordinator.next_rank)

Return the global rank of the process that follows the caller.

###

`prev_rank`

`property`

[¶](https://docs.vllm.ai#vllm.distributed.parallel_state.GroupCoordinator.prev_rank)

Return the global rank of the process that precedes the caller.

###

`_reap_completed_isends()`

[¶](https://docs.vllm.ai#vllm.distributed.parallel_state.GroupCoordinator._reap_completed_isends)

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

[¶](https://docs.vllm.ai#vllm.distributed.parallel_state.GroupCoordinator.all_reduce)

User-facing all-reduce function before we actually call the all-reduce operation.

We need this because Dynamo does not support passing an arbitrary object (`self`

in this case) to a custom op. We need to pass the group name as a string, and then look up the group coordinator from the group name, dispatch the all-reduce operation to the group coordinator.

In addition, PyTorch custom ops do not support mutation or returning a new tensor in the same op. So we always make the all-reduce operation out-of-place.

## Source code in `vllm/distributed/parallel_state.py`


###

`barrier()`

[¶](https://docs.vllm.ai#vllm.distributed.parallel_state.GroupCoordinator.barrier)

Barrier synchronization among the group. NOTE: don't use `device_group`

here! `barrier`

in NCCL is terrible because it is internally a broadcast operation with secretly created GPU tensors. It is easy to mess up the current device. Use the CPU group instead.

## Source code in `vllm/distributed/parallel_state.py`


###

`broadcast(input_, src=0)`

[¶](https://docs.vllm.ai#vllm.distributed.parallel_state.GroupCoordinator.broadcast)

Broadcast the input tensor. NOTE: `src`

is the local rank of the source rank.

## Source code in `vllm/distributed/parallel_state.py`


###

`broadcast_object(obj=None, src=0)`

[¶](https://docs.vllm.ai#vllm.distributed.parallel_state.GroupCoordinator.broadcast_object)

Broadcast the input object. NOTE: `src`

is the local rank of the source rank.

## Source code in `vllm/distributed/parallel_state.py`


###

`broadcast_object_list(obj_list, src=0, group=None)`

[¶](https://docs.vllm.ai#vllm.distributed.parallel_state.GroupCoordinator.broadcast_object_list)

Broadcast the input object list. NOTE: `src`

is the local rank of the source rank.

## Source code in `vllm/distributed/parallel_state.py`


###

`broadcast_tensor_dict(tensor_dict=None, src=0, group=None, metadata_group=None)`

[¶](https://docs.vllm.ai#vllm.distributed.parallel_state.GroupCoordinator.broadcast_tensor_dict)

Broadcast the input tensor dictionary. NOTE: `src`

is the local rank of the source rank.

## Source code in `vllm/distributed/parallel_state.py`


|
|

###

`gather(input_, dst=0, dim=-1)`

[¶](https://docs.vllm.ai#vllm.distributed.parallel_state.GroupCoordinator.gather)

NOTE: We assume that the input tensor is on the same device across all the ranks. NOTE: `dst`

is the local rank of the destination rank.

## Source code in `vllm/distributed/parallel_state.py`


###

`isend_object(obj, dst)`

[¶](https://docs.vllm.ai#vllm.distributed.parallel_state.GroupCoordinator.isend_object)

Non-blocking `send_object`

: isend size + pickled object on the CPU group. Returns a handle that retains the serialized source tensors until `wait`

drains both sends.

## Source code in `vllm/distributed/parallel_state.py`


###

`isend_tensor_dict(tensor_dict, dst=None, all_gather_group=None, all_gather_tensors=None)`

[¶](https://docs.vllm.ai#vllm.distributed.parallel_state.GroupCoordinator.isend_tensor_dict)

Send the input tensor dictionary asynchronously.

The returned handles are additionally self-retained in `self._pending_isends`

(together with the sent source tensors) and reaped lazily on subsequent calls, so fire-and-forget callers that drop the handles cannot free or overwrite the send buffers while the sends are still in flight. Callers that do keep the handles may `wait()`

them as before; the retention entry is dropped on reap either way.

## Source code in `vllm/distributed/parallel_state.py`


|
|

###

`make_sibling_device_group(group_desc=None)`

[¶](https://docs.vllm.ai#vllm.distributed.parallel_state.GroupCoordinator.make_sibling_device_group)

Create a new device-side ProcessGroup with the same per-rank membership as this coordinator's `device_group`

, but backed by a distinct communicator. This is a collective call: every world rank must invoke it. Used where we want to issue ops that can run concurrently with ops on `device_group`

.

## Source code in `vllm/distributed/parallel_state.py`


###

`recv(size, dtype, src=None)`

[¶](https://docs.vllm.ai#vllm.distributed.parallel_state.GroupCoordinator.recv)

Receives a tensor from the source rank.

## Source code in `vllm/distributed/parallel_state.py`


###

`recv_object(src)`

[¶](https://docs.vllm.ai#vllm.distributed.parallel_state.GroupCoordinator.recv_object)

Receive the input object list from the source rank.

## Source code in `vllm/distributed/parallel_state.py`


###

`recv_tensor_dict(src=None, all_gather_group=None, all_gather_tensors=None)`

[¶](https://docs.vllm.ai#vllm.distributed.parallel_state.GroupCoordinator.recv_tensor_dict)

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

[¶](https://docs.vllm.ai#vllm.distributed.parallel_state.GroupCoordinator.send)

Sends a tensor to the destination rank in a blocking way.

## Source code in `vllm/distributed/parallel_state.py`


###

`send_object(obj, dst)`

[¶](https://docs.vllm.ai#vllm.distributed.parallel_state.GroupCoordinator.send_object)

Send the input object list to the destination rank.

## Source code in `vllm/distributed/parallel_state.py`


###

`send_tensor_dict(tensor_dict, dst=None, all_gather_group=None, all_gather_tensors=None)`

[¶](https://docs.vllm.ai#vllm.distributed.parallel_state.GroupCoordinator.send_tensor_dict)

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

[¶](https://docs.vllm.ai#vllm.distributed.parallel_state.Handle)

##

`_RetainedHandle`

[¶](https://docs.vllm.ai#vllm.distributed.parallel_state._RetainedHandle)

Handle that retains source tensors until all posted work completes.

Used by `isend_object`

to keep the serialized CPU tensors alive while gloo copies them in the background; `wait`

drops the refs once drained.

`wait`

must be idempotent: gloo `Work.wait()`

is single-shot for point-to-point operations — calling it a second time on an already completed send blocks forever (verified empirically). Both the worker's top-of-step drain of `_pp_send_work`

and `_reap_completed_isends`

may wait the same entry's metadata handle, so the second caller must not re-wait the underlying works.

## Source code in `vllm/distributed/parallel_state.py`


##

`_apply_to_device_comms(action)`

[¶](https://docs.vllm.ai#vllm.distributed.parallel_state._apply_to_device_comms)

Apply `action`

to every group's device communicator.

Walks the registered parallel groups and skips those without a device communicator (absent at `world_size == 1`

).

## Source code in `vllm/distributed/parallel_state.py`


##

`_create_subgroups_split_group(group_ranks, group_name, torch_distributed_backend)`

[¶](https://docs.vllm.ai#vllm.distributed.parallel_state._create_subgroups_split_group)

Create the device + CPU subgroups for `GroupCoordinator`

via `torch.distributed.split_group`

.

`split_group`

is collective on the parent group, so every parent rank must enter with the same `split_ranks`

definition. Each rank receives the subgroup it belongs to.

## Source code in `vllm/distributed/parallel_state.py`


##

`_device_backend_str(torch_distributed_backend)`

[¶](https://docs.vllm.ai#vllm.distributed.parallel_state._device_backend_str)

Normalize `torch_distributed_backend`

to the `"<device>:<backend>"`

format required by `split_group`

's `backend`

argument.

Accepts either a bare backend name (e.g. `"nccl"`

) or an already-prefixed string (e.g. `"cuda:nccl"`

).

## Source code in `vllm/distributed/parallel_state.py`


##

`_elastic_join_warmup_ctx()`

[¶](https://docs.vllm.ai#vllm.distributed.parallel_state._elastic_join_warmup_ctx)

Defer communicator warm-up when joining a live elastic-EP cluster on ROCm.

The existing ranks defer their matching warm-up in create_standby_groups(), so a joining worker must too or the warm-up collective has no peers. Both sides warm up at commit.

## Source code in `vllm/distributed/parallel_state.py`


##

`_engram_dp_shard_size(world_size, data_parallel_size, replica_size)`

[¶](https://docs.vllm.ai#vllm.distributed.parallel_state._engram_dp_shard_size)

Size of DP shards aligned with complete replicas and node boundaries.

## Source code in `vllm/distributed/parallel_state.py`


##

`_get_unique_name(name)`

[¶](https://docs.vllm.ai#vllm.distributed.parallel_state._get_unique_name)

Get a unique name for the group.

Example: _get_unique_name("tp") -> "tp:0" _get_unique_name("tp") -> "tp:1"

## Source code in `vllm/distributed/parallel_state.py`


##

`_init_process_group_for_split_group(*, backend, distributed_init_method, store, world_size, rank, local_rank, timeout)`

[¶](https://docs.vllm.ai#vllm.distributed.parallel_state._init_process_group_for_split_group)

Initialize the default PG with both CPU (gloo) and device (e.g. nccl) backends and an eager `device_id`

binding so that subgroups can be created via `split_group`

(which requires the parent communicator to be eagerly initialized). Falls back to `gloo`

on CPU-only systems.

## Source code in `vllm/distributed/parallel_state.py`


##

`_init_stateless_group(group_ranks, group_name, host, backend, coord_store, use_device_communicator=True, use_all2all=False)`

[¶](https://docs.vllm.ai#vllm.distributed.parallel_state._init_stateless_group)

Create a StatelessGroupCoordinator with the given parameters.

## Source code in `vllm/distributed/parallel_state.py`


##

`_node_count(pg)`

[¶](https://docs.vllm.ai#vllm.distributed.parallel_state._node_count)

Returns the total number of nodes in the process group.

Parameters:

-

(`pg`

[¶](https://docs.vllm.ai#vllm.distributed.parallel_state._node_count(pg))`ProcessGroup |`

) –[StatelessProcessGroup](https://docs.vllm.ai/utils/#vllm.distributed.utils.StatelessProcessGroup)The process group to analyze


Returns:

-
(`int`


) –[int](https://docs.python.org/3/builtins/functions.html#int)The total number of nodes


## Source code in `vllm/distributed/parallel_state.py`


##

`_platform_device_type()`

[¶](https://docs.vllm.ai#vllm.distributed.parallel_state._platform_device_type)

Return the device-type string (e.g. `"cuda"`

, `"xpu"`

, `"cpu"`

) for the current platform, in the form expected by `torch.distributed.init_process_group(backend=...)`

.

## Source code in `vllm/distributed/parallel_state.py`


##

`_replace_active_groups(*, world, dp, ep, eplb, node_count)`

[¶](https://docs.vllm.ai#vllm.distributed.parallel_state._replace_active_groups)

Replace the active groups and return the groups they replaced.

The caller must destroy the returned DP, EP, WORLD, and EPLB groups collectively and in that order. Pass all-`None`

to remove the active groups without replacement.

## Source code in `vllm/distributed/parallel_state.py`


##

`_split_tensor_dict(tensor_dict)`

[¶](https://docs.vllm.ai#vllm.distributed.parallel_state._split_tensor_dict)

Split the tensor dictionary into two parts: 1. A list of (key, value) pairs. If the value is a tensor, it is replaced by its metadata. 2. A list of tensors.

## Source code in `vllm/distributed/parallel_state.py`


##

`_validate_default_pg_for_split_group()`

[¶](https://docs.vllm.ai#vllm.distributed.parallel_state._validate_default_pg_for_split_group)

When an external launcher (e.g. `torchrun`

) initialized the default PG, `GroupCoordinator`

cannot patch in additional backends or change the eager-init behavior — `split_group`

only selects subsets of an existing parent. Validate that the parent has both `device_id`

and a CPU (gloo) backend, and emit a descriptive error pointing at the exact init call to update otherwise.

## Source code in `vllm/distributed/parallel_state.py`


##

`checkpoint_prepare_distributed_state()`

[¶](https://docs.vllm.ai#vllm.distributed.parallel_state.checkpoint_prepare_distributed_state)

Prepare every device communicator for a process checkpoint.

## Source code in `vllm/distributed/parallel_state.py`


##

`checkpoint_restore_distributed_state()`

[¶](https://docs.vllm.ai#vllm.distributed.parallel_state.checkpoint_restore_distributed_state)

Restore every device communicator after a process checkpoint.

## Source code in `vllm/distributed/parallel_state.py`


##

`destroy_model_parallel()`

[¶](https://docs.vllm.ai#vllm.distributed.parallel_state.destroy_model_parallel)

Set the groups to none and destroy them.

## Source code in `vllm/distributed/parallel_state.py`


##

`ensure_model_parallel_initialized(tensor_model_parallel_size, pipeline_model_parallel_size, prefill_context_model_parallel_size=1, decode_context_model_parallel_size=1, backend=None)`

[¶](https://docs.vllm.ai#vllm.distributed.parallel_state.ensure_model_parallel_initialized)

Helper to initialize model parallel groups if they are not initialized, or ensure tensor-parallel and pipeline-parallel sizes are equal to expected values if the model parallel groups are initialized.

## Source code in `vllm/distributed/parallel_state.py`


##

`get_engram_dp_group()`

[¶](https://docs.vllm.ai#vllm.distributed.parallel_state.get_engram_dp_group)

Return the DP replicas that share one engram embedding table.

None when every replica holds a full (TP-sharded) copy, which is the case for models without engram layers and for replicas that span nodes.

## Source code in `vllm/distributed/parallel_state.py`


##

`get_engram_dp_size()`

[¶](https://docs.vllm.ai#vllm.distributed.parallel_state.get_engram_dp_size)

##

`get_etp_group()`

[¶](https://docs.vllm.ai#vllm.distributed.parallel_state.get_etp_group)

Return the Engram Tensor Parallel (ETP) group that shards one embedding table.

##

`get_node_count()`

[¶](https://docs.vllm.ai#vllm.distributed.parallel_state.get_node_count)

Return the total number of nodes in the distributed environment.

##

`get_tensor_model_parallel_rank()`

[¶](https://docs.vllm.ai#vllm.distributed.parallel_state.get_tensor_model_parallel_rank)

##

`get_tensor_model_parallel_world_size()`

[¶](https://docs.vllm.ai#vllm.distributed.parallel_state.get_tensor_model_parallel_world_size)

##

`graph_capture(device)`

[¶](https://docs.vllm.ai#vllm.distributed.parallel_state.graph_capture)

`graph_capture`

is a context manager which should surround the code that is capturing the CUDA graph. Its main purpose is to ensure that some operations will be run after the graph is captured, before the graph is replayed. It returns a `GraphCaptureContext`

object which contains the necessary data for the graph capture. Currently, it only contains the stream that the graph capture is running on. This stream is set to the current CUDA stream when the context manager is entered and reset to the default stream when the context manager is exited. This is to ensure that the graph capture is running on a separate stream from the default stream, in order to explicitly distinguish the kernels to capture from other kernels possibly launched on background in the default stream.

## Source code in `vllm/distributed/parallel_state.py`


##

`in_the_same_node_as(pg, source_rank=0)`

[¶](https://docs.vllm.ai#vllm.distributed.parallel_state.in_the_same_node_as)

This is a collective operation that returns if each rank is in the same node as the source rank. It tests if processes are attached to the same memory system (shared access to shared memory).

## Source code in `vllm/distributed/parallel_state.py`


|
|

##

`initialize_model_parallel(tensor_model_parallel_size=1, pipeline_model_parallel_size=1, prefill_context_model_parallel_size=1, decode_context_model_parallel_size=1, backend=None)`

[¶](https://docs.vllm.ai#vllm.distributed.parallel_state.initialize_model_parallel)

Initialize model parallel groups.

Parameters:

-

(`tensor_model_parallel_size`

[¶](https://docs.vllm.ai#vllm.distributed.parallel_state.initialize_model_parallel(tensor_model_parallel_size))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`1`

) –number of GPUs used for tensor model parallelism.

-

(`pipeline_model_parallel_size`

[¶](https://docs.vllm.ai#vllm.distributed.parallel_state.initialize_model_parallel(pipeline_model_parallel_size))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`1`

) –number of GPUs used for pipeline model parallelism.

-

(`prefill_context_model_parallel_size`

[¶](https://docs.vllm.ai#vllm.distributed.parallel_state.initialize_model_parallel(prefill_context_model_parallel_size))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`1`

) –number of GPUs used for context parallelism during prefill.

-

(`decode_context_model_parallel_size`

[¶](https://docs.vllm.ai#vllm.distributed.parallel_state.initialize_model_parallel(decode_context_model_parallel_size))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)| None`1`

) –number of GPUs used for context parallelism during decode.

-

(`backend`

[¶](https://docs.vllm.ai#vllm.distributed.parallel_state.initialize_model_parallel(backend))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)| None`None`

) –name of torch distributed communication backend.


Let's say we have a total of 8 GPUs denoted by g0 ... g7 and we use 2 GPUs to parallelize the model tensor, and 4 GPUs to parallelize the model pipeline. The present function will create 4 tensor model-parallel groups and 2 pipeline model-parallel groups: 4 tensor model-parallel groups: [g0, g1], [g2, g3], [g4, g5], [g6, g7] 2 pipeline model-parallel groups: [g0, g2, g4, g6], [g1, g3, g5, g7] Note that for efficiency, the caller should make sure adjacent ranks are on the same DGX box. For example if we are using 2 DGX-1 boxes with a total of 16 GPUs, rank 0 to 7 belong to the first box and ranks 8 to 15 belong to the second box.

## Source code in `vllm/distributed/parallel_state.py`


|
|

##

`is_global_first_rank()`

[¶](https://docs.vllm.ai#vllm.distributed.parallel_state.is_global_first_rank)

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

[¶](https://docs.vllm.ai#vllm.distributed.parallel_state.is_local_first_rank)

Check if the current process is the first local rank (rank 0 on its node).