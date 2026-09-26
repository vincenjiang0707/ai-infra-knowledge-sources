source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1low__precision_1_1_pull_reshape_through_dequantization.html
lastmod: 

# Class ov::pass::low_precision::PullReshapeThroughDequantization[#](https://docs.openvino.ai#class-ov-pass-low-precision-pullreshapethroughdequantization)

-
class PullReshapeThroughDequantization : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass13low_precision32PullReshapeThroughDequantizationE) [PullReshapeThroughDequantization](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1low__precision_1_1_pull_reshape_through_dequantization)propagates dequantization operations through Reshape operations. The transformation is used on constant subgraph weights to prepare a model for the next low precision transformations.For more details about the transformation, refer to PullReshapeThroughDequantization page in the OpenVINO Developer Guide.