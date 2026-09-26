source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityOpenAcc.html

# 7.106. CUpti_ActivityOpenAcc[#](https://docs.nvidia.com#cupti-activityopenacc)

-
struct CUpti_ActivityOpenAcc
[#](https://docs.nvidia.com#_CPPv421CUpti_ActivityOpenAcc) The base activity record for OpenAcc records.

The OpenACC activity API part uses a

[CUpti_ActivityOpenAcc](https://docs.nvidia.com#structcupti__activityopenacc)as a generic representation for any OpenACC activity. The ‘kind’ field is used to determine the specific activity kind, and from that the[CUpti_ActivityOpenAcc](https://docs.nvidia.com#structcupti__activityopenacc)object can be cast to the specific OpenACC activity record type appropriate for that kind.Note that all OpenACC activity record types are padded and aligned to ensure that each member of the record is naturally aligned.

See also

Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityOpenAcc4kindE) The kind of this activity.


-
[CUpti_OpenAccEventKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv422CUpti_OpenAccEventKind)eventKind[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityOpenAcc9eventKindE) CUPTI OpenACC event kind (.

See also


-
[CUpti_OpenAccConstructKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv426CUpti_OpenAccConstructKind)parentConstruct[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityOpenAcc15parentConstructE) CUPTI OpenACC parent construct kind (.

Note that for applications using PGI OpenACC runtime < 16.1, this will always be CUPTI_OPENACC_CONSTRUCT_KIND_UNKNOWN.

See also


-
uint32_t version
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityOpenAcc7versionE) Version number.


-
uint32_t implicit
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityOpenAcc8implicitE) 1 for any implicit event, such as an implicit wait at a synchronous data construct 0 otherwise


-
uint32_t deviceType
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityOpenAcc10deviceTypeE) Device type.


-
uint32_t deviceNumber
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityOpenAcc12deviceNumberE) Device number.


-
uint32_t threadId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityOpenAcc8threadIdE) ThreadId.


-
uint64_t asyncMap
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityOpenAcc8asyncMapE) Internal asynchronous queue number used.


-
uint32_t lineNo
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityOpenAcc6lineNoE) The line number of the directive or program construct or the starting line number of the OpenACC construct corresponding to the event.

A zero value means the line number is not known.


-
uint32_t endLineNo
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityOpenAcc9endLineNoE) For an OpenACC construct, this contains the line number of the end of the construct.

A zero value means the line number is not known.


-
uint32_t funcLineNo
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityOpenAcc10funcLineNoE) The line number of the first line of the function named in funcName.

A zero value means the line number is not known.


-
uint32_t funcEndLineNo
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityOpenAcc13funcEndLineNoE) The last line number of the function named in funcName.

A zero value means the line number is not known.


-
uint64_t start
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityOpenAcc5startE) CUPTI start timestamp.


-
uint64_t end
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityOpenAcc3endE) CUPTI end timestamp.


-
uint32_t cuDeviceId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityOpenAcc10cuDeviceIdE) CUDA device id Valid only if deviceType is acc_device_nvidia.


-
uint32_t cuContextId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityOpenAcc11cuContextIdE) CUDA context id Valid only if deviceType is acc_device_nvidia.


-
uint32_t cuStreamId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityOpenAcc10cuStreamIdE) CUDA stream id Valid only if deviceType is acc_device_nvidia.


-
uint32_t cuProcessId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityOpenAcc11cuProcessIdE) The ID of the process where the OpenACC activity is executing.


-
uint32_t cuThreadId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityOpenAcc10cuThreadIdE) The ID of the thread where the OpenACC activity is executing.


-
uint32_t externalId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityOpenAcc10externalIdE) The OpenACC correlation ID.

Valid only if deviceType is acc_device_nvidia. If not 0, it uniquely identifies this record. It is identical to the externalId in the preceding external correlation record of type CUPTI_EXTERNAL_CORRELATION_KIND_OPENACC.


-