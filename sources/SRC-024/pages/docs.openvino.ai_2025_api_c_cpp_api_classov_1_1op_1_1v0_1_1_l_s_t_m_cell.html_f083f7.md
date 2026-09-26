source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v0_1_1_l_s_t_m_cell.html
lastmod: 

# Class ov::op::v0::LSTMCell[#](https://docs.openvino.ai#class-ov-op-v0-lstmcell)

-
class LSTMCell : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[RNNCellBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_r_n_n_cell_base.html#_CPPv4N2ov2op4util11RNNCellBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v08LSTMCellE) Class for single lstm cell node.

See also

LSTMSequence,

[RNNCell](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_r_n_n_cell), GRUCellNote

Following implementation supports:

`peepholes`

Gers & Schmidhuber (2000)[https://ieeexplore.ieee.org/document/861302](https://ieeexplore.ieee.org/document/861302)Coupling input and forget gates.


Note

It calculates following equations:

it = f(Xt*(Wi^T) + Ht-1*(Ri^T) + Pi (.) Ct-1 + Wbi + Rbi) ft = f(Xt*(Wf^T) + Ht-1*(Rf^T) + Pf (.) Ct-1 + Wbf + Rbf) ct = g(Xt*(Wc^T) + Ht-1*(Rc^T) + Wbc + Rbc) Ct = ft (.) Ct-1 + it (.) ct ot = f(Xt*(Wo^T) + Ht-1*(Ro^T) + Po (.) Ct + Wbo + Rbo) Ht = ot (.) h(Ct) * - Is a dot product, (.) - is a Hadamard product (element-wise), f, g, h - are activation functions.

Note

This class represents only single

*cell*(for current time step) and not the whole LSTM Sequence layerPublic Functions

-
LSTMCell(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &X, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &initial_hidden_state, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &initial_cell_state, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &W, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &R, std::size_t hidden_size,[LSTMWeightsFormat](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17LSTMWeightsFormatE)weights_format =[LSTMWeightsFormat](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17LSTMWeightsFormatE)::[IFCO](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17LSTMWeightsFormat4IFCOE), const std::vector<std::string> &activations = std::vector<std::string>{"sigmoid", "tanh", "tanh"}, const std::vector<float> &activations_alpha = {}, const std::vector<float> &activations_beta = {}, float clip = 0.f, bool input_forget = false)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v08LSTMCell8LSTMCellERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeENSt6size_tE17LSTMWeightsFormatRKNSt6vectorINSt6stringEEERKNSt6vectorIfEERKNSt6vectorIfEEfb) Constructs

[LSTMCell](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_l_s_t_m_cell)node.- Parameters:
**X**–**[in]**The input tensor with shape: [batch_size, input_size].**initial_hidden_state**–**[in]**The hidden state tensor at current time step with shape: [batch_size, hidden_size].**initial_cell_state**–**[in]**The cell state tensor at current time step with shape: [batch_size, hidden_size].**W**–**[in]**The gate weights tensor with shape: [4*hidden_size, input_size].**R**–**[in]**The recurrence weights tensor with shape: [4*hidden_size, hidden_size].**hidden_size**–**[in]**The number of hidden units for recurrent cell.**weights_format**–**[in]**The order of gates in weights tensors. The default format is IFCO since it is used by DNNL.**activations**–**[in]**The vector of activation functions used inside recurrent cell.**activations_alpha**–**[in]**The vector of alpha parameters for activation functions in order respective to activation list.**activations_beta**–**[in]**The vector of beta parameters for activation functions in order respective to activation list.**clip**–**[in]**The value defining clipping range [-clip, clip] on input of activation functions.**input_forget**–**[in]**Controls coupling input and forget gates.



-
LSTMCell(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &X, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &initial_hidden_state, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &initial_cell_state, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &W, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &R, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &B, std::size_t hidden_size,[LSTMWeightsFormat](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17LSTMWeightsFormatE)weights_format =[LSTMWeightsFormat](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17LSTMWeightsFormatE)::[IFCO](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17LSTMWeightsFormat4IFCOE), const std::vector<std::string> &activations = std::vector<std::string>{"sigmoid", "tanh", "tanh"}, const std::vector<float> &activations_alpha = {}, const std::vector<float> &activations_beta = {}, float clip = 0.f, bool input_forget = false)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v08LSTMCell8LSTMCellERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeENSt6size_tE17LSTMWeightsFormatRKNSt6vectorINSt6stringEEERKNSt6vectorIfEERKNSt6vectorIfEEfb) Constructs

[LSTMCell](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_l_s_t_m_cell)node.- Parameters:
**X**–**[in]**The input tensor with shape: [batch_size, input_size].**initial_hidden_state**–**[in]**The hidden state tensor at current time step with shape: [batch_size, hidden_size].**initial_cell_state**–**[in]**The cell state tensor at current time step with shape: [batch_size, hidden_size].**W**–**[in]**The weight tensor with shape: [4*hidden_size, input_size].**R**–**[in]**The recurrence weight tensor with shape: [4*hidden_size, hidden_size].**B**–**[in]**The bias tensor for gates with shape: [4*hidden_size].**hidden_size**–**[in]**The number of hidden units for recurrent cell.**weights_format**–**[in]**The order of gates in weights tensors. The default format is IFCO since it is used by DNNL.**activations**–**[in]**The vector of activation functions used inside recurrent cell.**activations_alpha**–**[in]**The vector of alpha parameters for activation functions in order respective to activation list.**activations_beta**–**[in]**The vector of beta parameters for activation functions in order respective to activation list.**clip**–**[in]**The value defining clipping range [-clip, clip] on input of activation functions.**input_forget**–**[in]**Controls coupling input and forget gates.



-
LSTMCell(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &X, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &initial_hidden_state, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &initial_cell_state, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &W, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &R, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &B, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &P, std::size_t hidden_size,[LSTMWeightsFormat](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17LSTMWeightsFormatE)weights_format =[LSTMWeightsFormat](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17LSTMWeightsFormatE)::[IFCO](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17LSTMWeightsFormat4IFCOE), const std::vector<std::string> &activations = std::vector<std::string>{"sigmoid", "tanh", "tanh"}, const std::vector<float> &activations_alpha = {}, const std::vector<float> &activations_beta = {}, float clip = 0.f, bool input_forget = false)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v08LSTMCell8LSTMCellERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeENSt6size_tE17LSTMWeightsFormatRKNSt6vectorINSt6stringEEERKNSt6vectorIfEERKNSt6vectorIfEEfb) Constructs

[LSTMCell](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_l_s_t_m_cell)node.- Parameters:
**X**–**[in]**The input tensor with shape: [batch_size, input_size].**initial_hidden_state**–**[in]**The hidden state tensor at current time step with shape: [batch_size, hidden_size].**initial_cell_state**–**[in]**The cell state tensor at current time step with shape: [batch_size, hidden_size].**W**–**[in]**The weight tensor with shape: [4*hidden_size, input_size].**R**–**[in]**The recurrence weight tensor with shape: [4*hidden_size, hidden_size].**B**–**[in]**The bias tensor for gates with shape: [4*hidden_size].**P**–**[in]**The weight tensor for peepholes with shape: [3*hidden_size] - 3 equals to only iof gates. The order is: input, output, forget gates.**hidden_size**–**[in]**The number of hidden units for recurrent cell.**weights_format**–**[in]**The order of gates in weights tensors. The default format is IFCO since it is used by DNNL.**activations**–**[in]**The vector of activation functions used inside recurrent cell.**activations_alpha**–**[in]**The vector of alpha parameters for activation functions in order respective to activation list.**activations_beta**–**[in]**The vector of beta parameters for activation functions in order respective to activation list.**clip**–**[in]**The value defining clipping range [-clip, clip] on input of activation functions.**input_forget**–**[in]**Controls coupling input and forget gates.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v08LSTMCell24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.