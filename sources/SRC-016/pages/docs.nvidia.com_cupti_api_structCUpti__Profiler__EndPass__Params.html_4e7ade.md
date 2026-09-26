source: https://docs.nvidia.com/cupti/api/structCUpti__Profiler__EndPass__Params.html

# 7.177. CUpti_Profiler_EndPass_Params[#](https://docs.nvidia.com#cupti-profiler-endpass-params)

-
struct CUpti_Profiler_EndPass_Params
[#](https://docs.nvidia.com#_CPPv429CUpti_Profiler_EndPass_Params) Params for cuptiProfilerEndPass.

Public Members

-
size_t structSize
[#](https://docs.nvidia.com#_CPPv4N29CUpti_Profiler_EndPass_Params10structSizeE) [in] CUpti_Profiler_EndPass_Params_STRUCT_SIZE


-
void *pPriv
[#](https://docs.nvidia.com#_CPPv4N29CUpti_Profiler_EndPass_Params5pPrivE) [in] assign to NULL


-
CUcontext ctx
[#](https://docs.nvidia.com#_CPPv4N29CUpti_Profiler_EndPass_Params3ctxE) [in] if NULL, the current CUcontext is used


-
size_t passIndex
[#](https://docs.nvidia.com#_CPPv4N29CUpti_Profiler_EndPass_Params9passIndexE) [out] The targetNestingLevel that will be collected by the

*next*BeginPass.[out] The passIndex that will be collected by the

*next*BeginPass

-
uint8_t allPassesSubmitted
[#](https://docs.nvidia.com#_CPPv4N29CUpti_Profiler_EndPass_Params18allPassesSubmittedE) [out] becomes true when the last pass has been queued to the GPU


-
size_t structSize