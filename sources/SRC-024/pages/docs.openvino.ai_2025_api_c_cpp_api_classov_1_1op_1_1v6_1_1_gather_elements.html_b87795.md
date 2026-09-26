source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v6_1_1_gather_elements.html
lastmod: 

# Class ov::op::v6::GatherElements[#](https://docs.openvino.ai#class-ov-op-v6-gatherelements)

-
class GatherElements : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v614GatherElementsE) [GatherElements](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v6_1_1_gather_elements)operation.Public Functions

-
GatherElements(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &indices, const int64_t axis)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v614GatherElements14GatherElementsERK6OutputI4NodeERK6OutputI4NodeEK7int64_t) Constructs a

[GatherElements](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v6_1_1_gather_elements)operation.

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v614GatherElements24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
GatherElements(const