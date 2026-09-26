source: https://docs.nvidia.com/cupti/api/structCUpti__PCSamplingGetDataParams.html

# 7.148. CUpti_PCSamplingGetDataParams[#](https://docs.nvidia.com#cupti-pcsamplinggetdataparams)

-
struct CUpti_PCSamplingGetDataParams
[#](https://docs.nvidia.com#_CPPv429CUpti_PCSamplingGetDataParams) Params for cuptiPCSamplingEnable.

Public Members

-
size_t size
[#](https://docs.nvidia.com#_CPPv4N29CUpti_PCSamplingGetDataParams4sizeE) [w] Size of the data structure i.e.

CUpti_PCSamplingGetDataParamsSize CUPTI client should set the size of the structure. It will be used in CUPTI to check what fields are available in the structure. Used to preserve backward compatibility.


-
void *pPriv
[#](https://docs.nvidia.com#_CPPv4N29CUpti_PCSamplingGetDataParams5pPrivE) [w] Assign to NULL


-
CUcontext ctx
[#](https://docs.nvidia.com#_CPPv4N29CUpti_PCSamplingGetDataParams3ctxE) [w] CUcontext


-
void *pcSamplingData
[#](https://docs.nvidia.com#_CPPv4N29CUpti_PCSamplingGetDataParams14pcSamplingDataE) - Param pcSamplingData:
Data buffer to hold collected PC Sampling data PARSED_DATA Buffer type is void * which can point to PARSED_DATA Refer

[CUpti_PCSamplingData](https://docs.nvidia.com/structCUpti__PCSamplingData.html#structcupti__pcsamplingdata)for buffer format for PARSED_DATA


-
size_t size