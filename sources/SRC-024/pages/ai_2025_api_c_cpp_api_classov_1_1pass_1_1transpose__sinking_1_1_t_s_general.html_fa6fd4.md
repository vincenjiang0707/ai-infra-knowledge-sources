source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1transpose__sinking_1_1_t_s_general.html
lastmod: 

# Class ov::pass::transpose_sinking::TSGeneral[#](https://docs.openvino.ai#class-ov-pass-transpose-sinking-tsgeneral)

-
class TSGeneral : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[ModelPass](https://docs.openvino.ai/classov_1_1pass_1_1_model_pass.html#_CPPv4N2ov4pass9ModelPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass17transpose_sinking9TSGeneralE) [TSGeneral](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1transpose__sinking_1_1_t_s_general)transformation combines[TSGeneralForward](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1transpose__sinking_1_1_t_s_general_forward)and[TSGeneralBackward](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1transpose__sinking_1_1_t_s_general_backward)transformations into single[ModelPass](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1_model_pass)pass and inserts[ConstantFolding](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1_constant_folding)pass after them.