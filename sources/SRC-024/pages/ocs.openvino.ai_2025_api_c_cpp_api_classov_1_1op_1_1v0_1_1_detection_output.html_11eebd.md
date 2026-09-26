source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v0_1_1_detection_output.html
lastmod: 

# Class ov::op::v0::DetectionOutput[#](https://docs.openvino.ai#class-ov-op-v0-detectionoutput)

-
class DetectionOutput : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[DetectionOutputBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_detection_output_base.html#_CPPv4N2ov2op4util19DetectionOutputBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v015DetectionOutputE) Layer which performs non-max suppression to generate detection output using location and confidence predictions.

Public Functions

-
DetectionOutput(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &box_logits, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &class_preds, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &proposals, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &aux_class_preds, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &aux_box_preds, const[Attributes](https://docs.openvino.ai/structov_1_1op_1_1v0_1_1_detection_output_1_1_attributes.html#_CPPv4N2ov2op2v015DetectionOutput10AttributesE)&attrs)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v015DetectionOutput15DetectionOutputERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK10Attributes) Constructs a

[DetectionOutput](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_detection_output)operation.- Parameters:
**box_logits**– Box logits**class_preds**– Class predictions**proposals**– Proposals**aux_class_preds**– Auxilary class predictions**aux_box_preds**– Auxilary box predictions**attrs**– Detection[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)attributes



-
DetectionOutput(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &box_logits, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &class_preds, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &proposals, const[Attributes](https://docs.openvino.ai/structov_1_1op_1_1v0_1_1_detection_output_1_1_attributes.html#_CPPv4N2ov2op2v015DetectionOutput10AttributesE)&attrs)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v015DetectionOutput15DetectionOutputERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK10Attributes) Constructs a

[DetectionOutput](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_detection_output)operation.- Parameters:
**box_logits**– Box logits**class_preds**– Class predictions**proposals**– Proposals**attrs**– Detection[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)attributes



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v015DetectionOutput24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
struct Attributes : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[DetectionOutputBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_detection_output_base.html#_CPPv4N2ov2op4util19DetectionOutputBaseE)::[AttributesBase](https://docs.openvino.ai/structov_1_1op_1_1util_1_1_detection_output_base_1_1_attributes_base.html#_CPPv4N2ov2op4util19DetectionOutputBase14AttributesBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v015DetectionOutput10AttributesE)

-
DetectionOutput(const