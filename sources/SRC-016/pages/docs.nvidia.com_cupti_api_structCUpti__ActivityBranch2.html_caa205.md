source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityBranch2.html

# 7.7. CUpti_ActivityBranch2[#](https://docs.nvidia.com#cupti-activitybranch2)

-
struct CUpti_ActivityBranch2
[#](https://docs.nvidia.com#_CPPv421CUpti_ActivityBranch2) The activity record for source level result branch.

This activity record the locations of the branches in the source (CUPTI_ACTIVITY_KIND_BRANCH).

Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityBranch24kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_BRANCH.


-
uint32_t sourceLocatorId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityBranch215sourceLocatorIdE) The ID for source locator.


-
uint32_t correlationId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityBranch213correlationIdE) The correlation ID of the kernel to which this result is associated.


-
uint32_t functionId
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityBranch210functionIdE) Correlation ID with global/device function name.


-
uint32_t pcOffset
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityBranch28pcOffsetE) The pc offset for the branch.


-
uint32_t diverged
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityBranch28divergedE) Number of times this branch diverged.


-
uint64_t threadsExecuted
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityBranch215threadsExecutedE) This increments each time when this instruction is executed by number of threads that executed this instruction.


-
uint32_t executed
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityBranch28executedE) The number of times this instruction was executed per warp.

It will be incremented regardless of predicate or condition code.


-
uint32_t pad
[#](https://docs.nvidia.com#_CPPv4N21CUpti_ActivityBranch23padE) Undefined.

Reserved for internal use.


-