source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_pad_fusion_group_convolution.html
lastmod: 

# Class ov::pass::PadFusionGroupConvolution[#](https://docs.openvino.ai#class-ov-pass-padfusiongroupconvolution)

-
class PadFusionGroupConvolution : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass25PadFusionGroupConvolutionE) [PadFusion](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1_pad_fusion)transformation replaces following graph: Pad -> GroupConvolution to GroupConvolution, under following conditions.pad mode is

[op::PadMode::CONSTANT](https://docs.openvino.ai/group__ov__transformation__common__api.html#namespaceov_1_1op_1aff39ecf8a8a3110216bfe131cc8b9ae0a8d6b5cada83510220f59e00ce86d4d92)pad value is 0