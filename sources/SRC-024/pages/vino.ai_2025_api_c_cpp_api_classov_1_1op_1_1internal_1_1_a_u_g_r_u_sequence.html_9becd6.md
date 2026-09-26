source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1internal_1_1_a_u_g_r_u_sequence.html
lastmod: 

# Class ov::op::internal::AUGRUSequence[#](https://docs.openvino.ai#class-ov-op-internal-augrusequence)

-
class AUGRUSequence : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[RNNCellBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_r_n_n_cell_base.html#_CPPv4N2ov2op4util11RNNCellBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op8internal13AUGRUSequenceE) [AUGRUSequence](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1internal_1_1_a_u_g_r_u_sequence)operation.Public Functions

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op8internal13AUGRUSequence24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual void validate_and_infer_types() override