source: https://docs.openvino.ai/2025/api/c_cpp_api/class_convert_bitwise_to_logical.html
lastmod: 

# Class ConvertBitwiseToLogical[#](https://docs.openvino.ai#class-convertbitwisetological)

-
class ConvertBitwiseToLogical : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[GraphRewrite](https://docs.openvino.ai/classov_1_1pass_1_1_graph_rewrite.html#_CPPv4N2ov4pass12GraphRewriteE)[#](https://docs.openvino.ai#_CPPv423ConvertBitwiseToLogical) Converts Bitwise operators to Logical for boolean datatype for plugins that don’t support opset13 Bitwise and to allow for constant folding for bool.