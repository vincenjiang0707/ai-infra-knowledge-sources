source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v6_1_1_experimental_detectron_detection_output.html
lastmod: 

# Class ov::op::v6::ExperimentalDetectronDetectionOutput[#](https://docs.openvino.ai#class-ov-op-v6-experimentaldetectrondetectionoutput)

-
class ExperimentalDetectronDetectionOutput : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v636ExperimentalDetectronDetectionOutputE) An operation

[ExperimentalDetectronDetectionOutput](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v6_1_1_experimental_detectron_detection_output)performs non-maximum suppression to generate the detection output using information on location and score predictions.Public Functions

-
ExperimentalDetectronDetectionOutput(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &input_rois, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &input_deltas, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &input_scores, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &input_im_info, const[Attributes](https://docs.openvino.ai#_CPPv4N2ov2op2v636ExperimentalDetectronDetectionOutput10AttributesE)&attrs)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v636ExperimentalDetectronDetectionOutput36ExperimentalDetectronDetectionOutputERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK10Attributes) Constructs a

[ExperimentalDetectronDetectionOutput](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v6_1_1_experimental_detectron_detection_output)operation.- Parameters:
**input_rois**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)rois**input_deltas**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)deltas**input_scores**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)scores**input_im_info**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)image info**attrs**–[Attributes](https://docs.openvino.ai/group__ov__transformation__common__api.html#structov_1_1op_1_1v6_1_1_experimental_detectron_detection_output_1_1_attributes)attributes



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v636ExperimentalDetectronDetectionOutput24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
inline const
[Attributes](https://docs.openvino.ai#_CPPv4N2ov2op2v636ExperimentalDetectronDetectionOutput10AttributesE)&get_attrs() const[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v636ExperimentalDetectronDetectionOutput9get_attrsEv) Returns attributes of the operation

[ExperimentalDetectronDetectionOutput](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v6_1_1_experimental_detectron_detection_output).

-
void set_attrs(
[Attributes](https://docs.openvino.ai#_CPPv4N2ov2op2v636ExperimentalDetectronDetectionOutput10AttributesE)attrs)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v636ExperimentalDetectronDetectionOutput9set_attrsE10Attributes) Set the attributes of the operation

[ExperimentalDetectronDetectionOutput](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v6_1_1_experimental_detectron_detection_output).- Parameters:
**attrs**–[Attributes](https://docs.openvino.ai/group__ov__transformation__common__api.html#structov_1_1op_1_1v6_1_1_experimental_detectron_detection_output_1_1_attributes)to set.


-
struct Attributes
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v636ExperimentalDetectronDetectionOutput10AttributesE) Structure that specifies attributes of the operation.


-
ExperimentalDetectronDetectionOutput(const