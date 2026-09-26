source: https://docs.nvidia.com/cupti/api/structCUpti__Profiler__Host__GetMetricsInSinglePassSet__Params.html

# 7.189. CUpti_Profiler_Host_GetMetricsInSinglePassSet_Params[#](https://docs.nvidia.com#cupti-profiler-host-getmetricsinsinglepassset-params)

-
struct CUpti_Profiler_Host_GetMetricsInSinglePassSet_Params
[#](https://docs.nvidia.com#_CPPv452CUpti_Profiler_Host_GetMetricsInSinglePassSet_Params) Params for cuptiProfilerHostGetMetricsInSinglePassSet.

Public Members

-
size_t structSize
[#](https://docs.nvidia.com#_CPPv4N52CUpti_Profiler_Host_GetMetricsInSinglePassSet_Params10structSizeE) [in] Size of the data structure.


-
void *pPriv
[#](https://docs.nvidia.com#_CPPv4N52CUpti_Profiler_Host_GetMetricsInSinglePassSet_Params5pPrivE) [in] Assign to NULL


-
const char *pChipName
[#](https://docs.nvidia.com#_CPPv4N52CUpti_Profiler_Host_GetMetricsInSinglePassSet_Params9pChipNameE) [in] the chip name for which the metrics in the single pass metric set will be queried


-
const char *pSinglePassSetName
[#](https://docs.nvidia.com#_CPPv4N52CUpti_Profiler_Host_GetMetricsInSinglePassSet_Params18pSinglePassSetNameE) [in] the single pass metric set name for which the metrics will be queried


-
size_t numOfMetricsInSinglePassSet
[#](https://docs.nvidia.com#_CPPv4N52CUpti_Profiler_Host_GetMetricsInSinglePassSet_Params27numOfMetricsInSinglePassSetE) [inout] In Query mode, this will be returned as the number of metrics in the single pass metric set In Data retrieval mode, this must be set to the value returned in the query mode


-
size_t metricsBufferSize
[#](https://docs.nvidia.com#_CPPv4N52CUpti_Profiler_Host_GetMetricsInSinglePassSet_Params17metricsBufferSizeE) [inout] In Query mode, this will be returned as the buffer size needed for the metrics in the single pass metric set In Data retrieval mode, this must be set to the value returned in the query mode


-
size_t *pMetricsIndicesBuffer
[#](https://docs.nvidia.com#_CPPv4N52CUpti_Profiler_Host_GetMetricsInSinglePassSet_Params21pMetricsIndicesBufferE) [out] When set to NULL, the function call will treat it as query mode, otherwise it will treat it as data retrieval mode. User need to allocate the buffer for the metrics indices in the single pass metric set. The buffer size should be numOfMetricsInSinglePassSet * sizeof(size_t).


-
uint8_t *pMetricsBuffer
[#](https://docs.nvidia.com#_CPPv4N52CUpti_Profiler_Host_GetMetricsInSinglePassSet_Params14pMetricsBufferE) [out] When set to NULL, the function call will treat it as query mode, otherwise it will treat it as data retrieval mode. User need to allocate the buffer for the metrics in the single pass metric set. The buffer size should be metricsBufferSize bytes.


-
size_t structSize