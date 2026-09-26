source: https://docs.nvidia.com/cupti/api/structCUpti__GetCubinCrcParams.html

# 7.137. CUpti_GetCubinCrcParams[#](https://docs.nvidia.com#cupti-getcubincrcparams)

-
struct CUpti_GetCubinCrcParams
[#](https://docs.nvidia.com#_CPPv423CUpti_GetCubinCrcParams) Params for cuptiGetCubinCrc.

Public Members

-
size_t size
[#](https://docs.nvidia.com#_CPPv4N23CUpti_GetCubinCrcParams4sizeE) [w] Size of configuration structure.

CUPTI client should set the size of the structure. It will be used in CUPTI to check what fields are available in the structure. Used to preserve backward compatibility.


-
size_t cubinSize
[#](https://docs.nvidia.com#_CPPv4N23CUpti_GetCubinCrcParams9cubinSizeE) [w] Size of cubin binary.


-
const void *cubin
[#](https://docs.nvidia.com#_CPPv4N23CUpti_GetCubinCrcParams5cubinE) [w] Pointer to cubin binary


-
uint64_t cubinCrc
[#](https://docs.nvidia.com#_CPPv4N23CUpti_GetCubinCrcParams8cubinCrcE) [r] Computed CRC will be stored in it.


-
size_t size