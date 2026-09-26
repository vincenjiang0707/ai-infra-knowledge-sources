source: https://docs.nvidia.com/cupti/api/structCUpti__RangeProfiler__Enable__Params.html

# 7.207. CUpti_RangeProfiler_Enable_Params[#](https://docs.nvidia.com#cupti-rangeprofiler-enable-params)

-
struct CUpti_RangeProfiler_Enable_Params
[#](https://docs.nvidia.com#_CPPv433CUpti_RangeProfiler_Enable_Params) Params for cuptiRangeProfilerEnable.

Public Members

-
size_t structSize
[#](https://docs.nvidia.com#_CPPv4N33CUpti_RangeProfiler_Enable_Params10structSizeE) [in] Size of the data structure.


-
void *pPriv
[#](https://docs.nvidia.com#_CPPv4N33CUpti_RangeProfiler_Enable_Params5pPrivE) [in] Set to NULL.


-
CUcontext ctx
[#](https://docs.nvidia.com#_CPPv4N33CUpti_RangeProfiler_Enable_Params3ctxE) [in] Context to be used for profiling. For green context, users can convert the green context to CUDA context using cuCtxFromGreenCtx and pass the CUDA context to this API.


-
[CUpti_RangeProfiler_Object](https://docs.nvidia.com/group__CUPTI__RANGE__PROFILER__API.html#_CPPv426CUpti_RangeProfiler_Object)*pRangeProfilerObject[#](https://docs.nvidia.com#_CPPv4N33CUpti_RangeProfiler_Enable_Params20pRangeProfilerObjectE) [out] Range Profiler Object.


-
[CUpti_CacheControl_Mode](https://docs.nvidia.com/group__CUPTI__RANGE__PROFILER__API.html#_CPPv423CUpti_CacheControl_Mode)cacheControlMode[#](https://docs.nvidia.com#_CPPv4N33CUpti_RangeProfiler_Enable_Params16cacheControlModeE) [in] Cache-control mode. Defaults to CUPTI_CACHE_CONTROL_MODE_NONE for zero-initialized structs.


-
size_t structSize