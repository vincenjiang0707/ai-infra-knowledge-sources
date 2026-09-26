source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityMemory.html

# 7.83. CUpti_ActivityMemory[#](https://docs.nvidia.com#cupti-activitymemory)

-
struct CUpti_ActivityMemory
[#](https://docs.nvidia.com#_CPPv420CUpti_ActivityMemory) The activity record for memory.

This activity record represents a memory allocation and free operation (CUPTI_ACTIVITY_KIND_MEMORY). This activity record provides a single record for the memory allocation and memory release operations.

Note: It is recommended to move to the new activity record

[CUpti_ActivityMemory4](https://docs.nvidia.com/structCUpti__ActivityMemory4.html#structcupti__activitymemory4)enabled using the kind[CUPTI_ACTIVITY_KIND_MEMORY2](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#group__cupti__activity__api_1ggaefed720d5a60c3e8b286cd386c4913e3afc702c2e896e657930de3685d4ea3233).[CUpti_ActivityMemory4](https://docs.nvidia.com/structCUpti__ActivityMemory4.html#structcupti__activitymemory4)provides separate records for memory allocation and memory release operations. This allows to correlate the corresponding driver and runtime API activity record with the memory operation.Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityMemory4kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_MEMORY.


-
[CUpti_ActivityMemoryKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv424CUpti_ActivityMemoryKind)memoryKind[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityMemory10memoryKindE) The memory kind requested by the user.


-
uint64_t address
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityMemory7addressE) The virtual address of the allocation.


-
uint64_t bytes
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityMemory5bytesE) The number of bytes of memory allocated.


-
uint64_t start
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityMemory5startE) The start timestamp for the memory operation, i.e.

the time when memory was allocated, in ns.


-
uint64_t end
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityMemory3endE) The end timestamp for the memory operation, i.e.

the time when memory was freed, in ns. This will be 0 if memory is not freed in the application


-
uint64_t allocPC
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityMemory7allocPCE) The program counter of the allocation of memory.


-
uint64_t freePC
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityMemory6freePCE) The program counter of the freeing of memory.

This will be 0 if memory is not freed in the application


-
uint32_t processId
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityMemory9processIdE) The ID of the process to which this record belongs to.


-
uint32_t deviceId
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityMemory8deviceIdE) The ID of the device where the memory allocation is taking place.


-
uint32_t contextId
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityMemory9contextIdE) The ID of the context.

If context is NULL,

`contextId`

is set to CUPTI_INVALID_CONTEXT_ID.

-
uint32_t pad
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityMemory3padE) Undefined.

Reserved for internal use.


-
const char *name
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityMemory4nameE) Variable name.

This name is shared across all activity records representing the same symbol, and so should not be modified.


-