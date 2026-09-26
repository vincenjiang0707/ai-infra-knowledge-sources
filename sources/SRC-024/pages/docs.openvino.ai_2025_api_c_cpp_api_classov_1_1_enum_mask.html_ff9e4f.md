source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1_enum_mask.html
lastmod: 

# Class ov::EnumMask[#](https://docs.openvino.ai#class-ov-enummask)

-
template<typename T>

class EnumMask[#](https://docs.openvino.ai#_CPPv4I0EN2ov8EnumMaskE) Public Types

Public Functions

-
constexpr EnumMask() = default
[#](https://docs.openvino.ai#_CPPv4N2ov8EnumMask8EnumMaskEv) Some bit operations are not safe for signed values, we require enum type to use unsigned underlying type.


-
inline bool is_any_set(const
[EnumMask](https://docs.openvino.ai#_CPPv4I0EN2ov8EnumMaskE)&p) const[#](https://docs.openvino.ai#_CPPv4NK2ov8EnumMask10is_any_setERK8EnumMask) Check if any of the input parameter enum bit mask match.


-
inline bool is_set(const
[EnumMask](https://docs.openvino.ai#_CPPv4I0EN2ov8EnumMaskE)&p) const[#](https://docs.openvino.ai#_CPPv4NK2ov8EnumMask6is_setERK8EnumMask) Check if all of the input parameter enum bit mask match.


-
constexpr EnumMask() = default