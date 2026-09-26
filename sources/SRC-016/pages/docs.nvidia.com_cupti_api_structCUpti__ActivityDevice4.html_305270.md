source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityDevice4.html

# 7.21. CUpti_ActivityDevice4[#](https://docs.nvidia.com#cupti-activitydevice4)

-
struct CUpti_ActivityDevice4
[#](https://docs.nvidia.com#_CPPv421CUpti_ActivityDevice4) The activity record for a device.

(CUDA 11.6 onwards)

This activity record represents information about a GPU device (CUPTI_ACTIVITY_KIND_DEVICE). Device activity is now reported using the

[CUpti_ActivityDevice6](https://docs.nvidia.com/structCUpti__ActivityDevice6.html#structcupti__activitydevice6)activity record.Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice44kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_DEVICE.


-
[CUpti_ActivityFlag](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityFlag)flags[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice45flagsE) The flags associated with the device.

See also


-
uint64_t globalMemoryBandwidth
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice421globalMemoryBandwidthE) The global memory bandwidth available on the device, in kBytes/sec.


-
uint64_t globalMemorySize
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice416globalMemorySizeE) The amount of global memory on the device, in bytes.


-
uint32_t constantMemorySize
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice418constantMemorySizeE) The amount of constant memory on the device, in bytes.


-
uint32_t l2CacheSize
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice411l2CacheSizeE) The size of the L2 cache on the device, in bytes.


-
uint32_t numThreadsPerWarp
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice417numThreadsPerWarpE) The number of threads per warp on the device.


-
uint32_t coreClockRate
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice413coreClockRateE) The core clock rate of the device, in kHz.


-
uint32_t numMemcpyEngines
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice416numMemcpyEnginesE) Number of memory copy engines on the device.


-
uint32_t numMultiprocessors
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice418numMultiprocessorsE) Number of multiprocessors on the device.


-
uint32_t maxIPC
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice46maxIPCE) The maximum “instructions per cycle” possible on each device multiprocessor.


-
uint32_t maxWarpsPerMultiprocessor
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice425maxWarpsPerMultiprocessorE) Maximum number of warps that can be present on a multiprocessor at any given time.


-
uint32_t maxBlocksPerMultiprocessor
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice426maxBlocksPerMultiprocessorE) Maximum number of blocks that can be present on a multiprocessor at any given time.


Maximum amount of shared memory available per multiprocessor, in bytes.


-
uint32_t maxRegistersPerMultiprocessor
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice429maxRegistersPerMultiprocessorE) Maximum number of 32-bit registers available per multiprocessor.


-
uint32_t maxRegistersPerBlock
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice420maxRegistersPerBlockE) Maximum number of registers that can be allocated to a block.


Maximum amount of shared memory that can be assigned to a block, in bytes.


-
uint32_t maxThreadsPerBlock
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice418maxThreadsPerBlockE) Maximum number of threads allowed in a block.


-
uint32_t maxBlockDimX
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice412maxBlockDimXE) Maximum allowed X dimension for a block.


-
uint32_t maxBlockDimY
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice412maxBlockDimYE) Maximum allowed Y dimension for a block.


-
uint32_t maxBlockDimZ
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice412maxBlockDimZE) Maximum allowed Z dimension for a block.


-
uint32_t maxGridDimX
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice411maxGridDimXE) Maximum allowed X dimension for a grid.


-
uint32_t maxGridDimY
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice411maxGridDimYE) Maximum allowed Y dimension for a grid.


-
uint32_t maxGridDimZ
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice411maxGridDimZE) Maximum allowed Z dimension for a grid.


-
uint32_t computeCapabilityMajor
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice422computeCapabilityMajorE) Compute capability for the device, major number.


-
uint32_t computeCapabilityMinor
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice422computeCapabilityMinorE) Compute capability for the device, minor number.


-
uint32_t id
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice42idE) The device ID.


-
uint32_t eccEnabled
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice410eccEnabledE) ECC enabled flag for device.


-
CUuuid uuid
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice44uuidE) The device UUID.

This value is the globally unique immutable alphanumeric identifier of the device.


-
const char *name
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice44nameE) The device name.

This name is shared across all activity records representing instances of the device, and so should not be modified.


-
uint8_t isCudaVisible
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice413isCudaVisibleE) Flag to indicate whether the device is visible to CUDA.

Users can set the device visibility using CUDA_VISIBLE_DEVICES environment


-
uint8_t isMigEnabled
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice412isMigEnabledE) MIG enabled flag for device.


-
uint32_t gpuInstanceId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice413gpuInstanceIdE) GPU Instance id for MIG enabled devices.

If mig mode is disabled value is set to UINT32_MAX


-
uint32_t computeInstanceId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice417computeInstanceIdE) Compute Instance id for MIG enabled devices.

If mig mode is disabled value is set to UINT32_MAX


-
CUuuid migUuid
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice47migUuidE) The MIG UUID.

This value is the globally unique immutable alphanumeric identifier of the device.


-