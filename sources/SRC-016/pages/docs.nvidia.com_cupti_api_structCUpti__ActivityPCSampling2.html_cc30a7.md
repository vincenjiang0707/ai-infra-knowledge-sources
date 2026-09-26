source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityPCSampling2.html

# 7.116. CUpti_ActivityPCSampling2[#](https://docs.nvidia.com#cupti-activitypcsampling2)

-
struct CUpti_ActivityPCSampling2
[#](https://docs.nvidia.com#_CPPv425CUpti_ActivityPCSampling2) The activity record for PC sampling.

(deprecated in CUDA 9.0)

This activity records information obtained by sampling PC (CUPTI_ACTIVITY_KIND_PC_SAMPLING). PC sampling activities are now reported using the

[CUpti_ActivityPCSampling3](https://docs.nvidia.com/structCUpti__ActivityPCSampling3.html#structcupti__activitypcsampling3)activity record.Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityPCSampling24kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_PC_SAMPLING.


-
[CUpti_ActivityFlag](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityFlag)flags[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityPCSampling25flagsE) The properties of this instruction.


-
uint32_t sourceLocatorId
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityPCSampling215sourceLocatorIdE) The ID for source locator.


-
uint32_t correlationId
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityPCSampling213correlationIdE) The correlation ID of the kernel to which this result is associated.


-
uint32_t functionId
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityPCSampling210functionIdE) Correlation ID with global/device function name.


-
uint32_t pcOffset
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityPCSampling28pcOffsetE) The pc offset for the instruction.


-
uint32_t latencySamples
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityPCSampling214latencySamplesE) Number of times the PC was sampled with the stallReason in the record.

These samples indicate that no instruction was issued in that cycle from the warp scheduler from where the warp was sampled. Field is valid for devices with compute capability 6.0 and higher


-
uint32_t samples
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityPCSampling27samplesE) Number of times the PC was sampled with the stallReason in the record.

The same PC can be sampled with different stall reasons. The count includes latencySamples.


-
[CUpti_ActivityPCSamplingStallReason](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv435CUpti_ActivityPCSamplingStallReason)stallReason[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityPCSampling211stallReasonE) Current stall reason.

Includes one of the reasons from

[CUpti_ActivityPCSamplingStallReason](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#group__cupti__activity__api_1ga57bafb9baafeae0880dae6eaa1a8e12d)

-