source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityPreemption.html

# 7.123. CUpti_ActivityPreemption[#](https://docs.nvidia.com#cupti-activitypreemption)

-
struct CUpti_ActivityPreemption
[#](https://docs.nvidia.com#_CPPv424CUpti_ActivityPreemption) The activity record for a preemption of a CDP kernel.

This activity record represents a preemption of a CDP kernel.

Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityPreemption4kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_PREEMPTION.


-
[CUpti_ActivityPreemptionKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv428CUpti_ActivityPreemptionKind)preemptionKind[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityPreemption14preemptionKindE) kind of the preemption


-
uint64_t timestamp
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityPreemption9timestampE) The timestamp of the preemption, in ns.

A value of 0 indicates that timestamp information could not be collected for the preemption.


-
int64_t gridId
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityPreemption6gridIdE) The grid-id of the block that is preempted.


-
uint32_t blockX
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityPreemption6blockXE) The X-dimension of the block that is preempted.


-
uint32_t blockY
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityPreemption6blockYE) The Y-dimension of the block that is preempted.


-
uint32_t blockZ
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityPreemption6blockZE) The Z-dimension of the block that is preempted.


-
uint32_t pad
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityPreemption3padE) Undefined.

Reserved for internal use.


-