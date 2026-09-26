source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityMemoryPool.html

# 7.87. CUpti_ActivityMemoryPool[#](https://docs.nvidia.com#cupti-activitymemorypool)

-
struct CUpti_ActivityMemoryPool
[#](https://docs.nvidia.com#_CPPv424CUpti_ActivityMemoryPool) The activity record for memory pool.

This activity record represents a memory pool creation, destruction and trimming (CUPTI_ACTIVITY_KIND_MEMORY_POOL). This activity record provides separate records for memory pool creation, destruction and trimming operations. This allows to correlate the corresponding driver and runtime API activity record with the memory pool operation.

Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityMemoryPool4kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_MEMORY_POOL.


-
[CUpti_ActivityMemoryPoolOperationType](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv437CUpti_ActivityMemoryPoolOperationType)memoryPoolOperationType[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityMemoryPool23memoryPoolOperationTypeE) The memory operation requested by the user,

[CUpti_ActivityMemoryPoolOperationType](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#group__cupti__activity__api_1ga878fb2c94e0051169fdf0ca7982612a2).

-
[CUpti_ActivityMemoryPoolType](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv428CUpti_ActivityMemoryPoolType)memoryPoolType[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityMemoryPool14memoryPoolTypeE) The type of the memory pool,

[CUpti_ActivityMemoryPoolType](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#group__cupti__activity__api_1ga8c40b23a5fe82862b18d60c5c42399a8).

-
uint32_t correlationId
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityMemoryPool13correlationIdE) The correlation ID of the memory pool operation.

Each memory pool operation is assigned a unique correlation ID that is identical to the correlation ID in the driver and runtime API activity record that launched the memory operation.


-
uint32_t processId
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityMemoryPool9processIdE) The ID of the process to which this record belongs to.


-
uint32_t deviceId
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityMemoryPool8deviceIdE) The ID of the device where the memory pool is created.


-
size_t minBytesToKeep
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityMemoryPool14minBytesToKeepE) The minimum bytes to keep of the memory pool.

`minBytesToKeep`

is valid for CUPTI_ACTIVITY_MEMORY_POOL_OPERATION_TYPE_TRIMMED,[CUpti_ActivityMemoryPoolOperationType](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#group__cupti__activity__api_1ga878fb2c94e0051169fdf0ca7982612a2)

-
uint64_t address
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityMemoryPool7addressE) The virtual address of the allocation.


-
uint64_t size
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityMemoryPool4sizeE) The size of the memory pool operation in bytes.

`size`

is valid for CUPTI_ACTIVITY_MEMORY_POOL_TYPE_LOCAL,[CUpti_ActivityMemoryPoolType](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#group__cupti__activity__api_1ga8c40b23a5fe82862b18d60c5c42399a8).

-
uint64_t releaseThreshold
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityMemoryPool16releaseThresholdE) The release threshold of the memory pool.

`releaseThreshold`

is valid for CUPTI_ACTIVITY_MEMORY_POOL_TYPE_LOCAL,[CUpti_ActivityMemoryPoolType](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#group__cupti__activity__api_1ga8c40b23a5fe82862b18d60c5c42399a8).

-
uint64_t timestamp
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityMemoryPool9timestampE) The start timestamp for the memory operation, in ns.


-