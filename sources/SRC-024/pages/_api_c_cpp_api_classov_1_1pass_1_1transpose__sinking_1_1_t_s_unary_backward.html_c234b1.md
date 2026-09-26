source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1transpose__sinking_1_1_t_s_unary_backward.html
lastmod: 

# Class ov::pass::transpose_sinking::TSUnaryBackward[#](https://docs.openvino.ai#class-ov-pass-transpose-sinking-tsunarybackward)

-
class TSUnaryBackward : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass17transpose_sinking15TSUnaryBackwardE) [TSUnaryBackward](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1transpose__sinking_1_1_t_s_unary_backward)transformation sinks Transpose through UnaryElementwiseArithmetic, Clamp, Elu, SoftPlus, LogicalNot, Convert, IsInf, IsNaN, IsFinite in the backward direction.