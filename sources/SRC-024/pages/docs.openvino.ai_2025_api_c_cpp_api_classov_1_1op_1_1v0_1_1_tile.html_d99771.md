source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v0_1_1_tile.html
lastmod: 

# Class ov::op::v0::Tile[#](https://docs.openvino.ai#class-ov-op-v0-tile)

-
class Tile : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v04TileE) Dynamic Tiling operation which repeats a tensor multiple times along each dimension.

Public Functions

-
Tile(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &repeats)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v04Tile4TileERK6OutputI4NodeERK6OutputI4NodeE) Perform dynamic padding of a tensor.

- Parameters:
**data**– The node producing input tensor to be padded.**repeats**– The node producing the per-dimension replication factor



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v04Tile24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v04Tile12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
virtual bool evaluate(
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::TensorVector &outputs, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::TensorVector &inputs) const override[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v04Tile8evaluateERN2ov12TensorVectorERKN2ov12TensorVectorE) Evaluates the op on input_values putting results in output_values.

- Parameters:
**output_values**– Tensors for the outputs to compute. One for each result**input_values**– Tensors for the inputs. One for each inputs.

- Returns:
true if successful



-
Tile(const