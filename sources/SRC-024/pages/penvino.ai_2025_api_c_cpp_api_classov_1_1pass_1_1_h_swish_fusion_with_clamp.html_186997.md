source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_h_swish_fusion_with_clamp.html
lastmod: 

# Class ov::pass::HSwishFusionWithClamp[#](https://docs.openvino.ai#class-ov-pass-hswishfusionwithclamp)

-
class HSwishFusionWithClamp : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass21HSwishFusionWithClampE) [HSwishFusion](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_h_swish_fusion)transformation replaces a sub-graph (Clamp(x + 3, 0, 6) * x) with a HSwish * 6.

Site Navigation

Section Navigation

[HSwishFusion](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_h_swish_fusion) transformation replaces a sub-graph (Clamp(x + 3, 0, 6) * x) with a HSwish * 6.