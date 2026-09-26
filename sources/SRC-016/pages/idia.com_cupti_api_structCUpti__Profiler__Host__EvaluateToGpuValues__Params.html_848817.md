source: https://docs.nvidia.com/cupti/api/structCUpti__Profiler__Host__EvaluateToGpuValues__Params.html

# 7.183. CUpti_Profiler_Host_EvaluateToGpuValues_Params[#](https://docs.nvidia.com#cupti-profiler-host-evaluatetogpuvalues-params)

-
struct CUpti_Profiler_Host_EvaluateToGpuValues_Params
[#](https://docs.nvidia.com#_CPPv446CUpti_Profiler_Host_EvaluateToGpuValues_Params) Params for cuptiProfilerHostEvaluateToGpuValues.

Public Members

-
size_t structSize
[#](https://docs.nvidia.com#_CPPv4N46CUpti_Profiler_Host_EvaluateToGpuValues_Params10structSizeE) [in] Size of the data structure.


-
void *pPriv
[#](https://docs.nvidia.com#_CPPv4N46CUpti_Profiler_Host_EvaluateToGpuValues_Params5pPrivE) [in] Assign to NULL


-
[CUpti_Profiler_Host_Object](https://docs.nvidia.com/group__CUPTI__PROFILER__HOST__API.html#_CPPv426CUpti_Profiler_Host_Object)*pHostObject[#](https://docs.nvidia.com#_CPPv4N46CUpti_Profiler_Host_EvaluateToGpuValues_Params11pHostObjectE) [in] reference to the profiler host object allocated by CUPTI in cuptiProfilerHostInitialize


-
const uint8_t *pCounterDataImage
[#](https://docs.nvidia.com#_CPPv4N46CUpti_Profiler_Host_EvaluateToGpuValues_Params17pCounterDataImageE) [in] the counter data image where profiling data has been decoded


-
size_t counterDataImageSize
[#](https://docs.nvidia.com#_CPPv4N46CUpti_Profiler_Host_EvaluateToGpuValues_Params20counterDataImageSizeE) [in] size of counter data image


-
size_t rangeIndex
[#](https://docs.nvidia.com#_CPPv4N46CUpti_Profiler_Host_EvaluateToGpuValues_Params10rangeIndexE) [in] range index for which the range name will be queried


-
const char **ppMetricNames
[#](https://docs.nvidia.com#_CPPv4N46CUpti_Profiler_Host_EvaluateToGpuValues_Params13ppMetricNamesE) [in] the metrics for which GPU values will be evaluated for the range


-
size_t numMetrics
[#](https://docs.nvidia.com#_CPPv4N46CUpti_Profiler_Host_EvaluateToGpuValues_Params10numMetricsE) [in] number of metrics


-
double *pMetricValues
[#](https://docs.nvidia.com#_CPPv4N46CUpti_Profiler_Host_EvaluateToGpuValues_Params13pMetricValuesE) [out] output value for given metric and range index


-
size_t structSize