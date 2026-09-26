source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityInstantaneousEventInstance.html

# 7.48. CUpti_ActivityInstantaneousEventInstance[#](https://docs.nvidia.com#cupti-activityinstantaneouseventinstance)

-
struct CUpti_ActivityInstantaneousEventInstance
[#](https://docs.nvidia.com#_CPPv440CUpti_ActivityInstantaneousEventInstance) The activity record for an instantaneous CUPTI event with event domain instance information.

This activity record represents the a CUPTI event value for a specific event domain instance (CUPTI_ACTIVITY_KIND_EVENT_INSTANCE) sampled at a particular instant. This activity record kind is not produced by the activity API but is included for completeness and ease-of-use. Profiler frameworks built on top of CUPTI that collect event data may choose to use this type to store the collected event data. This activity record should be used when event domain instance information needs to be associated with the event.

Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N40CUpti_ActivityInstantaneousEventInstance4kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_INSTANTANEOUS_EVENT_INSTANCE.


-
CUpti_EventID id
[#](https://docs.nvidia.com#_CPPv4N40CUpti_ActivityInstantaneousEventInstance2idE) The event ID.


-
uint64_t value
[#](https://docs.nvidia.com#_CPPv4N40CUpti_ActivityInstantaneousEventInstance5valueE) The event value.


-
uint64_t timestamp
[#](https://docs.nvidia.com#_CPPv4N40CUpti_ActivityInstantaneousEventInstance9timestampE) The timestamp at which event is sampled.


-
uint32_t deviceId
[#](https://docs.nvidia.com#_CPPv4N40CUpti_ActivityInstantaneousEventInstance8deviceIdE) The device id.


-
uint8_t instance
[#](https://docs.nvidia.com#_CPPv4N40CUpti_ActivityInstantaneousEventInstance8instanceE) The event domain instance.


-
uint8_t pad[3]
[#](https://docs.nvidia.com#_CPPv4N40CUpti_ActivityInstantaneousEventInstance3padE) Undefined.

reserved for internal use


-