source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_gelu7_downgrade.html
lastmod: 

# Class ov::pass::Gelu7Downgrade[#](https://docs.openvino.ai#class-ov-pass-gelu7downgrade)

-
class Gelu7Downgrade : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass14Gelu7DowngradeE) [Gelu7Downgrade](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_gelu7_downgrade)converts v7::Gelu operation to v2::Gelu unconditionally. This is done because only limited set of plugins support v7::Gelu which has an attribute specifying approximation mode. For other plugins the behaviour is to use v2 version of the operation which does not support the approximation mode.