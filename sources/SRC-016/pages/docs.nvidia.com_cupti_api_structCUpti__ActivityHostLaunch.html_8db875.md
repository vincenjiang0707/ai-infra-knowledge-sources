source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityHostLaunch.html

# 7.46. CUpti_ActivityHostLaunch[#](https://docs.nvidia.com#cupti-activityhostlaunch)

-
struct CUpti_ActivityHostLaunch
[#](https://docs.nvidia.com#_CPPv424CUpti_ActivityHostLaunch) The activity record for host launch functions.

The corresponding activity kind is CUPTI_ACTIVITY_KIND_HOST_LAUNCH.

Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityHostLaunch4kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_HOST_LAUNCH.


-
uint32_t streamId
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityHostLaunch8streamIdE) The ID of the CUDA context to which the waiting CUDA stream belongs.


-
uint32_t contextId
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityHostLaunch9contextIdE) The ID of the CUDA context to which the waiting CUDA stream belongs.


-
uint32_t deviceId
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityHostLaunch8deviceIdE) The ID of the CUDA device to which the CUDA context and stream belong.

The host function is executing on the CPU, but it is associated with the CUDA device through the CUDA context and stream.


-
uint32_t correlationId
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityHostLaunch13correlationIdE) The correlation ID of the host launch operation.

Each operation is assigned a unique correlation ID that is identical to the correlation ID in the driver API activity record that launched the operation.


-
uint32_t processId
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityHostLaunch9processIdE) The ID of the process where the host function is executing.


-
uint32_t threadId
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityHostLaunch8threadIdE) The ID of the thread where the host function is executing.


-
uint64_t start
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityHostLaunch5startE) The start timestamp.

A value of CUPTI_TIMESTAMP_UNKNOWN indicates that the start time is unknown.


-
uint64_t end
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityHostLaunch3endE) The end timestamp.

A value of CUPTI_TIMESTAMP_UNKNOWN indicates that the start time is unknown.


-