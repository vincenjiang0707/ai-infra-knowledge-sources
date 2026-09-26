source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_gelu_fusion_with_erf_four.html
lastmod: 

# Class ov::pass::GeluFusionWithErfFour[#](https://docs.openvino.ai#class-ov-pass-gelufusionwitherffour)

-
class GeluFusionWithErfFour : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass21GeluFusionWithErfFourE) [GeluFusion](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_gelu_fusion)transformation replaces a sub-graph x * (0.5 + 0.5 * erf(x * (1 / sqrt(2)))) with a Gelu op.

Site Navigation

Section Navigation

[GeluFusion](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_gelu_fusion) transformation replaces a sub-graph x * (0.5 + 0.5 * erf(x * (1 / sqrt(2)))) with a Gelu op.