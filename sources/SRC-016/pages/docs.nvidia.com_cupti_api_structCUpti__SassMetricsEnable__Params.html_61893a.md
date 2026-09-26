source: https://docs.nvidia.com/cupti/api/structCUpti__SassMetricsEnable__Params.html

# 7.218. CUpti_SassMetricsEnable_Params[#](https://docs.nvidia.com#cupti-sassmetricsenable-params)

-
struct CUpti_SassMetricsEnable_Params
[#](https://docs.nvidia.com#_CPPv430CUpti_SassMetricsEnable_Params) Params for cuptiSassMetricsEnable.

Public Members

-
size_t structSize
[#](https://docs.nvidia.com#_CPPv4N30CUpti_SassMetricsEnable_Params10structSizeE) [in] equal to CUpti_SassMetricsEnable_Params_STRUCT_SIZE


-
void *pPriv
[#](https://docs.nvidia.com#_CPPv4N30CUpti_SassMetricsEnable_Params5pPrivE) [in] assign to NULL


-
CUcontext ctx
[#](https://docs.nvidia.com#_CPPv4N30CUpti_SassMetricsEnable_Params3ctxE) [in] CUDA context on which SASS metric data collection will be enabled. If set NULL, default context will be consider for SASS metric data collection.


-
uint8_t enableLazyPatching
[#](https://docs.nvidia.com#_CPPv4N30CUpti_SassMetricsEnable_Params18enableLazyPatchingE) [in] if false, all the functions will patched regardless of their execution with

[cuptiSassMetricsEnable()](https://docs.nvidia.com/group__CUPTI__SASS__METRICS__API.html#group__cupti__sass__metrics__api_1ga62ea0db81c966ddf066c28644f8b240f)API call. when this parameter is set to true, metric data collection for the function will be done at the very first execution in the enable/disble range.

-
size_t structSize