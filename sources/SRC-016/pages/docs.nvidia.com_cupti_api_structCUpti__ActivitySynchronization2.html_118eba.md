source: https://docs.nvidia.com/cupti/api/structCUpti__ActivitySynchronization2.html

# 7.129. CUpti_ActivitySynchronization2[#](https://docs.nvidia.com#cupti-activitysynchronization2)

-
struct CUpti_ActivitySynchronization2
[#](https://docs.nvidia.com#_CPPv430CUpti_ActivitySynchronization2) The activity record for synchronization management.

This activity is used to track various CUDA synchronization APIs. (CUPTI_ACTIVITY_KIND_SYNCHRONIZATION).

Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivitySynchronization24kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_SYNCHRONIZATION.


-
[CUpti_ActivitySynchronizationType](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv433CUpti_ActivitySynchronizationType)type[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivitySynchronization24typeE) The type of record.


-
uint64_t start
[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivitySynchronization25startE) The start timestamp for the function, in ns.

A value of 0 for both the start and end timestamps indicates that timestamp information could not be collected for the function.


-
uint64_t end
[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivitySynchronization23endE) The end timestamp for the function, in ns.

A value of 0 for both the start and end timestamps indicates that timestamp information could not be collected for the function.


-
uint32_t correlationId
[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivitySynchronization213correlationIdE) The correlation ID of the API to which this result is associated.


-
uint32_t contextId
[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivitySynchronization29contextIdE) The ID of the context for which the synchronization API is called.

In case of context synchronization API it is the context id for which the API is called. In case of stream/event synchronization it is the ID of the context where the stream/event was created.


-
uint32_t streamId
[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivitySynchronization28streamIdE) The compute stream for which the synchronization API is called.

A CUPTI_SYNCHRONIZATION_INVALID_VALUE value indicate the field is not applicable for this record. Not valid for cuCtxSynchronize, cuEventSynchronize.


-
uint32_t cudaEventId
[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivitySynchronization211cudaEventIdE) The event ID for which the synchronization API is called.

A CUPTI_SYNCHRONIZATION_INVALID_VALUE value indicate the field is not applicable for this record. Not valid for cuCtxSynchronize, cuStreamSynchronize.


-
uint64_t cudaEventSyncId
[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivitySynchronization215cudaEventSyncIdE) A unique ID to associate event synchronization records with the latest CUDA Event record.

Similar field is added in

[CUpti_ActivityCudaEvent2](https://docs.nvidia.com/structCUpti__ActivityCudaEvent2.html#structcupti__activitycudaevent2)to associate synchronization record to the CUDA Event record.The same CUDA event can be used multiple times, so the event id will not be unique to correlate the synchronization record with the latest CUDA Event record. This field will be unique and can be used to do the required correlation.

A CUPTI_SYNCHRONIZATION_INVALID_VALUE value indicates that the field is not applicable for this record. Valid only for synchronization records related to CUDA Events.


-
uint32_t returnValue
[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivitySynchronization211returnValueE) The return value for the synchronization record.

Use cuptiActivityEnableAllSyncRecords API to enable/disable collection of synchronization records with return value being non-zero. This will be a CUresult value.


-
uint32_t pad
[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivitySynchronization23padE) Undefined.

Reserved for internal use.


-