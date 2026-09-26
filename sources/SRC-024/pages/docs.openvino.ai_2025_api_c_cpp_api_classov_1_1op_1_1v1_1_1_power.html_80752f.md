source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v1_1_1_power.html
lastmod: 

# Class ov::op::v1::Power[#](https://docs.openvino.ai#class-ov-op-v1-power)

-
class Power : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[BinaryElementwiseArithmetic](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_binary_elementwise_arithmetic.html#_CPPv4N2ov2op4util27BinaryElementwiseArithmeticE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v15PowerE) Elementwise exponentiation operation.

*Inputs*Type

Description

`arg0`

\(N[d_1,\dots,d_n]~(n \geq 0)\)

A tensor of any shape and numeric element type.

`arg1`

\(N[d_1,\dots,d_n]~(n \geq 0)\)

A tensor of the same shape and element type as

`arg0`

.Type

Description

\(N[d_1,\dots,d_n]\)

The tensor \(T\), where \(T[i_1,\dots,i_n] = \texttt{arg0}[i_1,\dots,i_n]^{\texttt{arg1}[i_1,\dots,i_n]}\)

Public Functions

-
Power(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg0, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg1, const[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)&auto_broadcast =[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)([AutoBroadcastType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastTypeE)::[NUMPY](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastType5NUMPYE)))[#](https://docs.openvino.ai#_CPPv4N2ov2op2v15Power5PowerERK6OutputI4NodeERK6OutputI4NodeERK17AutoBroadcastSpec) Constructs an exponentiation operation.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v15Power12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
Power(const