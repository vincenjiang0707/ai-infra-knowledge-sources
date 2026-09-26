source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_convert_gather0_d.html
lastmod: 

# Class ov::pass::ConvertGather0D[#](https://docs.openvino.ai#class-ov-pass-convertgather0d)

-
class ConvertGather0D : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass15ConvertGather0DE) [ConvertGather0D](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_convert_gather0_d)decomposes v1::Gather operation into v0::Unsqueeze + v1::Gather + v0::Squeeze pattern when gather indices is scalar.

Site Navigation

Section Navigation

[ConvertGather0D](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_convert_gather0_d) decomposes v1::Gather operation into v0::Unsqueeze + v1::Gather + v0::Squeeze pattern when gather indices is scalar.