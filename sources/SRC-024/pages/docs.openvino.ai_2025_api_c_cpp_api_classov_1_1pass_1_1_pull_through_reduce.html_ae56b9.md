source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_pull_through_reduce.html
lastmod: 

# Class ov::pass::PullThroughReduce[#](https://docs.openvino.ai#class-ov-pass-pullthroughreduce)

-
class PullThroughReduce : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[GraphRewrite](https://docs.openvino.ai/classov_1_1pass_1_1_graph_rewrite.html#_CPPv4N2ov4pass12GraphRewriteE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass17PullThroughReduceE) [PullThroughReduce](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_pull_through_reduce)transformation The transformation pulls Reshape or Unsqueeze operators though Reduce ops if possible. In the further processing such Reshape/Unsqueeze can be often skipped as nop.