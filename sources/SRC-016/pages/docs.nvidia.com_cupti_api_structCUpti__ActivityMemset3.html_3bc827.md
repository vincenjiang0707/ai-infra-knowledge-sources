source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityMemset3.html

# 7.92. CUpti_ActivityMemset3[#](https://docs.nvidia.com#cupti-activitymemset3)

-
struct CUpti_ActivityMemset3
[#](https://docs.nvidia.com#_CPPv421CUpti_ActivityMemset3) The activity record for memset.

(deprecated in CUDA 11.6)

This activity record represents a memory set operation (CUPTI_ACTIVITY_KIND_MEMSET).

Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemset34kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_MEMSET.


-
uint32_t value
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemset35valueE) The value being assigned to memory by the memory set.


-
uint64_t bytes
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemset35bytesE) The number of bytes being set by the memory set.


-
uint64_t start
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemset35startE) The start timestamp for the memory set, in ns.

A value of 0 for both the start and end timestamps indicates that timestamp information could not be collected for the memory set.


-
uint64_t end
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemset33endE) The end timestamp for the memory set, in ns.

A value of 0 for both the start and end timestamps indicates that timestamp information could not be collected for the memory set.


-
uint32_t deviceId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemset38deviceIdE) The ID of the device where the memory set is occurring.


-
uint32_t contextId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemset39contextIdE) The ID of the context where the memory set is occurring.


-
uint32_t streamId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemset38streamIdE) The ID of the stream where the memory set is occurring.


-
uint32_t correlationId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemset313correlationIdE) The correlation ID of the memory set.

Each memory set is assigned a unique correlation ID that is identical to the correlation ID in the driver API activity record that launched the memory set.


-
uint16_t flags
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemset35flagsE) The flags associated with the memset.

See also


-
uint16_t memoryKind
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemset310memoryKindE) The memory kind of the memory set.

See also


-
uint32_t pad
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemset33padE) Undefined.

Reserved for internal use.


-
void *reserved0
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemset39reserved0E) Undefined.

Reserved for internal use.


-
uint64_t graphNodeId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemset311graphNodeIdE) The unique ID of the graph node that executed this memset through graph launch.

This field will be 0 if the memset is not executed through graph launch.


-
uint32_t graphId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemset37graphIdE) The unique ID of the graph that executed this memset through graph launch.

This field will be 0 if the memset is not executed through graph launch.


-
uint32_t padding
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemset37paddingE) Undefined.

Reserved for internal use.


-