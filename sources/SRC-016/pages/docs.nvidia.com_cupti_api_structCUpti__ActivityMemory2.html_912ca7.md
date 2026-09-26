source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityMemory2.html

# 7.84. CUpti_ActivityMemory2[#](https://docs.nvidia.com#cupti-activitymemory2)

-
struct CUpti_ActivityMemory2
[#](https://docs.nvidia.com#_CPPv421CUpti_ActivityMemory2) The activity record for memory.

This activity record represents a memory allocation and free operation (CUPTI_ACTIVITY_KIND_MEMORY2). This activity record provides separate records for memory allocation and memory release operations. This allows to correlate the corresponding driver and runtime API activity record with the memory operation.

Note: This activity record is an upgrade over

[CUpti_ActivityMemory](https://docs.nvidia.com/structCUpti__ActivityMemory.html#structcupti__activitymemory)enabled using the kind[CUPTI_ACTIVITY_KIND_MEMORY](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#group__cupti__activity__api_1ggaefed720d5a60c3e8b286cd386c4913e3afee93ef030088d7a992a1abd6d6e53b0).[CUpti_ActivityMemory](https://docs.nvidia.com/structCUpti__ActivityMemory.html#structcupti__activitymemory)provides a single record for the memory allocation and memory release operations.Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemory24kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_MEMORY2.


-
[CUpti_ActivityMemoryOperationType](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv433CUpti_ActivityMemoryOperationType)memoryOperationType[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemory219memoryOperationTypeE) The memory operation requested by the user,

[CUpti_ActivityMemoryOperationType](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#group__cupti__activity__api_1ga6404b89cfbbd60e04204244d230b15c4).

-
[CUpti_ActivityMemoryKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv424CUpti_ActivityMemoryKind)memoryKind[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemory210memoryKindE) The memory kind requested by the user,

[CUpti_ActivityMemoryKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#group__cupti__activity__api_1ga9969b86f0e54989b27080dc6083263bc).

-
uint32_t correlationId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemory213correlationIdE) The correlation ID of the memory operation.

Each memory operation is assigned a unique correlation ID that is identical to the correlation ID in the driver and runtime API activity record that launched the memory operation.


-
uint64_t address
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemory27addressE) The virtual address of the allocation.

The base address of the memory pool.


-
uint64_t bytes
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemory25bytesE) The number of bytes of memory allocated.


-
uint64_t timestamp
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemory29timestampE) The start timestamp for the memory operation, in ns.


-
uint64_t PC
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemory22PCE) The program counter of the memory operation.


-
uint32_t processId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemory29processIdE) The ID of the process to which this record belongs to.


-
uint32_t deviceId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemory28deviceIdE) The ID of the device where the memory operation is taking place.


-
uint32_t contextId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemory29contextIdE) The ID of the context.

If context is NULL,

`contextId`

is set to CUPTI_INVALID_CONTEXT_ID.

-
uint32_t streamId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemory28streamIdE) The ID of the stream.

If memory operation is not async,

`streamId`

is set to CUPTI_INVALID_STREAM_ID.

-
const char *name
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemory24nameE) Variable name.

This name is shared across all activity records representing the same symbol, and so should not be modified.


-
uint32_t isAsync
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemory27isAsyncE) `isAsync`

is set if memory operation happens through async memory APIs.

-
uint32_t pad1
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemory24pad1E) Undefined.

Reserved for internal use.


-
[CUpti_ActivityMemoryPoolType](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv428CUpti_ActivityMemoryPoolType)memoryPoolType[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemory214memoryPoolTypeE) The type of the memory pool,

[CUpti_ActivityMemoryPoolType](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#group__cupti__activity__api_1ga8c40b23a5fe82862b18d60c5c42399a8).

-
uint32_t pad2
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemory24pad2E) Undefined.

Reserved for internal use.


-
uint64_t releaseThreshold
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemory216releaseThresholdE) The release threshold of the memory pool in bytes.

`releaseThreshold`

is valid for CUPTI_ACTIVITY_MEMORY_POOL_TYPE_LOCAL,[CUpti_ActivityMemoryPoolType](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#group__cupti__activity__api_1ga8c40b23a5fe82862b18d60c5c42399a8).

-
union
[CUpti_ActivityMemory2](https://docs.nvidia.com#_CPPv421CUpti_ActivityMemory2)::[anonymous]::[anonymous] pool[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemory24poolE) The size of the memory pool in bytes and the processID of the memory pool.

`size`

is valid if`memoryPoolType`

is CUPTI_ACTIVITY_MEMORY_POOL_TYPE_LOCAL,[CUpti_ActivityMemoryPoolType](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#group__cupti__activity__api_1ga8c40b23a5fe82862b18d60c5c42399a8).`processId`

is valid if`memoryPoolType`

is CUPTI_ACTIVITY_MEMORY_POOL_TYPE_IMPORTED,[CUpti_ActivityMemoryPoolType](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#group__cupti__activity__api_1ga8c40b23a5fe82862b18d60c5c42399a8).

-
struct
[CUpti_ActivityMemory2](https://docs.nvidia.com#_CPPv421CUpti_ActivityMemory2)::[anonymous] memoryPoolConfig[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemory216memoryPoolConfigE) The memory pool configuration used for the memory operations.


-