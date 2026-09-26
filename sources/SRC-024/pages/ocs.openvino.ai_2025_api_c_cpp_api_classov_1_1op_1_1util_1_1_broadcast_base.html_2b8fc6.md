source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1util_1_1_broadcast_base.html
lastmod: 

# Class ov::op::util::BroadcastBase[#](https://docs.openvino.ai#class-ov-op-util-broadcastbase)

-
class BroadcastBase : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op4util13BroadcastBaseE) Subclassed by

[ov::op::v1::Broadcast](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_broadcast),[ov::op::v3::Broadcast](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_broadcast)Public Functions

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op4util13BroadcastBase24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual std::pair<bool,
[AxisSet](https://docs.openvino.ai/classov_1_1_axis_set.html#_CPPv4N2ov7AxisSetE)> get_broadcast_axes() const[#](https://docs.openvino.ai#_CPPv4NK2ov2op4util13BroadcastBase18get_broadcast_axesEv) - Returns:
true and the

[AxisSet](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_axis_set)if broadcast axes can be fully determined.


-
virtual bool evaluate(
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::TensorVector &outputs, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::TensorVector &inputs) const override[#](https://docs.openvino.ai#_CPPv4NK2ov2op4util13BroadcastBase8evaluateERN2ov12TensorVectorERKN2ov12TensorVectorE) Evaluates the op on input_values putting results in output_values.

- Parameters:
**output_values**– Tensors for the outputs to compute. One for each result**input_values**– Tensors for the inputs. One for each inputs.

- Returns:
true if successful



-
virtual void validate_and_infer_types() override