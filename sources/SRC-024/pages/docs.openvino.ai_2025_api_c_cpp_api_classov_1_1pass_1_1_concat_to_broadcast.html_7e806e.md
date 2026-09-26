source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_concat_to_broadcast.html
lastmod: 

# Class ov::pass::ConcatToBroadcast[#](https://docs.openvino.ai#class-ov-pass-concattobroadcast)

-
class ConcatToBroadcast : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass17ConcatToBroadcastE) [ConcatToBroadcast](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_concat_to_broadcast)transformation replaces Concat, having multiple inputs from the same output, with a Broadcast node.

Site Navigation

Section Navigation

[ConcatToBroadcast](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_concat_to_broadcast) transformation replaces Concat, having multiple inputs from the same output, with a Broadcast node.