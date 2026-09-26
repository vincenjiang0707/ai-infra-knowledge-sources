source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v0_1_1_interpolate.html
lastmod: 

# Class ov::op::v0::Interpolate[#](https://docs.openvino.ai#class-ov-op-v0-interpolate)

-
class Interpolate : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v011InterpolateE) Layer which performs bilinear interpolation.

Public Functions

-
Interpolate(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &image, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &output_shape, const[Attributes](https://docs.openvino.ai/structov_1_1op_1_1v0_1_1_interpolate_1_1_attributes.html#_CPPv4N2ov2op2v011Interpolate10AttributesE)&attrs)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v011Interpolate11InterpolateERK6OutputI4NodeERK6OutputI4NodeERK10Attributes) Constructs a

[Interpolate](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_interpolate)operation.

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v011Interpolate24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
struct Attributes
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v011Interpolate10AttributesE) Structure that specifies attributes for interpolation.


-
Interpolate(const