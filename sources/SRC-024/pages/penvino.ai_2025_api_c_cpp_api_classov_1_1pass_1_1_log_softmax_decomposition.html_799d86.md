source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_log_softmax_decomposition.html
lastmod: 

# Class ov::pass::LogSoftmaxDecomposition[#](https://docs.openvino.ai#class-ov-pass-logsoftmaxdecomposition)

-
class LogSoftmaxDecomposition : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass23LogSoftmaxDecompositionE) [LogSoftmaxDecomposition](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_log_softmax_decomposition)transformation into sub-graph x - log(reduce_sum(exp(x), axis)).

Site Navigation

Section Navigation

[LogSoftmaxDecomposition](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_log_softmax_decomposition) transformation into sub-graph x - log(reduce_sum(exp(x), axis)).