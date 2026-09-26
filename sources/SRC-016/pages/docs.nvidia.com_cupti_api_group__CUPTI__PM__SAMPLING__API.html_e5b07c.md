source: https://docs.nvidia.com/cupti/api/group__CUPTI__PM__SAMPLING__API.html

# 6.7. CUPTI PM Sampling API[#](https://docs.nvidia.com#cupti-pm-sampling-api)

Functions to enable, disable, start, stop, and decode PM sampling.

## 6.7.1. Data Structures[#](https://docs.nvidia.com#data-structures)

[CUpti_PmSampling_CounterDataImage_Initialize_Params](https://docs.nvidia.com/structCUpti__PmSampling__CounterDataImage__Initialize__Params.html#structcupti__pmsampling__counterdataimage__initialize__params)Params for cuptiPmSamplingCounterDataImageInitialize.

[CUpti_PmSampling_CounterData_GetSampleInfo_Params](https://docs.nvidia.com/structCUpti__PmSampling__CounterData__GetSampleInfo__Params.html#structcupti__pmsampling__counterdata__getsampleinfo__params)Params for cuptiPmSamplingCounterDataGetSampleInfo.

[CUpti_PmSampling_DecodeData_Params](https://docs.nvidia.com/structCUpti__PmSampling__DecodeData__Params.html#structcupti__pmsampling__decodedata__params)Params for cuptiPmSamplingDecodeData.

[CUpti_PmSampling_Disable_Params](https://docs.nvidia.com/structCUpti__PmSampling__Disable__Params.html#structcupti__pmsampling__disable__params)Params for cuptiPmSamplingDisable.

[CUpti_PmSampling_Enable_Params](https://docs.nvidia.com/structCUpti__PmSampling__Enable__Params.html#structcupti__pmsampling__enable__params)Params for cuptiPmSamplingEnable.

[CUpti_PmSampling_GetCounterAvailability_Params](https://docs.nvidia.com/structCUpti__PmSampling__GetCounterAvailability__Params.html#structcupti__pmsampling__getcounteravailability__params)Params for cuptiPmSamplingGetCounterData.

[CUpti_PmSampling_GetCounterDataInfo_Params](https://docs.nvidia.com/structCUpti__PmSampling__GetCounterDataInfo__Params.html#structcupti__pmsampling__getcounterdatainfo__params)Params for cuptiPmSamplingGetCounterDataInfo.

[CUpti_PmSampling_GetCounterDataSize_Params](https://docs.nvidia.com/structCUpti__PmSampling__GetCounterDataSize__Params.html#structcupti__pmsampling__getcounterdatasize__params)Params for cuptiPmSamplingGetCounterDataSize.

[CUpti_PmSampling_SetConfig_Params](https://docs.nvidia.com/structCUpti__PmSampling__SetConfig__Params.html#structcupti__pmsampling__setconfig__params)Params for cuptiPmSamplingSetConfig.

[CUpti_PmSampling_Start_Params](https://docs.nvidia.com/structCUpti__PmSampling__Start__Params.html#structcupti__pmsampling__start__params)Params for cuptiPmSamplingStart.

[CUpti_PmSampling_Stop_Params](https://docs.nvidia.com/structCUpti__PmSampling__Stop__Params.html#structcupti__pmsampling__stop__params)Params for cuptiPmSamplingStop.


## 6.7.2. Macros[#](https://docs.nvidia.com#macros)

[CUpti_PmSampling_CounterDataImage_Initialize_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__pm__sampling__api_1gad11d2b9dfa11fcd94a90cdfb3ec8fc5a)[CUpti_PmSampling_CounterData_GetSampleInfo_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__pm__sampling__api_1ga123eaa0d2d3cd10e383cf92559ab3137)[CUpti_PmSampling_DecodeData_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__pm__sampling__api_1ga6d5e44c84d76bab17f286c1de2bfb4c0)[CUpti_PmSampling_Disable_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__pm__sampling__api_1ga096908b1c57b19bfd4dabaa04a12d780)[CUpti_PmSampling_Enable_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__pm__sampling__api_1gaaf7fec97616a34fa846022079d1886f9)[CUpti_PmSampling_GetCounterAvailability_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__pm__sampling__api_1gae9addd087ae488faedba340ff0c136a1)[CUpti_PmSampling_GetCounterDataInfo_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__pm__sampling__api_1ga2bc56051d14807db5c0f48d02e005acf)[CUpti_PmSampling_GetCounterDataSize_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__pm__sampling__api_1gab01b3bc2d06e5bc8fa70a427a32c7157)[CUpti_PmSampling_SetConfig_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__pm__sampling__api_1gafba9c7156922bb8a725038a14219b1b2)[CUpti_PmSampling_Start_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__pm__sampling__api_1ga297aae8430bf60191e7c1eefa560272c)[CUpti_PmSampling_Stop_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__pm__sampling__api_1ga1193b3c5b93d002ba75d5d46cdf9e490)

## 6.7.3. Enumerations[#](https://docs.nvidia.com#enumerations)

## 6.7.4. Functions[#](https://docs.nvidia.com#functions)

- CUptiResult
[cuptiPmSamplingCounterDataGetSampleInfo](https://docs.nvidia.com#group__cupti__pm__sampling__api_1ga3c38a9c0143e8bfc8e2ee095ecc3fc17)(CUpti_PmSampling_CounterData_GetSampleInfo_Params *pParams) Get the sample info (start and end time stamp) for the given sample index.

- CUptiResult
[cuptiPmSamplingCounterDataImageInitialize](https://docs.nvidia.com#group__cupti__pm__sampling__api_1ga1040c72a2d49cc84d4ed50e881321162)(CUpti_PmSampling_CounterDataImage_Initialize_Params *pParams) Initialize the counter data to CUPTI record format for storing the metric data.

- CUptiResult
[cuptiPmSamplingDecodeData](https://docs.nvidia.com#group__cupti__pm__sampling__api_1ga1e0f1d1e28911b48feca1013ce7e8b2f)(CUpti_PmSampling_DecodeData_Params *pParams) Decode the metrics data stored in the hardware buffer to the counter data image.

- CUptiResult
[cuptiPmSamplingDisable](https://docs.nvidia.com#group__cupti__pm__sampling__api_1gac1ac579527ecb597b0bc93c94afea46b)(CUpti_PmSampling_Disable_Params *pParams) Disable PM sampling on the CUDA device and destroy the PM sampling object.

- CUptiResult
[cuptiPmSamplingEnable](https://docs.nvidia.com#group__cupti__pm__sampling__api_1ga45cbdf31b186142549243cb527d75bd1)(CUpti_PmSampling_Enable_Params *pParams) Create a PM sampling object and enable PM sampling on the CUDA device.

- CUptiResult
[cuptiPmSamplingGetCounterAvailability](https://docs.nvidia.com#group__cupti__pm__sampling__api_1gaedd567fb5a0c2ad11c8b22ec43d78928)(CUpti_PmSampling_GetCounterAvailability_Params *pParams) Query counter availibility information in a buffer which can be used to filter unavailable raw metrics on host.

- CUptiResult
[cuptiPmSamplingGetCounterDataInfo](https://docs.nvidia.com#group__cupti__pm__sampling__api_1ga89b6ff5cc9570cb7059271d13e474aba)(CUpti_PmSampling_GetCounterDataInfo_Params *pParams) Get the counter data info like number of samples, number of populated samples and number of completed samples in a counter data image.

- CUptiResult
[cuptiPmSamplingGetCounterDataSize](https://docs.nvidia.com#group__cupti__pm__sampling__api_1ga4009c1c98fc72c30c4c0be60eb98f23f)(CUpti_PmSampling_GetCounterDataSize_Params *pParams) Query the size of the counter data image which will be used to store the metrics data.

- CUptiResult
[cuptiPmSamplingSetConfig](https://docs.nvidia.com#group__cupti__pm__sampling__api_1gabf81ed3dcee860a444e8e2e1e2e92e1b)(CUpti_PmSampling_SetConfig_Params *pParams) Set the configuration for PM sampling like sampling interval, HW buffer size, trigger mode and the config image which has scheduling info for metric collection.

- CUptiResult
[cuptiPmSamplingStart](https://docs.nvidia.com#group__cupti__pm__sampling__api_1gaffbd0feb903fc251064a4d5e0a1a567e)(CUpti_PmSampling_Start_Params *pParams) Start the PM sampling.

- CUptiResult
[cuptiPmSamplingStop](https://docs.nvidia.com#group__cupti__pm__sampling__api_1ga553c2d78d8fb6658cb6c667d2308be30)(CUpti_PmSampling_Stop_Params *pParams) Stop the PM sampling.


## 6.7.5. Typedefs[#](https://docs.nvidia.com#typedefs)

## 6.7.6. Macros[#](https://docs.nvidia.com#id1)

-
CUpti_PmSampling_CounterDataImage_Initialize_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_PmSampling_CounterDataImage_Initialize_Params_STRUCT_SIZE)

-
CUpti_PmSampling_CounterData_GetSampleInfo_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_PmSampling_CounterData_GetSampleInfo_Params_STRUCT_SIZE)

-
CUpti_PmSampling_DecodeData_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_PmSampling_DecodeData_Params_STRUCT_SIZE)

-
CUpti_PmSampling_Disable_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_PmSampling_Disable_Params_STRUCT_SIZE)

-
CUpti_PmSampling_Enable_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_PmSampling_Enable_Params_STRUCT_SIZE)

-
CUpti_PmSampling_GetCounterAvailability_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_PmSampling_GetCounterAvailability_Params_STRUCT_SIZE)

-
CUpti_PmSampling_GetCounterDataInfo_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_PmSampling_GetCounterDataInfo_Params_STRUCT_SIZE)

-
CUpti_PmSampling_GetCounterDataSize_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_PmSampling_GetCounterDataSize_Params_STRUCT_SIZE)

-
CUpti_PmSampling_SetConfig_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_PmSampling_SetConfig_Params_STRUCT_SIZE)

-
CUpti_PmSampling_Start_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_PmSampling_Start_Params_STRUCT_SIZE)

-
CUpti_PmSampling_Stop_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_PmSampling_Stop_Params_STRUCT_SIZE)

## 6.7.7. Enumerations[#](https://docs.nvidia.com#id2)

-
enum CUpti_PmSampling_DecodeStopReason
[#](https://docs.nvidia.com#_CPPv433CUpti_PmSampling_DecodeStopReason) *Values:*-
enumerator CUPTI_PM_SAMPLING_DECODE_STOP_REASON_OTHER
[#](https://docs.nvidia.com#_CPPv4N33CUpti_PmSampling_DecodeStopReason42CUPTI_PM_SAMPLING_DECODE_STOP_REASON_OTHERE)

-
enumerator CUPTI_PM_SAMPLING_DECODE_STOP_REASON_COUNTER_DATA_FULL
[#](https://docs.nvidia.com#_CPPv4N33CUpti_PmSampling_DecodeStopReason54CUPTI_PM_SAMPLING_DECODE_STOP_REASON_COUNTER_DATA_FULLE) Counter data image is full.


-
enumerator CUPTI_PM_SAMPLING_DECODE_STOP_REASON_END_OF_RECORDS
[#](https://docs.nvidia.com#_CPPv4N33CUpti_PmSampling_DecodeStopReason51CUPTI_PM_SAMPLING_DECODE_STOP_REASON_END_OF_RECORDSE) All the records in the hardware buffer is decoded.


-
enumerator CUPTI_PM_SAMPLING_DECODE_STOP_REASON_COUNT
[#](https://docs.nvidia.com#_CPPv4N33CUpti_PmSampling_DecodeStopReason42CUPTI_PM_SAMPLING_DECODE_STOP_REASON_COUNTE)

-
enumerator CUPTI_PM_SAMPLING_DECODE_STOP_REASON_OTHER

-
enum CUpti_PmSampling_HardwareBuffer_AppendMode
[#](https://docs.nvidia.com#_CPPv442CUpti_PmSampling_HardwareBuffer_AppendMode) *Values:*-
enumerator CUPTI_PM_SAMPLING_HARDWARE_BUFFER_APPEND_MODE_KEEP_OLDEST
[#](https://docs.nvidia.com#_CPPv4N42CUpti_PmSampling_HardwareBuffer_AppendMode57CUPTI_PM_SAMPLING_HARDWARE_BUFFER_APPEND_MODE_KEEP_OLDESTE) Keep the oldest records in the hardware buffer. CUPTI will report error for overflow in case hardware buffer is getting filled up.


-
enumerator CUPTI_PM_SAMPLING_HARDWARE_BUFFER_APPEND_MODE_KEEP_LATEST
[#](https://docs.nvidia.com#_CPPv4N42CUpti_PmSampling_HardwareBuffer_AppendMode57CUPTI_PM_SAMPLING_HARDWARE_BUFFER_APPEND_MODE_KEEP_LATESTE) Keep the latest records in the hardware buffer. Note: This mode is not supported on Turing GPU architecture. It is supported on Ampere and later GPU architectures.


-
enumerator CUPTI_PM_SAMPLING_HARDWARE_BUFFER_APPEND_MODE_KEEP_OLDEST

-
enum CUpti_PmSampling_TriggerMode
[#](https://docs.nvidia.com#_CPPv428CUpti_PmSampling_TriggerMode) *Values:*-
enumerator CUPTI_PM_SAMPLING_TRIGGER_MODE_GPU_SYSCLK_INTERVAL
[#](https://docs.nvidia.com#_CPPv4N28CUpti_PmSampling_TriggerMode50CUPTI_PM_SAMPLING_TRIGGER_MODE_GPU_SYSCLK_INTERVALE) The trigger is based off of the SYSCLK frequency, note SYS frequency by default is variable. the sample interval (set in the struct

[CUpti_PmSampling_SetConfig_Params](https://docs.nvidia.com/structCUpti__PmSampling__SetConfig__Params.html#structcupti__pmsampling__setconfig__params)) is in terms of clocks.

-
enumerator CUPTI_PM_SAMPLING_TRIGGER_MODE_GPU_TIME_INTERVAL
[#](https://docs.nvidia.com#_CPPv4N28CUpti_PmSampling_TriggerMode48CUPTI_PM_SAMPLING_TRIGGER_MODE_GPU_TIME_INTERVALE) The trigger is based off of a fixed frequency source. The sample interval (set in the struct

[CUpti_PmSampling_SetConfig_Params](https://docs.nvidia.com/structCUpti__PmSampling__SetConfig__Params.html#structcupti__pmsampling__setconfig__params)) is in terms of nanoseconds. Note: This trigger mode is not supported on Turing GPU architecture and GA100 GPU. It is supported on Ampere GA10x and later GPU architectures.

-
enumerator CUPTI_PM_SAMPLING_TRIGGER_MODE_COUNT
[#](https://docs.nvidia.com#_CPPv4N28CUpti_PmSampling_TriggerMode36CUPTI_PM_SAMPLING_TRIGGER_MODE_COUNTE)

-
enumerator CUPTI_PM_SAMPLING_TRIGGER_MODE_GPU_SYSCLK_INTERVAL

## 6.7.8. Functions[#](https://docs.nvidia.com#id3)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiPmSamplingCounterDataGetSampleInfo(
) Get the sample info (start and end time stamp) for the given sample index.

Each sample is distinguished by the start and end time stamp.

- Parameters:
**pParams**– A pointer to[CUpti_PmSampling_CounterData_GetSampleInfo_Params](https://docs.nvidia.com/structCUpti__PmSampling__CounterData__GetSampleInfo__Params.html#structcupti__pmsampling__counterdata__getsampleinfo__params)- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if any`pParams`

is not valid**CUPTI_ERROR_UNKNOWN**– for any internal error



[#](https://docs.nvidia.com#_CPPv439cuptiPmSamplingCounterDataGetSampleInfoP49CUpti_PmSampling_CounterData_GetSampleInfo_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiPmSamplingCounterDataImageInitialize(
) Initialize the counter data to CUPTI record format for storing the metric data.

- Parameters:
**pParams**– A pointer to[CUpti_PmSampling_CounterDataImage_Initialize_Params](https://docs.nvidia.com/structCUpti__PmSampling__CounterDataImage__Initialize__Params.html#structcupti__pmsampling__counterdataimage__initialize__params)- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if any`pParams`

is not valid**CUPTI_ERROR_INVALID_OPERATION**– if PM sampling CounterDataInitialize is called without enabling PM sampling**CUPTI_ERROR_UNKNOWN**– for any internal error



[#](https://docs.nvidia.com#_CPPv441cuptiPmSamplingCounterDataImageInitializeP51CUpti_PmSampling_CounterDataImage_Initialize_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiPmSamplingDecodeData( ,[CUpti_PmSampling_DecodeData_Params](https://docs.nvidia.com/structCUpti__PmSampling__DecodeData__Params.html#_CPPv434CUpti_PmSampling_DecodeData_Params)*pParamsDecode the metrics data stored in the hardware buffer to the counter data image.

- Parameters:
**pParams**– A pointer to[CUpti_PmSampling_DecodeData_Params](https://docs.nvidia.com/structCUpti__PmSampling__DecodeData__Params.html#structcupti__pmsampling__decodedata__params)- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if any`pParams`

is not valid**CUPTI_ERROR_INVALID_OPERATION**– if PM sampling DecodeData is called without enabling PM sampling**CUPTI_ERROR_OUT_OF_MEMORY**– if there is record overflow in the hardware buffer**CUPTI_ERROR_UNKNOWN**– for any internal error



[#](https://docs.nvidia.com#_CPPv425cuptiPmSamplingDecodeDataP34CUpti_PmSampling_DecodeData_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiPmSamplingDisable( ,[CUpti_PmSampling_Disable_Params](https://docs.nvidia.com/structCUpti__PmSampling__Disable__Params.html#_CPPv431CUpti_PmSampling_Disable_Params)*pParamsDisable PM sampling on the CUDA device and destroy the PM sampling object.

- Parameters:
**pParams**– A pointer to[CUpti_PmSampling_Disable_Params](https://docs.nvidia.com/structCUpti__PmSampling__Disable__Params.html#structcupti__pmsampling__disable__params)- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if any`pParams`

is not valid**CUPTI_ERROR_UNKNOWN**– for any internal error



[#](https://docs.nvidia.com#_CPPv422cuptiPmSamplingDisableP31CUpti_PmSampling_Disable_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiPmSamplingEnable( ,[CUpti_PmSampling_Enable_Params](https://docs.nvidia.com/structCUpti__PmSampling__Enable__Params.html#_CPPv430CUpti_PmSampling_Enable_Params)*pParamsCreate a PM sampling object and enable PM sampling on the CUDA device.

- Parameters:
**pParams**– A pointer to[CUpti_PmSampling_Enable_Params](https://docs.nvidia.com/structCUpti__PmSampling__Enable__Params.html#structcupti__pmsampling__enable__params)- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if any`pParams`

is not valid**CUPTI_ERROR_OUT_OF_MEMORY**– if memory allocation fails while creating the PM sampling object**CUPTI_ERROR_INVALID_OPERATION**– if PM sampling is already enabled on the device**CUPTI_ERROR_INSUFFICIENT_PRIVILEGES**– if the user does not have sufficient privileges to perform the operation**CUPTI_ERROR_UNKNOWN**– for any internal error



[#](https://docs.nvidia.com#_CPPv421cuptiPmSamplingEnableP30CUpti_PmSampling_Enable_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiPmSamplingGetCounterAvailability(
) Query counter availibility information in a buffer which can be used to filter unavailable raw metrics on host.

Note: This API may fail, if any profiling or sampling session is active on the specified device.

- Parameters:
**pParams**– A pointer to[CUpti_PmSampling_GetCounterAvailability_Params](https://docs.nvidia.com/structCUpti__PmSampling__GetCounterAvailability__Params.html#structcupti__pmsampling__getcounteravailability__params)- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if any`pParams`

is not valid**CUPTI_ERROR_INSUFFICIENT_PRIVILEGES**– if the user does not have sufficient privileges to perform the operation**CUPTI_ERROR_UNKNOWN**– for any internal error



[#](https://docs.nvidia.com#_CPPv437cuptiPmSamplingGetCounterAvailabilityP46CUpti_PmSampling_GetCounterAvailability_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiPmSamplingGetCounterDataInfo(
) Get the counter data info like number of samples, number of populated samples and number of completed samples in a counter data image.

- Parameters:
**pParams**– A pointer to[CUpti_PmSampling_GetCounterDataInfo_Params](https://docs.nvidia.com/structCUpti__PmSampling__GetCounterDataInfo__Params.html#structcupti__pmsampling__getcounterdatainfo__params)- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if any`pParams`

is not valid**CUPTI_ERROR_UNKNOWN**– for any internal error



[#](https://docs.nvidia.com#_CPPv433cuptiPmSamplingGetCounterDataInfoP42CUpti_PmSampling_GetCounterDataInfo_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiPmSamplingGetCounterDataSize(
) Query the size of the counter data image which will be used to store the metrics data.

User need to allocate the memory for the counter data image based on the size returned by this API.

- Parameters:
**pParams**– A pointer to[CUpti_PmSampling_GetCounterDataSize_Params](https://docs.nvidia.com/structCUpti__PmSampling__GetCounterDataSize__Params.html#structcupti__pmsampling__getcounterdatasize__params)- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if any`pParams`

is not valid**CUPTI_ERROR_INVALID_OPERATION**– if PM sampling GetCounterDataSize is called without enabling PM sampling**CUPTI_ERROR_UNKNOWN**– for any internal error



[#](https://docs.nvidia.com#_CPPv433cuptiPmSamplingGetCounterDataSizeP42CUpti_PmSampling_GetCounterDataSize_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiPmSamplingSetConfig( ,[CUpti_PmSampling_SetConfig_Params](https://docs.nvidia.com/structCUpti__PmSampling__SetConfig__Params.html#_CPPv433CUpti_PmSampling_SetConfig_Params)*pParamsSet the configuration for PM sampling like sampling interval, HW buffer size, trigger mode and the config image which has scheduling info for metric collection.

- Parameters:
**pParams**– A pointer to[CUpti_PmSampling_SetConfig_Params](https://docs.nvidia.com/structCUpti__PmSampling__SetConfig__Params.html#structcupti__pmsampling__setconfig__params)- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if any`pParams`

is not valid**CUPTI_ERROR_NOT_SUPPORTED**– for config image which require multiple passes for data collection



[#](https://docs.nvidia.com#_CPPv424cuptiPmSamplingSetConfigP33CUpti_PmSampling_SetConfig_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiPmSamplingStart( ,[CUpti_PmSampling_Start_Params](https://docs.nvidia.com/structCUpti__PmSampling__Start__Params.html#_CPPv429CUpti_PmSampling_Start_Params)*pParamsStart the PM sampling.

The GPU will start collecting the metrics data periodically based on trigger type and sampling interval passed in

[CUpti_PmSampling_SetConfig_Params](https://docs.nvidia.com/structCUpti__PmSampling__SetConfig__Params.html#structcupti__pmsampling__setconfig__params). The collected data will be stored in the hardware buffer.- Parameters:
**pParams**– A pointer to[CUpti_PmSampling_Start_Params](https://docs.nvidia.com/structCUpti__PmSampling__Start__Params.html#structcupti__pmsampling__start__params)- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if any`pParams`

is not valid**CUPTI_ERROR_INVALID_OPERATION**– if PM sampling Start is called without enabling PM sampling, and PM sampling is already started**CUPTI_ERROR_UNKNOWN**– for any internal error



[#](https://docs.nvidia.com#_CPPv420cuptiPmSamplingStartP29CUpti_PmSampling_Start_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiPmSamplingStop( ,[CUpti_PmSampling_Stop_Params](https://docs.nvidia.com/structCUpti__PmSampling__Stop__Params.html#_CPPv428CUpti_PmSampling_Stop_Params)*pParamsStop the PM sampling.

The GPU will stop collecting the metrics data.

- Parameters:
**pParams**– A pointer to[CUpti_PmSampling_Stop_Params](https://docs.nvidia.com/structCUpti__PmSampling__Stop__Params.html#structcupti__pmsampling__stop__params)- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if any`pParams`

is not valid**CUPTI_ERROR_INVALID_OPERATION**– if PM sampling Stop is called without enabling PM sampling, and PM sampling is already stopped**CUPTI_ERROR_UNKNOWN**– for any internal error



[#](https://docs.nvidia.com#_CPPv419cuptiPmSamplingStopP28CUpti_PmSampling_Stop_Params)

## 6.7.9. Typedefs[#](https://docs.nvidia.com#id4)

-
typedef struct
[CUpti_PmSampling_Object](https://docs.nvidia.com#_CPPv423CUpti_PmSampling_Object)CUpti_PmSampling_Object[#](https://docs.nvidia.com#_CPPv423CUpti_PmSampling_Object)