source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityUnifiedMemoryCounter.html

# 7.130. CUpti_ActivityUnifiedMemoryCounter[#](https://docs.nvidia.com#cupti-activityunifiedmemorycounter)

-
struct CUpti_ActivityUnifiedMemoryCounter
[#](https://docs.nvidia.com#_CPPv434CUpti_ActivityUnifiedMemoryCounter) The activity record for Unified Memory counters (deprecated in CUDA 7.0)

This activity record represents a Unified Memory counter (CUPTI_ACTIVITY_KIND_UNIFIED_MEMORY_COUNTER).

Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N34CUpti_ActivityUnifiedMemoryCounter4kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_UNIFIED_MEMORY_COUNTER.


-
[CUpti_ActivityUnifiedMemoryCounterKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv438CUpti_ActivityUnifiedMemoryCounterKind)counterKind[#](https://docs.nvidia.com#_CPPv4N34CUpti_ActivityUnifiedMemoryCounter11counterKindE) The Unified Memory counter kind.


-
[CUpti_ActivityUnifiedMemoryCounterScope](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv439CUpti_ActivityUnifiedMemoryCounterScope)scope[#](https://docs.nvidia.com#_CPPv4N34CUpti_ActivityUnifiedMemoryCounter5scopeE) Scope of the Unified Memory counter.


-
uint32_t deviceId
[#](https://docs.nvidia.com#_CPPv4N34CUpti_ActivityUnifiedMemoryCounter8deviceIdE) The ID of the device involved in the memory transfer operation.

It is not relevant if the scope of the counter is global (all devices).


-
uint64_t value
[#](https://docs.nvidia.com#_CPPv4N34CUpti_ActivityUnifiedMemoryCounter5valueE) Value of the counter.


-
uint64_t timestamp
[#](https://docs.nvidia.com#_CPPv4N34CUpti_ActivityUnifiedMemoryCounter9timestampE) The timestamp when this sample was retrieved, in ns.

A value of 0 indicates that timestamp information could not be collected


-
uint32_t processId
[#](https://docs.nvidia.com#_CPPv4N34CUpti_ActivityUnifiedMemoryCounter9processIdE) The ID of the process to which this record belongs to.

In case of global scope, processId is undefined.


-
uint32_t pad
[#](https://docs.nvidia.com#_CPPv4N34CUpti_ActivityUnifiedMemoryCounter3padE) Undefined.

Reserved for internal use.


-