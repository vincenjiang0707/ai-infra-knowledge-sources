source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1transpose__sinking_1_1_t_s_binary_backward.html
lastmod: 

# Class ov::pass::transpose_sinking::TSBinaryBackward[#](https://docs.openvino.ai#class-ov-pass-transpose-sinking-tsbinarybackward)

-
class TSBinaryBackward : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass17transpose_sinking16TSBinaryBackwardE) [TSBinaryBackward](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1transpose__sinking_1_1_t_s_binary_backward)transformation sinks Transpose through BinaryElementwiseArithmetic, BinaryElementwiseComparison, BinaryElementwiseLogical and PRelu operations in the backward direction.