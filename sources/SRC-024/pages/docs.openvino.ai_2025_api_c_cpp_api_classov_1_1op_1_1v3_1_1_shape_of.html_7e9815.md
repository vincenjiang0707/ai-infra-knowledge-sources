source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v3_1_1_shape_of.html
lastmod: 

# Class ov::op::v3::ShapeOf[#](https://docs.openvino.ai#class-ov-op-v3-shapeof)

-
class ShapeOf : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[ShapeOfBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_shape_of_base.html#_CPPv4N2ov2op4util11ShapeOfBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v37ShapeOfE) Operation that returns the shape of its input argument as a tensor.

Public Functions

-
ShapeOf(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)output_type =[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[i64](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7element3i64EN6Type_t3i64E))[#](https://docs.openvino.ai#_CPPv4N2ov2op2v37ShapeOf7ShapeOfERK6OutputI4NodeEKN7element4TypeE) Constructs a shape-of operation.


-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v37ShapeOf24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v37ShapeOf12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
ShapeOf(const