source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v4_1_1_range.html
lastmod: 

# Class ov::op::v4::Range[#](https://docs.openvino.ai#class-ov-op-v4-range)

-
class Range : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v45RangeE) [Range](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v4_1_1_range)operation, analogous to`arange()`

in Numpy.Public Functions

-
Range() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v45Range5RangeEv) Constructs an unitialized range operation.


-
Range(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &start, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &stop, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &step,[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)output_type)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v45Range5RangeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeEN7element4TypeE) Constructs a range operation.

- Parameters:
**start**– The tensor producing the start value. Must be a scalar of numeric element type.**stop**– The tensor producing the stop value. Must be a scalar of numeric element type.**step**– The tensor producing the step value. Must be a scalar of numeric element type.**output_type**– The type of the output.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v45Range24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v45Range12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
Range() = default