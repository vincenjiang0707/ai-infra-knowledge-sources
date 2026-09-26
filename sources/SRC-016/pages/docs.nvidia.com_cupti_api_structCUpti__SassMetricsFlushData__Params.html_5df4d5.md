source: https://docs.nvidia.com/cupti/api/structCUpti__SassMetricsFlushData__Params.html

# 7.219. CUpti_SassMetricsFlushData_Params[#](https://docs.nvidia.com#cupti-sassmetricsflushdata-params)

-
struct CUpti_SassMetricsFlushData_Params
[#](https://docs.nvidia.com#_CPPv433CUpti_SassMetricsFlushData_Params) Params for cuptiSassMetricsFlushData.

Public Members

-
size_t structSize
[#](https://docs.nvidia.com#_CPPv4N33CUpti_SassMetricsFlushData_Params10structSizeE) [in] equal to CUpti_SassMetricsFlushData_Params_STRUCT_SIZE


-
void *pPriv
[#](https://docs.nvidia.com#_CPPv4N33CUpti_SassMetricsFlushData_Params5pPrivE) [in] assign to NULL


-
CUcontext ctx
[#](https://docs.nvidia.com#_CPPv4N33CUpti_SassMetricsFlushData_Params3ctxE) [in] CUDA context on which SASS metric data collection was enabled. If set NULL, default context will be consider for SASS metric data collection.


-
size_t numOfPatchedInstructionRecords
[#](https://docs.nvidia.com#_CPPv4N33CUpti_SassMetricsFlushData_Params30numOfPatchedInstructionRecordsE) [in] number of patched instruction record will be retrived, user can call

[cuptiSassMetricsGetDataProperties()](https://docs.nvidia.com/group__CUPTI__SASS__METRICS__API.html#group__cupti__sass__metrics__api_1ga2601b1a5b4fe4b9253cdb81f04120b1e)for getting total number of records available.

-
size_t numOfInstances
[#](https://docs.nvidia.com#_CPPv4N33CUpti_SassMetricsFlushData_Params14numOfInstancesE) [in] number of patched instruction record instances for a metric, user can call

[cuptiSassMetricsGetDataProperties()](https://docs.nvidia.com/group__CUPTI__SASS__METRICS__API.html#group__cupti__sass__metrics__api_1ga2601b1a5b4fe4b9253cdb81f04120b1e)for getting total number of instances for each record per metric available.

-
[CUpti_SassMetrics_Data](https://docs.nvidia.com/structCUpti__SassMetrics__Data.html#_CPPv422CUpti_SassMetrics_Data)*pMetricsData[#](https://docs.nvidia.com#_CPPv4N33CUpti_SassMetricsFlushData_Params12pMetricsDataE) [out]


-
size_t structSize