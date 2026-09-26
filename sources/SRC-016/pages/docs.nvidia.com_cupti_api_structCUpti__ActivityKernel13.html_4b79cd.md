source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityKernel13.html

# 7.59. CUpti_ActivityKernel13[#](https://docs.nvidia.com#cupti-activitykernel13)

-
struct CUpti_ActivityKernel13
[#](https://docs.nvidia.com#_CPPv422CUpti_ActivityKernel13) The activity record for kernel (version 13).

This activity record represents a kernel execution (CUPTI_ACTIVITY_KIND_KERNEL and CUPTI_ACTIVITY_KIND_CONCURRENT_KERNEL)

This version adds source graph node ID and source graph ID fields.

Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityKernel134kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_KERNEL or CUPTI_ACTIVITY_KIND_CONCURRENT_KERNEL.


-
uint8_t requested
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityKernel139requestedE) The cache configuration requested by the kernel.

The value is one of the CUfunc_cache enumeration values from cuda.h.


-
uint8_t executed
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityKernel138executedE) The cache configuration used for the kernel.

The value is one of the CUfunc_cache enumeration values from cuda.h.


-
union
[CUpti_ActivityKernel13](https://docs.nvidia.com#_CPPv422CUpti_ActivityKernel13)::[anonymous] cacheConfig[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityKernel1311cacheConfigE) For devices with compute capability 7.5+ cacheConfig values are not updated in case field isSharedMemoryCarveoutRequested is set.


The shared memory configuration used for the kernel.

The value is one of the CUsharedconfig enumeration values from cuda.h.


-
uint16_t registersPerThread
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityKernel1318registersPerThreadE) The number of registers required for each thread executing the kernel.


-
[CUpti_ActivityPartitionedGlobalCacheConfig](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv442CUpti_ActivityPartitionedGlobalCacheConfig)partitionedGlobalCacheRequested[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityKernel1331partitionedGlobalCacheRequestedE) The partitioned global caching requested for the kernel.

Partitioned global caching is required to enable caching on certain chips, such as devices with compute capability 5.2.


-
[CUpti_ActivityPartitionedGlobalCacheConfig](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv442CUpti_ActivityPartitionedGlobalCacheConfig)partitionedGlobalCacheExecuted[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityKernel1330partitionedGlobalCacheExecutedE) The partitioned global caching executed for the kernel.

Partitioned global caching is required to enable caching on certain chips, such as devices with compute capability 5.2. Partitioned global caching can be automatically disabled if the occupancy requirement of the launch cannot support caching.


-
uint64_t start
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityKernel135startE) The start timestamp for the kernel execution, in ns.

A value of 0 for both the start and end timestamps indicates that timestamp information could not be collected for the kernel.


-
uint64_t end
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityKernel133endE) The end timestamp for the kernel execution, in ns.

A value of 0 for both the start and end timestamps indicates that timestamp information could not be collected for the kernel.


-
uint64_t completed
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityKernel139completedE) The completed timestamp for the kernel execution, in ns.

It represents the completion of all it’s child kernels and the kernel itself. A value of CUPTI_TIMESTAMP_UNKNOWN indicates that the completion time is unknown.


-
uint32_t deviceId
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityKernel138deviceIdE) The ID of the device where the kernel is executing.


-
uint32_t contextId
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityKernel139contextIdE) The ID of the context where the kernel is executing.


-
uint32_t streamId
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityKernel138streamIdE) The ID of the stream where the kernel is executing.


-
int32_t gridX
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityKernel135gridXE) The X-dimension grid size for the kernel.


-
int32_t gridY
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityKernel135gridYE) The Y-dimension grid size for the kernel.


-
int32_t gridZ
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityKernel135gridZE) The Z-dimension grid size for the kernel.


-
int32_t blockX
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityKernel136blockXE) The X-dimension block size for the kernel.


-
int32_t blockY
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityKernel136blockYE) The Y-dimension block size for the kernel.


-
int32_t blockZ
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityKernel136blockZE) The Z-dimension grid size for the kernel.


The static shared memory allocated for the kernel, in bytes.


The dynamic shared memory reserved for the kernel, in bytes.


-
uint32_t localMemoryPerThread
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityKernel1320localMemoryPerThreadE) The amount of local memory reserved for each thread, in bytes.


-
uint32_t localMemoryTotal
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityKernel1316localMemoryTotalE) The total amount of local memory reserved for the kernel, in bytes (deprecated in CUDA 11.8).

Refer field localMemoryTotal_v2


-
uint32_t correlationId
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityKernel1313correlationIdE) The correlation ID of the kernel.

Each kernel execution is assigned a unique correlation ID that is identical to the correlation ID in the driver or runtime API activity record that launched the kernel.


-
int64_t gridId
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityKernel136gridIdE) The grid ID of the kernel.

Each kernel is assigned a unique grid ID at runtime.


-
const char *name
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityKernel134nameE) The name of the kernel.

This name is shared across all activity records representing the same kernel, and so should not be modified.


-
void *reserved0
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityKernel139reserved0E) Undefined.

Reserved for internal use.


-
uint64_t queued
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityKernel136queuedE) The timestamp when the kernel is queued up in the command buffer, in ns.

A value of CUPTI_TIMESTAMP_UNKNOWN indicates that the queued time could not be collected for the kernel. This timestamp is not collected by default. Use API

[cuptiActivityEnableLatencyTimestamps()](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#group__cupti__activity__api_1ga4b50c0c1634913f8157cfcfe84f19fa9)to enable collection.Command buffer is a buffer written by CUDA driver to send commands like kernel launch, memory copy etc to the GPU. All launches of CUDA kernels are asynchronous with respect to the host, the host requests the launch by writing commands into the command buffer, then returns without checking the GPU’s progress.


-
uint64_t submitted
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityKernel139submittedE) The timestamp when the command buffer containing the kernel launch is submitted to the GPU, in ns.

A value of CUPTI_TIMESTAMP_UNKNOWN indicates that the submitted time could not be collected for the kernel. This timestamp is not collected by default. Use API

[cuptiActivityEnableLatencyTimestamps()](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#group__cupti__activity__api_1ga4b50c0c1634913f8157cfcfe84f19fa9)to enable collection.

-
uint8_t launchType
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityKernel1310launchTypeE) The indicates if the kernel was executed via a regular launch or via a single/multi device cooperative launch.

See also


This indicates if CU_FUNC_ATTRIBUTE_PREFERRED_SHARED_MEMORY_CARVEOUT was updated for the kernel launch.


Shared memory carveout value requested for the function in percentage of the total resource.

The value will be updated only if field isSharedMemoryCarveoutRequested is set.


-
uint8_t padding
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityKernel137paddingE) Undefined.

Reserved for internal use.


Shared memory size set by the driver.


-
uint64_t graphNodeId
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityKernel1311graphNodeIdE) The unique ID of the graph node that launched this kernel through graph launch APIs.

This field will be 0 if the kernel is not launched through graph launch APIs.


-
[CUpti_FuncShmemLimitConfig](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv426CUpti_FuncShmemLimitConfig)shmemLimitConfig[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityKernel1316shmemLimitConfigE) The shared memory limit config for the kernel.

This field shows whether user has opted for a higher per block limit of dynamic shared memory.


-
uint32_t graphId
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityKernel137graphIdE) The unique ID of the graph that launched this kernel through graph launch APIs.

This field will be 0 if the kernel is not launched through graph launch APIs.


-
CUaccessPolicyWindow *pAccessPolicyWindow
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityKernel1319pAccessPolicyWindowE) The pointer to the access policy window.

The structure CUaccessPolicyWindow is defined in cuda.h.


-
uint32_t channelID
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityKernel139channelIDE) The ID of the HW channel on which the kernel is launched.


-
[CUpti_ChannelType](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv417CUpti_ChannelType)channelType[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityKernel1311channelTypeE) The type of the channel.


-
uint32_t clusterX
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityKernel138clusterXE) The X-dimension cluster size for the kernel.

Field is valid for devices with compute capability 9.0 and higher


-
uint32_t clusterY
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityKernel138clusterYE) The Y-dimension cluster size for the kernel.

Field is valid for devices with compute capability 9.0 and higher


-
uint32_t clusterZ
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityKernel138clusterZE) The Z-dimension cluster size for the kernel.

Field is valid for devices with compute capability 9.0 and higher


-
uint32_t clusterSchedulingPolicy
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityKernel1323clusterSchedulingPolicyE) The cluster scheduling policy for the kernel.

Refer CUclusterSchedulingPolicy Field is valid for devices with compute capability 9.0 and higher


-
uint64_t localMemoryTotal_v2
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityKernel1319localMemoryTotal_v2E) The total amount of local memory reserved for the kernel, in bytes.


-
uint32_t maxPotentialClusterSize
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityKernel1323maxPotentialClusterSizeE) The maximum cluster size for the kernel.


-
uint32_t maxActiveClusters
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityKernel1317maxActiveClustersE) The maximum clusters that could co-exist on the target device for the kernel.


-
uint8_t isDeviceLaunched
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityKernel1316isDeviceLaunchedE) This field is set to 1 if the kernel is part of a device launched graph.


-
int32_t priority
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityKernel138priorityE) The launch priority of the kernel.


-
uint32_t executionModel
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityKernel1314executionModelE) The execution model of the kernel function.

See also


-
uint32_t sourceGraphId
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityKernel1313sourceGraphIdE) The unique graph ID of the node from which the kernel node was instantiated or last updated.

This field will be 0 if the kernel is not launched through graph launch APIs.


-
uint32_t padding6
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityKernel138padding6E) Reserved for internal use.


-
uint64_t sourceGraphNodeId
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityKernel1317sourceGraphNodeIdE) The unique graph node ID of the node from which the kernel node was instantiated or last updated.

This field will be 0 if the kernel is not launched through graph launch APIs.


-