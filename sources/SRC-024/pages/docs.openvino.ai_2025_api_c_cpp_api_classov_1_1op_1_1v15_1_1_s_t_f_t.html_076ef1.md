source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v15_1_1_s_t_f_t.html
lastmod: 

# Class ov::op::v15::STFT[#](https://docs.openvino.ai#class-ov-op-v15-stft)

-
class STFT : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v154STFTE) An operation

[STFT](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v15_1_1_s_t_f_t)that computes the Short Time Fourier Transform.Public Functions

-
STFT(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &window, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &frame_size, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &frame_step, const bool transpose_frames)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v154STFT4STFTERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeEKb) Constructs a

[STFT](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v15_1_1_s_t_f_t)operation.- Parameters:
**data**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)data**window**– Window to perform[STFT](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v15_1_1_s_t_f_t)**frame_size**– Scalar value representing the size of Fourier Transform**frame_step**– The distance (number of samples) between successive window frames**transpose_frames**– Flag to set output shape layout. If true the`frames`

dimension is at out_shape[2], otherwise it is at out_shape[1].



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v154STFT24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
STFT(const