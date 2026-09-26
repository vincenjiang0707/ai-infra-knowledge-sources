source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityEvent.html

# 7.31. CUpti_ActivityEvent[#](https://docs.nvidia.com#cupti-activityevent)

-
struct CUpti_ActivityEvent
[#](https://docs.nvidia.com#_CPPv419CUpti_ActivityEvent) The activity record for a CUPTI event.

This activity record represents a CUPTI event value (CUPTI_ACTIVITY_KIND_EVENT). This activity record kind is not produced by the activity API but is included for completeness and ease-of-use. Profile frameworks built on top of CUPTI that collect event data may choose to use this type to store the collected event data.

Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N19CUpti_ActivityEvent4kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_EVENT.


-
CUpti_EventID id
[#](https://docs.nvidia.com#_CPPv4N19CUpti_ActivityEvent2idE) The event ID.


-
uint64_t value
[#](https://docs.nvidia.com#_CPPv4N19CUpti_ActivityEvent5valueE) The event value.


-
CUpti_EventDomainID domain
[#](https://docs.nvidia.com#_CPPv4N19CUpti_ActivityEvent6domainE) The event domain ID.


-
uint32_t correlationId
[#](https://docs.nvidia.com#_CPPv4N19CUpti_ActivityEvent13correlationIdE) The correlation ID of the event.

Use of this ID is user-defined, but typically this ID value will equal the correlation ID of the kernel for which the event was gathered.


-