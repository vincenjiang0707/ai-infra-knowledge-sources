source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_soft_plus_fusion.html
lastmod: 

# Class ov::pass::SoftPlusFusion[#](https://docs.openvino.ai#class-ov-pass-softplusfusion)

-
class SoftPlusFusion : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass14SoftPlusFusionE) [SoftPlusFusion](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_soft_plus_fusion)transformation replaces group of operations: log(exp(x) + 1) to SoftPlus op.

Site Navigation

Section Navigation

[SoftPlusFusion](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_soft_plus_fusion) transformation replaces group of operations: log(exp(x) + 1) to SoftPlus op.