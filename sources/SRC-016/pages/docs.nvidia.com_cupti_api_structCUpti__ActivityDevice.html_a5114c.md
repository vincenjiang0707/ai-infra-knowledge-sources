source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityDevice.html

# 7.18. CUpti_ActivityDevice[#](https://docs.nvidia.com#cupti-activitydevice)

-
struct CUpti_ActivityDevice
[#](https://docs.nvidia.com#_CPPv420CUpti_ActivityDevice) The activity record for a device.

(deprecated)

This activity record represents information about a GPU device (CUPTI_ACTIVITY_KIND_DEVICE). Device activity is now reported using the

[CUpti_ActivityDevice6](https://docs.nvidia.com/structCUpti__ActivityDevice6.html#structcupti__activitydevice6)activity record.Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityDevice4kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_DEVICE.


-
[CUpti_ActivityFlag](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityFlag)flags[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityDevice5flagsE) The flags associated with the device.

See also


-
uint64_t globalMemoryBandwidth
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityDevice21globalMemoryBandwidthE) The global memory bandwidth available on the device, in kBytes/sec.


-
uint64_t globalMemorySize
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityDevice16globalMemorySizeE) The amount of global memory on the device, in bytes.


-
uint32_t constantMemorySize
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityDevice18constantMemorySizeE) The amount of constant memory on the device, in bytes.


-
uint32_t l2CacheSize
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityDevice11l2CacheSizeE) The size of the L2 cache on the device, in bytes.


-
uint32_t numThreadsPerWarp
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityDevice17numThreadsPerWarpE) The number of threads per warp on the device.


-
uint32_t coreClockRate
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityDevice13coreClockRateE) The core clock rate of the device, in kHz.


-
uint32_t numMemcpyEngines
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityDevice16numMemcpyEnginesE) Number of memory copy engines on the device.


-
uint32_t numMultiprocessors
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityDevice18numMultiprocessorsE) Number of multiprocessors on the device.


-
uint32_t maxIPC
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityDevice6maxIPCE) The maximum “instructions per cycle” possible on each device multiprocessor.


-
uint32_t maxWarpsPerMultiprocessor
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityDevice25maxWarpsPerMultiprocessorE) Maximum number of warps that can be present on a multiprocessor at any given time.


-
uint32_t maxBlocksPerMultiprocessor
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityDevice26maxBlocksPerMultiprocessorE) Maximum number of blocks that can be present on a multiprocessor at any given time.


-
uint32_t maxRegistersPerBlock
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityDevice20maxRegistersPerBlockE) Maximum number of registers that can be allocated to a block.


Maximum amount of shared memory that can be assigned to a block, in bytes.


-
uint32_t maxThreadsPerBlock
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityDevice18maxThreadsPerBlockE) Maximum number of threads allowed in a block.


-
uint32_t maxBlockDimX
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityDevice12maxBlockDimXE) Maximum allowed X dimension for a block.


-
uint32_t maxBlockDimY
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityDevice12maxBlockDimYE) Maximum allowed Y dimension for a block.


-
uint32_t maxBlockDimZ
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityDevice12maxBlockDimZE) Maximum allowed Z dimension for a block.


-
uint32_t maxGridDimX
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityDevice11maxGridDimXE) Maximum allowed X dimension for a grid.


-
uint32_t maxGridDimY
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityDevice11maxGridDimYE) Maximum allowed Y dimension for a grid.


-
uint32_t maxGridDimZ
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityDevice11maxGridDimZE) Maximum allowed Z dimension for a grid.


-
uint32_t computeCapabilityMajor
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityDevice22computeCapabilityMajorE) Compute capability for the device, major number.


-
uint32_t computeCapabilityMinor
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityDevice22computeCapabilityMinorE) Compute capability for the device, minor number.


-
uint32_t id
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityDevice2idE) The device ID.


-
uint32_t pad
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityDevice3padE) Undefined.

Reserved for internal use.


-
const char *name
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityDevice4nameE) The device name.

This name is shared across all activity records representing instances of the device, and so should not be modified.


-