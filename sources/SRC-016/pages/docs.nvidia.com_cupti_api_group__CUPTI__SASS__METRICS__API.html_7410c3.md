source: https://docs.nvidia.com/cupti/api/group__CUPTI__SASS__METRICS__API.html

# 6.12. CUPTI SASS Metrics API[#](https://docs.nvidia.com#cupti-sass-metrics-api)

Functions, types, and enums that implement the CUPTI SASS Metrics API.

## 6.12.1. Data Structures[#](https://docs.nvidia.com#data-structures)

[CUpti_SassMetricsDisable_Params](https://docs.nvidia.com/structCUpti__SassMetricsDisable__Params.html#structcupti__sassmetricsdisable__params)Params for cuptiSassMetricsDisable.

[CUpti_SassMetricsEnable_Params](https://docs.nvidia.com/structCUpti__SassMetricsEnable__Params.html#structcupti__sassmetricsenable__params)Params for cuptiSassMetricsEnable.

[CUpti_SassMetricsFlushData_Params](https://docs.nvidia.com/structCUpti__SassMetricsFlushData__Params.html#structcupti__sassmetricsflushdata__params)Params for cuptiSassMetricsFlushData.

[CUpti_SassMetricsGetDataProperties_Params](https://docs.nvidia.com/structCUpti__SassMetricsGetDataProperties__Params.html#structcupti__sassmetricsgetdataproperties__params)Params for cuptiSassMetricsGetDataProperties.

[CUpti_SassMetricsSetConfig_Params](https://docs.nvidia.com/structCUpti__SassMetricsSetConfig__Params.html#structcupti__sassmetricssetconfig__params)Params for cuptiSassMetricsSetConfig.

[CUpti_SassMetricsUnsetConfig_Params](https://docs.nvidia.com/structCUpti__SassMetricsUnsetConfig__Params.html#structcupti__sassmetricsunsetconfig__params)Params for cuptiSassMetricsUnsetConfig.

[CUpti_SassMetrics_Config](https://docs.nvidia.com/structCUpti__SassMetrics__Config.html#structcupti__sassmetrics__config)[CUpti_SassMetrics_Data](https://docs.nvidia.com/structCUpti__SassMetrics__Data.html#structcupti__sassmetrics__data)[CUpti_SassMetrics_GetMetrics_Params](https://docs.nvidia.com/structCUpti__SassMetrics__GetMetrics__Params.html#structcupti__sassmetrics__getmetrics__params)Params for cuptiSassMetricsGetMetrics.

[CUpti_SassMetrics_GetNumOfMetrics_Params](https://docs.nvidia.com/structCUpti__SassMetrics__GetNumOfMetrics__Params.html#structcupti__sassmetrics__getnumofmetrics__params)Params for cuptiSassMetricsGetNumOfMetrics.

[CUpti_SassMetrics_GetProperties_Params](https://docs.nvidia.com/structCUpti__SassMetrics__GetProperties__Params.html#structcupti__sassmetrics__getproperties__params)Params for cuptiSassMetricsGetProperties.

[CUpti_SassMetrics_InstanceValue](https://docs.nvidia.com/structCUpti__SassMetrics__InstanceValue.html#structcupti__sassmetrics__instancevalue)[CUpti_SassMetrics_MetricDetails](https://docs.nvidia.com/structCUpti__SassMetrics__MetricDetails.html#structcupti__sassmetrics__metricdetails)

## 6.12.2. Macros[#](https://docs.nvidia.com#macros)

[CUpti_SassMetricsDisable_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__sass__metrics__api_1gab431fb57bd1c85a13f126797d78ee3f8)[CUpti_SassMetricsEnable_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__sass__metrics__api_1gaa61089a37e7b9b36589a04f22f21285e)[CUpti_SassMetricsFlushData_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__sass__metrics__api_1ga093a80d978971b5297910971b4c16d73)[CUpti_SassMetricsGetDataProperties_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__sass__metrics__api_1ga2a5d48ee930b99df2baad153c247101b)[CUpti_SassMetricsSetConfig_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__sass__metrics__api_1gaf4abade746722e2bb09f29c7010f1af3)[CUpti_SassMetricsUnsetConfig_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__sass__metrics__api_1gaf23c4a704d07179f861729c330092cd9)[CUpti_SassMetrics_GetMetrics_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__sass__metrics__api_1ga4e9099dc471765098f15babb8720d1de)[CUpti_SassMetrics_GetNumOfMetrics_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__sass__metrics__api_1ga89b98cf940aacb9e8fc3563eba4efa12)[CUpti_SassMetrics_GetProperties_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__sass__metrics__api_1ga4b9139a820a7905b5ded353ba1e83114)[CUpti_SassMetrics_InstanceValue_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__sass__metrics__api_1ga6107c8e716fc8e0fa42e4a415e841933)

## 6.12.3. Enumerations[#](https://docs.nvidia.com#enumerations)

## 6.12.4. Functions[#](https://docs.nvidia.com#functions)

- CUptiResult
[cuptiSassMetricsDisable](https://docs.nvidia.com#group__cupti__sass__metrics__api_1gadf8447d381211251c69cdaf3221a5fec)(CUpti_SassMetricsDisable_Params *pParams) SASS metric data collection disable API will mark the end of a range, any kernel launched after this API call will not be profiled for the SASS metrics.

- CUptiResult
[cuptiSassMetricsEnable](https://docs.nvidia.com#group__cupti__sass__metrics__api_1ga62ea0db81c966ddf066c28644f8b240f)(CUpti_SassMetricsEnable_Params *pParams) Sass metric data collection enable API will mark the start of a range, between which kernel will be profiled for SASS metrics.

- CUptiResult
[cuptiSassMetricsFlushData](https://docs.nvidia.com#group__cupti__sass__metrics__api_1ga17d012eec574a36a7a8724177ba5e356)(CUpti_SassMetricsFlushData_Params *pParams) Flush SASS metrics data from CUPTI internal buffer to the user buffer.

- CUptiResult
[cuptiSassMetricsGetDataProperties](https://docs.nvidia.com#group__cupti__sass__metrics__api_1ga2601b1a5b4fe4b9253cdb81f04120b1e)(CUpti_SassMetricsGetDataProperties_Params *pParams) SASS metric data properties API will give the data regarding number of instances of a metric value and number of SASS instruction data has been collected.

- CUptiResult
[cuptiSassMetricsGetMetrics](https://docs.nvidia.com#group__cupti__sass__metrics__api_1gad3c097f40817fd8411c086c39ef74d0a)(CUpti_SassMetrics_GetMetrics_Params *pParams) Get the list of all supported SASS metrics for the chip.

- CUptiResult
[cuptiSassMetricsGetNumOfMetrics](https://docs.nvidia.com#group__cupti__sass__metrics__api_1ga3019950028060e943b12b7fc6f1b9188)(CUpti_SassMetrics_GetNumOfMetrics_Params *pParams) Get the number of supported SASS metrics for the chip.

- CUptiResult
[cuptiSassMetricsGetProperties](https://docs.nvidia.com#group__cupti__sass__metrics__api_1ga391895709314386ece556a4e69f727ef)(CUpti_SassMetrics_GetProperties_Params *pParams) Get metric properties for the queried metric.

- CUptiResult
[cuptiSassMetricsSetConfig](https://docs.nvidia.com#group__cupti__sass__metrics__api_1ga0c3e83b6fa0938f8da75bea89092f848)(CUpti_SassMetricsSetConfig_Params *pParams) Set config for the SASS metric data collection for a device.

- CUptiResult
[cuptiSassMetricsUnsetConfig](https://docs.nvidia.com#group__cupti__sass__metrics__api_1ga5676647f379b5101a09e24e1caa045d7)(CUpti_SassMetricsUnsetConfig_Params *pParams) Unset config API will reset the SASS metric data collection configuration for the device.


## 6.12.5. Macros[#](https://docs.nvidia.com#id1)

-
CUpti_SassMetricsDisable_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_SassMetricsDisable_Params_STRUCT_SIZE)

-
CUpti_SassMetricsEnable_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_SassMetricsEnable_Params_STRUCT_SIZE)

-
CUpti_SassMetricsFlushData_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_SassMetricsFlushData_Params_STRUCT_SIZE)

-
CUpti_SassMetricsGetDataProperties_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_SassMetricsGetDataProperties_Params_STRUCT_SIZE)

-
CUpti_SassMetricsSetConfig_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_SassMetricsSetConfig_Params_STRUCT_SIZE)

-
CUpti_SassMetricsUnsetConfig_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_SassMetricsUnsetConfig_Params_STRUCT_SIZE)

-
CUpti_SassMetrics_GetMetrics_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_SassMetrics_GetMetrics_Params_STRUCT_SIZE)

-
CUpti_SassMetrics_GetNumOfMetrics_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_SassMetrics_GetNumOfMetrics_Params_STRUCT_SIZE)

-
CUpti_SassMetrics_GetProperties_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_SassMetrics_GetProperties_Params_STRUCT_SIZE)

-
CUpti_SassMetrics_InstanceValue_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_SassMetrics_InstanceValue_STRUCT_SIZE)

## 6.12.6. Enumerations[#](https://docs.nvidia.com#id2)

-
enum CUpti_SassMetrics_OutputGranularity
[#](https://docs.nvidia.com#_CPPv435CUpti_SassMetrics_OutputGranularity) *Values:*-
enumerator CUPTI_SASS_METRICS_OUTPUT_GRANULARITY_GPU
[#](https://docs.nvidia.com#_CPPv4N35CUpti_SassMetrics_OutputGranularity41CUPTI_SASS_METRICS_OUTPUT_GRANULARITY_GPUE) SASS metric data will be collected at GPU level. In

[CUpti_SassMetricsGetDataProperties_Params](https://docs.nvidia.com/structCUpti__SassMetricsGetDataProperties__Params.html#structcupti__sassmetricsgetdataproperties__params)struct the numOfInstances will be equal to 1.

-
enumerator CUPTI_SASS_METRICS_OUTPUT_GRANULARITY_SM
[#](https://docs.nvidia.com#_CPPv4N35CUpti_SassMetrics_OutputGranularity40CUPTI_SASS_METRICS_OUTPUT_GRANULARITY_SME) SASS metric data will be collected at SM level In

[CUpti_SassMetricsGetDataProperties_Params](https://docs.nvidia.com/structCUpti__SassMetricsGetDataProperties__Params.html#structcupti__sassmetricsgetdataproperties__params)struct the numOfInstances will be equal to number of SMs in the GPU.

-
enumerator CUPTI_SASS_METRICS_OUTPUT_GRANULARITY_SMSP
[#](https://docs.nvidia.com#_CPPv4N35CUpti_SassMetrics_OutputGranularity42CUPTI_SASS_METRICS_OUTPUT_GRANULARITY_SMSPE) SASS metric data will be collected at SM sub-partition level In

[CUpti_SassMetricsGetDataProperties_Params](https://docs.nvidia.com/structCUpti__SassMetricsGetDataProperties__Params.html#structcupti__sassmetricsgetdataproperties__params)struct the numOfInstances will be equal to number of SM sub-partitions in the GPU.

-
enumerator CUPTI_SASS_METRICS_OUTPUT_GRANULARITY_INVALID
[#](https://docs.nvidia.com#_CPPv4N35CUpti_SassMetrics_OutputGranularity45CUPTI_SASS_METRICS_OUTPUT_GRANULARITY_INVALIDE)

-
enumerator CUPTI_SASS_METRICS_OUTPUT_GRANULARITY_GPU

## 6.12.7. Functions[#](https://docs.nvidia.com#id3)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiSassMetricsDisable( ,[CUpti_SassMetricsDisable_Params](https://docs.nvidia.com/structCUpti__SassMetricsDisable__Params.html#_CPPv431CUpti_SassMetricsDisable_Params)*pParamsSASS metric data collection disable API will mark the end of a range, any kernel launched after this API call will not be profiled for the SASS metrics.

- Parameters:
**pParams**– A pointer to[CUpti_SassMetricsDisable_Params](https://docs.nvidia.com/structCUpti__SassMetricsDisable__Params.html#structcupti__sassmetricsdisable__params)- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if any`pParams`

is not valid**CUPTI_ERROR_NOT_SUPPORTED**– indicates that the system/device doesn’t support SASS metric data collection**CUPTI_ERROR_INVALID_CONTEXT**– if any cuda context has not been created prior to this API call**CUPTI_ERROR_INVALID_OPERATION**– if this API is called multiple times for a cuda context without calling[cuptiSassMetricsEnable()](https://docs.nvidia.com#group__cupti__sass__metrics__api_1ga62ea0db81c966ddf066c28644f8b240f)API or called before[cuptiSassMetricsSetConfig()](https://docs.nvidia.com#group__cupti__sass__metrics__api_1ga0c3e83b6fa0938f8da75bea89092f848)API call.



[#](https://docs.nvidia.com#_CPPv423cuptiSassMetricsDisableP31CUpti_SassMetricsDisable_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiSassMetricsEnable( ,[CUpti_SassMetricsEnable_Params](https://docs.nvidia.com/structCUpti__SassMetricsEnable__Params.html#_CPPv430CUpti_SassMetricsEnable_Params)*pParamsSass metric data collection enable API will mark the start of a range, between which kernel will be profiled for SASS metrics.

- Parameters:
**pParams**– A pointer to[CUpti_SassMetricsEnable_Params](https://docs.nvidia.com/structCUpti__SassMetricsEnable__Params.html#structcupti__sassmetricsenable__params)- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if any`pParams`

is not valid**CUPTI_ERROR_NOT_SUPPORTED**– indicates that the system/device doesn’t support SASS metric data collection**CUPTI_ERROR_INVALID_CONTEXT**– if any cuda context has not been created prior to this API call**CUPTI_ERROR_INVALID_OPERATION**– if this API is called multiple times for a cuda context without calling[cuptiSassMetricsDisable()](https://docs.nvidia.com#group__cupti__sass__metrics__api_1gadf8447d381211251c69cdaf3221a5fec)API or called before[cuptiSassMetricsSetConfig()](https://docs.nvidia.com#group__cupti__sass__metrics__api_1ga0c3e83b6fa0938f8da75bea89092f848)API call.



[#](https://docs.nvidia.com#_CPPv422cuptiSassMetricsEnableP30CUpti_SassMetricsEnable_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiSassMetricsFlushData( ,[CUpti_SassMetricsFlushData_Params](https://docs.nvidia.com/structCUpti__SassMetricsFlushData__Params.html#_CPPv433CUpti_SassMetricsFlushData_Params)*pParamsFlush SASS metrics data from CUPTI internal buffer to the user buffer.

User needs to allocate the buffer for retrieving the data. The number of records collected can be queried using the API

[cuptiSassMetricsGetDataProperties()](https://docs.nvidia.com#group__cupti__sass__metrics__api_1ga2601b1a5b4fe4b9253cdb81f04120b1e).- Parameters:
**pParams**– A pointer to[CUpti_SassMetricsFlushData_Params](https://docs.nvidia.com/structCUpti__SassMetricsFlushData__Params.html#structcupti__sassmetricsflushdata__params)- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if any`pParams`

is not valid**CUPTI_ERROR_NOT_SUPPORTED**– indicates that the system/device doesn’t support SASS metric data collection.**CUPTI_ERROR_INVALID_OPERATION**– if this API is called outside the enable/disable range.



[#](https://docs.nvidia.com#_CPPv425cuptiSassMetricsFlushDataP33CUpti_SassMetricsFlushData_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiSassMetricsGetDataProperties(
) SASS metric data properties API will give the data regarding number of instances of a metric value and number of SASS instruction data has been collected.

The number of instances of a metric will vary as per user set the output granularity level with CUpti_SassMetrics_OutputGranularity value. User need to allocate memory for retriving the SASS data using

[cuptiSassMetricsFlushData()](https://docs.nvidia.com#group__cupti__sass__metrics__api_1ga17d012eec574a36a7a8724177ba5e356)API.- Parameters:
**pParams**– A pointer to[CUpti_SassMetricsGetDataProperties_Params](https://docs.nvidia.com/structCUpti__SassMetricsGetDataProperties__Params.html#structcupti__sassmetricsgetdataproperties__params)- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if any`pParams`

is not valid**CUPTI_ERROR_NOT_SUPPORTED**– indicates that the system/device doesn’t support SASS metric data collection**CUPTI_ERROR_INVALID_OPERATION**– if this API is called outside the enable/disable range.



[#](https://docs.nvidia.com#_CPPv433cuptiSassMetricsGetDataPropertiesP41CUpti_SassMetricsGetDataProperties_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiSassMetricsGetMetrics( ,[CUpti_SassMetrics_GetMetrics_Params](https://docs.nvidia.com/structCUpti__SassMetrics__GetMetrics__Params.html#_CPPv435CUpti_SassMetrics_GetMetrics_Params)*pParamsGet the list of all supported SASS metrics for the chip.

- Parameters:
**pParams**– A pointer to[CUpti_SassMetrics_GetMetrics_Params](https://docs.nvidia.com/structCUpti__SassMetrics__GetMetrics__Params.html#structcupti__sassmetrics__getmetrics__params)- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if any`pParams`

is not valid**CUPTI_ERROR_NOT_SUPPORTED**– indicates that the system/device doesn’t support SASS metric collection



[#](https://docs.nvidia.com#_CPPv426cuptiSassMetricsGetMetricsP35CUpti_SassMetrics_GetMetrics_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiSassMetricsGetNumOfMetrics( ,[CUpti_SassMetrics_GetNumOfMetrics_Params](https://docs.nvidia.com/structCUpti__SassMetrics__GetNumOfMetrics__Params.html#_CPPv440CUpti_SassMetrics_GetNumOfMetrics_Params)*pParamsGet the number of supported SASS metrics for the chip.

- Parameters:
**pParams**– A pointer to[CUpti_SassMetrics_GetNumOfMetrics_Params](https://docs.nvidia.com/structCUpti__SassMetrics__GetNumOfMetrics__Params.html#structcupti__sassmetrics__getnumofmetrics__params)- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if any`pParams`

is not valid**CUPTI_ERROR_NOT_SUPPORTED**– indicates that the system/device doesn’t support SASS metric collection



[#](https://docs.nvidia.com#_CPPv431cuptiSassMetricsGetNumOfMetricsP40CUpti_SassMetrics_GetNumOfMetrics_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiSassMetricsGetProperties( ,[CUpti_SassMetrics_GetProperties_Params](https://docs.nvidia.com/structCUpti__SassMetrics__GetProperties__Params.html#_CPPv438CUpti_SassMetrics_GetProperties_Params)*pParamsGet metric properties for the queried metric.

For a given metric the results will be put in CUpti_SassMetrics_MetricDetails which stores metric ID, description of the metric.

- Parameters:
**pParams**– A pointer to[CUpti_SassMetrics_GetProperties_Params](https://docs.nvidia.com/structCUpti__SassMetrics__GetProperties__Params.html#structcupti__sassmetrics__getproperties__params)- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if any`pParams`

is not valid**CUPTI_ERROR_NOT_SUPPORTED**– indicates that the system/device doesn’t support SASS metric data collection



[#](https://docs.nvidia.com#_CPPv429cuptiSassMetricsGetPropertiesP38CUpti_SassMetrics_GetProperties_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiSassMetricsSetConfig( ,[CUpti_SassMetricsSetConfig_Params](https://docs.nvidia.com/structCUpti__SassMetricsSetConfig__Params.html#_CPPv433CUpti_SassMetricsSetConfig_Params)*pParamsSet config for the SASS metric data collection for a device.

User need to call this API before calling any of the SASS metric data collection APIs. Each set config API call need to be followed by cuptiSassPatchingUnSetConfig API before calling the

[cuptiSassMetricsSetConfig()](https://docs.nvidia.com#group__cupti__sass__metrics__api_1ga0c3e83b6fa0938f8da75bea89092f848)API again for the same device.- Parameters:
**pParams**– A pointer to[CUpti_SassMetricsSetConfig_Params](https://docs.nvidia.com/structCUpti__SassMetricsSetConfig__Params.html#structcupti__sassmetricssetconfig__params)- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if any`pParams`

is not valid**CUPTI_ERROR_INVALID_CONTEXT**– if any cuda context has not been created prior to this API call**CUPTI_ERROR_INVALID_OPERATION**– if this is called multiple times for the device without calling unset config API**CUPTI_ERROR_NOT_SUPPORTED**– indicates that the system/device doesn’t support SASS metric data collection



[#](https://docs.nvidia.com#_CPPv425cuptiSassMetricsSetConfigP33CUpti_SassMetricsSetConfig_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiSassMetricsUnsetConfig( ,[CUpti_SassMetricsUnsetConfig_Params](https://docs.nvidia.com/structCUpti__SassMetricsUnsetConfig__Params.html#_CPPv435CUpti_SassMetricsUnsetConfig_Params)*pParamsUnset config API will reset the SASS metric data collection configuration for the device.

Once this API called CUPTI will deallocate all the memory allocated and remove all the configuration for SASS metric data collection. User can only call this API for a device where

[cuptiSassMetricsSetConfig()](https://docs.nvidia.com#group__cupti__sass__metrics__api_1ga0c3e83b6fa0938f8da75bea89092f848)API has been called earlier for the device.- Parameters:
**pParams**– A pointer to[CUpti_SassMetricsSetConfig_Params](https://docs.nvidia.com/structCUpti__SassMetricsSetConfig__Params.html#structcupti__sassmetricssetconfig__params)- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if any`pParams`

is not valid**CUPTI_ERROR_INVALID_CONTEXT**– if any cuda context has not been created prior to this API call**CUPTI_ERROR_INVALID_OPERATION**– if this is called multiple times for the device without calling set config API**CUPTI_ERROR_NOT_SUPPORTED**– indicates that the system/device doesn’t support SASS metric data collection



[#](https://docs.nvidia.com#_CPPv427cuptiSassMetricsUnsetConfigP35CUpti_SassMetricsUnsetConfig_Params)