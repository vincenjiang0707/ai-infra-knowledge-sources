source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v1_1_1_select.html
lastmod: 

# Class ov::op::v1::Select[#](https://docs.openvino.ai#class-ov-op-v1-select)

-
class Select : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v16SelectE) Elementwise selection operation.

*Inputs*Type

Description

`arg0`

\(\texttt{bool}[d_1,\dots,d_n]~(n \geq 0)\)

A tensor of any shape, with element

`bool`

.`arg1`

\(E[d_1,\dots,d_n]~(n \geq 0)\)

A tensor of a shape that is broadcast-compatible with

`arg0`

, with any element type.`arg2`

\(E[d_1,\dots,d_n]~(n \geq 0)\)

A tensor of a shape that is broadcast-compatible with

`arg0`

, and same element type as`arg1`

.`auto_broadcast`

Auto broadcast specification.

Type

Description

\(E[d_1,\dots,d_n]\)

The tensor \(T\), where \(T[i_1,\dots,i_n] = \texttt{arg1}[i_1,\dots,i_n]\text{ if }\texttt{arg0}[i_1,\dots,i_n] \neq 0\text{, else }\texttt{arg2}[i_1,\dots,i_n]\)

Public Functions

-
inline Select()
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v16Select6SelectEv) Constructs a selection operation.


-
Select(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg0, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg1, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg2, const[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)&auto_broadcast =[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)([AutoBroadcastType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastTypeE)::[NUMPY](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastType5NUMPYE)))[#](https://docs.openvino.ai#_CPPv4N2ov2op2v16Select6SelectERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK17AutoBroadcastSpec) Constructs a selection operation.


-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v16Select24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
inline virtual const
[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)&get_autob() const override[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v16Select9get_autobEv) - Returns:
the autobroadcasr spec



-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v16Select12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
inline Select()