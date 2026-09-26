source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_h_swish_fusion_with_h_sigmoid.html
lastmod: 

# Class ov::pass::HSwishFusionWithHSigmoid[#](https://docs.openvino.ai#class-ov-pass-hswishfusionwithhsigmoid)

-
class HSwishFusionWithHSigmoid : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass24HSwishFusionWithHSigmoidE) [HSwishFusion](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_h_swish_fusion)transformation replaces a sub-graph x * HSigmoid(x) with a HSwish op.

Site Navigation

Section Navigation

[HSwishFusion](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_h_swish_fusion) transformation replaces a sub-graph x * HSigmoid(x) with a HSwish op.