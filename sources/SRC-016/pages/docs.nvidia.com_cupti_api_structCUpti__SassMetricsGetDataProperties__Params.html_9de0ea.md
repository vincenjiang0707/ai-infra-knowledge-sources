source: https://docs.nvidia.com/cupti/api/structCUpti__SassMetricsGetDataProperties__Params.html

# 7.220. CUpti_SassMetricsGetDataProperties_Params[#](https://docs.nvidia.com#cupti-sassmetricsgetdataproperties-params)

-
struct CUpti_SassMetricsGetDataProperties_Params
[#](https://docs.nvidia.com#_CPPv441CUpti_SassMetricsGetDataProperties_Params) Params for cuptiSassMetricsGetDataProperties.

Public Members

-
size_t structSize
[#](https://docs.nvidia.com#_CPPv4N41CUpti_SassMetricsGetDataProperties_Params10structSizeE) [in] equal to CUpti_SassMetricsGetDataProperties_Params_STRUCT_SIZE


-
void *pPriv
[#](https://docs.nvidia.com#_CPPv4N41CUpti_SassMetricsGetDataProperties_Params5pPrivE) [in] assign to NULL


-
CUcontext ctx
[#](https://docs.nvidia.com#_CPPv4N41CUpti_SassMetricsGetDataProperties_Params3ctxE) [in] CUDA context on which SASS metric data collection was enabled. If set NULL, default context will be consider for SASS metric data collection.


-
size_t numOfPatchedInstructionRecords
[#](https://docs.nvidia.com#_CPPv4N41CUpti_SassMetricsGetDataProperties_Params30numOfPatchedInstructionRecordsE) [out] total number of SASS records has been collected


-
size_t numOfInstances
[#](https://docs.nvidia.com#_CPPv4N41CUpti_SassMetricsGetDataProperties_Params14numOfInstancesE) [out] number of instances for each metric value per instruction. This will depend on CUpti_SassPatching_OutputGranularity level set for the metric config.


-
size_t structSize