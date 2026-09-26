source: https://docs.nvidia.com/cupti/api/structCUpti__Profiler__Host__GetSubMetrics__Params.html

# 7.193. CUpti_Profiler_Host_GetSubMetrics_Params[#](https://docs.nvidia.com#cupti-profiler-host-getsubmetrics-params)

-
struct CUpti_Profiler_Host_GetSubMetrics_Params
[#](https://docs.nvidia.com#_CPPv440CUpti_Profiler_Host_GetSubMetrics_Params) Params for cuptiProfilerHostGetSubMetrics.

Public Members

-
size_t structSize
[#](https://docs.nvidia.com#_CPPv4N40CUpti_Profiler_Host_GetSubMetrics_Params10structSizeE) [in] Size of the data structure.


-
void *pPriv
[#](https://docs.nvidia.com#_CPPv4N40CUpti_Profiler_Host_GetSubMetrics_Params5pPrivE) [in] Assign to NULL


-
[CUpti_Profiler_Host_Object](https://docs.nvidia.com/group__CUPTI__PROFILER__HOST__API.html#_CPPv426CUpti_Profiler_Host_Object)*pHostObject[#](https://docs.nvidia.com#_CPPv4N40CUpti_Profiler_Host_GetSubMetrics_Params11pHostObjectE) [in] reference to the profiler host object allocated by CUPTI in cuptiProfilerHostInitialize


-
[CUpti_MetricType](https://docs.nvidia.com/group__CUPTI__PROFILER__HOST__API.html#_CPPv416CUpti_MetricType)metricType[#](https://docs.nvidia.com#_CPPv4N40CUpti_Profiler_Host_GetSubMetrics_Params10metricTypeE) [in] the metric type for queried metric


-
const char *pMetricName
[#](https://docs.nvidia.com#_CPPv4N40CUpti_Profiler_Host_GetSubMetrics_Params11pMetricNameE) [in] metric name for which sub-metric will be listed. Metric name can be with or without extension (rollup or submetric)


-
size_t numOfSubmetrics
[#](https://docs.nvidia.com#_CPPv4N40CUpti_Profiler_Host_GetSubMetrics_Params15numOfSubmetricsE) [out] number of submetrics supported


-
const char **ppSubMetrics
[#](https://docs.nvidia.com#_CPPv4N40CUpti_Profiler_Host_GetSubMetrics_Params12ppSubMetricsE) [out] list of submetrics supported for the metric.


-
size_t structSize