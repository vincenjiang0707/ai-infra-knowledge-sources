source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityPCSamplingConfig.html

# 7.118. CUpti_ActivityPCSamplingConfig[#](https://docs.nvidia.com#cupti-activitypcsamplingconfig)

-
struct CUpti_ActivityPCSamplingConfig
[#](https://docs.nvidia.com#_CPPv430CUpti_ActivityPCSamplingConfig) PC sampling configuration structure.

This structure defines the pc sampling configuration.

See function

[cuptiActivityConfigurePCSampling](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#group__cupti__activity__api_1ga115305aadc838df99d88283fc64c4317)Public Members

-
uint32_t size
[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivityPCSamplingConfig4sizeE) Size of configuration structure.

CUPTI client should set the size of the structure. It will be used in CUPTI to check what fields are available in the structure. Used to preserve backward compatibility.


-
[CUpti_ActivityPCSamplingPeriod](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv430CUpti_ActivityPCSamplingPeriod)samplingPeriod[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivityPCSamplingConfig14samplingPeriodE) There are 5 level provided for sampling period.

The level internally maps to a period in terms of cycles. Same level can map to different number of cycles on different gpus. No of cycles will be chosen to minimize information loss. The period chosen will be given by samplingPeriodInCycles in

[CUpti_ActivityPCSamplingRecordInfo](https://docs.nvidia.com/structCUpti__ActivityPCSamplingRecordInfo.html#structcupti__activitypcsamplingrecordinfo)for each kernel instance.

-
uint32_t samplingPeriod2
[#](https://docs.nvidia.com#_CPPv4N30CUpti_ActivityPCSamplingConfig15samplingPeriod2E) This will override the period set by samplingPeriod.

Value 0 in samplingPeriod2 will be considered as samplingPeriod2 should not be used and samplingPeriod should be used. Valid values for samplingPeriod2 are between 5 to 31 both inclusive. This will set the sampling period to (2^samplingPeriod2) cycles.


-
uint32_t size