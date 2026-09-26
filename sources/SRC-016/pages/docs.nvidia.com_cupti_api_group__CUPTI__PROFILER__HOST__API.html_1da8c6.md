source: https://docs.nvidia.com/cupti/api/group__CUPTI__PROFILER__HOST__API.html

# 6.8. CUPTI Profiler Host API[#](https://docs.nvidia.com#cupti-profiler-host-api)

Functions, types, and enums that implement the CUPTI Profiler Host API.

## 6.8.1. Data Structures[#](https://docs.nvidia.com#data-structures)

[CUpti_Profiler_Host_ConfigAddMetrics_Params](https://docs.nvidia.com/structCUpti__Profiler__Host__ConfigAddMetrics__Params.html#structcupti__profiler__host__configaddmetrics__params)Params for cuptiProfilerHostConfigAddMetrics.

[CUpti_Profiler_Host_Deinitialize_Params](https://docs.nvidia.com/structCUpti__Profiler__Host__Deinitialize__Params.html#structcupti__profiler__host__deinitialize__params)Params for cuptiProfilerHostDeinitialize.

[CUpti_Profiler_Host_EvaluateToGpuValues_Params](https://docs.nvidia.com/structCUpti__Profiler__Host__EvaluateToGpuValues__Params.html#structcupti__profiler__host__evaluatetogpuvalues__params)Params for cuptiProfilerHostEvaluateToGpuValues.

[CUpti_Profiler_Host_GetBaseMetrics_Params](https://docs.nvidia.com/structCUpti__Profiler__Host__GetBaseMetrics__Params.html#structcupti__profiler__host__getbasemetrics__params)Params for cuptiProfilerHostGetSupportedMetrics.

[CUpti_Profiler_Host_GetConfigImageSize_Params](https://docs.nvidia.com/structCUpti__Profiler__Host__GetConfigImageSize__Params.html#structcupti__profiler__host__getconfigimagesize__params)Params for cuptiProfilerHostGetConfigImageSize.

[CUpti_Profiler_Host_GetConfigImage_Params](https://docs.nvidia.com/structCUpti__Profiler__Host__GetConfigImage__Params.html#structcupti__profiler__host__getconfigimage__params)Params for cuptiProfilerHostGetConfigImage.

[CUpti_Profiler_Host_GetMaxNumHardwareMetricsPerPass_Params](https://docs.nvidia.com/structCUpti__Profiler__Host__GetMaxNumHardwareMetricsPerPass__Params.html#structcupti__profiler__host__getmaxnumhardwaremetricsperpass__params)Params for cuptiProfilerHostGetMaxNumHardwareMetricsPerPass.

[CUpti_Profiler_Host_GetMetricProperties_Params](https://docs.nvidia.com/structCUpti__Profiler__Host__GetMetricProperties__Params.html#structcupti__profiler__host__getmetricproperties__params)Params for cuptiProfilerHostGetMetricProperties.

[CUpti_Profiler_Host_GetMetricsInSinglePassSet_Params](https://docs.nvidia.com/structCUpti__Profiler__Host__GetMetricsInSinglePassSet__Params.html#structcupti__profiler__host__getmetricsinsinglepassset__params)Params for cuptiProfilerHostGetMetricsInSinglePassSet.

[CUpti_Profiler_Host_GetNumOfPasses_Params](https://docs.nvidia.com/structCUpti__Profiler__Host__GetNumOfPasses__Params.html#structcupti__profiler__host__getnumofpasses__params)Params for cuptiProfilerHostGetNumOfPasses.

[CUpti_Profiler_Host_GetRangeName_Params](https://docs.nvidia.com/structCUpti__Profiler__Host__GetRangeName__Params.html#structcupti__profiler__host__getrangename__params)Params for cuptiProfilerHostGetRangeName.

[CUpti_Profiler_Host_GetSinglePassSets_Params](https://docs.nvidia.com/structCUpti__Profiler__Host__GetSinglePassSets__Params.html#structcupti__profiler__host__getsinglepasssets__params)Params for cuptiProfilerHostGetSinglePassSets.

[CUpti_Profiler_Host_GetSubMetrics_Params](https://docs.nvidia.com/structCUpti__Profiler__Host__GetSubMetrics__Params.html#structcupti__profiler__host__getsubmetrics__params)Params for cuptiProfilerHostGetSubMetrics.

[CUpti_Profiler_Host_GetSupportedChips_Params](https://docs.nvidia.com/structCUpti__Profiler__Host__GetSupportedChips__Params.html#structcupti__profiler__host__getsupportedchips__params)Params for cuptiProfilerHostGetSupportedChips.

[CUpti_Profiler_Host_Initialize_Params](https://docs.nvidia.com/structCUpti__Profiler__Host__Initialize__Params.html#structcupti__profiler__host__initialize__params)Params for cuptiProfilerHostInitialize.

[CUpti_Profiler_Host_SetDevicePartitionInfo_Params](https://docs.nvidia.com/structCUpti__Profiler__Host__SetDevicePartitionInfo__Params.html#structcupti__profiler__host__setdevicepartitioninfo__params)Params for cuptiProfilerHostSetDevicePartitionInfo.


## 6.8.2. Macros[#](https://docs.nvidia.com#macros)

[CUpti_Profiler_Host_ConfigAddMetrics_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__profiler__host__api_1gaf67a452b1c4b5dad3b1c940a48893501)[CUpti_Profiler_Host_Deinitialize_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__profiler__host__api_1gaabc27da3fd8df836ce123c560c2dca72)[CUpti_Profiler_Host_EvaluateToGpuValues_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__profiler__host__api_1gab97543f9bd49bf30bc526cb016638a00)[CUpti_Profiler_Host_GetBaseMetrics_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__profiler__host__api_1ga2258c6f8a4a40616135af8a15a555358)[CUpti_Profiler_Host_GetConfigImageSize_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__profiler__host__api_1ga2484267ccf05bd08826e50ac4f4d04f8)[CUpti_Profiler_Host_GetConfigImage_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__profiler__host__api_1gafd45104d051f42d1ef4a3ffb2e95e2e8)[CUpti_Profiler_Host_GetMaxNumHardwareMetricsPerPass_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__profiler__host__api_1gaa32677433116e106d5ef7b9150c8e5e6)[CUpti_Profiler_Host_GetMetricProperties_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__profiler__host__api_1gac40ebae3da9507358bed161d092a36d1)[CUpti_Profiler_Host_GetMetricsInSinglePassSet_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__profiler__host__api_1ga1f4a7f704f10f4ccd0502ff20bc45392)[CUpti_Profiler_Host_GetNumOfPasses_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__profiler__host__api_1gad9967636b27320a1797dd270194a149c)[CUpti_Profiler_Host_GetRangeName_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__profiler__host__api_1ga51a37594dfa9c113ee5cd51ca5a274c8)[CUpti_Profiler_Host_GetSinglePassSets_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__profiler__host__api_1gaa7d295aa361cd8aed514127df7a4374b)[CUpti_Profiler_Host_GetSubMetrics_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__profiler__host__api_1gaf814d8c17e1e9dff6b8955390edcc098)[CUpti_Profiler_Host_GetSupportedChips_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__profiler__host__api_1gad7255a38cdd68c9b0b18c590591cfaa2)[CUpti_Profiler_Host_Initialize_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__profiler__host__api_1ga3335e5101b75d8981ce253d9e6597a61)[CUpti_Profiler_Host_SetDevicePartitionInfo_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__profiler__host__api_1ga8966169d5e5e32284b3bf953bba3e5f9)

## 6.8.3. Enumerations[#](https://docs.nvidia.com#enumerations)

## 6.8.4. Functions[#](https://docs.nvidia.com#functions)

- CUptiResult
[cuptiProfilerHostConfigAddMetrics](https://docs.nvidia.com#group__cupti__profiler__host__api_1gafc7a43e4d0774169f71dddffe11dea1b)(CUpti_Profiler_Host_ConfigAddMetrics_Params *pParams) Add the metrics to the profiler host object for generating the config image.

- CUptiResult
[cuptiProfilerHostDeinitialize](https://docs.nvidia.com#group__cupti__profiler__host__api_1gacbd2ed7196ec7eea08f643d53d6aa1b6)(CUpti_Profiler_Host_Deinitialize_Params *pParams) Deinitialize and destroy the profiler host object (CUpti_Profiler_Host_Object).

- CUptiResult
[cuptiProfilerHostEvaluateToGpuValues](https://docs.nvidia.com#group__cupti__profiler__host__api_1ga388a983e8bcfc889721c17aae2e67a4f)(CUpti_Profiler_Host_EvaluateToGpuValues_Params *pParams) Evaluate the metric values for the range index stored in the counter data.

- CUptiResult
[cuptiProfilerHostGetBaseMetrics](https://docs.nvidia.com#group__cupti__profiler__host__api_1gac22e710e7ab4a829fe7078ca03d3dd72)(CUpti_Profiler_Host_GetBaseMetrics_Params *pParams) Get the list of supported base metrics for the chip.

- CUptiResult
[cuptiProfilerHostGetConfigImage](https://docs.nvidia.com#group__cupti__profiler__host__api_1ga6d5be3c323b994c6663457bfa977f083)(CUpti_Profiler_Host_GetConfigImage_Params *pParams) Get the config image for the metrics added to the profiler host object.

- CUptiResult
[cuptiProfilerHostGetConfigImageSize](https://docs.nvidia.com#group__cupti__profiler__host__api_1ga3c3b73ef795e55cab71436e4d0dfb662)(CUpti_Profiler_Host_GetConfigImageSize_Params *pParams) Get the size of the config image for the metrics added to the profiler host object.

- CUptiResult
[cuptiProfilerHostGetMaxNumHardwareMetricsPerPass](https://docs.nvidia.com#group__cupti__profiler__host__api_1gada083d0e2eb8712beeba0635d327df2b)(CUpti_Profiler_Host_GetMaxNumHardwareMetricsPerPass_Params *pParams) Get the maximum number of hardware metrics (metric names which doesn't include

*sass*keyword) that can be scheduled in a single pass for a chip.- CUptiResult
[cuptiProfilerHostGetMetricProperties](https://docs.nvidia.com#group__cupti__profiler__host__api_1ga623e00d7b19a7beebbeac85df5634b3e)(CUpti_Profiler_Host_GetMetricProperties_Params *pParams) Get the properties of the metric.

- CUptiResult
[cuptiProfilerHostGetMetricsInSinglePassSet](https://docs.nvidia.com#group__cupti__profiler__host__api_1ga0cbdbc7457214655611ec19fc15063ed)(CUpti_Profiler_Host_GetMetricsInSinglePassSet_Params *pParams) Get all the metrics defined in the single pass metric set.

- CUptiResult
[cuptiProfilerHostGetNumOfPasses](https://docs.nvidia.com#group__cupti__profiler__host__api_1gae2d8591e46bcee448fe9fa23d6854756)(CUpti_Profiler_Host_GetNumOfPasses_Params *pParams) Get the number of passes required for profiling the scheduled metrics in the config image.

- CUptiResult
[cuptiProfilerHostGetRangeName](https://docs.nvidia.com#group__cupti__profiler__host__api_1ga3b3a93d25139edf57fa20078521b431c)(CUpti_Profiler_Host_GetRangeName_Params *pParams) Get the range name for the range index stored in the counter data.

- CUptiResult
[cuptiProfilerHostGetSinglePassSets](https://docs.nvidia.com#group__cupti__profiler__host__api_1gaef29112ebeaf0bf683f5ed5539e6c357)(CUpti_Profiler_Host_GetSinglePassSets_Params *pParams) Get the single pass metric sets defined in the metric config file.

- CUptiResult
[cuptiProfilerHostGetSubMetrics](https://docs.nvidia.com#group__cupti__profiler__host__api_1ga21763899041aea8bfd60db908dbe477f)(CUpti_Profiler_Host_GetSubMetrics_Params *pParams) Get the list of supported sub-metrics for the metric.

- CUptiResult
[cuptiProfilerHostGetSupportedChips](https://docs.nvidia.com#group__cupti__profiler__host__api_1gae7eeeebc5b7e501bfb7e003dbce610f2)(CUpti_Profiler_Host_GetSupportedChips_Params *pParams) Get the list of supported chips.

- CUptiResult
[cuptiProfilerHostInitialize](https://docs.nvidia.com#group__cupti__profiler__host__api_1ga50ce9879e2460d04e1e759cf23043825)(CUpti_Profiler_Host_Initialize_Params *pParams) Create and initialize the profiler host object (CUpti_Profiler_Host_Object).

- CUptiResult
[cuptiProfilerHostSetDevicePartitionInfo](https://docs.nvidia.com#group__cupti__profiler__host__api_1gae2acff2140fd3cdfbd91f47b8db1c1b8)(CUpti_Profiler_Host_SetDevicePartitionInfo_Params *pParams) Set the device partition information for metric evaluation on Green Contexts.


## 6.8.5. Typedefs[#](https://docs.nvidia.com#typedefs)

## 6.8.6. Macros[#](https://docs.nvidia.com#id1)

-
CUpti_Profiler_Host_ConfigAddMetrics_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_Profiler_Host_ConfigAddMetrics_Params_STRUCT_SIZE)

-
CUpti_Profiler_Host_Deinitialize_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_Profiler_Host_Deinitialize_Params_STRUCT_SIZE)

-
CUpti_Profiler_Host_EvaluateToGpuValues_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_Profiler_Host_EvaluateToGpuValues_Params_STRUCT_SIZE)

-
CUpti_Profiler_Host_GetBaseMetrics_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_Profiler_Host_GetBaseMetrics_Params_STRUCT_SIZE)

-
CUpti_Profiler_Host_GetConfigImageSize_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_Profiler_Host_GetConfigImageSize_Params_STRUCT_SIZE)

-
CUpti_Profiler_Host_GetConfigImage_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_Profiler_Host_GetConfigImage_Params_STRUCT_SIZE)

-
CUpti_Profiler_Host_GetMaxNumHardwareMetricsPerPass_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_Profiler_Host_GetMaxNumHardwareMetricsPerPass_Params_STRUCT_SIZE)

-
CUpti_Profiler_Host_GetMetricProperties_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_Profiler_Host_GetMetricProperties_Params_STRUCT_SIZE)

-
CUpti_Profiler_Host_GetMetricsInSinglePassSet_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_Profiler_Host_GetMetricsInSinglePassSet_Params_STRUCT_SIZE)

-
CUpti_Profiler_Host_GetNumOfPasses_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_Profiler_Host_GetNumOfPasses_Params_STRUCT_SIZE)

-
CUpti_Profiler_Host_GetRangeName_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_Profiler_Host_GetRangeName_Params_STRUCT_SIZE)

-
CUpti_Profiler_Host_GetSinglePassSets_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_Profiler_Host_GetSinglePassSets_Params_STRUCT_SIZE)

-
CUpti_Profiler_Host_GetSubMetrics_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_Profiler_Host_GetSubMetrics_Params_STRUCT_SIZE)

-
CUpti_Profiler_Host_GetSupportedChips_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_Profiler_Host_GetSupportedChips_Params_STRUCT_SIZE)

-
CUpti_Profiler_Host_Initialize_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_Profiler_Host_Initialize_Params_STRUCT_SIZE)

-
CUpti_Profiler_Host_SetDevicePartitionInfo_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_Profiler_Host_SetDevicePartitionInfo_Params_STRUCT_SIZE)

## 6.8.7. Enumerations[#](https://docs.nvidia.com#id2)

-
enum CUpti_MetricCollectionScope
[#](https://docs.nvidia.com#_CPPv427CUpti_MetricCollectionScope) *Values:*-
enumerator CUPTI_METRIC_COLLECTION_SCOPE_CONTEXT
[#](https://docs.nvidia.com#_CPPv4N27CUpti_MetricCollectionScope37CUPTI_METRIC_COLLECTION_SCOPE_CONTEXTE)

-
enumerator CUPTI_METRIC_COLLECTION_SCOPE_DEVICE
[#](https://docs.nvidia.com#_CPPv4N27CUpti_MetricCollectionScope36CUPTI_METRIC_COLLECTION_SCOPE_DEVICEE)

-
enumerator CUPTI_METRIC_COLLECTION_SCOPE_INVALID
[#](https://docs.nvidia.com#_CPPv4N27CUpti_MetricCollectionScope37CUPTI_METRIC_COLLECTION_SCOPE_INVALIDE)

-
enumerator CUPTI_METRIC_COLLECTION_SCOPE_CONTEXT

## 6.8.8. Functions[#](https://docs.nvidia.com#id3)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiProfilerHostConfigAddMetrics(
) Add the metrics to the profiler host object for generating the config image.

The config image will have the required information to schedule the metrics for collecting the profiling data. Note:

PM sampling only supports single pass config image.

CUPTI has single pass sets supported for a chip, all metrics in a set can be collected in a single pass.

[cuptiProfilerHostGetSinglePassSets](https://docs.nvidia.com#group__cupti__profiler__host__api_1gaef29112ebeaf0bf683f5ed5539e6c357)API can be used to get the single pass sets supported for a chip.[cuptiProfilerHostGetMetricsInSinglePassSet](https://docs.nvidia.com#group__cupti__profiler__host__api_1ga0cbdbc7457214655611ec19fc15063ed)API can be used to get the metrics supported for a single pass set.

- Parameters:
**pParams**– A pointer to[CUpti_Profiler_Host_ConfigAddMetrics_Params](https://docs.nvidia.com/structCUpti__Profiler__Host__ConfigAddMetrics__Params.html#structcupti__profiler__host__configaddmetrics__params)- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if any`pParams`

is not valid**CUPTI_ERROR_INVALID_METRIC_NAME**– if the metric name is not valid or not supported for the chip**CUPTI_ERROR_UNKNOWN**– for any internal error



[#](https://docs.nvidia.com#_CPPv433cuptiProfilerHostConfigAddMetricsP43CUpti_Profiler_Host_ConfigAddMetrics_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiProfilerHostDeinitialize( ,[CUpti_Profiler_Host_Deinitialize_Params](https://docs.nvidia.com/structCUpti__Profiler__Host__Deinitialize__Params.html#_CPPv439CUpti_Profiler_Host_Deinitialize_Params)*pParamsDeinitialize and destroy the profiler host object (CUpti_Profiler_Host_Object).

- Parameters:
**pParams**– A pointer to[CUpti_Profiler_Host_Deinitialize_Params](https://docs.nvidia.com/structCUpti__Profiler__Host__Deinitialize__Params.html#structcupti__profiler__host__deinitialize__params)- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if any`pParams`

is not valid**CUPTI_ERROR_UNKNOWN**– for any internal error



[#](https://docs.nvidia.com#_CPPv429cuptiProfilerHostDeinitializeP39CUpti_Profiler_Host_Deinitialize_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiProfilerHostEvaluateToGpuValues(
) Evaluate the metric values for the range index stored in the counter data.

- Parameters:
**pParams**– A pointer to[CUpti_Profiler_Host_EvaluateToGpuValues_Params](https://docs.nvidia.com/structCUpti__Profiler__Host__EvaluateToGpuValues__Params.html#structcupti__profiler__host__evaluatetogpuvalues__params)- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if any`pParams`

is not valid**CUPTI_ERROR_INVALID_METRIC_NAME**– if the metric name is not valid or not supported for the chip**CUPTI_ERROR_UNKNOWN**– for any internal error



[#](https://docs.nvidia.com#_CPPv436cuptiProfilerHostEvaluateToGpuValuesP46CUpti_Profiler_Host_EvaluateToGpuValues_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiProfilerHostGetBaseMetrics(
) Get the list of supported base metrics for the chip.

- Parameters:
**pParams**– A pointer to[CUpti_Profiler_Host_GetBaseMetrics_Params](https://docs.nvidia.com/structCUpti__Profiler__Host__GetBaseMetrics__Params.html#structcupti__profiler__host__getbasemetrics__params)- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if any`pParams`

is not valid**CUPTI_ERROR_UNKNOWN**– for any internal error



[#](https://docs.nvidia.com#_CPPv431cuptiProfilerHostGetBaseMetricsP41CUpti_Profiler_Host_GetBaseMetrics_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiProfilerHostGetConfigImage(
) Get the config image for the metrics added to the profiler host object.

User will pass the allocated buffer to store the config image.

- Parameters:
**pParams**– A pointer to[CUpti_Profiler_Host_GetConfigImage_Params](https://docs.nvidia.com/structCUpti__Profiler__Host__GetConfigImage__Params.html#structcupti__profiler__host__getconfigimage__params)- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if any`pParams`

is not valid**CUPTI_ERROR_UNKNOWN**– for any internal error



[#](https://docs.nvidia.com#_CPPv431cuptiProfilerHostGetConfigImageP41CUpti_Profiler_Host_GetConfigImage_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiProfilerHostGetConfigImageSize(
) Get the size of the config image for the metrics added to the profiler host object.

Users need to allocate the buffer for storing the config image.

- Parameters:
**pParams**– A pointer to[CUpti_Profiler_Host_GetConfigImageSize_Params](https://docs.nvidia.com/structCUpti__Profiler__Host__GetConfigImageSize__Params.html#structcupti__profiler__host__getconfigimagesize__params)- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if any`pParams`

is not valid**CUPTI_ERROR_UNKNOWN**– for any internal error



[#](https://docs.nvidia.com#_CPPv435cuptiProfilerHostGetConfigImageSizeP45CUpti_Profiler_Host_GetConfigImageSize_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiProfilerHostGetMaxNumHardwareMetricsPerPass(
) Get the maximum number of hardware metrics (metric names which doesn’t include

*sass*keyword) that can be scheduled in a single pass for a chip.While this represents a theoretical upper limit, practical constraints may prevent reaching this threshold for a specific set of metrics. Furthermore, the maximum achievable value is contingent upon the characteristics and architecture of the chip in question.

Use cuptiProfilerHostGetNumOfPasses API for getting the actual number of passes required for the for collecting the profiling data for the scheduled metrics in a config image.

- Parameters:
**pParams**– A pointer to[CUpti_Profiler_Host_GetMaxNumHardwareMetricsPerPass_Params](https://docs.nvidia.com/structCUpti__Profiler__Host__GetMaxNumHardwareMetricsPerPass__Params.html#structcupti__profiler__host__getmaxnumhardwaremetricsperpass__params)- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if any`pParams`

is not valid**CUPTI_ERROR_UNKNOWN**– for any internal error



[#](https://docs.nvidia.com#_CPPv448cuptiProfilerHostGetMaxNumHardwareMetricsPerPassP58CUpti_Profiler_Host_GetMaxNumHardwareMetricsPerPass_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiProfilerHostGetMetricProperties(
) Get the properties of the metric.

- Parameters:
**pParams**– A pointer to[CUpti_Profiler_Host_GetMetricProperties_Params](https://docs.nvidia.com/structCUpti__Profiler__Host__GetMetricProperties__Params.html#structcupti__profiler__host__getmetricproperties__params)- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if any`pParams`

is not valid**CUPTI_ERROR_INVALID_METRIC_NAME**– if the metric name is not valid or not supported for the chip**CUPTI_ERROR_UNKNOWN**– for any internal error



[#](https://docs.nvidia.com#_CPPv436cuptiProfilerHostGetMetricPropertiesP46CUpti_Profiler_Host_GetMetricProperties_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiProfilerHostGetMetricsInSinglePassSet(
) Get all the metrics defined in the single pass metric set.

Profiling data for the metrics in a single pass metric set can be collected in a single pass.

This is a two-phase function to retrieve metrics in a single-pass metric set. First pass (query mode): Set pParams->pMetricsBuffer = NULL and pParams->pMetricsIndicesBuffer = NULL The function returns required buffer sizes in:

numOfMetricsInSinglePassSet: Number of metrics in set

metricsBufferSize: Total buffer size needed for metric data


Second pass (data retrieval):

Set pParams->pMetricsBuffer = allocated buffer for metrics

Set pParams->pMetricsIndicesBuffer = allocated buffer for metrics indices

Set pParams->numOfMetricsInSinglePassSet = number of metrics in set

Set pParams->metricsBufferSize = allocated buffer size for metrics

Call the function again to populate the buffers


- Parameters:
**pParams**– A pointer to[CUpti_Profiler_Host_GetMetricsInSinglePassSet_Params](https://docs.nvidia.com/structCUpti__Profiler__Host__GetMetricsInSinglePassSet__Params.html#structcupti__profiler__host__getmetricsinsinglepassset__params)- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if any`pParams`

is not valid also when either of pMetricsBuffer and pMetricsIndicesBuffer are NULL while the other is not NULL**CUPTI_ERROR_UNKNOWN**– for any internal error



[#](https://docs.nvidia.com#_CPPv442cuptiProfilerHostGetMetricsInSinglePassSetP52CUpti_Profiler_Host_GetMetricsInSinglePassSet_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiProfilerHostGetNumOfPasses(
) Get the number of passes required for profiling the scheduled metrics in the config image.

- Parameters:
**pParams**– A pointer to[CUpti_Profiler_Host_GetNumOfPasses_Params](https://docs.nvidia.com/structCUpti__Profiler__Host__GetNumOfPasses__Params.html#structcupti__profiler__host__getnumofpasses__params)- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if any`pParams`

is not valid**CUPTI_ERROR_UNKNOWN**– for any internal error



[#](https://docs.nvidia.com#_CPPv431cuptiProfilerHostGetNumOfPassesP41CUpti_Profiler_Host_GetNumOfPasses_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiProfilerHostGetRangeName( ,[CUpti_Profiler_Host_GetRangeName_Params](https://docs.nvidia.com/structCUpti__Profiler__Host__GetRangeName__Params.html#_CPPv439CUpti_Profiler_Host_GetRangeName_Params)*pParamsGet the range name for the range index stored in the counter data.

In Range profiler, for Auto range mode the range name will be numeric value assigned to the kernel based on execution order. For user range mode, the name of range will be based on the range name provided by the user using Push range API.

- Parameters:
**pParams**– A pointer to[CUpti_Profiler_Host_GetRangeName_Params](https://docs.nvidia.com/structCUpti__Profiler__Host__GetRangeName__Params.html#structcupti__profiler__host__getrangename__params)- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if any`pParams`

is not valid**CUPTI_ERROR_UNKNOWN**– for any internal error



[#](https://docs.nvidia.com#_CPPv429cuptiProfilerHostGetRangeNameP39CUpti_Profiler_Host_GetRangeName_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiProfilerHostGetSinglePassSets(
) Get the single pass metric sets defined in the metric config file.

Profiling data for the metrics in a single pass metric set can be collected in a single pass.

- Parameters:
**pParams**– A pointer to[CUpti_Profiler_Host_GetSinglePassSets_Params](https://docs.nvidia.com/structCUpti__Profiler__Host__GetSinglePassSets__Params.html#structcupti__profiler__host__getsinglepasssets__params)when ppSinglePassSets is NULL, the function will return the number of single pass metric sets and the caller needs to allocate the buffer for the single pass metric sets using the number of single pass metric sets. (i.e. ppSinglePassSets)- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if any`pParams`

is not valid**CUPTI_ERROR_UNKNOWN**– for any internal error



[#](https://docs.nvidia.com#_CPPv434cuptiProfilerHostGetSinglePassSetsP44CUpti_Profiler_Host_GetSinglePassSets_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiProfilerHostGetSubMetrics( ,[CUpti_Profiler_Host_GetSubMetrics_Params](https://docs.nvidia.com/structCUpti__Profiler__Host__GetSubMetrics__Params.html#_CPPv440CUpti_Profiler_Host_GetSubMetrics_Params)*pParamsGet the list of supported sub-metrics for the metric.

- Parameters:
**pParams**– A pointer to[CUpti_Profiler_Host_GetSubMetrics_Params](https://docs.nvidia.com/structCUpti__Profiler__Host__GetSubMetrics__Params.html#structcupti__profiler__host__getsubmetrics__params)- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if any`pParams`

is not valid**CUPTI_ERROR_INVALID_METRIC_NAME**– if the metric name is not valid or not supported for the chip**CUPTI_ERROR_UNKNOWN**– for any internal error



[#](https://docs.nvidia.com#_CPPv430cuptiProfilerHostGetSubMetricsP40CUpti_Profiler_Host_GetSubMetrics_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiProfilerHostGetSupportedChips(
) Get the list of supported chips.

- Parameters:
**pParams**– A pointer to[CUpti_Profiler_Host_GetSupportedChips_Params](https://docs.nvidia.com/structCUpti__Profiler__Host__GetSupportedChips__Params.html#structcupti__profiler__host__getsupportedchips__params)- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if any`pParams`

is not valid**CUPTI_ERROR_UNKNOWN**– for any internal error



[#](https://docs.nvidia.com#_CPPv434cuptiProfilerHostGetSupportedChipsP44CUpti_Profiler_Host_GetSupportedChips_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiProfilerHostInitialize( ,[CUpti_Profiler_Host_Initialize_Params](https://docs.nvidia.com/structCUpti__Profiler__Host__Initialize__Params.html#_CPPv437CUpti_Profiler_Host_Initialize_Params)*pParamsCreate and initialize the profiler host object (CUpti_Profiler_Host_Object).

- Parameters:
**pParams**– A pointer to[CUpti_Profiler_Host_Initialize_Params](https://docs.nvidia.com/structCUpti__Profiler__Host__Initialize__Params.html#structcupti__profiler__host__initialize__params)- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if any`pParams`

is not valid**CUPTI_ERROR_NOT_INITIALIZED**– if CUPTI could not dynamically load the nvperf* libraries. Ensure libnvperf_host.so and libnvperf_target.so, shipped alongside libcupti.so, are discoverable by the dynamic linker.**CUPTI_ERROR_UNKNOWN**– for any internal error



[#](https://docs.nvidia.com#_CPPv427cuptiProfilerHostInitializeP37CUpti_Profiler_Host_Initialize_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiProfilerHostSetDevicePartitionInfo(
) Set the device partition information for metric evaluation on Green Contexts.

When profiling workloads running on Green Contexts, the device resources (such as Streaming Multiprocessors) are partitioned among multiple Green Contexts. This partition information is essential for correctly evaluating and scaling metric values from the collected counter data.

The device partition information should be obtained from the target side using

[cuptiRangeProfilerGetDevicePartitionInfo](https://docs.nvidia.com/group__CUPTI__RANGE__PROFILER__API.html#group__cupti__range__profiler__api_1ga5bc20e82550fba23fc3fc6caba8363ab)after starting the range profiler on a Green Context. This information must be set on the profiler host object before calling[cuptiProfilerHostEvaluateToGpuValues](https://docs.nvidia.com#group__cupti__profiler__host__api_1ga388a983e8bcfc889721c17aae2e67a4f)to ensure accurate metric evaluation that accounts for the partitioned device resources.Note: This API is only required when profiling on Green Contexts. For profiling on regular CUDA contexts that have access to all device resources, this API is not needed.

- Parameters:
**pParams**– A pointer to[CUpti_Profiler_Host_SetDevicePartitionInfo_Params](https://docs.nvidia.com/structCUpti__Profiler__Host__SetDevicePartitionInfo__Params.html#structcupti__profiler__host__setdevicepartitioninfo__params)- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if any`pParams`

is not valid**CUPTI_ERROR_UNKNOWN**– for any internal error



[#](https://docs.nvidia.com#_CPPv439cuptiProfilerHostSetDevicePartitionInfoP49CUpti_Profiler_Host_SetDevicePartitionInfo_Params)

## 6.8.9. Typedefs[#](https://docs.nvidia.com#id4)

-
typedef struct
[CUpti_Profiler_Host_Object](https://docs.nvidia.com#_CPPv426CUpti_Profiler_Host_Object)CUpti_Profiler_Host_Object[#](https://docs.nvidia.com#_CPPv426CUpti_Profiler_Host_Object)