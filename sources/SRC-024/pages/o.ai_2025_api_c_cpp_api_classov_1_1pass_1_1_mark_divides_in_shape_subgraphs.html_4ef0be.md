source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_mark_divides_in_shape_subgraphs.html
lastmod: 

# Class ov::pass::MarkDividesInShapeSubgraphs[#](https://docs.openvino.ai#class-ov-pass-markdividesinshapesubgraphs)

-
class MarkDividesInShapeSubgraphs : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MarkPrecisionSensitiveShapeOfSubgraphs](https://docs.openvino.ai/classov_1_1pass_1_1_mark_precision_sensitive_shape_of_subgraphs.html#_CPPv4N2ov4pass38MarkPrecisionSensitiveShapeOfSubgraphsE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass27MarkDividesInShapeSubgraphsE) [MarkDividesInShapeSubgraphs](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_mark_divides_in_shape_subgraphs)marks the Divide layers inside of all shape subgraphs starting from precision-sensitive input and ending at the ShapeOf node as disabled for[ConvertDivide](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1_convert_divide)transformation.