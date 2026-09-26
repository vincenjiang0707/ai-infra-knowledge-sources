source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1low__precision_1_1_multiply_to_group_convolution_transformation.html
lastmod: 

# Class ov::pass::low_precision::MultiplyToGroupConvolutionTransformation[#](https://docs.openvino.ai#class-ov-pass-low-precision-multiplytogroupconvolutiontransformation)

-
class MultiplyToGroupConvolutionTransformation : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[low_precision](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4pass13low_precisionE)::[CleanupTransformation](https://docs.openvino.ai/classov_1_1pass_1_1low__precision_1_1_cleanup_transformation.html#_CPPv4N2ov4pass13low_precision21CleanupTransformationE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass13low_precision40MultiplyToGroupConvolutionTransformationE) [MultiplyToGroupConvolutionTransformation](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1low__precision_1_1_multiply_to_group_convolution_transformation)replace quantized Multiply operations to GroupConvolution to speed up inference.For more details about the transformation, refer to MultiplyToGroupConvolutionTransformation page in the OpenVINO Developer Guide.