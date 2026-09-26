source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/minimax_rms_norm/lamport_workspace/
lastmod: 2026-09-24

#

`vllm.model_executor.layers.minimax_rms_norm.lamport_workspace`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.minimax_rms_norm.lamport_workspace)

Classes:

-
–[IpcBuffer](https://docs.vllm.ai#vllm.model_executor.layers.minimax_rms_norm.lamport_workspace.IpcBuffer)Allocates CUDA device memory and exchanges IPC handles with all ranks

-
–[LamportWorkspace](https://docs.vllm.ai#vllm.model_executor.layers.minimax_rms_norm.lamport_workspace.LamportWorkspace)Self-contained workspace for Lamport-based cross-GPU AllReduce.


Functions:

-
–[get_allreduce_workspace](https://docs.vllm.ai#vllm.model_executor.layers.minimax_rms_norm.lamport_workspace.get_allreduce_workspace)Return a cached workspace tensor for the given (rank, world_size) pair.


##

`IpcBuffer`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.minimax_rms_norm.lamport_workspace.IpcBuffer)

Allocates CUDA device memory and exchanges IPC handles with all ranks so that every rank holds a valid device pointer to every other rank's buffer.

Methods:

-
–[serialize](https://docs.vllm.ai#vllm.model_executor.layers.minimax_rms_norm.lamport_workspace.IpcBuffer.serialize)Return peer pointers as a list of int64 values (one per rank).


## Source code in `vllm/model_executor/layers/minimax_rms_norm/lamport_workspace.py`


###

`serialize()`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.minimax_rms_norm.lamport_workspace.IpcBuffer.serialize)

Return peer pointers as a list of int64 values (one per rank).

## Source code in `vllm/model_executor/layers/minimax_rms_norm/lamport_workspace.py`


##

`LamportWorkspace`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.minimax_rms_norm.lamport_workspace.LamportWorkspace)

Self-contained workspace for Lamport-based cross-GPU AllReduce.

#### Parameters[¶](https://docs.vllm.ai#vllm.model_executor.layers.minimax_rms_norm.lamport_workspace.LamportWorkspace--parameters)

rank : int Local rank (0-based). world_size : int Total number of ranks in the TP group. comm_size : int Size in bytes of *one* Lamport buffer slot. The total IPC allocation per rank is `3 * comm_size`

(triple-buffering). Must be large enough to hold the per-slot data written by the kernel. Use `compute_comm_size_for_minimax()`

for a safe default. process_group : optional `torch.distributed`

process group for IPC handle exchange. `None`

uses the default group.

Methods:

-
–[compute_comm_size_for_minimax](https://docs.vllm.ai#vllm.model_executor.layers.minimax_rms_norm.lamport_workspace.LamportWorkspace.compute_comm_size_for_minimax)Return a safe

`comm_size`

(in bytes) for MiniMaxReduceRMSKernel.

Attributes:

## Source code in `vllm/model_executor/layers/minimax_rms_norm/lamport_workspace.py`


|
|

###

`workspace`

`property`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.minimax_rms_norm.lamport_workspace.LamportWorkspace.workspace)

Device tensor (int64) that can be passed to the kernel as `void** workspace`

.

###

`compute_comm_size_for_minimax(max_tokens, world_size, fused_qk=True)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.minimax_rms_norm.lamport_workspace.LamportWorkspace.compute_comm_size_for_minimax)

Return a safe `comm_size`

(in bytes) for MiniMaxReduceRMSKernel.

## The kernel stores per-token variance scalars in the Lamport buffer

- single-matrix path:
`world_size × max_tokens × 4`

bytes per slot - fused Q+K path:
`world_size × 2 × ceil(max_tokens/4) × 16`

bytes per slot

The returned value is rounded up to 2 MiB alignment.

## Source code in `vllm/model_executor/layers/minimax_rms_norm/lamport_workspace.py`


##

`_check(error)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.minimax_rms_norm.lamport_workspace._check)

Raise on CUDA runtime error.

## Source code in `vllm/model_executor/layers/minimax_rms_norm/lamport_workspace.py`


##

`_lamport_fill_neg_zero(device_ptr, size_bytes)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.minimax_rms_norm.lamport_workspace._lamport_fill_neg_zero)

Fill device memory with IEEE-754 negative zero (-0.0f = 0x80000000). This is the "slot empty" sentinel for the Lamport protocol: the kernel spin-waits until a value is *not* negative zero.

## Source code in `vllm/model_executor/layers/minimax_rms_norm/lamport_workspace.py`


##

`get_allreduce_workspace(rank, world_size, comm_size=None, max_tokens=16384, process_group=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.minimax_rms_norm.lamport_workspace.get_allreduce_workspace)

Return a cached workspace tensor for the given (rank, world_size) pair.

On first call the workspace is allocated and IPC handles are exchanged; subsequent calls with the same arguments return the cached tensor.

#### Parameters[¶](https://docs.vllm.ai#vllm.model_executor.layers.minimax_rms_norm.lamport_workspace.get_allreduce_workspace--parameters)

rank, world_size : int TP rank and TP size. comm_size : int, optional Explicit slot size in bytes. If `None`

, computed automatically from `max_tokens`

and `world_size`

(fused Q+K path). max_tokens : int Maximum number of tokens per batch (used when `comm_size is None`

). process_group : optional `torch.distributed`

process group.