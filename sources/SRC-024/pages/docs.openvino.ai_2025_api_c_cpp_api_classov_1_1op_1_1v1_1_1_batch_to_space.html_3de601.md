source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v1_1_1_batch_to_space.html
lastmod: 

# Class ov::op::v1::BatchToSpace[#](https://docs.openvino.ai#class-ov-op-v1-batchtospace)

-
class BatchToSpace : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v112BatchToSpaceE) [BatchToSpace](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_batch_to_space)permutes data from the batch dimension of the data tensor into spatial dimensions.Note

Values from the batch dimension are moved in spatial blocks dimensions.

Output node produces a tensor with shape: `[batch / (block_shape[0] * block_shape[1] * ... * block_shape[N - 1]), D_1 * block_shape[1] - crops_begin[1] - crops_end[1], D_2 * block_shape[2] - crops_begin[2] - crops_end[2], ..., D_{N - 1} * block_shape[N - 1] - crops_begin[N - 1] - crops_end[N - 1]` of the same type as `data` input.

Public Functions

-
BatchToSpace(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &block_shape, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &crops_begin, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &crops_end)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v112BatchToSpace12BatchToSpaceERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeE) Constructs a

[BatchToSpace](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_batch_to_space)operation.- Parameters:
**data**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing the data tensor**block_shape**– The sizes of the block of values to be moved**crops_begin**– Specifies the amount to crop from the beginning along each axis of`data`

input**crops_end**– Specifies the amount to crop from the ending along each axis of`data`

input.



-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v112BatchToSpace12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v112BatchToSpace24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
BatchToSpace(const