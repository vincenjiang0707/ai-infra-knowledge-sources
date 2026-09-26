source: https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/nccl4py/group.html

# Group Operations[](https://docs.nvidia.com#group-operations)

Free functions and helpers for batching NCCL operations into groups. See
[Group Calls](https://docs.nvidia.com/usage/groups.html#group-calls) for usage details.

## group[](https://docs.nvidia.com#group)

-
nccl.core.group() Generator[None, None, None]
[](https://docs.nvidia.com#nccl.core.group) Context manager for NCCL group operations.

Automatically calls

on entry and`group_start()`

on exit, ensuring proper cleanup even if an exception occurs.`group_end()`

Simulation mode is not supported here. To simulate, call

and`group_start()`

directly and pass`group_end()`

`simulate=True`

to.`group_end()`


## group_start[](https://docs.nvidia.com#group-start)

-
nccl.core.group_start() None
[](https://docs.nvidia.com#nccl.core.group_start) Starts a group of NCCL operations.

All NCCL operations called after this will be batched together and executed when

is called. This can improve performance by allowing NCCL to optimize the operation sequence.`group_end()`


## group_end[](https://docs.nvidia.com#group-end)

-
nccl.core.group_end(
***,*simulate: Literal[False] = False*) None[](https://docs.nvidia.com#nccl.core.group_end) -
nccl.core.group_end(
***,*simulate: Literal[True]*)[GroupSimInfo](https://docs.nvidia.com#nccl.core.GroupSimInfo) -
nccl.core.group_end(
***,*simulate: bool*)[GroupSimInfo](https://docs.nvidia.com#nccl.core.GroupSimInfo)| None Ends a group of NCCL operations.

By default, executes all operations queued since the last

. When`group_start()`

`simulate=True`

, the queued operations are simulated instead of executed, and the estimated execution time is returned in a.`GroupSimInfo`

- Parameters:
**simulate**– When True, simulates the group instead of executing it and returns acarrying the estimated time. Defaults to False.`GroupSimInfo`

- Returns:
`None`

when`simulate=False`

; awith the simulation result when`GroupSimInfo`

`simulate=True`

.


## GroupSimInfo[](https://docs.nvidia.com#groupsiminfo)

-
*class*nccl.core.GroupSimInfo(*estimated_time: float*)[](https://docs.nvidia.com#nccl.core.GroupSimInfo) Bases:

`object`

Result of an NCCL group simulation.

Returned by

when called with`group_end()`

`simulate=True`

.-
estimated_time
*: float*[](https://docs.nvidia.com#nccl.core.GroupSimInfo.estimated_time) Estimated execution time for the simulated group operations, in seconds.


-
estimated_time