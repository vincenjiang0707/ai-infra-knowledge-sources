source: https://docs.nvidia.com/cupti/api/structCUpti__Profiler__CounterDataImageOptions.html

# 7.168. CUpti_Profiler_CounterDataImageOptions[#](https://docs.nvidia.com#cupti-profiler-counterdataimageoptions)

-
struct CUpti_Profiler_CounterDataImageOptions
[#](https://docs.nvidia.com#_CPPv438CUpti_Profiler_CounterDataImageOptions) Input parameter to define the counterDataImage.

Public Members

-
size_t structSize
[#](https://docs.nvidia.com#_CPPv4N38CUpti_Profiler_CounterDataImageOptions10structSizeE) [in] CUpti_Profiler_CounterDataImageOptions_Params_STRUCT_SIZE


-
void *pPriv
[#](https://docs.nvidia.com#_CPPv4N38CUpti_Profiler_CounterDataImageOptions5pPrivE) [in] assign to NULL


-
const uint8_t *pCounterDataPrefix
[#](https://docs.nvidia.com#_CPPv4N38CUpti_Profiler_CounterDataImageOptions18pCounterDataPrefixE) [in] Address of CounterDataPrefix generated from NVPW_CounterDataBuilder_GetCounterDataPrefix().

Must be align(8).


-
size_t counterDataPrefixSize
[#](https://docs.nvidia.com#_CPPv4N38CUpti_Profiler_CounterDataImageOptions21counterDataPrefixSizeE) [in] Size of CounterDataPrefix generated from NVPW_CounterDataBuilder_GetCounterDataPrefix().


-
uint32_t maxNumRanges
[#](https://docs.nvidia.com#_CPPv4N38CUpti_Profiler_CounterDataImageOptions12maxNumRangesE) [in] Maximum number of ranges that can be profiled


-
uint32_t maxNumRangeTreeNodes
[#](https://docs.nvidia.com#_CPPv4N38CUpti_Profiler_CounterDataImageOptions20maxNumRangeTreeNodesE) [in] Maximum number of RangeTree nodes; must be >= maxNumRanges


-
uint32_t maxRangeNameLength
[#](https://docs.nvidia.com#_CPPv4N38CUpti_Profiler_CounterDataImageOptions18maxRangeNameLengthE) [in] Maximum string length of each RangeName, including the trailing NULL character


-
size_t structSize