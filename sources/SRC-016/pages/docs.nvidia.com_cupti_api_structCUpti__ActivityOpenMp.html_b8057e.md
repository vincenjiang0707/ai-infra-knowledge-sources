source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityOpenMp.html

# 7.110. CUpti_ActivityOpenMp[#](https://docs.nvidia.com#cupti-activityopenmp)

-
struct CUpti_ActivityOpenMp
[#](https://docs.nvidia.com#_CPPv420CUpti_ActivityOpenMp) The base activity record for OpenMp records.

See also

Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityOpenMp4kindE) The kind of this activity.


-
[CUpti_OpenMpEventKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv421CUpti_OpenMpEventKind)eventKind[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityOpenMp9eventKindE) CUPTI OpenMP event kind (.

See also

CUpti_OpenMpEventKind)


-
uint32_t version
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityOpenMp7versionE) Version number.


-
uint32_t threadId
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityOpenMp8threadIdE) ThreadId.


-
uint64_t start
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityOpenMp5startE) CUPTI start timestamp.


-
uint64_t end
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityOpenMp3endE) CUPTI end timestamp.


-
uint32_t cuProcessId
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityOpenMp11cuProcessIdE) The ID of the process where the OpenMP activity is executing.


-
uint32_t cuThreadId
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityOpenMp10cuThreadIdE) The ID of the thread where the OpenMP activity is executing.


-