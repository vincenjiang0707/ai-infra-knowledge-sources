source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v15_1_1_string_tensor_unpack.html
lastmod: 

# Class ov::op::v15::StringTensorUnpack[#](https://docs.openvino.ai#class-ov-op-v15-stringtensorunpack)

-
class StringTensorUnpack : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1518StringTensorUnpackE) Operator unpacking a batch of strings into three tensors.

Public Functions

-
StringTensorUnpack(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1518StringTensorUnpack18StringTensorUnpackERK6OutputI4NodeE) Constructs a

[StringTensorUnpack](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v15_1_1_string_tensor_unpack)operation.- Parameters:
**data**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)of type[element::string](https://docs.openvino.ai/group__ov__transformation__common__api.html#group__ov__element__cpp__api_1ga4460befbdeb69377360bdc52b2e61a25)


-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1518StringTensorUnpack24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
StringTensorUnpack(const