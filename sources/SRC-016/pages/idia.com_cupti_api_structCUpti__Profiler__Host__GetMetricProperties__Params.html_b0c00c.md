source: https://docs.nvidia.com/cupti/api/structCUpti__Profiler__Host__GetMetricProperties__Params.html

# 7.188. CUpti_Profiler_Host_GetMetricProperties_Params[#](https://docs.nvidia.com#cupti-profiler-host-getmetricproperties-params)

-
struct CUpti_Profiler_Host_GetMetricProperties_Params
[#](https://docs.nvidia.com#_CPPv446CUpti_Profiler_Host_GetMetricProperties_Params) Params for cuptiProfilerHostGetMetricProperties.

Public Members

-
size_t structSize
[#](https://docs.nvidia.com#_CPPv4N46CUpti_Profiler_Host_GetMetricProperties_Params10structSizeE) [in] Size of the data structure.


-
void *pPriv
[#](https://docs.nvidia.com#_CPPv4N46CUpti_Profiler_Host_GetMetricProperties_Params5pPrivE) [in] Assign to NULL


-
[CUpti_Profiler_Host_Object](https://docs.nvidia.com/group__CUPTI__PROFILER__HOST__API.html#_CPPv426CUpti_Profiler_Host_Object)*pHostObject[#](https://docs.nvidia.com#_CPPv4N46CUpti_Profiler_Host_GetMetricProperties_Params11pHostObjectE) [in] reference to the profiler host object allocated by CUPTI in cuptiProfilerHostInitialize


-
const char *pMetricName
[#](https://docs.nvidia.com#_CPPv4N46CUpti_Profiler_Host_GetMetricProperties_Params11pMetricNameE) [in] metric name for which its properties will be listed. Metric name can be with or without extension (rollup or submetric)


-
const char *pDescription
[#](https://docs.nvidia.com#_CPPv4N46CUpti_Profiler_Host_GetMetricProperties_Params12pDescriptionE) [out] a short description about the metric


-
const char *pHwUnit
[#](https://docs.nvidia.com#_CPPv4N46CUpti_Profiler_Host_GetMetricProperties_Params7pHwUnitE) [out] associated hw unit for the metric


-
const char *pDimUnit
[#](https://docs.nvidia.com#_CPPv4N46CUpti_Profiler_Host_GetMetricProperties_Params8pDimUnitE) [out] the dimension of the metric values


-
[CUpti_MetricType](https://docs.nvidia.com/group__CUPTI__PROFILER__HOST__API.html#_CPPv416CUpti_MetricType)metricType[#](https://docs.nvidia.com#_CPPv4N46CUpti_Profiler_Host_GetMetricProperties_Params10metricTypeE) [out] the metric type (counter, ratio or throughput)


-
[CUpti_MetricCollectionScope](https://docs.nvidia.com/group__CUPTI__PROFILER__HOST__API.html#_CPPv427CUpti_MetricCollectionScope)metricCollectionScope[#](https://docs.nvidia.com#_CPPv4N46CUpti_Profiler_Host_GetMetricProperties_Params21metricCollectionScopeE) [out] the metric collection scope (context, device)


-
size_t structSize