source: https://docs.nvidia.com/cupti/api/structCUpti__PCSamplingGetStallReasonsParams.html

# 7.150. CUpti_PCSamplingGetStallReasonsParams[#](https://docs.nvidia.com#cupti-pcsamplinggetstallreasonsparams)

-
struct CUpti_PCSamplingGetStallReasonsParams
[#](https://docs.nvidia.com#_CPPv437CUpti_PCSamplingGetStallReasonsParams) Params for cuptiPCSamplingGetStallReasons.

Public Members

-
size_t size
[#](https://docs.nvidia.com#_CPPv4N37CUpti_PCSamplingGetStallReasonsParams4sizeE) [w] Size of the data structure i.e.

CUpti_PCSamplingGetStallReasonsParamsSize CUPTI client should set the size of the structure. It will be used in CUPTI to check what fields are available in the structure. Used to preserve backward compatibility.


-
void *pPriv
[#](https://docs.nvidia.com#_CPPv4N37CUpti_PCSamplingGetStallReasonsParams5pPrivE) [w] Assign to NULL


-
CUcontext ctx
[#](https://docs.nvidia.com#_CPPv4N37CUpti_PCSamplingGetStallReasonsParams3ctxE) [w] CUcontext


-
size_t numStallReasons
[#](https://docs.nvidia.com#_CPPv4N37CUpti_PCSamplingGetStallReasonsParams15numStallReasonsE) [w] Number of stall reasons


-
uint32_t *stallReasonIndex
[#](https://docs.nvidia.com#_CPPv4N37CUpti_PCSamplingGetStallReasonsParams16stallReasonIndexE) [r] Stall reason index


-
char **stallReasons
[#](https://docs.nvidia.com#_CPPv4N37CUpti_PCSamplingGetStallReasonsParams12stallReasonsE) [r] Stall reasons name


-
size_t size