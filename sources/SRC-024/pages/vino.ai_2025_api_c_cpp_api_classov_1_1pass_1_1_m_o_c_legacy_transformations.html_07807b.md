source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_m_o_c_legacy_transformations.html
lastmod: 

# Class ov::pass::MOCLegacyTransformations[#](https://docs.openvino.ai#class-ov-pass-moclegacytransformations)

-
class MOCLegacyTransformations : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[ModelPass](https://docs.openvino.ai/classov_1_1pass_1_1_model_pass.html#_CPPv4N2ov4pass9ModelPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass24MOCLegacyTransformationsE) This transformation is an entry point for OpenVINO transformations that will be applied inside MOC. This transformations container is filled with legacy transformations to reach parity between legacy front-ends and new frontends calling from the

[Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)Optimizer. It contains transformations to avoid limitations of OpenVINO 1.X API such as unsupported INT64 for inputs, usage of NCHW layout that is critical for TensorFlow models.