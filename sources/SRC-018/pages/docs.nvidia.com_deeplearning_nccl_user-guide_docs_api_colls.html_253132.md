source: https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/api/colls.html

# Collective Communication Functions[](https://docs.nvidia.com#collective-communication-functions)

The following NCCL APIs provide some commonly used collective operations.

## ncclAllReduce[](https://docs.nvidia.com#ncclallreduce)

-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclAllReduce(const void *sendbuff, void *recvbuff, size_t count,[ncclDataType_t](https://docs.nvidia.com/types.html#c.ncclDataType_t)datatype,[ncclRedOp_t](https://docs.nvidia.com/types.html#c.ncclRedOp_t)op,[ncclComm_t](https://docs.nvidia.com/types.html#c.ncclComm_t)comm, cudaStream_t stream)[](https://docs.nvidia.com#c.ncclAllReduce) Reduces data arrays of length

`count`

in`sendbuff`

using the`op`

operation and leaves identical copies of the result in each`recvbuff`

.In-place operation will happen if

`sendbuff == recvbuff`

.

Related links: [AllReduce](https://docs.nvidia.com/usage/collectives.html#allreduce).

## ncclBroadcast[](https://docs.nvidia.com#ncclbroadcast)

-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclBroadcast(const void *sendbuff, void *recvbuff, size_t count,[ncclDataType_t](https://docs.nvidia.com/types.html#c.ncclDataType_t)datatype, int root,[ncclComm_t](https://docs.nvidia.com/types.html#c.ncclComm_t)comm, cudaStream_t stream)[](https://docs.nvidia.com#c.ncclBroadcast) Copies

`count`

elements from`sendbuff`

on the`root`

rank to all ranks’`recvbuff`

.`sendbuff`

is only used on rank`root`

and ignored for other ranks.In-place operation will happen if

`sendbuff == recvbuff`

.

-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclBcast(void *buff, size_t count,[ncclDataType_t](https://docs.nvidia.com/types.html#c.ncclDataType_t)datatype, int root,[ncclComm_t](https://docs.nvidia.com/types.html#c.ncclComm_t)comm, cudaStream_t stream)[](https://docs.nvidia.com#c.ncclBcast) Legacy in-place version of

`ncclBroadcast`

in a similar fashion to MPI_Bcast. A call toncclBcast(buff, count, datatype, root, comm, stream)

is equivalent to

ncclBroadcast(buff, buff, count, datatype, root, comm, stream)


Related links: [Broadcast](https://docs.nvidia.com/usage/collectives.html#broadcast)

## ncclReduce[](https://docs.nvidia.com#ncclreduce)

-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclReduce(const void *sendbuff, void *recvbuff, size_t count,[ncclDataType_t](https://docs.nvidia.com/types.html#c.ncclDataType_t)datatype,[ncclRedOp_t](https://docs.nvidia.com/types.html#c.ncclRedOp_t)op, int root,[ncclComm_t](https://docs.nvidia.com/types.html#c.ncclComm_t)comm, cudaStream_t stream)[](https://docs.nvidia.com#c.ncclReduce) Reduce data arrays of length

`count`

in`sendbuff`

into`recvbuff`

on the`root`

rank using the`op`

operation.`recvbuff`

is only used on rank`root`

and ignored for other ranks.In-place operation will happen if

`sendbuff == recvbuff`

.

Related links: [Reduce](https://docs.nvidia.com/usage/collectives.html#reduce).

## ncclAllGather[](https://docs.nvidia.com#ncclallgather)

-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclAllGather(const void *sendbuff, void *recvbuff, size_t sendcount,[ncclDataType_t](https://docs.nvidia.com/types.html#c.ncclDataType_t)datatype,[ncclComm_t](https://docs.nvidia.com/types.html#c.ncclComm_t)comm, cudaStream_t stream)[](https://docs.nvidia.com#c.ncclAllGather) Gathers

`sendcount`

values from all GPUs and leaves identical copies of the result in each`recvbuff`

, receiving data from rank`i`

at offset`i*sendcount`

.Note: This assumes the receive count is equal to

`nranks*sendcount`

, which means that`recvbuff`

should have a size of at least`nranks*sendcount`

elements.In-place operation will happen if

`sendbuff == recvbuff + rank * sendcount`

.

Related links: [AllGather](https://docs.nvidia.com/usage/collectives.html#allgather), [In-place Operations](https://docs.nvidia.com/usage/inplace.html#in-place-operations).

## ncclReduceScatter[](https://docs.nvidia.com#ncclreducescatter)

-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclReduceScatter(const void *sendbuff, void *recvbuff, size_t recvcount,[ncclDataType_t](https://docs.nvidia.com/types.html#c.ncclDataType_t)datatype,[ncclRedOp_t](https://docs.nvidia.com/types.html#c.ncclRedOp_t)op,[ncclComm_t](https://docs.nvidia.com/types.html#c.ncclComm_t)comm, cudaStream_t stream)[](https://docs.nvidia.com#c.ncclReduceScatter) Reduce data in

`sendbuff`

from all GPUs using the`op`

operation and leave the reduced result scattered over the devices so that the`recvbuff`

on rank`i`

will contain the i-th block of the result.Note: This assumes the send count is equal to

`nranks*recvcount`

, which means that`sendbuff`

should have a size of at least`nranks*recvcount`

elements.In-place operation will happen if

`recvbuff == sendbuff + rank * recvcount`

.

Related links: [ReduceScatter](https://docs.nvidia.com/usage/collectives.html#reducescatter), [In-place Operations](https://docs.nvidia.com/usage/inplace.html#in-place-operations).

## ncclAlltoAll[](https://docs.nvidia.com#ncclalltoall)

-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclAlltoAll(const void *sendbuff, void *recvbuff, size_t count,[ncclDataType_t](https://docs.nvidia.com/types.html#c.ncclDataType_t)datatype,[ncclComm_t](https://docs.nvidia.com/types.html#c.ncclComm_t)comm, cudaStream_t stream)[](https://docs.nvidia.com#c.ncclAlltoAll) Each rank sends

`count`

values to all other ranks and receives`count`

values from all other ranks. Data to send to destination rank`j`

is taken from`sendbuff+j*count`

and data received from source rank`i`

is placed at`recvbuff+i*count`

.Note: This assumes both the total send and receive count is equal to

`nranks*count`

, which means that`sendbuff`

and`recvbuff`

should have a size of at least`nranks*count`

elements.In-place operation is currently not supported.


Related links: [AlltoAll](https://docs.nvidia.com/usage/collectives.html#alltoall).

## ncclGather[](https://docs.nvidia.com#ncclgather)

-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclGather(const void *sendbuff, void *recvbuff, size_t count,[ncclDataType_t](https://docs.nvidia.com/types.html#c.ncclDataType_t)datatype, int root,[ncclComm_t](https://docs.nvidia.com/types.html#c.ncclComm_t)comm, cudaStream_t stream)[](https://docs.nvidia.com#c.ncclGather) Each rank sends

`count`

elements from`sendbuff`

to the`root`

rank. On the`root`

rank, data from rank`i`

is placed at`recvbuff + i*count`

. On non-root ranks,`recvbuff`

is not used.Note: This assumes the receive count is equal to

`nranks*count`

, which means that`recvbuff`

should have a size of at least`nranks*count`

elements.In-place operation will happen if

`sendbuff == recvbuff + root * count`

.

Related links: [Gather](https://docs.nvidia.com/usage/collectives.html#gather).

## ncclScatter[](https://docs.nvidia.com#ncclscatter)

-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclScatter(const void *sendbuff, void *recvbuff, size_t count,[ncclDataType_t](https://docs.nvidia.com/types.html#c.ncclDataType_t)datatype, int root,[ncclComm_t](https://docs.nvidia.com/types.html#c.ncclComm_t)comm, cudaStream_t stream)[](https://docs.nvidia.com#c.ncclScatter) Each rank receives

`count`

elements from the`root`

rank. On the`root`

rank,`count`

elements from`sendbuff + i*count`

are sent to rank`i`

. On non-root ranks,`sendbuff`

is not used.Note: This assumes the send count is equal to

`nranks*count`

, which means that`sendbuff`

should have a size of at least`nranks*count`

elements.In-place operation will happen if

`recvbuff == sendbuff + root * count`

.

Related links: [Scatter](https://docs.nvidia.com/usage/collectives.html#scatter).

## Per-Collective Configuration Variants[](https://docs.nvidia.com#per-collective-configuration-variants)

Every collective above also has an `*Config`

variant that takes a trailing
[ ncclCollConfig_t](https://docs.nvidia.com/types.html#c.ncclCollConfig_t) argument for per-call customization (algorithm
selection, CTA counts, and similar overrides described under

[ncclCollConfig_t](https://docs.nvidia.com/types.html#ncclcollconfig)). Initialize the config with

`NCCL_COLLCONFIG_INITIALIZER`

and set it identically on every rank.
Passing `config == NULL`

is equivalent to calling the plain API.-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclAllReduceConfig(const void *sendbuff, void *recvbuff, size_t count,[ncclDataType_t](https://docs.nvidia.com/types.html#c.ncclDataType_t)datatype,[ncclRedOp_t](https://docs.nvidia.com/types.html#c.ncclRedOp_t)op,[ncclComm_t](https://docs.nvidia.com/types.html#c.ncclComm_t)comm, cudaStream_t stream, const[ncclCollConfig_t](https://docs.nvidia.com/types.html#c.ncclCollConfig_t)*config)[](https://docs.nvidia.com#c.ncclAllReduceConfig) Configurable variant of

.`ncclAllReduce()`


-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclBroadcastConfig(const void *sendbuff, void *recvbuff, size_t count,[ncclDataType_t](https://docs.nvidia.com/types.html#c.ncclDataType_t)datatype, int root,[ncclComm_t](https://docs.nvidia.com/types.html#c.ncclComm_t)comm, cudaStream_t stream, const[ncclCollConfig_t](https://docs.nvidia.com/types.html#c.ncclCollConfig_t)*config)[](https://docs.nvidia.com#c.ncclBroadcastConfig) Configurable variant of

.`ncclBroadcast()`


-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclReduceConfig(const void *sendbuff, void *recvbuff, size_t count,[ncclDataType_t](https://docs.nvidia.com/types.html#c.ncclDataType_t)datatype,[ncclRedOp_t](https://docs.nvidia.com/types.html#c.ncclRedOp_t)op, int root,[ncclComm_t](https://docs.nvidia.com/types.html#c.ncclComm_t)comm, cudaStream_t stream, const[ncclCollConfig_t](https://docs.nvidia.com/types.html#c.ncclCollConfig_t)*config)[](https://docs.nvidia.com#c.ncclReduceConfig) Configurable variant of

.`ncclReduce()`


-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclAllGatherConfig(const void *sendbuff, void *recvbuff, size_t sendcount,[ncclDataType_t](https://docs.nvidia.com/types.html#c.ncclDataType_t)datatype,[ncclComm_t](https://docs.nvidia.com/types.html#c.ncclComm_t)comm, cudaStream_t stream, const[ncclCollConfig_t](https://docs.nvidia.com/types.html#c.ncclCollConfig_t)*config)[](https://docs.nvidia.com#c.ncclAllGatherConfig) Configurable variant of

.`ncclAllGather()`


-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclReduceScatterConfig(const void *sendbuff, void *recvbuff, size_t recvcount,[ncclDataType_t](https://docs.nvidia.com/types.html#c.ncclDataType_t)datatype,[ncclRedOp_t](https://docs.nvidia.com/types.html#c.ncclRedOp_t)op,[ncclComm_t](https://docs.nvidia.com/types.html#c.ncclComm_t)comm, cudaStream_t stream, const[ncclCollConfig_t](https://docs.nvidia.com/types.html#c.ncclCollConfig_t)*config)[](https://docs.nvidia.com#c.ncclReduceScatterConfig) Configurable variant of

.`ncclReduceScatter()`


-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclAlltoAllConfig(const void *sendbuff, void *recvbuff, size_t count,[ncclDataType_t](https://docs.nvidia.com/types.html#c.ncclDataType_t)datatype,[ncclComm_t](https://docs.nvidia.com/types.html#c.ncclComm_t)comm, cudaStream_t stream, const[ncclCollConfig_t](https://docs.nvidia.com/types.html#c.ncclCollConfig_t)*config)[](https://docs.nvidia.com#c.ncclAlltoAllConfig) Configurable variant of

.`ncclAlltoAll()`


-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclGatherConfig(const void *sendbuff, void *recvbuff, size_t count,[ncclDataType_t](https://docs.nvidia.com/types.html#c.ncclDataType_t)datatype, int root,[ncclComm_t](https://docs.nvidia.com/types.html#c.ncclComm_t)comm, cudaStream_t stream, const[ncclCollConfig_t](https://docs.nvidia.com/types.html#c.ncclCollConfig_t)*config)[](https://docs.nvidia.com#c.ncclGatherConfig) Configurable variant of

.`ncclGather()`


-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclScatterConfig(const void *sendbuff, void *recvbuff, size_t count,[ncclDataType_t](https://docs.nvidia.com/types.html#c.ncclDataType_t)datatype, int root,[ncclComm_t](https://docs.nvidia.com/types.html#c.ncclComm_t)comm, cudaStream_t stream, const[ncclCollConfig_t](https://docs.nvidia.com/types.html#c.ncclCollConfig_t)*config)[](https://docs.nvidia.com#c.ncclScatterConfig) Configurable variant of

.`ncclScatter()`