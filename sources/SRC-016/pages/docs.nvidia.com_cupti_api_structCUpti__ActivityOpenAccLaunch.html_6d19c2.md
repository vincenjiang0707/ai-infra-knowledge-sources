source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityOpenAccLaunch.html

# 7.108. CUpti_ActivityOpenAccLaunch[#](https://docs.nvidia.com#cupti-activityopenacclaunch)

-
struct CUpti_ActivityOpenAccLaunch
[#](https://docs.nvidia.com#_CPPv427CUpti_ActivityOpenAccLaunch) The activity record for OpenACC launch.

(CUPTI_ACTIVITY_KIND_OPENACC_LAUNCH).

Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N27CUpti_ActivityOpenAccLaunch4kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_OPENACC_LAUNCH.


-
[CUpti_OpenAccEventKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv422CUpti_OpenAccEventKind)eventKind[#](https://docs.nvidia.com#_CPPv4N27CUpti_ActivityOpenAccLaunch9eventKindE) CUPTI OpenACC event kind (.

See also


-
[CUpti_OpenAccConstructKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv426CUpti_OpenAccConstructKind)parentConstruct[#](https://docs.nvidia.com#_CPPv4N27CUpti_ActivityOpenAccLaunch15parentConstructE) CUPTI OpenACC parent construct kind (.

Note that for applications using PGI OpenACC runtime < 16.1, this will always be CUPTI_OPENACC_CONSTRUCT_KIND_UNKNOWN.

See also


-
uint32_t version
[#](https://docs.nvidia.com#_CPPv4N27CUpti_ActivityOpenAccLaunch7versionE) Version number.


-
uint32_t implicit
[#](https://docs.nvidia.com#_CPPv4N27CUpti_ActivityOpenAccLaunch8implicitE) 1 for any implicit event, such as an implicit wait at a synchronous data construct 0 otherwise


-
uint32_t deviceType
[#](https://docs.nvidia.com#_CPPv4N27CUpti_ActivityOpenAccLaunch10deviceTypeE) Device type.


-
uint32_t deviceNumber
[#](https://docs.nvidia.com#_CPPv4N27CUpti_ActivityOpenAccLaunch12deviceNumberE) Device number.


-
uint32_t threadId
[#](https://docs.nvidia.com#_CPPv4N27CUpti_ActivityOpenAccLaunch8threadIdE) ThreadId.


-
uint64_t asyncMap
[#](https://docs.nvidia.com#_CPPv4N27CUpti_ActivityOpenAccLaunch8asyncMapE) Internal asynchronous queue number used.


-
uint32_t lineNo
[#](https://docs.nvidia.com#_CPPv4N27CUpti_ActivityOpenAccLaunch6lineNoE) The line number of the directive or program construct or the starting line number of the OpenACC construct corresponding to the event.

A negative or zero value means the line number is not known.


-
uint32_t endLineNo
[#](https://docs.nvidia.com#_CPPv4N27CUpti_ActivityOpenAccLaunch9endLineNoE) For an OpenACC construct, this contains the line number of the end of the construct.

A negative or zero value means the line number is not known.


-
uint32_t funcLineNo
[#](https://docs.nvidia.com#_CPPv4N27CUpti_ActivityOpenAccLaunch10funcLineNoE) The line number of the first line of the function named in func_name.

A negative or zero value means the line number is not known.


-
uint32_t funcEndLineNo
[#](https://docs.nvidia.com#_CPPv4N27CUpti_ActivityOpenAccLaunch13funcEndLineNoE) The last line number of the function named in func_name.

A negative or zero value means the line number is not known.


-
uint64_t start
[#](https://docs.nvidia.com#_CPPv4N27CUpti_ActivityOpenAccLaunch5startE) CUPTI start timestamp.


-
uint64_t end
[#](https://docs.nvidia.com#_CPPv4N27CUpti_ActivityOpenAccLaunch3endE) CUPTI end timestamp.


-
uint32_t cuDeviceId
[#](https://docs.nvidia.com#_CPPv4N27CUpti_ActivityOpenAccLaunch10cuDeviceIdE) CUDA device id Valid only if deviceType is acc_device_nvidia.


-
uint32_t cuContextId
[#](https://docs.nvidia.com#_CPPv4N27CUpti_ActivityOpenAccLaunch11cuContextIdE) CUDA context id Valid only if deviceType is acc_device_nvidia.


-
uint32_t cuStreamId
[#](https://docs.nvidia.com#_CPPv4N27CUpti_ActivityOpenAccLaunch10cuStreamIdE) CUDA stream id Valid only if deviceType is acc_device_nvidia.


-
uint32_t cuProcessId
[#](https://docs.nvidia.com#_CPPv4N27CUpti_ActivityOpenAccLaunch11cuProcessIdE) The ID of the process where the OpenACC activity is executing.


-
uint32_t cuThreadId
[#](https://docs.nvidia.com#_CPPv4N27CUpti_ActivityOpenAccLaunch10cuThreadIdE) The ID of the thread where the OpenACC activity is executing.


-
uint32_t externalId
[#](https://docs.nvidia.com#_CPPv4N27CUpti_ActivityOpenAccLaunch10externalIdE) The OpenACC correlation ID.

Valid only if deviceType is acc_device_nvidia. If not 0, it uniquely identifies this record. It is identical to the externalId in the preceding external correlation record of type CUPTI_EXTERNAL_CORRELATION_KIND_OPENACC.


-
const char *srcFile
[#](https://docs.nvidia.com#_CPPv4N27CUpti_ActivityOpenAccLaunch7srcFileE) A pointer to null-terminated string containing the name of or path to the source file, if known, or a null pointer if not.


-
const char *funcName
[#](https://docs.nvidia.com#_CPPv4N27CUpti_ActivityOpenAccLaunch8funcNameE) A pointer to a null-terminated string containing the name of the function in which the event occurred.


-
uint64_t numGangs
[#](https://docs.nvidia.com#_CPPv4N27CUpti_ActivityOpenAccLaunch8numGangsE) The number of gangs created for this kernel launch.


-
uint64_t numWorkers
[#](https://docs.nvidia.com#_CPPv4N27CUpti_ActivityOpenAccLaunch10numWorkersE) The number of workers created for this kernel launch.


-
uint64_t vectorLength
[#](https://docs.nvidia.com#_CPPv4N27CUpti_ActivityOpenAccLaunch12vectorLengthE) The number of vector lanes created for this kernel launch.


-
const char *kernelName
[#](https://docs.nvidia.com#_CPPv4N27CUpti_ActivityOpenAccLaunch10kernelNameE) A pointer to null-terminated string containing the name of the kernel being launched, if known, or a null pointer if not.


-