source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_unsupported_nodes_strides_propagation.html
lastmod: 

# Class ov::pass::UnsupportedNodesStridesPropagation[#](https://docs.openvino.ai#class-ov-pass-unsupportednodesstridespropagation)

-
class UnsupportedNodesStridesPropagation : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass34UnsupportedNodesStridesPropagationE) [UnsupportedNodesStridesPropagation](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_unsupported_nodes_strides_propagation)inserts pooling between current node and its consumers if the consumers have different StridesProp attributes.