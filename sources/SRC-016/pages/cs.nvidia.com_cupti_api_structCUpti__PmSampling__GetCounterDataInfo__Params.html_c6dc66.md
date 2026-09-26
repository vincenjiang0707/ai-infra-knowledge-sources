source: https://docs.nvidia.com/cupti/api/structCUpti__PmSampling__GetCounterDataInfo__Params.html

# 7.161. CUpti_PmSampling_GetCounterDataInfo_Params[#](https://docs.nvidia.com#cupti-pmsampling-getcounterdatainfo-params)

-
struct CUpti_PmSampling_GetCounterDataInfo_Params
[#](https://docs.nvidia.com#_CPPv442CUpti_PmSampling_GetCounterDataInfo_Params) Params for cuptiPmSamplingGetCounterDataInfo.

Public Members

-
size_t structSize
[#](https://docs.nvidia.com#_CPPv4N42CUpti_PmSampling_GetCounterDataInfo_Params10structSizeE) [in] Size of the data structure.


-
void *pPriv
[#](https://docs.nvidia.com#_CPPv4N42CUpti_PmSampling_GetCounterDataInfo_Params5pPrivE) [in] Set to NULL.


-
const uint8_t *pCounterDataImage
[#](https://docs.nvidia.com#_CPPv4N42CUpti_PmSampling_GetCounterDataInfo_Params17pCounterDataImageE) [in] Counter data image.


-
size_t counterDataImageSize
[#](https://docs.nvidia.com#_CPPv4N42CUpti_PmSampling_GetCounterDataInfo_Params20counterDataImageSizeE) [in] Size of the counter data image.


-
size_t numTotalSamples
[#](https://docs.nvidia.com#_CPPv4N42CUpti_PmSampling_GetCounterDataInfo_Params15numTotalSamplesE) [out] Number of samples in the counter data image.


-
size_t numPopulatedSamples
[#](https://docs.nvidia.com#_CPPv4N42CUpti_PmSampling_GetCounterDataInfo_Params19numPopulatedSamplesE) [out] Number of populated samples.


-
size_t numCompletedSamples
[#](https://docs.nvidia.com#_CPPv4N42CUpti_PmSampling_GetCounterDataInfo_Params19numCompletedSamplesE) [out] Number of samples that have been completed.


-
size_t structSize