source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityGraphHostNode.html

# 7.40. CUpti_ActivityGraphHostNode[#](https://docs.nvidia.com#cupti-activitygraphhostnode)

-
struct CUpti_ActivityGraphHostNode
[#](https://docs.nvidia.com#_CPPv427CUpti_ActivityGraphHostNode) Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N27CUpti_ActivityGraphHostNode4kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_GRAPH_HOST_NODE.


-
uint32_t streamId
[#](https://docs.nvidia.com#_CPPv4N27CUpti_ActivityGraphHostNode8streamIdE) The ID of the stream that waits for the graph host node to finish.


-
uint32_t contextId
[#](https://docs.nvidia.com#_CPPv4N27CUpti_ActivityGraphHostNode9contextIdE) The ID of the CUDA context to which the waiting CUDA stream belongs.


-
uint32_t deviceId
[#](https://docs.nvidia.com#_CPPv4N27CUpti_ActivityGraphHostNode8deviceIdE) The ID of the CUDA device to which the CUDA context and stream belong.

The graph host node is executing on the CPU, but it is associated with the CUDA device through the CUDA context and stream.


-
uint32_t correlationId
[#](https://docs.nvidia.com#_CPPv4N27CUpti_ActivityGraphHostNode13correlationIdE) The correlation ID of the graph host node operation.

Each operation is assigned a unique correlation ID that is identical to the correlation ID in the driver API activity record that launched the operation.


-
uint32_t graphId
[#](https://docs.nvidia.com#_CPPv4N27CUpti_ActivityGraphHostNode7graphIdE) The unique ID of the graph that executed this host node through graph launch.


-
uint64_t graphNodeId
[#](https://docs.nvidia.com#_CPPv4N27CUpti_ActivityGraphHostNode11graphNodeIdE) The unique ID of the graph node that executed this host node through graph launch.


-
uint32_t processId
[#](https://docs.nvidia.com#_CPPv4N27CUpti_ActivityGraphHostNode9processIdE) The ID of the process where the host node is executing.


-
uint32_t threadId
[#](https://docs.nvidia.com#_CPPv4N27CUpti_ActivityGraphHostNode8threadIdE) The ID of the thread where the host node is executing.


-
uint64_t start
[#](https://docs.nvidia.com#_CPPv4N27CUpti_ActivityGraphHostNode5startE) The start timestamp.

A value of CUPTI_TIMESTAMP_UNKNOWN indicates that the start time is unknown.


-
uint64_t end
[#](https://docs.nvidia.com#_CPPv4N27CUpti_ActivityGraphHostNode3endE) The end timestamp.

A value of CUPTI_TIMESTAMP_UNKNOWN indicates that the start time is unknown.


-