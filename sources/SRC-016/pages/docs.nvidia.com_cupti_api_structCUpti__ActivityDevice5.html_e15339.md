source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityDevice5.html

# 7.22. CUpti_ActivityDevice5[#](https://docs.nvidia.com#cupti-activitydevice5)

-
struct CUpti_ActivityDevice5
[#](https://docs.nvidia.com#_CPPv421CUpti_ActivityDevice5) The activity record for a device.

(CUDA 11.6 onwards)

This activity record represents information about a GPU device (CUPTI_ACTIVITY_KIND_DEVICE).

Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice54kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_DEVICE.


-
[CUpti_ActivityFlag](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityFlag)flags[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice55flagsE) The flags associated with the device.

See also


-
uint64_t globalMemoryBandwidth
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice521globalMemoryBandwidthE) The global memory bandwidth available on the device, in kBytes/sec.


-
uint64_t globalMemorySize
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice516globalMemorySizeE) The amount of global memory on the device, in bytes.


-
uint32_t constantMemorySize
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice518constantMemorySizeE) The amount of constant memory on the device, in bytes.


-
uint32_t l2CacheSize
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice511l2CacheSizeE) The size of the L2 cache on the device, in bytes.


-
uint32_t numThreadsPerWarp
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice517numThreadsPerWarpE) The number of threads per warp on the device.


-
uint32_t coreClockRate
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice513coreClockRateE) The core clock rate of the device, in kHz.


-
uint32_t numMemcpyEngines
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice516numMemcpyEnginesE) Number of memory copy engines on the device.


-
uint32_t numMultiprocessors
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice518numMultiprocessorsE) Number of multiprocessors on the device.


-
uint32_t maxIPC
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice56maxIPCE) The maximum “instructions per cycle” possible on each device multiprocessor.


-
uint32_t maxWarpsPerMultiprocessor
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice525maxWarpsPerMultiprocessorE) Maximum number of warps that can be present on a multiprocessor at any given time.


-
uint32_t maxBlocksPerMultiprocessor
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice526maxBlocksPerMultiprocessorE) Maximum number of blocks that can be present on a multiprocessor at any given time.


Maximum amount of shared memory available per multiprocessor, in bytes.


-
uint32_t maxRegistersPerMultiprocessor
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice529maxRegistersPerMultiprocessorE) Maximum number of 32-bit registers available per multiprocessor.


-
uint32_t maxRegistersPerBlock
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice520maxRegistersPerBlockE) Maximum number of registers that can be allocated to a block.


Maximum amount of shared memory that can be assigned to a block, in bytes.


-
uint32_t maxThreadsPerBlock
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice518maxThreadsPerBlockE) Maximum number of threads allowed in a block.


-
uint32_t maxBlockDimX
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice512maxBlockDimXE) Maximum allowed X dimension for a block.


-
uint32_t maxBlockDimY
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice512maxBlockDimYE) Maximum allowed Y dimension for a block.


-
uint32_t maxBlockDimZ
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice512maxBlockDimZE) Maximum allowed Z dimension for a block.


-
uint32_t maxGridDimX
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice511maxGridDimXE) Maximum allowed X dimension for a grid.


-
uint32_t maxGridDimY
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice511maxGridDimYE) Maximum allowed Y dimension for a grid.


-
uint32_t maxGridDimZ
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice511maxGridDimZE) Maximum allowed Z dimension for a grid.


-
uint32_t computeCapabilityMajor
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice522computeCapabilityMajorE) Compute capability for the device, major number.


-
uint32_t computeCapabilityMinor
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice522computeCapabilityMinorE) Compute capability for the device, minor number.


-
uint32_t id
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice52idE) The device ID.


-
uint32_t eccEnabled
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice510eccEnabledE) ECC enabled flag for device.


-
CUuuid uuid
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice54uuidE) The device UUID.

This value is the globally unique immutable alphanumeric identifier of the device.


-
const char *name
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice54nameE) The device name.

This name is shared across all activity records representing instances of the device, and so should not be modified.


-
uint8_t isCudaVisible
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice513isCudaVisibleE) Flag to indicate whether the device is visible to CUDA.

Users can set the device visibility using CUDA_VISIBLE_DEVICES environment


-
uint8_t isMigEnabled
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice512isMigEnabledE) MIG enabled flag for device.


-
uint32_t gpuInstanceId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice513gpuInstanceIdE) GPU Instance id for MIG enabled devices.

If mig mode is disabled value is set to UINT32_MAX


-
uint32_t computeInstanceId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice517computeInstanceIdE) Compute Instance id for MIG enabled devices.

If mig mode is disabled value is set to UINT32_MAX


-
CUuuid migUuid
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice57migUuidE) The MIG UUID.

This value is the globally unique immutable alphanumeric identifier of the device.


-
uint32_t isNumaNode
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice510isNumaNodeE) Numa (Non-uniform memory access) information for device GPU is a NUMA node or not.


-
uint32_t numaId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice56numaIdE) Numa (Non-uniform memory access) information for device NUMA node ID of the GPU memory if GPU is not a NUMA node, it returns invalidNumaId.


-