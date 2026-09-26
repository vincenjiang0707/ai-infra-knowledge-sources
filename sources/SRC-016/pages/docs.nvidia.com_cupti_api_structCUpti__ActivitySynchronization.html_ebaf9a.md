source: https://docs.nvidia.com/cupti/api/structCUpti__ActivitySynchronization.html

# 7.128. CUpti_ActivitySynchronization[#](https://docs.nvidia.com#cupti-activitysynchronization)

-
struct CUpti_ActivitySynchronization
[#](https://docs.nvidia.com#_CPPv429CUpti_ActivitySynchronization) The activity record for synchronization management.

This activity is used to track various CUDA synchronization APIs. (CUPTI_ACTIVITY_KIND_SYNCHRONIZATION).

Structure deprecated in CUDA 12.8: Refer to

[CUpti_ActivitySynchronization2](https://docs.nvidia.com/structCUpti__ActivitySynchronization2.html#structcupti__activitysynchronization2)for the latest structure.Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N29CUpti_ActivitySynchronization4kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_SYNCHRONIZATION.


-
[CUpti_ActivitySynchronizationType](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv433CUpti_ActivitySynchronizationType)type[#](https://docs.nvidia.com#_CPPv4N29CUpti_ActivitySynchronization4typeE) The type of record.


-
uint64_t start
[#](https://docs.nvidia.com#_CPPv4N29CUpti_ActivitySynchronization5startE) The start timestamp for the function, in ns.

A value of 0 for both the start and end timestamps indicates that timestamp information could not be collected for the function.


-
uint64_t end
[#](https://docs.nvidia.com#_CPPv4N29CUpti_ActivitySynchronization3endE) The end timestamp for the function, in ns.

A value of 0 for both the start and end timestamps indicates that timestamp information could not be collected for the function.


-
uint32_t correlationId
[#](https://docs.nvidia.com#_CPPv4N29CUpti_ActivitySynchronization13correlationIdE) The correlation ID of the API to which this result is associated.


-
uint32_t contextId
[#](https://docs.nvidia.com#_CPPv4N29CUpti_ActivitySynchronization9contextIdE) The ID of the context for which the synchronization API is called.

In case of context synchronization API it is the context id for which the API is called. In case of stream/event synchronization it is the ID of the context where the stream/event was created.


-
uint32_t streamId
[#](https://docs.nvidia.com#_CPPv4N29CUpti_ActivitySynchronization8streamIdE) The compute stream for which the synchronization API is called.

A CUPTI_SYNCHRONIZATION_INVALID_VALUE value indicate the field is not applicable for this record. Not valid for cuCtxSynchronize, cuEventSynchronize.


-
uint32_t cudaEventId
[#](https://docs.nvidia.com#_CPPv4N29CUpti_ActivitySynchronization11cudaEventIdE) The event ID for which the synchronization API is called.

A CUPTI_SYNCHRONIZATION_INVALID_VALUE value indicate the field is not applicable for this record. Not valid for cuCtxSynchronize, cuStreamSynchronize.


-