source: https://docs.nvidia.com/cupti/api/structCUpti__PmSampling__GetCounterDataSize__Params.html

# 7.162. CUpti_PmSampling_GetCounterDataSize_Params[#](https://docs.nvidia.com#cupti-pmsampling-getcounterdatasize-params)

-
struct CUpti_PmSampling_GetCounterDataSize_Params
[#](https://docs.nvidia.com#_CPPv442CUpti_PmSampling_GetCounterDataSize_Params) Params for cuptiPmSamplingGetCounterDataSize.

Public Members

-
size_t structSize
[#](https://docs.nvidia.com#_CPPv4N42CUpti_PmSampling_GetCounterDataSize_Params10structSizeE) [in] Size of the data structure.


-
void *pPriv
[#](https://docs.nvidia.com#_CPPv4N42CUpti_PmSampling_GetCounterDataSize_Params5pPrivE) [in] Set to NULL.


-
[CUpti_PmSampling_Object](https://docs.nvidia.com/group__CUPTI__PM__SAMPLING__API.html#_CPPv423CUpti_PmSampling_Object)*pPmSamplingObject[#](https://docs.nvidia.com#_CPPv4N42CUpti_PmSampling_GetCounterDataSize_Params17pPmSamplingObjectE) [in] PM sampling object.


-
const char **pMetricNames
[#](https://docs.nvidia.com#_CPPv4N42CUpti_PmSampling_GetCounterDataSize_Params12pMetricNamesE) [in] Names of the metrics to be collected.


-
size_t numMetrics
[#](https://docs.nvidia.com#_CPPv4N42CUpti_PmSampling_GetCounterDataSize_Params10numMetricsE) [in] Number of metrics to be collected.


-
uint32_t maxSamples
[#](https://docs.nvidia.com#_CPPv4N42CUpti_PmSampling_GetCounterDataSize_Params10maxSamplesE) [in] Maximum number of samples to be stored in the counter data image.


-
size_t counterDataSize
[#](https://docs.nvidia.com#_CPPv4N42CUpti_PmSampling_GetCounterDataSize_Params15counterDataSizeE) [out] Size of the counter data image.


-
size_t structSize