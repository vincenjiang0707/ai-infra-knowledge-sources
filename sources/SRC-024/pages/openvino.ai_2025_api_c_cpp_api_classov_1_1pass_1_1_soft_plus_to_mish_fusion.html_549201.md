source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_soft_plus_to_mish_fusion.html
lastmod: 

# Class ov::pass::SoftPlusToMishFusion[#](https://docs.openvino.ai#class-ov-pass-softplustomishfusion)

-
class SoftPlusToMishFusion : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass20SoftPlusToMishFusionE) [SoftPlusToMishFusion](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_soft_plus_to_mish_fusion)transformation replaces group of operations: x * tanh(softplus(x)) to Mish op.

Site Navigation

Section Navigation

[SoftPlusToMishFusion](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_soft_plus_to_mish_fusion) transformation replaces group of operations: x * tanh(softplus(x)) to Mish op.