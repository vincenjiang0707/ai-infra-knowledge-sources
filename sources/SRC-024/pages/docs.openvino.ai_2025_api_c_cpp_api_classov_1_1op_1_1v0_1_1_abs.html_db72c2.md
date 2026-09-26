source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v0_1_1_abs.html
lastmod: 

# Class ov::op::v0::Abs[#](https://docs.openvino.ai#class-ov-op-v0-abs)

-
class Abs : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[UnaryElementwiseArithmetic](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_unary_elementwise_arithmetic.html#_CPPv4N2ov2op4util26UnaryElementwiseArithmeticE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v03AbsE) Elementwise absolute value operation.

Public Functions

-
Abs() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v03Abs3AbsEv) Constructs an absolute value operation.


-
Abs(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v03Abs3AbsERK6OutputI4NodeE) Constructs an absolute value operation.

[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)`[d1, ...]`

- Parameters:
**arg**–[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)that produces the input tensor.`[d1, ...]`



-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v03Abs12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
Abs() = default