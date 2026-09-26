source: https://docs.nvidia.com/cupti/api/structCUpti__PCSamplingPCData.html

# 7.151. CUpti_PCSamplingPCData[#](https://docs.nvidia.com#cupti-pcsamplingpcdata)

-
struct CUpti_PCSamplingPCData
[#](https://docs.nvidia.com#_CPPv422CUpti_PCSamplingPCData) PC Sampling data.

Public Members

-
size_t size
[#](https://docs.nvidia.com#_CPPv4N22CUpti_PCSamplingPCData4sizeE) [w] Size of the data structure.

CUPTI client should set the size of the structure. It will be used in CUPTI to check what fields are available in the structure. Used to preserve backward compatibility.


-
uint64_t cubinCrc
[#](https://docs.nvidia.com#_CPPv4N22CUpti_PCSamplingPCData8cubinCrcE) [r] Unique cubin id


-
uint64_t pcOffset
[#](https://docs.nvidia.com#_CPPv4N22CUpti_PCSamplingPCData8pcOffsetE) [r] PC offset


-
uint32_t functionIndex
[#](https://docs.nvidia.com#_CPPv4N22CUpti_PCSamplingPCData13functionIndexE) The function’s unique symbol index in the module.


-
uint32_t pad
[#](https://docs.nvidia.com#_CPPv4N22CUpti_PCSamplingPCData3padE) Padding.


-
char *functionName
[#](https://docs.nvidia.com#_CPPv4N22CUpti_PCSamplingPCData12functionNameE) [r] The function name.

This name string might be shared across all the records including records from activity APIs representing the same function, and so it should not be modified or freed until post processing of all the records is done. Once done, it is user’s responsibility to free the memory using free() function.


-
size_t stallReasonCount
[#](https://docs.nvidia.com#_CPPv4N22CUpti_PCSamplingPCData16stallReasonCountE) [r] Collected stall reason count


-
[CUpti_PCSamplingStallReason](https://docs.nvidia.com/structCUpti__PCSamplingStallReason.html#_CPPv427CUpti_PCSamplingStallReason)*stallReason[#](https://docs.nvidia.com#_CPPv4N22CUpti_PCSamplingPCData11stallReasonE) [r] Stall reason id Total samples


-
uint32_t correlationId
[#](https://docs.nvidia.com#_CPPv4N22CUpti_PCSamplingPCData13correlationIdE) The correlation ID of the kernel to which this result is associated.

Only valid for serialized mode of pc sampling collection. For continous mode of collection the correlationId will be set to 0.


-
size_t size