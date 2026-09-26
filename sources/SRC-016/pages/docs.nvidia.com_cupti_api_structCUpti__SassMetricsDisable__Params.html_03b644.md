source: https://docs.nvidia.com/cupti/api/structCUpti__SassMetricsDisable__Params.html

# 7.217. CUpti_SassMetricsDisable_Params[#](https://docs.nvidia.com#cupti-sassmetricsdisable-params)

-
struct CUpti_SassMetricsDisable_Params
[#](https://docs.nvidia.com#_CPPv431CUpti_SassMetricsDisable_Params) Params for cuptiSassMetricsDisable.

Public Members

-
size_t structSize
[#](https://docs.nvidia.com#_CPPv4N31CUpti_SassMetricsDisable_Params10structSizeE) [in] equal to CUpti_SassMetricsDisable_Params_STRUCT_SIZE


-
void *pPriv
[#](https://docs.nvidia.com#_CPPv4N31CUpti_SassMetricsDisable_Params5pPrivE) [in] assign to NULL


-
CUcontext ctx
[#](https://docs.nvidia.com#_CPPv4N31CUpti_SassMetricsDisable_Params3ctxE) [in] CUDA context on which SASS metric data collection will be disabled. If set NULL, default context will be consider for SASS metric data collection.


-
size_t numOfDroppedRecords
[#](https://docs.nvidia.com#_CPPv4N31CUpti_SassMetricsDisable_Params19numOfDroppedRecordsE) [out] Num of dropped SASS records will be equal to numOfPatchedInstructions * numOfInstances. Number of dropped records will be zero when data is flushed prior to calling the disable API.


-
size_t structSize