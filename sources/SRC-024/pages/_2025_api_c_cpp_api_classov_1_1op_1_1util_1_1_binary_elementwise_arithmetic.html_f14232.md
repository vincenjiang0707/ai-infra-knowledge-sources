source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1util_1_1_binary_elementwise_arithmetic.html
lastmod: 

# Class ov::op::util::BinaryElementwiseArithmetic[#](https://docs.openvino.ai#class-ov-op-util-binaryelementwisearithmetic)

-
class BinaryElementwiseArithmetic : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op4util27BinaryElementwiseArithmeticE) Abstract base class for elementwise binary arithmetic operations, i.e., operations where the same scalar binary arithmetic operation is applied to each corresponding pair of elements in the two input tensors. Implicit broadcast of input tensors is supported through one of the AutoBroadcast modes.

For example, if the underlying arithmetic operation (determined by the subclass) is \(\mathit{op}(x,y)\), the input tensors \([[x_0,y_0],[z_0,w_0]]\) and \([[x_1,y_1],[z_1,w_1]]\) will be mapped to \([[\mathit{op}(x_0,x_1),\mathit{op}(y_0,y_1)],[\mathit{op}(z_0,z_1),\mathit{op}(w_0,w_1)]]\).

*Inputs*Type

Description

`arg0`

\(N[d_1,\dots,d_n]~(n \geq 0)\)

A tensor of any shape. The element type \(N\) may be any numeric type.

`arg1`

\(N[d_1,\dots,d_n]~(n \geq 0)\)

A tensor of the same element type as

`arg0`

.`autob`

Auto broadcast specification.

Type

Description

\(N[d_1,\dots,d_n]\)

The tensor \(T\), where \(T[i_1,\dots,i_n] = \mathit{op}(\texttt{arg0}[i_1,\dots,i_n],\texttt{arg1}[i_1,\dots,i_n])\). This will always have the same shape and element type as the input tensors (after auto broadcasting).

Subclassed by

[ov::op::v0::SquaredDifference](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_squared_difference),[ov::op::v1::Add](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_add),[ov::op::v1::Divide](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_divide),[ov::op::v1::FloorMod](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_floor_mod),[ov::op::v1::Maximum](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_maximum),[ov::op::v1::Minimum](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_minimum),[ov::op::v1::Mod](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_mod),[ov::op::v1::Multiply](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_multiply),[ov::op::v1::Power](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_power),[ov::op::v1::Subtract](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_subtract)Public Functions

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op4util27BinaryElementwiseArithmetic24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
inline virtual const
[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)&get_autob() const override[#](https://docs.openvino.ai#_CPPv4NK2ov2op4util27BinaryElementwiseArithmetic9get_autobEv) - Returns:
the autobroadcasr spec



-
virtual void validate_and_infer_types() override