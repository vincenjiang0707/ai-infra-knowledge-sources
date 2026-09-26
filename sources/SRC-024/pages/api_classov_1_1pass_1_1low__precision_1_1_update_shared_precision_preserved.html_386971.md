source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1low__precision_1_1_update_shared_precision_preserved.html
lastmod: 

# Class ov::pass::low_precision::UpdateSharedPrecisionPreserved[#](https://docs.openvino.ai#class-ov-pass-low-precision-updatesharedprecisionpreserved)

-
template<typename AttributeType, typename ExpectedAttributeType =
[AttributeType](https://docs.openvino.ai#_CPPv4I00EN2ov4pass13low_precision30UpdateSharedPrecisionPreservedE)>

class UpdateSharedPrecisionPreserved : public[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4I00EN2ov4pass13low_precision30UpdateSharedPrecisionPreservedE) [UpdateSharedPrecisionPreserved](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1low__precision_1_1_update_shared_precision_preserved)transformation updates shared AttributeType attribute instance value to true for precision preserved operations if ExpectedAttributeType exist.For more details about the transformation, refer to UpdateSharedPrecisionPreserved page in the OpenVINO Developer Guide.