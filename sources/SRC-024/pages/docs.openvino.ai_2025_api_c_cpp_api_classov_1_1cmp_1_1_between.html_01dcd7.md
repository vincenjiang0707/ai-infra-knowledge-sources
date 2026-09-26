source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1cmp_1_1_between.html
lastmod: 

# Class ov::cmp::Between[#](https://docs.openvino.ai#class-ov-cmp-between)

-
template<class T,
[Bound](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov3cmp5BoundE)BMode =[Bound](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov3cmp5BoundE)::[NONE](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov3cmp5Bound4NONEE)>

class Between[#](https://docs.openvino.ai#_CPPv4I0_5BoundEN2ov3cmp7BetweenE) Compare if value is between lower and upper bounds.

The

[Between](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1cmp_1_1_between)comparator has four modes to check value:Bound::None (lower, upper)

Bound::LOWER [lower, upper)

Bound::UPPER (lower, upper]

Bound::BOTH [lower, upper]


- Template Parameters:
**T**– Value type to compare.**BMode**– Compare bounds mode.