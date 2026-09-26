source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v8_1_1_gather.html
lastmod: 

# Class ov::op::v8::Gather[#](https://docs.openvino.ai#class-ov-op-v8-gather)

-
class Gather : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[GatherBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_gather_base.html#_CPPv4N2ov2op4util10GatherBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v86GatherE) [Gather](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v8_1_1_gather)slices from axis of data according to indices. Negative indices are supported and indicate reverse indexing from the end.Subclassed by

[ov::op::internal::GatherCompressed](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1internal_1_1_gather_compressed)Public Functions

-
Gather(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &indices, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &axis, const int64_t batch_dims = 0)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v86Gather6GatherERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeEK7int64_t) - Parameters:
**data**– The tensor from which slices are gathered**indices**–[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)with indexes to gather**axis**– The tensor is a dimension index to gather data from**batch_dims**– The number of batch dimension in data and indices tensors.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v86Gather24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
Gather(const