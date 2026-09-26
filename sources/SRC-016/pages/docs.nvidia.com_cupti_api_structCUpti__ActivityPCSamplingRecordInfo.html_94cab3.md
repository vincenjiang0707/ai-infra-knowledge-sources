source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityPCSamplingRecordInfo.html

# 7.119. CUpti_ActivityPCSamplingRecordInfo[#](https://docs.nvidia.com#cupti-activitypcsamplingrecordinfo)

-
struct CUpti_ActivityPCSamplingRecordInfo
[#](https://docs.nvidia.com#_CPPv434CUpti_ActivityPCSamplingRecordInfo) The activity record for record status for PC sampling.

This activity records information obtained by sampling PC (CUPTI_ACTIVITY_KIND_PC_SAMPLING_RECORD_INFO).

Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N34CUpti_ActivityPCSamplingRecordInfo4kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_PC_SAMPLING_RECORD_INFO.


-
uint32_t correlationId
[#](https://docs.nvidia.com#_CPPv4N34CUpti_ActivityPCSamplingRecordInfo13correlationIdE) The correlation ID of the kernel to which this result is associated.


-
uint64_t totalSamples
[#](https://docs.nvidia.com#_CPPv4N34CUpti_ActivityPCSamplingRecordInfo12totalSamplesE) Number of times the PC was sampled for this kernel instance including all dropped samples.


-
uint64_t droppedSamples
[#](https://docs.nvidia.com#_CPPv4N34CUpti_ActivityPCSamplingRecordInfo14droppedSamplesE) Number of samples that were dropped by hardware due to backpressure/overflow.


-
uint64_t samplingPeriodInCycles
[#](https://docs.nvidia.com#_CPPv4N34CUpti_ActivityPCSamplingRecordInfo22samplingPeriodInCyclesE) Sampling period in terms of number of cycles .


-