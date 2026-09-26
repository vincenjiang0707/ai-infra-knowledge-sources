source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1transpose__sinking_1_1_t_s_binary_forward.html
lastmod: 

# Class ov::pass::transpose_sinking::TSBinaryForward[#](https://docs.openvino.ai#class-ov-pass-transpose-sinking-tsbinaryforward)

-
class TSBinaryForward : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[transpose_sinking](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4pass17transpose_sinkingE)::[TSForwardBase](https://docs.openvino.ai/classov_1_1pass_1_1transpose__sinking_1_1_t_s_forward_base.html#_CPPv4N2ov4pass17transpose_sinking13TSForwardBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass17transpose_sinking15TSBinaryForwardE) [TSBinaryForward](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1transpose__sinking_1_1_t_s_binary_forward)transformation sinks Transpose through BinaryElementwiseArithmetic, BinaryElementwiseComparison, BinaryElementwiseLogical and PRelu operations in the forward direction.