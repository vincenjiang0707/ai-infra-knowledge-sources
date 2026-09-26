source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v0_1_1_cosh.html
lastmod: 

# Class ov::op::v0::Cosh[#](https://docs.openvino.ai#class-ov-op-v0-cosh)

-
class Cosh : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[UnaryElementwiseArithmetic](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_unary_elementwise_arithmetic.html#_CPPv4N2ov2op4util26UnaryElementwiseArithmeticE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v04CoshE) Elementwise hyperbolic cosine (cosh) operation.

Public Functions

-
Cosh() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v04Cosh4CoshEv) Constructs a hyperbolic cosine operation.


-
Cosh(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v04Cosh4CoshERK6OutputI4NodeE) Constructs a hyperbolic cosine operation.

- Parameters:
**arg**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)that produces the input tensor.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v04Cosh12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
Cosh() = default