source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityGraphTrace2.html

# 7.42. CUpti_ActivityGraphTrace2[#](https://docs.nvidia.com#cupti-activitygraphtrace2)

-
struct CUpti_ActivityGraphTrace2
[#](https://docs.nvidia.com#_CPPv425CUpti_ActivityGraphTrace2) The activity record for trace of graph execution.

This activity record represents execution for a graph without giving visibility about the execution of its nodes. This is intended to reduce overheads in tracing each node. The activity kind is CUPTI_ACTIVITY_KIND_GRAPH_TRACE

Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityGraphTrace24kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_GRAPH_TRACE.


-
uint32_t correlationId
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityGraphTrace213correlationIdE) The correlation ID of the graph launch.

Each graph launch is assigned a unique correlation ID that is identical to the correlation ID in the driver API activity record that launched the graph.


-
uint64_t start
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityGraphTrace25startE) The start timestamp for the graph execution, in ns.

A value of 0 for both the start and end timestamps indicates that timestamp information could not be collected for the graph.


-
uint64_t end
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityGraphTrace23endE) The end timestamp for the graph execution, in ns.

A value of 0 for both the start and end timestamps indicates that timestamp information could not be collected for the graph.


-
uint32_t deviceId
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityGraphTrace28deviceIdE) The ID of the device where the first node of the graph is executed.

If this is INT_MAX, then the start is on the host.


-
uint32_t graphId
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityGraphTrace27graphIdE) The unique ID of the graph that is launched.


-
uint32_t contextId
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityGraphTrace29contextIdE) The ID of the context where the first node of the graph is executed.

If this is INT_MAX, then the start is on the host.


-
uint32_t streamId
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityGraphTrace28streamIdE) The ID of the stream where the graph is being launched.


-
void *reserved
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityGraphTrace28reservedE) This field is reserved for internal use.


-
uint32_t endDeviceId
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityGraphTrace211endDeviceIdE) The ID of the device where last node of the graph is executed.


-
uint32_t endContextId
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityGraphTrace212endContextIdE) The ID of the context where the last node of the graph is executed.


-