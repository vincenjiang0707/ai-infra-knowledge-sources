source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v3_1_1_non_zero.html
lastmod: 

# Class ov::op::v3::NonZero[#](https://docs.openvino.ai#class-ov-op-v3-nonzero)

-
class NonZero : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v37NonZeroE) [NonZero](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_non_zero)operation returning indices of non-zero elements in the input tensor.Note

The indices are returned by-dimension in row-major order. For example the following output contains 3 indices of a 3D input tensor elements: [[0, 0, 2], [0, 1, 1], [0, 1, 2]] The values point to input elements at [0,0,0], [0,1,1] and [2,1,2]

Public Functions

-
NonZero(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v37NonZero7NonZeroERK6OutputI4NodeE) Constructs a

[NonZero](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_non_zero)operation.Note

The output type is int64.

- Parameters:
**arg**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)that produces the input tensor.


-
NonZero(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const std::string &output_type)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v37NonZero7NonZeroERK6OutputI4NodeERKNSt6stringE) Constructs a

[NonZero](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_non_zero)operation.- Parameters:
**arg**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)that produces the input tensor.**output_type**– produce indices. Currently, only ‘int64’ or ‘int32’ are supported



-
NonZero(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&output_type)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v37NonZero7NonZeroERK6OutputI4NodeERKN7element4TypeE) Constructs a

[NonZero](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_non_zero)operation.- Parameters:
**arg**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)that produces the input tensor.**output_type**– produce indices. Currently, only int64 or int32 are supported



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v37NonZero24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v37NonZero12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
NonZero(const