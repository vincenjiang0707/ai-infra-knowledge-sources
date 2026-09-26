source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_random_uniform_fusion.html
lastmod: 

# Class ov::pass::RandomUniformFusion[#](https://docs.openvino.ai#class-ov-pass-randomuniformfusion)

-
class RandomUniformFusion : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass19RandomUniformFusionE) [RandomUniformFusion](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_random_uniform_fusion)transformation replaces RandomUniform -> Add or RandomUniform -> Mul subgraph with a RandomUniform and replaces min and max const with corrected values.