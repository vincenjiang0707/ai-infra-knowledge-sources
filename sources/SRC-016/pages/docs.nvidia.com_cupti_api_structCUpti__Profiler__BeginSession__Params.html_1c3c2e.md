source: https://docs.nvidia.com/cupti/api/structCUpti__Profiler__BeginSession__Params.html

# 7.167. CUpti_Profiler_BeginSession_Params[#](https://docs.nvidia.com#cupti-profiler-beginsession-params)

-
struct CUpti_Profiler_BeginSession_Params
[#](https://docs.nvidia.com#_CPPv434CUpti_Profiler_BeginSession_Params) Params for cuptiProfilerBeginSession.

Public Members

-
size_t structSize
[#](https://docs.nvidia.com#_CPPv4N34CUpti_Profiler_BeginSession_Params10structSizeE) [in] CUpti_Profiler_BeginSession_Params_STRUCT_SIZE


-
void *pPriv
[#](https://docs.nvidia.com#_CPPv4N34CUpti_Profiler_BeginSession_Params5pPrivE) [in] assign to NULL


-
CUcontext ctx
[#](https://docs.nvidia.com#_CPPv4N34CUpti_Profiler_BeginSession_Params3ctxE) [in] if NULL, the current CUcontext is used


-
size_t counterDataImageSize
[#](https://docs.nvidia.com#_CPPv4N34CUpti_Profiler_BeginSession_Params20counterDataImageSizeE) [in] size calculated from cuptiProfilerCounterDataImageCalculateSize


-
uint8_t *pCounterDataImage
[#](https://docs.nvidia.com#_CPPv4N34CUpti_Profiler_BeginSession_Params17pCounterDataImageE) [in] address of CounterDataImage


-
size_t counterDataScratchBufferSize
[#](https://docs.nvidia.com#_CPPv4N34CUpti_Profiler_BeginSession_Params28counterDataScratchBufferSizeE) [in] size calculated from cuptiProfilerCounterDataImageInitializeScratchBuffer


-
uint8_t *pCounterDataScratchBuffer
[#](https://docs.nvidia.com#_CPPv4N34CUpti_Profiler_BeginSession_Params25pCounterDataScratchBufferE) [in] address of CounterDataImage scratch buffer


-
uint8_t bDumpCounterDataInFile
[#](https://docs.nvidia.com#_CPPv4N34CUpti_Profiler_BeginSession_Params22bDumpCounterDataInFileE) [in] [optional]


-
const char *pCounterDataFilePath
[#](https://docs.nvidia.com#_CPPv4N34CUpti_Profiler_BeginSession_Params20pCounterDataFilePathE) [in] [optional]


-
[CUpti_ProfilerRange](https://docs.nvidia.com/group__CUPTI__PROFILER__API.html#_CPPv419CUpti_ProfilerRange)range[#](https://docs.nvidia.com#_CPPv4N34CUpti_Profiler_BeginSession_Params5rangeE) [in] CUpti_ProfilerRange


-
[CUpti_ProfilerReplayMode](https://docs.nvidia.com/group__CUPTI__PROFILER__API.html#_CPPv424CUpti_ProfilerReplayMode)replayMode[#](https://docs.nvidia.com#_CPPv4N34CUpti_Profiler_BeginSession_Params10replayModeE) [in] CUpti_ProfilerReplayMode


-
size_t maxRangesPerPass
[#](https://docs.nvidia.com#_CPPv4N34CUpti_Profiler_BeginSession_Params16maxRangesPerPassE) [in] Maximum number of ranges that can be recorded in a single pass.


-
size_t maxLaunchesPerPass
[#](https://docs.nvidia.com#_CPPv4N34CUpti_Profiler_BeginSession_Params18maxLaunchesPerPassE) [in] Maximum number of kernel launches that can be recorded in a single pass; must be >= maxRangesPerPass.


-
size_t structSize