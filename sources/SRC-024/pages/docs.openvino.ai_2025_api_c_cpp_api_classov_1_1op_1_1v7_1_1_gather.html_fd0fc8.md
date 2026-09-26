source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v7_1_1_gather.html
lastmod: 

# Class ov::op::v7::Gather[#](https://docs.openvino.ai#class-ov-op-v7-gather)

-
class Gather : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[GatherBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_gather_base.html#_CPPv4N2ov2op4util10GatherBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v76GatherE) [Gather](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v7_1_1_gather)slices from axis of data according to indices.Public Functions

-
Gather(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &indices, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &axis, const int64_t batch_dims = 0)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v76Gather6GatherERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeEK7int64_t)

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v76Gather24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
Gather(const