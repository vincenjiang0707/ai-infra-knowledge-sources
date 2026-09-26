source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v0_1_1_depth_to_space.html
lastmod: 

# Class ov::op::v0::DepthToSpace[#](https://docs.openvino.ai#class-ov-op-v0-depthtospace)

-
class DepthToSpace : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v012DepthToSpaceE) [DepthToSpace](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_depth_to_space)permutes data from the depth dimension of the input blob into spatial dimensions.[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)node produces a tensor with shape: [N, C/(blocksize * blocksize), H * blocksize, W * blocksize]Note

Values from the depth dimension (assuming NCHW layout) are moved in spatial blocks to the height and width dimensions.

Public Functions

-
DepthToSpace(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const DepthToSpaceMode &mode, std::size_t block_size = 1)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v012DepthToSpace12DepthToSpaceERK6OutputI4NodeERK16DepthToSpaceModeNSt6size_tE) Constructs a

[DepthToSpace](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_depth_to_space)operation.- Parameters:
**data**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing the input tensor**mode**– Specifies how the input depth dimension is split to block coordinates**block_size**– The size of the block of values to be moved



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v012DepthToSpace24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v012DepthToSpace12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
DepthToSpace(const