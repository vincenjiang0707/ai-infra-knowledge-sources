source: https://docs.nvidia.com/cupti/api/structCUpti__PCSamplingEnableParams.html

# 7.147. CUpti_PCSamplingEnableParams[#](https://docs.nvidia.com#cupti-pcsamplingenableparams)

-
struct CUpti_PCSamplingEnableParams
[#](https://docs.nvidia.com#_CPPv428CUpti_PCSamplingEnableParams) Params for cuptiPCSamplingEnable.

Public Members

-
size_t size
[#](https://docs.nvidia.com#_CPPv4N28CUpti_PCSamplingEnableParams4sizeE) [w] Size of the data structure i.e.

CUpti_PCSamplingEnableParamsSize CUPTI client should set the size of the structure. It will be used in CUPTI to check what fields are available in the structure. Used to preserve backward compatibility.


-
void *pPriv
[#](https://docs.nvidia.com#_CPPv4N28CUpti_PCSamplingEnableParams5pPrivE) [w] Assign to NULL


-
CUcontext ctx
[#](https://docs.nvidia.com#_CPPv4N28CUpti_PCSamplingEnableParams3ctxE) [w] CUcontext


-
size_t size