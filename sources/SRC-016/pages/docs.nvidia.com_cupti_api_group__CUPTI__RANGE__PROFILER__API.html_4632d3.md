source: https://docs.nvidia.com/cupti/api/group__CUPTI__RANGE__PROFILER__API.html

# 6.10. CUPTI Range Profiling API[#](https://docs.nvidia.com#cupti-range-profiling-api)

Functions, types, and enums that implement the CUPTI Range Profiling API.

## 6.10.1. Data Structures[#](https://docs.nvidia.com#data-structures)

[CUpti_RangeProfiler_CounterDataImage_Initialize_Params](https://docs.nvidia.com/structCUpti__RangeProfiler__CounterDataImage__Initialize__Params.html#structcupti__rangeprofiler__counterdataimage__initialize__params)Params for cuptiRangeProfilerCounterDataImageInitialize.

[CUpti_RangeProfiler_CounterData_GetRangeInfo_Params](https://docs.nvidia.com/structCUpti__RangeProfiler__CounterData__GetRangeInfo__Params.html#structcupti__rangeprofiler__counterdata__getrangeinfo__params)Params for cuptiRangeProfilerCounterDataGetRangeInfo.

[CUpti_RangeProfiler_DecodeData_Params](https://docs.nvidia.com/structCUpti__RangeProfiler__DecodeData__Params.html#structcupti__rangeprofiler__decodedata__params)Params for cuptiRangeProfilerDecodeData.

[CUpti_RangeProfiler_Disable_Params](https://docs.nvidia.com/structCUpti__RangeProfiler__Disable__Params.html#structcupti__rangeprofiler__disable__params)Params for cuptiRangeProfilerDisable.

[CUpti_RangeProfiler_Enable_Params](https://docs.nvidia.com/structCUpti__RangeProfiler__Enable__Params.html#structcupti__rangeprofiler__enable__params)Params for cuptiRangeProfilerEnable.

[CUpti_RangeProfiler_GetCounterDataInfo_Params](https://docs.nvidia.com/structCUpti__RangeProfiler__GetCounterDataInfo__Params.html#structcupti__rangeprofiler__getcounterdatainfo__params)Params for cuptiRangeProfilerGetCounterDataInfo.

[CUpti_RangeProfiler_GetCounterDataSize_Params](https://docs.nvidia.com/structCUpti__RangeProfiler__GetCounterDataSize__Params.html#structcupti__rangeprofiler__getcounterdatasize__params)Params for cuptiRangeProfilerGetCounterDataSize.

[CUpti_RangeProfiler_GetDevicePartitionInfo_Params](https://docs.nvidia.com/structCUpti__RangeProfiler__GetDevicePartitionInfo__Params.html#structcupti__rangeprofiler__getdevicepartitioninfo__params)Params for cuptiRangeProfilerGetDevicePartitionInfo.

[CUpti_RangeProfiler_PopRange_Params](https://docs.nvidia.com/structCUpti__RangeProfiler__PopRange__Params.html#structcupti__rangeprofiler__poprange__params)Params for cuptiRangeProfilerPopRange.

[CUpti_RangeProfiler_PushRange_Params](https://docs.nvidia.com/structCUpti__RangeProfiler__PushRange__Params.html#structcupti__rangeprofiler__pushrange__params)Params for cuptiRangeProfilerPushRange.

[CUpti_RangeProfiler_SetConfig_Params](https://docs.nvidia.com/structCUpti__RangeProfiler__SetConfig__Params.html#structcupti__rangeprofiler__setconfig__params)Params for cuptiRangeProfilerSetConfig.

[CUpti_RangeProfiler_Start_Params](https://docs.nvidia.com/structCUpti__RangeProfiler__Start__Params.html#structcupti__rangeprofiler__start__params)Params for cuptiRangeProfilerStart.

[CUpti_RangeProfiler_Stop_Params](https://docs.nvidia.com/structCUpti__RangeProfiler__Stop__Params.html#structcupti__rangeprofiler__stop__params)Params for cuptiRangeProfilerStop.


## 6.10.2. Macros[#](https://docs.nvidia.com#macros)

[CUpti_RangeProfiler_CounterDataImage_Initialize_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__range__profiler__api_1ga0e05a12d7a8d2247d7b1ac68d04306d2)[CUpti_RangeProfiler_CounterData_GetRangeInfo_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__range__profiler__api_1gaae9493b0f31e271797efbd19e0e46342)[CUpti_RangeProfiler_DecodeData_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__range__profiler__api_1gae363ce62c78e6900feb39096c0339475)[CUpti_RangeProfiler_Disable_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__range__profiler__api_1ga15cb38194d2e74710c9e3d3c3ecf3437)[CUpti_RangeProfiler_Enable_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__range__profiler__api_1ga149dfba551985671e3b5a3eace593429)[CUpti_RangeProfiler_GetCounterDataInfo_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__range__profiler__api_1ga52d83581c5b7af09147023812f5a376a)[CUpti_RangeProfiler_GetCounterDataSize_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__range__profiler__api_1gad897ff02fe1739b7e7baaba4681d0a80)[CUpti_RangeProfiler_GetDevicePartitionInfo_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__range__profiler__api_1gae283bed858eec7edbe69bb1928a5f3c5)[CUpti_RangeProfiler_PopRange_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__range__profiler__api_1gaf62c1c24617186634882ca68a37f24d0)[CUpti_RangeProfiler_PushRange_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__range__profiler__api_1ga9fd7034c790b8672f7eb962f56d2357d)[CUpti_RangeProfiler_SetConfig_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__range__profiler__api_1gade89b2634d6bd954ce2d8b0c3dc36d34)[CUpti_RangeProfiler_Start_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__range__profiler__api_1ga7f9eaa1f465fb3d7b112d0faf1bd3341)[CUpti_RangeProfiler_Stop_Params_STRUCT_SIZE](https://docs.nvidia.com#group__cupti__range__profiler__api_1ga7168662a5f02cd2d1c31556843eed230)

## 6.10.3. Enumerations[#](https://docs.nvidia.com#enumerations)

[CUpti_CacheControl_Mode](https://docs.nvidia.com#group__cupti__range__profiler__api_1ga34bd24cdc4884783e5e19bdc042ee224)Cache control modes for Range Profiler replay passes.


## 6.10.4. Functions[#](https://docs.nvidia.com#functions)

- CUptiResult
[cuptiRangeProfilerCounterDataGetRangeInfo](https://docs.nvidia.com#group__cupti__range__profiler__api_1ga3a75df42394dd3a9e92815a95b5974ee)(CUpti_RangeProfiler_CounterData_GetRangeInfo_Params *pParams) Get the range name for the given range index.

- CUptiResult
[cuptiRangeProfilerCounterDataImageInitialize](https://docs.nvidia.com#group__cupti__range__profiler__api_1gac9b723489c1bf0b5a7e7fa37f276a6de)(CUpti_RangeProfiler_CounterDataImage_Initialize_Params *pParams) Initialize the counter data image with the profiling data for the ranges profiled.

- CUptiResult
[cuptiRangeProfilerDecodeData](https://docs.nvidia.com#group__cupti__range__profiler__api_1gab7ea389b1957ec7cd26162ad7af7205a)(CUpti_RangeProfiler_DecodeData_Params *pParams) Decode the profiling data stored in the hardware to the counter data image passed in the SetConfig API.

- CUptiResult
[cuptiRangeProfilerDisable](https://docs.nvidia.com#group__cupti__range__profiler__api_1ga062be4b9c43eec450718b2d01ceda582)(CUpti_RangeProfiler_Disable_Params *pParams) Disable the range profiler on the CUDA context and destroy the range profiler object.

- CUptiResult
[cuptiRangeProfilerEnable](https://docs.nvidia.com#group__cupti__range__profiler__api_1ga7ea8fd4160643df21e66c2242d044010)(CUpti_RangeProfiler_Enable_Params *pParams) Create a range profiler object and enable range profiling on the CUDA context.

- CUptiResult
[cuptiRangeProfilerGetCounterDataInfo](https://docs.nvidia.com#group__cupti__range__profiler__api_1gaab887096e8046e1e99ea98bf80039099)(CUpti_RangeProfiler_GetCounterDataInfo_Params *pParams) Get the number of ranges stored in the counter data image.

- CUptiResult
[cuptiRangeProfilerGetCounterDataSize](https://docs.nvidia.com#group__cupti__range__profiler__api_1ga1dfe3a77592a9bd10e4d7321c17ea664)(CUpti_RangeProfiler_GetCounterDataSize_Params *pParams) Get the size of the counter data image required to store the profiling data for the ranges profiled.

- CUptiResult
[cuptiRangeProfilerGetDevicePartitionInfo](https://docs.nvidia.com#group__cupti__range__profiler__api_1ga5bc20e82550fba23fc3fc6caba8363ab)(CUpti_RangeProfiler_GetDevicePartitionInfo_Params *pParams) Get the device partition information for a Green Context.

- CUptiResult
[cuptiRangeProfilerPopRange](https://docs.nvidia.com#group__cupti__range__profiler__api_1ga7470778814dac22a92d76ffc2e63b527)(CUpti_RangeProfiler_PopRange_Params *pParams) pop the current range to the Range Profiler.

- CUptiResult
[cuptiRangeProfilerPushRange](https://docs.nvidia.com#group__cupti__range__profiler__api_1gaef4180eb7242908530fc8c4f23e22c9f)(CUpti_RangeProfiler_PushRange_Params *pParams) Add a new range to the Range Profiler with a given range name.

- CUptiResult
[cuptiRangeProfilerSetConfig](https://docs.nvidia.com#group__cupti__range__profiler__api_1ga1553671fd1ddda16ba35a923a6c84cc5)(CUpti_RangeProfiler_SetConfig_Params *pParams) Set the configuration for range profiler like maximum number of ranges per pass, number of nesting levels, range and replay mode and the config image which has scheduling info for metric collection.

- CUptiResult
[cuptiRangeProfilerStart](https://docs.nvidia.com#group__cupti__range__profiler__api_1gaae839f931a50f1436df35367e3e71416)(CUpti_RangeProfiler_Start_Params *pParams) Start the range profiler.

- CUptiResult
[cuptiRangeProfilerStop](https://docs.nvidia.com#group__cupti__range__profiler__api_1gae64164c9209b9fb92d2d91b61b052643)(CUpti_RangeProfiler_Stop_Params *pParams) Stop the range profiler.


## 6.10.5. Typedefs[#](https://docs.nvidia.com#typedefs)

## 6.10.6. Variables[#](https://docs.nvidia.com#variables)

- size_t
[CUpti_RangeProfiler_CounterDataImage_Initialize_Params::counterDataSize](https://docs.nvidia.com/structCUpti__RangeProfiler__CounterDataImage__Initialize__Params.html#group__cupti__range__profiler__api_1ga1d90460a42dfa8338a44c98c6ca8447c) [in] Size of the counter data image.

- uint8_t *
[CUpti_RangeProfiler_CounterDataImage_Initialize_Params::pCounterData](https://docs.nvidia.com/structCUpti__RangeProfiler__CounterDataImage__Initialize__Params.html#group__cupti__range__profiler__api_1gac3d8d47120022d012f8182893902db70) [in] Counter data image.

- void *
[CUpti_RangeProfiler_CounterDataImage_Initialize_Params::pPriv](https://docs.nvidia.com/structCUpti__RangeProfiler__CounterDataImage__Initialize__Params.html#group__cupti__range__profiler__api_1ga1368f4ac952ee03fbec20d3d9bcc1c08) [in] Set to NULL.

- CUpti_RangeProfiler_Object *
[CUpti_RangeProfiler_CounterDataImage_Initialize_Params::pRangeProfilerObject](https://docs.nvidia.com/structCUpti__RangeProfiler__CounterDataImage__Initialize__Params.html#group__cupti__range__profiler__api_1ga9b844d59038705bf4fbecd26c66a837b) [in] Periodic sampler object.

- size_t
[CUpti_RangeProfiler_CounterDataImage_Initialize_Params::structSize](https://docs.nvidia.com/structCUpti__RangeProfiler__CounterDataImage__Initialize__Params.html#group__cupti__range__profiler__api_1gafdca529f38105686f872437858f24139) [in] Size of the data structure.

- size_t
[CUpti_RangeProfiler_CounterData_GetRangeInfo_Params::counterDataImageSize](https://docs.nvidia.com/structCUpti__RangeProfiler__CounterData__GetRangeInfo__Params.html#group__cupti__range__profiler__api_1ga8041306b27b4b058ef2443ed79c6568a) [in] Size of the counter data image.

- const uint8_t *
[CUpti_RangeProfiler_CounterData_GetRangeInfo_Params::pCounterDataImage](https://docs.nvidia.com/structCUpti__RangeProfiler__CounterData__GetRangeInfo__Params.html#group__cupti__range__profiler__api_1ga29dc19d5b050d1b99dcfd43e42285dd8) [in] Counter data image.

- void *
[CUpti_RangeProfiler_CounterData_GetRangeInfo_Params::pPriv](https://docs.nvidia.com/structCUpti__RangeProfiler__CounterData__GetRangeInfo__Params.html#group__cupti__range__profiler__api_1ga0f337197fe68930fb2d3c99d6087ff89) [in] Set to NULL.

- const char *
[CUpti_RangeProfiler_CounterData_GetRangeInfo_Params::rangeDelimiter](https://docs.nvidia.com/structCUpti__RangeProfiler__CounterData__GetRangeInfo__Params.html#group__cupti__range__profiler__api_1ga75e306d44f7533b2ba3b0b9ffac8cbc8) [in] range delimiter.

- size_t
[CUpti_RangeProfiler_CounterData_GetRangeInfo_Params::rangeIndex](https://docs.nvidia.com/structCUpti__RangeProfiler__CounterData__GetRangeInfo__Params.html#group__cupti__range__profiler__api_1ga4ff0f6e45ea6f743d1df2657cae683ee) [in] Index of the sample.

- const char *
[CUpti_RangeProfiler_CounterData_GetRangeInfo_Params::rangeName](https://docs.nvidia.com/structCUpti__RangeProfiler__CounterData__GetRangeInfo__Params.html#group__cupti__range__profiler__api_1ga9c48064fa05cdd84371ac1e0631e70ab) [out] RangeName;

- size_t
[CUpti_RangeProfiler_CounterData_GetRangeInfo_Params::structSize](https://docs.nvidia.com/structCUpti__RangeProfiler__CounterData__GetRangeInfo__Params.html#group__cupti__range__profiler__api_1ga4300fe6030920d13613a683b71c6ed0f) [in] Size of the data structure.

- size_t
[CUpti_RangeProfiler_DecodeData_Params::numOfRangeDropped](https://docs.nvidia.com/structCUpti__RangeProfiler__DecodeData__Params.html#group__cupti__range__profiler__api_1gac845a296fb7cc80e8b12eb8e01383590) [out] Number of ranges dropped in the processed passes.

- void *
[CUpti_RangeProfiler_DecodeData_Params::pPriv](https://docs.nvidia.com/structCUpti__RangeProfiler__DecodeData__Params.html#group__cupti__range__profiler__api_1ga3b23e8519bc7dc75456245860f8e77d9) [in] Set to NULL.

- CUpti_RangeProfiler_Object *
[CUpti_RangeProfiler_DecodeData_Params::pRangeProfilerObject](https://docs.nvidia.com/structCUpti__RangeProfiler__DecodeData__Params.html#group__cupti__range__profiler__api_1gaedca8261ba00773c53e81e5e43694c05) [in] Range Profiler Object.

- size_t
[CUpti_RangeProfiler_DecodeData_Params::structSize](https://docs.nvidia.com/structCUpti__RangeProfiler__DecodeData__Params.html#group__cupti__range__profiler__api_1gac9b29940ef0b38cf96b6e40c93072d82) [in] Size of the data structure.

- void *
[CUpti_RangeProfiler_Disable_Params::pPriv](https://docs.nvidia.com/structCUpti__RangeProfiler__Disable__Params.html#group__cupti__range__profiler__api_1ga86a2c9d380149b16e9b2ff9de04d11ff) [in] Set to NULL.

- CUpti_RangeProfiler_Object *
[CUpti_RangeProfiler_Disable_Params::pRangeProfilerObject](https://docs.nvidia.com/structCUpti__RangeProfiler__Disable__Params.html#group__cupti__range__profiler__api_1ga2fc5d90a3682b9513e5151eff6d7f823) [in] Range Profiler Object.

- size_t
[CUpti_RangeProfiler_Disable_Params::structSize](https://docs.nvidia.com/structCUpti__RangeProfiler__Disable__Params.html#group__cupti__range__profiler__api_1ga7421c8b9ea92075a285d4f3ed6a5da94) [in] Size of the data structure.

- CUpti_CacheControl_Mode
[CUpti_RangeProfiler_Enable_Params::cacheControlMode](https://docs.nvidia.com/structCUpti__RangeProfiler__Enable__Params.html#group__cupti__range__profiler__api_1ga847210f2b38b804d8014c2b98b92c512) [in] Cache-control mode. Defaults to CUPTI_CACHE_CONTROL_MODE_NONE for zero-initialized structs.

- CUcontext
[CUpti_RangeProfiler_Enable_Params::ctx](https://docs.nvidia.com/structCUpti__RangeProfiler__Enable__Params.html#group__cupti__range__profiler__api_1ga7a18fdb35efe46ce814d120d593b5f6d) [in] Context to be used for profiling. For green context, users can convert the green context to CUDA context using cuCtxFromGreenCtx and pass the CUDA context to this API.

- void *
[CUpti_RangeProfiler_Enable_Params::pPriv](https://docs.nvidia.com/structCUpti__RangeProfiler__Enable__Params.html#group__cupti__range__profiler__api_1gab5891a5da7ada305a5cd99e37ceeac93) [in] Set to NULL.

- CUpti_RangeProfiler_Object *
[CUpti_RangeProfiler_Enable_Params::pRangeProfilerObject](https://docs.nvidia.com/structCUpti__RangeProfiler__Enable__Params.html#group__cupti__range__profiler__api_1ga37bc40b5b69bce2c0ce7e71cc5da4eea) [out] Range Profiler Object.

- size_t
[CUpti_RangeProfiler_Enable_Params::structSize](https://docs.nvidia.com/structCUpti__RangeProfiler__Enable__Params.html#group__cupti__range__profiler__api_1ga8c1832bf0b6e0e21b717a91ce0a81b9e) [in] Size of the data structure.

- size_t
[CUpti_RangeProfiler_GetCounterDataInfo_Params::counterDataImageSize](https://docs.nvidia.com/structCUpti__RangeProfiler__GetCounterDataInfo__Params.html#group__cupti__range__profiler__api_1ga8452238bbaeb986570caadbacb898731) [in] Size of the counter data image.

- size_t
[CUpti_RangeProfiler_GetCounterDataInfo_Params::numTotalRanges](https://docs.nvidia.com/structCUpti__RangeProfiler__GetCounterDataInfo__Params.html#group__cupti__range__profiler__api_1ga2add79360bc9b38beb82489c3a24c5ca) [out] Number of ranges in the counter data image.

- const uint8_t *
[CUpti_RangeProfiler_GetCounterDataInfo_Params::pCounterDataImage](https://docs.nvidia.com/structCUpti__RangeProfiler__GetCounterDataInfo__Params.html#group__cupti__range__profiler__api_1ga4fbf569b5f025323e6582da90356d2ee) [in] Counter data image.

- void *
[CUpti_RangeProfiler_GetCounterDataInfo_Params::pPriv](https://docs.nvidia.com/structCUpti__RangeProfiler__GetCounterDataInfo__Params.html#group__cupti__range__profiler__api_1gacf912cc745637f04b96568c3d0a3545d) [in] Set to NULL.

- size_t
[CUpti_RangeProfiler_GetCounterDataInfo_Params::structSize](https://docs.nvidia.com/structCUpti__RangeProfiler__GetCounterDataInfo__Params.html#group__cupti__range__profiler__api_1ga42e4d3406a7de18a71a3b277bf8d0b54) [in] Size of the data structure.

- size_t
[CUpti_RangeProfiler_GetCounterDataSize_Params::counterDataSize](https://docs.nvidia.com/structCUpti__RangeProfiler__GetCounterDataSize__Params.html#group__cupti__range__profiler__api_1gab50ff8781c882eee147020596dd3c7b9) [out] Size of the counter data image.

- size_t
[CUpti_RangeProfiler_GetCounterDataSize_Params::maxNumOfRanges](https://docs.nvidia.com/structCUpti__RangeProfiler__GetCounterDataSize__Params.html#group__cupti__range__profiler__api_1ga3c410a612233e4d9c7e3584ad1fac8c5) [in] Maximum number of ranges to be stored in the counter data image.

- uint32_t
[CUpti_RangeProfiler_GetCounterDataSize_Params::maxNumRangeTreeNodes](https://docs.nvidia.com/structCUpti__RangeProfiler__GetCounterDataSize__Params.html#group__cupti__range__profiler__api_1ga89f3373e6f852f45d0f2a698c3bccc83) [in] Maximum number of RangeTree nodes; must be >= maxNumOfRanges

- size_t
[CUpti_RangeProfiler_GetCounterDataSize_Params::numMetrics](https://docs.nvidia.com/structCUpti__RangeProfiler__GetCounterDataSize__Params.html#group__cupti__range__profiler__api_1ga87b89bb8216415cd987abf662bb567ae) [in] Number of metrics to be collected.

- const char **
[CUpti_RangeProfiler_GetCounterDataSize_Params::pMetricNames](https://docs.nvidia.com/structCUpti__RangeProfiler__GetCounterDataSize__Params.html#group__cupti__range__profiler__api_1gab1407455abc5b9b17f080e90540281db) [in] Names of the metrics to be collected.

- void *
[CUpti_RangeProfiler_GetCounterDataSize_Params::pPriv](https://docs.nvidia.com/structCUpti__RangeProfiler__GetCounterDataSize__Params.html#group__cupti__range__profiler__api_1ga519ca98c5681f8362e9e29abf103f861) [in] Set to NULL.

- CUpti_RangeProfiler_Object *
[CUpti_RangeProfiler_GetCounterDataSize_Params::pRangeProfilerObject](https://docs.nvidia.com/structCUpti__RangeProfiler__GetCounterDataSize__Params.html#group__cupti__range__profiler__api_1ga676472eb7738b1cf9ae0180d99052550) [in] Periodic sampler object.

- size_t
[CUpti_RangeProfiler_GetCounterDataSize_Params::structSize](https://docs.nvidia.com/structCUpti__RangeProfiler__GetCounterDataSize__Params.html#group__cupti__range__profiler__api_1ga89d081c33aa7a81cc0bf8af9bea27762) [in] Size of the data structure.

- size_t
[CUpti_RangeProfiler_GetDevicePartitionInfo_Params::devicePartitionInfoSize](https://docs.nvidia.com/structCUpti__RangeProfiler__GetDevicePartitionInfo__Params.html#group__cupti__range__profiler__api_1gadd80775912397fc56cc9d99d6deff17a) [inout] If

`pDevicePartitionInfo`

is NULL, then the required buffer size is returned in`devicePartitionInfoSize`

. Otherwise,`devicePartitionInfoSize`

should be set to the allocated buffer size of`pDevicePartitionInfo`

.- uint8_t *
[CUpti_RangeProfiler_GetDevicePartitionInfo_Params::pDevicePartitionInfo](https://docs.nvidia.com/structCUpti__RangeProfiler__GetDevicePartitionInfo__Params.html#group__cupti__range__profiler__api_1ga66ef9b09e6aa66f04781d63d81c56f4f) [inout] Buffer to store the device partition information. Set to NULL in the first call to query the required buffer size. In the second call, pass an allocated buffer of size

`devicePartitionInfoSize`

to receive the partition information encoding the SM resource allocation for the Green Context.- void *
[CUpti_RangeProfiler_GetDevicePartitionInfo_Params::pPriv](https://docs.nvidia.com/structCUpti__RangeProfiler__GetDevicePartitionInfo__Params.html#group__cupti__range__profiler__api_1ga6649cd80cb7d398481c7f444aec9f30e) [in] Set to NULL.

- CUpti_RangeProfiler_Object *
[CUpti_RangeProfiler_GetDevicePartitionInfo_Params::pRangeProfilerObject](https://docs.nvidia.com/structCUpti__RangeProfiler__GetDevicePartitionInfo__Params.html#group__cupti__range__profiler__api_1ga887fbfb3afdd0c75b22da290c84d7f2e) [in] Range profiler object created via cuptiRangeProfilerEnable on a Green Context.

- size_t
[CUpti_RangeProfiler_GetDevicePartitionInfo_Params::structSize](https://docs.nvidia.com/structCUpti__RangeProfiler__GetDevicePartitionInfo__Params.html#group__cupti__range__profiler__api_1ga529a4d4e482fcc18afb0119ea341aeb3) [in] Size of the data structure.

- void *
[CUpti_RangeProfiler_PopRange_Params::pPriv](https://docs.nvidia.com/structCUpti__RangeProfiler__PopRange__Params.html#group__cupti__range__profiler__api_1gac5ed09dc655241c74fd9f420edd74dd4) [in] Set to NULL.

- CUpti_RangeProfiler_Object *
[CUpti_RangeProfiler_PopRange_Params::pRangeProfilerObject](https://docs.nvidia.com/structCUpti__RangeProfiler__PopRange__Params.html#group__cupti__range__profiler__api_1gab50d8339a4888f766374f3587bc393a6) [in] Range Profiler Object.

- size_t
[CUpti_RangeProfiler_PopRange_Params::structSize](https://docs.nvidia.com/structCUpti__RangeProfiler__PopRange__Params.html#group__cupti__range__profiler__api_1ga3d89d097eb893ab92083844a4180bd33) [in] Size of the data structure.

- void *
[CUpti_RangeProfiler_PushRange_Params::pPriv](https://docs.nvidia.com/structCUpti__RangeProfiler__PushRange__Params.html#group__cupti__range__profiler__api_1ga374f1d6ea45cf8d1e4bcd159b2347014) [in] Set to NULL.

- const char *
[CUpti_RangeProfiler_PushRange_Params::pRangeName](https://docs.nvidia.com/structCUpti__RangeProfiler__PushRange__Params.html#group__cupti__range__profiler__api_1ga613933c1ee227b269f0455eb8a313311) [in] Name of the range to be profiled (only valid for User range mode).

- CUpti_RangeProfiler_Object *
[CUpti_RangeProfiler_PushRange_Params::pRangeProfilerObject](https://docs.nvidia.com/structCUpti__RangeProfiler__PushRange__Params.html#group__cupti__range__profiler__api_1gaad27da303b73f6144fbb5d900a6f9f09) [in] Range Profiler Object.

- size_t
[CUpti_RangeProfiler_PushRange_Params::structSize](https://docs.nvidia.com/structCUpti__RangeProfiler__PushRange__Params.html#group__cupti__range__profiler__api_1gaa0f62f1a20e2cafb1e7a9b733ec45703) [in] Size of the data structure.

- size_t
[CUpti_RangeProfiler_SetConfig_Params::configSize](https://docs.nvidia.com/structCUpti__RangeProfiler__SetConfig__Params.html#group__cupti__range__profiler__api_1ga3e348cbc7b8ba5decb74d5f056ee1091) [in] Size of the config image.

- size_t
[CUpti_RangeProfiler_SetConfig_Params::counterDataImageSize](https://docs.nvidia.com/structCUpti__RangeProfiler__SetConfig__Params.html#group__cupti__range__profiler__api_1ga14a831019118b31889b355fa5d243801) [in] Size of the counter data image.

- size_t
[CUpti_RangeProfiler_SetConfig_Params::maxRangesPerPass](https://docs.nvidia.com/structCUpti__RangeProfiler__SetConfig__Params.html#group__cupti__range__profiler__api_1ga55cdd497ed7664af548c75cb2a8284a2) [in] Maximum number of ranges that can be profiled in a pass.

- uint16_t
[CUpti_RangeProfiler_SetConfig_Params::minNestingLevel](https://docs.nvidia.com/structCUpti__RangeProfiler__SetConfig__Params.html#group__cupti__range__profiler__api_1gaf8c400b93c279be74455a2f8aae66c8e) [in] minimum nesting level to be profiled.

- uint16_t
[CUpti_RangeProfiler_SetConfig_Params::numNestingLevels](https://docs.nvidia.com/structCUpti__RangeProfiler__SetConfig__Params.html#group__cupti__range__profiler__api_1ga667ba0af505cb76470c6b6dcb838df53) [in] number of nesting level to be profiled. For Auto range mode, this should be set to 1.

- const uint8_t *
[CUpti_RangeProfiler_SetConfig_Params::pConfig](https://docs.nvidia.com/structCUpti__RangeProfiler__SetConfig__Params.html#group__cupti__range__profiler__api_1gafc6d788eebcd7940cdd64fef8a83af64) [in] Config image.

- uint8_t *
[CUpti_RangeProfiler_SetConfig_Params::pCounterDataImage](https://docs.nvidia.com/structCUpti__RangeProfiler__SetConfig__Params.html#group__cupti__range__profiler__api_1ga5c623c9a9ad64dc150c0344b63457da1) [in] Counter data image.

- void *
[CUpti_RangeProfiler_SetConfig_Params::pPriv](https://docs.nvidia.com/structCUpti__RangeProfiler__SetConfig__Params.html#group__cupti__range__profiler__api_1gaee9490e61e663783e8903d622b7961c4) [in] Set to NULL.

- CUpti_RangeProfiler_Object *
[CUpti_RangeProfiler_SetConfig_Params::pRangeProfilerObject](https://docs.nvidia.com/structCUpti__RangeProfiler__SetConfig__Params.html#group__cupti__range__profiler__api_1ga6fa9bb4d40c4b5a4921ecf9e749244b2) [in] Range Profiler Object.

- size_t
[CUpti_RangeProfiler_SetConfig_Params::passIndex](https://docs.nvidia.com/structCUpti__RangeProfiler__SetConfig__Params.html#group__cupti__range__profiler__api_1ga7f5fa82b24fce407ba0f3e786bbc12ee) [in] Pass index for the replay session.

- CUpti_ProfilerRange
[CUpti_RangeProfiler_SetConfig_Params::range](https://docs.nvidia.com/structCUpti__RangeProfiler__SetConfig__Params.html#group__cupti__range__profiler__api_1gabb8fbb27546b3cc3f002272ec5e9b592) [in] Profiling Range mode.

- CUpti_ProfilerReplayMode
[CUpti_RangeProfiler_SetConfig_Params::replayMode](https://docs.nvidia.com/structCUpti__RangeProfiler__SetConfig__Params.html#group__cupti__range__profiler__api_1ga8200339927bc146a33faaf998e170c5f) [in] Replay mode.

- size_t
[CUpti_RangeProfiler_SetConfig_Params::structSize](https://docs.nvidia.com/structCUpti__RangeProfiler__SetConfig__Params.html#group__cupti__range__profiler__api_1ga29a60c6ec5c370fcded6ae0cefd71184) [in] Size of the data structure.

- uint16_t
[CUpti_RangeProfiler_SetConfig_Params::targetNestingLevel](https://docs.nvidia.com/structCUpti__RangeProfiler__SetConfig__Params.html#group__cupti__range__profiler__api_1gab1412c0987906032f40db58b7f84d992) [in] Target nesting level for the replay session.

- void *
[CUpti_RangeProfiler_Start_Params::pPriv](https://docs.nvidia.com/structCUpti__RangeProfiler__Start__Params.html#group__cupti__range__profiler__api_1gac45fc2c99f9804a742e60d977288ec67) [in] Set to NULL.

- CUpti_RangeProfiler_Object *
[CUpti_RangeProfiler_Start_Params::pRangeProfilerObject](https://docs.nvidia.com/structCUpti__RangeProfiler__Start__Params.html#group__cupti__range__profiler__api_1ga390dc0e01e173f3f064d5caf4982fa4f) [in] Range Profiler Object.

- size_t
[CUpti_RangeProfiler_Start_Params::structSize](https://docs.nvidia.com/structCUpti__RangeProfiler__Start__Params.html#group__cupti__range__profiler__api_1gaf1ff22bb568401284f5bbf54e84e891a) [in] Size of the data structure.

- uint8_t
[CUpti_RangeProfiler_Stop_Params::isAllPassSubmitted](https://docs.nvidia.com/structCUpti__RangeProfiler__Stop__Params.html#group__cupti__range__profiler__api_1gaa743861c117b2829c1a62ed3bc9d88cb) [out] 1 if all passes are submitted to GPU for collection, 0 otherwise.

- void *
[CUpti_RangeProfiler_Stop_Params::pPriv](https://docs.nvidia.com/structCUpti__RangeProfiler__Stop__Params.html#group__cupti__range__profiler__api_1ga0c7fa56b173998b89f435d8bfea89fe5) [in] Set to NULL.

- CUpti_RangeProfiler_Object *
[CUpti_RangeProfiler_Stop_Params::pRangeProfilerObject](https://docs.nvidia.com/structCUpti__RangeProfiler__Stop__Params.html#group__cupti__range__profiler__api_1gaf865e36991d9793c5ae6228d46234536) [in] Range Profiler Object.

- size_t
[CUpti_RangeProfiler_Stop_Params::passIndex](https://docs.nvidia.com/structCUpti__RangeProfiler__Stop__Params.html#group__cupti__range__profiler__api_1gaadc3cfcf036043a5efc8e844b0edf226) [out] pass index for the replay session.

- size_t
[CUpti_RangeProfiler_Stop_Params::structSize](https://docs.nvidia.com/structCUpti__RangeProfiler__Stop__Params.html#group__cupti__range__profiler__api_1gafe667406164c367515d6f1ed22917d60) [in] Size of the data structure.

- size_t
[CUpti_RangeProfiler_Stop_Params::targetNestingLevel](https://docs.nvidia.com/structCUpti__RangeProfiler__Stop__Params.html#group__cupti__range__profiler__api_1ga9ac20d88a8af57f475cfc0d3acf1e5d1) [out] target nesting level for the replay session.


## 6.10.7. Macros[#](https://docs.nvidia.com#id1)

-
CUpti_RangeProfiler_CounterDataImage_Initialize_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_RangeProfiler_CounterDataImage_Initialize_Params_STRUCT_SIZE)

-
CUpti_RangeProfiler_CounterData_GetRangeInfo_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_RangeProfiler_CounterData_GetRangeInfo_Params_STRUCT_SIZE)

-
CUpti_RangeProfiler_DecodeData_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_RangeProfiler_DecodeData_Params_STRUCT_SIZE)

-
CUpti_RangeProfiler_Disable_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_RangeProfiler_Disable_Params_STRUCT_SIZE)

-
CUpti_RangeProfiler_Enable_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_RangeProfiler_Enable_Params_STRUCT_SIZE)

-
CUpti_RangeProfiler_GetCounterDataInfo_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_RangeProfiler_GetCounterDataInfo_Params_STRUCT_SIZE)

-
CUpti_RangeProfiler_GetCounterDataSize_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_RangeProfiler_GetCounterDataSize_Params_STRUCT_SIZE)

-
CUpti_RangeProfiler_GetDevicePartitionInfo_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_RangeProfiler_GetDevicePartitionInfo_Params_STRUCT_SIZE)

-
CUpti_RangeProfiler_PopRange_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_RangeProfiler_PopRange_Params_STRUCT_SIZE)

-
CUpti_RangeProfiler_PushRange_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_RangeProfiler_PushRange_Params_STRUCT_SIZE)

-
CUpti_RangeProfiler_SetConfig_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_RangeProfiler_SetConfig_Params_STRUCT_SIZE)

-
CUpti_RangeProfiler_Start_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_RangeProfiler_Start_Params_STRUCT_SIZE)

-
CUpti_RangeProfiler_Stop_Params_STRUCT_SIZE
[#](https://docs.nvidia.com#c.CUpti_RangeProfiler_Stop_Params_STRUCT_SIZE)

## 6.10.8. Enumerations[#](https://docs.nvidia.com#id2)

-
enum CUpti_CacheControl_Mode
[#](https://docs.nvidia.com#_CPPv423CUpti_CacheControl_Mode) Cache control modes for Range Profiler replay passes.

Cache control resets supported GPU cache state before each profiling pass so replayed passes start from comparable cache state. The default is NONE so zero-initialized enable parameters preserve previous behavior.

Currently, L2 cache state is supported.

**Since**CUDA 13.4


*Values:*-
enumerator CUPTI_CACHE_CONTROL_MODE_NONE
[#](https://docs.nvidia.com#_CPPv4N23CUpti_CacheControl_Mode29CUPTI_CACHE_CONTROL_MODE_NONEE) Disable cache control.

Replay passes may observe cache state from earlier passes, matching behavior before this field was added.


-
enumerator CUPTI_CACHE_CONTROL_MODE_ALL
[#](https://docs.nvidia.com#_CPPv4N23CUpti_CacheControl_Mode28CUPTI_CACHE_CONTROL_MODE_ALLE) Reset all cache state supported by this CUPTI version before each pass.

Currently, this resets supported L2 cache state.


-
enumerator CUPTI_CACHE_CONTROL_MODE_L2
[#](https://docs.nvidia.com#_CPPv4N23CUpti_CacheControl_Mode27CUPTI_CACHE_CONTROL_MODE_L2E) Reset supported L2 cache state before each pass.


-
enumerator CUPTI_CACHE_CONTROL_MODE_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N23CUpti_CacheControl_Mode34CUPTI_CACHE_CONTROL_MODE_FORCE_INTE)


## 6.10.9. Functions[#](https://docs.nvidia.com#id3)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiRangeProfilerCounterDataGetRangeInfo(
) Get the range name for the given range index.

- Parameters:
**pParams**– A pointer to[CUpti_RangeProfiler_CounterData_GetRangeInfo_Params](https://docs.nvidia.com/structCUpti__RangeProfiler__CounterData__GetRangeInfo__Params.html#structcupti__rangeprofiler__counterdata__getrangeinfo__params)- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if any`pParams`

is not valid**CUPTI_ERROR_UNKNOWN**– for any internal error



[#](https://docs.nvidia.com#_CPPv441cuptiRangeProfilerCounterDataGetRangeInfoP51CUpti_RangeProfiler_CounterData_GetRangeInfo_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiRangeProfilerCounterDataImageInitialize(
) Initialize the counter data image with the profiling data for the ranges profiled.

- Parameters:
**pParams**– A pointer to[CUpti_RangeProfiler_CounterDataImage_Initialize_Params](https://docs.nvidia.com/structCUpti__RangeProfiler__CounterDataImage__Initialize__Params.html#structcupti__rangeprofiler__counterdataimage__initialize__params)- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if any`pParams`

is not valid**CUPTI_ERROR_INVALID_OPERATION**– if range profiler CounterDataImageInitialize is called without enabling range profiler**CUPTI_ERROR_UNKNOWN**– for any internal error



[#](https://docs.nvidia.com#_CPPv444cuptiRangeProfilerCounterDataImageInitializeP54CUpti_RangeProfiler_CounterDataImage_Initialize_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiRangeProfilerDecodeData( ,[CUpti_RangeProfiler_DecodeData_Params](https://docs.nvidia.com/structCUpti__RangeProfiler__DecodeData__Params.html#_CPPv437CUpti_RangeProfiler_DecodeData_Params)*pParamsDecode the profiling data stored in the hardware to the counter data image passed in the SetConfig API.

This API should be called after cuptiRangeProfilerStop. The counter data image will be updated with the profiling data for the ranges profiled.

For the cases where the number of ranges counter data image can store is less than the number of ranges profiled (= maxRangesPerPass in SetConfig API), the counter data image will report dropped ranges.

- Parameters:
**pParams**– A pointer to[CUpti_RangeProfiler_DecodeData_Params](https://docs.nvidia.com/structCUpti__RangeProfiler__DecodeData__Params.html#structcupti__rangeprofiler__decodedata__params)- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if any`pParams`

is not valid**CUPTI_ERROR_INVALID_OPERATION**– if range profiler DecodeData is called without enabling range profiler**CUPTI_ERROR_UNKNOWN**– for any internal error



[#](https://docs.nvidia.com#_CPPv428cuptiRangeProfilerDecodeDataP37CUpti_RangeProfiler_DecodeData_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiRangeProfilerDisable( ,[CUpti_RangeProfiler_Disable_Params](https://docs.nvidia.com/structCUpti__RangeProfiler__Disable__Params.html#_CPPv434CUpti_RangeProfiler_Disable_Params)*pParamsDisable the range profiler on the CUDA context and destroy the range profiler object.

- Parameters:
**pParams**– A pointer to[CUpti_RangeProfiler_Disable_Params](https://docs.nvidia.com/structCUpti__RangeProfiler__Disable__Params.html#structcupti__rangeprofiler__disable__params)- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if any`pParams`

is not valid



[#](https://docs.nvidia.com#_CPPv425cuptiRangeProfilerDisableP34CUpti_RangeProfiler_Disable_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiRangeProfilerEnable( ,[CUpti_RangeProfiler_Enable_Params](https://docs.nvidia.com/structCUpti__RangeProfiler__Enable__Params.html#_CPPv433CUpti_RangeProfiler_Enable_Params)*pParamsCreate a range profiler object and enable range profiling on the CUDA context.

- Parameters:
**pParams**– A pointer to[CUpti_RangeProfiler_Enable_Params](https://docs.nvidia.com/structCUpti__RangeProfiler__Enable__Params.html#structcupti__rangeprofiler__enable__params)- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if any`pParams`

is not valid**CUPTI_ERROR_OUT_OF_MEMORY**– if memory allocation fails while creating the Range Profiler object or cache-control resources**CUPTI_ERROR_INSUFFICIENT_PRIVILEGES**– if the user does not have sufficient privileges to perform the operation**CUPTI_ERROR_UNKNOWN**– for any internal error



[#](https://docs.nvidia.com#_CPPv424cuptiRangeProfilerEnableP33CUpti_RangeProfiler_Enable_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiRangeProfilerGetCounterDataInfo(
) Get the number of ranges stored in the counter data image.

- Parameters:
**pParams**– A pointer to[CUpti_RangeProfiler_GetCounterDataInfo_Params](https://docs.nvidia.com/structCUpti__RangeProfiler__GetCounterDataInfo__Params.html#structcupti__rangeprofiler__getcounterdatainfo__params)- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if any`pParams`

is not valid**CUPTI_ERROR_UNKNOWN**– for any internal error



[#](https://docs.nvidia.com#_CPPv436cuptiRangeProfilerGetCounterDataInfoP45CUpti_RangeProfiler_GetCounterDataInfo_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiRangeProfilerGetCounterDataSize(
) Get the size of the counter data image required to store the profiling data for the ranges profiled.

- Parameters:
**pParams**– A pointer to[CUpti_RangeProfiler_GetCounterDataSize_Params](https://docs.nvidia.com/structCUpti__RangeProfiler__GetCounterDataSize__Params.html#structcupti__rangeprofiler__getcounterdatasize__params)- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if any`pParams`

is not valid**CUPTI_ERROR_INVALID_OPERATION**– if range profiler GetCounterDataSize is called without enabling range profiler**CUPTI_ERROR_UNKNOWN**– for any internal error



[#](https://docs.nvidia.com#_CPPv436cuptiRangeProfilerGetCounterDataSizeP45CUpti_RangeProfiler_GetCounterDataSize_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiRangeProfilerGetDevicePartitionInfo(
) Get the device partition information for a Green Context.

Green Contexts are created by partitioning device resources such as Streaming Multiprocessors (SMs) using CUDA APIs like cuDevSmResourceSplitByCount and cuGreenCtxCreate. When range profiling is enabled on a Green Context, the device partition information encodes how the device resources are divided among the Green Contexts.

This API retrieves the device partition information from the range profiler object, which is required for accurate metric evaluation on the host side. The retrieved partition information should be passed to

[cuptiProfilerHostSetDevicePartitionInfo](https://docs.nvidia.com/group__CUPTI__PROFILER__HOST__API.html#group__cupti__profiler__host__api_1gae2acff2140fd3cdfbd91f47b8db1c1b8)before evaluating metrics using[cuptiProfilerHostEvaluateToGpuValues](https://docs.nvidia.com/group__CUPTI__PROFILER__HOST__API.html#group__cupti__profiler__host__api_1ga388a983e8bcfc889721c17aae2e67a4f). This API needs to be called after[cuptiRangeProfilerStart](https://docs.nvidia.com#group__cupti__range__profiler__api_1gaae839f931a50f1436df35367e3e71416).This is a two-phase function:

First call: Set

`pDevicePartitionInfo`

to NULL to query the required buffer size. The required size is returned in`devicePartitionInfoSize`

.Second call: Allocate a buffer of the returned size and set

`pDevicePartitionInfo`

to point to it. Set`devicePartitionInfoSize`

to the allocated buffer size. The function populates the buffer with the device partition information.

- Parameters:
**pParams**– A pointer to[CUpti_RangeProfiler_GetDevicePartitionInfo_Params](https://docs.nvidia.com/structCUpti__RangeProfiler__GetDevicePartitionInfo__Params.html#structcupti__rangeprofiler__getdevicepartitioninfo__params)- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if any`pParams`

is not valid**CUPTI_ERROR_UNKNOWN**– for any internal error



[#](https://docs.nvidia.com#_CPPv440cuptiRangeProfilerGetDevicePartitionInfoP49CUpti_RangeProfiler_GetDevicePartitionInfo_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiRangeProfilerPopRange( ,[CUpti_RangeProfiler_PopRange_Params](https://docs.nvidia.com/structCUpti__RangeProfiler__PopRange__Params.html#_CPPv435CUpti_RangeProfiler_PopRange_Params)*pParamspop the current range to the Range Profiler.

The number of pop range API call should be same as number of push ranges in the same order.

- Parameters:
**pParams**– A pointer to[CUpti_RangeProfiler_PopRange_Params](https://docs.nvidia.com/structCUpti__RangeProfiler__PopRange__Params.html#structcupti__rangeprofiler__poprange__params)- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if any`pParams`

is not valid**CUPTI_ERROR_INVALID_OPERATION**– if range profiler PopRange is called without enabling range profiler**CUPTI_ERROR_UNKNOWN**– for any internal error



[#](https://docs.nvidia.com#_CPPv426cuptiRangeProfilerPopRangeP35CUpti_RangeProfiler_PopRange_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiRangeProfilerPushRange( ,[CUpti_RangeProfiler_PushRange_Params](https://docs.nvidia.com/structCUpti__RangeProfiler__PushRange__Params.html#_CPPv436CUpti_RangeProfiler_PushRange_Params)*pParamsAdd a new range to the Range Profiler with a given range name.

For nested ranges, this API should be called again for the innermost range. For profiling the nested range, users need to set the values for minNestingLevel and numNestingLevels in the SetConfig API.

- Parameters:
**pParams**– A pointer to[CUpti_RangeProfiler_PushRange_Params](https://docs.nvidia.com/structCUpti__RangeProfiler__PushRange__Params.html#structcupti__rangeprofiler__pushrange__params)- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if any`pParams`

is not valid**CUPTI_ERROR_INVALID_OPERATION**– if range profiler PushRange is called without enabling range profiler**CUPTI_ERROR_UNKNOWN**– for any internal error



[#](https://docs.nvidia.com#_CPPv427cuptiRangeProfilerPushRangeP36CUpti_RangeProfiler_PushRange_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiRangeProfilerSetConfig( ,[CUpti_RangeProfiler_SetConfig_Params](https://docs.nvidia.com/structCUpti__RangeProfiler__SetConfig__Params.html#_CPPv436CUpti_RangeProfiler_SetConfig_Params)*pParamsSet the configuration for range profiler like maximum number of ranges per pass, number of nesting levels, range and replay mode and the config image which has scheduling info for metric collection.

- Parameters:
**pParams**– A pointer to[CUpti_RangeProfiler_SetConfig_Params](https://docs.nvidia.com/structCUpti__RangeProfiler__SetConfig__Params.html#structcupti__rangeprofiler__setconfig__params)- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if any`pParams`

is not valid



[#](https://docs.nvidia.com#_CPPv427cuptiRangeProfilerSetConfigP36CUpti_RangeProfiler_SetConfig_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiRangeProfilerStart( ,[CUpti_RangeProfiler_Start_Params](https://docs.nvidia.com/structCUpti__RangeProfiler__Start__Params.html#_CPPv432CUpti_RangeProfiler_Start_Params)*pParamsStart the range profiler.

- Parameters:
**pParams**– A pointer to[CUpti_RangeProfiler_Start_Params](https://docs.nvidia.com/structCUpti__RangeProfiler__Start__Params.html#structcupti__rangeprofiler__start__params)- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if any`pParams`

is not valid**CUPTI_ERROR_INVALID_OPERATION**– if range profiler Start is called without enabling range profiler**CUPTI_ERROR_UNKNOWN**– for any internal error



[#](https://docs.nvidia.com#_CPPv423cuptiRangeProfilerStartP32CUpti_RangeProfiler_Start_Params)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiRangeProfilerStop( ,[CUpti_RangeProfiler_Stop_Params](https://docs.nvidia.com/structCUpti__RangeProfiler__Stop__Params.html#_CPPv431CUpti_RangeProfiler_Stop_Params)*pParamsStop the range profiler.

- Parameters:
**pParams**– A pointer to[CUpti_RangeProfiler_Stop_Params](https://docs.nvidia.com/structCUpti__RangeProfiler__Stop__Params.html#structcupti__rangeprofiler__stop__params)- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– if any`pParams`

is not valid**CUPTI_ERROR_INVALID_OPERATION**– if range profiler Stop is called without enabling range profiler**CUPTI_ERROR_UNKNOWN**– for any internal error



[#](https://docs.nvidia.com#_CPPv422cuptiRangeProfilerStopP31CUpti_RangeProfiler_Stop_Params)

## 6.10.10. Typedefs[#](https://docs.nvidia.com#id4)

-
typedef struct
[CUpti_RangeProfiler_Object](https://docs.nvidia.com#_CPPv426CUpti_RangeProfiler_Object)CUpti_RangeProfiler_Object[#](https://docs.nvidia.com#_CPPv426CUpti_RangeProfiler_Object)