source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityDeviceGraphTrace.html

# 7.25. CUpti_ActivityDeviceGraphTrace[#](https://docs.nvidia.com#cupti-activitydevicegraphtrace)

-
struct CUpti_ActivityDeviceGraphTrace
[#](https://docs.nvidia.com#_CPPv430CUpti_ActivityDeviceGraphTrace) The activity record for trace of device graph execution.

This activity record represents execution for a device launched graph without giving visibility about the execution of its nodes. This is intended to reduce overheads in tracing each node. The activity kind is CUPTI_ACTIVITY_KIND_DEVICE_GRAPH_TRACE

Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivityDeviceGraphTrace4kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_DEVICE_GRAPH_TRACE.


-
uint32_t deviceId
[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivityDeviceGraphTrace8deviceIdE) The ID of the device where the first node of the graph is executed.


-
uint64_t start
[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivityDeviceGraphTrace5startE) The start timestamp for the graph execution, in ns.

A value of 0 for both the start and end timestamps indicates that timestamp information could not be collected for the graph.


-
uint64_t end
[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivityDeviceGraphTrace3endE) The end timestamp for the graph execution, in ns.

A value of 0 for both the start and end timestamps indicates that timestamp information could not be collected for the graph.


-
uint32_t graphId
[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivityDeviceGraphTrace7graphIdE) The unique ID of the graph that is launched.


-
uint32_t launcherGraphId
[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivityDeviceGraphTrace15launcherGraphIdE) The unique ID of the graph that has launched this graph.

This value is not valid if Hardware Event System (HES) is turned ON.


-
uint32_t deviceLaunchMode
[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivityDeviceGraphTrace16deviceLaunchModeE) The type of launch.

See

[CUpti_DeviceGraphLaunchMode](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#group__cupti__activity__api_1ga55d6dad35d3ac4c54d84614b92310179)This value is not valid if Hardware Event System (HES) is turned ON.

-
uint32_t contextId
[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivityDeviceGraphTrace9contextIdE) The ID of the context where the first node of the graph is executed.


-
uint64_t streamId
[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivityDeviceGraphTrace8streamIdE) The ID of the stream where the graph is being launched.

This value is not valid if Hardware Event System (HES) is turned ON.


-
void *reserved
[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivityDeviceGraphTrace8reservedE) This field is reserved for internal use.


-