source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_normalize_l2_fusion.html
lastmod: 

# Class ov::pass::NormalizeL2Fusion[#](https://docs.openvino.ai#class-ov-pass-normalizel2fusion)

-
class NormalizeL2Fusion : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass17NormalizeL2FusionE) [NormalizeL2Fusion](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_normalize_l2_fusion)transformation replaces sub-graphs: x/(sqrt(max(reduce_sum(x[j0, …, jN]**2, axes), eps)) x/(sqrt(add(reduce_sum(x[j0, …, jN]**2, axes), eps)) x/(pow(max(reduce_sum(x[j0, …, jN]**2, axes), eps), 0.5) x/(pow(add(reduce_sum(x[j0, …, jN]**2, axes), eps), 0.5) x*(pow(max(reduce_sum(x[j0, …, jN]**2, axes), eps), -0.5) x*(pow(add(reduce_sum(x[j0, …, jN]**2, axes), eps), -0.5) with a NormalizeL2(x, axes, eps, eps_mode[MAX|ADD]) op.