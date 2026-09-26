source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityMemcpyPtoP2.html

# 7.80. CUpti_ActivityMemcpyPtoP2[#](https://docs.nvidia.com#cupti-activitymemcpyptop2)

-
struct CUpti_ActivityMemcpyPtoP2
[#](https://docs.nvidia.com#_CPPv425CUpti_ActivityMemcpyPtoP2) The activity record for peer-to-peer memory copies.

(deprecated in CUDA 11.1)

This activity record represents a peer-to-peer memory copy (CUPTI_ACTIVITY_KIND_MEMCPY2).

Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityMemcpyPtoP24kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_MEMCPY2.


-
uint8_t copyKind
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityMemcpyPtoP28copyKindE) The kind of the memory copy, stored as a byte to reduce record size.

See also


-
uint8_t srcKind
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityMemcpyPtoP27srcKindE) The source memory kind read by the memory copy, stored as a byte to reduce record size.

See also


-
uint8_t dstKind
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityMemcpyPtoP27dstKindE) The destination memory kind read by the memory copy, stored as a byte to reduce record size.

See also


-
uint8_t flags
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityMemcpyPtoP25flagsE) The flags associated with the memory copy.

See also


-
uint64_t bytes
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityMemcpyPtoP25bytesE) The number of bytes transferred by the memory copy.


-
uint64_t start
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityMemcpyPtoP25startE) The start timestamp for the memory copy, in ns.

A value of 0 for both the start and end timestamps indicates that timestamp information could not be collected for the memory copy.


-
uint64_t end
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityMemcpyPtoP23endE) The end timestamp for the memory copy, in ns.

A value of 0 for both the start and end timestamps indicates that timestamp information could not be collected for the memory copy.


-
uint32_t deviceId
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityMemcpyPtoP28deviceIdE) The ID of the device where the memory copy is occurring.


-
uint32_t contextId
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityMemcpyPtoP29contextIdE) The ID of the context where the memory copy is occurring.


-
uint32_t streamId
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityMemcpyPtoP28streamIdE) The ID of the stream where the memory copy is occurring.


-
uint32_t srcDeviceId
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityMemcpyPtoP211srcDeviceIdE) The ID of the device where memory is being copied from.


-
uint32_t srcContextId
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityMemcpyPtoP212srcContextIdE) The ID of the context owning the memory being copied from.


-
uint32_t dstDeviceId
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityMemcpyPtoP211dstDeviceIdE) The ID of the device where memory is being copied to.


-
uint32_t dstContextId
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityMemcpyPtoP212dstContextIdE) The ID of the context owning the memory being copied to.


-
uint32_t correlationId
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityMemcpyPtoP213correlationIdE) The correlation ID of the memory copy.

Each memory copy is assigned a unique correlation ID that is identical to the correlation ID in the driver and runtime API activity record that launched the memory copy.


-
void *reserved0
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityMemcpyPtoP29reserved0E) Undefined.

Reserved for internal use.


-
uint64_t graphNodeId
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityMemcpyPtoP211graphNodeIdE) The unique ID of the graph node that executed the memcpy through graph launch.

This field will be 0 if memcpy is not done using graph launch.


-