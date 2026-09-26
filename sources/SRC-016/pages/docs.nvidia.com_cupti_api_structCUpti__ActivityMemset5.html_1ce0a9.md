source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityMemset5.html

# 7.94. CUpti_ActivityMemset5[#](https://docs.nvidia.com#cupti-activitymemset5)

-
struct CUpti_ActivityMemset5
[#](https://docs.nvidia.com#_CPPv421CUpti_ActivityMemset5) The activity record for memset (version 5).

This activity record represents a memory set operation (CUPTI_ACTIVITY_KIND_MEMSET).

Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemset54kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_MEMSET.


-
uint32_t value
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemset55valueE) The value being assigned to memory by the memory set.


-
uint64_t bytes
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemset55bytesE) The number of bytes being set by the memory set.


-
uint64_t start
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemset55startE) The start timestamp for the memory set, in ns.

A value of 0 for both the start and end timestamps indicates that timestamp information could not be collected for the memory set.


-
uint64_t end
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemset53endE) The end timestamp for the memory set, in ns.

A value of 0 for both the start and end timestamps indicates that timestamp information could not be collected for the memory set.


-
uint32_t deviceId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemset58deviceIdE) The ID of the device where the memory set is occurring.


-
uint32_t contextId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemset59contextIdE) The ID of the context where the memory set is occurring.


-
uint32_t streamId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemset58streamIdE) The ID of the stream where the memory set is occurring.


-
uint32_t correlationId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemset513correlationIdE) The correlation ID of the memory set.

Each memory set is assigned a unique correlation ID that is identical to the correlation ID in the driver API activity record that launched the memory set.


-
uint16_t flags
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemset55flagsE) The flags associated with the memset.

See also


-
uint16_t memoryKind
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemset510memoryKindE) The memory kind of the memory set.

See also


-
uint32_t pad
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemset53padE) Undefined.

Reserved for internal use.


-
void *reserved0
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemset59reserved0E) Undefined.

Reserved for internal use.


-
uint64_t graphNodeId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemset511graphNodeIdE) The unique ID of the graph node that executed this memset through graph launch.

This field will be 0 if the memset is not executed through graph launch.


-
uint32_t graphId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemset57graphIdE) The unique ID of the graph that executed this memset through graph launch.

This field will be 0 if the memset is not executed through graph launch.


-
uint32_t channelID
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemset59channelIDE) The ID of the HW channel on which the memory set is occurring.


-
[CUpti_ChannelType](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv417CUpti_ChannelType)channelType[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemset511channelTypeE) The type of the channel.


-
uint8_t isDeviceLaunched
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemset516isDeviceLaunchedE) This field is used to indicate if the memset operation is part of a device graph launch.


-
uint8_t pad2[3]
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemset54pad2E) Undefined.

Reserved for internal use


-
uint32_t sourceGraphId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemset513sourceGraphIdE) The unique graph ID of the node from which the memset node was instantiated or last updated.

This field will be 0 if the memset is not launched through graph launch APIs.


-
uint32_t pad3
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemset54pad3E) Undefined.

Reserved for internal use


-
uint64_t sourceGraphNodeId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityMemset517sourceGraphNodeIdE) The unique graph node ID of the node from which the memset node was instantiated or last updated.

This field will be 0 if the memset is not launched through graph launch APIs.


-