source: https://docs.nvidia.com/cupti/api/group__CUPTI__PCSAMPLING__API.html

# 6.5. CUPTI PC Sampling API[#](https://docs.nvidia.com#cupti-pc-sampling-api)

Functions, types, and enums that implement the CUPTI PC Sampling API.

## 6.5.1. Data Structures[#](https://docs.nvidia.com#data-structures)

[CUpti_GetCubinCrcParams](https://docs.nvidia.com/structCUpti__GetCubinCrcParams.html#structcupti__getcubincrcparams)Params for cuptiGetCubinCrc.

[CUpti_GetSassToSourceCorrelationParams](https://docs.nvidia.com/structCUpti__GetSassToSourceCorrelationParams.html#structcupti__getsasstosourcecorrelationparams)Params for cuptiGetSassToSourceCorrelation.

[CUpti_PCSamplingConfigurationInfo](https://docs.nvidia.com/structCUpti__PCSamplingConfigurationInfo.html#structcupti__pcsamplingconfigurationinfo)PC sampling configuration information structure.

[CUpti_PCSamplingConfigurationInfoParams](https://docs.nvidia.com/structCUpti__PCSamplingConfigurationInfoParams.html#structcupti__pcsamplingconfigurationinfoparams)PC sampling configuration structure.

[CUpti_PCSamplingData](https://docs.nvidia.com/structCUpti__PCSamplingData.html#structcupti__pcsamplingdata)Collected PC Sampling data.

[CUpti_PCSamplingDisableParams](https://docs.nvidia.com/structCUpti__PCSamplingDisableParams.html#structcupti__pcsamplingdisableparams)Params for cuptiPCSamplingDisable.

[CUpti_PCSamplingEnableParams](https://docs.nvidia.com/structCUpti__PCSamplingEnableParams.html#structcupti__pcsamplingenableparams)Params for cuptiPCSamplingEnable.

[CUpti_PCSamplingGetDataParams](https://docs.nvidia.com/structCUpti__PCSamplingGetDataParams.html#structcupti__pcsamplinggetdataparams)Params for cuptiPCSamplingEnable.

[CUpti_PCSamplingGetNumStallReasonsParams](https://docs.nvidia.com/structCUpti__PCSamplingGetNumStallReasonsParams.html#structcupti__pcsamplinggetnumstallreasonsparams)Params for cuptiPCSamplingGetNumStallReasons.

[CUpti_PCSamplingGetStallReasonsParams](https://docs.nvidia.com/structCUpti__PCSamplingGetStallReasonsParams.html#structcupti__pcsamplinggetstallreasonsparams)Params for cuptiPCSamplingGetStallReasons.

[CUpti_PCSamplingPCData](https://docs.nvidia.com/structCUpti__PCSamplingPCData.html#structcupti__pcsamplingpcdata)PC Sampling data.

[CUpti_PCSamplingStallReason](https://docs.nvidia.com/structCUpti__PCSamplingStallReason.html#structcupti__pcsamplingstallreason)PC Sampling stall reasons.

[CUpti_PCSamplingStartParams](https://docs.nvidia.com/structCUpti__PCSamplingStartParams.html#structcupti__pcsamplingstartparams)Params for cuptiPCSamplingStart.

[CUpti_PCSamplingStopParams](https://docs.nvidia.com/structCUpti__PCSamplingStopParams.html#structcupti__pcsamplingstopparams)Params for cuptiPCSamplingStop.


## 6.5.2. Macros[#](https://docs.nvidia.com#macros)

[CUPTI_STALL_REASON_STRING_SIZE](https://docs.nvidia.com#group__cupti__pcsampling__api_1ga01e2b11edb4043cd7badb6e9bc633436)[CUpti_GetCubinCrcParamsSize](https://docs.nvidia.com#group__cupti__pcsampling__api_1gaed673536dae9e836d2e0cafcab2fcecf)[CUpti_GetSassToSourceCorrelationParamsSize](https://docs.nvidia.com#group__cupti__pcsampling__api_1gab4d7fd0794cc91e552fa152ec27942c8)[CUpti_PCSamplingConfigurationInfoParamsSize](https://docs.nvidia.com#group__cupti__pcsampling__api_1ga771d0d65f3758f7cdde0d48413d74edc)[CUpti_PCSamplingDisableParamsSize](https://docs.nvidia.com#group__cupti__pcsampling__api_1ga8c71d642ad8e73e8391010df933602f4)[CUpti_PCSamplingEnableParamsSize](https://docs.nvidia.com#group__cupti__pcsampling__api_1gaf07117be5ce240847c071b8c06714205)[CUpti_PCSamplingGetDataParamsSize](https://docs.nvidia.com#group__cupti__pcsampling__api_1ga7e60fb1b540fbf8fed873659b1a73504)[CUpti_PCSamplingGetNumStallReasonsParamsSize](https://docs.nvidia.com#group__cupti__pcsampling__api_1ga0af867c3f1df9c88d5fd5865569ac4bb)[CUpti_PCSamplingGetStallReasonsParamsSize](https://docs.nvidia.com#group__cupti__pcsampling__api_1gaac3a039136534c0ad483d44cc1182530)[CUpti_PCSamplingStartParamsSize](https://docs.nvidia.com#group__cupti__pcsampling__api_1gade38addc00d93826b867b2788de817d7)[CUpti_PCSamplingStopParamsSize](https://docs.nvidia.com#group__cupti__pcsampling__api_1ga0c9ca6508bb651375c4f51d65bf5a684)

## 6.5.3. Enumerations[#](https://docs.nvidia.com#enumerations)

[CUpti_PCSamplingCollectionMode](https://docs.nvidia.com#group__cupti__pcsampling__api_1ga7fcaa834e5520b282b2a3b1de3f304b4)PC Sampling collection mode.

[CUpti_PCSamplingConfigurationAttributeType](https://docs.nvidia.com#group__cupti__pcsampling__api_1ga4fe866bd47d8825f4d46cc52c8e29bb5)PC Sampling configuration attributes.

[CUpti_PCSamplingOutputDataFormat](https://docs.nvidia.com#group__cupti__pcsampling__api_1ga6959d5af9fa0ce5b41af09276fc190f7)PC Sampling output data format.


## 6.5.4. Functions[#](https://docs.nvidia.com#functions)

- CUptiResult
[cuptiGetCubinCrc](https://docs.nvidia.com#group__cupti__pcsampling__api_1ga58d9101ff62121eb735b19167153a4b3)(CUpti_GetCubinCrcParams *pParams) Get the CRC of cubin.

- CUptiResult
[cuptiGetSassToSourceCorrelation](https://docs.nvidia.com#group__cupti__pcsampling__api_1ga35c9023ef22a59235de77b15496814eb)(CUpti_GetSassToSourceCorrelationParams *pParams) SASS to Source correlation.

- CUptiResult
[cuptiPCSamplingDisable](https://docs.nvidia.com#group__cupti__pcsampling__api_1gacbe97deb69ca2795102902544df571e3)(CUpti_PCSamplingDisableParams *pParams) Disable PC sampling.

- CUptiResult
[cuptiPCSamplingEnable](https://docs.nvidia.com#group__cupti__pcsampling__api_1gaf76a8824108dc7517ba80c2e56d46058)(CUpti_PCSamplingEnableParams *pParams) Enable PC sampling.

- CUptiResult
[cuptiPCSamplingGetConfigurationAttribute](https://docs.nvidia.com#group__cupti__pcsampling__api_1gada8f3c53c8673e56a689a67cae7e8df2)(CUpti_PCSamplingConfigurationInfoParams *pParams) Read PC Sampling configuration attribute.

- CUptiResult
[cuptiPCSamplingGetData](https://docs.nvidia.com#group__cupti__pcsampling__api_1ga6a34245ee39a52a31e231845af598e6b)(CUpti_PCSamplingGetDataParams *pParams) Flush GPU PC sampling data periodically.

- CUptiResult
[cuptiPCSamplingGetNumStallReasons](https://docs.nvidia.com#group__cupti__pcsampling__api_1ga5f5393a42625671275d30efaf8e25c3b)(CUpti_PCSamplingGetNumStallReasonsParams *pParams) Get PC sampling stall reason count.

- CUptiResult
[cuptiPCSamplingGetStallReasons](https://docs.nvidia.com#group__cupti__pcsampling__api_1ga74ff0bc692635200205045f6da595b8d)(CUpti_PCSamplingGetStallReasonsParams *pParams) Get PC sampling stall reasons.

- CUptiResult
[cuptiPCSamplingSetConfigurationAttribute](https://docs.nvidia.com#group__cupti__pcsampling__api_1gaf3e8842fda99b4c1659c2d2f1c18674e)(CUpti_PCSamplingConfigurationInfoParams *pParams) Write PC Sampling configuration attribute.

- CUptiResult
[cuptiPCSamplingStart](https://docs.nvidia.com#group__cupti__pcsampling__api_1ga569d99977964b8f7b0f771a153666a6f)(CUpti_PCSamplingStartParams *pParams) Start PC sampling.

- CUptiResult
[cuptiPCSamplingStop](https://docs.nvidia.com#group__cupti__pcsampling__api_1ga942cf8284013fe62b61d5988e6c1052f)(CUpti_PCSamplingStopParams *pParams) Stop PC sampling.

- CUptiResult
[cuptiRegisterComputeCrcCallback](https://docs.nvidia.com#group__cupti__pcsampling__api_1ga675da588e3db103435a3aa360b13c005)(CUpti_ComputeCrcCallbackFunc funcComputeCubinCrc) Register callback function with CUPTI to use your own algorithm to compute cubin crc.


## 6.5.5. Typedefs[#](https://docs.nvidia.com#typedefs)

[CUpti_ComputeCrcCallbackFunc](https://docs.nvidia.com#group__cupti__pcsampling__api_1ga227bc03374c7c672e634c7ca6d6374e5)Function type for callback used by CUPTI to request crc of loaded module.


## 6.5.6. Macros[#](https://docs.nvidia.com#id1)

-
CUPTI_STALL_REASON_STRING_SIZE
[#](https://docs.nvidia.com#c.CUPTI_STALL_REASON_STRING_SIZE)

-
CUpti_GetCubinCrcParamsSize
[#](https://docs.nvidia.com#c.CUpti_GetCubinCrcParamsSize)

-
CUpti_GetSassToSourceCorrelationParamsSize
[#](https://docs.nvidia.com#c.CUpti_GetSassToSourceCorrelationParamsSize)

-
CUpti_PCSamplingConfigurationInfoParamsSize
[#](https://docs.nvidia.com#c.CUpti_PCSamplingConfigurationInfoParamsSize)

-
CUpti_PCSamplingDisableParamsSize
[#](https://docs.nvidia.com#c.CUpti_PCSamplingDisableParamsSize)

-
CUpti_PCSamplingEnableParamsSize
[#](https://docs.nvidia.com#c.CUpti_PCSamplingEnableParamsSize)

-
CUpti_PCSamplingGetDataParamsSize
[#](https://docs.nvidia.com#c.CUpti_PCSamplingGetDataParamsSize)

-
CUpti_PCSamplingGetNumStallReasonsParamsSize
[#](https://docs.nvidia.com#c.CUpti_PCSamplingGetNumStallReasonsParamsSize)

-
CUpti_PCSamplingGetStallReasonsParamsSize
[#](https://docs.nvidia.com#c.CUpti_PCSamplingGetStallReasonsParamsSize)

-
CUpti_PCSamplingStartParamsSize
[#](https://docs.nvidia.com#c.CUpti_PCSamplingStartParamsSize)

-
CUpti_PCSamplingStopParamsSize
[#](https://docs.nvidia.com#c.CUpti_PCSamplingStopParamsSize)

## 6.5.7. Enumerations[#](https://docs.nvidia.com#id2)

-
enum CUpti_PCSamplingCollectionMode
[#](https://docs.nvidia.com#_CPPv430CUpti_PCSamplingCollectionMode) PC Sampling collection mode.

*Values:*-
enumerator CUPTI_PC_SAMPLING_COLLECTION_MODE_INVALID
[#](https://docs.nvidia.com#_CPPv4N30CUpti_PCSamplingCollectionMode41CUPTI_PC_SAMPLING_COLLECTION_MODE_INVALIDE) INVALID Value.


-
enumerator CUPTI_PC_SAMPLING_COLLECTION_MODE_CONTINUOUS
[#](https://docs.nvidia.com#_CPPv4N30CUpti_PCSamplingCollectionMode44CUPTI_PC_SAMPLING_COLLECTION_MODE_CONTINUOUSE) Continuous mode.

Kernels are not serialized in this mode.


-
enumerator CUPTI_PC_SAMPLING_COLLECTION_MODE_KERNEL_SERIALIZED
[#](https://docs.nvidia.com#_CPPv4N30CUpti_PCSamplingCollectionMode51CUPTI_PC_SAMPLING_COLLECTION_MODE_KERNEL_SERIALIZEDE) Serialized mode.

Kernels are serialized in this mode.


-
enumerator CUPTI_PC_SAMPLING_COLLECTION_MODE_INVALID

-
enum CUpti_PCSamplingConfigurationAttributeType
[#](https://docs.nvidia.com#_CPPv442CUpti_PCSamplingConfigurationAttributeType) PC Sampling configuration attributes.

PC Sampling configuration attribute types. These attributes can be read using

[cuptiPCSamplingGetConfigurationAttribute](https://docs.nvidia.com#group__cupti__pcsampling__api_1gada8f3c53c8673e56a689a67cae7e8df2)and can be written using[cuptiPCSamplingSetConfigurationAttribute](https://docs.nvidia.com#group__cupti__pcsampling__api_1gaf3e8842fda99b4c1659c2d2f1c18674e). Attributes marked [r] can only be read using[cuptiPCSamplingGetConfigurationAttribute](https://docs.nvidia.com#group__cupti__pcsampling__api_1gada8f3c53c8673e56a689a67cae7e8df2)[w] can only be written using[cuptiPCSamplingSetConfigurationAttribute](https://docs.nvidia.com#group__cupti__pcsampling__api_1gaf3e8842fda99b4c1659c2d2f1c18674e)[rw] can be read using[cuptiPCSamplingGetConfigurationAttribute](https://docs.nvidia.com#group__cupti__pcsampling__api_1gada8f3c53c8673e56a689a67cae7e8df2)and written using[cuptiPCSamplingSetConfigurationAttribute](https://docs.nvidia.com#group__cupti__pcsampling__api_1gaf3e8842fda99b4c1659c2d2f1c18674e)*Values:*-
enumerator CUPTI_PC_SAMPLING_CONFIGURATION_ATTR_TYPE_INVALID
[#](https://docs.nvidia.com#_CPPv4N42CUpti_PCSamplingConfigurationAttributeType49CUPTI_PC_SAMPLING_CONFIGURATION_ATTR_TYPE_INVALIDE)

-
enumerator CUPTI_PC_SAMPLING_CONFIGURATION_ATTR_TYPE_SAMPLING_PERIOD
[#](https://docs.nvidia.com#_CPPv4N42CUpti_PCSamplingConfigurationAttributeType57CUPTI_PC_SAMPLING_CONFIGURATION_ATTR_TYPE_SAMPLING_PERIODE) [rw] Sampling period for PC Sampling.

DEFAULT - CUPTI defined value based on number of SMs Valid values for the sampling periods are between 5 to 31 both inclusive. This will set the sampling period to (2^samplingPeriod) cycles. For e.g. for sampling period = 5 to 31, cycles = 32, 64, 128,…, 2^31 Value is a uint32_t


-
enumerator CUPTI_PC_SAMPLING_CONFIGURATION_ATTR_TYPE_STALL_REASON
[#](https://docs.nvidia.com#_CPPv4N42CUpti_PCSamplingConfigurationAttributeType54CUPTI_PC_SAMPLING_CONFIGURATION_ATTR_TYPE_STALL_REASONE) [w] Number of stall reasons to collect.

DEFAULT - All stall reasons will be collected Value is a size_t [w] Stall reasons to collect DEFAULT - All stall reasons will be collected Input value should be a pointer pointing to array of stall reason indexes containing all the stall reason indexes to collect.


-
enumerator CUPTI_PC_SAMPLING_CONFIGURATION_ATTR_TYPE_SCRATCH_BUFFER_SIZE
[#](https://docs.nvidia.com#_CPPv4N42CUpti_PCSamplingConfigurationAttributeType61CUPTI_PC_SAMPLING_CONFIGURATION_ATTR_TYPE_SCRATCH_BUFFER_SIZEE) [rw] Size of SW buffer for raw PC counter data downloaded from HW buffer DEFAULT - 1 MB, which can accommodate approximately 5500 PCs with all stall reasons Approximately it takes 16 Bytes (and some fixed size memory) to accommodate one PC with one stall reason For e.g.

1 PC with 1 stall reason = 32 Bytes 1 PC with 2 stall reason = 48 Bytes 1 PC with 4 stall reason = 96 Bytes Value is a size_t


-
enumerator CUPTI_PC_SAMPLING_CONFIGURATION_ATTR_TYPE_HARDWARE_BUFFER_SIZE
[#](https://docs.nvidia.com#_CPPv4N42CUpti_PCSamplingConfigurationAttributeType62CUPTI_PC_SAMPLING_CONFIGURATION_ATTR_TYPE_HARDWARE_BUFFER_SIZEE) [rw] Size of HW buffer in bytes DEFAULT - 512 MB If sampling period is too less, HW buffer can overflow and drop PC data Value is a size_t


-
enumerator CUPTI_PC_SAMPLING_CONFIGURATION_ATTR_TYPE_COLLECTION_MODE
[#](https://docs.nvidia.com#_CPPv4N42CUpti_PCSamplingConfigurationAttributeType57CUPTI_PC_SAMPLING_CONFIGURATION_ATTR_TYPE_COLLECTION_MODEE) [rw] PC Sampling collection mode DEFAULT - CUPTI_PC_SAMPLING_COLLECTION_MODE_CONTINUOUS Input value should be of type

[CUpti_PCSamplingCollectionMode](https://docs.nvidia.com#group__cupti__pcsampling__api_1ga7fcaa834e5520b282b2a3b1de3f304b4).

-
enumerator CUPTI_PC_SAMPLING_CONFIGURATION_ATTR_TYPE_ENABLE_START_STOP_CONTROL
[#](https://docs.nvidia.com#_CPPv4N42CUpti_PCSamplingConfigurationAttributeType67CUPTI_PC_SAMPLING_CONFIGURATION_ATTR_TYPE_ENABLE_START_STOP_CONTROLE) [rw] Control over PC Sampling data collection range Default - 0 1 - Allows user to start and stop PC Sampling using APIs -

[cuptiPCSamplingStart()](https://docs.nvidia.com#group__cupti__pcsampling__api_1ga569d99977964b8f7b0f771a153666a6f)- Start PC Sampling[cuptiPCSamplingStop()](https://docs.nvidia.com#group__cupti__pcsampling__api_1ga942cf8284013fe62b61d5988e6c1052f)- Stop PC Sampling Value is a uint32_t

-
enumerator CUPTI_PC_SAMPLING_CONFIGURATION_ATTR_TYPE_OUTPUT_DATA_FORMAT
[#](https://docs.nvidia.com#_CPPv4N42CUpti_PCSamplingConfigurationAttributeType60CUPTI_PC_SAMPLING_CONFIGURATION_ATTR_TYPE_OUTPUT_DATA_FORMATE) [w] Value for output data format Default - CUPTI_PC_SAMPLING_OUTPUT_DATA_FORMAT_PARSED Input value should be of type

[CUpti_PCSamplingOutputDataFormat](https://docs.nvidia.com#group__cupti__pcsampling__api_1ga6959d5af9fa0ce5b41af09276fc190f7).

-
enumerator CUPTI_PC_SAMPLING_CONFIGURATION_ATTR_TYPE_SAMPLING_DATA_BUFFER
[#](https://docs.nvidia.com#_CPPv4N42CUpti_PCSamplingConfigurationAttributeType62CUPTI_PC_SAMPLING_CONFIGURATION_ATTR_TYPE_SAMPLING_DATA_BUFFERE) [w] Data buffer to hold collected PC Sampling data PARSED_DATA Default - none.

Buffer type is void * which can point to PARSED_DATA Refer

[CUpti_PCSamplingData](https://docs.nvidia.com/structCUpti__PCSamplingData.html#structcupti__pcsamplingdata)for buffer format for PARSED_DATA

-
enumerator CUPTI_PC_SAMPLING_CONFIGURATION_ATTR_TYPE_WORKER_THREAD_PERIODIC_SLEEP_SPAN
[#](https://docs.nvidia.com#_CPPv4N42CUpti_PCSamplingConfigurationAttributeType75CUPTI_PC_SAMPLING_CONFIGURATION_ATTR_TYPE_WORKER_THREAD_PERIODIC_SLEEP_SPANE) [rw] Control sleep time of the worker threads created by CUPTI for various PC sampling operations.

CUPTI creates multiple worker threads to offload certain operations to these threads. This includes decoding of HW data to the CUPTI PC sampling data and correlating PC data to SASS instructions. CUPTI wakes up these threads periodically. Default - 100 milliseconds. Value is a uint32_t


-
enumerator CUPTI_PC_SAMPLING_CONFIGURATION_ATTR_TYPE_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N42CUpti_PCSamplingConfigurationAttributeType51CUPTI_PC_SAMPLING_CONFIGURATION_ATTR_TYPE_FORCE_INTE)

-
enumerator CUPTI_PC_SAMPLING_CONFIGURATION_ATTR_TYPE_INVALID

## 6.5.8. Functions[#](https://docs.nvidia.com#id3)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiGetCubinCrc()[CUpti_GetCubinCrcParams](https://docs.nvidia.com/structCUpti__GetCubinCrcParams.html#_CPPv423CUpti_GetCubinCrcParams)*pParams[#](https://docs.nvidia.com#_CPPv416cuptiGetCubinCrcP23CUpti_GetCubinCrcParams) Get the CRC of cubin.

This function returns the CRC of provided cubin binary.

- Parameters:
**pParams**– A pointer to[CUpti_GetCubinCrcParams](https://docs.nvidia.com/structCUpti__GetCubinCrcParams.html#structcupti__getcubincrcparams)- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if parameter cubin is NULL or provided cubinSize is zero or size field is not set.



-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiGetSassToSourceCorrelation( ,[CUpti_GetSassToSourceCorrelationParams](https://docs.nvidia.com/structCUpti__GetSassToSourceCorrelationParams.html#_CPPv438CUpti_GetSassToSourceCorrelationParams)*pParamsSASS to Source correlation.

It is expected from user to free allocated memory for fileName and dirName after use.

- Parameters:
**pParams**– A pointer to[CUpti_GetSassToSourceCorrelationParams](https://docs.nvidia.com/structCUpti__GetSassToSourceCorrelationParams.html#structcupti__getsasstosourcecorrelationparams)- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if either of the parameters cubin or functionName is NULL or cubinSize is zero or size field is not set correctly.**CUPTI_ERROR_INVALID_MODULE**– provided cubin is invalid.**CUPTI_ERROR_UNKNOWN**– an internal error occurred. This error code is also used for cases when the function is not present in the module. A better error code will be returned in the future release.



[#](https://docs.nvidia.com#_CPPv431cuptiGetSassToSourceCorrelationP38CUpti_GetSassToSourceCorrelationParams)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiPCSamplingDisable( ,[CUpti_PCSamplingDisableParams](https://docs.nvidia.com/structCUpti__PCSamplingDisableParams.html#_CPPv429CUpti_PCSamplingDisableParams)*pParamsDisable PC sampling.

For application which doesn’t destroy the CUDA context explicitly, this API does the PC Sampling tear-down, joins threads and copies PC records in the buffer provided during the PC sampling configuration. PC records which can’t be accommodated in the buffer are discarded.

- Parameters:
**pParams**– A pointer to[CUpti_PCSamplingDisableParams](https://docs.nvidia.com/structCUpti__PCSamplingDisableParams.html#structcupti__pcsamplingdisableparams)- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if any`pParams`

is not valid**CUPTI_ERROR_NOT_SUPPORTED**– indicates that the system/device does not support the API



[#](https://docs.nvidia.com#_CPPv422cuptiPCSamplingDisableP29CUpti_PCSamplingDisableParams)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiPCSamplingEnable( ,[CUpti_PCSamplingEnableParams](https://docs.nvidia.com/structCUpti__PCSamplingEnableParams.html#_CPPv428CUpti_PCSamplingEnableParams)*pParamsEnable PC sampling.

- Parameters:
**pParams**– A pointer to[CUpti_PCSamplingEnableParams](https://docs.nvidia.com/structCUpti__PCSamplingEnableParams.html#structcupti__pcsamplingenableparams)- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if any`pParams`

is not valid**CUPTI_ERROR_NOT_SUPPORTED**– indicates that the system/device does not support the API



[#](https://docs.nvidia.com#_CPPv421cuptiPCSamplingEnableP28CUpti_PCSamplingEnableParams)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiPCSamplingGetConfigurationAttribute( ,[CUpti_PCSamplingConfigurationInfoParams](https://docs.nvidia.com/structCUpti__PCSamplingConfigurationInfoParams.html#_CPPv439CUpti_PCSamplingConfigurationInfoParams)*pParamsRead PC Sampling configuration attribute.

- Parameters:
**pParams**– A pointer to[CUpti_PCSamplingConfigurationInfoParams](https://docs.nvidia.com/structCUpti__PCSamplingConfigurationInfoParams.html#structcupti__pcsamplingconfigurationinfoparams)containing PC sampling configuration.- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_OPERATION**– if this API is called with some invalid attribute.**CUPTI_ERROR_INVALID_PARAMETER**– if`attrib`

is not valid or any`pParams`

is not valid**CUPTI_ERROR_PARAMETER_SIZE_NOT_SUFFICIENT**– indicates that the`value`

buffer is too small to hold the attribute value**CUPTI_ERROR_NOT_SUPPORTED**– indicates that the system/device does not support the API



[#](https://docs.nvidia.com#_CPPv440cuptiPCSamplingGetConfigurationAttributeP39CUpti_PCSamplingConfigurationInfoParams)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiPCSamplingGetData( ,[CUpti_PCSamplingGetDataParams](https://docs.nvidia.com/structCUpti__PCSamplingGetDataParams.html#_CPPv429CUpti_PCSamplingGetDataParams)*pParamsFlush GPU PC sampling data periodically.

Flushing of GPU PC Sampling data is required at following point to maintain uniqueness of PCs: For CUPTI_PC_SAMPLING_COLLECTION_MODE_CONTINUOUS, after every module load-unload-load For CUPTI_PC_SAMPLING_COLLECTION_MODE_KERNEL_SERIALIZED, after every kernel ends If configuration option CUPTI_PC_SAMPLING_CONFIGURATION_ATTR_TYPE_ENABLE_START_STOP_CONTROL is enabled, then after every range end i.e.

[cuptiPCSamplingStop()](https://docs.nvidia.com#group__cupti__pcsampling__api_1ga942cf8284013fe62b61d5988e6c1052f)If application is profiled in CUPTI_PC_SAMPLING_COLLECTION_MODE_CONTINUOUS, with disabled

CUPTI_PC_SAMPLING_CONFIGURATION_ATTR_TYPE_ENABLE_START_STOP_CONTROL, and there is no module unload, user can collect data in two ways: Use

[cuptiPCSamplingGetData()](https://docs.nvidia.com#group__cupti__pcsampling__api_1ga6a34245ee39a52a31e231845af598e6b)API periodically Use[cuptiPCSamplingDisable()](https://docs.nvidia.com#group__cupti__pcsampling__api_1gacbe97deb69ca2795102902544df571e3)on application exit and read GPU PC sampling data from sampling data buffer passed during configuration. Note: In case,[cuptiPCSamplingGetData()](https://docs.nvidia.com#group__cupti__pcsampling__api_1ga6a34245ee39a52a31e231845af598e6b)API is not called periodically, then sampling data buffer passed during configuration should be large enough to hold all PCs data.[cuptiPCSamplingGetData()](https://docs.nvidia.com#group__cupti__pcsampling__api_1ga6a34245ee39a52a31e231845af598e6b)API never does device synchronization. It is possible that when the API is called there is some unconsumed data from the HW buffer. In this case CUPTI provides only the data available with it at that moment.- Parameters:
**pParams**– A pointer to[CUpti_PCSamplingGetDataParams](https://docs.nvidia.com/structCUpti__PCSamplingGetDataParams.html#structcupti__pcsamplinggetdataparams)- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_OPERATION**– if this API is called without enabling PC sampling.**CUPTI_ERROR_INVALID_PARAMETER**– if any`pParams`

is not valid**CUPTI_ERROR_NOT_SUPPORTED**– indicates that the system/device**CUPTI_ERROR_OUT_OF_MEMORY**– indicates that the HW buffer is full does not support the API



[#](https://docs.nvidia.com#_CPPv422cuptiPCSamplingGetDataP29CUpti_PCSamplingGetDataParams)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiPCSamplingGetNumStallReasons( ,[CUpti_PCSamplingGetNumStallReasonsParams](https://docs.nvidia.com/structCUpti__PCSamplingGetNumStallReasonsParams.html#_CPPv440CUpti_PCSamplingGetNumStallReasonsParams)*pParamsGet PC sampling stall reason count.

- Parameters:
**pParams**– A pointer to[CUpti_PCSamplingGetNumStallReasonsParams](https://docs.nvidia.com/structCUpti__PCSamplingGetNumStallReasonsParams.html#structcupti__pcsamplinggetnumstallreasonsparams)- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if any`pParams`

is not valid**CUPTI_ERROR_NOT_SUPPORTED**– indicates that the system/device does not support the API



[#](https://docs.nvidia.com#_CPPv433cuptiPCSamplingGetNumStallReasonsP40CUpti_PCSamplingGetNumStallReasonsParams)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiPCSamplingGetStallReasons( ,[CUpti_PCSamplingGetStallReasonsParams](https://docs.nvidia.com/structCUpti__PCSamplingGetStallReasonsParams.html#_CPPv437CUpti_PCSamplingGetStallReasonsParams)*pParamsGet PC sampling stall reasons.

- Parameters:
**pParams**– A pointer to[CUpti_PCSamplingGetStallReasonsParams](https://docs.nvidia.com/structCUpti__PCSamplingGetStallReasonsParams.html#structcupti__pcsamplinggetstallreasonsparams)- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if any`pParams`

is not valid**CUPTI_ERROR_NOT_SUPPORTED**– indicates that the system/device does not support the API



[#](https://docs.nvidia.com#_CPPv430cuptiPCSamplingGetStallReasonsP37CUpti_PCSamplingGetStallReasonsParams)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiPCSamplingSetConfigurationAttribute( ,[CUpti_PCSamplingConfigurationInfoParams](https://docs.nvidia.com/structCUpti__PCSamplingConfigurationInfoParams.html#_CPPv439CUpti_PCSamplingConfigurationInfoParams)*pParamsWrite PC Sampling configuration attribute.

- Parameters:
**pParams**– A pointer to[CUpti_PCSamplingConfigurationInfoParams](https://docs.nvidia.com/structCUpti__PCSamplingConfigurationInfoParams.html#structcupti__pcsamplingconfigurationinfoparams)containing PC sampling configuration.- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_OPERATION**– if this API is called with some invalid`attrib`

.**CUPTI_ERROR_INVALID_PARAMETER**– if attribute`value`

is not valid or any`pParams`

is not valid**CUPTI_ERROR_NOT_SUPPORTED**– indicates that the system/device does not support the API



[#](https://docs.nvidia.com#_CPPv440cuptiPCSamplingSetConfigurationAttributeP39CUpti_PCSamplingConfigurationInfoParams)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiPCSamplingStart( ,[CUpti_PCSamplingStartParams](https://docs.nvidia.com/structCUpti__PCSamplingStartParams.html#_CPPv427CUpti_PCSamplingStartParams)*pParamsStart PC sampling.

User can collect PC Sampling data for user-defined range specified by Start/Stop APIs. This API can be used to mark starting of range. Set configuration option

CUPTI_PC_SAMPLING_CONFIGURATION_ATTR_TYPE_ENABLE_START_STOP_CONTROL to use this API.

- Parameters:
**pParams**– A pointer to[CUpti_PCSamplingStartParams](https://docs.nvidia.com/structCUpti__PCSamplingStartParams.html#structcupti__pcsamplingstartparams)- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_OPERATION**– if this API is called with incorrect PC Sampling configuration.**CUPTI_ERROR_INVALID_PARAMETER**– if any`pParams`

is not valid**CUPTI_ERROR_NOT_SUPPORTED**– indicates that the system/device does not support the API



[#](https://docs.nvidia.com#_CPPv420cuptiPCSamplingStartP27CUpti_PCSamplingStartParams)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiPCSamplingStop()[CUpti_PCSamplingStopParams](https://docs.nvidia.com/structCUpti__PCSamplingStopParams.html#_CPPv426CUpti_PCSamplingStopParams)*pParams[#](https://docs.nvidia.com#_CPPv419cuptiPCSamplingStopP26CUpti_PCSamplingStopParams) Stop PC sampling.

User can collect PC Sampling data for user-defined range specified by Start/Stop APIs. This API can be used to mark end of range. Set configuration option

CUPTI_PC_SAMPLING_CONFIGURATION_ATTR_TYPE_ENABLE_START_STOP_CONTROL to use this API.

- Parameters:
**pParams**– A pointer to[CUpti_PCSamplingStopParams](https://docs.nvidia.com/structCUpti__PCSamplingStopParams.html#structcupti__pcsamplingstopparams)- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_OPERATION**– if this API is called with incorrect PC Sampling configuration.**CUPTI_ERROR_INVALID_PARAMETER**– if any`pParams`

is not valid**CUPTI_ERROR_NOT_SUPPORTED**– indicates that the system/device does not support the API



-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiRegisterComputeCrcCallback( ,[CUpti_ComputeCrcCallbackFunc](https://docs.nvidia.com#_CPPv428CUpti_ComputeCrcCallbackFunc)funcComputeCubinCrcRegister callback function with CUPTI to use your own algorithm to compute cubin crc.

This function registers a callback function and it gets called from CUPTI when a CUDA module is loaded.

- Parameters:
**funcComputeCubinCrc**– callback is invoked when a CUDA module is loaded.- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if`funcComputeCubinCrc`

is NULL.



[#](https://docs.nvidia.com#_CPPv431cuptiRegisterComputeCrcCallback28CUpti_ComputeCrcCallbackFunc)

## 6.5.9. Typedefs[#](https://docs.nvidia.com#id4)

-
typedef void (*CUpti_ComputeCrcCallbackFunc)(const void *cubin, size_t cubinSize, uint64_t *cubinCrc)
[#](https://docs.nvidia.com#_CPPv428CUpti_ComputeCrcCallbackFunc) Function type for callback used by CUPTI to request crc of loaded module.

This callback function ask for crc of provided module in function. The provided crc will be stored in PC sampling records i.e. in the field ‘cubinCrc’ of the PC sampling struct

[CUpti_PCSamplingPCData](https://docs.nvidia.com/structCUpti__PCSamplingPCData.html#structcupti__pcsamplingpcdata). The CRC is uses during the offline source correlation to uniquely identify the module.- Param cubin:
The pointer to cubin binary

- Param cubinSize:
The size of cubin binary.

- Param cubinCrc:
Returns the computed crc of cubin.