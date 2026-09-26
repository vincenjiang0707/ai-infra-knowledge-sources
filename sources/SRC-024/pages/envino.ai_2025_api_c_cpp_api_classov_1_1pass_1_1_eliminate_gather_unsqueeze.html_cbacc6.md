source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_eliminate_gather_unsqueeze.html
lastmod: 

# Class ov::pass::EliminateGatherUnsqueeze[#](https://docs.openvino.ai#class-ov-pass-eliminategatherunsqueeze)

-
class EliminateGatherUnsqueeze : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass24EliminateGatherUnsqueezeE) Matches Gather ->[Binary Operation]-> Unsqueeze If axis for Gather and Unsqueeze is the same and Gather indices are scalar Unsqueeze is being removed and indices become 1D. Must be executed after

[SharedOpOptimization](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_shared_op_optimization)— It is possible to have multiple similar Unsqueeze operations after Gather, so they must be optimized beforehand.