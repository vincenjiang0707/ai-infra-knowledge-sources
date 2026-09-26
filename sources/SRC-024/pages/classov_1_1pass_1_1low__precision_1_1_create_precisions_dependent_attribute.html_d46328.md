source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1low__precision_1_1_create_precisions_dependent_attribute.html
lastmod: 

# Class ov::pass::low_precision::CreatePrecisionsDependentAttribute[#](https://docs.openvino.ai#class-ov-pass-low-precision-createprecisionsdependentattribute)

-
template<typename AttributeType, typename OperationType>

class CreatePrecisionsDependentAttribute : public[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4I00EN2ov4pass13low_precision34CreatePrecisionsDependentAttributeE) [CreatePrecisionsDependentAttribute](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1low__precision_1_1_create_precisions_dependent_attribute)transformation marks OperationType operations by[PrecisionPreservedAttribute](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1_precision_preserved_attribute)and AttributeType attributes with the same shared part.For more details about the transformation, refer to CreatePrecisionsDependentAttribute page in the OpenVINO Developer Guide.