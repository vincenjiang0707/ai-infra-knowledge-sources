source: https://docs.nvidia.com/cupti/api/structCUpti__SassMetricsUnsetConfig__Params.html

# 7.222. CUpti_SassMetricsUnsetConfig_Params[#](https://docs.nvidia.com#cupti-sassmetricsunsetconfig-params)

-
struct CUpti_SassMetricsUnsetConfig_Params
[#](https://docs.nvidia.com#_CPPv435CUpti_SassMetricsUnsetConfig_Params) Params for cuptiSassMetricsUnsetConfig.

Public Members

-
size_t structSize
[#](https://docs.nvidia.com#_CPPv4N35CUpti_SassMetricsUnsetConfig_Params10structSizeE) [in] equal to CUpti_SassMetricsUnsetConfig_Params_STRUCT_SIZE


-
void *pPriv
[#](https://docs.nvidia.com#_CPPv4N35CUpti_SassMetricsUnsetConfig_Params5pPrivE) [in] assign to NULL


-
uint32_t deviceIndex
[#](https://docs.nvidia.com#_CPPv4N35CUpti_SassMetricsUnsetConfig_Params11deviceIndexE) [in] device index for which SASS metric data collection config will get reset, user need to call this API for all the devices on which the the SASS metric data collection have been configured.


-
size_t structSize