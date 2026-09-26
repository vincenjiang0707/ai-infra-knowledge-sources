source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityComputeEngineCtxSwitch.html

# 7.9. CUpti_ActivityComputeEngineCtxSwitch[#](https://docs.nvidia.com#cupti-activitycomputeenginectxswitch)

-
struct CUpti_ActivityComputeEngineCtxSwitch
[#](https://docs.nvidia.com#_CPPv436CUpti_ActivityComputeEngineCtxSwitch) The activity record for trace of CUDA context switch events.

The corresponding activity kind is CUPTI_ACTIVITY_KIND_COMPUTE_ENGINE_CTX_SWITCH.

Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N36CUpti_ActivityComputeEngineCtxSwitch4kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_COMPUTE_ENGINE_CTX_SWITCH.


-
uint32_t contextId
[#](https://docs.nvidia.com#_CPPv4N36CUpti_ActivityComputeEngineCtxSwitch9contextIdE) The ID of the CUDA context.


-
uint64_t timestamp
[#](https://docs.nvidia.com#_CPPv4N36CUpti_ActivityComputeEngineCtxSwitch9timestampE) The timestamp at which the CUpti_ComputeEngineCtxSwitchOperationType occurs.


-
[CUpti_ComputeEngineCtxSwitchOperationType](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv441CUpti_ComputeEngineCtxSwitchOperationType)operationType[#](https://docs.nvidia.com#_CPPv4N36CUpti_ActivityComputeEngineCtxSwitch13operationTypeE) The type of the Compute Engine Context switch operation.

CUPTI_COMPUTE_ENGINE_CTX_SWITCH_OPERATION_START indicates the start of the context switch operation. CUPTI_COMPUTE_ENGINE_CTX_SWITCH_OPERATION_END indicates the end of the context switch operation.


-