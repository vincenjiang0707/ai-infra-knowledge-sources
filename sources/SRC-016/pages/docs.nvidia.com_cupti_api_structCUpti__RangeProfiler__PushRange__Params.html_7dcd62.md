source: https://docs.nvidia.com/cupti/api/structCUpti__RangeProfiler__PushRange__Params.html

# 7.212. CUpti_RangeProfiler_PushRange_Params[#](https://docs.nvidia.com#cupti-rangeprofiler-pushrange-params)

-
struct CUpti_RangeProfiler_PushRange_Params
[#](https://docs.nvidia.com#_CPPv436CUpti_RangeProfiler_PushRange_Params) Params for cuptiRangeProfilerPushRange.

Public Members

-
size_t structSize
[#](https://docs.nvidia.com#_CPPv4N36CUpti_RangeProfiler_PushRange_Params10structSizeE) [in] Size of the data structure.


-
void *pPriv
[#](https://docs.nvidia.com#_CPPv4N36CUpti_RangeProfiler_PushRange_Params5pPrivE) [in] Set to NULL.


-
[CUpti_RangeProfiler_Object](https://docs.nvidia.com/group__CUPTI__RANGE__PROFILER__API.html#_CPPv426CUpti_RangeProfiler_Object)*pRangeProfilerObject[#](https://docs.nvidia.com#_CPPv4N36CUpti_RangeProfiler_PushRange_Params20pRangeProfilerObjectE) [in] Range Profiler Object.


-
const char *pRangeName
[#](https://docs.nvidia.com#_CPPv4N36CUpti_RangeProfiler_PushRange_Params10pRangeNameE) [in] Name of the range to be profiled (only valid for User range mode).


-
size_t structSize