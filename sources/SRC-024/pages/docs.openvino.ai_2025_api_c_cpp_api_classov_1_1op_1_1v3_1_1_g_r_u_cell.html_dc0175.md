source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v3_1_1_g_r_u_cell.html
lastmod: 

# Class ov::op::v3::GRUCell[#](https://docs.openvino.ai#class-ov-op-v3-grucell)

-
class GRUCell : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[RNNCellBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_r_n_n_cell_base.html#_CPPv4N2ov2op4util11RNNCellBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v37GRUCellE) Class for GRU cell node.

Note

Note this class represents only single

*cell*and not whole GRU*layer*.Public Functions

-
GRUCell(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &X, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &initial_hidden_state, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &W, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &R, std::size_t hidden_size)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v37GRUCell7GRUCellERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeENSt6size_tE) Constructs

[GRUCell](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_g_r_u_cell)node.- Parameters:
**X**–**[in]**The input tensor with shape: [batch_size, input_size].**initial_hidden_state**–**[in]**The hidden state tensor at current time step with shape: [batch_size, hidden_size].**W**–**[in]**The weight tensor with shape: [gates_count * hidden_size, input_size].**R**–**[in]**The recurrence weight tensor with shape: [gates_count * hidden_size, hidden_size].**hidden_size**–**[in]**The number of hidden units for recurrent cell.



-
GRUCell(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &X, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &initial_hidden_state, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &W, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &R, std::size_t hidden_size, const std::vector<std::string> &activations, const std::vector<float> &activations_alpha, const std::vector<float> &activations_beta, float clip, bool linear_before_reset)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v37GRUCell7GRUCellERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeENSt6size_tERKNSt6vectorINSt6stringEEERKNSt6vectorIfEERKNSt6vectorIfEEfb) Constructs

[GRUCell](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_g_r_u_cell)node.- Parameters:
**X**–**[in]**The input tensor with shape: [batch_size, input_size].**initial_hidden_state**–**[in]**The hidden state tensor at current time step with shape: [batch_size, hidden_size].**W**–**[in]**The weight tensor with shape: [gates_count * hidden_size, input_size].**R**–**[in]**The recurrence weight tensor with shape: [gates_count * hidden_size, hidden_size].**hidden_size**–**[in]**The number of hidden units for recurrent cell.**activations**–**[in]**The vector of activation functions used inside recurrent cell.**activations_alpha**–**[in]**The vector of alpha parameters for activation functions in order respective to activation list.**activations_beta**–**[in]**The vector of beta parameters for activation functions in order respective to activation list.**clip**–**[in]**The value defining clipping range [-clip, clip] on input of activation functions.



-
GRUCell(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &X, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &initial_hidden_state, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &W, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &R, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &B, std::size_t hidden_size, const std::vector<std::string> &activations = std::vector<std::string>{"sigmoid", "tanh"}, const std::vector<float> &activations_alpha = {}, const std::vector<float> &activations_beta = {}, float clip = 0.f, bool linear_before_reset = false)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v37GRUCell7GRUCellERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeENSt6size_tERKNSt6vectorINSt6stringEEERKNSt6vectorIfEERKNSt6vectorIfEEfb) Constructs

[GRUCell](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_g_r_u_cell)node.- Parameters:
**X**–**[in]**The input tensor with shape: [batch_size, input_size].**initial_hidden_state**–**[in]**The hidden state tensor at current time step with shape: [batch_size, hidden_size].**W**–**[in]**The weight tensor with shape: [gates_count * hidden_size, input_size].**R**–**[in]**The recurrence weight tensor with shape: [gates_count * hidden_size, hidden_size].**hidden_size**–**[in]**The number of hidden units for recurrent cell.**B**–**[in]**The sum of biases (weight and recurrence) for update, reset and hidden gates. If linear_before_reset := true then biases for hidden gates are placed separately (weight and recurrence).[Shape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_shape): [gates_count * hidden_size] if linear_before_reset := false[Shape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_shape): [(gates_count + 1) * hidden_size] if linear_before_reset := true**activations**–**[in]**The vector of activation functions used inside recurrent cell.**activations_alpha**–**[in]**The vector of alpha parameters for activation functions in order respective to activation list.**activations_beta**–**[in]**The vector of beta parameters for activation functions in order respective to activation list.**clip**–**[in]**The value defining clipping range [-clip, clip] on input of activation functions.**linear_before_reset**–**[in]**Whether or not to apply the linear transformation before multiplying by the output of the reset gate.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v37GRUCell24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
GRUCell(const