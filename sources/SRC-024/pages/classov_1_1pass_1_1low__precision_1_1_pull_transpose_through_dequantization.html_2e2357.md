source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1low__precision_1_1_pull_transpose_through_dequantization.html
lastmod: 

# Class ov::pass::low_precision::PullTransposeThroughDequantization[#](https://docs.openvino.ai#class-ov-pass-low-precision-pulltransposethroughdequantization)

-
class PullTransposeThroughDequantization : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass13low_precision34PullTransposeThroughDequantizationE) [PullTransposeThroughDequantization](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1low__precision_1_1_pull_transpose_through_dequantization)propagates dequantization operations through Transpose operations. The transformation is used on constant subgraph weights to prepare a model for the next low precision transformations.For more details about the transformation, refer to PullTransposeThroughDequantization page in the OpenVINO Developer Guide.