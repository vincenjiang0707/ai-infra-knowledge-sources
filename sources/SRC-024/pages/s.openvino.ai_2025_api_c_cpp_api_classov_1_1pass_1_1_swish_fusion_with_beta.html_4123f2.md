source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_swish_fusion_with_beta.html
lastmod: 

# Class ov::pass::SwishFusionWithBeta[#](https://docs.openvino.ai#class-ov-pass-swishfusionwithbeta)

-
class SwishFusionWithBeta : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass19SwishFusionWithBetaE) [SwishFusionWithSigmoid](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_swish_fusion_with_sigmoid)replaces a sub-graphs x / (1.0 + exp(-x * beta)) with a Swish op.

Site Navigation

Section Navigation

[SwishFusionWithSigmoid](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_swish_fusion_with_sigmoid) replaces a sub-graphs x / (1.0 + exp(-x * beta)) with a Swish op.