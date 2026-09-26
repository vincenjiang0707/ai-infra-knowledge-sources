source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v3_1_1_scatter_n_d_update.html
lastmod: 

# Class ov::op::v3::ScatterNDUpdate[#](https://docs.openvino.ai#class-ov-op-v3-scatterndupdate)

-
class ScatterNDUpdate : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[ScatterNDBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_scatter_n_d_base.html#_CPPv4N2ov2op4util13ScatterNDBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v315ScatterNDUpdateE) Add updates to slices from inputs addressed by indices.

Public Functions

-
inline ScatterNDUpdate(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &inputs, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &indices, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &updates)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v315ScatterNDUpdate15ScatterNDUpdateERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeE) - Parameters:
**inputs**–[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)**indices**– Index tensor: Data type must be

or[element::i32](https://docs.openvino.ai/group__ov__transformation__common__api.html#group__ov__element__cpp__api_1ga53dd97bfbd724cee3266cc80d758f323)[element::i64](https://docs.openvino.ai/group__ov__transformation__common__api.html#group__ov__element__cpp__api_1ga6c86a9a54d44fc205ad9cbf28ca556a6)**updates**–[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor): Must have same type as inputs



-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v315ScatterNDUpdate12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
inline ScatterNDUpdate(const