source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_mark_dequantization.html
lastmod: 

# Class ov::pass::MarkDequantization[#](https://docs.openvino.ai#class-ov-pass-markdequantization)

-
class MarkDequantization : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass18MarkDequantizationE) [MarkDequantization](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_mark_dequantization)matches Dequantization subgraphs and marks Subtract and Multiply nodes with the dequantization attribute. Also if Convert nodes are part of the subgraph they might be marked with the disable_const_folding attribute.If Convert -> Reshape/Unsqueeze are part of the Dequantization subraph, Convert and Reshape/Unsqueeze nodes will be swapped to eliminate Reshape/Unsqueeze in the next

[ConstantFolding](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1_constant_folding).Dequantization subgraph may have two forms: with and without Subtract. ZeroPoints and Scale might be present as subgraphs and include Convert ops.

Input ZeroPoints │ │ ▼ ▼ Convert (opt) Reshape/Unsqueeze │ │ ▼ ▼ Scale Input Scale Subtract │ │ │ │ ▼ ▼ ▼ │ (opt) Reshape/Unsqueeze Convert (opt) Reshape/Unsqueeze │ │ │ │ ▼ ▼ ▼ ▼ Multiply Multiply