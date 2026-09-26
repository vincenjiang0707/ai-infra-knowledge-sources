source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityMemory4.html

# 7.86. CUpti_ActivityMemory4[#](https://docs.nvidia.com#cupti-activitymemory4)

-
struct CUpti_ActivityMemory4
[#](https://docs.nvidia.com#_CPPv421CUpti_ActivityMemory4) The activity record for memory.

This activity record represents a memory allocation and free operation (CUPTI_ACTIVITY_KIND_MEMORY2). This activity record provides separate records for memory allocation and memory release operations. This allows to correlate the corresponding driver and runtime API activity record with the memory operation.

Note: This activity record is an upgrade over

[CUpti_ActivityMemory](https://docs.nvidia.com/structCUpti__ActivityMemory.html#structcupti__activitymemory)enabled using the kind[CUPTI_ACTIVITY_KIND_MEMORY](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#group__cupti__activity__api_1ggaefed720d5a60c3e8b286cd386c4913e3afee93ef030088d7a992a1abd6d6e53b0).[CUpti_ActivityMemory](https://docs.nvidia.com/structCUpti__ActivityMemory.html#structcupti__activitymemory)provides a single record for the memory allocation and memory release operations.Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemory44kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_MEMORY2.


-
[CUpti_ActivityMemoryOperationType](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv433CUpti_ActivityMemoryOperationType)memoryOperationType[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemory419memoryOperationTypeE) The memory operation requested by the user,

[CUpti_ActivityMemoryOperationType](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#group__cupti__activity__api_1ga6404b89cfbbd60e04204244d230b15c4).

-
[CUpti_ActivityMemoryKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv424CUpti_ActivityMemoryKind)memoryKind[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemory410memoryKindE) The memory kind requested by the user,

[CUpti_ActivityMemoryKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#group__cupti__activity__api_1ga9969b86f0e54989b27080dc6083263bc).

-
uint32_t correlationId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemory413correlationIdE) The correlation ID of the memory operation.

Each memory operation is assigned a unique correlation ID that is identical to the correlation ID in the driver and runtime API activity record that launched the memory operation.


-
uint64_t address
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemory47addressE) The virtual address of the allocation.

The base address of the memory pool.


-
uint64_t bytes
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemory45bytesE) The number of bytes of memory allocated.


-
uint64_t timestamp
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemory49timestampE) The start timestamp for the memory operation, in ns.


-
uint64_t PC
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemory42PCE) The program counter of the memory operation.


-
uint32_t processId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemory49processIdE) The ID of the process to which this record belongs to.


-
uint32_t deviceId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemory48deviceIdE) The ID of the device where the memory operation is taking place.


-
uint32_t contextId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemory49contextIdE) The ID of the context.

If context is NULL,

`contextId`

is set to CUPTI_INVALID_CONTEXT_ID.

-
uint32_t streamId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemory48streamIdE) The ID of the stream.

If memory operation is not async,

`streamId`

is set to CUPTI_INVALID_STREAM_ID.

-
const char *name
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemory44nameE) Variable name.

This name is shared across all activity records representing the same symbol, and so should not be modified.


-
uint32_t isAsync
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemory47isAsyncE) `isAsync`

is set if memory operation happens through async memory APIs.

-
uint32_t pad1
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemory44pad1E) Undefined.

Reserved for internal use.


-
[CUpti_ActivityMemoryPoolType](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv428CUpti_ActivityMemoryPoolType)memoryPoolType[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemory414memoryPoolTypeE) The type of the memory pool,

[CUpti_ActivityMemoryPoolType](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#group__cupti__activity__api_1ga8c40b23a5fe82862b18d60c5c42399a8).

-
uint32_t pad2
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemory44pad2E) Undefined.

Reserved for internal use.


-
uint64_t releaseThreshold
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemory416releaseThresholdE) The release threshold of the memory pool in bytes.

`releaseThreshold`

is valid for CUPTI_ACTIVITY_MEMORY_POOL_TYPE_LOCAL,[CUpti_ActivityMemoryPoolType](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#group__cupti__activity__api_1ga8c40b23a5fe82862b18d60c5c42399a8).

-
union
[CUpti_ActivityMemory4](https://docs.nvidia.com#_CPPv421CUpti_ActivityMemory4)::[anonymous]::[anonymous] pool[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemory44poolE) The size of memory pool in bytes and the processId of the memory pools

`size`

is valid if`memoryPoolType`

is CUPTI_ACTIVITY_MEMORY_POOL_TYPE_LOCAL,[CUpti_ActivityMemoryPoolType](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#group__cupti__activity__api_1ga8c40b23a5fe82862b18d60c5c42399a8).`processId`

is valid if`memoryPoolType`

is CUPTI_ACTIVITY_MEMORY_POOL_TYPE_IMPORTED,[CUpti_ActivityMemoryPoolType](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#group__cupti__activity__api_1ga8c40b23a5fe82862b18d60c5c42399a8)

-
uint64_t utilizedSize
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemory412utilizedSizeE) The utilized size of the memory pool.

`utilizedSize`

is valid for CUPTI_ACTIVITY_MEMORY_POOL_TYPE_LOCAL,[CUpti_ActivityMemoryPoolType](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#group__cupti__activity__api_1ga8c40b23a5fe82862b18d60c5c42399a8).

-
struct
[CUpti_ActivityMemory4](https://docs.nvidia.com#_CPPv421CUpti_ActivityMemory4)::[anonymous] memoryPoolConfig[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemory416memoryPoolConfigE) The memory pool configuration used for the memory operations.


-
const char *source
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemory46sourceE) The shared object or binary that the memory allocation request comes from.


-