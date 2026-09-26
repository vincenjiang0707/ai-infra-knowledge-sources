source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityContext3.html

# 7.14. CUpti_ActivityContext3[#](https://docs.nvidia.com#cupti-activitycontext3)

-
struct CUpti_ActivityContext3
[#](https://docs.nvidia.com#_CPPv422CUpti_ActivityContext3) The activity record for a context.

This activity record represents information about a context (CUPTI_ACTIVITY_KIND_CONTEXT).

Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityContext34kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_CONTEXT.


-
uint32_t contextId
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityContext39contextIdE) The context ID.


-
uint32_t deviceId
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityContext38deviceIdE) The device ID.


-
uint16_t computeApiKind
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityContext314computeApiKindE) The compute API kind.

See also


-
uint16_t nullStreamId
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityContext312nullStreamIdE) The ID for the NULL stream in this context.


-
uint32_t parentContextId
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityContext315parentContextIdE) The ID of the parent context.

It would be 0 if context does not have parent


-
uint8_t isGreenContext
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityContext314isGreenContextE) This field indicates whether the context is a green context.


-
uint16_t numMultiprocessors
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityContext318numMultiprocessorsE) Number of multiprocessors assigned to the green context Invalid if the field ‘isGreenContext’ is 0.


-
[CUpti_ContextCigMode](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv420CUpti_ContextCigMode)cigMode[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityContext37cigModeE) This field indicates the CIG mode.


-