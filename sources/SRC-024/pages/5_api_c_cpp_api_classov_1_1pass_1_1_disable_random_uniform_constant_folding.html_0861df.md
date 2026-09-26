source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_disable_random_uniform_constant_folding.html
lastmod: 

# Class ov::pass::DisableRandomUniformConstantFolding[#](https://docs.openvino.ai#class-ov-pass-disablerandomuniformconstantfolding)

-
class DisableRandomUniformConstantFolding : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass35DisableRandomUniformConstantFoldingE) Disables

[ConstantFolding](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1_constant_folding)for RandomUniform operation. It is required as RandomUniform should generate new sequence each run.