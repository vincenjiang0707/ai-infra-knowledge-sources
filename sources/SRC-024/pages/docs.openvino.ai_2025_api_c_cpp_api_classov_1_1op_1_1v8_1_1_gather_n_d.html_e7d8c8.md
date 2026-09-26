source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v8_1_1_gather_n_d.html
lastmod: 

# Class ov::op::v8::GatherND[#](https://docs.openvino.ai#class-ov-op-v8-gathernd)

-
class GatherND : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[GatherNDBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_gather_n_d_base.html#_CPPv4N2ov2op4util12GatherNDBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v88GatherNDE) [GatherND](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v8_1_1_gather_n_d)operation.Public Functions

-
GatherND(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &indices, const size_t batch_dims = 0)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v88GatherND8GatherNDERK6OutputI4NodeERK6OutputI4NodeEK6size_t) Constructs a

[GatherND](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v8_1_1_gather_n_d)operation.

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v88GatherND24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
GatherND(const