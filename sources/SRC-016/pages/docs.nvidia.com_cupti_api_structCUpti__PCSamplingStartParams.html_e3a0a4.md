source: https://docs.nvidia.com/cupti/api/structCUpti__PCSamplingStartParams.html

# 7.153. CUpti_PCSamplingStartParams[#](https://docs.nvidia.com#cupti-pcsamplingstartparams)

-
struct CUpti_PCSamplingStartParams
[#](https://docs.nvidia.com#_CPPv427CUpti_PCSamplingStartParams) Params for cuptiPCSamplingStart.

Public Members

-
size_t size
[#](https://docs.nvidia.com#_CPPv4N27CUpti_PCSamplingStartParams4sizeE) [w] Size of the data structure i.e.

CUpti_PCSamplingStartParamsSize CUPTI client should set the size of the structure. It will be used in CUPTI to check what fields are available in the structure. Used to preserve backward compatibility.


-
void *pPriv
[#](https://docs.nvidia.com#_CPPv4N27CUpti_PCSamplingStartParams5pPrivE) [w] Assign to NULL


-
CUcontext ctx
[#](https://docs.nvidia.com#_CPPv4N27CUpti_PCSamplingStartParams3ctxE) [w] CUcontext


-
size_t size