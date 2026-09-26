source: https://docs.nvidia.com/cupti/api/structCUpti__SassMetricsSetConfig__Params.html

# 7.221. CUpti_SassMetricsSetConfig_Params[#](https://docs.nvidia.com#cupti-sassmetricssetconfig-params)

-
struct CUpti_SassMetricsSetConfig_Params
[#](https://docs.nvidia.com#_CPPv433CUpti_SassMetricsSetConfig_Params) Params for cuptiSassMetricsSetConfig.

Public Members

-
size_t structSize
[#](https://docs.nvidia.com#_CPPv4N33CUpti_SassMetricsSetConfig_Params10structSizeE) [in] equal to CUpti_SassMetricsSetConfig_Params_STRUCT_SIZE


-
void *pPriv
[#](https://docs.nvidia.com#_CPPv4N33CUpti_SassMetricsSetConfig_Params5pPrivE) [in] assign to NULL


-
size_t numOfMetricConfig
[#](https://docs.nvidia.com#_CPPv4N33CUpti_SassMetricsSetConfig_Params17numOfMetricConfigE) [in] num of metric configs, will be equal to number of metrics queried


-
[CUpti_SassMetrics_Config](https://docs.nvidia.com/structCUpti__SassMetrics__Config.html#_CPPv424CUpti_SassMetrics_Config)*pConfigs[#](https://docs.nvidia.com#_CPPv4N33CUpti_SassMetricsSetConfig_Params8pConfigsE) [in] list of metric config generated for given sass metrics


-
uint32_t deviceIndex
[#](https://docs.nvidia.com#_CPPv4N33CUpti_SassMetricsSetConfig_Params11deviceIndexE) [in] device index for which config will be set, user can call this once for the device on which the the SASS metric data will be collected


-
size_t structSize