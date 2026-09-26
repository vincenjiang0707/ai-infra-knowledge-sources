source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v3_1_1_scatter_update.html
lastmod: 

# Class ov::op::v3::ScatterUpdate[#](https://docs.openvino.ai#class-ov-op-v3-scatterupdate)

-
class ScatterUpdate : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[ScatterBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_scatter_base.html#_CPPv4N2ov2op4util11ScatterBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v313ScatterUpdateE) Set new values to slices from data addressed by indices.

Public Functions

-
ScatterUpdate(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &indices, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &updates, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &axis)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v313ScatterUpdate13ScatterUpdateERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeE) Constructs

[ScatterUpdate](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_scatter_update)operator object.- Parameters:
**data**– The input tensor to be updated.**indices**– The tensor with indexes which will be updated.**updates**– The tensor with update values.**axis**–**[in]**The axis at which elements will be updated.



-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v313ScatterUpdate12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
ScatterUpdate(const