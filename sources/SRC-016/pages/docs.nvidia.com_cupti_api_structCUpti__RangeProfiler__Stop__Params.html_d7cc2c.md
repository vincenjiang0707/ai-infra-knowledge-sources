source: https://docs.nvidia.com/cupti/api/structCUpti__RangeProfiler__Stop__Params.html

# 7.215. CUpti_RangeProfiler_Stop_Params[#](https://docs.nvidia.com#cupti-rangeprofiler-stop-params)

-
struct CUpti_RangeProfiler_Stop_Params
[#](https://docs.nvidia.com#_CPPv431CUpti_RangeProfiler_Stop_Params) Params for cuptiRangeProfilerStop.

Public Members

-
size_t structSize
[#](https://docs.nvidia.com#_CPPv4N31CUpti_RangeProfiler_Stop_Params10structSizeE) [in] Size of the data structure.


-
void *pPriv
[#](https://docs.nvidia.com#_CPPv4N31CUpti_RangeProfiler_Stop_Params5pPrivE) [in] Set to NULL.


-
[CUpti_RangeProfiler_Object](https://docs.nvidia.com/group__CUPTI__RANGE__PROFILER__API.html#_CPPv426CUpti_RangeProfiler_Object)*pRangeProfilerObject[#](https://docs.nvidia.com#_CPPv4N31CUpti_RangeProfiler_Stop_Params20pRangeProfilerObjectE) [in] Range Profiler Object.


-
size_t passIndex
[#](https://docs.nvidia.com#_CPPv4N31CUpti_RangeProfiler_Stop_Params9passIndexE) [out] pass index for the replay session.


-
size_t targetNestingLevel
[#](https://docs.nvidia.com#_CPPv4N31CUpti_RangeProfiler_Stop_Params18targetNestingLevelE) [out] target nesting level for the replay session.


-
uint8_t isAllPassSubmitted
[#](https://docs.nvidia.com#_CPPv4N31CUpti_RangeProfiler_Stop_Params18isAllPassSubmittedE) [out] 1 if all passes are submitted to GPU for collection, 0 otherwise.


-
size_t structSize