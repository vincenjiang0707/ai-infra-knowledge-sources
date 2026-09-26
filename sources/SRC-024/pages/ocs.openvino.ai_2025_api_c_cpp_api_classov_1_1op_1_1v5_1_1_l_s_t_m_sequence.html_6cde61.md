source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v5_1_1_l_s_t_m_sequence.html
lastmod: 

# Class ov::op::v5::LSTMSequence[#](https://docs.openvino.ai#class-ov-op-v5-lstmsequence)

-
class LSTMSequence : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[RNNCellBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_r_n_n_cell_base.html#_CPPv4N2ov2op4util11RNNCellBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v512LSTMSequenceE) Class for lstm sequence node.

See also

LSTMCell, RNNCell, GRUCell

Note

It follows notation and equations defined as in ONNX standard:

[onnx/onnx](https://github.com/onnx/onnx/blob/master/docs/Operators.md#LSTM)Public Functions

-
inline virtual size_t get_default_output_index() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v512LSTMSequence24get_default_output_indexEv) Returns the output of the default output, or throws if there is none.


-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v512LSTMSequence24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
inline virtual size_t get_default_output_index() const override