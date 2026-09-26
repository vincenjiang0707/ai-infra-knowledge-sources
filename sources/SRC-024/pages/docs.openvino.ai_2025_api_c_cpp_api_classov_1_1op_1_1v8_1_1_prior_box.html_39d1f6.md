source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v8_1_1_prior_box.html
lastmod: 

# Class ov::op::v8::PriorBox[#](https://docs.openvino.ai#class-ov-op-v8-priorbox)

-
class PriorBox : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v88PriorBoxE) Layer which generates prior boxes of specified sizes normalized to input image size.

Public Functions

-
PriorBox(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &layer_shape, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &image_shape, const[Attributes](https://docs.openvino.ai/structov_1_1op_1_1v8_1_1_prior_box_1_1_attributes.html#_CPPv4N2ov2op2v88PriorBox10AttributesE)&attrs)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v88PriorBox8PriorBoxERK6OutputI4NodeERK6OutputI4NodeERK10Attributes) Constructs a

[PriorBox](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v8_1_1_prior_box)operation.

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v88PriorBox24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v88PriorBox12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
struct Attributes
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v88PriorBox10AttributesE)

-
PriorBox(const