source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityStream.html

# 7.127. CUpti_ActivityStream[#](https://docs.nvidia.com#cupti-activitystream)

-
struct CUpti_ActivityStream
[#](https://docs.nvidia.com#_CPPv420CUpti_ActivityStream) The activity record for CUDA stream.

This activity is used to track created streams. (CUPTI_ACTIVITY_KIND_STREAM).

Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityStream4kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_STREAM.


-
uint32_t contextId
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityStream9contextIdE) The ID of the context where the stream was created.


-
uint32_t streamId
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityStream8streamIdE) A unique stream ID to identify the stream.


-
uint32_t priority
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityStream8priorityE) The clamped priority for the stream.


-
[CUpti_ActivityStreamFlag](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv424CUpti_ActivityStreamFlag)flag[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityStream4flagE) Flags associated with the stream.


-
uint32_t correlationId
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityStream13correlationIdE) The correlation ID of the API to which this result is associated.


-