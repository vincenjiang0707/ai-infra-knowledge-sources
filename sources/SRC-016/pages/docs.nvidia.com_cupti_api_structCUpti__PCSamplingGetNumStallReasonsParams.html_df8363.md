source: https://docs.nvidia.com/cupti/api/structCUpti__PCSamplingGetNumStallReasonsParams.html

# 7.149. CUpti_PCSamplingGetNumStallReasonsParams[#](https://docs.nvidia.com#cupti-pcsamplinggetnumstallreasonsparams)

-
struct CUpti_PCSamplingGetNumStallReasonsParams
[#](https://docs.nvidia.com#_CPPv440CUpti_PCSamplingGetNumStallReasonsParams) Params for cuptiPCSamplingGetNumStallReasons.

Public Members

-
size_t size
[#](https://docs.nvidia.com#_CPPv4N40CUpti_PCSamplingGetNumStallReasonsParams4sizeE) [w] Size of the data structure i.e.

CUpti_PCSamplingGetNumStallReasonsParamsSize CUPTI client should set the size of the structure. It will be used in CUPTI to check what fields are available in the structure. Used to preserve backward compatibility.


-
void *pPriv
[#](https://docs.nvidia.com#_CPPv4N40CUpti_PCSamplingGetNumStallReasonsParams5pPrivE) [w] Assign to NULL


-
CUcontext ctx
[#](https://docs.nvidia.com#_CPPv4N40CUpti_PCSamplingGetNumStallReasonsParams3ctxE) [w] CUcontext


-
size_t *numStallReasons
[#](https://docs.nvidia.com#_CPPv4N40CUpti_PCSamplingGetNumStallReasonsParams15numStallReasonsE) [r] Number of stall reasons


-
size_t size