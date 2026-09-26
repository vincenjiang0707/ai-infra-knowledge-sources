source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1low__precision_1_1_create_attribute.html
lastmod: 

# Class ov::pass::low_precision::CreateAttribute[#](https://docs.openvino.ai#class-ov-pass-low-precision-createattribute)

-
template<typename AttributeType, typename OperationType =
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[pattern](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4pass7patternE)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4pass7pattern2opE)::[Label](https://docs.openvino.ai/classov_1_1pass_1_1pattern_1_1op_1_1_label.html#_CPPv4N2ov4pass7pattern2op5LabelE)>

class CreateAttribute : public[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[low_precision](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4pass13low_precisionE)::[BaseMatcherPass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4pass13low_precision15BaseMatcherPassE)[#](https://docs.openvino.ai#_CPPv4I00EN2ov4pass13low_precision15CreateAttributeE) [CreateAttribute](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1low__precision_1_1_create_attribute)transformation marks OperationType operations by AttributeType attribute.For more details about the transformation, refer to CreateAttribute page in the OpenVINO Developer Guide.