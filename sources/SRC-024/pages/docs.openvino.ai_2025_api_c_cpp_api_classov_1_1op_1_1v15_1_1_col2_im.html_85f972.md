source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v15_1_1_col2_im.html
lastmod: 

# Class ov::op::v15::Col2Im[#](https://docs.openvino.ai#class-ov-op-v15-col2im)

-
class Col2Im : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v156Col2ImE) Operator combining sliding blocks into an image tensor.

Public Functions

-
Col2Im(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &output_size, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &kernel_size, const[Strides](https://docs.openvino.ai/classov_1_1_strides.html#_CPPv4N2ov7StridesE)&strides =[Strides](https://docs.openvino.ai/classov_1_1_strides.html#_CPPv4N2ov7StridesE){1, 1}, const[Strides](https://docs.openvino.ai/classov_1_1_strides.html#_CPPv4N2ov7StridesE)&dilations =[Strides](https://docs.openvino.ai/classov_1_1_strides.html#_CPPv4N2ov7StridesE){1, 1}, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&pads_begin =[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE){0, 0}, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&pads_end =[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE){0, 0})[#](https://docs.openvino.ai#_CPPv4N2ov2op3v156Col2Im6Col2ImERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK7StridesRK7StridesRK5ShapeRK5Shape) Constructs a

[Col2Im](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v15_1_1_col2_im)operation.- Parameters:
**data**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)tensor with data**output_size**–[Shape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_shape)of the spatial dimensions of the output image**kernel_size**– Size of the sliding blocks**strides**– Stride in the sliding blocks in the input spatial dimensions**dilations**– Local stride of the elements**pads_begin**– Paddings at the beginning of each spatial axis, if undefined no padding is applied**pads_end**– Paddings at the end of each spatial axis, if undefined no padding is applied



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v156Col2Im24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
Col2Im(const