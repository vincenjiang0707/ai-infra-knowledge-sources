source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityMemDecompress.html

# 7.72. CUpti_ActivityMemDecompress[#](https://docs.nvidia.com#cupti-activitymemdecompress)

-
struct CUpti_ActivityMemDecompress
[#](https://docs.nvidia.com#_CPPv427CUpti_ActivityMemDecompress) The activity record for trace of decompression operations.

This activity record represents execution for a batch of decompression operatios. The activity kind is CUPTI_ACTIVITY_KIND_MEM_DECOMPRESS

Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N27CUpti_ActivityMemDecompress4kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_MEM_DECOMPRESS.


-
uint32_t deviceId
[#](https://docs.nvidia.com#_CPPv4N27CUpti_ActivityMemDecompress8deviceIdE) The ID of the device.


-
uint32_t contextId
[#](https://docs.nvidia.com#_CPPv4N27CUpti_ActivityMemDecompress9contextIdE) The ID of the context.


-
uint32_t streamId
[#](https://docs.nvidia.com#_CPPv4N27CUpti_ActivityMemDecompress8streamIdE) The ID of the stream.


-
uint32_t channelID
[#](https://docs.nvidia.com#_CPPv4N27CUpti_ActivityMemDecompress9channelIDE) The ID of the HW channel on which the memory copy is occurring.


-
[CUpti_ChannelType](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv417CUpti_ChannelType)channelType[#](https://docs.nvidia.com#_CPPv4N27CUpti_ActivityMemDecompress11channelTypeE) The type of the channel.


-
uint32_t correlationId
[#](https://docs.nvidia.com#_CPPv4N27CUpti_ActivityMemDecompress13correlationIdE) The correlation ID of the decompression operations.

Each operation is assigned a unique correlation ID that is identical to the correlation ID in the driver API activity record that launched the operation.


-
uint32_t numberOfOperations
[#](https://docs.nvidia.com#_CPPv4N27CUpti_ActivityMemDecompress18numberOfOperationsE) The number of operations in the batch.


-
uint64_t sourceBytes
[#](https://docs.nvidia.com#_CPPv4N27CUpti_ActivityMemDecompress11sourceBytesE) The number of bytes to be read and decompressed in the batch operation.


-
void *reserved0
[#](https://docs.nvidia.com#_CPPv4N27CUpti_ActivityMemDecompress9reserved0E) This field is reserved for internal use.


-
uint64_t start
[#](https://docs.nvidia.com#_CPPv4N27CUpti_ActivityMemDecompress5startE) The start timestamp.

A value of CUPTI_TIMESTAMP_UNKNOWN indicates that the start time is unknown.


-
uint64_t end
[#](https://docs.nvidia.com#_CPPv4N27CUpti_ActivityMemDecompress3endE) The end timestamp.

A value of CUPTI_TIMESTAMP_UNKNOWN indicates that the start time is unknown.


-