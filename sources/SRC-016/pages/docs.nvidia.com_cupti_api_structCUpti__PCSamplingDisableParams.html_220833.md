source: https://docs.nvidia.com/cupti/api/structCUpti__PCSamplingDisableParams.html

# 7.146. CUpti_PCSamplingDisableParams[#](https://docs.nvidia.com#cupti-pcsamplingdisableparams)

-
struct CUpti_PCSamplingDisableParams
[#](https://docs.nvidia.com#_CPPv429CUpti_PCSamplingDisableParams) Params for cuptiPCSamplingDisable.

Public Members

-
size_t size
[#](https://docs.nvidia.com#_CPPv4N29CUpti_PCSamplingDisableParams4sizeE) [w] Size of the data structure i.e.

CUpti_PCSamplingDisableParamsSize CUPTI client should set the size of the structure. It will be used in CUPTI to check what fields are available in the structure. Used to preserve backward compatibility.


-
void *pPriv
[#](https://docs.nvidia.com#_CPPv4N29CUpti_PCSamplingDisableParams5pPrivE) [w] Assign to NULL


-
CUcontext ctx
[#](https://docs.nvidia.com#_CPPv4N29CUpti_PCSamplingDisableParams3ctxE) [w] CUcontext


-
size_t size