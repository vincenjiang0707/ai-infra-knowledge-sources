source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_replace_concat_reduce_by_min_or_max.html
lastmod: 

# Class ov::pass::ReplaceConcatReduceByMinOrMax[#](https://docs.openvino.ai#class-ov-pass-replaceconcatreducebyminormax)

-
class ReplaceConcatReduceByMinOrMax : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass29ReplaceConcatReduceByMinOrMaxE) [ReplaceConcatReduceByMinOrMax](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_replace_concat_reduce_by_min_or_max)transformation replaces Concat with 2 inputs and ReduceMin/Max by a single Minimum/Maximum with 2 inputs and inserts squeeze in case when Reduce has keep_dims = false.