source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityEventInstance.html

# 7.32. CUpti_ActivityEventInstance[#](https://docs.nvidia.com#cupti-activityeventinstance)

-
struct CUpti_ActivityEventInstance
[#](https://docs.nvidia.com#_CPPv427CUpti_ActivityEventInstance) The activity record for a CUPTI event with instance information.

This activity record represents the a CUPTI event value for a specific event domain instance (CUPTI_ACTIVITY_KIND_EVENT_INSTANCE). This activity record kind is not produced by the activity API but is included for completeness and ease-of-use. Profile frameworks built on top of CUPTI that collect event data may choose to use this type to store the collected event data. This activity record should be used when event domain instance information needs to be associated with the event.

Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N27CUpti_ActivityEventInstance4kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_EVENT_INSTANCE.


-
CUpti_EventID id
[#](https://docs.nvidia.com#_CPPv4N27CUpti_ActivityEventInstance2idE) The event ID.


-
CUpti_EventDomainID domain
[#](https://docs.nvidia.com#_CPPv4N27CUpti_ActivityEventInstance6domainE) The event domain ID.


-
uint32_t instance
[#](https://docs.nvidia.com#_CPPv4N27CUpti_ActivityEventInstance8instanceE) The event domain instance.


-
uint64_t value
[#](https://docs.nvidia.com#_CPPv4N27CUpti_ActivityEventInstance5valueE) The event value.


-
uint32_t correlationId
[#](https://docs.nvidia.com#_CPPv4N27CUpti_ActivityEventInstance13correlationIdE) The correlation ID of the event.

Use of this ID is user-defined, but typically this ID value will equal the correlation ID of the kernel for which the event was gathered.


-
uint32_t pad
[#](https://docs.nvidia.com#_CPPv4N27CUpti_ActivityEventInstance3padE) Undefined.

Reserved for internal use.


-