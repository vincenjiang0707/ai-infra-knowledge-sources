source: https://docs.nvidia.com/cupti/api/structCUpti__SassMetrics__GetMetrics__Params.html

# 7.225. CUpti_SassMetrics_GetMetrics_Params[#](https://docs.nvidia.com#cupti-sassmetrics-getmetrics-params)

-
struct CUpti_SassMetrics_GetMetrics_Params
[#](https://docs.nvidia.com#_CPPv435CUpti_SassMetrics_GetMetrics_Params) Params for cuptiSassMetricsGetMetrics.

Public Members

-
size_t structSize
[#](https://docs.nvidia.com#_CPPv4N35CUpti_SassMetrics_GetMetrics_Params10structSizeE) [in] should be equal to CUpti_SassMetrics_GetMetrics_Params_STRUCT_SIZE


-
void *pPriv
[#](https://docs.nvidia.com#_CPPv4N35CUpti_SassMetrics_GetMetrics_Params5pPrivE) [in] assign to NULL


-
const char *pChipName
[#](https://docs.nvidia.com#_CPPv4N35CUpti_SassMetrics_GetMetrics_Params9pChipNameE) [in] chip name for which metrics will be queried


-
size_t numOfMetrics
[#](https://docs.nvidia.com#_CPPv4N35CUpti_SassMetrics_GetMetrics_Params12numOfMetricsE) [in] number of metrics supported for the queried chip (can be queried using

[cuptiSassMetricsGetNumOfMetrics()](https://docs.nvidia.com/group__CUPTI__SASS__METRICS__API.html#group__cupti__sass__metrics__api_1ga3019950028060e943b12b7fc6f1b9188))

-
[CUpti_SassMetrics_MetricDetails](https://docs.nvidia.com/structCUpti__SassMetrics__MetricDetails.html#_CPPv431CUpti_SassMetrics_MetricDetails)*pMetricsList[#](https://docs.nvidia.com#_CPPv4N35CUpti_SassMetrics_GetMetrics_Params12pMetricsListE) [out] list of metrics supported for queried chip


-
size_t structSize