source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityModule.html

# 7.97. CUpti_ActivityModule[#](https://docs.nvidia.com#cupti-activitymodule)

-
struct CUpti_ActivityModule
[#](https://docs.nvidia.com#_CPPv420CUpti_ActivityModule) The activity record for a CUDA module.

This activity record represents a CUDA module (CUPTI_ACTIVITY_KIND_MODULE). This activity record kind is not produced by the activity API but is included for completeness and ease-of-use. Profile frameworks built on top of CUPTI that collect module data from the module callback may choose to use this type to store the collected module data.