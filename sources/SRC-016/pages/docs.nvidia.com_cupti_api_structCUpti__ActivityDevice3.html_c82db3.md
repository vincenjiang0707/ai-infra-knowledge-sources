source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityDevice3.html

# 7.20. CUpti_ActivityDevice3[#](https://docs.nvidia.com#cupti-activitydevice3)

-
struct CUpti_ActivityDevice3
[#](https://docs.nvidia.com#_CPPv421CUpti_ActivityDevice3) The activity record for a device.

(CUDA 7.0 onwards)

This activity record represents information about a GPU device (CUPTI_ACTIVITY_KIND_DEVICE). Device activity is now reported using the

[CUpti_ActivityDevice6](https://docs.nvidia.com/structCUpti__ActivityDevice6.html#structcupti__activitydevice6)activity record.Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice34kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_DEVICE.


-
[CUpti_ActivityFlag](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityFlag)flags[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice35flagsE) The flags associated with the device.

See also


-
uint64_t globalMemoryBandwidth
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice321globalMemoryBandwidthE) The global memory bandwidth available on the device, in kBytes/sec.


-
uint64_t globalMemorySize
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice316globalMemorySizeE) The amount of global memory on the device, in bytes.


-
uint32_t constantMemorySize
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice318constantMemorySizeE) The amount of constant memory on the device, in bytes.


-
uint32_t l2CacheSize
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice311l2CacheSizeE) The size of the L2 cache on the device, in bytes.


-
uint32_t numThreadsPerWarp
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice317numThreadsPerWarpE) The number of threads per warp on the device.


-
uint32_t coreClockRate
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice313coreClockRateE) The core clock rate of the device, in kHz.


-
uint32_t numMemcpyEngines
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice316numMemcpyEnginesE) Number of memory copy engines on the device.


-
uint32_t numMultiprocessors
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice318numMultiprocessorsE) Number of multiprocessors on the device.


-
uint32_t maxIPC
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice36maxIPCE) The maximum “instructions per cycle” possible on each device multiprocessor.


-
uint32_t maxWarpsPerMultiprocessor
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice325maxWarpsPerMultiprocessorE) Maximum number of warps that can be present on a multiprocessor at any given time.


-
uint32_t maxBlocksPerMultiprocessor
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice326maxBlocksPerMultiprocessorE) Maximum number of blocks that can be present on a multiprocessor at any given time.


Maximum amount of shared memory available per multiprocessor, in bytes.


-
uint32_t maxRegistersPerMultiprocessor
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice329maxRegistersPerMultiprocessorE) Maximum number of 32-bit registers available per multiprocessor.


-
uint32_t maxRegistersPerBlock
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice320maxRegistersPerBlockE) Maximum number of registers that can be allocated to a block.


Maximum amount of shared memory that can be assigned to a block, in bytes.


-
uint32_t maxThreadsPerBlock
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice318maxThreadsPerBlockE) Maximum number of threads allowed in a block.


-
uint32_t maxBlockDimX
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice312maxBlockDimXE) Maximum allowed X dimension for a block.


-
uint32_t maxBlockDimY
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice312maxBlockDimYE) Maximum allowed Y dimension for a block.


-
uint32_t maxBlockDimZ
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice312maxBlockDimZE) Maximum allowed Z dimension for a block.


-
uint32_t maxGridDimX
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice311maxGridDimXE) Maximum allowed X dimension for a grid.


-
uint32_t maxGridDimY
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice311maxGridDimYE) Maximum allowed Y dimension for a grid.


-
uint32_t maxGridDimZ
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice311maxGridDimZE) Maximum allowed Z dimension for a grid.


-
uint32_t computeCapabilityMajor
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice322computeCapabilityMajorE) Compute capability for the device, major number.


-
uint32_t computeCapabilityMinor
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice322computeCapabilityMinorE) Compute capability for the device, minor number.


-
uint32_t id
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice32idE) The device ID.


-
uint32_t eccEnabled
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice310eccEnabledE) ECC enabled flag for device.


-
CUuuid uuid
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice34uuidE) The device UUID.

This value is the globally unique immutable alphanumeric identifier of the device.


-
const char *name
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice34nameE) The device name.

This name is shared across all activity records representing instances of the device, and so should not be modified.


-
uint8_t isCudaVisible
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityDevice313isCudaVisibleE) Flag to indicate whether the device is visible to CUDA.

Users can set the device visibility using CUDA_VISIBLE_DEVICES environment


-