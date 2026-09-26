source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_nop_broadcast.html
lastmod: 

# Class ov::pass::NopBroadcast[#](https://docs.openvino.ai#class-ov-pass-nopbroadcast)

-
class NopBroadcast : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass12NopBroadcastE) Optimizes out Broadcast(data, Maximum(shape, ones)) if labels on data and shape are equal Use case with data being empty should not be considered here since original graph has Maximum with ones.