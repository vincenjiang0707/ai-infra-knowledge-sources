source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v5_1_1_loop.html
lastmod: 

# Class ov::op::v5::Loop[#](https://docs.openvino.ai#class-ov-op-v5-loop)

-
class Loop : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[SubGraphOp](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_sub_graph_op.html#_CPPv4N2ov2op4util10SubGraphOpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v54LoopE) Iterate a body over tensors, accumulating into tensors.

Public Functions

-
Loop(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &trip_count, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &execution_condition)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v54Loop4LoopERK6OutputI4NodeERK6OutputI4NodeE) Constructs a

[Loop](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v5_1_1_loop)operation.

-
virtual
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> get_concatenated_slices(const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &value, int64_t start, int64_t stride, int64_t part_size, int64_t end, int64_t axis) override[#](https://docs.openvino.ai#_CPPv4N2ov2op2v54Loop23get_concatenated_slicesERK6OutputI4NodeE7int64_t7int64_t7int64_t7int64_t7int64_t) Concatenates slices from all iterations.

- Parameters:
**value**– The value supplying slice values from each iteration.**start**– First index on axis of the slicing**stride**– Stepping of the slice**part_size**– Size of the slice on axis**end**– The last index on axis of the slicing**axis**– The axis to slice along

- Returns:
The concatenated slices.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v54Loop24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool evaluate(
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::TensorVector &outputs, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::TensorVector &inputs) const override[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v54Loop8evaluateERN2ov12TensorVectorERKN2ov12TensorVectorE) Evaluates the op on input_values putting results in output_values.

- Parameters:
**output_values**– Tensors for the outputs to compute. One for each result**input_values**– Tensors for the inputs. One for each inputs.

- Returns:
true if successful



-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v54Loop12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
struct SpecialBodyPorts
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v54Loop16SpecialBodyPortsE) Allows to define the purpose of inputs/outputs in the body.


-
Loop(const