source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityKernel4.html

# 7.62. CUpti_ActivityKernel4[#](https://docs.nvidia.com#cupti-activitykernel4)

-
struct CUpti_ActivityKernel4
[#](https://docs.nvidia.com#_CPPv421CUpti_ActivityKernel4) The activity record for a kernel (CUDA 9.0(with sm_70 support) onwards).

(deprecated in CUDA 11.0)

This activity record represents a kernel execution (CUPTI_ACTIVITY_KIND_KERNEL and CUPTI_ACTIVITY_KIND_CONCURRENT_KERNEL). Kernel activities are now reported using the

[CUpti_ActivityKernel9](https://docs.nvidia.com/structCUpti__ActivityKernel9.html#structcupti__activitykernel9)activity record.Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityKernel44kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_KERNEL or CUPTI_ACTIVITY_KIND_CONCURRENT_KERNEL.


-
uint8_t requested
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityKernel49requestedE) The cache configuration requested by the kernel.

The value is one of the CUfunc_cache enumeration values from cuda.h.


-
uint8_t executed
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityKernel48executedE) The cache configuration used for the kernel.

The value is one of the CUfunc_cache enumeration values from cuda.h.


-
union
[CUpti_ActivityKernel4](https://docs.nvidia.com#_CPPv421CUpti_ActivityKernel4)::[anonymous] cacheConfig[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityKernel411cacheConfigE) For devices with compute capability 7.5+ cacheConfig values are not updated in case field isSharedMemoryCarveoutRequested is set.


The shared memory configuration used for the kernel.

The value is one of the CUsharedconfig enumeration values from cuda.h.


-
uint16_t registersPerThread
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityKernel418registersPerThreadE) The number of registers required for each thread executing the kernel.


-
[CUpti_ActivityPartitionedGlobalCacheConfig](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv442CUpti_ActivityPartitionedGlobalCacheConfig)partitionedGlobalCacheRequested[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityKernel431partitionedGlobalCacheRequestedE) The partitioned global caching requested for the kernel.

Partitioned global caching is required to enable caching on certain chips, such as devices with compute capability 5.2.


-
[CUpti_ActivityPartitionedGlobalCacheConfig](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv442CUpti_ActivityPartitionedGlobalCacheConfig)partitionedGlobalCacheExecuted[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityKernel430partitionedGlobalCacheExecutedE) The partitioned global caching executed for the kernel.

Partitioned global caching is required to enable caching on certain chips, such as devices with compute capability 5.2. Partitioned global caching can be automatically disabled if the occupancy requirement of the launch cannot support caching.


-
uint64_t start
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityKernel45startE) The start timestamp for the kernel execution, in ns.

A value of 0 for both the start and end timestamps indicates that timestamp information could not be collected for the kernel.


-
uint64_t end
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityKernel43endE) The end timestamp for the kernel execution, in ns.

A value of 0 for both the start and end timestamps indicates that timestamp information could not be collected for the kernel.


-
uint64_t completed
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityKernel49completedE) The completed timestamp for the kernel execution, in ns.

It represents the completion of all it’s child kernels and the kernel itself. A value of CUPTI_TIMESTAMP_UNKNOWN indicates that the completion time is unknown.


-
uint32_t deviceId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityKernel48deviceIdE) The ID of the device where the kernel is executing.


-
uint32_t contextId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityKernel49contextIdE) The ID of the context where the kernel is executing.


-
uint32_t streamId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityKernel48streamIdE) The ID of the stream where the kernel is executing.


-
int32_t gridX
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityKernel45gridXE) The X-dimension grid size for the kernel.


-
int32_t gridY
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityKernel45gridYE) The Y-dimension grid size for the kernel.


-
int32_t gridZ
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityKernel45gridZE) The Z-dimension grid size for the kernel.


-
int32_t blockX
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityKernel46blockXE) The X-dimension block size for the kernel.


-
int32_t blockY
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityKernel46blockYE) The Y-dimension block size for the kernel.


-
int32_t blockZ
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityKernel46blockZE) The Z-dimension grid size for the kernel.


The static shared memory allocated for the kernel, in bytes.


The dynamic shared memory reserved for the kernel, in bytes.


-
uint32_t localMemoryPerThread
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityKernel420localMemoryPerThreadE) The amount of local memory reserved for each thread, in bytes.


-
uint32_t localMemoryTotal
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityKernel416localMemoryTotalE) The total amount of local memory reserved for the kernel, in bytes.


-
uint32_t correlationId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityKernel413correlationIdE) The correlation ID of the kernel.

Each kernel execution is assigned a unique correlation ID that is identical to the correlation ID in the driver or runtime API activity record that launched the kernel.


-
int64_t gridId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityKernel46gridIdE) The grid ID of the kernel.

Each kernel is assigned a unique grid ID at runtime.


-
const char *name
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityKernel44nameE) The name of the kernel.

This name is shared across all activity records representing the same kernel, and so should not be modified.


-
void *reserved0
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityKernel49reserved0E) Undefined.

Reserved for internal use.


-
uint64_t queued
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityKernel46queuedE) The timestamp when the kernel is queued up in the command buffer, in ns.

A value of CUPTI_TIMESTAMP_UNKNOWN indicates that the queued time could not be collected for the kernel. This timestamp is not collected by default. Use API

[cuptiActivityEnableLatencyTimestamps()](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#group__cupti__activity__api_1ga4b50c0c1634913f8157cfcfe84f19fa9)to enable collection.Command buffer is a buffer written by CUDA driver to send commands like kernel launch, memory copy etc to the GPU. All launches of CUDA kernels are asynchronous with respect to the host, the host requests the launch by writing commands into the command buffer, then returns without checking the GPU’s progress.


-
uint64_t submitted
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityKernel49submittedE) The timestamp when the command buffer containing the kernel launch is submitted to the GPU, in ns.

A value of CUPTI_TIMESTAMP_UNKNOWN indicates that the submitted time could not be collected for the kernel. This timestamp is not collected by default. Use API

[cuptiActivityEnableLatencyTimestamps()](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#group__cupti__activity__api_1ga4b50c0c1634913f8157cfcfe84f19fa9)to enable collection.

-
uint8_t launchType
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityKernel410launchTypeE) The indicates if the kernel was executed via a regular launch or via a single/multi device cooperative launch.

See also


This indicates if CU_FUNC_ATTRIBUTE_PREFERRED_SHARED_MEMORY_CARVEOUT was updated for the kernel launch.


Shared memory carveout value requested for the function in percentage of the total resource.

The value will be updated only if field isSharedMemoryCarveoutRequested is set.


-
uint8_t padding
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityKernel47paddingE) Undefined.

Reserved for internal use.


Shared memory size set by the driver.


-