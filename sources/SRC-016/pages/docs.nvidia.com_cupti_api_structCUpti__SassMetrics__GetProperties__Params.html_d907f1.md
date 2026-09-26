source: https://docs.nvidia.com/cupti/api/structCUpti__SassMetrics__GetProperties__Params.html

# 7.227. CUpti_SassMetrics_GetProperties_Params[#](https://docs.nvidia.com#cupti-sassmetrics-getproperties-params)

-
struct CUpti_SassMetrics_GetProperties_Params
[#](https://docs.nvidia.com#_CPPv438CUpti_SassMetrics_GetProperties_Params) Params for cuptiSassMetricsGetProperties.

Public Members

-
size_t structSize
[#](https://docs.nvidia.com#_CPPv4N38CUpti_SassMetrics_GetProperties_Params10structSizeE) [in] should be equal to CUpti_SassMetrics_GetProperties_Params_STRUCT_SIZE


-
void *pPriv
[#](https://docs.nvidia.com#_CPPv4N38CUpti_SassMetrics_GetProperties_Params5pPrivE) [in] assign to NULL


-
const char *pChipName
[#](https://docs.nvidia.com#_CPPv4N38CUpti_SassMetrics_GetProperties_Params9pChipNameE) [in] chip name for which metric will be queried


-
const char *pMetricName
[#](https://docs.nvidia.com#_CPPv4N38CUpti_SassMetrics_GetProperties_Params11pMetricNameE) [in] metric name


-
[CUpti_SassMetrics_MetricDetails](https://docs.nvidia.com/structCUpti__SassMetrics__MetricDetails.html#_CPPv431CUpti_SassMetrics_MetricDetails)metric[#](https://docs.nvidia.com#_CPPv4N38CUpti_SassMetrics_GetProperties_Params6metricE) [out] returns the metric ID and the metric description


-
size_t structSize