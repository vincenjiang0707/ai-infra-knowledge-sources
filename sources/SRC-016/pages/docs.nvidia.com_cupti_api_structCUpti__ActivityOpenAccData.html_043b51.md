source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityOpenAccData.html

# 7.107. CUpti_ActivityOpenAccData[#](https://docs.nvidia.com#cupti-activityopenaccdata)

-
struct CUpti_ActivityOpenAccData
[#](https://docs.nvidia.com#_CPPv425CUpti_ActivityOpenAccData) The activity record for OpenACC data.

(CUPTI_ACTIVITY_KIND_OPENACC_DATA).

Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityOpenAccData4kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_OPENACC_DATA.


-
[CUpti_OpenAccEventKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv422CUpti_OpenAccEventKind)eventKind[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityOpenAccData9eventKindE) CUPTI OpenACC event kind (.

See also


-
uint32_t threadId
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityOpenAccData8threadIdE) ThreadId.


-
uint64_t start
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityOpenAccData5startE) CUPTI start timestamp.


-
uint64_t end
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityOpenAccData3endE) CUPTI end timestamp.


-
uint32_t cuDeviceId
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityOpenAccData10cuDeviceIdE) CUDA device id Valid only if deviceType is acc_device_nvidia.


-
uint32_t cuContextId
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityOpenAccData11cuContextIdE) CUDA context id Valid only if deviceType is acc_device_nvidia.


-
uint32_t cuStreamId
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityOpenAccData10cuStreamIdE) CUDA stream id Valid only if deviceType is acc_device_nvidia.


-
uint32_t cuProcessId
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityOpenAccData11cuProcessIdE) The ID of the process where the OpenACC activity is executing.


-
uint32_t cuThreadId
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityOpenAccData10cuThreadIdE) The ID of the thread where the OpenACC activity is executing.


-
uint32_t externalId
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityOpenAccData10externalIdE) The OpenACC correlation ID.

Valid only if deviceType is acc_device_nvidia. If not 0, it uniquely identifies this record. It is identical to the externalId in the preceding external correlation record of type CUPTI_EXTERNAL_CORRELATION_KIND_OPENACC.


-
uint64_t bytes
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityOpenAccData5bytesE) Number of bytes.


-
uint64_t hostPtr
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityOpenAccData7hostPtrE) Host pointer if available.


-
uint64_t devicePtr
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityOpenAccData9devicePtrE) Device pointer if available.


-