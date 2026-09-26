source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityCudaEvent.html

# 7.16. CUpti_ActivityCudaEvent[#](https://docs.nvidia.com#cupti-activitycudaevent)

-
struct CUpti_ActivityCudaEvent
[#](https://docs.nvidia.com#_CPPv423CUpti_ActivityCudaEvent) The activity record for CUDA event.

This activity is used to track recorded events. (CUPTI_ACTIVITY_KIND_CUDA_EVENT).

Structure deprecated in CUDA 12.8: Refer to

[CUpti_ActivityCudaEvent2](https://docs.nvidia.com/structCUpti__ActivityCudaEvent2.html#structcupti__activitycudaevent2)for the latest structure.Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityCudaEvent4kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_CUDA_EVENT.


-
uint32_t correlationId
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityCudaEvent13correlationIdE) The correlation ID of the API to which this result is associated.


-
uint32_t contextId
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityCudaEvent9contextIdE) The ID of the context where the event was recorded.


-
uint32_t streamId
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityCudaEvent8streamIdE) The compute stream where the event was recorded.


-
uint32_t eventId
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityCudaEvent7eventIdE) A unique event ID to identify the event record.


-
uint32_t pad
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ActivityCudaEvent3padE) Undefined.

Reserved for internal use.


-