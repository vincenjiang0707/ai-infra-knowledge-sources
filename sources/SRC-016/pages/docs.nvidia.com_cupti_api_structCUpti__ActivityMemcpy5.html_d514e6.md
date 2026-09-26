source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityMemcpy5.html

# 7.76. CUpti_ActivityMemcpy5[#](https://docs.nvidia.com#cupti-activitymemcpy5)

-
struct CUpti_ActivityMemcpy5
[#](https://docs.nvidia.com#_CPPv421CUpti_ActivityMemcpy5) The activity record for memory copies.

This activity record represents a memory copy (CUPTI_ACTIVITY_KIND_MEMCPY).

Structure deprecated in CUDA 12.8: Refer to

[CUpti_ActivityMemcpy6](https://docs.nvidia.com/structCUpti__ActivityMemcpy6.html#structcupti__activitymemcpy6)for the latest structure.Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemcpy54kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_MEMCPY.


-
uint8_t copyKind
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemcpy58copyKindE) The kind of the memory copy, stored as a byte to reduce record size.

See also


-
uint8_t srcKind
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemcpy57srcKindE) The source memory kind read by the memory copy, stored as a byte to reduce record size.

See also


-
uint8_t dstKind
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemcpy57dstKindE) The destination memory kind read by the memory copy, stored as a byte to reduce record size.

See also


-
uint8_t flags
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemcpy55flagsE) The flags associated with the memory copy.

See also


-
uint64_t bytes
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemcpy55bytesE) The number of bytes transferred by the memory copy.


-
uint64_t start
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemcpy55startE) The start timestamp for the memory copy, in ns.

A value of 0 for both the start and end timestamps indicates that timestamp information could not be collected for the memory copy.


-
uint64_t end
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemcpy53endE) The end timestamp for the memory copy, in ns.

A value of 0 for both the start and end timestamps indicates that timestamp information could not be collected for the memory copy.


-
uint32_t deviceId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemcpy58deviceIdE) The ID of the device where the memory copy is occurring.


-
uint32_t contextId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemcpy59contextIdE) The ID of the context where the memory copy is occurring.


-
uint32_t streamId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemcpy58streamIdE) The ID of the stream where the memory copy is occurring.


-
uint32_t correlationId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemcpy513correlationIdE) The correlation ID of the memory copy.

Each memory copy is assigned a unique correlation ID that is identical to the correlation ID in the driver API activity record that launched the memory copy.


-
uint32_t runtimeCorrelationId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemcpy520runtimeCorrelationIdE) The runtime correlation ID of the memory copy.

Each memory copy is assigned a unique runtime correlation ID that is identical to the correlation ID in the runtime API activity record that launched the memory copy.


-
uint32_t pad
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemcpy53padE) Undefined.

Reserved for internal use.


-
void *reserved0
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemcpy59reserved0E) Undefined.

Reserved for internal use.


-
uint64_t graphNodeId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemcpy511graphNodeIdE) The unique ID of the graph node that executed this memcpy through graph launch.

This field will be 0 if the memcpy is not done through graph launch.


-
uint32_t graphId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemcpy57graphIdE) The unique ID of the graph that executed this memcpy through graph launch.

This field will be 0 if the memcpy is not done through graph launch.


-
uint32_t channelID
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemcpy59channelIDE) The ID of the HW channel on which the memory copy is occurring.


-
[CUpti_ChannelType](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv417CUpti_ChannelType)channelType[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemcpy511channelTypeE) The type of the channel.


-
uint32_t pad2
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemcpy54pad2E) Reserved for internal use.


-