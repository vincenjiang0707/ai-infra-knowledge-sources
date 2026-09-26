source: https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/api/device_setup.html

# Device API – Host-Side Setup[](https://docs.nvidia.com#device-api-host-side-setup)

## Host-Side Setup[](https://docs.nvidia.com#host-side-setup)

**Host functions and types.** The following are for use in host code: creating and destroying device communicators,
querying properties, and the requirement and property types. The [ ncclDevComm](https://docs.nvidia.com#c.ncclDevComm) structure is then passed to
device code.

### ncclDevComm[](https://docs.nvidia.com#nccldevcomm)

-
type ncclDevComm
[](https://docs.nvidia.com#c.ncclDevComm) A structure describing a device communicator, as created on the host side using

. The structure is used primarily on the device side. In general, fields in this struct are considered internal and should not be accessed by users. An exception is made for the following fields, which are guaranteed to be stable across NCCL versions:`ncclDevCommCreate()`

-
int rank
[](https://docs.nvidia.com#c.ncclDevComm.rank) The rank within the communicator.


-
int nRanks
[](https://docs.nvidia.com#c.ncclDevComm.nRanks) The size of the communicator.


-
int lsaRank
[](https://docs.nvidia.com#c.ncclDevComm.lsaRank)

-
int rank

### ncclDevCommCreate[](https://docs.nvidia.com#nccldevcommcreate)

-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclDevCommCreate([ncclComm_t](https://docs.nvidia.com/types.html#c.ncclComm_t)comm, struct[ncclDevCommRequirements](https://docs.nvidia.com#c.ncclDevCommRequirements)const *reqs, struct[ncclDevComm](https://docs.nvidia.com#c.ncclDevComm)*outDevComm)[](https://docs.nvidia.com#c.ncclDevCommCreate) Creates a new device communicator (see

) corresponding to the supplied host-side communicator`ncclDevComm`

*comm*. The result is returned in the*outDevComm*buffer (which needs to be supplied by the caller). The caller needs to also provide a filled-in list of requirements via the*reqs*argument (see); the function will allocate any necessary resources to meet them. It is recommended to call`ncclDevCommRequirements`

before calling the function; the function will fail if the specified requirements are not supported. Since this is a collective call, every rank in the communicator needs to participate. If called within a group,`ncclCommQueryProperties()`

*outDevComm*may not be filled in until`ncclGroupEnd()`

has completed.Note that this is a

*host-side*function.

### ncclDevCommDestroy[](https://docs.nvidia.com#nccldevcommdestroy)

-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclDevCommDestroy([ncclComm_t](https://docs.nvidia.com/types.html#c.ncclComm_t)comm, struct[ncclDevComm](https://docs.nvidia.com#c.ncclDevComm)const *devComm)[](https://docs.nvidia.com#c.ncclDevCommDestroy) Destroys a device communicator (see

) previously created using`ncclDevComm`

and releases any allocated resources. The caller must ensure that no device kernel that uses this device communicator could be running at the time this function is invoked.`ncclDevCommCreate()`

Note that this is a

*host-side*function.

### ncclDevCommRequirements[](https://docs.nvidia.com#nccldevcommrequirements)

-
type ncclDevCommRequirements
[](https://docs.nvidia.com#c.ncclDevCommRequirements) A host-side structure specifying the list of requirements when creating device communicators (see

). Since NCCL 2.29, this struct must be initialized using`ncclDevComm`

`NCCL_DEV_COMM_REQUIREMENTS_INITIALIZER`

.-
int lsaBarrierCount
[](https://docs.nvidia.com#c.ncclDevCommRequirements.lsaBarrierCount) Specifies the number of memory barriers to allocate (see

). These barriers are necessary to write fused kernel and may be required by building blocks such as those in`ncclLsaBarrierSession`

[Device API – Remote Reduce and Copy: Building Blocks for Custom Communication Kernels](https://docs.nvidia.com/device_reducecopy.html#device-api-reducecopy).

-
int railGinBarrierCount
[](https://docs.nvidia.com#c.ncclDevCommRequirements.railGinBarrierCount) Specifies the number of railed network barriers to allocate (see

; available since NCCL 2.28.7).`ncclGinBarrierSession`


-
int barrierCount
[](https://docs.nvidia.com#c.ncclDevCommRequirements.barrierCount) Specifies the number of network/rail hybrid barriers to allocate (see

; available since NCCL 2.28.7).`ncclBarrierSession`


-
int ginSignalCount
[](https://docs.nvidia.com#c.ncclDevCommRequirements.ginSignalCount) Specifies the number of network signals to allocate (see

; available since NCCL 2.28.7).`ncclGinSignal_t`


-
int ginCounterCount
[](https://docs.nvidia.com#c.ncclDevCommRequirements.ginCounterCount) Specifies the number of network counters to allocate (see

; available since NCCL 2.28.7).`ncclGinCounter_t`


-
bool ginForceEnable
[](https://docs.nvidia.com#c.ncclDevCommRequirements.ginForceEnable) **Deprecated.**Forces GIN (GPU-Initiated Networking) support to be enabled by automatically setting`ginConnectionType`

to. This field is deprecated in favor of explicitly setting`NCCL_GIN_CONNECTION_FULL`

to the desired value. When set to`ginConnectionType`

`true`

, it overrides the`ginConnectionType`

field. New code should usedirectly instead of this field. Available since NCCL 2.28.7, deprecated since NCCL 2.29.7.`ginConnectionType`


-
[ncclGinConnectionType_t](https://docs.nvidia.com#c.ncclGinConnectionType_t)ginConnectionType[](https://docs.nvidia.com#c.ncclDevCommRequirements.ginConnectionType) Specifies the type of GIN connection to establish (see

). If GIN resources are requested (e.g.,`ncclGinConnectionType_t`

`ginSignalCount`

,`ginCounterCount`

,`barrierCount`

, or`railGinBarrierCount`

) while this field is, device communicator creation fails with`NCCL_GIN_CONNECTION_NONE`

`ncclInvalidArgument`

. Available since NCCL 2.29.7.

-
int ginCustomStride
[](https://docs.nvidia.com#c.ncclDevCommRequirements.ginCustomStride) Specifies the rank stride when

is`ginConnectionType`

. Available since NCCL 2.31.`NCCL_GIN_CONNECTION_CUSTOM_STRIDE`


-
ncclDevResourceRequirements_t *resourceRequirementsList
[](https://docs.nvidia.com#c.ncclDevCommRequirements.resourceRequirementsList) Specifies a list of resource requirements. This is best set to NULL for now.


-
ncclTeamRequirements_t *teamRequirementsList
[](https://docs.nvidia.com#c.ncclDevCommRequirements.teamRequirementsList) Specifies a list of requirements for particular teams. This is best set to NULL for now.


-
int ginTrafficClass
[](https://docs.nvidia.com#c.ncclDevCommRequirements.ginTrafficClass) Specifies the GIN traffic class. See

[Quality of Service](https://docs.nvidia.com/usage/communicators.html#communicators-qos)for more details. Available since NCCL 2.30.3.

-
int worldGinBarrierCount
[](https://docs.nvidia.com#c.ncclDevCommRequirements.worldGinBarrierCount) Specifies the number of world network barriers to allocate. Available since NCCL 2.30.3.


-
bool ginStrongSignalsRequired
[](https://docs.nvidia.com#c.ncclDevCommRequirements.ginStrongSignalsRequired) Specifies whether GIN strong signals are required. Set to false if kernels using this communicator will not use strong signal operations (such as

and`ncclGin_StrongSignalInc`

). Default is true. Available since NCCL 2.30.5.`ncclGin_StrongVASignalAdd`


-
bool ginVaSignalsRequired
[](https://docs.nvidia.com#c.ncclDevCommRequirements.ginVaSignalsRequired) Specifies whether GIN VA signals are required. Set to false if kernels using this communicator do not use GIN VA signals (such as

and`ncclGin_WeakVASignalInc`

). Default is true. Available since NCCL 2.30.5.`ncclGin_StrongVASignalAdd`


-
int cftCaps
[](https://docs.nvidia.com#c.ncclDevCommRequirements.cftCaps) Bitmask of CFT capabilities requested for the device communicator (see

[Device API - CFT](https://docs.nvidia.com/device_cft.html#device-api-cft)). Setfor unicast CFT logical endpoint support,`NCCL_CFT`

for multicast CFT support,`NCCL_CFT_MULTIMEM`

for no CFT support (default). Available since NCCL 2.31.`NCCL_CFT_NONE`


-
int cftBarrierCount
[](https://docs.nvidia.com#c.ncclDevCommRequirements.cftBarrierCount) Specifies the number of CFT barriers to allocate (see

). Available since NCCL 2.31.`ncclCftBarrierSession`


-
int lsaBarrierCount

### ncclCommQueryProperties[](https://docs.nvidia.com#ncclcommqueryproperties)

-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclCommQueryProperties([ncclComm_t](https://docs.nvidia.com/types.html#c.ncclComm_t)comm,[ncclCommProperties_t](https://docs.nvidia.com#c.ncclCommProperties_t)*props)[](https://docs.nvidia.com#c.ncclCommQueryProperties) Exposes communicator properties by filling in

*props*. Before calling this function,*props*must be initialized using`NCCL_COMM_PROPERTIES_INITIALIZER`

. Introduced in NCCL 2.29.Note that this is a

*host-side*function.

### ncclCommProperties_t[](https://docs.nvidia.com#ncclcommproperties-t)

-
type ncclCommProperties_t
[](https://docs.nvidia.com#c.ncclCommProperties_t) A structure describing the properties of the communicator. Introduced in NCCL 2.29. Properties include:

-
int rank
[](https://docs.nvidia.com#c.ncclCommProperties_t.rank) Rank within the communicator.


-
int nRanks
[](https://docs.nvidia.com#c.ncclCommProperties_t.nRanks) Size of the communicator.


-
int cudaDev
[](https://docs.nvidia.com#c.ncclCommProperties_t.cudaDev) CUDA device index.


-
int nvmlDev
[](https://docs.nvidia.com#c.ncclCommProperties_t.nvmlDev) NVML device index.


-
bool deviceApiSupport
[](https://docs.nvidia.com#c.ncclCommProperties_t.deviceApiSupport) Whether the device API is supported. If false, a

cannot be created.`ncclDevComm`


-
bool multimemSupport
[](https://docs.nvidia.com#c.ncclCommProperties_t.multimemSupport) Whether ranks in the same

[LSA](https://docs.nvidia.com/usage/bufferreg.html#device-api-lsa)team can communicate using multimem. If false, acannot be created with multimem resources.`ncclDevComm`


-
[ncclGinType_t](https://docs.nvidia.com#c.ncclGinType_t)ginType[](https://docs.nvidia.com#c.ncclCommProperties_t.ginType) The GIN type supported by the communicator. If equal to

, a`NCCL_GIN_TYPE_NONE`

cannot be created with GIN connection type`ncclDevComm`

.`NCCL_GIN_CONNECTION_FULL`


-
[ncclGinType_t](https://docs.nvidia.com#c.ncclGinType_t)railedGinType[](https://docs.nvidia.com#c.ncclCommProperties_t.railedGinType) The railed GIN type supported by the communicator. If equal to

, a`NCCL_GIN_TYPE_NONE`

cannot be created with GIN connection type`ncclDevComm`

. Available since NCCL 2.29.7.`NCCL_GIN_CONNECTION_RAIL`


-
uint64_t commHash
[](https://docs.nvidia.com#c.ncclCommProperties_t.commHash) Communicator hash identifier shared across all ranks in the communicator. Available since NCCL 2.31.


-
int ginMinStride
[](https://docs.nvidia.com#c.ncclCommProperties_t.ginMinStride) The minimum value allowed for

`ginCustomStride`

. This value is based on the network connectivity. For example, when[NCCL_CROSS_NIC](https://docs.nvidia.com/env.html#env-nccl-cross-nic)is`0`

,`ginMinStride`

is increased so that strides spanning rail boundaries are not possible.`ginMinStride`

is`INT_MAX`

if GIN connectivity does not follow a uniform stride pattern, in which casecannot be used. Available since NCCL 2.31.`NCCL_GIN_CONNECTION_CUSTOM_STRIDE`


-
int rank

### ncclGinType_t[](https://docs.nvidia.com#ncclgintype-t)

-
enum ncclGinType_t
[](https://docs.nvidia.com#c.ncclGinType_t) GIN type. Communication between different GIN types is not supported. Possible values include:

-
enumerator NCCL_GIN_TYPE_NONE
[](https://docs.nvidia.com#c.ncclGinType_t.NCCL_GIN_TYPE_NONE) GIN is not supported.


-
enumerator NCCL_GIN_TYPE_PROXY
[](https://docs.nvidia.com#c.ncclGinType_t.NCCL_GIN_TYPE_PROXY) Host Proxy GIN type.


-
enumerator NCCL_GIN_TYPE_GDAKI
[](https://docs.nvidia.com#c.ncclGinType_t.NCCL_GIN_TYPE_GDAKI) GPUDirect Async Kernel-Initiated (GDAKI) GIN type.


-
enumerator NCCL_GIN_TYPE_GPI
[](https://docs.nvidia.com#c.ncclGinType_t.NCCL_GIN_TYPE_GPI) GPU-Push Interface (GPI) GIN type. Requires SpectrumX - see

[SpectrumX documentation](https://networking-docs.nvidia.com/hpcxum/2.51/spectrum-x-nccl-plugin#GPU-Initiated-Networking-(GIN))for details. Added as an experimental feature in NCCL 2.30.6.

-
enumerator NCCL_GIN_TYPE_EFA_GDA
[](https://docs.nvidia.com#c.ncclGinType_t.NCCL_GIN_TYPE_EFA_GDA) AWS EFA GPUDirect Async (GDA) GIN type. Requires the AWS OFI plugin for NCCL - see AWS EFA

[documentation](https://github.com/aws/aws-ofi-nccl)and[getting started guide](https://github.com/aws/aws-ofi-nccl/blob/master/doc/gin-getting-started.md)for details. Available since NCCL 2.31.

-
enumerator NCCL_GIN_TYPE_NONE

### ncclGinConnectionType_t[](https://docs.nvidia.com#ncclginconnectiontype-t)

-
enum ncclGinConnectionType_t
[](https://docs.nvidia.com#c.ncclGinConnectionType_t) Specifies the type of GIN connection for device communicators. This enum controls whether GIN (GPU-Initiated Networking) resources should be allocated and what connection type to use. Used in

when creating device communicators. Available since NCCL 2.29.7.`ncclDevCommRequirements`

-
enumerator NCCL_GIN_CONNECTION_NONE
[](https://docs.nvidia.com#c.ncclGinConnectionType_t.NCCL_GIN_CONNECTION_NONE) No GIN connectivity.


-
enumerator NCCL_GIN_CONNECTION_FULL
[](https://docs.nvidia.com#c.ncclGinConnectionType_t.NCCL_GIN_CONNECTION_FULL) Full GIN connectivity. Each rank is connected to all other ranks.


-
enumerator NCCL_GIN_CONNECTION_RAIL
[](https://docs.nvidia.com#c.ncclGinConnectionType_t.NCCL_GIN_CONNECTION_RAIL) Railed GIN connectivity. Each rank is connected to other ranks in the same rail team.


-
enumerator NCCL_GIN_CONNECTION_CUSTOM_STRIDE
[](https://docs.nvidia.com#c.ncclGinConnectionType_t.NCCL_GIN_CONNECTION_CUSTOM_STRIDE) Strided GIN connectivity. Each rank is connected to other ranks separated by a fixed stride. Available since NCCL 2.31.


-
enumerator NCCL_GIN_CONNECTION_NONE

## Host-Accessible Device Pointer Functions[](https://docs.nvidia.com#host-accessible-device-pointer-functions)

**Host functions.** The following are callable from host code only. They provide host-side access to device pointer
functionality, enabling host code to obtain pointers to [LSA](https://docs.nvidia.com/usage/bufferreg.html#device-api-lsa) memory regions.

All functions return `ncclResult_t`

error codes. On success, `ncclSuccess`

is returned.
On failure, appropriate error codes are returned (e.g., `ncclInvalidArgument`

for invalid parameters,
`ncclInternalError`

for internal failures), unless otherwise specified.

The returned pointers are valid for the lifetime of the window. Pointers should not be used after either the window or communicator is destroyed. Obtained pointers are device pointers.

### ncclGetLsaMultimemDevicePointer[](https://docs.nvidia.com#ncclgetlsamultimemdevicepointer)

-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclGetLsaMultimemDevicePointer([ncclWindow_t](https://docs.nvidia.com/types.html#c.ncclWindow_t)window, size_t offset, void **outPtr)[](https://docs.nvidia.com#c.ncclGetLsaMultimemDevicePointer) Returns a multimem base pointer for the

[LSA](https://docs.nvidia.com/usage/bufferreg.html#device-api-lsa)team associated with the given window. This function provides host-side access to the multimem memory functionality.*window*is the NCCL window object (must not be NULL).*offset*is the byte offset within the window.*outPtr*is the output parameter for the multimem pointer (must not be NULL).This function requires

[LSA](https://docs.nvidia.com/usage/bufferreg.html#device-api-lsa)multimem support (multicast capability on the system). The window must be registered with a communicator that supports symmetric memory, and the hardware must support NVLink SHARP multicast functionality.Note

If the system does not support multimem, the function returns

`ncclSuccess`

with`*outPtr`

set to`nullptr`

. This allows applications to gracefully detect and handle the absence of multimem support without breaking the communicator. Users should check if the returned pointer is`nullptr`

to determine availability.Example:

void* multimemPtr; ncclResult_t result = ncclGetLsaMultimemDevicePointer(window, 0, &multimemPtr); if (result == ncclSuccess) { if (multimemPtr != nullptr) { // Use multimemPtr for multimem operations } else { // Multimem not supported, use fallback approach } }


### ncclGetMultimemDevicePointer[](https://docs.nvidia.com#ncclgetmultimemdevicepointer)

-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclGetMultimemDevicePointer([ncclWindow_t](https://docs.nvidia.com/types.html#c.ncclWindow_t)window, size_t offset, ncclMultimemHandle multimem, void **outPtr)[](https://docs.nvidia.com#c.ncclGetMultimemDevicePointer) Returns a multimem base pointer using a provided multimem handle instead of the window’s internal multimem. This function enables using external or custom multimem handles for pointer calculation.

*window*is the NCCL window object (must not be NULL).*offset*is the byte offset within the window.*multimem*is the multimem handle containing the multimem base pointer (multimem.mcBasePtr must not be NULL).*outPtr*is the output parameter for the multimem pointer (must not be NULL).This function requires

[LSA](https://docs.nvidia.com/usage/bufferreg.html#device-api-lsa)multimem support (multicast capability on the system).Note

If the system does not support multimem, the function returns

`ncclSuccess`

with`*outPtr`

set to`nullptr`

. The function validates that`multimem.mcBasePtr`

is not nullptr before proceeding.Example:

// Get multimem handle from device communicator setup ncclMultimemHandle customHandle; // ... (obtain handle) void* multimemPtr; ncclResult_t result = ncclGetMultimemDevicePointer(window, 0, customHandle, &multimemPtr); if (result == ncclSuccess) { if (multimemPtr != nullptr) { // Use multimemPtr for multimem operations with custom handle } else { // Multimem not supported, use fallback approach } }


### ncclGetLsaDevicePointer[](https://docs.nvidia.com#ncclgetlsadevicepointer)

-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclGetLsaDevicePointer([ncclWindow_t](https://docs.nvidia.com/types.html#c.ncclWindow_t)window, size_t offset, int lsaRank, void **outPtr)[](https://docs.nvidia.com#c.ncclGetLsaDevicePointer) Returns a load/store accessible pointer to the memory buffer of a specific

[LSA](https://docs.nvidia.com/usage/bufferreg.html#device-api-lsa)peer within the window. This function provides host-side access to LSA pointer functionality using LSA rank directly.*window*is the NCCL window object (must not be NULL).*offset*is the byte offset within the window (must be >= 0 and < window size).*lsaRank*is the LSA rank of the target peer (must be >= 0 and < LSA team size).*outPtr*is the output parameter for the LSA pointer (must not be NULL).On success,

`ncclSuccess`

is returned and the LSA pointer is returned in`outPtr`

.The window must be registered with a communicator that supports LSA. The LSA rank must be within the valid range for the LSA team, and the target peer must be load/store accessible (P2P connectivity required).

Example:

void* lsaPtr; ncclResult_t result = ncclGetLsaDevicePointer(window, 0, 1, &lsaPtr); if (result == ncclSuccess) { // Use lsaPtr to access LSA peer 1's memory }


### ncclGetPeerDevicePointer[](https://docs.nvidia.com#ncclgetpeerdevicepointer)

-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclGetPeerDevicePointer([ncclWindow_t](https://docs.nvidia.com/types.html#c.ncclWindow_t)window, size_t offset, int peer, void **outPtr)[](https://docs.nvidia.com#c.ncclGetPeerDevicePointer) Returns a load/store accessible pointer to the memory buffer of a specific world rank peer within the window. This function converts world rank to

[LSA](https://docs.nvidia.com/usage/bufferreg.html#device-api-lsa)rank internally and provides host-side access to peer pointer functionality.*window*is the NCCL window object (must not be NULL).*offset*is the byte offset within the window.*peer*is the world rank of the target peer (must be >= 0 and < communicator size).*outPtr*is the output parameter for the peer pointer (must not be NULL).On success,

`ncclSuccess`

is returned and the peer pointer is returned in`outPtr`

.If the peer is not reachable via

[LSA](https://docs.nvidia.com/usage/bufferreg.html#device-api-lsa)(not in LSA team),`outPtr`

is set to NULL and`ncclSuccess`

is returned. This matches the behavior of the device-side`ncclGetPeerPointer`

function.The window must be registered with a communicator that supports LSA. The peer rank must be within the valid range for the communicator, and the target peer must be load/store accessible (P2P connectivity required).

Example:

void* peerPtr; ncclResult_t result = ncclGetPeerDevicePointer(window, 0, 2, &peerPtr); if (result == ncclSuccess) { if (peerPtr != NULL) { // Use peerPtr to access world rank 2's memory } else { // Peer 2 is not reachable via LSA } }