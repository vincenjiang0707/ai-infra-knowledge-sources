source: https://docs.nvidia.com/cupti/api/structCUpti__RangeProfiler__GetCounterDataSize__Params.html

# 7.209. CUpti_RangeProfiler_GetCounterDataSize_Params[#](https://docs.nvidia.com#cupti-rangeprofiler-getcounterdatasize-params)

-
struct CUpti_RangeProfiler_GetCounterDataSize_Params
[#](https://docs.nvidia.com#_CPPv445CUpti_RangeProfiler_GetCounterDataSize_Params) Params for cuptiRangeProfilerGetCounterDataSize.

Public Members

-
size_t structSize
[#](https://docs.nvidia.com#_CPPv4N45CUpti_RangeProfiler_GetCounterDataSize_Params10structSizeE) [in] Size of the data structure.


-
void *pPriv
[#](https://docs.nvidia.com#_CPPv4N45CUpti_RangeProfiler_GetCounterDataSize_Params5pPrivE) [in] Set to NULL.


-
[CUpti_RangeProfiler_Object](https://docs.nvidia.com/group__CUPTI__RANGE__PROFILER__API.html#_CPPv426CUpti_RangeProfiler_Object)*pRangeProfilerObject[#](https://docs.nvidia.com#_CPPv4N45CUpti_RangeProfiler_GetCounterDataSize_Params20pRangeProfilerObjectE) [in] Periodic sampler object.


-
const char **pMetricNames
[#](https://docs.nvidia.com#_CPPv4N45CUpti_RangeProfiler_GetCounterDataSize_Params12pMetricNamesE) [in] Names of the metrics to be collected.


-
size_t numMetrics
[#](https://docs.nvidia.com#_CPPv4N45CUpti_RangeProfiler_GetCounterDataSize_Params10numMetricsE) [in] Number of metrics to be collected.


-
size_t maxNumOfRanges
[#](https://docs.nvidia.com#_CPPv4N45CUpti_RangeProfiler_GetCounterDataSize_Params14maxNumOfRangesE) [in] Maximum number of ranges to be stored in the counter data image.


-
uint32_t maxNumRangeTreeNodes
[#](https://docs.nvidia.com#_CPPv4N45CUpti_RangeProfiler_GetCounterDataSize_Params20maxNumRangeTreeNodesE) [in] Maximum number of RangeTree nodes; must be >= maxNumOfRanges


-
size_t counterDataSize
[#](https://docs.nvidia.com#_CPPv4N45CUpti_RangeProfiler_GetCounterDataSize_Params15counterDataSizeE) [out] Size of the counter data image.


-
size_t structSize