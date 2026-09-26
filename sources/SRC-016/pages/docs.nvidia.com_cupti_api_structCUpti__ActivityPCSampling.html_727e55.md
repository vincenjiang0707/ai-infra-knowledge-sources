source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityPCSampling.html

# 7.115. CUpti_ActivityPCSampling[#](https://docs.nvidia.com#cupti-activitypcsampling)

-
struct CUpti_ActivityPCSampling
[#](https://docs.nvidia.com#_CPPv424CUpti_ActivityPCSampling) The activity record for PC sampling.

(deprecated in CUDA 8.0)

This activity records information obtained by sampling PC (CUPTI_ACTIVITY_KIND_PC_SAMPLING). PC sampling activities are now reported using the

[CUpti_ActivityPCSampling2](https://docs.nvidia.com/structCUpti__ActivityPCSampling2.html#structcupti__activitypcsampling2)activity record.Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityPCSampling4kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_PC_SAMPLING.


-
[CUpti_ActivityFlag](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityFlag)flags[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityPCSampling5flagsE) The properties of this instruction.


-
uint32_t sourceLocatorId
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityPCSampling15sourceLocatorIdE) The ID for source locator.


-
uint32_t correlationId
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityPCSampling13correlationIdE) The correlation ID of the kernel to which this result is associated.


-
uint32_t functionId
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityPCSampling10functionIdE) Correlation ID with global/device function name.


-
uint32_t pcOffset
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityPCSampling8pcOffsetE) The pc offset for the instruction.


-
uint32_t samples
[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityPCSampling7samplesE) Number of times the PC was sampled with the stallReason in the record.

The same PC can be sampled with different stall reasons.


-
[CUpti_ActivityPCSamplingStallReason](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv435CUpti_ActivityPCSamplingStallReason)stallReason[#](https://docs.nvidia.com#_CPPv4N24CUpti_ActivityPCSampling11stallReasonE) Current stall reason.

Includes one of the reasons from

[CUpti_ActivityPCSamplingStallReason](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#group__cupti__activity__api_1ga57bafb9baafeae0880dae6eaa1a8e12d)

-