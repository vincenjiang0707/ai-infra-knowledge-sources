source: https://docs.nvidia.com/cupti/api/structCUPTI_1_1PcSamplingUtil_1_1CUptiUtil__MergePcSampDataParams.html

# 8.1.1.5. CUptiUtil_MergePcSampDataParams[#](https://docs.nvidia.com#cuptiutil-mergepcsampdataparams)

Fully qualified name: `CUPTI::PcSamplingUtil::CUptiUtil_MergePcSampDataParams`


-
struct CUptiUtil_MergePcSampDataParams
[#](https://docs.nvidia.com#_CPPv4N5CUPTI14PcSamplingUtil31CUptiUtil_MergePcSampDataParamsE) Params for

[CuptiUtilMergePcSampData](https://docs.nvidia.com/group__CUPTI__PCSAMPLING__UTILITY.html#group__cupti__pcsampling__utility_1ga4987e223c4132503d622f29ce5a9546e).Public Members

-
size_t size
[#](https://docs.nvidia.com#_CPPv4N5CUPTI14PcSamplingUtil31CUptiUtil_MergePcSampDataParams4sizeE) Size of the data structure i.e.

CUpti_PCSamplingDisableParamsSize CUPTI client should set the size of the structure. It will be used in CUPTI to check what fields are available in the structure. Used to preserve backward compatibility.


-
size_t numberOfBuffers
[#](https://docs.nvidia.com#_CPPv4N5CUPTI14PcSamplingUtil31CUptiUtil_MergePcSampDataParams15numberOfBuffersE) Number of buffers to merge.


-
[CUpti_PCSamplingData](https://docs.nvidia.com/structCUpti__PCSamplingData.html#_CPPv420CUpti_PCSamplingData)*PcSampDataBuffer[#](https://docs.nvidia.com#_CPPv4N5CUPTI14PcSamplingUtil31CUptiUtil_MergePcSampDataParams16PcSampDataBufferE) Pointer to array of buffers to merge.


-
[CUpti_PCSamplingData](https://docs.nvidia.com/structCUpti__PCSamplingData.html#_CPPv420CUpti_PCSamplingData)**MergedPcSampDataBuffers[#](https://docs.nvidia.com#_CPPv4N5CUPTI14PcSamplingUtil31CUptiUtil_MergePcSampDataParams23MergedPcSampDataBuffersE) Pointer to array of merged buffers as per the range id.


-
size_t *numMergedBuffer
[#](https://docs.nvidia.com#_CPPv4N5CUPTI14PcSamplingUtil31CUptiUtil_MergePcSampDataParams15numMergedBufferE) Number of merged buffers.


-
size_t size