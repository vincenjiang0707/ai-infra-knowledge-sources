source: https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/api/group.html

# Group Calls[](https://docs.nvidia.com#group-calls)

Group primitives define the behavior of the current thread to avoid blocking. They can therefore be used from multiple threads independently.

Related links: [Group Calls](https://docs.nvidia.com/usage/groups.html#group-calls).

## ncclGroupStart[](https://docs.nvidia.com#ncclgroupstart)

-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclGroupStart()[](https://docs.nvidia.com#c.ncclGroupStart) Start a group call.

All subsequent calls to NCCL until ncclGroupEnd will not block due to inter-CPU synchronization.


## ncclGroupEnd[](https://docs.nvidia.com#ncclgroupend)

-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclGroupEnd()[](https://docs.nvidia.com#c.ncclGroupEnd) End a group call.

Returns when all operations since ncclGroupStart have been processed. This means the communication primitives have been enqueued to the provided streams, but are not necessarily complete.

When used with the ncclCommInitRank call, the ncclGroupEnd call waits for all communicators to be initialized.


## ncclGroupSimulateEnd[](https://docs.nvidia.com#ncclgroupsimulateend)

-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclGroupSimulateEnd([ncclSimInfo_t](https://docs.nvidia.com/types.html#c.ncclSimInfo_t)*simInfo)[](https://docs.nvidia.com#c.ncclGroupSimulateEnd) Simulate a ncclGroupEnd() call and return NCCL’s simulation info in a structure passed as an argument.