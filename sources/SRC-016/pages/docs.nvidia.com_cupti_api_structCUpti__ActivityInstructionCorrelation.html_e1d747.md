source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityInstructionCorrelation.html

# 7.51. CUpti_ActivityInstructionCorrelation[#](https://docs.nvidia.com#cupti-activityinstructioncorrelation)

-
struct CUpti_ActivityInstructionCorrelation
[#](https://docs.nvidia.com#_CPPv436CUpti_ActivityInstructionCorrelation) The activity record for source-level sass/source line-by-line correlation.

This activity records source level sass/source correlation information. (CUPTI_ACTIVITY_KIND_INSTRUCTION_CORRELATION).

Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N36CUpti_ActivityInstructionCorrelation4kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_INSTRUCTION_CORRELATION.


-
[CUpti_ActivityFlag](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityFlag)flags[#](https://docs.nvidia.com#_CPPv4N36CUpti_ActivityInstructionCorrelation5flagsE) The properties of this instruction.


-
uint32_t sourceLocatorId
[#](https://docs.nvidia.com#_CPPv4N36CUpti_ActivityInstructionCorrelation15sourceLocatorIdE) The ID for source locator.


-
uint32_t functionId
[#](https://docs.nvidia.com#_CPPv4N36CUpti_ActivityInstructionCorrelation10functionIdE) Correlation ID with global/device function name.


-
uint32_t pcOffset
[#](https://docs.nvidia.com#_CPPv4N36CUpti_ActivityInstructionCorrelation8pcOffsetE) The pc offset for the instruction.


-
uint32_t pad
[#](https://docs.nvidia.com#_CPPv4N36CUpti_ActivityInstructionCorrelation3padE) Undefined.

Reserved for internal use.


-