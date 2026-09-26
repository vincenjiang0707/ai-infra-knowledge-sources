source: https://docs.nvidia.com/cupti/api/structCUpti__NvtxExtPayloadAttr.html

# 7.142. CUpti_NvtxExtPayloadAttr[#](https://docs.nvidia.com#cupti-nvtxextpayloadattr)

-
struct CUpti_NvtxExtPayloadAttr
[#](https://docs.nvidia.com#_CPPv424CUpti_NvtxExtPayloadAttr) Public Members

-
uint32_t structSize
[#](https://docs.nvidia.com#_CPPv4N24CUpti_NvtxExtPayloadAttr10structSizeE) Size of the struct in bytes.


-
uint32_t type
[#](https://docs.nvidia.com#_CPPv4N24CUpti_NvtxExtPayloadAttr4typeE) The payload type.


-
void *attributes
[#](https://docs.nvidia.com#_CPPv4N24CUpti_NvtxExtPayloadAttr10attributesE) The attributes of the payload.

Depending on the type, typecast the pointer: CUPTI_NVTX_EXT_PAYLOAD_TYPE_SCHEMA: nvtxPayloadSchemaAttr_t CUPTI_NVTX_EXT_PAYLOAD_TYPE_ENUM: nvtxPayloadEnumAttr_t


-
uint32_t structSize