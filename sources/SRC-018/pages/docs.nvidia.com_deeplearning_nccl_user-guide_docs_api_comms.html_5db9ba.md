source: https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/api/comms.html

# Communicator Creation and Management Functions[](https://docs.nvidia.com#communicator-creation-and-management-functions)

The following functions are public APIs exposed by NCCL to create and manage the collective communication operations.

## ncclGetLastError[](https://docs.nvidia.com#ncclgetlasterror)

-
const char *ncclGetLastError(
[ncclComm_t](https://docs.nvidia.com/types.html#c.ncclComm_t)comm)[](https://docs.nvidia.com#c.ncclGetLastError)

Returns a human-readable string corresponding to the last error that occurred in NCCL. Note: The error is not cleared by calling this function. Please note that the string returned by ncclGetLastError could be unrelated to the current call and can be a result of previously launched asynchronous operations, if any.

## ncclGetErrorString[](https://docs.nvidia.com#ncclgeterrorstring)

-
const char *ncclGetErrorString(
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)result)[](https://docs.nvidia.com#c.ncclGetErrorString)

Returns a human-readable string corresponding to the passed error code.

## ncclGetVersion[](https://docs.nvidia.com#ncclgetversion)

-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclGetVersion(int *version)[](https://docs.nvidia.com#c.ncclGetVersion)

The ncclGetVersion function returns the version number of the currently linked NCCL library.
The NCCL version number is returned in *version* and encoded as an integer which includes the
`NCCL_MAJOR`

, `NCCL_MINOR`

and `NCCL_PATCH`

levels.
The version number returned will be the same as the `NCCL_VERSION_CODE`

defined in *nccl.h*.
NCCL version numbers can be compared using the supplied macro `NCCL_VERSION`

as `NCCL_VERSION(MAJOR,MINOR,PATCH)`


## ncclGetUniqueId[](https://docs.nvidia.com#ncclgetuniqueid)

-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclGetUniqueId(ncclUniqueId *uniqueId)[](https://docs.nvidia.com#c.ncclGetUniqueId)

Generates an Id to be used in ncclCommInitRank. ncclGetUniqueId should be
called once when creating a communicator and the Id should be distributed to all ranks in the
communicator before calling ncclCommInitRank. *uniqueId* should point to a ncclUniqueId object allocated by the user.

## ncclSetEncryption[](https://docs.nvidia.com#ncclsetencryption)

-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclSetEncryption(const[ncclEncryptionConfig_t](https://docs.nvidia.com/types.html#c.ncclEncryptionConfig_t)*config)[](https://docs.nvidia.com#c.ncclSetEncryption)

Configures process-global encryption for NCCL-owned TCP sockets. A configuration with `mode`

set to
`NCCL_ENCRYPTION_MODE_PSK`

requests TLS encryption using the supplied PSK.

Applications should call this function before [ ncclGetUniqueId()](https://docs.nvidia.com#c.ncclGetUniqueId) or any other NCCL operation that may create
network connections. All processes that communicate with each other must use the same PSK and keep it unchanged for the
job. See

[Setup](https://docs.nvidia.com/setup.html#setup-label)for build requirements, traffic coverage, and operational guidance.

## ncclCommInitRank[](https://docs.nvidia.com#ncclcomminitrank)

-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclCommInitRank([ncclComm_t](https://docs.nvidia.com/types.html#c.ncclComm_t)*comm, int nranks, ncclUniqueId commId, int rank)[](https://docs.nvidia.com#c.ncclCommInitRank)

Creates a new communicator (multi thread/process version).
*rank* must be between 0 and *nranks*-1 and unique within a communicator clique.
Each rank is associated to a CUDA device, which has to be set before calling
ncclCommInitRank.
ncclCommInitRank implicitly synchronizes with other ranks, hence it must be
called by different threads/processes or used within ncclGroupStart/ncclGroupEnd.

## ncclCommInitAll[](https://docs.nvidia.com#ncclcomminitall)

-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclCommInitAll([ncclComm_t](https://docs.nvidia.com/types.html#c.ncclComm_t)*comms, int ndev, const int *devlist)[](https://docs.nvidia.com#c.ncclCommInitAll)

Creates a clique of communicators (single process version) in a blocking way.
This is a convenience function to create a single-process communicator clique.
Returns an array of *ndev* newly initialized communicators in *comms*.
*comms* should be pre-allocated with size at least ndev*sizeof([ ncclComm_t](https://docs.nvidia.com/types.html#c.ncclComm_t)).

*devlist*defines the CUDA devices associated with each rank. If

*devlist*is NULL, the first

*ndev*CUDA devices are used, in order.

## ncclCommInitRankConfig[](https://docs.nvidia.com#ncclcomminitrankconfig)

-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclCommInitRankConfig([ncclComm_t](https://docs.nvidia.com/types.html#c.ncclComm_t)*comm, int nranks, ncclUniqueId commId, int rank,[ncclConfig_t](https://docs.nvidia.com/types.html#c.ncclConfig_t)*config)[](https://docs.nvidia.com#c.ncclCommInitRankConfig)

This function works the same way as *ncclCommInitRank* but accepts a configuration argument of extra attributes for
the communicator. If config is passed as NULL, the communicator will have the default behavior, as if ncclCommInitRank
was called.

See the [Creating a communicator with options](https://docs.nvidia.com/usage/communicators.html#init-rank-config) section for details on configuration options.

## ncclCommInitRankScalable[](https://docs.nvidia.com#ncclcomminitrankscalable)

-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclCommInitRankScalable([ncclComm_t](https://docs.nvidia.com/types.html#c.ncclComm_t)*newcomm, int nranks, int myrank, int nId, ncclUniqueId *commIds,[ncclConfig_t](https://docs.nvidia.com/types.html#c.ncclConfig_t)*config)[](https://docs.nvidia.com#c.ncclCommInitRankScalable)

This function works the same way as *ncclCommInitRankConfig* but accepts a list of ncclUniqueIds instead of a single one.
If only one ncclUniqueId is passed, the communicator will be initialized as if ncclCommInitRankConfig was called.
The provided ncclUniqueIds will all be used to initialize the single communicator given in argument.

See the [Creating a communicator with options](https://docs.nvidia.com/usage/communicators.html#init-rank-config) section for details on how to create and distribute the list of ncclUniqueIds.

## ncclCommSplit[](https://docs.nvidia.com#ncclcommsplit)

-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclCommSplit([ncclComm_t](https://docs.nvidia.com/types.html#c.ncclComm_t)comm, int color, int key,[ncclComm_t](https://docs.nvidia.com/types.html#c.ncclComm_t)*newcomm,[ncclConfig_t](https://docs.nvidia.com/types.html#c.ncclConfig_t)*config)[](https://docs.nvidia.com#c.ncclCommSplit)

The *ncclCommSplit* is a collective function and creates a set of new communicators from an existing one. Ranks which
pass the same *color* value will be part of the same group; color must be a non-negative value. If it is
passed as *NCCL_SPLIT_NOCOLOR*, it means that the rank will not be part of any group, therefore returning NULL
as newcomm.
The value of key will determine the rank order, and the smaller key means the smaller rank in new communicator.
If keys are equal between ranks, then the rank in the original communicator will be used to order ranks.
If the new communicator needs to have a special configuration, it can be passed as *config*, otherwise setting
config to NULL will make the new communicator inherit the original communicator’s configuration.
When split, there should not be any outstanding NCCL operations on the *comm*. Otherwise, it might cause
a deadlock.

## ncclCommShrink[](https://docs.nvidia.com#ncclcommshrink)

-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclCommShrink([ncclComm_t](https://docs.nvidia.com/types.html#c.ncclComm_t)comm, int *excludeRanksList, int excludeRanksCount,[ncclComm_t](https://docs.nvidia.com/types.html#c.ncclComm_t)*newcomm,[ncclConfig_t](https://docs.nvidia.com/types.html#c.ncclConfig_t)*config, int shrinkFlags)[](https://docs.nvidia.com#c.ncclCommShrink)

The *ncclCommShrink* function creates a new communicator by removing specified ranks from an existing communicator.
It is a collective function that must be called by all participating ranks in the newly created communicator.
Ranks that are part of *excludeRanksList* should not call this function.
The original ranks listed in *excludeRanksList* (of size *excludeRanksCount*) will be excluded from the new communicator.
Within the new communicator, ranks will be updated to maintain a contiguous set of ids.
If the new communicator needs a special configuration, it can be passed as *config*; otherwise, setting config to NULL will make the new communicator inherit the configuration of the parent communicator.

The *shrinkFlags* parameter controls the behavior of the operation. Use *NCCL_SHRINK_DEFAULT* (or *0*) for normal operation, or *NCCL_SHRINK_ABORT* when shrinking after an error on the parent communicator.
Specifically, when using *NCCL_SHRINK_DEFAULT*, there should not be any outstanding NCCL operations on the *comm* to avoid potential deadlocks. Further, if the parent communicator has the flag config.shrinkShare set to 1, NCCL will reuse the parent communicator resources.
On the other hand, when using *NCCL_SHRINK_ABORT*, NCCL will automatically abort any outstanding operations on the parent communicator, and no resources will be shared between the parent and the newly created communicator.

## ncclCommGetUniqueId[](https://docs.nvidia.com#ncclcommgetuniqueid)

-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclCommGetUniqueId([ncclComm_t](https://docs.nvidia.com/types.html#c.ncclComm_t)comm, ncclUniqueId *uniqueId)[](https://docs.nvidia.com#c.ncclCommGetUniqueId)

The *ncclCommGetUniqueId* function generates a unique identifier for growing an
existing communicator exactly once. This function must be called by only one
rank (the coordinator) before each grow operation on the existing communicator.
The coordinator is responsible for distributing the *uniqueId* to all new ranks
before they join the communicator via *ncclCommGrow*. This function should only
be called when there are no outstanding NCCL operations on the communicator.

## ncclCommGrow[](https://docs.nvidia.com#ncclcommgrow)

-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclCommGrow([ncclComm_t](https://docs.nvidia.com/types.html#c.ncclComm_t)comm, int nRanks, const ncclUniqueId *uniqueId, int rank,[ncclComm_t](https://docs.nvidia.com/types.html#c.ncclComm_t)*newcomm,[ncclConfig_t](https://docs.nvidia.com/types.html#c.ncclConfig_t)*config)[](https://docs.nvidia.com#c.ncclCommGrow)

The *ncclCommGrow* function creates a new communicator by adding new ranks to an existing communicator.
It must be called by both existing ranks (from the parent communicator) and new ranks (joining the communicator).

**For existing ranks:**

*comm*should be the parent communicator*rank*must be set to*-1*(existing ranks retain their original rank in the new communicator)*uniqueId*unused. (existing ranks receive coordination information internally)The function creates

*newcomm*with the same rank as in the parent communicator

**For new ranks:**

*comm*should be*NULL**rank*must be set to the desired rank in the new communicator (must be >= parent communicator size)*uniqueId*must be the unique identifier obtained from*ncclCommGetUniqueId*called by the coordinator

The *nRanks* parameter specifies the total number of ranks in the new communicator and must be greater than the size of the parent communicator.
If the new communicator needs a special configuration, it can be passed as *config*; otherwise, setting config to NULL will make the new communicator inherit the configuration of the parent communicator (for existing ranks) or use default configuration (for new ranks).

There should not be any outstanding NCCL operations on the parent communicator when calling this function to avoid potential deadlocks.
After the grow operation completes, the parent communicator should be destroyed using *ncclCommDestroy* to free resources.

**Example workflow:**

Coordinator rank calls

*ncclCommGetUniqueId*to generate the grow identifierCoordinator distributes the

*uniqueId*to all new ranks (out-of-band)All existing ranks call

*ncclCommGrow*with*comm*=parent,*rank*=-1,*uniqueId*=NULLAll new ranks call

*ncclCommGrow*with*comm*=NULL,*rank*=new_rank,*uniqueId*=received_id

## ncclCommRevoke[](https://docs.nvidia.com#ncclcommrevoke)

-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclCommRevoke([ncclComm_t](https://docs.nvidia.com/types.html#c.ncclComm_t)comm, int revokeFlags)[](https://docs.nvidia.com#c.ncclCommRevoke)

Revokes in-flight operations on a communicator without destroying resources. Successful return may be *ncclInProgress* (non-blocking) while revocation completes asynchronously; applications can query *ncclCommGetAsyncError* until it returns *ncclSuccess*.

*revokeFlags* must be set to *NCCL_REVOKE_DEFAULT* (0). Other values are reserved for future use.

After revoke completes, the communicator is quiesced and safe for destroy, split, and shrink. Launching new collectives on a revoked communicator returns *ncclInvalidUsage*. Calling *ncclCommFinalize* after revoke is not supported. Resource sharing via *splitShare*/*shrinkShare* is disabled when the parent communicator is revoked.

## ncclCommFinalize[](https://docs.nvidia.com#ncclcommfinalize)

-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclCommFinalize([ncclComm_t](https://docs.nvidia.com/types.html#c.ncclComm_t)comm)[](https://docs.nvidia.com#c.ncclCommFinalize)

Finalize a communicator object *comm*. When the communicator is marked as nonblocking, *ncclCommFinalize* is a
nonblocking function. Successful return from it will set communicator state as *ncclInProgress* and indicates
the communicator is under finalization where all uncompleted operations and the network-related resources are
being flushed and freed.
Once all NCCL operations are complete, the communicator will transition to the *ncclSuccess* state. Users
can query that state with *ncclCommGetAsyncError*.

This function is an intra-node collective call. When a single thread finalizes multiple ranks (multiple GPUs per thread), the calls must be grouped with *ncclGroupStart*/*ncclGroupEnd* to avoid a hang.

## ncclCommDestroy[](https://docs.nvidia.com#ncclcommdestroy)

-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclCommDestroy([ncclComm_t](https://docs.nvidia.com/types.html#c.ncclComm_t)comm)[](https://docs.nvidia.com#c.ncclCommDestroy)

Destroy a communicator object *comm*. If *ncclCommFinalize* is called by users, users should guarantee that the state
of the communicator becomes *ncclSuccess* before calling *ncclCommDestroy*. In all cases, the communicator should no
longer be accessed after *ncclCommDestroy* returns. It is recommended that users call *ncclCommFinalize* and then
*ncclCommDestroy*.

*ncclCommDestroy* will call *ncclCommFinalize* internally, unless *ncclCommFinalize* was previously called on the
communicator. If *ncclCommFinalize* was previously called on the communicator object *comm*, then *ncclCommDestroy* is a
purely local operation.

This function is an intra-node collective call, which all ranks on the same node should call to avoid a hang.

## ncclCommAbort[](https://docs.nvidia.com#ncclcommabort)

-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclCommAbort([ncclComm_t](https://docs.nvidia.com/types.html#c.ncclComm_t)comm)[](https://docs.nvidia.com#c.ncclCommAbort)

*ncclCommAbort* frees resources that are allocated to a communicator object *comm* and aborts any uncompleted
operations before destroying the communicator. All active ranks are required to call this function in order to
abort the NCCL communicator successfully. For more use cases, please check [Fault Tolerance](https://docs.nvidia.com/usage/communicators.html#ft).

## ncclCommGetAsyncError[](https://docs.nvidia.com#ncclcommgetasyncerror)

-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclCommGetAsyncError([ncclComm_t](https://docs.nvidia.com/types.html#c.ncclComm_t)comm,[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)*asyncError)[](https://docs.nvidia.com#c.ncclCommGetAsyncError)

Queries the progress and potential errors of asynchronous NCCL operations.
Operations which do not require a stream argument (e.g. ncclCommFinalize) can be considered complete as soon
as the function returns *ncclSuccess*; operations with a stream argument (e.g. ncclAllReduce) will return
*ncclSuccess* as soon as the operation is posted on the stream but may also report errors through
ncclCommGetAsyncError() until they are completed. If the return code of any NCCL function is *ncclInProgress*,
it means the operation is in the process of being enqueued in the background, and users must query the states
of the communicators until all the states become *ncclSuccess* before calling another NCCL function. Before the
states change into *ncclSuccess*, users are not allowed to issue CUDA kernel to the streams being used by NCCL.
If there has been an error on the communicator, user should destroy the communicator with [ ncclCommAbort()](https://docs.nvidia.com#c.ncclCommAbort).
If an error occurs on the communicator, nothing can be assumed about the completion or correctness of operations
enqueued on that communicator.

## ncclCommCount[](https://docs.nvidia.com#ncclcommcount)

-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclCommCount(const[ncclComm_t](https://docs.nvidia.com/types.html#c.ncclComm_t)comm, int *count)[](https://docs.nvidia.com#c.ncclCommCount)

Returns in *count* the number of ranks in the NCCL communicator *comm*.

## ncclCommCuDevice[](https://docs.nvidia.com#ncclcommcudevice)

-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclCommCuDevice(const[ncclComm_t](https://docs.nvidia.com/types.html#c.ncclComm_t)comm, int *device)[](https://docs.nvidia.com#c.ncclCommCuDevice)

Returns in *device* the CUDA device associated with the NCCL communicator *comm*.

## ncclCommUserRank[](https://docs.nvidia.com#ncclcommuserrank)

-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclCommUserRank(const[ncclComm_t](https://docs.nvidia.com/types.html#c.ncclComm_t)comm, int *rank)[](https://docs.nvidia.com#c.ncclCommUserRank)

Returns in *rank* the rank of the caller in the NCCL communicator *comm*.

## ncclCommRegister[](https://docs.nvidia.com#ncclcommregister)

-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclCommRegister(const[ncclComm_t](https://docs.nvidia.com/types.html#c.ncclComm_t)comm, void *buff, size_t size, void **handle)[](https://docs.nvidia.com#c.ncclCommRegister)

Registers the buffer *buff* with *size* under communicator *comm* for zero-copy communication; *handle* is
returned for future deregistration. See *buff* and *size* requirements and more instructions in [User Buffer Registration](https://docs.nvidia.com/usage/bufferreg.html#user-buffer-reg).

## ncclCommDeregister[](https://docs.nvidia.com#ncclcommderegister)

-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclCommDeregister(const[ncclComm_t](https://docs.nvidia.com/types.html#c.ncclComm_t)comm, void *handle)[](https://docs.nvidia.com#c.ncclCommDeregister)

Deregister buffer represented by *handle* under communicator *comm*.

## ncclCommWindowRegister[](https://docs.nvidia.com#ncclcommwindowregister)

-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclCommWindowRegister([ncclComm_t](https://docs.nvidia.com/types.html#c.ncclComm_t)comm, void *buff, size_t size,[ncclWindow_t](https://docs.nvidia.com/types.html#c.ncclWindow_t)*win, int winFlags)[](https://docs.nvidia.com#c.ncclCommWindowRegister)

Collectively register local buffer *buff* with *size* under communicator *comm* into NCCL window. Since this is a collective call,
every rank in the communicator needs to participate in the registration. Size may differ across ranks; callers are
responsible for ensuring later operations only access ranges that are valid for the ranks participating in that operation. *win* is
returned for future deregistration (if called within a group, the value may not be filled in until ncclGroupEnd() has completed).
See *buff* requirement and more instructions in [User Buffer Registration](https://docs.nvidia.com/usage/bufferreg.html#user-buffer-reg). User can also pass
different win flags to control the registration behavior. For more win flags information, please refer to [Window Registration Flags](https://docs.nvidia.com/flags.html#win-flags).
Host APIs do not accept buffers that are symmetrically registered more than once. Passing such buffers to host APIs results
in undefined behavior.

## ncclCommWindowDeregister[](https://docs.nvidia.com#ncclcommwindowderegister)

-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclCommWindowDeregister([ncclComm_t](https://docs.nvidia.com/types.html#c.ncclComm_t)comm,[ncclWindow_t](https://docs.nvidia.com/types.html#c.ncclWindow_t)win)[](https://docs.nvidia.com#c.ncclCommWindowDeregister)

Deregister NCCL window represented by *win* under communicator *comm*. Deregistration is local to the rank, and
caller needs to make sure the corresponding buffer within the window is not being accessed by any NCCL operation.

## ncclMemAlloc[](https://docs.nvidia.com#ncclmemalloc)

-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclMemAlloc(void **ptr, size_t size)[](https://docs.nvidia.com#c.ncclMemAlloc)

Allocate a GPU buffer with *size*. Allocated buffer head address will be returned by *ptr*,
and the actual allocated size can be larger than requested because of the buffer granularity
requirements from all types of NCCL optimizations.

## ncclMemFree[](https://docs.nvidia.com#ncclmemfree)

-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclMemFree(void *ptr)[](https://docs.nvidia.com#c.ncclMemFree)

Free memory allocated by *ncclMemAlloc()*.

## ncclCommSuspend[](https://docs.nvidia.com#ncclcommsuspend)

-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclCommSuspend([ncclComm_t](https://docs.nvidia.com/types.html#c.ncclComm_t)comm, int flags)[](https://docs.nvidia.com#c.ncclCommSuspend)

Suspend communicator operations to free resources. The communicator cannot be used for any NCCL operations
while suspended. There should be no outstanding NCCL operations on *comm* when this function is called.

The *flags* parameter controls which resources are released:

*NCCL_SUSPEND_MEM*(`0x01`

) – Release dynamic GPU memory allocations held by the communicator.

A suspended communicator can be restored to an active state by calling *ncclCommResume*.

## ncclCommResume[](https://docs.nvidia.com#ncclcommresume)

-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclCommResume([ncclComm_t](https://docs.nvidia.com/types.html#c.ncclComm_t)comm)[](https://docs.nvidia.com#c.ncclCommResume)

Resume all previously suspended resources on communicator *comm*. After this call returns successfully, the
communicator is fully operational and can be used for NCCL operations again.

## ncclCommMemStats[](https://docs.nvidia.com#ncclcommmemstats)

-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclCommMemStats([ncclComm_t](https://docs.nvidia.com/types.html#c.ncclComm_t)comm,[ncclCommMemStat_t](https://docs.nvidia.com/types.html#c.ncclCommMemStat_t)stat, uint64_t *value)[](https://docs.nvidia.com#c.ncclCommMemStats)

Query communicator memory statistics. The *stat* parameter selects which statistic to retrieve, and the
result is written to **value*. See [ ncclCommMemStat_t](https://docs.nvidia.com/types.html#c.ncclCommMemStat_t) for the list of available statistics.