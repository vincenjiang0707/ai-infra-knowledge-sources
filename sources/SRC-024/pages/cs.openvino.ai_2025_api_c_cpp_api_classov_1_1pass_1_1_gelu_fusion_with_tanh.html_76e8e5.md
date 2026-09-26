source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_gelu_fusion_with_tanh.html
lastmod: 

# Class ov::pass::GeluFusionWithTanh[#](https://docs.openvino.ai#class-ov-pass-gelufusionwithtanh)

-
class GeluFusionWithTanh : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass18GeluFusionWithTanhE) [GeluFusion](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_gelu_fusion)transformation replaces a sub-graph x * (0.5 * (1 + tanh([sqrt(2 / pi)] * [x + 0.044715^3]))) with a Gelu (Tanh) op.

Site Navigation

Section Navigation

[GeluFusion](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_gelu_fusion) transformation replaces a sub-graph x * (0.5 * (1 + tanh([sqrt(2 / pi)] * [x + 0.044715^3]))) with a Gelu (Tanh) op.