source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1low__precision_1_1_fold_convert_transformation.html
lastmod: 

# Class ov::pass::low_precision::FoldConvertTransformation[#](https://docs.openvino.ai#class-ov-pass-low-precision-foldconverttransformation)

-
class FoldConvertTransformation : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[low_precision](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4pass13low_precisionE)::[CleanupTransformation](https://docs.openvino.ai/classov_1_1pass_1_1low__precision_1_1_cleanup_transformation.html#_CPPv4N2ov4pass13low_precision21CleanupTransformationE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass13low_precision25FoldConvertTransformationE) [FoldConvertTransformation](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1low__precision_1_1_fold_convert_transformation)evaluates Convert operation on Subtract constant subgraph. Important notice: this transformation ignores[DisableConstantFolding](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1_disable_constant_folding)runtime attribute.For more details about the transformation, refer to FoldConvertTransformation page in the OpenVINO Developer Guide.