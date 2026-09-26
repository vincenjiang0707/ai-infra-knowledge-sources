source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_mark_precision_sensitive_shape_of_subgraphs.html
lastmod: 

# Class ov::pass::MarkPrecisionSensitiveShapeOfSubgraphs[#](https://docs.openvino.ai#class-ov-pass-markprecisionsensitiveshapeofsubgraphs)

-
class MarkPrecisionSensitiveShapeOfSubgraphs : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[ModelPass](https://docs.openvino.ai/classov_1_1pass_1_1_model_pass.html#_CPPv4N2ov4pass9ModelPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass38MarkPrecisionSensitiveShapeOfSubgraphsE) [MarkPrecisionSensitiveShapeOfSubgraphs](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_mark_precision_sensitive_shape_of_subgraphs)marks entirely all shape subgraphs starting from precision-sensitive inputs and ending at the ShapeOf node as disabled for FP16 compression.Subclassed by

[ov::pass::MarkDividesInShapeSubgraphs](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_mark_divides_in_shape_subgraphs),[ov::pass::MarkPrecisionSensitiveConstants](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_mark_precision_sensitive_constants),[ov::pass::MarkShapeOfSubgraphs](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_mark_shape_of_subgraphs)