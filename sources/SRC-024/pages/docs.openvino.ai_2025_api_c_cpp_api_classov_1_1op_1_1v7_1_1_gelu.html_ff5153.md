source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v7_1_1_gelu.html
lastmod: 

# Class ov::op::v7::Gelu[#](https://docs.openvino.ai#class-ov-op-v7-gelu)

-
class Gelu : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[UnaryElementwiseArithmetic](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_unary_elementwise_arithmetic.html#_CPPv4N2ov2op4util26UnaryElementwiseArithmeticE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v74GeluE) Gaussian Error Linear Unit f(x) = 0.5 * x * (1 + erf( x / sqrt(2) ) for “approximation” = “erf” f(x) = 0.5 * x * (1 + tanh([sqrt(2 / pi)] * [x + 0.044715^3]) for “approximation” = “tanh”.

Public Functions

-
Gelu(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data,[GeluApproximationMode](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op21GeluApproximationModeE)mode =[GeluApproximationMode](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op21GeluApproximationModeE)::[ERF](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op21GeluApproximationMode3ERFE))[#](https://docs.openvino.ai#_CPPv4N2ov2op2v74Gelu4GeluERK6OutputI4NodeE21GeluApproximationMode) Constructs a

[Gelu](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v7_1_1_gelu)operation.- Parameters:
**data**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)tensor**mode**– Approximation mode



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v74Gelu24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v74Gelu12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
Gelu(const