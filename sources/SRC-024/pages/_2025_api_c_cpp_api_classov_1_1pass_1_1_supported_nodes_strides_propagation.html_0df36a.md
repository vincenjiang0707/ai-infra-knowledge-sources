source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_supported_nodes_strides_propagation.html
lastmod: 

# Class ov::pass::SupportedNodesStridesPropagation[#](https://docs.openvino.ai#class-ov-pass-supportednodesstridespropagation)

-
class SupportedNodesStridesPropagation : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass32SupportedNodesStridesPropagationE) [SupportedNodesStridesPropagation](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_supported_nodes_strides_propagation)either propagates stride (greater than 1) from current node up through the graph or inserts pooling between current node and its consumers if the consumers have different StridesProp attributes.