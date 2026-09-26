source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_shrink_weights.html
lastmod: 

# Class ov::pass::ShrinkWeights[#](https://docs.openvino.ai#class-ov-pass-shrinkweights)

-
class ShrinkWeights : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[ModelPass](https://docs.openvino.ai/classov_1_1pass_1_1_model_pass.html#_CPPv4N2ov4pass9ModelPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass13ShrinkWeightsE) Based on masks in Constant operation it inserts Gather operations to shrink them. After this pass execution

[ConstantFolding](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1_constant_folding)is required.

Site Navigation

Section Navigation