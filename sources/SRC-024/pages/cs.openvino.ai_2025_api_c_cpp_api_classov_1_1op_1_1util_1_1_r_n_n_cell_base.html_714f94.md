source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1util_1_1_r_n_n_cell_base.html
lastmod: 

# Class ov::op::util::RNNCellBase[#](https://docs.openvino.ai#class-ov-op-util-rnncellbase)

-
class RNNCellBase : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op4util11RNNCellBaseE) Base class for all recurrent network cells.

Note

It holds all common attributes.

Subclassed by

[ov::op::internal::AUGRUCell](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1internal_1_1_a_u_g_r_u_cell),[ov::op::internal::AUGRUSequence](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1internal_1_1_a_u_g_r_u_sequence),[ov::op::v0::LSTMCell](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_l_s_t_m_cell),[ov::op::v0::RNNCell](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_r_n_n_cell),[ov::op::v3::GRUCell](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_g_r_u_cell),[ov::op::v4::LSTMCell](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v4_1_1_l_s_t_m_cell),[ov::op::v5::GRUSequence](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v5_1_1_g_r_u_sequence),[ov::op::v5::LSTMSequence](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v5_1_1_l_s_t_m_sequence),[ov::op::v5::RNNSequence](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v5_1_1_r_n_n_sequence)Public Functions

-
RNNCellBase(const OutputVector &args, std::size_t hidden_size, float clip, const std::vector<std::string> &activations, const std::vector<float> &activations_alpha, const std::vector<float> &activations_beta)
[#](https://docs.openvino.ai#_CPPv4N2ov2op4util11RNNCellBase11RNNCellBaseERK12OutputVectorNSt6size_tEfRKNSt6vectorINSt6stringEEERKNSt6vectorIfEERKNSt6vectorIfEE) Constructs a

[RNNCellBase](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_r_n_n_cell_base)class.- Parameters:
**hidden_size**–**[in]**The number of hidden units for recurrent cell.**clip**–**[in]**The value defining clipping range [-clip, clip] on input of activation functions.**activations**–**[in]**The vector of activation functions used inside recurrent cell.**activations_alpha**–**[in]**The vector of alpha parameters for activation functions in order respective to activation list.**activations_beta**–**[in]**The vector of beta parameters for activation functions in order respective to activation list.



-
void validate_input_rank_dimension(const std::vector<
[PartialShape](https://docs.openvino.ai/classov_1_1_partial_shape.html#_CPPv4N2ov12PartialShapeE)> &input)[#](https://docs.openvino.ai#_CPPv4N2ov2op4util11RNNCellBase29validate_input_rank_dimensionERKNSt6vectorI12PartialShapeEE) Validates static rank and dimension for provided input parameters. Additionally input_size dimension is checked for X and W inputs.

- Parameters:
**input**–**[in]**Vector with RNN-Cell op inputs in following order: X, initial_hidden_state, W, R and B.


-
RNNCellBase(const OutputVector &args, std::size_t hidden_size, float clip, const std::vector<std::string> &activations, const std::vector<float> &activations_alpha, const std::vector<float> &activations_beta)