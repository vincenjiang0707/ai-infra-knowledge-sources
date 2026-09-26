source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1low__precision_1_1_add_transformation.html
lastmod: 

# Class ov::pass::low_precision::AddTransformation[#](https://docs.openvino.ai#class-ov-pass-low-precision-addtransformation)

-
class AddTransformation : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[low_precision](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4pass13low_precisionE)::[EltwiseBaseTransformation](https://docs.openvino.ai/classov_1_1pass_1_1low__precision_1_1_eltwise_base_transformation.html#_CPPv4N2ov4pass13low_precision25EltwiseBaseTransformationE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass13low_precision17AddTransformationE) [AddTransformation](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1low__precision_1_1_add_transformation)propagates dequantization subtraction from one input branch to another and propagates dequantization multiplication from the same branch through Add operation.For more details about the transformation, refer to AddTransformation page in the OpenVINO Developer Guide.