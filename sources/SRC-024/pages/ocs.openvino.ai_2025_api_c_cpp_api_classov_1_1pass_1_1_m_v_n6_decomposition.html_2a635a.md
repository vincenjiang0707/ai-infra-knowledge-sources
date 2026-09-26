source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_m_v_n6_decomposition.html
lastmod: 

# Class ov::pass::MVN6Decomposition[#](https://docs.openvino.ai#class-ov-pass-mvn6decomposition)

-
class MVN6Decomposition : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass17MVN6DecompositionE) [MVN6Decomposition](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_m_v_n6_decomposition)transformation into sub-graph x - ReduceMean(x, axes) if normalize_variance is false and into sub-graph (x - ReduceMean(x, axes)) / Sqrt(ReduceMean((x - ReduceMean(x, axes)) ^ 2)) if normalize_variance is true.