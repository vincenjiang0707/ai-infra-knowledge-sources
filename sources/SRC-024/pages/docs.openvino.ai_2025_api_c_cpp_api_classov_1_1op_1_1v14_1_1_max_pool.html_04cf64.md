source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v14_1_1_max_pool.html
lastmod: 

# Class ov::op::v14::MaxPool[#](https://docs.openvino.ai#class-ov-op-v14-maxpool)

-
class MaxPool : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[MaxPoolBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_max_pool_base.html#_CPPv4N2ov2op4util11MaxPoolBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v147MaxPoolE) MaxPooling operation with values and indices calculated as individual outputs.

Public Functions

-
MaxPool(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const[Strides](https://docs.openvino.ai/classov_1_1_strides.html#_CPPv4N2ov7StridesE)&strides, const[Strides](https://docs.openvino.ai/classov_1_1_strides.html#_CPPv4N2ov7StridesE)&dilations, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&pads_begin, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&pads_end, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&kernel, const[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[RoundingType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op12RoundingTypeE)rounding_type =[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[RoundingType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op12RoundingTypeE)::[FLOOR](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op12RoundingType5FLOORE), const[PadType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadTypeE)auto_pad =[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[PadType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadTypeE)::[EXPLICIT](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadType8EXPLICITE), const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)index_element_type =[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[i64](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7element3i64EN6Type_t3i64E), const int64_t axis = 0)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v147MaxPool7MaxPoolERK6OutputI4NodeERK7StridesRK7StridesRK5ShapeRK5ShapeRK5ShapeKN2op12RoundingTypeEK7PadTypeKN7element4TypeEK7int64_t) Constructs a parametrized

[MaxPool](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v14_1_1_max_pool)operation.- Parameters:
**arg**–[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)of a node producing the feature tensor to be pooled.**strides**– The strides of the pooling filter.**dilations**– The dilations of the pooling filter.**pads_begin**– Paddings at the beginning of each spatial axis.**pads_end**– Paddings at the end of each spatial axis.**kernel**– The kernel shape.**rounding_type**– Whether to use ceiling or floor rounding type while computing the output shape.**auto_pad**– The pad type for automatic calculation of the padding sizes.**index_element_type**– The data type used by the second output tensor containing the selected indices.**axis**– Indicates a dimension in the input data shape which should be used as a starting point for calculation of the upper bound of allowed values of the indices output.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v147MaxPool24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)get_index_element_type() const noexcept[#](https://docs.openvino.ai#_CPPv4NK2ov2op3v147MaxPool22get_index_element_typeEv) - Returns:
The data type of the second output tensor (indices).



-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op3v147MaxPool12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
MaxPool(const