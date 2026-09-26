source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityBranch.html

# 7.6. CUpti_ActivityBranch[#](https://docs.nvidia.com#cupti-activitybranch)

-
struct CUpti_ActivityBranch
[#](https://docs.nvidia.com#_CPPv420CUpti_ActivityBranch) The activity record for source level result branch.

(deprecated)

This activity record the locations of the branches in the source (CUPTI_ACTIVITY_KIND_BRANCH). Branch activities are now reported using the

[CUpti_ActivityBranch2](https://docs.nvidia.com/structCUpti__ActivityBranch2.html#structcupti__activitybranch2)activity record.Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityBranch4kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_BRANCH.


-
uint32_t sourceLocatorId
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityBranch15sourceLocatorIdE) The ID for source locator.


-
uint32_t correlationId
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityBranch13correlationIdE) The correlation ID of the kernel to which this result is associated.


-
uint32_t pcOffset
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityBranch8pcOffsetE) The pc offset for the branch.


-
uint32_t executed
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityBranch8executedE) The number of times this instruction was executed per warp.

It will be incremented regardless of predicate or condition code.


-
uint32_t diverged
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityBranch8divergedE) Number of times this branch diverged.


-
uint64_t threadsExecuted
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityBranch15threadsExecutedE) This increments each time when this instruction is executed by number of threads that executed this instruction.


-