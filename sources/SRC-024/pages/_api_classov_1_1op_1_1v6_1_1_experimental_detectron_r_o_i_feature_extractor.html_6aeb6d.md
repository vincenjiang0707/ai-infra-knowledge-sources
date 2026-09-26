source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v6_1_1_experimental_detectron_r_o_i_feature_extractor.html
lastmod: 

# Class ov::op::v6::ExperimentalDetectronROIFeatureExtractor[#](https://docs.openvino.ai#class-ov-op-v6-experimentaldetectronroifeatureextractor)

-
class ExperimentalDetectronROIFeatureExtractor : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v640ExperimentalDetectronROIFeatureExtractorE) An operation

[ExperimentalDetectronROIFeatureExtractor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v6_1_1_experimental_detectron_r_o_i_feature_extractor)is the ROIAlign operation applied over a feature pyramid.Public Functions

-
ExperimentalDetectronROIFeatureExtractor(const OutputVector &args, const
[Attributes](https://docs.openvino.ai#_CPPv4N2ov2op2v640ExperimentalDetectronROIFeatureExtractor10AttributesE)&attrs)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v640ExperimentalDetectronROIFeatureExtractor40ExperimentalDetectronROIFeatureExtractorERK12OutputVectorRK10Attributes) Constructs a

[ExperimentalDetectronROIFeatureExtractor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v6_1_1_experimental_detectron_r_o_i_feature_extractor)operation.- Parameters:
**args**– Inputs of[ExperimentalDetectronROIFeatureExtractor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v6_1_1_experimental_detectron_r_o_i_feature_extractor)**attrs**– Operation attributes



-
ExperimentalDetectronROIFeatureExtractor(const NodeVector &args, const
[Attributes](https://docs.openvino.ai#_CPPv4N2ov2op2v640ExperimentalDetectronROIFeatureExtractor10AttributesE)&attrs)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v640ExperimentalDetectronROIFeatureExtractor40ExperimentalDetectronROIFeatureExtractorERK10NodeVectorRK10Attributes) Constructs a

[ExperimentalDetectronROIFeatureExtractor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v6_1_1_experimental_detectron_r_o_i_feature_extractor)operation.- Parameters:
**args**– Inputs of[ExperimentalDetectronROIFeatureExtractor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v6_1_1_experimental_detectron_r_o_i_feature_extractor)**attrs**– Operation attributes



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v640ExperimentalDetectronROIFeatureExtractor24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
inline const
[Attributes](https://docs.openvino.ai#_CPPv4N2ov2op2v640ExperimentalDetectronROIFeatureExtractor10AttributesE)&get_attrs() const[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v640ExperimentalDetectronROIFeatureExtractor9get_attrsEv) Returns attributes of the operation.


-
void set_attrs(
[Attributes](https://docs.openvino.ai#_CPPv4N2ov2op2v640ExperimentalDetectronROIFeatureExtractor10AttributesE)attrs)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v640ExperimentalDetectronROIFeatureExtractor9set_attrsE10Attributes) Set the

[ExperimentalDetectronROIFeatureExtractor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v6_1_1_experimental_detectron_r_o_i_feature_extractor)’s attributes.- Parameters:
**attrs**–[Attributes](https://docs.openvino.ai/group__ov__transformation__common__api.html#structov_1_1op_1_1v6_1_1_experimental_detectron_r_o_i_feature_extractor_1_1_attributes)to set.


-
struct Attributes
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v640ExperimentalDetectronROIFeatureExtractor10AttributesE) Structure that specifies attributes of the operation.


-
ExperimentalDetectronROIFeatureExtractor(const OutputVector &args, const