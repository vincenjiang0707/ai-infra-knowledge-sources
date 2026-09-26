source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v0_1_1_elu.html
lastmod: 

# Class ov::op::v0::Elu[#](https://docs.openvino.ai#class-ov-op-v0-elu)

-
class Elu : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[UnaryElementwiseArithmetic](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_unary_elementwise_arithmetic.html#_CPPv4N2ov2op4util26UnaryElementwiseArithmeticE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v03EluE) Exponential Linear Unit x < 0 => f(x) = alpha * (exp(x) - 1.) x >= 0 => f(x) = x.

Public Functions

-
Elu(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const double alpha)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v03Elu3EluERK6OutputI4NodeEKd) Constructs an

[Elu](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_elu)operation.- Parameters:
**data**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)tensor**alpha**– Multiplier for negative values



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v03Elu24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
Elu(const