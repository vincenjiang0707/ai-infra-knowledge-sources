source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v0_1_1_tan.html
lastmod: 

# Class ov::op::v0::Tan[#](https://docs.openvino.ai#class-ov-op-v0-tan)

-
class Tan : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[UnaryElementwiseArithmetic](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_unary_elementwise_arithmetic.html#_CPPv4N2ov2op4util26UnaryElementwiseArithmeticE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v03TanE) Elementwise tangent operation.

*Inputs*Type

Description

`arg`

\(N[d_1,\dots,d_n]~(n \geq 0)\)

A tensor of any shape and numeric element type.

Type

Description

\(N[d_1,\dots,d_n]\)

The tensor \(T\), where \(T[i_1,\dots,i_n] = \tan(\texttt{arg}[i_1,\dots,i_n])\)