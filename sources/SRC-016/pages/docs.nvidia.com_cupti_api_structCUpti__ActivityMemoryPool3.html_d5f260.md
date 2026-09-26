source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityMemoryPool3.html

# 7.89. CUpti_ActivityMemoryPool3[#](https://docs.nvidia.com#cupti-activitymemorypool3)

-
struct CUpti_ActivityMemoryPool3
[#](https://docs.nvidia.com#_CPPv425CUpti_ActivityMemoryPool3) The activity record for memory pool.

This activity record represents a memory pool creation, destruction and trimming (CUPTI_ACTIVITY_KIND_MEMORY_POOL). This activity record provides separate records for memory pool creation, destruction and trimming operations. This allows to correlate the corresponding driver and runtime API activity record with the memory pool operation.

Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityMemoryPool34kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_MEMORY_POOL.


-
[CUpti_ActivityMemoryPoolOperationType](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv437CUpti_ActivityMemoryPoolOperationType)memoryPoolOperationType[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityMemoryPool323memoryPoolOperationTypeE) The memory operation requested by the user,

[CUpti_ActivityMemoryPoolOperationType](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#group__cupti__activity__api_1ga878fb2c94e0051169fdf0ca7982612a2).

-
[CUpti_ActivityMemoryPoolType](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv428CUpti_ActivityMemoryPoolType)memoryPoolType[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityMemoryPool314memoryPoolTypeE) The type of the memory pool,

[CUpti_ActivityMemoryPoolType](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#group__cupti__activity__api_1ga8c40b23a5fe82862b18d60c5c42399a8).

-
uint32_t correlationId
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityMemoryPool313correlationIdE) The correlation ID of the memory pool operation.

Each memory pool operation is assigned a unique correlation ID that is identical to the correlation ID in the driver and runtime API activity record that launched the memory operation.


-
uint32_t processId
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityMemoryPool39processIdE) The ID of the process to which this record belongs to.


-
uint32_t deviceId
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityMemoryPool38deviceIdE) The ID of the device where the memory pool is created.


-
size_t minBytesToKeep
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityMemoryPool314minBytesToKeepE) The minimum bytes to keep of the memory pool.

`minBytesToKeep`

is valid for CUPTI_ACTIVITY_MEMORY_POOL_OPERATION_TYPE_TRIMMED,[CUpti_ActivityMemoryPoolOperationType](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#group__cupti__activity__api_1ga878fb2c94e0051169fdf0ca7982612a2)

-
uint64_t address
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityMemoryPool37addressE) The virtual address of the allocation.


-
uint64_t size
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityMemoryPool34sizeE) The size of the memory pool operation in bytes.

`size`

is valid for CUPTI_ACTIVITY_MEMORY_POOL_TYPE_LOCAL,[CUpti_ActivityMemoryPoolType](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#group__cupti__activity__api_1ga8c40b23a5fe82862b18d60c5c42399a8).

-
uint64_t releaseThreshold
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityMemoryPool316releaseThresholdE) The release threshold of the memory pool.

`releaseThreshold`

is valid for CUPTI_ACTIVITY_MEMORY_POOL_TYPE_LOCAL,[CUpti_ActivityMemoryPoolType](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#group__cupti__activity__api_1ga8c40b23a5fe82862b18d60c5c42399a8).

-
uint64_t timestamp
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityMemoryPool39timestampE) The start timestamp for the memory operation, in ns.


-
uint64_t utilizedSize
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityMemoryPool312utilizedSizeE) The utilized size of the memory pool.

`utilizedSize`

is valid for CUPTI_ACTIVITY_MEMORY_POOL_TYPE_LOCAL,[CUpti_ActivityMemoryPoolType](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#group__cupti__activity__api_1ga8c40b23a5fe82862b18d60c5c42399a8).

-
uint8_t isManagedPool
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityMemoryPool313isManagedPoolE) Whether the pool is of managed memory allocation or pinned memory allocation.

If it is 0, it is pinned and if it is 1, the memory pool allocation is of managed memory type.


-
uint8_t pad2[7]
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityMemoryPool34pad2E) Undefined.

Reserved for internal use.


-