source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v1_1_1_broadcast.html
lastmod: 

# Class ov::op::v1::Broadcast[#](https://docs.openvino.ai#class-ov-op-v1-broadcast)

-
class Broadcast : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[BroadcastBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_broadcast_base.html#_CPPv4N2ov2op4util13BroadcastBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v19BroadcastE) Operation which “adds” axes to an input tensor, replicating elements from the input as needed along the new axes.

Public Functions

-
Broadcast() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v19Broadcast9BroadcastEv) Constructs a broadcast operation.


-
Broadcast(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &target_shape, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &axes_mapping, const[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)&broadcast_spec =[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)())[#](https://docs.openvino.ai#_CPPv4N2ov2op2v19Broadcast9BroadcastERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK17AutoBroadcastSpec) Constructs a broadcast operation.

- Parameters:
**arg**– The input tensor to be broadcast.**target_shape**– The shape of the output tensor.**axes_mapping**– The axis positions (0-based) in the result that correspond to input axes. ‘Arg’ tensor is broadcast along the remaining axes. E.g.,[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)[Shape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_shape)- [3, 4], Target[Shape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_shape)- [3, 5, 4, 4] axes_mapping - [0, 2] =>[Broadcast](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_broadcast)along axes 1 and 3. axes_mapping - [0, 3] =>[Broadcast](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_broadcast)along axes 1 and 2.**broadcast_spec**–[Broadcast](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_broadcast)specification to use for determining broadcast axes. ‘axes_mapping’ is ignored if broadcast_spec is not NONE



-
Broadcast(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &target_shape, const[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)&broadcast_spec =[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)([AutoBroadcastType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastTypeE)::[NUMPY](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastType5NUMPYE)))[#](https://docs.openvino.ai#_CPPv4N2ov2op2v19Broadcast9BroadcastERK6OutputI4NodeERK6OutputI4NodeERK17AutoBroadcastSpec) Constructs a broadcast operation.

- Parameters:
**arg**– The input tensor to be broadcast.**target_shape**– The shape of the output tensor.**broadcast_spec**–[Broadcast](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_broadcast)specification to use for determining broadcast axes



-
inline const
[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)&get_broadcast_spec() const[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v19Broadcast18get_broadcast_specEv) - Returns:
[Broadcast](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_broadcast)Specification.


-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v19Broadcast24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool evaluate(
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::TensorVector &outputs, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::TensorVector &inputs) const override[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v19Broadcast8evaluateERN2ov12TensorVectorERKN2ov12TensorVectorE) Evaluates the op on input_values putting results in output_values.

- Parameters:
**output_values**– Tensors for the outputs to compute. One for each result**input_values**– Tensors for the inputs. One for each inputs.

- Returns:
true if successful



-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v19Broadcast12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
Broadcast() = default