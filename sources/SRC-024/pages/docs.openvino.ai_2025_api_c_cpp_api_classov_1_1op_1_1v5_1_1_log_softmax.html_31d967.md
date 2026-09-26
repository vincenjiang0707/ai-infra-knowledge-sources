source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v5_1_1_log_softmax.html
lastmod: 

# Class ov::op::v5::LogSoftmax[#](https://docs.openvino.ai#class-ov-op-v5-logsoftmax)

-
class LogSoftmax : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v510LogSoftmaxE) [LogSoftmax](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v5_1_1_log_softmax)operation.Public Functions

-
LogSoftmax(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const int64_t axis)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v510LogSoftmax10LogSoftmaxERK6OutputI4NodeEK7int64_t) Constructs a

[LogSoftmax](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v5_1_1_log_softmax)operation.[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)`[d0, ...]`

- Parameters:
**arg**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)that produces the first input tensor.`[d0, ...]`

**axis**– The axis position (0-based) on which to calculate the[LogSoftmax](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v5_1_1_log_softmax).



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v510LogSoftmax24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
LogSoftmax(const