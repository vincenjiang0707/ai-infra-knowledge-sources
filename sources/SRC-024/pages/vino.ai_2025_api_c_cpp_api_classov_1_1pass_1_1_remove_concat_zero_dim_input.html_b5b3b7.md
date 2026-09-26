source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_remove_concat_zero_dim_input.html
lastmod: 

# Class ov::pass::RemoveConcatZeroDimInput[#](https://docs.openvino.ai#class-ov-pass-removeconcatzerodiminput)

-
class RemoveConcatZeroDimInput : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass24RemoveConcatZeroDimInputE) [RemoveConcatZeroDimInput](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_remove_concat_zero_dim_input)transformation removes input of Concat if the tensor size is equal to 0.

Site Navigation

Section Navigation

[RemoveConcatZeroDimInput](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_remove_concat_zero_dim_input) transformation removes input of Concat if the tensor size is equal to 0.