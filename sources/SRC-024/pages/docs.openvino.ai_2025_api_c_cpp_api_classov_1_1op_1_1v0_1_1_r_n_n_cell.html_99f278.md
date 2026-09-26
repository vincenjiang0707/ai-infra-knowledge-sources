source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v0_1_1_r_n_n_cell.html
lastmod: 

# Class ov::op::v0::RNNCell[#](https://docs.openvino.ai#class-ov-op-v0-rnncell)

-
class RNNCell : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[RNNCellBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_r_n_n_cell_base.html#_CPPv4N2ov2op4util11RNNCellBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v07RNNCellE) Class for single RNN cell node.

See also

LSTMSequence,

[LSTMCell](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_l_s_t_m_cell), GRUCellNote

It follows notation and equations defined as in ONNX standard:

[onnx/onnx](https://github.com/onnx/onnx/blob/master/docs/Operators.md#RNN)Note

It calculates following equations:

Ht = f(Xt*(Wi^T) + Ht-1*(Ri^T) + Wbi + Rbi) * - Is a dot product, f - is activation functions.

Note

This class represents only single

*cell*(for current time step) and not the whole RNN Sequence layerPublic Functions

-
RNNCell(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &X, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &initial_hidden_state, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &W, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &R, std::size_t hidden_size, const std::vector<std::string> &activations = std::vector<std::string>{"tanh"}, const std::vector<float> &activations_alpha = {}, const std::vector<float> &activations_beta = {}, float clip = 0.f)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v07RNNCell7RNNCellERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeENSt6size_tERKNSt6vectorINSt6stringEEERKNSt6vectorIfEERKNSt6vectorIfEEf) Constructs

[RNNCell](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_r_n_n_cell)node.- Parameters:
**X**–**[in]**The input tensor with shape: [batch_size, input_size].**initial_hidden_state**–**[in]**The hidden state tensor at current time step with shape: [batch_size, hidden_size].**W**–**[in]**The weight tensor with shape: [hidden_size, input_size].**R**–**[in]**The recurrence weight tensor with shape: [hidden_size, hidden_size].**hidden_size**–**[in]**The number of hidden units for recurrent cell.**activations**–**[in]**The vector of activation functions used inside recurrent cell.**activations_alpha**–**[in]**The vector of alpha parameters for activation functions in order respective to activation list.**activations_beta**–**[in]**The vector of beta parameters for activation functions in order respective to activation list.**clip**–**[in]**The value defining clipping range [-clip, clip] on input of activation functions.



-
RNNCell(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &X, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &initial_hidden_state, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &W, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &R, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &B, std::size_t hidden_size, const std::vector<std::string> &activations = std::vector<std::string>{"tanh"}, const std::vector<float> &activations_alpha = {}, const std::vector<float> &activations_beta = {}, float clip = 0.f)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v07RNNCell7RNNCellERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeENSt6size_tERKNSt6vectorINSt6stringEEERKNSt6vectorIfEERKNSt6vectorIfEEf) Constructs

[RNNCell](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_r_n_n_cell)node.- Parameters:
**X**–**[in]**The input tensor with shape: [batch_size, input_size].**initial_hidden_state**–**[in]**The hidden state tensor at current time step with shape: [batch_size, hidden_size].**W**–**[in]**The weight tensor with shape: [hidden_size, input_size].**R**–**[in]**The recurrence weight tensor with shape: [hidden_size, hidden_size].**B**–**[in]**The bias tensor for input gate with shape: [hidden_size].**hidden_size**–**[in]**The number of hidden units for recurrent cell.**activations**–**[in]**The vector of activation functions used inside recurrent cell.**activations_alpha**–**[in]**The vector of alpha parameters for activation functions in order respective to activation list.**activations_beta**–**[in]**The vector of beta parameters for activation functions in order respective to activation list.**clip**–**[in]**The value defining clipping range [-clip, clip] on input of activation functions.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v07RNNCell24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
RNNCell(const