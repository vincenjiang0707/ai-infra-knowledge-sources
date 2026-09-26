source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v1_1_1_avg_pool.html
lastmod: 

# Class ov::op::v1::AvgPool[#](https://docs.openvino.ai#class-ov-op-v1-avgpool)

-
class AvgPool : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[AvgPoolBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_avg_pool_base.html#_CPPv4N2ov2op4util11AvgPoolBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v17AvgPoolE) Batched average pooling operation.

Public Functions

-
AvgPool() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v17AvgPool7AvgPoolEv) Constructs a batched average pooling operation.


-
AvgPool(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const[Strides](https://docs.openvino.ai/classov_1_1_strides.html#_CPPv4N2ov7StridesE)&strides, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&pads_begin, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&pads_end, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&kernel, bool exclude_pad,[RoundingType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op12RoundingTypeE)rounding_type =[RoundingType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op12RoundingTypeE)::[FLOOR](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op12RoundingType5FLOORE), const[PadType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadTypeE)&auto_pad =[PadType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadTypeE)::[EXPLICIT](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadType8EXPLICITE))[#](https://docs.openvino.ai#_CPPv4N2ov2op2v17AvgPool7AvgPoolERK6OutputI4NodeERK7StridesRK5ShapeRK5ShapeRK5Shapeb12RoundingTypeRK7PadType) Constructs a batched average pooling operation.

- Parameters:
**arg**– The output producing the input data batch tensor.`[d1, dn]`

**strides**– The strides.`[n]`

**pads_begin**– The beginning of padding shape.`[n]`

**pads_end**– The end of padding shape.`[n]`

**kernel**– The kernel shape.`[n]`

**exclude_pad**– If false then averages include padding elements, each treated as the number zero. If true, padding elements are entirely ignored when computing averages.**rounding_type**– Whether to use ceiling or floor rounding type while computing output shape.**auto_pad**– Padding type to use for additional padded dimensions



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v17AvgPool24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
AvgPool() = default