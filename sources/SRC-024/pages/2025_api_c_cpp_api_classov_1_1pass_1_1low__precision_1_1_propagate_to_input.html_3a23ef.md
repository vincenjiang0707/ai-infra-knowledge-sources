source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1low__precision_1_1_propagate_to_input.html
lastmod: 

# Class ov::pass::low_precision::PropagateToInput[#](https://docs.openvino.ai#class-ov-pass-low-precision-propagatetoinput)

-
template<typename AttributeType>

class PropagateToInput : public[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4I0EN2ov4pass13low_precision16PropagateToInputE) [PropagateToInput](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1low__precision_1_1_propagate_to_input)transformation propagates AttributeType shared value attribute instances from parent output ports to consumers input ports.For more details about the transformation, refer to PropagateToInput page in the OpenVINO Developer Guide.