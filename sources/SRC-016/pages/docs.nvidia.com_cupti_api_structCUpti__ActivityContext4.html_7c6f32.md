source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityContext4.html

# 7.15. CUpti_ActivityContext4[#](https://docs.nvidia.com#cupti-activitycontext4)

-
struct CUpti_ActivityContext4
[#](https://docs.nvidia.com#_CPPv422CUpti_ActivityContext4) The activity record for a context.

This activity record represents information about a context (CUPTI_ACTIVITY_KIND_CONTEXT).

Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityContext44kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_CONTEXT.


-
uint32_t contextId
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityContext49contextIdE) The context ID.


-
uint32_t deviceId
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityContext48deviceIdE) The device ID.


-
uint16_t computeApiKind
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityContext414computeApiKindE) The compute API kind.

See also


-
uint16_t nullStreamId
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityContext412nullStreamIdE) The ID for the NULL stream in this context.


-
uint32_t parentContextId
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityContext415parentContextIdE) The ID of the parent context.

It would be 0 if context does not have parent


-
uint8_t isGreenContext
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityContext414isGreenContextE) This field indicates whether the context is a green context.


-
uint8_t padding
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityContext47paddingE) Undefined.

Reserved for internal use.


-
uint16_t numMultiprocessors
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityContext418numMultiprocessorsE) Number of multiprocessors assigned to the green context Invalid if the field ‘isGreenContext’ is 0.


-
[CUpti_ContextCigMode](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv420CUpti_ContextCigMode)cigMode[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityContext47cigModeE) This field indicates the CIG mode.


-
uint32_t padding2
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityContext48padding2E) Undefined.

Reserved for internal use.


-
uint64_t processId
[#](https://docs.nvidia.com#_CPPv4N22CUpti_ActivityContext49processIdE) The ID of the process associated with the context.


-