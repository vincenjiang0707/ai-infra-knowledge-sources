source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v0_1_1_asin.html
lastmod: 

# Class ov::op::v0::Asin[#](https://docs.openvino.ai#class-ov-op-v0-asin)

-
class Asin : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[UnaryElementwiseArithmetic](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_unary_elementwise_arithmetic.html#_CPPv4N2ov2op4util26UnaryElementwiseArithmeticE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v04AsinE) Elementwise inverse sine (arcsin) operation.

Public Functions

-
Asin() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v04Asin4AsinEv) Constructs an arcsin operation.


-
Asin(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v04Asin4AsinERK6OutputI4NodeE) Constructs an arcsin operation.

[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)`[d1, ...]`

- Parameters:
**arg**–[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)that produces the input tensor.`[d1, ...]`



-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v04Asin12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
Asin() = default