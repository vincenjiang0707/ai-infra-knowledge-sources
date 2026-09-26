source: https://docs.nvidia.com/cupti/api/structCUpti__PCSamplingConfigurationInfo.html

# 7.143. CUpti_PCSamplingConfigurationInfo[#](https://docs.nvidia.com#cupti-pcsamplingconfigurationinfo)

-
struct CUpti_PCSamplingConfigurationInfo
[#](https://docs.nvidia.com#_CPPv433CUpti_PCSamplingConfigurationInfo) PC sampling configuration information structure.

This structure provides

[CUpti_PCSamplingConfigurationAttributeType](https://docs.nvidia.com/group__CUPTI__PCSAMPLING__API.html#group__cupti__pcsampling__api_1ga4fe866bd47d8825f4d46cc52c8e29bb5)which can be configured or queried for PC sampling configurationPublic Members

-
[CUpti_PCSamplingConfigurationAttributeType](https://docs.nvidia.com/group__CUPTI__PCSAMPLING__API.html#_CPPv442CUpti_PCSamplingConfigurationAttributeType)attributeType[#](https://docs.nvidia.com#_CPPv4N33CUpti_PCSamplingConfigurationInfo13attributeTypeE) Refer

[CUpti_PCSamplingConfigurationAttributeType](https://docs.nvidia.com/group__CUPTI__PCSAMPLING__API.html#group__cupti__pcsampling__api_1ga4fe866bd47d8825f4d46cc52c8e29bb5)for all supported attribute types.

-
struct
[CUpti_PCSamplingConfigurationInfo](https://docs.nvidia.com#_CPPv433CUpti_PCSamplingConfigurationInfo)::[anonymous]::[anonymous] invalidData[#](https://docs.nvidia.com#_CPPv4N33CUpti_PCSamplingConfigurationInfo11invalidDataE) Invalid Value.


-
struct
[CUpti_PCSamplingConfigurationInfo](https://docs.nvidia.com#_CPPv433CUpti_PCSamplingConfigurationInfo)::[anonymous]::[anonymous] samplingPeriodData[#](https://docs.nvidia.com#_CPPv4N33CUpti_PCSamplingConfigurationInfo18samplingPeriodDataE) Refer

[CUPTI_PC_SAMPLING_CONFIGURATION_ATTR_TYPE_SAMPLING_PERIOD](https://docs.nvidia.com/group__CUPTI__PCSAMPLING__API.html#group__cupti__pcsampling__api_1gga4fe866bd47d8825f4d46cc52c8e29bb5a5a3304f055fc43b3f1885f2b5fe3d35c).

-
struct
[CUpti_PCSamplingConfigurationInfo](https://docs.nvidia.com#_CPPv433CUpti_PCSamplingConfigurationInfo)::[anonymous]::[anonymous] stallReasonData[#](https://docs.nvidia.com#_CPPv4N33CUpti_PCSamplingConfigurationInfo15stallReasonDataE) Refer

[CUPTI_PC_SAMPLING_CONFIGURATION_ATTR_TYPE_STALL_REASON](https://docs.nvidia.com/group__CUPTI__PCSAMPLING__API.html#group__cupti__pcsampling__api_1gga4fe866bd47d8825f4d46cc52c8e29bb5a6b99e85c0ca755ba6f1e1b68af6de405).

-
struct
[CUpti_PCSamplingConfigurationInfo](https://docs.nvidia.com#_CPPv433CUpti_PCSamplingConfigurationInfo)::[anonymous]::[anonymous] scratchBufferSizeData[#](https://docs.nvidia.com#_CPPv4N33CUpti_PCSamplingConfigurationInfo21scratchBufferSizeDataE) Refer

[CUPTI_PC_SAMPLING_CONFIGURATION_ATTR_TYPE_SCRATCH_BUFFER_SIZE](https://docs.nvidia.com/group__CUPTI__PCSAMPLING__API.html#group__cupti__pcsampling__api_1gga4fe866bd47d8825f4d46cc52c8e29bb5a8f4358cee727885dde3311a81bb996cc).

-
struct
[CUpti_PCSamplingConfigurationInfo](https://docs.nvidia.com#_CPPv433CUpti_PCSamplingConfigurationInfo)::[anonymous]::[anonymous] hardwareBufferSizeData[#](https://docs.nvidia.com#_CPPv4N33CUpti_PCSamplingConfigurationInfo22hardwareBufferSizeDataE) Refer

[CUPTI_PC_SAMPLING_CONFIGURATION_ATTR_TYPE_HARDWARE_BUFFER_SIZE](https://docs.nvidia.com/group__CUPTI__PCSAMPLING__API.html#group__cupti__pcsampling__api_1gga4fe866bd47d8825f4d46cc52c8e29bb5a979e3dbbec977c8141ba3e01b8dbf014).

-
struct
[CUpti_PCSamplingConfigurationInfo](https://docs.nvidia.com#_CPPv433CUpti_PCSamplingConfigurationInfo)::[anonymous]::[anonymous] collectionModeData[#](https://docs.nvidia.com#_CPPv4N33CUpti_PCSamplingConfigurationInfo18collectionModeDataE) Refer

[CUPTI_PC_SAMPLING_CONFIGURATION_ATTR_TYPE_COLLECTION_MODE](https://docs.nvidia.com/group__CUPTI__PCSAMPLING__API.html#group__cupti__pcsampling__api_1gga4fe866bd47d8825f4d46cc52c8e29bb5aa561bd34aebe51eb26e4695ea0d865bb).

-
struct
[CUpti_PCSamplingConfigurationInfo](https://docs.nvidia.com#_CPPv433CUpti_PCSamplingConfigurationInfo)::[anonymous]::[anonymous] enableStartStopControlData[#](https://docs.nvidia.com#_CPPv4N33CUpti_PCSamplingConfigurationInfo26enableStartStopControlDataE) Refer

[CUPTI_PC_SAMPLING_CONFIGURATION_ATTR_TYPE_ENABLE_START_STOP_CONTROL](https://docs.nvidia.com/group__CUPTI__PCSAMPLING__API.html#group__cupti__pcsampling__api_1gga4fe866bd47d8825f4d46cc52c8e29bb5ac75dea72b5908405f9096dd1ae27366b).

-
struct
[CUpti_PCSamplingConfigurationInfo](https://docs.nvidia.com#_CPPv433CUpti_PCSamplingConfigurationInfo)::[anonymous]::[anonymous] outputDataFormatData[#](https://docs.nvidia.com#_CPPv4N33CUpti_PCSamplingConfigurationInfo20outputDataFormatDataE) Refer

[CUPTI_PC_SAMPLING_CONFIGURATION_ATTR_TYPE_OUTPUT_DATA_FORMAT](https://docs.nvidia.com/group__CUPTI__PCSAMPLING__API.html#group__cupti__pcsampling__api_1gga4fe866bd47d8825f4d46cc52c8e29bb5aa19b4a5c74150e029c95a6a320018f6a).

-
struct
[CUpti_PCSamplingConfigurationInfo](https://docs.nvidia.com#_CPPv433CUpti_PCSamplingConfigurationInfo)::[anonymous]::[anonymous] samplingDataBufferData[#](https://docs.nvidia.com#_CPPv4N33CUpti_PCSamplingConfigurationInfo22samplingDataBufferDataE) Refer

[CUPTI_PC_SAMPLING_CONFIGURATION_ATTR_TYPE_SAMPLING_DATA_BUFFER](https://docs.nvidia.com/group__CUPTI__PCSAMPLING__API.html#group__cupti__pcsampling__api_1gga4fe866bd47d8825f4d46cc52c8e29bb5acefa869098e32174b5ed1e8dfd96af06).

-
struct
[CUpti_PCSamplingConfigurationInfo](https://docs.nvidia.com#_CPPv433CUpti_PCSamplingConfigurationInfo)::[anonymous]::[anonymous] workerThreadPeriodicSleepSpanData[#](https://docs.nvidia.com#_CPPv4N33CUpti_PCSamplingConfigurationInfo33workerThreadPeriodicSleepSpanDataE) Refer

[CUPTI_PC_SAMPLING_CONFIGURATION_ATTR_TYPE_WORKER_THREAD_PERIODIC_SLEEP_SPAN](https://docs.nvidia.com/group__CUPTI__PCSAMPLING__API.html#group__cupti__pcsampling__api_1gga4fe866bd47d8825f4d46cc52c8e29bb5a67b78d0e6180a9cb3220e49e6b842748).

-