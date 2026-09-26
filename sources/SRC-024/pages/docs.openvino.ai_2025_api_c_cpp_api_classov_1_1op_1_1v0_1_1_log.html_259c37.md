source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v0_1_1_log.html
lastmod: 

# Class ov::op::v0::Log[#](https://docs.openvino.ai#class-ov-op-v0-log)

-
class Log : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[UnaryElementwiseArithmetic](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_unary_elementwise_arithmetic.html#_CPPv4N2ov2op4util26UnaryElementwiseArithmeticE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v03LogE) Elementwise natural log operation.

Public Functions

-
Log() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v03Log3LogEv) Constructs a natural log operation.


-
Log(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v03Log3LogERK6OutputI4NodeE) Constructs a natural log operation.

- Parameters:
**arg**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)that produces the input tensor.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v03Log12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
Log() = default