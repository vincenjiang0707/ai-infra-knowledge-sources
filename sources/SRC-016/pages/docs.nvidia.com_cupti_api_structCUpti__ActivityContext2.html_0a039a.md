source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityContext2.html

# 7.13. CUpti_ActivityContext2[#](https://docs.nvidia.com#cupti-activitycontext2)

-
struct CUpti_ActivityContext2
[#](https://docs.nvidia.com#_CPPv422CUpti_ActivityContext2) The activity record for a context.

This activity record represents information about a context (CUPTI_ACTIVITY_KIND_CONTEXT). Context activity is now reported using

[CUpti_ActivityContext3](https://docs.nvidia.com/structCUpti__ActivityContext3.html#structcupti__activitycontext3)recordPublic Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityContext24kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_CONTEXT.


-
uint32_t contextId
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityContext29contextIdE) The context ID.


-
uint32_t deviceId
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityContext28deviceIdE) The device ID.


-
uint16_t computeApiKind
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityContext214computeApiKindE) The compute API kind.

See also


-
uint16_t nullStreamId
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityContext212nullStreamIdE) The ID for the NULL stream in this context.


-
uint32_t parentContextId
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityContext215parentContextIdE) The ID of the parent context.

It would be 0 if context does not have parent


-
uint8_t isGreenContext
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityContext214isGreenContextE) This field indicates whether the context is a green context.


-
uint16_t numMultiprocessors
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityContext218numMultiprocessorsE) Number of multiprocessors assigned to the green context Invalid if the field ‘isGreenContext’ is 0.


-