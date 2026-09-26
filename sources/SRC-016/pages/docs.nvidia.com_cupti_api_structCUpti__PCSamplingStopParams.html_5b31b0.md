source: https://docs.nvidia.com/cupti/api/structCUpti__PCSamplingStopParams.html

# 7.154. CUpti_PCSamplingStopParams[#](https://docs.nvidia.com#cupti-pcsamplingstopparams)

-
struct CUpti_PCSamplingStopParams
[#](https://docs.nvidia.com#_CPPv426CUpti_PCSamplingStopParams) Params for cuptiPCSamplingStop.

Public Members

-
size_t size
[#](https://docs.nvidia.com#_CPPv4N26CUpti_PCSamplingStopParams4sizeE) [w] Size of the data structure i.e.

CUpti_PCSamplingStopParamsSize CUPTI client should set the size of the structure. It will be used in CUPTI to check what fields are available in the structure. Used to preserve backward compatibility.


-
void *pPriv
[#](https://docs.nvidia.com#_CPPv4N26CUpti_PCSamplingStopParams5pPrivE) [w] Assign to NULL


-
CUcontext ctx
[#](https://docs.nvidia.com#_CPPv4N26CUpti_PCSamplingStopParams3ctxE) [w] CUcontext


-
size_t size