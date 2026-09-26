source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1util_1_1_max_pool_base.html
lastmod: 

# Class ov::op::util::MaxPoolBase[#](https://docs.openvino.ai#class-ov-op-util-maxpoolbase)

-
class MaxPoolBase : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op4util11MaxPoolBaseE) Subclassed by

[ov::op::v14::MaxPool](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v14_1_1_max_pool),[ov::op::v1::MaxPool](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_max_pool),[ov::op::v8::MaxPool](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v8_1_1_max_pool)Public Functions

-
MaxPoolBase(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const[Strides](https://docs.openvino.ai/classov_1_1_strides.html#_CPPv4N2ov7StridesE)&strides, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&pads_begin, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&pads_end, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&kernel, const[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[RoundingType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op12RoundingTypeE)rounding_mode =[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[RoundingType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op12RoundingTypeE)::[FLOOR](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op12RoundingType5FLOORE), const[PadType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadTypeE)auto_pad =[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[PadType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadTypeE)::[EXPLICIT](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadType8EXPLICITE))[#](https://docs.openvino.ai#_CPPv4N2ov2op4util11MaxPoolBase11MaxPoolBaseERK6OutputI4NodeERK7StridesRK5ShapeRK5ShapeRK5ShapeKN2op12RoundingTypeEK7PadType) - Parameters:
**arg**– The node producing the input data batch tensor.**strides**– The strides.**pads_begin**– The beginning of padding shape.**pads_end**– The end of padding shape.**kernel**– The kernel shape.**rounding_mode**– Whether to use ceiling or floor rounding type while computing output shape.**auto_pad**– The pad type for automatically computing padding sizes.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op4util11MaxPoolBase24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
inline
[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[RoundingType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op12RoundingTypeE)get_rounding_type() const[#](https://docs.openvino.ai#_CPPv4NK2ov2op4util11MaxPoolBase17get_rounding_typeEv) - Returns:
The ceiling mode being used for output shape computations



-
MaxPoolBase(const