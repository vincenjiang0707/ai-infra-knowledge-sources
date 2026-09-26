source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1transpose__sinking_1_1_t_s_fuse.html
lastmod: 

# Class ov::pass::transpose_sinking::TSFuse[#](https://docs.openvino.ai#class-ov-pass-transpose-sinking-tsfuse)

-
class TSFuse : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass17transpose_sinking6TSFuseE) [TSFuse](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1transpose__sinking_1_1_t_s_fuse)transformation eliminates 2 consecutive Transposes if they result in no changes to input or fuses them to single Transpose if input gets changed.