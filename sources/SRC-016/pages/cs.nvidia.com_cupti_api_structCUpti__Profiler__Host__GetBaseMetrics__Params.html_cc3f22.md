source: https://docs.nvidia.com/cupti/api/structCUpti__Profiler__Host__GetBaseMetrics__Params.html

# 7.184. CUpti_Profiler_Host_GetBaseMetrics_Params[#](https://docs.nvidia.com#cupti-profiler-host-getbasemetrics-params)

-
struct CUpti_Profiler_Host_GetBaseMetrics_Params
[#](https://docs.nvidia.com#_CPPv441CUpti_Profiler_Host_GetBaseMetrics_Params) Params for cuptiProfilerHostGetSupportedMetrics.

Public Members

-
size_t structSize
[#](https://docs.nvidia.com#_CPPv4N41CUpti_Profiler_Host_GetBaseMetrics_Params10structSizeE) [in] Size of the data structure.


-
void *pPriv
[#](https://docs.nvidia.com#_CPPv4N41CUpti_Profiler_Host_GetBaseMetrics_Params5pPrivE) [in] Assign to NULL


-
struct
[CUpti_Profiler_Host_Object](https://docs.nvidia.com/group__CUPTI__PROFILER__HOST__API.html#_CPPv426CUpti_Profiler_Host_Object)*pHostObject[#](https://docs.nvidia.com#_CPPv4N41CUpti_Profiler_Host_GetBaseMetrics_Params11pHostObjectE) [in] reference to the profiler host object allocated by CUPTI in cuptiProfilerHostInitialize


-
[CUpti_MetricType](https://docs.nvidia.com/group__CUPTI__PROFILER__HOST__API.html#_CPPv416CUpti_MetricType)metricType[#](https://docs.nvidia.com#_CPPv4N41CUpti_Profiler_Host_GetBaseMetrics_Params10metricTypeE) [in] metric type (counter, ratio, throughput)


-
const char **ppMetricNames
[#](https://docs.nvidia.com#_CPPv4N41CUpti_Profiler_Host_GetBaseMetrics_Params13ppMetricNamesE) [out] list of base metrics supported of queried metric type for the chip


-
size_t numMetrics
[#](https://docs.nvidia.com#_CPPv4N41CUpti_Profiler_Host_GetBaseMetrics_Params10numMetricsE) [out] number of metrics


-
size_t structSize