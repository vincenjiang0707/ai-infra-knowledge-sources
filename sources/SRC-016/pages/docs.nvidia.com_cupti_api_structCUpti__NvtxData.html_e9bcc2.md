source: https://docs.nvidia.com/cupti/api/structCUpti__NvtxData.html

# 7.141. CUpti_NvtxData[#](https://docs.nvidia.com#cupti-nvtxdata)

-
struct CUpti_NvtxData
[#](https://docs.nvidia.com#_CPPv414CUpti_NvtxData) Data passed into a NVTX callback function.

Data passed into a NVTX callback function as the

`cbdata`

argument to[CUpti_CallbackFunc](https://docs.nvidia.com/group__CUPTI__CALLBACK__API.html#group__cupti__callback__api_1ga21bab4f7f7e04488b0e7edcea9f5a49c). The`cbdata`

will be this type for`domain`

equal to CUPTI_CB_DOMAIN_NVTX. Unless otherwise notes, the callback data is valid only within the invocation of the callback function that is passed the data. If you need to retain some data for use outside of the callback, you must make a copy of that data.Public Members

-
const char *functionName
[#](https://docs.nvidia.com#_CPPv4N14CUpti_NvtxData12functionNameE) Name of the NVTX API function which issued the callback.

This string is a global constant and so may be accessed outside of the callback.


-
const void *functionParams
[#](https://docs.nvidia.com#_CPPv4N14CUpti_NvtxData14functionParamsE) Pointer to the arguments passed to the NVTX API call.

See generated_nvtx_meta.h for structure definitions for the parameters for each NVTX API function.


-
const void *functionReturnValue
[#](https://docs.nvidia.com#_CPPv4N14CUpti_NvtxData19functionReturnValueE) Pointer to the return value of the NVTX API call.

See nvToolsExt.h for each NVTX API function’s return value.


-
const char *functionName