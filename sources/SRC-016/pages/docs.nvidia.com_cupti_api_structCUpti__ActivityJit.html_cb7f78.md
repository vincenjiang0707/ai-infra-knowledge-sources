source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityJit.html

# 7.53. CUpti_ActivityJit[#](https://docs.nvidia.com#cupti-activityjit)

-
struct CUpti_ActivityJit
[#](https://docs.nvidia.com#_CPPv417CUpti_ActivityJit) The activity record for JIT operations.

This activity represents the JIT operations (compile, load, store) of a CUmodule from the Compute Cache. Gives the exact hashed path of where the cached module is loaded from, or where the module will be stored after Just-In-Time (JIT) compilation.

JIT activity is now reported using

[CUpti_ActivityJit2](https://docs.nvidia.com/structCUpti__ActivityJit2.html#structcupti__activityjit2)recordPublic Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N17CUpti_ActivityJit4kindE) The activity record kind must be CUPTI_ACTIVITY_KIND_JIT.


-
[CUpti_ActivityJitEntryType](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv426CUpti_ActivityJitEntryType)jitEntryType[#](https://docs.nvidia.com#_CPPv4N17CUpti_ActivityJit12jitEntryTypeE) The JIT entry type.


-
[CUpti_ActivityJitOperationType](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv430CUpti_ActivityJitOperationType)jitOperationType[#](https://docs.nvidia.com#_CPPv4N17CUpti_ActivityJit16jitOperationTypeE) The JIT operation type.


-
uint32_t deviceId
[#](https://docs.nvidia.com#_CPPv4N17CUpti_ActivityJit8deviceIdE) The device ID.


-
uint64_t start
[#](https://docs.nvidia.com#_CPPv4N17CUpti_ActivityJit5startE) The start timestamp for the JIT operation, in ns.

A value of 0 for both the start and end timestamps indicates that timestamp information could not be collected for the JIT operation.


-
uint64_t end
[#](https://docs.nvidia.com#_CPPv4N17CUpti_ActivityJit3endE) The end timestamp for the JIT operation, in ns.

A value of 0 for both the start and end timestamps indicates that timestamp information could not be collected for the JIT operation.


-
uint32_t correlationId
[#](https://docs.nvidia.com#_CPPv4N17CUpti_ActivityJit13correlationIdE) The correlation ID of the JIT operation to which records belong to.

Each JIT operation is assigned a unique correlation ID that is identical to the correlation ID in the driver or runtime API activity record that launched the JIT operation.


-
uint32_t padding
[#](https://docs.nvidia.com#_CPPv4N17CUpti_ActivityJit7paddingE) Internal use.


-
uint64_t jitOperationCorrelationId
[#](https://docs.nvidia.com#_CPPv4N17CUpti_ActivityJit25jitOperationCorrelationIdE) The correlation ID to correlate JIT compilation, load and store operations.

Each JIT compilation unit is assigned a unique correlation ID at the time of the JIT compilation. This correlation id can be used to find the matching JIT cache load/store records.


-
uint64_t cacheSize
[#](https://docs.nvidia.com#_CPPv4N17CUpti_ActivityJit9cacheSizeE) The size of compute cache.


-
const char *cachePath
[#](https://docs.nvidia.com#_CPPv4N17CUpti_ActivityJit9cachePathE) The path where the fat binary is cached.


-