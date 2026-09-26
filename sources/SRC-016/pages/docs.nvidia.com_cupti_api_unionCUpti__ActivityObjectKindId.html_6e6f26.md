source: https://docs.nvidia.com/cupti/api/unionCUpti__ActivityObjectKindId.html

# 7.105. CUpti_ActivityObjectKindId[#](https://docs.nvidia.com#cupti-activityobjectkindid)

-
union CUpti_ActivityObjectKindId
[#](https://docs.nvidia.com#_CPPv426CUpti_ActivityObjectKindId) *#include </dvs/p4/build/sw/devtools/Agora/Rel/CUDA13.4/Built/Int/rel-pub/linux-desktop-glibc_2_11_3-x64/Shared/Cuda/Modules/Cupti/Inc/cupti_activity.h>*Identifiers for object kinds as specified by CUpti_ActivityObjectKind.

See also

Public Members

-
uint32_t processId
[#](https://docs.nvidia.com#_CPPv4N26CUpti_ActivityObjectKindId9processIdE)

-
uint32_t threadId
[#](https://docs.nvidia.com#_CPPv4N26CUpti_ActivityObjectKindId8threadIdE)

-
struct
[CUpti_ActivityObjectKindId](https://docs.nvidia.com#_CPPv426CUpti_ActivityObjectKindId)::[anonymous] pt[#](https://docs.nvidia.com#_CPPv4N26CUpti_ActivityObjectKindId2ptE) A process object requires that we identify the process ID.

A thread object requires that we identify both the process and thread ID.


-
uint32_t deviceId
[#](https://docs.nvidia.com#_CPPv4N26CUpti_ActivityObjectKindId8deviceIdE)

-
uint32_t contextId
[#](https://docs.nvidia.com#_CPPv4N26CUpti_ActivityObjectKindId9contextIdE)

-
uint32_t streamId
[#](https://docs.nvidia.com#_CPPv4N26CUpti_ActivityObjectKindId8streamIdE)

-
struct
[CUpti_ActivityObjectKindId](https://docs.nvidia.com#_CPPv426CUpti_ActivityObjectKindId)::[anonymous] dcs[#](https://docs.nvidia.com#_CPPv4N26CUpti_ActivityObjectKindId3dcsE) A device object requires that we identify the device ID.

A context object requires that we identify both the device and context ID. A stream object requires that we identify device, context, and stream ID.


-
uint32_t processId