source: https://docs.nvidia.com/cupti/api/structCUpti__RangeProfiler__CounterData__GetRangeInfo__Params.html

# 7.204. CUpti_RangeProfiler_CounterData_GetRangeInfo_Params[#](https://docs.nvidia.com#cupti-rangeprofiler-counterdata-getrangeinfo-params)

-
struct CUpti_RangeProfiler_CounterData_GetRangeInfo_Params
[#](https://docs.nvidia.com#_CPPv451CUpti_RangeProfiler_CounterData_GetRangeInfo_Params) Params for cuptiRangeProfilerCounterDataGetRangeInfo.

Public Members

-
size_t structSize
[#](https://docs.nvidia.com#_CPPv4N51CUpti_RangeProfiler_CounterData_GetRangeInfo_Params10structSizeE) [in] Size of the data structure.


-
void *pPriv
[#](https://docs.nvidia.com#_CPPv4N51CUpti_RangeProfiler_CounterData_GetRangeInfo_Params5pPrivE) [in] Set to NULL.


-
const uint8_t *pCounterDataImage
[#](https://docs.nvidia.com#_CPPv4N51CUpti_RangeProfiler_CounterData_GetRangeInfo_Params17pCounterDataImageE) [in] Counter data image.


-
size_t counterDataImageSize
[#](https://docs.nvidia.com#_CPPv4N51CUpti_RangeProfiler_CounterData_GetRangeInfo_Params20counterDataImageSizeE) [in] Size of the counter data image.


-
size_t rangeIndex
[#](https://docs.nvidia.com#_CPPv4N51CUpti_RangeProfiler_CounterData_GetRangeInfo_Params10rangeIndexE) [in] Index of the sample.


-
const char *rangeDelimiter
[#](https://docs.nvidia.com#_CPPv4N51CUpti_RangeProfiler_CounterData_GetRangeInfo_Params14rangeDelimiterE) [in] range delimiter.


-
const char *rangeName
[#](https://docs.nvidia.com#_CPPv4N51CUpti_RangeProfiler_CounterData_GetRangeInfo_Params9rangeNameE) [out] RangeName;


-
size_t structSize