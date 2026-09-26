source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_pull_unsqueeze_through_reduce.html
lastmod: 

# Class ov::pass::PullUnsqueezeThroughReduce[#](https://docs.openvino.ai#class-ov-pass-pullunsqueezethroughreduce)

-
class PullUnsqueezeThroughReduce : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass26PullUnsqueezeThroughReduceE) [PullUnsqueezeThroughReduce](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_pull_unsqueeze_through_reduce)transformation The transformation pulls Unsqueeze operator though Reduce ops if possible. In the further processing such Unsqueeze can be often skipped as nop.