source: https://docs.nvidia.com/cupti/api/structCUpti__RangeProfiler__DecodeData__Params.html

# 7.205. CUpti_RangeProfiler_DecodeData_Params[#](https://docs.nvidia.com#cupti-rangeprofiler-decodedata-params)

-
struct CUpti_RangeProfiler_DecodeData_Params
[#](https://docs.nvidia.com#_CPPv437CUpti_RangeProfiler_DecodeData_Params) Params for cuptiRangeProfilerDecodeData.

Public Members

-
size_t structSize
[#](https://docs.nvidia.com#_CPPv4N37CUpti_RangeProfiler_DecodeData_Params10structSizeE) [in] Size of the data structure.


-
void *pPriv
[#](https://docs.nvidia.com#_CPPv4N37CUpti_RangeProfiler_DecodeData_Params5pPrivE) [in] Set to NULL.


-
[CUpti_RangeProfiler_Object](https://docs.nvidia.com/group__CUPTI__RANGE__PROFILER__API.html#_CPPv426CUpti_RangeProfiler_Object)*pRangeProfilerObject[#](https://docs.nvidia.com#_CPPv4N37CUpti_RangeProfiler_DecodeData_Params20pRangeProfilerObjectE) [in] Range Profiler Object.


-
size_t numOfRangeDropped
[#](https://docs.nvidia.com#_CPPv4N37CUpti_RangeProfiler_DecodeData_Params17numOfRangeDroppedE) [out] Number of ranges dropped in the processed passes.


-
size_t structSize