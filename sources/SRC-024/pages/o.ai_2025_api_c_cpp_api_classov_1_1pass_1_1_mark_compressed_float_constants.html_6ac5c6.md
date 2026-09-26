source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_mark_compressed_float_constants.html
lastmod: 

# Class ov::pass::MarkCompressedFloatConstants[#](https://docs.openvino.ai#class-ov-pass-markcompressedfloatconstants)

-
class MarkCompressedFloatConstants : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass28MarkCompressedFloatConstantsE) Prevents

[ConstantFolding](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1_constant_folding)for low precision Const + Convert_To_FP32 to keep original FW float Constants. Original precision should be kept as long as possible, this prevents redundant conversions and saves memory. E.g. if original FW model was already compressed no need to upcast during CF, store intermediate f32 consts and then again compress them to low precision during save_model.