source: https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/nccl4py/communicator/status.html

# Status and Utility Methods[](https://docs.nvidia.com#status-and-utility-methods)

Methods on [ Communicator](https://docs.nvidia.com/class.html#nccl.core.Communicator) for resource cleanup and error/status
queries.

## close_all_resources[](https://docs.nvidia.com#close-all-resources)

-
Communicator.close_all_resources() None
[](https://docs.nvidia.com#nccl.core.Communicator.close_all_resources) Closes all resources owned by this communicator.

Called automatically during

and`destroy()`

, but can be called manually. Performs best-effort cleanup, ignoring any errors that occur during resource deallocation. Idempotent: safe to call multiple times.`abort()`


## get_last_error[](https://docs.nvidia.com#get-last-error)

-
Communicator.get_last_error() str
[](https://docs.nvidia.com#nccl.core.Communicator.get_last_error) Returns the last error string for this communicator.

- Raises:
– If the communicator is not initialized.**NcclInvalid**


## get_async_error[](https://docs.nvidia.com#get-async-error)

-
Communicator.get_async_error() nccl.bindings.nccl.Result
[](https://docs.nvidia.com#nccl.core.Communicator.get_async_error) Queries the progress and potential errors of asynchronous NCCL operations.

Operations without a stream argument (e.g.

) are complete when they return`finalize()`

`ncclSuccess`

. Operations with a stream argument (e.g.) return`reduce()`

`ncclSuccess`

when posted but may report errors through this method until completed. If any NCCL function returns`ncclInProgress`

, users must query the communicator state until it becomes`ncclSuccess`

before calling another NCCL function.Before the state becomes

`ncclSuccess`

, do not issue CUDA kernels on streams used by NCCL. If an error occurs, destroy the communicator with; nothing can be assumed about the completion or correctness of enqueued operations after an error.`abort()`

- Returns:
Current state of the communicator (

`ncclSuccess`

,`ncclInProgress`

, or an error code).- Raises:
– If the communicator is not initialized.**NcclInvalid**

See also


## get_mem_stat[](https://docs.nvidia.com#get-mem-stat)

-
Communicator.get_mem_stat(
*stat:*) int[NcclCommMemStat](https://docs.nvidia.com#nccl.core.NcclCommMemStat)[](https://docs.nvidia.com#nccl.core.Communicator.get_mem_stat) Queries communicator memory statistics.

- Parameters:
**stat**– The memory statistic to query.- Returns:
The memory statistic value (bytes, or 0/1 for GPU_MEM_SUSPENDED).

- Raises:
– If the communicator is not initialized.**NcclInvalid**


## NcclCommMemStat[](https://docs.nvidia.com#ncclcommmemstat)

-
*class*nccl.core.NcclCommMemStat(*value*,*names=<not given>*,**values*,*module=None*,*qualname=None*,*type=None*,*start=1*,*boundary=None*)[](https://docs.nvidia.com#nccl.core.NcclCommMemStat) Bases:

`IntEnum`

Memory-statistic selector, mirroring

.`ncclCommMemStat_t`

Used as the

`stat`

argument ofto identify which memory statistic to query. All values are returned in bytes except`Communicator.get_mem_stat()`

, which is a 0/1 flag.`GPU_MEM_SUSPENDED`

-
GPU_MEM_SUSPEND
*= 0*[](https://docs.nvidia.com#nccl.core.NcclCommMemStat.GPU_MEM_SUSPEND) Communicator-allocated GPU memory that can be released by

(bytes).`Communicator.suspend()`


-
GPU_MEM_SUSPENDED
*= 1*[](https://docs.nvidia.com#nccl.core.NcclCommMemStat.GPU_MEM_SUSPENDED) Whether communicator-allocated GPU memory is currently suspended (

`0`

= active,`1`

= suspended).

-
GPU_MEM_PERSIST
*= 2*[](https://docs.nvidia.com#nccl.core.NcclCommMemStat.GPU_MEM_PERSIST) Communicator-allocated GPU memory that cannot be suspended (bytes).


-
GPU_MEM_TOTAL
*= 3*[](https://docs.nvidia.com#nccl.core.NcclCommMemStat.GPU_MEM_TOTAL) Total communicator-allocated GPU memory tracked by NCCL (bytes).


-
GPU_MEM_SUSPEND

## get_error_string[](https://docs.nvidia.com#get-error-string)

Module-level helper to render an NCCL result code as a human-readable string.

-
nccl.core.get_error_string(
*nccl_result: _nccl_bindings.Result | int*) str[](https://docs.nvidia.com#nccl.core.get_error_string) Returns a human-readable error string for an NCCL result code.

- Parameters:
**nccl_result**– NCCL result code.- Returns:
Human-readable error message corresponding to the result code.