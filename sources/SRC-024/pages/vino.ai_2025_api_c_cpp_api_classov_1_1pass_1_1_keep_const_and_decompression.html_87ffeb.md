source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_keep_const_and_decompression.html
lastmod: 

# Class ov::pass::KeepConstAndDecompression[#](https://docs.openvino.ai#class-ov-pass-keepconstanddecompression)

-
class KeepConstAndDecompression : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass25KeepConstAndDecompressionE) Disables

[ConstantFolding](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1_constant_folding)for Convert operation and prevents conversion of f16 Consts to f32.

Site Navigation

Section Navigation

Disables [ConstantFolding](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1_constant_folding) for Convert operation and prevents conversion of f16 Consts to f32.