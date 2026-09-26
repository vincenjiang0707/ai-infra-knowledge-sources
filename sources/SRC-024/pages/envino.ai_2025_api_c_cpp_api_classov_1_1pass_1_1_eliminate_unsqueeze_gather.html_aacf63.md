source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_eliminate_unsqueeze_gather.html
lastmod: 

# Class ov::pass::EliminateUnsqueezeGather[#](https://docs.openvino.ai#class-ov-pass-eliminateunsqueezegather)

-
class EliminateUnsqueezeGather : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass24EliminateUnsqueezeGatherE) Remove Unsqueeze + Gather pair, if Gather gathers data by dimension that was previously added by Unsqueeze.


Site Navigation

Section Navigation

Remove Unsqueeze + Gather pair, if Gather gathers data by dimension that was previously added by Unsqueeze.