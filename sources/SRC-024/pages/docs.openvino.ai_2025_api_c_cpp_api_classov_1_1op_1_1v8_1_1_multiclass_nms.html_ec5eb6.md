source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v8_1_1_multiclass_nms.html
lastmod: 

# Class ov::op::v8::MulticlassNms[#](https://docs.openvino.ai#class-ov-op-v8-multiclassnms)

-
class MulticlassNms : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[MulticlassNmsBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_multiclass_nms_base.html#_CPPv4N2ov2op4util17MulticlassNmsBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v813MulticlassNmsE) [MulticlassNms](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v8_1_1_multiclass_nms)operation.Public Functions

-
MulticlassNms() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v813MulticlassNms13MulticlassNmsEv) Constructs a conversion operation.


-
MulticlassNms(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &boxes, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &scores, const Attributes &attrs)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v813MulticlassNms13MulticlassNmsERK6OutputI4NodeERK6OutputI4NodeERK10Attributes) Constructs a

[MulticlassNms](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v8_1_1_multiclass_nms)operation.

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v813MulticlassNms24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
MulticlassNms() = default