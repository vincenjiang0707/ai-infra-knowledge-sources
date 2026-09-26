source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityOverheadCommandBufferFullData.html

# 7.114. CUpti_ActivityOverheadCommandBufferFullData[#](https://docs.nvidia.com#cupti-activityoverheadcommandbufferfulldata)

-
struct CUpti_ActivityOverheadCommandBufferFullData
[#](https://docs.nvidia.com#_CPPv443CUpti_ActivityOverheadCommandBufferFullData) The structure to provide additional data for CUPTI_ACTIVITY_OVERHEAD_COMMAND_BUFFER_FULL.

Public Members

-
uint32_t commandBufferLength
[#](https://docs.nvidia.com#_CPPv4N43CUpti_ActivityOverheadCommandBufferFullData19commandBufferLengthE) The remaining space in the command buffer.

This field will always be zero when the command buffer is full, making it not useful in such cases.


-
uint32_t channelID
[#](https://docs.nvidia.com#_CPPv4N43CUpti_ActivityOverheadCommandBufferFullData9channelIDE) The channel ID of the command buffer.


-
uint32_t channelType
[#](https://docs.nvidia.com#_CPPv4N43CUpti_ActivityOverheadCommandBufferFullData11channelTypeE) The channel type of the command buffer.


-
uint32_t commandBufferLength