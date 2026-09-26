source: https://docs.nvidia.com/cupti/api/structCUpti__Profiler__CounterDataImage__InitializeScratchBuffer__Params.html

# 7.171. CUpti_Profiler_CounterDataImage_InitializeScratchBuffer_Params[#](https://docs.nvidia.com#cupti-profiler-counterdataimage-initializescratchbuffer-params)

-
struct CUpti_Profiler_CounterDataImage_InitializeScratchBuffer_Params
[#](https://docs.nvidia.com#_CPPv462CUpti_Profiler_CounterDataImage_InitializeScratchBuffer_Params) Params for cuptiProfilerCounterDataImageInitializeScratchBuffer.

Public Members

-
size_t structSize
[#](https://docs.nvidia.com#_CPPv4N62CUpti_Profiler_CounterDataImage_InitializeScratchBuffer_Params10structSizeE) [in] CUpti_Profiler_CounterDataImage_InitializeScratchBuffer_Params_STRUCT_SIZE


-
void *pPriv
[#](https://docs.nvidia.com#_CPPv4N62CUpti_Profiler_CounterDataImage_InitializeScratchBuffer_Params5pPrivE) [in] assign to NULL


-
size_t counterDataImageSize
[#](https://docs.nvidia.com#_CPPv4N62CUpti_Profiler_CounterDataImage_InitializeScratchBuffer_Params20counterDataImageSizeE) [in] size calculated from cuptiProfilerCounterDataImageCalculateSize


-
uint8_t *pCounterDataImage
[#](https://docs.nvidia.com#_CPPv4N62CUpti_Profiler_CounterDataImage_InitializeScratchBuffer_Params17pCounterDataImageE) [in]


-
size_t counterDataScratchBufferSize
[#](https://docs.nvidia.com#_CPPv4N62CUpti_Profiler_CounterDataImage_InitializeScratchBuffer_Params28counterDataScratchBufferSizeE) [in] size calculated using cuptiProfilerCounterDataImageCalculateScratchBufferSize


-
uint8_t *pCounterDataScratchBuffer
[#](https://docs.nvidia.com#_CPPv4N62CUpti_Profiler_CounterDataImage_InitializeScratchBuffer_Params25pCounterDataScratchBufferE) [in] the scratch buffer to be initialized.


-
size_t structSize