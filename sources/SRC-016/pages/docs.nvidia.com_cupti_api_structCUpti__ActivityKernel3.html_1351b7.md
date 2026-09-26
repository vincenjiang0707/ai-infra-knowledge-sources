source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityKernel3.html

# 7.61. CUpti_ActivityKernel3[#](https://docs.nvidia.com#cupti-activitykernel3)

-
struct CUpti_ActivityKernel3
[#](https://docs.nvidia.com#_CPPv421CUpti_ActivityKernel3) The activity record for a kernel (CUDA 6.5(with sm_52 support) onwards).

(deprecated in CUDA 9.0)

This activity record represents a kernel execution (CUPTI_ACTIVITY_KIND_KERNEL and CUPTI_ACTIVITY_KIND_CONCURRENT_KERNEL). Kernel activities are now reported using the

[CUpti_ActivityKernel9](https://docs.nvidia.com/structCUpti__ActivityKernel9.html#structcupti__activitykernel9)activity record.Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityKernel34kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_KERNEL or CUPTI_ACTIVITY_KIND_CONCURRENT_KERNEL.


-
uint8_t requested
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityKernel39requestedE) The cache configuration requested by the kernel.

The value is one of the CUfunc_cache enumeration values from cuda.h.


-
uint8_t executed
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityKernel38executedE) The cache configuration used for the kernel.

The value is one of the CUfunc_cache enumeration values from cuda.h.


The shared memory configuration used for the kernel.

The value is one of the CUsharedconfig enumeration values from cuda.h.


-
uint16_t registersPerThread
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityKernel318registersPerThreadE) The number of registers required for each thread executing the kernel.


-
[CUpti_ActivityPartitionedGlobalCacheConfig](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv442CUpti_ActivityPartitionedGlobalCacheConfig)partitionedGlobalCacheRequested[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityKernel331partitionedGlobalCacheRequestedE) The partitioned global caching requested for the kernel.

Partitioned global caching is required to enable caching on certain chips, such as devices with compute capability 5.2.


-
[CUpti_ActivityPartitionedGlobalCacheConfig](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv442CUpti_ActivityPartitionedGlobalCacheConfig)partitionedGlobalCacheExecuted[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityKernel330partitionedGlobalCacheExecutedE) The partitioned global caching executed for the kernel.

Partitioned global caching is required to enable caching on certain chips, such as devices with compute capability 5.2. Partitioned global caching can be automatically disabled if the occupancy requirement of the launch cannot support caching.


-
uint64_t start
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityKernel35startE) The start timestamp for the kernel execution, in ns.

A value of 0 for both the start and end timestamps indicates that timestamp information could not be collected for the kernel.


-
uint64_t end
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityKernel33endE) The end timestamp for the kernel execution, in ns.

A value of 0 for both the start and end timestamps indicates that timestamp information could not be collected for the kernel.


-
uint64_t completed
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityKernel39completedE) The completed timestamp for the kernel execution, in ns.

It represents the completion of all it’s child kernels and the kernel itself. A value of CUPTI_TIMESTAMP_UNKNOWN indicates that the completion time is unknown.


-
uint32_t deviceId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityKernel38deviceIdE) The ID of the device where the kernel is executing.


-
uint32_t contextId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityKernel39contextIdE) The ID of the context where the kernel is executing.


-
uint32_t streamId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityKernel38streamIdE) The ID of the stream where the kernel is executing.


-
int32_t gridX
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityKernel35gridXE) The X-dimension grid size for the kernel.


-
int32_t gridY
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityKernel35gridYE) The Y-dimension grid size for the kernel.


-
int32_t gridZ
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityKernel35gridZE) The Z-dimension grid size for the kernel.


-
int32_t blockX
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityKernel36blockXE) The X-dimension block size for the kernel.


-
int32_t blockY
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityKernel36blockYE) The Y-dimension block size for the kernel.


-
int32_t blockZ
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityKernel36blockZE) The Z-dimension grid size for the kernel.


The static shared memory allocated for the kernel, in bytes.


The dynamic shared memory reserved for the kernel, in bytes.


-
uint32_t localMemoryPerThread
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityKernel320localMemoryPerThreadE) The amount of local memory reserved for each thread, in bytes.


-
uint32_t localMemoryTotal
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityKernel316localMemoryTotalE) The total amount of local memory reserved for the kernel, in bytes.


-
uint32_t correlationId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityKernel313correlationIdE) The correlation ID of the kernel.

Each kernel execution is assigned a unique correlation ID that is identical to the correlation ID in the driver or runtime API activity record that launched the kernel.


-
int64_t gridId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityKernel36gridIdE) The grid ID of the kernel.

Each kernel is assigned a unique grid ID at runtime.


-
const char *name
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityKernel34nameE) The name of the kernel.

This name is shared across all activity records representing the same kernel, and so should not be modified.


-
void *reserved0
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityKernel39reserved0E) Undefined.

Reserved for internal use.


-