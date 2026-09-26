source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_softmax_decomposition.html
lastmod: 

# Class ov::pass::SoftmaxDecomposition[#](https://docs.openvino.ai#class-ov-pass-softmaxdecomposition)

-
class SoftmaxDecomposition : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass20SoftmaxDecompositionE) [SoftmaxDecomposition](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_softmax_decomposition)transformation replaces softmax with following graph:+---------------+ │ │ │ input │ │ │ +---------------+ │ │ │ v │ +-----------+ │ │ │ │ │ ReduceMax │ │ │ │ │ +-----------+ │ │ │ │ v v +---------------+ │ │ │ Sub │ │ │ +---------------+ | | v +---------------+ │ │ │ Exp │ │ │ +---------------+ │ │ │ v │ +-----------+ │ │ │ │ │ ReduceSum │ │ │ │ │ +-----------+ │ │ │ │ v v +-------------+ | │ | Div │ │ │ +-------------+