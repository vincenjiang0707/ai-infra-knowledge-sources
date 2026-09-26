source: https://docs.nvidia.com/cupti/api/structCUpti__PmSampling__DecodeData__Params.html

# 7.157. CUpti_PmSampling_DecodeData_Params[#](https://docs.nvidia.com#cupti-pmsampling-decodedata-params)

-
struct CUpti_PmSampling_DecodeData_Params
[#](https://docs.nvidia.com#_CPPv434CUpti_PmSampling_DecodeData_Params) Params for cuptiPmSamplingDecodeData.

Public Members

-
size_t structSize
[#](https://docs.nvidia.com#_CPPv4N34CUpti_PmSampling_DecodeData_Params10structSizeE) [in] Size of the data structure.


-
void *pPriv
[#](https://docs.nvidia.com#_CPPv4N34CUpti_PmSampling_DecodeData_Params5pPrivE) [in] Set to NULL.


-
[CUpti_PmSampling_Object](https://docs.nvidia.com/group__CUPTI__PM__SAMPLING__API.html#_CPPv423CUpti_PmSampling_Object)*pPmSamplingObject[#](https://docs.nvidia.com#_CPPv4N34CUpti_PmSampling_DecodeData_Params17pPmSamplingObjectE) [in] PM sampling object.


-
uint8_t *pCounterDataImage
[#](https://docs.nvidia.com#_CPPv4N34CUpti_PmSampling_DecodeData_Params17pCounterDataImageE) [in] Counter data image.


-
size_t counterDataImageSize
[#](https://docs.nvidia.com#_CPPv4N34CUpti_PmSampling_DecodeData_Params20counterDataImageSizeE) [in] Size of the counter data image.


-
[CUpti_PmSampling_DecodeStopReason](https://docs.nvidia.com/group__CUPTI__PM__SAMPLING__API.html#_CPPv433CUpti_PmSampling_DecodeStopReason)decodeStopReason[#](https://docs.nvidia.com#_CPPv4N34CUpti_PmSampling_DecodeData_Params16decodeStopReasonE) [out] decode stop reason


-
uint8_t overflow
[#](https://docs.nvidia.com#_CPPv4N34CUpti_PmSampling_DecodeData_Params8overflowE) [out] overflow status for hardware buffer. To avoid overflow, either increase the hardwareBufferSize value in

[CUpti_PmSampling_SetConfig_Params](https://docs.nvidia.com/structCUpti__PmSampling__SetConfig__Params.html#structcupti__pmsampling__setconfig__params)or increase the sampling interval.

-
size_t structSize