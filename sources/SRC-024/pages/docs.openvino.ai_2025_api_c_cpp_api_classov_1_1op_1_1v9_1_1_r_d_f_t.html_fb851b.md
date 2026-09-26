source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v9_1_1_r_d_f_t.html
lastmod: 

# Class ov::op::v9::RDFT[#](https://docs.openvino.ai#class-ov-op-v9-rdft)

-
class RDFT : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[FFTBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_f_f_t_base.html#_CPPv4N2ov2op4util7FFTBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v94RDFTE) An operation

[RDFT](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v9_1_1_r_d_f_t)that computes the discrete real-to-complex Fourier transformation.Public Functions

-
RDFT(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &axes)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v94RDFT4RDFTERK6OutputI4NodeERK6OutputI4NodeE) Constructs a

[RDFT](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v9_1_1_r_d_f_t)operation.[RDFT](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v9_1_1_r_d_f_t)is performed for full size axes.

-
RDFT(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &axes, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &signal_size)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v94RDFT4RDFTERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeE) Constructs a

[RDFT](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v9_1_1_r_d_f_t)operation.

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v94RDFT24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
RDFT(const