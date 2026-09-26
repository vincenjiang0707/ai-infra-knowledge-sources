source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1low__precision_1_1_convert_subtract_constant.html
lastmod: 

# Class ov::pass::low_precision::ConvertSubtractConstant[#](https://docs.openvino.ai#class-ov-pass-low-precision-convertsubtractconstant)

-
class ConvertSubtractConstant : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass13low_precision23ConvertSubtractConstantE) [ConvertSubtractConstant](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1low__precision_1_1_convert_subtract_constant)marks Convert operations on constant subgraph by DISABLED_CONSTANT_FOLDING attribute to prevent constant folding.For more details about the transformation, refer to ConvertSubtractConstant page in the OpenVINO Developer Guide.