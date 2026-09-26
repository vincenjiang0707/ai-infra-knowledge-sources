source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityCdpKernel.html

# 7.8. CUpti_ActivityCdpKernel[#](https://docs.nvidia.com#cupti-activitycdpkernel)

-
struct CUpti_ActivityCdpKernel
[#](https://docs.nvidia.com#_CPPv423CUpti_ActivityCdpKernel) The activity record for CDP (CUDA Dynamic Parallelism) kernel.

This activity record represents a CDP kernel execution.

Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityCdpKernel4kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_CDP_KERNEL.


-
uint8_t requested
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityCdpKernel9requestedE) The cache configuration requested by the kernel.

The value is one of the CUfunc_cache enumeration values from cuda.h.


-
uint8_t executed
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityCdpKernel8executedE) The cache configuration used for the kernel.

The value is one of the CUfunc_cache enumeration values from cuda.h.


The shared memory configuration used for the kernel.

The value is one of the CUsharedconfig enumeration values from cuda.h.


-
uint16_t registersPerThread
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityCdpKernel18registersPerThreadE) The number of registers required for each thread executing the kernel.


-
uint64_t start
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityCdpKernel5startE) The start timestamp for the kernel execution, in ns.

A value of 0 for both the start and end timestamps indicates that timestamp information could not be collected for the kernel.


-
uint64_t end
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityCdpKernel3endE) The end timestamp for the kernel execution, in ns.

A value of 0 for both the start and end timestamps indicates that timestamp information could not be collected for the kernel.


-
uint32_t deviceId
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityCdpKernel8deviceIdE) The ID of the device where the kernel is executing.


-
uint32_t contextId
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityCdpKernel9contextIdE) The ID of the context where the kernel is executing.


-
uint32_t streamId
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityCdpKernel8streamIdE) The ID of the stream where the kernel is executing.


-
int32_t gridX
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityCdpKernel5gridXE) The X-dimension grid size for the kernel.


-
int32_t gridY
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityCdpKernel5gridYE) The Y-dimension grid size for the kernel.


-
int32_t gridZ
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityCdpKernel5gridZE) The Z-dimension grid size for the kernel.


-
int32_t blockX
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityCdpKernel6blockXE) The X-dimension block size for the kernel.


-
int32_t blockY
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityCdpKernel6blockYE) The Y-dimension block size for the kernel.


-
int32_t blockZ
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityCdpKernel6blockZE) The Z-dimension grid size for the kernel.


The static shared memory allocated for the kernel, in bytes.


The dynamic shared memory reserved for the kernel, in bytes.


-
uint32_t localMemoryPerThread
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityCdpKernel20localMemoryPerThreadE) The amount of local memory reserved for each thread, in bytes.


-
uint32_t localMemoryTotal
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityCdpKernel16localMemoryTotalE) The total amount of local memory reserved for the kernel, in bytes.


-
uint32_t correlationId
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityCdpKernel13correlationIdE) The correlation ID of the kernel.

Each kernel execution is assigned a unique correlation ID that is identical to the correlation ID in the driver API activity record that launched the kernel.


-
int64_t gridId
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityCdpKernel6gridIdE) The grid ID of the kernel.

Each kernel execution is assigned a unique grid ID.


-
int64_t parentGridId
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityCdpKernel12parentGridIdE) The grid ID of the parent kernel.


-
uint64_t queued
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityCdpKernel6queuedE) The timestamp when kernel is queued up, in ns.

A value of CUPTI_TIMESTAMP_UNKNOWN indicates that the queued time is unknown.


-
uint64_t submitted
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityCdpKernel9submittedE) The timestamp when kernel is submitted to the gpu, in ns.

A value of CUPTI_TIMESTAMP_UNKNOWN indicates that the submission time is unknown.


-
uint64_t completed
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityCdpKernel9completedE) The timestamp when kernel is marked as completed, in ns.

A value of CUPTI_TIMESTAMP_UNKNOWN indicates that the completion time is unknown.


-
uint32_t parentBlockX
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityCdpKernel12parentBlockXE) The X-dimension of the parent block.


-
uint32_t parentBlockY
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityCdpKernel12parentBlockYE) The Y-dimension of the parent block.


-
uint32_t parentBlockZ
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityCdpKernel12parentBlockZE) The Z-dimension of the parent block.


-
uint32_t pad
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityCdpKernel3padE) Undefined.

Reserved for internal use.


-
const char *name
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityCdpKernel4nameE) The name of the kernel.

This name is shared across all activity records representing the same kernel, and so should not be modified.


-