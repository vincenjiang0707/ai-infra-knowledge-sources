source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v12_1_1_group_normalization.html
lastmod: 

# Class ov::op::v12::GroupNormalization[#](https://docs.openvino.ai#class-ov-op-v12-groupnormalization)

-
class GroupNormalization : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1218GroupNormalizationE) [GroupNormalization](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v12_1_1_group_normalization)operation over the input tensor.Public Functions

-
GroupNormalization(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &scale, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &bias, int64_t num_groups, double epsilon)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1218GroupNormalization18GroupNormalizationERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeE7int64_td) - Parameters:
**data**– The input tensor to be normalized**scale**– The tensor containing scale values for each channel**bias**– The tensor containing bias values for each channel**num_groups**– The number of groups that the channel dimension will be divided into**epsilon**– The value that prevents divisions by zero in[GroupNormalization](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v12_1_1_group_normalization)formula



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1218GroupNormalization24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
GroupNormalization(const