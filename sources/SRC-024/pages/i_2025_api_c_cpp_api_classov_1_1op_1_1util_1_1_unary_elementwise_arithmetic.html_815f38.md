source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1util_1_1_unary_elementwise_arithmetic.html
lastmod: 

# Class ov::op::util::UnaryElementwiseArithmetic[#](https://docs.openvino.ai#class-ov-op-util-unaryelementwisearithmetic)

-
class UnaryElementwiseArithmetic : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op4util26UnaryElementwiseArithmeticE) Abstract base class for elementwise unary arithmetic operations, i.e., operations where the same scalar arithmetic operation is applied to each element.

For example, if the underlying operation (determined by the subclass) is \(\mathit{op}(x)\), the input tensor \([[x,y],[z,w]]\) will be mapped to \([[\mathit{op}(x),\mathit{op}(y)],[\mathit{op}(z),\mathit{op}(w)]]\).

*Inputs*Type

Description

`arg`

\(N[d_1,\dots,d_n]~(n \geq 0)\)

A tensor of any shape. The element type \(N\) may be any numeric type.

Type

Description

\(N[d_1,\dots,d_n]\)

The tensor \(T\), where \(T[i_1,\dots,i_n] = \mathit{op}(\texttt{arg}[i_1,\dots,i_n])\). This will always have the same shape and element type as the input tensor.

Subclassed by

[ov::op::v0::Abs](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_abs),[ov::op::v0::Acos](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_acos),[ov::op::v0::Asin](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_asin),[ov::op::v0::Atan](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_atan),[ov::op::v0::Ceiling](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_ceiling),[ov::op::v0::Clamp](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_clamp),[ov::op::v0::Cos](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_cos),[ov::op::v0::Cosh](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_cosh),[ov::op::v0::Elu](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_elu),[ov::op::v0::Erf](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_erf),[ov::op::v0::Exp](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_exp),[ov::op::v0::Floor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_floor),[ov::op::v0::GRN](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_g_r_n),[ov::op::v0::Gelu](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_gelu),[ov::op::v0::Log](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_log),[ov::op::v0::Negative](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_negative),[ov::op::v0::Relu](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_relu),[ov::op::v0::Sigmoid](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_sigmoid),[ov::op::v0::Sign](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_sign),[ov::op::v0::Sin](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_sin),[ov::op::v0::Sinh](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_sinh),[ov::op::v0::Sqrt](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_sqrt),[ov::op::v0::Tan](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_tan),[ov::op::v0::Tanh](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_tanh),[ov::op::v3::Acosh](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_acosh),[ov::op::v3::Asinh](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_asinh),[ov::op::v3::Atanh](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_atanh),[ov::op::v4::HSwish](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v4_1_1_h_swish),[ov::op::v4::Mish](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v4_1_1_mish),[ov::op::v4::SoftPlus](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v4_1_1_soft_plus),[ov::op::v5::HSigmoid](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v5_1_1_h_sigmoid),[ov::op::v5::Round](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v5_1_1_round),[ov::op::v7::Gelu](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v7_1_1_gelu),[ov::op::v9::SoftSign](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v9_1_1_soft_sign)Public Functions

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op4util26UnaryElementwiseArithmetic24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual void validate_and_infer_types() override