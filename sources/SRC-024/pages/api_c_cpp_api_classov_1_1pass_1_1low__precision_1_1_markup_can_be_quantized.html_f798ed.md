source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1low__precision_1_1_markup_can_be_quantized.html
lastmod: 

# Class ov::pass::low_precision::MarkupCanBeQuantized[#](https://docs.openvino.ai#class-ov-pass-low-precision-markupcanbequantized)

-
class MarkupCanBeQuantized : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[ModelPass](https://docs.openvino.ai/classov_1_1pass_1_1_model_pass.html#_CPPv4N2ov4pass9ModelPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass13low_precision20MarkupCanBeQuantizedE) [MarkupCanBeQuantized](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1low__precision_1_1_markup_can_be_quantized)transformation marks Convolution, ConvolutionBackpropData, GroupConvolution and Concat operations as able to be quantized or not. If an operation is not quantized, then[PrecisionsAttribute](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1_precisions_attribute)attribute instance is created with empty precisions.For more details about the transformation, refer to MarkupCanBeQuantized page in the OpenVINO Developer Guide.