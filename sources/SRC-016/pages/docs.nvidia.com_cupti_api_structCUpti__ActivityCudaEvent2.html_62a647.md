source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityCudaEvent2.html

# 7.17. CUpti_ActivityCudaEvent2[#](https://docs.nvidia.com#cupti-activitycudaevent2)

-
struct CUpti_ActivityCudaEvent2
[#](https://docs.nvidia.com#_CPPv424CUpti_ActivityCudaEvent2) The activity record for CUDA event.

This activity is used to track recorded events. (CUPTI_ACTIVITY_KIND_CUDA_EVENT).

Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityCudaEvent24kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_CUDA_EVENT.


-
uint32_t correlationId
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityCudaEvent213correlationIdE) The correlation ID of the API to which this result is associated.


-
uint32_t contextId
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityCudaEvent29contextIdE) The ID of the context where the event was recorded.


-
uint32_t streamId
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityCudaEvent28streamIdE) The compute stream where the event was recorded.


-
uint32_t eventId
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityCudaEvent27eventIdE) A unique event ID to identify the event record.


-
uint32_t pad
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityCudaEvent23padE) Undefined.

Reserved for internal use.


-
uint32_t deviceId
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityCudaEvent28deviceIdE) The ID of the device where the event was recorded.


-
uint32_t pad2
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityCudaEvent24pad2E) Undefined.

Reserved for internal use.


-
void *reserved0
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityCudaEvent29reserved0E) Undefined.

Reserved for internal use.


-
uint64_t deviceTimestamp
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityCudaEvent215deviceTimestampE) The device-side timestamp on CUDA event record.

Timestamp is in nanoseconds. Collection of this field is disabled by default. It can be enabled by calling CUPTI API

[cuptiActivityEnableCudaEventDeviceTimestamps](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#group__cupti__activity__api_1ga86a82dd4c053b885030dc12863c4b209)

-
uint64_t cudaEventSyncId
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityCudaEvent215cudaEventSyncIdE) A unique ID to associate event synchronization records with the latest CUDA Event record.


-