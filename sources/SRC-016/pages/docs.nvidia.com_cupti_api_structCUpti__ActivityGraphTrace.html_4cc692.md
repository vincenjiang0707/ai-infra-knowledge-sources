source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityGraphTrace.html

# 7.41. CUpti_ActivityGraphTrace[#](https://docs.nvidia.com#cupti-activitygraphtrace)

-
struct CUpti_ActivityGraphTrace
[#](https://docs.nvidia.com#_CPPv424CUpti_ActivityGraphTrace) The activity record for trace of graph execution.

This activity record represents execution for a graph without giving visibility about the execution of its nodes. This is intended to reduce overheads in tracing each node. The activity kind is CUPTI_ACTIVITY_KIND_GRAPH_TRACE Graph trace activity is now reported using

[CUpti_ActivityGraphTrace2](https://docs.nvidia.com/structCUpti__ActivityGraphTrace2.html#structcupti__activitygraphtrace2)record.Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityGraphTrace4kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_GRAPH_TRACE.


-
uint32_t correlationId
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityGraphTrace13correlationIdE) The correlation ID of the graph launch.

Each graph launch is assigned a unique correlation ID that is identical to the correlation ID in the driver API activity record that launched the graph.


-
uint64_t start
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityGraphTrace5startE) The start timestamp for the graph execution, in ns.

A value of 0 for both the start and end timestamps indicates that timestamp information could not be collected for the graph.


-
uint64_t end
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityGraphTrace3endE) The end timestamp for the graph execution, in ns.

A value of 0 for both the start and end timestamps indicates that timestamp information could not be collected for the graph.


-
uint32_t deviceId
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityGraphTrace8deviceIdE) The ID of the device where the graph execution is occurring.


-
uint32_t graphId
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityGraphTrace7graphIdE) The unique ID of the graph that is launched.


-
uint32_t contextId
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityGraphTrace9contextIdE) The ID of the context where the graph is being launched.


-
uint32_t streamId
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityGraphTrace8streamIdE) The ID of the stream where the graph is being launched.


-
void *reserved
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityGraphTrace8reservedE) This field is reserved for internal use.


-