source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_concat_reduce_fusion.html
lastmod: 

# Class ov::pass::ConcatReduceFusion[#](https://docs.openvino.ai#class-ov-pass-concatreducefusion)

-
class ConcatReduceFusion : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[GraphRewrite](https://docs.openvino.ai/classov_1_1pass_1_1_graph_rewrite.html#_CPPv4N2ov4pass12GraphRewriteE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass18ConcatReduceFusionE) [ConcatReduceFusion](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_concat_reduce_fusion)pass replaces the following graph:by a single Minimum/Maximum with 2 inputs and tries to eliminate Squeeze/Unsqueeze layers before and after Min/Max.+---------------+ +---------------+ │ │ | | │ input │ | input | │ │ | | +---------------+ +---------------- | | | | \ / \ / \ / \ / \ / \ / \ / \ / \ / +---------------+ | | | Concat | | | +---------------- | v +---------------+ | | | ReduceMin/ | | ReduceMax | +----------------