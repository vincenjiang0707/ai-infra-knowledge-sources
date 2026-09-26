source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1util_1_1_gather_base.html
lastmod: 

# Class ov::op::util::GatherBase[#](https://docs.openvino.ai#class-ov-op-util-gatherbase)

-
class GatherBase : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op4util10GatherBaseE) [GatherBase](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_gather_base)basic class for Gather[v1](https://docs.openvino.ai/group__ov__transformation__common__api.html#namespaceov_1_1op_1_1v1)and[v7](https://docs.openvino.ai/group__ov__transformation__common__api.html#namespaceov_1_1op_1_1v7).Subclassed by

[ov::op::v1::Gather](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_gather),[ov::op::v7::Gather](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v7_1_1_gather),[ov::op::v8::Gather](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v8_1_1_gather)Public Functions

-
GatherBase(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &indices, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &axis, const int64_t batch_dims = 0)[#](https://docs.openvino.ai#_CPPv4N2ov2op4util10GatherBase10GatherBaseERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeEK7int64_t) - Parameters:
**data**– The tensor from which slices are gathered**indices**–[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)with indexes to gather**axis**– The tensor is a dimension index to gather data from**batch_dims**– The number of batch dimension in data and indices tensors



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op4util10GatherBase24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op4util10GatherBase12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
GatherBase(const