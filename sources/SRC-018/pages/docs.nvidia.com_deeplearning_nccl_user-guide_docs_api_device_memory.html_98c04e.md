source: https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/api/device_memory.html

# Device API – Memory and LSA[](https://docs.nvidia.com#device-api-memory-and-lsa)

This page documents device-side memory and LSA (load/store accessible) functionality. For host-accessible device
pointer functions, see [Host-Accessible Device Pointer Functions](https://docs.nvidia.com/device_setup.html#device-api-host-functions) in the setup guide.

## LSA[](https://docs.nvidia.com#lsa)

**Device functions.** The following are callable from device (GPU) code only. LSA is used by the pointer accessors
below.

### ncclLsaBarrierSession[](https://docs.nvidia.com#nccllsabarriersession)

-
template<typename Coop>

class ncclLsaBarrierSession[](https://docs.nvidia.com#_CPPv4I0E21ncclLsaBarrierSession) A class representing a memory barrier session.

-
ncclLsaBarrierSession(
[Coop](https://docs.nvidia.com#_CPPv4I0E21ncclLsaBarrierSession)coop, ncclDevComm const &comm, ncclTeamTagLsa tag, uint32_t index, bool multimem = false)[](https://docs.nvidia.com#_CPPv4N21ncclLsaBarrierSession21ncclLsaBarrierSessionE4CoopRK11ncclDevComm14ncclTeamTagLsa8uint32_tb) Initializes a new memory barrier session.

*coop*represents a cooperative group (see[Thread Groups](https://docs.nvidia.com/usage/deviceapi.html#devapi-coops)).*comm*is the device communicator created using.`ncclDevCommCreate()`

*ncclTeamTagLsa*is here to indicate which subset of ranks the barrier will apply to. The identifier of the underlying barrier to use is provided by*index*(it should be different for each*coop*; typically set to`blockIdx.x`

to ensure uniqueness between CTAs).*multimem*requests a hardware-accelerated implementation using memory multicast.

-
void arrive(
[Coop](https://docs.nvidia.com#_CPPv4I0E21ncclLsaBarrierSession), cuda::memory_order order)[](https://docs.nvidia.com#_CPPv4N21ncclLsaBarrierSession6arriveE4CoopN4cuda12memory_orderE) Signals the arrival of the thread at the barrier session.


-
ncclLsaBarrierSession(

### ncclGetPeerPointer[](https://docs.nvidia.com#ncclgetpeerpointer)

-
void *ncclGetPeerPointer(ncclWindow_t w, size_t offset, int peer)
[](https://docs.nvidia.com#_CPPv418ncclGetPeerPointer12ncclWindow_t6size_ti) Returns a load/store accessible pointer to the memory buffer of device

*peer*within the window*w*.*offset*is byte-based.*peer*is a rank index within the world team (see[Teams](https://docs.nvidia.com/usage/deviceapi.html#devapi-teams)). This function will return NULL if the*peer*is not within the[LSA](https://docs.nvidia.com/usage/bufferreg.html#device-api-lsa)team.

### ncclGetLsaPointer[](https://docs.nvidia.com#ncclgetlsapointer)

-
void *ncclGetLsaPointer(ncclWindow_t w, size_t offset, int lsaPeer)
[](https://docs.nvidia.com#_CPPv417ncclGetLsaPointer12ncclWindow_t6size_ti) Returns a load/store accessible pointer to the memory buffer of device

*lsaPeer*within the window*w*.*offset*is byte-based. This is similar to`ncclGetPeerPointer`

, but here*lsaPeer*is a rank index within the[LSA](https://docs.nvidia.com/usage/bufferreg.html#device-api-lsa)team (see[Teams](https://docs.nvidia.com/usage/deviceapi.html#devapi-teams)). For high-level reduce and copy operations over LSA memory, see[Device API – Remote Reduce and Copy: Building Blocks for Custom Communication Kernels](https://docs.nvidia.com/device_reducecopy.html#device-api-reducecopy).

### ncclGetLocalPointer[](https://docs.nvidia.com#ncclgetlocalpointer)

-
void *ncclGetLocalPointer(ncclWindow_t w, size_t offset)
[](https://docs.nvidia.com#_CPPv419ncclGetLocalPointer12ncclWindow_t6size_t) Returns a load-store accessible pointer to the memory buffer of the current device within the window

*w*.*offset*is byte-based. This is just a shortcut version of`ncclGetPeerPointer`

with*devComm.rank*as*peer*, or`ncclGetLsaPointer`

with*devComm.lsaRank*as*lsaPeer*.

## Multimem[](https://docs.nvidia.com#multimem)

### ncclGetLsaMultimemPointer[](https://docs.nvidia.com#ncclgetlsamultimempointer)

-
void *ncclGetLsaMultimemPointer(ncclWindow_t w, size_t offset, ncclDevComm const &devComm)
[](https://docs.nvidia.com#_CPPv425ncclGetLsaMultimemPointer12ncclWindow_t6size_tRK11ncclDevComm) Returns a multicast memory pointer associated with the window

*w*and device communicator*devComm*.*offset*is byte-based. Availability of multicast memory is hardware-dependent. Currently unsupported for memory regions that contain host-backed segments (CU_MEM_LOCATION_TYPE_HOST_NUMA).