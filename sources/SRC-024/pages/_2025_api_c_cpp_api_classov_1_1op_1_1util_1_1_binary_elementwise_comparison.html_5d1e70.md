source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1util_1_1_binary_elementwise_comparison.html
lastmod: 

# Class ov::op::util::BinaryElementwiseComparison[#](https://docs.openvino.ai#class-ov-op-util-binaryelementwisecomparison)

-
class BinaryElementwiseComparison : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op4util27BinaryElementwiseComparisonE) Abstract base class for elementwise binary comparison operations, i.e., operations where the same scalar binary comparison operation is applied to each corresponding pair of elements in two input tensors. Implicit broadcast of input tensors is supported through one of the AutoBroadcast modes.

For example, if the underlying comparison operation (determined by the subclass) is \(\mathit{op}(x,y)\), the input tensors \([[x_0,y_0],[z_0,w_0]]\) and \([[x_1,y_1],[z_1,w_1]]\) will be mapped to \([[\mathit{op}(x_0,x_1),\mathit{op}(y_0,y_1)],[\mathit{op}(z_0,z_1),\mathit{op}(w_0,w_1)]]\).

*Inputs*Type

Description

`arg0`

\(E[d_1,\dots,d_n]~(n \geq 0)\)

A tensor of any shape and element type.

`arg1`

\(E[d_1,\dots,d_n]~(n \geq 0)\)

A tensor of the same shape and element type as

`arg0`

.`autob`

Auto broadcast specification.

Type

Description

\(\texttt{bool}[d_1,\dots,d_n]\)

The tensor \(T\), where \(T[i_1,\dots,i_n] = \mathit{op}(\texttt{arg0}[i_1,\dots,i_n],\texttt{arg1}[i_1,\dots,i_n])\). This will always have the same shape as the input tensors, and the element type

`bool`

.Subclassed by

[ov::op::v1::Equal](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_equal),[ov::op::v1::Greater](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_greater),[ov::op::v1::GreaterEqual](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_greater_equal),[ov::op::v1::Less](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_less),[ov::op::v1::LessEqual](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_less_equal),[ov::op::v1::NotEqual](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_not_equal)Public Functions

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op4util27BinaryElementwiseComparison24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
inline virtual const
[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)&get_autob() const override[#](https://docs.openvino.ai#_CPPv4NK2ov2op4util27BinaryElementwiseComparison9get_autobEv) - Returns:
the autobroadcasr spec



-
virtual void validate_and_infer_types() override