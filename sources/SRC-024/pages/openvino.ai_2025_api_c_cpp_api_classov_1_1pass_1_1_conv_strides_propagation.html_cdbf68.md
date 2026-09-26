source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_conv_strides_propagation.html
lastmod: 

# Class ov::pass::ConvStridesPropagation[#](https://docs.openvino.ai#class-ov-pass-convstridespropagation)

-
class ConvStridesPropagation : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass22ConvStridesPropagationE) [ConvStridesPropagation](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_conv_strides_propagation)either propagates stride (greater than 1) from Convolution up through the graph or inserts pooling between current node and its consumers if the consumers have different StridesProp attributes.[Strides](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_strides)can be propagated if Convolution kernel is {1, 1, …}.