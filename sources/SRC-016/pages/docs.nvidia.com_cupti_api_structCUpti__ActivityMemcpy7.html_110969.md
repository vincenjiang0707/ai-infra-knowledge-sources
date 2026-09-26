source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityMemcpy7.html

# 7.78. CUpti_ActivityMemcpy7[#](https://docs.nvidia.com#cupti-activitymemcpy7)

-
struct CUpti_ActivityMemcpy7
[#](https://docs.nvidia.com#_CPPv421CUpti_ActivityMemcpy7) The activity record for memory copies (version 7).

This activity record represents a memory copy (CUPTI_ACTIVITY_KIND_MEMCPY).

Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemcpy74kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_MEMCPY.


-
uint8_t copyKind
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemcpy78copyKindE) The kind of the memory copy, stored as a byte to reduce record size.

See also


-
uint8_t srcKind
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemcpy77srcKindE) The source memory kind read by the memory copy, stored as a byte to reduce record size.

See also


-
uint8_t dstKind
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemcpy77dstKindE) The destination memory kind read by the memory copy, stored as a byte to reduce record size.

See also


-
uint8_t flags
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemcpy75flagsE) The flags associated with the memory copy.

See also


-
uint64_t bytes
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemcpy75bytesE) The number of bytes transferred by the memory copy.


-
uint64_t start
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemcpy75startE) The start timestamp for the memory copy, in ns.

A value of 0 for both the start and end timestamps indicates that timestamp information could not be collected for the memory copy.


-
uint64_t end
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemcpy73endE) The end timestamp for the memory copy, in ns.

A value of 0 for both the start and end timestamps indicates that timestamp information could not be collected for the memory copy.


-
uint32_t deviceId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemcpy78deviceIdE) The ID of the device where the memory copy is occurring.


-
uint32_t contextId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemcpy79contextIdE) The ID of the context where the memory copy is occurring.


-
uint32_t streamId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemcpy78streamIdE) The ID of the stream where the memory copy is occurring.


-
uint32_t correlationId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemcpy713correlationIdE) The correlation ID of the memory copy.

Each memory copy is assigned a unique correlation ID that is identical to the correlation ID in the driver API activity record that launched the memory copy.


-
uint32_t runtimeCorrelationId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemcpy720runtimeCorrelationIdE) The runtime correlation ID of the memory copy.

Each memory copy is assigned a unique runtime correlation ID that is identical to the correlation ID in the runtime API activity record that launched the memory copy.


-
uint32_t pad
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemcpy73padE) Undefined.

Reserved for internal use.


-
void *reserved0
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemcpy79reserved0E) Undefined.

Reserved for internal use.


-
uint64_t graphNodeId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemcpy711graphNodeIdE) The unique ID of the graph node that executed this memcpy through graph launch.

This field will be 0 if the memcpy is not done through graph launch.


-
uint32_t graphId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemcpy77graphIdE) The unique ID of the graph that executed this memcpy through graph launch.

This field will be 0 if the memcpy is not done through graph launch.


-
uint32_t channelID
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemcpy79channelIDE) The ID of the HW channel on which the memory copy is occurring.


-
[CUpti_ChannelType](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv417CUpti_ChannelType)channelType[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemcpy711channelTypeE) The type of the channel.


-
uint8_t isDeviceLaunched
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemcpy716isDeviceLaunchedE) This field is used to indicate if the memcpy operation is part of a device graph launch.


-
uint8_t pad2[3]
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemcpy74pad2E) Reserved for internal use.


-
uint64_t copyCount
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemcpy79copyCountE) The total number of memcopy operations traced in this record.

This field is valid for memcpy operations happening using MemcpyBatchAsync APIs in CUDA. In MemcpyBatchAsync APIs, multiple memcpy operations are batched together for optimization purposes based on certain heuristics. For other memcpy operations, this field will be 1.


-
uint32_t sourceGraphId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemcpy713sourceGraphIdE) The unique graph ID of the node from which the memcpy node was instantiated or last updated.

This field will be 0 if the memcpy is not launched through graph launch APIs.


-
uint32_t pad3
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemcpy74pad3E) Reserved for internal use.


-
uint64_t sourceGraphNodeId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemcpy717sourceGraphNodeIdE) The unique graph node ID of the node from which the memcpy node was instantiated or last updated.

This field will be 0 if the memcpy is not launched through graph launch APIs.


-