source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v3_1_1_scatter_elements_update.html
lastmod: 

# Class ov::op::v3::ScatterElementsUpdate[#](https://docs.openvino.ai#class-ov-op-v3-scatterelementsupdate)

-
class ScatterElementsUpdate : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[ScatterElementsUpdateBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_scatter_elements_update_base.html#_CPPv4N2ov2op4util25ScatterElementsUpdateBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v321ScatterElementsUpdateE) [ScatterElementsUpdate](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_scatter_elements_update)operation.Public Functions

-
ScatterElementsUpdate(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &indices, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &updates, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &axis)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v321ScatterElementsUpdate21ScatterElementsUpdateERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeE) Constructs a

[ScatterElementsUpdate](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_scatter_elements_update)node.- Parameters:
**data**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)data**indices**– Data entry index that will be updated**updates**– Update values**axis**– Axis to scatter on



-
ScatterElementsUpdate(const