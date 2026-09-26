source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v1_1_1_space_to_batch.html
lastmod: 

# Class ov::op::v1::SpaceToBatch[#](https://docs.openvino.ai#class-ov-op-v1-spacetobatch)

-
class SpaceToBatch : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v112SpaceToBatchE) [SpaceToBatch](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_space_to_batch)permutes data tensor blocks of spatial data into batch dimension.Note

Values from spatial blocks dimensions are moved in the batch dimension.

Output node produces a tensor with shape: tensor with shape `[batch * block_shape[0] * block_shape[1] * ... * block_shape[N - 1], (pads_begin[1] + D_1 + pads_end[1]) / block_shape[1], (pads_begin[2] + D_2 + pads_end[2]) / block_shape[2], ..., (pads_begin[N - 1] + D_{N - 1} + pads_end[N - 1]) / block_shape[N - 1]` of the same type as `data` input.

Public Functions

-
SpaceToBatch(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &block_shape, const[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &pads_begin, const[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &pads_end)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v112SpaceToBatch12SpaceToBatchERK6OutputI4NodeERK6OutputI4NodeERK6OutputIN2ov4NodeEERK6OutputIN2ov4NodeEE) Constructs a

[SpaceToBatch](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_space_to_batch)operation.- Parameters:
**data**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing the data tensor**block_shape**– The sizes of the block of values to be moved**pads_begin**– Specifies the padding for the beginning along each axis of`data`

input**pads_end**– Specifies the padding for the ending along each axis of`data`

input.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v112SpaceToBatch24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v112SpaceToBatch12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
SpaceToBatch(const