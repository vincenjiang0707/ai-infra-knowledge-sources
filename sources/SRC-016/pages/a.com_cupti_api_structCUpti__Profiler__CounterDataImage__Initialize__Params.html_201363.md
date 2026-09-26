source: https://docs.nvidia.com/cupti/api/structCUpti__Profiler__CounterDataImage__Initialize__Params.html

# 7.172. CUpti_Profiler_CounterDataImage_Initialize_Params[#](https://docs.nvidia.com#cupti-profiler-counterdataimage-initialize-params)

-
struct CUpti_Profiler_CounterDataImage_Initialize_Params
[#](https://docs.nvidia.com#_CPPv449CUpti_Profiler_CounterDataImage_Initialize_Params) Params for cuptiProfilerCounterDataImageInitialize.

Public Members

-
size_t structSize
[#](https://docs.nvidia.com#_CPPv4N49CUpti_Profiler_CounterDataImage_Initialize_Params10structSizeE) [in] CUpti_Profiler_CounterDataImage_Initialize_Params_STRUCT_SIZE


-
void *pPriv
[#](https://docs.nvidia.com#_CPPv4N49CUpti_Profiler_CounterDataImage_Initialize_Params5pPrivE) [in] assign to NULL


-
size_t sizeofCounterDataImageOptions
[#](https://docs.nvidia.com#_CPPv4N49CUpti_Profiler_CounterDataImage_Initialize_Params29sizeofCounterDataImageOptionsE) [in] CUpti_Profiler_CounterDataImageOptions_STRUCT_SIZE


-
const
[CUpti_Profiler_CounterDataImageOptions](https://docs.nvidia.com/structCUpti__Profiler__CounterDataImageOptions.html#_CPPv438CUpti_Profiler_CounterDataImageOptions)*pOptions[#](https://docs.nvidia.com#_CPPv4N49CUpti_Profiler_CounterDataImage_Initialize_Params8pOptionsE) [in] Pointer to Counter Data Image Options


-
size_t counterDataImageSize
[#](https://docs.nvidia.com#_CPPv4N49CUpti_Profiler_CounterDataImage_Initialize_Params20counterDataImageSizeE) [in] Size calculated from cuptiProfilerCounterDataImageCalculateSize


-
uint8_t *pCounterDataImage
[#](https://docs.nvidia.com#_CPPv4N49CUpti_Profiler_CounterDataImage_Initialize_Params17pCounterDataImageE) [in] The buffer to be initialized.


-
size_t structSize