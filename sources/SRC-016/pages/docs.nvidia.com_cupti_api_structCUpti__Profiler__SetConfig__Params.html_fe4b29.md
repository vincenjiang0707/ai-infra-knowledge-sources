source: https://docs.nvidia.com/cupti/api/structCUpti__Profiler__SetConfig__Params.html

# 7.201. CUpti_Profiler_SetConfig_Params[#](https://docs.nvidia.com#cupti-profiler-setconfig-params)

-
struct CUpti_Profiler_SetConfig_Params
[#](https://docs.nvidia.com#_CPPv431CUpti_Profiler_SetConfig_Params) Params for cuptiProfilerSetConfig.

Public Members

-
size_t structSize
[#](https://docs.nvidia.com#_CPPv4N31CUpti_Profiler_SetConfig_Params10structSizeE) [in] CUpti_Profiler_SetConfig_Params_STRUCT_SIZE


-
void *pPriv
[#](https://docs.nvidia.com#_CPPv4N31CUpti_Profiler_SetConfig_Params5pPrivE) [in] assign to NULL


-
CUcontext ctx
[#](https://docs.nvidia.com#_CPPv4N31CUpti_Profiler_SetConfig_Params3ctxE) [in] if NULL, the current CUcontext is used


-
const uint8_t *pConfig
[#](https://docs.nvidia.com#_CPPv4N31CUpti_Profiler_SetConfig_Params7pConfigE) [in] Config created by NVPW_RawMetricsConfig_GetConfigImage(). Must be align(8).


-
size_t configSize
[#](https://docs.nvidia.com#_CPPv4N31CUpti_Profiler_SetConfig_Params10configSizeE) [in] size of config


-
uint16_t minNestingLevel
[#](https://docs.nvidia.com#_CPPv4N31CUpti_Profiler_SetConfig_Params15minNestingLevelE) [in] the lowest nesting level to be profiled; must be >= 1


-
uint16_t numNestingLevels
[#](https://docs.nvidia.com#_CPPv4N31CUpti_Profiler_SetConfig_Params16numNestingLevelsE) [in] the number of nesting levels to profile; must be >= 1


-
size_t passIndex
[#](https://docs.nvidia.com#_CPPv4N31CUpti_Profiler_SetConfig_Params9passIndexE) [in] Set this to zero for in-app replay; set this to the output of EndPass() for application replay


-
uint16_t targetNestingLevel
[#](https://docs.nvidia.com#_CPPv4N31CUpti_Profiler_SetConfig_Params18targetNestingLevelE) [in] Set this to minNestingLevel for in-app replay; set this to the output of EndPass() for application


-
size_t structSize