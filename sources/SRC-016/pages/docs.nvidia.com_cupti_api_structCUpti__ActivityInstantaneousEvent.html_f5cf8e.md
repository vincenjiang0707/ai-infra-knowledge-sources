source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityInstantaneousEvent.html

# 7.47. CUpti_ActivityInstantaneousEvent[#](https://docs.nvidia.com#cupti-activityinstantaneousevent)

-
struct CUpti_ActivityInstantaneousEvent
[#](https://docs.nvidia.com#_CPPv432CUpti_ActivityInstantaneousEvent) The activity record for an instantaneous CUPTI event.

This activity record represents a CUPTI event value (CUPTI_ACTIVITY_KIND_EVENT) sampled at a particular instant. This activity record kind is not produced by the activity API but is included for completeness and ease-of-use. Profiler frameworks built on top of CUPTI that collect event data at a particular time may choose to use this type to store the collected event data.

Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N32CUpti_ActivityInstantaneousEvent4kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_INSTANTANEOUS_EVENT.


-
CUpti_EventID id
[#](https://docs.nvidia.com#_CPPv4N32CUpti_ActivityInstantaneousEvent2idE) The event ID.


-
uint64_t value
[#](https://docs.nvidia.com#_CPPv4N32CUpti_ActivityInstantaneousEvent5valueE) The event value.


-
uint64_t timestamp
[#](https://docs.nvidia.com#_CPPv4N32CUpti_ActivityInstantaneousEvent9timestampE) The timestamp at which event is sampled.


-
uint32_t deviceId
[#](https://docs.nvidia.com#_CPPv4N32CUpti_ActivityInstantaneousEvent8deviceIdE) The device id.


-
uint32_t reserved
[#](https://docs.nvidia.com#_CPPv4N32CUpti_ActivityInstantaneousEvent8reservedE) Undefined.

reserved for internal use


-