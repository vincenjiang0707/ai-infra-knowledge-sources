source: https://docs.nvidia.com/cupti/api/structCUpti__PmSampling__CounterData__GetSampleInfo__Params.html

# 7.156. CUpti_PmSampling_CounterData_GetSampleInfo_Params[#](https://docs.nvidia.com#cupti-pmsampling-counterdata-getsampleinfo-params)

-
struct CUpti_PmSampling_CounterData_GetSampleInfo_Params
[#](https://docs.nvidia.com#_CPPv449CUpti_PmSampling_CounterData_GetSampleInfo_Params) Params for cuptiPmSamplingCounterDataGetSampleInfo.

Public Members

-
size_t structSize
[#](https://docs.nvidia.com#_CPPv4N49CUpti_PmSampling_CounterData_GetSampleInfo_Params10structSizeE) [in] Size of the data structure.


-
void *pPriv
[#](https://docs.nvidia.com#_CPPv4N49CUpti_PmSampling_CounterData_GetSampleInfo_Params5pPrivE) [in] Set to NULL.


-
[CUpti_PmSampling_Object](https://docs.nvidia.com/group__CUPTI__PM__SAMPLING__API.html#_CPPv423CUpti_PmSampling_Object)*pPmSamplingObject[#](https://docs.nvidia.com#_CPPv4N49CUpti_PmSampling_CounterData_GetSampleInfo_Params17pPmSamplingObjectE) [in] PM sampling object.


-
const uint8_t *pCounterDataImage
[#](https://docs.nvidia.com#_CPPv4N49CUpti_PmSampling_CounterData_GetSampleInfo_Params17pCounterDataImageE) [in] Counter data image.


-
size_t counterDataImageSize
[#](https://docs.nvidia.com#_CPPv4N49CUpti_PmSampling_CounterData_GetSampleInfo_Params20counterDataImageSizeE) [in] Size of the counter data image.


-
size_t sampleIndex
[#](https://docs.nvidia.com#_CPPv4N49CUpti_PmSampling_CounterData_GetSampleInfo_Params11sampleIndexE) [in] Index of the sample.


-
uint64_t startTimestamp
[#](https://docs.nvidia.com#_CPPv4N49CUpti_PmSampling_CounterData_GetSampleInfo_Params14startTimestampE) [out] Start time of the sample.


-
uint64_t endTimestamp
[#](https://docs.nvidia.com#_CPPv4N49CUpti_PmSampling_CounterData_GetSampleInfo_Params12endTimestampE) [out] End time of the sample.


-
size_t structSize