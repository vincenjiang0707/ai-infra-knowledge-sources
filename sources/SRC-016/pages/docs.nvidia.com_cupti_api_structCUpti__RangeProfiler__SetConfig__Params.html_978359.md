source: https://docs.nvidia.com/cupti/api/structCUpti__RangeProfiler__SetConfig__Params.html

# 7.213. CUpti_RangeProfiler_SetConfig_Params[#](https://docs.nvidia.com#cupti-rangeprofiler-setconfig-params)

-
struct CUpti_RangeProfiler_SetConfig_Params
[#](https://docs.nvidia.com#_CPPv436CUpti_RangeProfiler_SetConfig_Params) Params for cuptiRangeProfilerSetConfig.

Public Members

-
size_t structSize
[#](https://docs.nvidia.com#_CPPv4N36CUpti_RangeProfiler_SetConfig_Params10structSizeE) [in] Size of the data structure.


-
void *pPriv
[#](https://docs.nvidia.com#_CPPv4N36CUpti_RangeProfiler_SetConfig_Params5pPrivE) [in] Set to NULL.


-
[CUpti_RangeProfiler_Object](https://docs.nvidia.com/group__CUPTI__RANGE__PROFILER__API.html#_CPPv426CUpti_RangeProfiler_Object)*pRangeProfilerObject[#](https://docs.nvidia.com#_CPPv4N36CUpti_RangeProfiler_SetConfig_Params20pRangeProfilerObjectE) [in] Range Profiler Object.


-
size_t configSize
[#](https://docs.nvidia.com#_CPPv4N36CUpti_RangeProfiler_SetConfig_Params10configSizeE) [in] Size of the config image.


-
const uint8_t *pConfig
[#](https://docs.nvidia.com#_CPPv4N36CUpti_RangeProfiler_SetConfig_Params7pConfigE) [in] Config image.


-
size_t counterDataImageSize
[#](https://docs.nvidia.com#_CPPv4N36CUpti_RangeProfiler_SetConfig_Params20counterDataImageSizeE) [in] Size of the counter data image.


-
uint8_t *pCounterDataImage
[#](https://docs.nvidia.com#_CPPv4N36CUpti_RangeProfiler_SetConfig_Params17pCounterDataImageE) [in] Counter data image.


-
[CUpti_ProfilerRange](https://docs.nvidia.com/group__CUPTI__PROFILER__API.html#_CPPv419CUpti_ProfilerRange)range[#](https://docs.nvidia.com#_CPPv4N36CUpti_RangeProfiler_SetConfig_Params5rangeE) [in] Profiling Range mode.


-
[CUpti_ProfilerReplayMode](https://docs.nvidia.com/group__CUPTI__PROFILER__API.html#_CPPv424CUpti_ProfilerReplayMode)replayMode[#](https://docs.nvidia.com#_CPPv4N36CUpti_RangeProfiler_SetConfig_Params10replayModeE) [in] Replay mode.


-
size_t maxRangesPerPass
[#](https://docs.nvidia.com#_CPPv4N36CUpti_RangeProfiler_SetConfig_Params16maxRangesPerPassE) [in] Maximum number of ranges that can be profiled in a pass.


-
uint16_t numNestingLevels
[#](https://docs.nvidia.com#_CPPv4N36CUpti_RangeProfiler_SetConfig_Params16numNestingLevelsE) [in] number of nesting level to be profiled. For Auto range mode, this should be set to 1.


-
uint16_t minNestingLevel
[#](https://docs.nvidia.com#_CPPv4N36CUpti_RangeProfiler_SetConfig_Params15minNestingLevelE) [in] minimum nesting level to be profiled.


-
size_t passIndex
[#](https://docs.nvidia.com#_CPPv4N36CUpti_RangeProfiler_SetConfig_Params9passIndexE) [in] Pass index for the replay session.


-
uint16_t targetNestingLevel
[#](https://docs.nvidia.com#_CPPv4N36CUpti_RangeProfiler_SetConfig_Params18targetNestingLevelE) [in] Target nesting level for the replay session.


-
size_t structSize