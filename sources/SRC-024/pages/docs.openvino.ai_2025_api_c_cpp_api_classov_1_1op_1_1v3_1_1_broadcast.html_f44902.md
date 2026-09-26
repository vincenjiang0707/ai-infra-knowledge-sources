source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v3_1_1_broadcast.html
lastmod: 

# Class ov::op::v3::Broadcast[#](https://docs.openvino.ai#class-ov-op-v3-broadcast)

-
class Broadcast : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[BroadcastBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_broadcast_base.html#_CPPv4N2ov2op4util13BroadcastBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v39BroadcastE) Operation which “adds” axes to an input tensor, replicating elements from the input as needed along the new axes.

Public Functions

-
Broadcast() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v39Broadcast9BroadcastEv) Constructs a broadcast operation.


-
Broadcast(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &target_shape, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &axes_mapping, const[BroadcastModeSpec](https://docs.openvino.ai/structov_1_1op_1_1_broadcast_mode_spec.html#_CPPv4N2ov2op17BroadcastModeSpecE)&broadcast_spec =[BroadcastType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op13BroadcastTypeE)::[EXPLICIT](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op13BroadcastType8EXPLICITE))[#](https://docs.openvino.ai#_CPPv4N2ov2op2v39Broadcast9BroadcastERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK17BroadcastModeSpec) Constructs a broadcast operation.

- Parameters:
**arg**– The input tensor to be broadcast.**target_shape**– The shape of the output tensor.**axes_mapping**– The axis positions (0-based) in the result that correspond to input axes. ‘Arg’ tensor is broadcast along the remaining axes. E.g.,[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)[Shape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_shape)- [3, 4], Target[Shape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_shape)- [3, 5, 4, 4] axes_mapping - [0, 2] =>[Broadcast](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_broadcast)along axes 1 and 3. axes_mapping - [0, 3] =>[Broadcast](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_broadcast)along axes 1 and 2.**broadcast_spec**–[Broadcast](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_broadcast)specification to use for determining broadcast axes. ‘axes_mapping’ should not be provided if mode other than explicit (none) is used.



-
Broadcast(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &target_shape, const[BroadcastModeSpec](https://docs.openvino.ai/structov_1_1op_1_1_broadcast_mode_spec.html#_CPPv4N2ov2op17BroadcastModeSpecE)&broadcast_spec =[BroadcastType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op13BroadcastTypeE)::[NUMPY](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op13BroadcastType5NUMPYE))[#](https://docs.openvino.ai#_CPPv4N2ov2op2v39Broadcast9BroadcastERK6OutputI4NodeERK6OutputI4NodeERK17BroadcastModeSpec) Constructs a broadcast operation.

- Parameters:
**arg**– The input tensor to be broadcast.**target_shape**– The shape of the output tensor.**broadcast_spec**–[Broadcast](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_broadcast)specification to use for determining broadcast axes



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v39Broadcast24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual std::pair<bool,
[AxisSet](https://docs.openvino.ai/classov_1_1_axis_set.html#_CPPv4N2ov7AxisSetE)> get_broadcast_axes() const override[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v39Broadcast18get_broadcast_axesEv) - Returns:
true and the

[AxisSet](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_axis_set)if broadcast axes can be fully determined.


-
virtual bool evaluate(
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::TensorVector &outputs, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::TensorVector &inputs) const override[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v39Broadcast8evaluateERN2ov12TensorVectorERKN2ov12TensorVectorE) Evaluates the op on input_values putting results in output_values.

- Parameters:
**output_values**– Tensors for the outputs to compute. One for each result**input_values**– Tensors for the inputs. One for each inputs.

- Returns:
true if successful



-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v39Broadcast12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
Broadcast() = default