source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityUnifiedMemoryCounterConfig.html

# 7.133. CUpti_ActivityUnifiedMemoryCounterConfig[#](https://docs.nvidia.com#cupti-activityunifiedmemorycounterconfig)

-
struct CUpti_ActivityUnifiedMemoryCounterConfig
[#](https://docs.nvidia.com#_CPPv440CUpti_ActivityUnifiedMemoryCounterConfig) Unified Memory counters configuration structure.

This structure controls the enable/disable of the various Unified Memory counters consisting of scope, kind and other parameters. See function

[cuptiActivityConfigureUnifiedMemoryCounter](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#group__cupti__activity__api_1ga8ec9b1229ba07a98aac9db4600d4325c)Public Members

-
[CUpti_ActivityUnifiedMemoryCounterScope](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv439CUpti_ActivityUnifiedMemoryCounterScope)scope[#](https://docs.nvidia.com#_CPPv4N40CUpti_ActivityUnifiedMemoryCounterConfig5scopeE) Unified Memory counter Counter scope.

(deprecated in CUDA 7.0)


-
[CUpti_ActivityUnifiedMemoryCounterKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv438CUpti_ActivityUnifiedMemoryCounterKind)kind[#](https://docs.nvidia.com#_CPPv4N40CUpti_ActivityUnifiedMemoryCounterConfig4kindE) Unified Memory counter Counter kind.


-
uint32_t deviceId
[#](https://docs.nvidia.com#_CPPv4N40CUpti_ActivityUnifiedMemoryCounterConfig8deviceIdE) Device id of the target device.

This is relevant only for single device scopes. (deprecated in CUDA 7.0)


-
uint32_t enable
[#](https://docs.nvidia.com#_CPPv4N40CUpti_ActivityUnifiedMemoryCounterConfig6enableE) Control to enable/disable the counter.

To enable the counter set it to non-zero value while disable is indicated by zero.


-