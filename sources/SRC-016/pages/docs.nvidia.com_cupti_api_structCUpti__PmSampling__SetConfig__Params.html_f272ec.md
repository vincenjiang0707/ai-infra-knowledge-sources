source: https://docs.nvidia.com/cupti/api/structCUpti__PmSampling__SetConfig__Params.html

# 7.163. CUpti_PmSampling_SetConfig_Params[#](https://docs.nvidia.com#cupti-pmsampling-setconfig-params)

-
struct CUpti_PmSampling_SetConfig_Params
[#](https://docs.nvidia.com#_CPPv433CUpti_PmSampling_SetConfig_Params) Params for cuptiPmSamplingSetConfig.

Public Members

-
size_t structSize
[#](https://docs.nvidia.com#_CPPv4N33CUpti_PmSampling_SetConfig_Params10structSizeE) [in] Size of the data structure.


-
void *pPriv
[#](https://docs.nvidia.com#_CPPv4N33CUpti_PmSampling_SetConfig_Params5pPrivE) [in] Set to NULL.


-
[CUpti_PmSampling_Object](https://docs.nvidia.com/group__CUPTI__PM__SAMPLING__API.html#_CPPv423CUpti_PmSampling_Object)*pPmSamplingObject[#](https://docs.nvidia.com#_CPPv4N33CUpti_PmSampling_SetConfig_Params17pPmSamplingObjectE) [in] PM sampling object.


-
size_t configSize
[#](https://docs.nvidia.com#_CPPv4N33CUpti_PmSampling_SetConfig_Params10configSizeE) [in] Size of the config image.


-
const uint8_t *pConfig
[#](https://docs.nvidia.com#_CPPv4N33CUpti_PmSampling_SetConfig_Params7pConfigE) [in] Config image.


-
size_t hardwareBufferSize
[#](https://docs.nvidia.com#_CPPv4N33CUpti_PmSampling_SetConfig_Params18hardwareBufferSizeE) [in] The hardware buffer size in which raw PM sampling data will be stored. These samples will be decoded to counter data image with

[cuptiPmSamplingDecodeData](https://docs.nvidia.com/group__CUPTI__PM__SAMPLING__API.html#group__cupti__pm__sampling__api_1ga1e0f1d1e28911b48feca1013ce7e8b2f)call.

-
uint64_t samplingInterval
[#](https://docs.nvidia.com#_CPPv4N33CUpti_PmSampling_SetConfig_Params16samplingIntervalE) [in] For the trigger mode

`CUPTI_PM_SAMPLING_TRIGGER_MODE_GPU_SYSCLK_INTERVAL`

, sampling interval is the number of sys clock cycles. For the trigger mode`CUPTI_PM_SAMPLING_TRIGGER_MODE_GPU_TIME_INTERVAL`

, sampling interval is in nanoseconds.

-
[CUpti_PmSampling_TriggerMode](https://docs.nvidia.com/group__CUPTI__PM__SAMPLING__API.html#_CPPv428CUpti_PmSampling_TriggerMode)triggerMode[#](https://docs.nvidia.com#_CPPv4N33CUpti_PmSampling_SetConfig_Params11triggerModeE) [in] Trigger mode. Note: CUPTI_PM_SAMPLING_TRIGGER_MODE_GPU_TIME_INTERVAL is not supported in Turing and GA100. Supported from GA10x onwards.


-
[CUpti_PmSampling_HardwareBuffer_AppendMode](https://docs.nvidia.com/group__CUPTI__PM__SAMPLING__API.html#_CPPv442CUpti_PmSampling_HardwareBuffer_AppendMode)hwBufferAppendMode[#](https://docs.nvidia.com#_CPPv4N33CUpti_PmSampling_SetConfig_Params18hwBufferAppendModeE) [in] Append mode for the records in hardware buffer. For KEEP_OLDEST mode, all the records will be kept in the buffer and in case hardware buffer is getting filled up. overflow will be set to 1 in

[CUpti_PmSampling_DecodeData_Params](https://docs.nvidia.com/structCUpti__PmSampling__DecodeData__Params.html#structcupti__pmsampling__decodedata__params). For KEEP_LATEST mode, the new records will overwrite the oldest records in the buffer in case of filled buffer.

-
size_t structSize