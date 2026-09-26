source: https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/api/device_cft.html

# Device API - CFT[](https://docs.nvidia.com#device-api-cft)

## Compute Fabric Transport[](https://docs.nvidia.com#compute-fabric-transport)

Compute Fabric Transport (CFT) support is available starting with NCCL 2.31. CFT exposes CUDA fabric logical endpoints to device kernels so they can move data across a CFT-capable fabric using fabric instructions. NCCL provides the team, logical endpoint, transfer, reduction, and barrier helpers needed to use those endpoints from the Device API.

CFT is intended for systems where all participating ranks can create compatible CUDA fabric logical endpoints. Kernels that use the CFT helpers require CUDA Toolkit support for fabric PTX instructions and must be compiled for architectures that support those instructions.

## CFT Communicator Requirements[](https://docs.nvidia.com#cft-communicator-requirements)

Request CFT resources when creating the device communicator with [ ncclDevCommCreate()](https://docs.nvidia.com/device_setup.html#c.ncclDevCommCreate).

`cftCaps`

[](https://docs.nvidia.com#cftcaps)

Bitmask of

[and]`NCCL_CFT`

[values. If CFT resources are requested on a communicator where not all ranks support CFT,]`NCCL_CFT_MULTIMEM`

[fails.]`ncclDevCommCreate()`


`cftBarrierCount`

[](https://docs.nvidia.com#cftbarriercount)

Number of CFT barriers to allocate for

[. This should match the number of independently addressed barrier slots used by the kernel, commonly one per CTA with]`ncclCftBarrierSession`

`blockIdx.x`

as the barrier index.

```
ncclDevComm devComm;
ncclDevCommRequirements reqs = NCCL_DEV_COMM_REQUIREMENTS_INITIALIZER;
reqs.cftCaps = NCCL_CFT | NCCL_CFT_MULTIMEM;
reqs.cftBarrierCount = nCTAs;
NCCLCHECK(ncclDevCommCreate(comm, &reqs, &devComm));
```

Use [ NCCL_CFT](https://docs.nvidia.com#c.NCCL_CFT) to request unicast CFT logical endpoints. Use

[when the kernel also uses multicast CFT operations or multimem CFT barriers.](https://docs.nvidia.com#c.NCCL_CFT_MULTIMEM)

`NCCL_CFT_MULTIMEM`

-
NCCL_CFT_NONE
[](https://docs.nvidia.com#c.NCCL_CFT_NONE) No CFT capability is requested.


-
NCCL_CFT
[](https://docs.nvidia.com#c.NCCL_CFT) Request unicast CFT logical endpoint support.


-
NCCL_CFT_MULTIMEM
[](https://docs.nvidia.com#c.NCCL_CFT_MULTIMEM) Request multicast CFT logical endpoint support.


## CFT Teams[](https://docs.nvidia.com#cft-teams)

CFT operations may use `ncclTeam_t`

and `ncclTeam`

values to
address peers.

-
ncclTeam_t ncclTeamCft(
[ncclComm_t](https://docs.nvidia.com/types.html#c.ncclComm_t)comm,[ncclCftTeamMode_t](https://docs.nvidia.com#c.ncclCftTeamMode_t)mode)[](https://docs.nvidia.com#c.ncclTeamCft) Returns the host-side unicast CFT team containing ranks that are part of the CFT unicast group.

*comm*is the host-side communicator and*mode*is a selector used to filter the subset of CFT unicast group ranks that are part of the team (useful to build hierarchical communication patterns).

-
ncclTeam_t ncclTeamCftMultimem(
[ncclComm_t](https://docs.nvidia.com/types.html#c.ncclComm_t)comm)[](https://docs.nvidia.com#c.ncclTeamCftMultimem) Returns the host-side multicast CFT team containing all the ranks that are part of the CFT multicast group.


-
ncclTeam ncclTeamCft(ncclDevComm const &comm, ncclCftTeamMode_t mode)
[](https://docs.nvidia.com#_CPPv411ncclTeamCftRK11ncclDevComm17ncclCftTeamMode_t) Returns the device-side unicast CFT team containing ranks that are part of the CFT unicast group.

*comm*is the device-side communicator and*mode*is a selector used to filter the subset of CFT unicast group ranks that are part of the team (useful to build hierarchical communication patterns).

-
ncclTeam ncclTeamCftMultimem(ncclDevComm const &comm)
[](https://docs.nvidia.com#_CPPv419ncclTeamCftMultimemRK11ncclDevComm) Returns the device-side multicast CFT team containing all the ranks that are part of the CFT multicast group.


-
type ncclCftTeamMode_t
[](https://docs.nvidia.com#c.ncclCftTeamMode_t) Selects the CFT team layout returned by

.`ncclTeamCft()`

-
NCCL_CFT_TEAM_FLAT
[](https://docs.nvidia.com#c.ncclCftTeamMode_t.NCCL_CFT_TEAM_FLAT) Flat CFT team includes all the ranks that are part of the CFT unicast group.


-
NCCL_CFT_TEAM_HIER_MULTIMEM
[](https://docs.nvidia.com#c.ncclCftTeamMode_t.NCCL_CFT_TEAM_HIER_MULTIMEM) Hierarchical CFT team includes ranks that are part of the CFT unicast group and share the same index across different multicast CFT groups.


-
NCCL_CFT_TEAM_HIER_LSA
[](https://docs.nvidia.com#c.ncclCftTeamMode_t.NCCL_CFT_TEAM_HIER_LSA) Hierarchical CFT team includes ranks that are part of the CFT unicast group and share the same index across different LSA groups.


-
NCCL_CFT_TEAM_FLAT

## Logical Endpoint Queries[](https://docs.nvidia.com#logical-endpoint-queries)

CFT data movement routines operate on a logical endpoint ID and an offset within that endpoint. NCCL provides host-side and device-side helpers for translating registered windows and peer ranks into those values.

-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclGetCftDeviceLeInfo([ncclWindow_t](https://docs.nvidia.com/types.html#c.ncclWindow_t)window, size_t offset, int peerCft, ncclTeam_t cftTeam, ncclCftLeId *leId, size_t *leOffset)[](https://docs.nvidia.com#c.ncclGetCftDeviceLeInfo) Host-side query for the logical endpoint

*leId*and*leOffset*corresponding to*window*, byte*offset*, and*peerCft*within*cftTeam*.

-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclGetPeerDeviceLeInfo([ncclWindow_t](https://docs.nvidia.com/types.html#c.ncclWindow_t)window, size_t offset, int peerWorld, ncclCftLeId *leId, size_t *leOffset)[](https://docs.nvidia.com#c.ncclGetPeerDeviceLeInfo) Host-side query for the logical endpoint

*leId*and*leOffset*corresponding to*window*, byte*offset*and*peerWorld*within the world team.

-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclGetMultimemDeviceLeInfo([ncclWindow_t](https://docs.nvidia.com/types.html#c.ncclWindow_t)window, size_t offset, ncclCftLeId *leId, size_t *leOffset)[](https://docs.nvidia.com#c.ncclGetMultimemDeviceLeInfo) Host-side query for the multicast logical endpoint

*leId*and*leOffset*corresponding to*window*and byte*offset*.

-
void ncclGetCftLeInfo(ncclWindow_t w, size_t offset, int peerCft, ncclTeam cftTeam, ncclDevComm const &comm, ncclCftLeId *leId, size_t *leOffset)
[](https://docs.nvidia.com#_CPPv416ncclGetCftLeInfo12ncclWindow_t6size_ti8ncclTeamRK11ncclDevCommP11ncclCftLeIdP6size_t) Device-side query for the logical endpoint

*leId*and*leOffset*corresponding to*window*, byte*offset*,*peerCft*within*cftTeam*and device*comm*.

-
void ncclGetPeerLeInfo(ncclWindow_t w, size_t offset, int peerWorld, ncclDevComm const &comm, ncclCftLeId *leId, size_t *leOffset)
[](https://docs.nvidia.com#_CPPv417ncclGetPeerLeInfo12ncclWindow_t6size_tiRK11ncclDevCommP11ncclCftLeIdP6size_t) Device-side query for the logical endpoint

*leId*and*leOffset*corresponding to*window*, byte*offset*,*peerWorld*within the world team and device*comm*.

-
void ncclGetMultimemLeInfo(ncclWindow_t w, size_t offset, ncclDevComm const &comm, ncclCftLeId *leId, size_t *leOffset)
[](https://docs.nvidia.com#_CPPv421ncclGetMultimemLeInfo12ncclWindow_t6size_tRK11ncclDevCommP11ncclCftLeIdP6size_t) Device-side query for the multicast logical endpoint

*leId*and*leOffset*corresponding to*window*, byte*offset*and device*comm*.

Host-side CFT queries require the communicator to create CFT logical endpoints
before the query is issued. Set `hostCftMode`

in [ ncclConfig_t](https://docs.nvidia.com/types.html#c.ncclConfig_t) when
creating the communicator if the application needs to query CFT endpoint
information from host code before creating a CFT-enabled device communicator.

## CFT Operations[](https://docs.nvidia.com#cft-operations)

-
struct ncclCftSmem
[](https://docs.nvidia.com#_CPPv411ncclCftSmem) A user-managed shared memory state object used by

to track progress of outstanding CFT operations. The object can track a specific amount of in-flight data, limiting the number of outstanding CFT operations. Specifically, the object can track up to 16MB of non-fetching CFT operations (i.e.,`ncclCft`

`put`

,`red`

and their multicast variants) and up to 1MB of fetching CFT operations (i.e.,`get`

,`pullred`

).

-
template<typename Coop>

class ncclCft[](https://docs.nvidia.com#_CPPv4I0E7ncclCft) A class encompassing major elements of CFT support.

-
ncclCft(
[Coop](https://docs.nvidia.com#_CPPv4I0E7ncclCft)coop,[ncclCftSmem](https://docs.nvidia.com#_CPPv411ncclCftSmem)&cftSmem)[](https://docs.nvidia.com#_CPPv4N7ncclCft7ncclCftE4CoopR11ncclCftSmem) Initializes a new

`ncclCft`

object.*cftSmem*is a user-managed shared memory state used by threads in*coop*to make progress on fabric operations and to check for their completion.

-
void put(OpCoop coop, ncclCftLeId leId, size_t leOffset, void *smemSource, uint32_t bytes)
[](https://docs.nvidia.com#_CPPv4N7ncclCft3putE6OpCoop11ncclCftLeId6size_tPv8uint32_t) Initiates an asynchronous transfer of

*bytes*bytes from the shared memory buffer referenced by*smemSource*to the unicast logical endpoint referenced by*leId*at offset*leOffset*.*coop*can include a subset of the threads in the cooperative group used to create the CFT object. Cooperative groups initiating fabric operations independently under the same CFT object share its state.

-
void putCpMask(OpCoop coop, ncclCftLeId leId, size_t leOffset, void *smemSource, uint32_t bytes, uint16_t cpMask)
[](https://docs.nvidia.com#_CPPv4N7ncclCft9putCpMaskE6OpCoop11ncclCftLeId6size_tPv8uint32_t8uint16_t) Variant of

with an explicit copy mask. The copy mask is a 16-bit integer where bits correspond to the bytes of every 16-byte word being copied. A bit is set to 1 if the corresponding byte ought to be copied to the destination logical endpoint, or it is set to 0 otherwise.`ncclCft::put()`


-
void putMultimem(OpCoop coop, ncclCftLeId leId, size_t leOffset, void *smemSource, uint32_t bytes)
[](https://docs.nvidia.com#_CPPv4N7ncclCft11putMultimemE6OpCoop11ncclCftLeId6size_tPv8uint32_t) Multicast variant of

where`ncclCft::put()`

*leId*references a logical endpoint for which the thebit was set in the`NCCL_CFT_MULTIMEM`

`cftCaps`

bitmask at device communicator creation time.

-
void putMultimemCpMask(OpCoop coop, ncclCftLeId leId, size_t leOffset, void *smemSource, uint32_t bytes, uint16_t cpMask)
[](https://docs.nvidia.com#_CPPv4N7ncclCft17putMultimemCpMaskE6OpCoop11ncclCftLeId6size_tPv8uint32_t8uint16_t) Multicast variant of

with an explicit copy mask.`ncclCft::put()`


-
void get(OpCoop coop, ncclCftLeId leId, size_t leOffset, void *smemDestination, uint32_t bytes)
[](https://docs.nvidia.com#_CPPv4N7ncclCft3getE6OpCoop11ncclCftLeId6size_tPv8uint32_t) Initiates an asynchronous transfer of

*bytes*bytes from the unicast logical endpoint referenced by*leId*at offset*leOffset*to the shared memory buffer referenced by*smemDestination*.*coop*can include a subset of the threads in the cooperative group used to create the CFT object. Cooperative groups initiating fabric operations independently under the same CFT object share its state.

-
void red(OpCoop coop, ncclCftLeId leId, size_t leOffset, RedOp const &red, void *smemSource, uint32_t bytes)
[](https://docs.nvidia.com#_CPPv4N7ncclCft3redE6OpCoop11ncclCftLeId6size_tRK5RedOpPv8uint32_t) Initiates an asynchronous reduction operation (see

[Reduction Operations](https://docs.nvidia.com#cft-reduction-operators)for reduction tags and data types) for*bytes*bytes from the shared memory buffer referenced by*smemSource*to the unicast logical endpoint referenced by*leId*at offset*leOffset*.*coop*can include a subset of the threads in the cooperative group used to create the CFT object. Cooperative groups initiating fabric operations independently under the same CFT object share its state.

-
void redMultimem(OpCoop coop, ncclCftLeId leId, size_t leOffset, RedOp const &red, void *smemSource, uint32_t bytes)
[](https://docs.nvidia.com#_CPPv4N7ncclCft11redMultimemE6OpCoop11ncclCftLeId6size_tRK5RedOpPv8uint32_t) Multicast reduction variant of

where`ncclCft::red()`

*leId*references a logical endpoint for which thebit was set in the`NCCL_CFT_MULTIMEM`

`cftCaps`

bitmask at device communicator creation time.

-
void pullRed(OpCoop coop, ncclCftLeId leId, size_t leOffset, RedOp const &red, void *smemDestination, uint32_t bytes)
[](https://docs.nvidia.com#_CPPv4N7ncclCft7pullRedE6OpCoop11ncclCftLeId6size_tRK5RedOpPv8uint32_t) Initiates an asynchronous reduction operation (see

[Reduction Operations](https://docs.nvidia.com#cft-reduction-operators)for reduction tags and data types) for*bytes*bytes from the multicast logical endpoint referenced by*leId*at offset*leOffset*to the shared memory buffer referenced by*smemDestination*.*leId*references a logical endpoint for which thebit was set in the`NCCL_CFT_MULTIMEM`

`cftCaps`

bitmask at device communicator creation time.*coop*must be ncclCoopWarp.

-
void submit(OpCoop coop)
[](https://docs.nvidia.com#_CPPv4N7ncclCft6submitE6OpCoop) Submits previously initiated CFT operations for all the threads in

*coop*, allowing them to make forward progress. Every cooperative group (`OpCoop`

) that initiated fabric operations must call submit beforeand`ncclCft::flushSmem()`

.`ncclCft::flush()`


-
void flushSmem(OpCoop coop)
[](https://docs.nvidia.com#_CPPv4N7ncclCft9flushSmemE6OpCoop) Makes all the threads in

*coop*wait for CFT operations that consume shared memory data. All the shared memory buffers that source data to outstanding fabric operations can be reused after the function returns. Users can call this function to wait for shared memory buffers to be consumed by previously initiated CFT operations before initiating new ones, and callonly when they need to wait for the completion of all the outstanding CFT operations, e.g., because they reached the number of in-flight bytes that the CFT shared memory state object can track.`ncclCft::flush()`


-
void flush(OpCoop coop, bool *hasReport = nullptr, uint32_t *report = nullptr)
[](https://docs.nvidia.com#_CPPv4N7ncclCft5flushE6OpCoopPbP8uint32_t) Flushes outstanding CFT operations for all the threads in

*coop*and waits for their completion. When flush returns shared memory buffers are safe to reuse.*coop*must include the threads of all cooperative groups that initiated fabric operations under the same CFT object. No other cooperative group can initiate fabric operations until flush has completed. If the operation succeeds*hasReport*is set to false and*report*is not modified. If the operation fails*hasReport*is set to`true`

and*report*is set to an error code that can be decoded via the`cudaFabricOpErrorStatusGet/Count`

.

-
ncclCft(

`smemSource`

and `smemDestination`

pointers must be 16-byte aligned, and `bytes`

must be a multiple of 16.
CFT operates on shared memory; a typical kernel stages data through shared memory, issues one or more operations,
then calls [ ncclCft::submit()](https://docs.nvidia.com#_CPPv4N7ncclCft6submitE6OpCoop) and

[or](https://docs.nvidia.com#_CPPv4N7ncclCft5flushE6OpCoopPbP8uint32_t)

`ncclCft::flush()`

[as required by the reuse and ordering rules of the kernel.](https://docs.nvidia.com#_CPPv4N7ncclCft9flushSmemE6OpCoop)

`ncclCft::flushSmem()`

## Reduction Operations[](https://docs.nvidia.com#reduction-operations)

Reduction fabric operations use operation tag types:

-
struct ncclCftOpSum
[](https://docs.nvidia.com#_CPPv412ncclCftOpSum)

-
struct ncclCftOpAnd
[](https://docs.nvidia.com#_CPPv412ncclCftOpAnd)

-
struct ncclCftOpXor
[](https://docs.nvidia.com#_CPPv412ncclCftOpXor)

-
struct ncclCftOpOr
[](https://docs.nvidia.com#_CPPv411ncclCftOpOr)

-
struct ncclCftOpMin
[](https://docs.nvidia.com#_CPPv412ncclCftOpMin)

-
struct ncclCftOpMax
[](https://docs.nvidia.com#_CPPv412ncclCftOpMax)

Refer to CFT PTX documentation for supported reductions and data types.

## CFT Barriers[](https://docs.nvidia.com#cft-barriers)

Applications request CFT barrier resources with `cftBarrierCount`

in
[ ncclDevCommRequirements](https://docs.nvidia.com/device_setup.html#c.ncclDevCommRequirements), then use

[from device code. The barrier count should cover every barrier index used by the kernel.](https://docs.nvidia.com#_CPPv4I0E21ncclCftBarrierSession)

`ncclCftBarrierSession`

-
template<typename Coop>

class ncclCftBarrierSession[](https://docs.nvidia.com#_CPPv4I0E21ncclCftBarrierSession) A CFT-backed barrier session.

-
ncclCftBarrierSession(
[Coop](https://docs.nvidia.com#_CPPv4I0E21ncclCftBarrierSession)coop, ncclDevComm const &comm, uint32_t index, bool multimem = false)[](https://docs.nvidia.com#_CPPv4N21ncclCftBarrierSession21ncclCftBarrierSessionE4CoopRK11ncclDevComm8uint32_tb) Initializes a new CFT barrier session.

*coop*represents a cooperative group (see[Thread Groups](https://docs.nvidia.com/usage/deviceapi.html#devapi-coops)) of threads that synchronize throught the barrier.*comm*is the device communicator for which barrier resources were requested.*index*selects the barrier slot from the device communicator.*multimem*can be set to`true`

to select multicast CFT barrier resources (requires CFT barriers to be created withcapability).`NCCL_CFT_MULTIMEM`


-
void arrive(
[Coop](https://docs.nvidia.com#_CPPv4I0E21ncclCftBarrierSession)coop, cuda::memory_order order,[ncclMemProxyType](https://docs.nvidia.com#_CPPv416ncclMemProxyType)producer,[ncclMemProxyType](https://docs.nvidia.com#_CPPv416ncclMemProxyType)consumer)[](https://docs.nvidia.com#_CPPv4N21ncclCftBarrierSession6arriveE4CoopN4cuda12memory_orderE16ncclMemProxyType16ncclMemProxyType) Signals arrival at the barrier.

*order*dictates the semantics used to order memory accesses from different proxies around the barrier.*producer*indicates the type of proxy that stored the data into global memory.*consumer*indicates the type of proxy that will be loading the*producer*data from global memory.

-
void wait(
[Coop](https://docs.nvidia.com#_CPPv4I0E21ncclCftBarrierSession)coop, cuda::memory_order order,[ncclMemProxyType](https://docs.nvidia.com#_CPPv416ncclMemProxyType)producer,[ncclMemProxyType](https://docs.nvidia.com#_CPPv416ncclMemProxyType)consumer)[](https://docs.nvidia.com#_CPPv4N21ncclCftBarrierSession4waitE4CoopN4cuda12memory_orderE16ncclMemProxyType16ncclMemProxyType) Waits for the barrier to complete. It can be used to establish a

`happens-before`

relationship between*producer*and*consumer*when*order*complements the memory ordering semantics of the matching.`ncclCftBarrierSession::arrive()`


-
void sync(
[Coop](https://docs.nvidia.com#_CPPv4I0E21ncclCftBarrierSession)coop, cuda::memory_order order,[ncclMemProxyType](https://docs.nvidia.com#_CPPv416ncclMemProxyType)producer,[ncclMemProxyType](https://docs.nvidia.com#_CPPv416ncclMemProxyType)consumer)[](https://docs.nvidia.com#_CPPv4N21ncclCftBarrierSession4syncE4CoopN4cuda12memory_orderE16ncclMemProxyType16ncclMemProxyType) Combines

and`ncclCftBarrierSession::arrive()`

.`ncclCftBarrierSession::wait()`


-
ncclResult_t wait(
[Coop](https://docs.nvidia.com#_CPPv4I0E21ncclCftBarrierSession)coop, cuda::memory_order order,[ncclMemProxyType](https://docs.nvidia.com#_CPPv416ncclMemProxyType)producer,[ncclMemProxyType](https://docs.nvidia.com#_CPPv416ncclMemProxyType)consumer, uint64_t timeoutCycles)[](https://docs.nvidia.com#_CPPv4N21ncclCftBarrierSession4waitE4CoopN4cuda12memory_orderE16ncclMemProxyType16ncclMemProxyType8uint64_t)

-
ncclResult_t sync(
[Coop](https://docs.nvidia.com#_CPPv4I0E21ncclCftBarrierSession)coop, cuda::memory_order order,[ncclMemProxyType](https://docs.nvidia.com#_CPPv416ncclMemProxyType)producer,[ncclMemProxyType](https://docs.nvidia.com#_CPPv416ncclMemProxyType)consumer, uint64_t timeoutCycles)[](https://docs.nvidia.com#_CPPv4N21ncclCftBarrierSession4syncE4CoopN4cuda12memory_orderE16ncclMemProxyType16ncclMemProxyType8uint64_t) Timeout-returning variants of

and`ncclCftBarrierSession::wait()`

.`ncclCftBarrierSession::sync()`


-
ncclCftBarrierSession(

-
void ncclMemFence(Coop coop, cuda::memory_order order,
[ncclMemProxyType](https://docs.nvidia.com#_CPPv416ncclMemProxyType)producer,[ncclMemProxyType](https://docs.nvidia.com#_CPPv416ncclMemProxyType)consumer,[ncclMemFenceScope](https://docs.nvidia.com#_CPPv417ncclMemFenceScope)scope)[](https://docs.nvidia.com#_CPPv412ncclMemFence4CoopN4cuda12memory_orderE16ncclMemProxyType16ncclMemProxyType17ncclMemFenceScope) Issues a memory fence between producer and consumer proxy domains for the participating threads.

*coop*represents a cooperative group of threads which memory accesses are ordered around the fence.*order*dictates the semantics used to order memory accesses from different proxies around the fence.*producer*indicates the type of proxy that stored the data into memory.*consumer*indicates the type of proxy that will be loading the*producer*data from memory.*scope*indicates the point of consistency for the memory accesses around the fence.