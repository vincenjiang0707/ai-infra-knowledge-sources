source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1util_1_1_f_f_t_base.html
lastmod: 

# Class ov::op::util::FFTBase[#](https://docs.openvino.ai#class-ov-op-util-fftbase)

-
class FFTBase : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op4util7FFTBaseE) Base class for operations DFT and DFT.

Subclassed by

[ov::op::v7::DFT](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v7_1_1_d_f_t),[ov::op::v7::IDFT](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v7_1_1_i_d_f_t),[ov::op::v9::IRDFT](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v9_1_1_i_r_d_f_t),[ov::op::v9::RDFT](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v9_1_1_r_d_f_t)Public Functions

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op4util7FFTBase24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual void validate_and_infer_types() override