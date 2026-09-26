source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_mark_precision_sensitive_constants.html
lastmod: 

# Class ov::pass::MarkPrecisionSensitiveConstants[#](https://docs.openvino.ai#class-ov-pass-markprecisionsensitiveconstants)

-
class MarkPrecisionSensitiveConstants : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MarkPrecisionSensitiveShapeOfSubgraphs](https://docs.openvino.ai/classov_1_1pass_1_1_mark_precision_sensitive_shape_of_subgraphs.html#_CPPv4N2ov4pass38MarkPrecisionSensitiveShapeOfSubgraphsE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass31MarkPrecisionSensitiveConstantsE) [MarkPrecisionSensitiveConstants](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_mark_precision_sensitive_constants)marks the constants inside of all shape subgraphs starting from precision-sensitive inputs and ending at the ShapeOf node as disabled for FP16 compression.