source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v6_1_1_experimental_detectron_prior_grid_generator.html
lastmod: 

# Class ov::op::v6::ExperimentalDetectronPriorGridGenerator[#](https://docs.openvino.ai#class-ov-op-v6-experimentaldetectronpriorgridgenerator)

-
class ExperimentalDetectronPriorGridGenerator : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v639ExperimentalDetectronPriorGridGeneratorE) An operation

[ExperimentalDetectronPriorGridGenerator](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v6_1_1_experimental_detectron_prior_grid_generator)generates prior grids of specified sizes.Public Functions

-
ExperimentalDetectronPriorGridGenerator(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &priors, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &feature_map, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &im_data, const[Attributes](https://docs.openvino.ai#_CPPv4N2ov2op2v639ExperimentalDetectronPriorGridGenerator10AttributesE)&attrs)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v639ExperimentalDetectronPriorGridGenerator39ExperimentalDetectronPriorGridGeneratorERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK10Attributes) Constructs a

[ExperimentalDetectronDetectionOutput](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v6_1_1_experimental_detectron_detection_output)operation.

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v639ExperimentalDetectronPriorGridGenerator24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
inline const
[Attributes](https://docs.openvino.ai#_CPPv4N2ov2op2v639ExperimentalDetectronPriorGridGenerator10AttributesE)&get_attrs() const[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v639ExperimentalDetectronPriorGridGenerator9get_attrsEv) Returns attributes of this operation.


-
void set_attrs(
[Attributes](https://docs.openvino.ai#_CPPv4N2ov2op2v639ExperimentalDetectronPriorGridGenerator10AttributesE)attrs)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v639ExperimentalDetectronPriorGridGenerator9set_attrsE10Attributes) Set the attributes of the operation

[ExperimentalDetectronPriorGridGenerator](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v6_1_1_experimental_detectron_prior_grid_generator).- Parameters:
**attrs**–[Attributes](https://docs.openvino.ai/group__ov__transformation__common__api.html#structov_1_1op_1_1v6_1_1_experimental_detectron_prior_grid_generator_1_1_attributes)to set.


-
struct Attributes
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v639ExperimentalDetectronPriorGridGenerator10AttributesE) Structure that specifies attributes of the operation.


-
ExperimentalDetectronPriorGridGenerator(const