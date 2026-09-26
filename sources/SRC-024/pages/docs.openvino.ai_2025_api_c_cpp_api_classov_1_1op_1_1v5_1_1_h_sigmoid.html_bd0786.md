source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v5_1_1_h_sigmoid.html
lastmod: 

A [HSigmoid](group__ov__transformation__common__api.html#classov_1_1op_1_1v5_1_1_h_sigmoid) Activation Function f(x) = min(max(x + 3, 0), 6) / 6 or f(x) = min(ReLU(x + 3), 6) / 6.

Public Functions

-
HSigmoid(const
[Output](group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg)

Constructs a [HSigmoid](group__ov__transformation__common__api.html#classov_1_1op_1_1v5_1_1_h_sigmoid) operation.

- Parameters:
**data** – [Input](group__ov__transformation__common__api.html#classov_1_1_input) tensor



-
virtual bool has_evaluate() const override

Allows to get information about availability of evaluate method for the current operation.