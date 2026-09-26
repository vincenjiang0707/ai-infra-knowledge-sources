source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_gelu_fusion_with_erf_one.html
lastmod: 

# Class ov::pass::GeluFusionWithErfOne[#](https://docs.openvino.ai#class-ov-pass-gelufusionwitherfone)

-
class GeluFusionWithErfOne : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass20GeluFusionWithErfOneE) [GeluFusion](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_gelu_fusion)transformation replaces a sub-graph (0.5 * x) * (1 + erf(x / sqrt(2))) with a Gelu op.

Site Navigation

Section Navigation

[GeluFusion](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_gelu_fusion) transformation replaces a sub-graph (0.5 * x) * (1 + erf(x / sqrt(2))) with a Gelu op.