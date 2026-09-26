source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_m_o_c_transformations.html
lastmod: 

# Class ov::pass::MOCTransformations[#](https://docs.openvino.ai#class-ov-pass-moctransformations)

-
class MOCTransformations : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[ModelPass](https://docs.openvino.ai/classov_1_1pass_1_1_model_pass.html#_CPPv4N2ov4pass9ModelPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass18MOCTransformationsE) This transformation is an entry point for OpenVINO transformations that will be applied inside MOC. And in future this transformations container will be filled with transformations pipeline but now it remains empty.

Public Functions

-
inline explicit MOCTransformations(bool use_shapes, bool low_precision_enabled = true)
[#](https://docs.openvino.ai#_CPPv4N2ov4pass18MOCTransformations18MOCTransformationsEbb) use_shapes = True enables transformations which are depends on shapes and also it enables

[ConstantFolding](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1_constant_folding)for all ShapeOf operations.low_precision_enabled = True enables preserving mechanisms that helps to keep

[low_precision](https://docs.openvino.ai/group__ov__transformation__common__api.html#namespaceov_1_1pass_1_1low__precision)sub-graphs as is.

-
inline explicit MOCTransformations(bool use_shapes, bool low_precision_enabled = true)