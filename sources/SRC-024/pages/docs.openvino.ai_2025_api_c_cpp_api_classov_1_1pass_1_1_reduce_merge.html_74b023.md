source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_reduce_merge.html
lastmod: 

# Class ov::pass::ReduceMerge[#](https://docs.openvino.ai#class-ov-pass-reducemerge)

-
class ReduceMerge : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass11ReduceMergeE) [ReduceMerge](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_reduce_merge)transformation matches following graph:+——-—+ +——-—+ | A | | B | +——-—+ +——-—+ | |

| | v v +—–

—+ +—–—+ | Reduce | | C | +—–—+ +—–—+ | | | —-— | | v v +——-—+ | Reduce | +——-—+and replaces with:

+——-—+ +—————-—+ | A | | Concat/Constant | +——-—+ +—————-—+ | | | —–— | | v v +——-—+ | Reduce | +——-—++----------+ +----------+ | B | | C | +----------+ +----------+ | | ------- ------- | | v v