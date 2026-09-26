source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityMemcpy3.html

# 7.74. CUpti_ActivityMemcpy3[#](https://docs.nvidia.com#cupti-activitymemcpy3)

-
struct CUpti_ActivityMemcpy3
[#](https://docs.nvidia.com#_CPPv421CUpti_ActivityMemcpy3) The activity record for memory copies.

(deprecated in CUDA 11.1)

This activity record represents a memory copy (CUPTI_ACTIVITY_KIND_MEMCPY).

Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemcpy34kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_MEMCPY.


-
uint8_t copyKind
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemcpy38copyKindE) The kind of the memory copy, stored as a byte to reduce record size.

See also


-
uint8_t srcKind
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemcpy37srcKindE) The source memory kind read by the memory copy, stored as a byte to reduce record size.

See also


-
uint8_t dstKind
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemcpy37dstKindE) The destination memory kind read by the memory copy, stored as a byte to reduce record size.

See also


-
uint8_t flags
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemcpy35flagsE) The flags associated with the memory copy.

See also


-
uint64_t bytes
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemcpy35bytesE) The number of bytes transferred by the memory copy.


-
uint64_t start
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemcpy35startE) The start timestamp for the memory copy, in ns.

A value of 0 for both the start and end timestamps indicates that timestamp information could not be collected for the memory copy.


-
uint64_t end
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemcpy33endE) The end timestamp for the memory copy, in ns.

A value of 0 for both the start and end timestamps indicates that timestamp information could not be collected for the memory copy.


-
uint32_t deviceId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemcpy38deviceIdE) The ID of the device where the memory copy is occurring.


-
uint32_t contextId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemcpy39contextIdE) The ID of the context where the memory copy is occurring.


-
uint32_t streamId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemcpy38streamIdE) The ID of the stream where the memory copy is occurring.


-
uint32_t correlationId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemcpy313correlationIdE) The correlation ID of the memory copy.

Each memory copy is assigned a unique correlation ID that is identical to the correlation ID in the driver API activity record that launched the memory copy.


-
uint32_t runtimeCorrelationId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemcpy320runtimeCorrelationIdE) The runtime correlation ID of the memory copy.

Each memory copy is assigned a unique runtime correlation ID that is identical to the correlation ID in the runtime API activity record that launched the memory copy.


-
uint32_t pad
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemcpy33padE) Undefined.

Reserved for internal use.


-
void *reserved0
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemcpy39reserved0E) Undefined.

Reserved for internal use.


-
uint64_t graphNodeId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemcpy311graphNodeIdE) The unique ID of the graph node that executed this memcpy through graph launch.

This field will be 0 if the memcpy is not done through graph launch.


-