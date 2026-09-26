source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityInstructionExecution.html

# 7.52. CUpti_ActivityInstructionExecution[#](https://docs.nvidia.com#cupti-activityinstructionexecution)

-
struct CUpti_ActivityInstructionExecution
[#](https://docs.nvidia.com#_CPPv434CUpti_ActivityInstructionExecution) The activity record for source-level instruction execution.

This activity records result for source level instruction execution. (CUPTI_ACTIVITY_KIND_INSTRUCTION_EXECUTION).

Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N34CUpti_ActivityInstructionExecution4kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_INSTRUCTION_EXECUTION.


-
[CUpti_ActivityFlag](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityFlag)flags[#](https://docs.nvidia.com#_CPPv4N34CUpti_ActivityInstructionExecution5flagsE) The properties of this instruction execution.


-
uint32_t sourceLocatorId
[#](https://docs.nvidia.com#_CPPv4N34CUpti_ActivityInstructionExecution15sourceLocatorIdE) The ID for source locator.


-
uint32_t correlationId
[#](https://docs.nvidia.com#_CPPv4N34CUpti_ActivityInstructionExecution13correlationIdE) The correlation ID of the kernel to which this result is associated.


-
uint32_t functionId
[#](https://docs.nvidia.com#_CPPv4N34CUpti_ActivityInstructionExecution10functionIdE) Correlation ID with global/device function name.


-
uint32_t pcOffset
[#](https://docs.nvidia.com#_CPPv4N34CUpti_ActivityInstructionExecution8pcOffsetE) The pc offset for the instruction.


-
uint64_t threadsExecuted
[#](https://docs.nvidia.com#_CPPv4N34CUpti_ActivityInstructionExecution15threadsExecutedE) This increments each time when this instruction is executed by number of threads that executed this instruction, regardless of predicate or condition code.


-
uint64_t notPredOffThreadsExecuted
[#](https://docs.nvidia.com#_CPPv4N34CUpti_ActivityInstructionExecution25notPredOffThreadsExecutedE) This increments each time when this instruction is executed by number of threads that executed this instruction with predicate and condition code evaluating to true.


-
uint32_t executed
[#](https://docs.nvidia.com#_CPPv4N34CUpti_ActivityInstructionExecution8executedE) The number of times this instruction was executed per warp.

It will be incremented regardless of predicate or condition code.


-
uint32_t pad
[#](https://docs.nvidia.com#_CPPv4N34CUpti_ActivityInstructionExecution3padE) Undefined.

Reserved for internal use.


-