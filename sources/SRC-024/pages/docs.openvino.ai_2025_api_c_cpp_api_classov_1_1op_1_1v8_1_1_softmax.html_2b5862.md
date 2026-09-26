source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v8_1_1_softmax.html
lastmod: 

# Class ov::op::v8::Softmax[#](https://docs.openvino.ai#class-ov-op-v8-softmax)

-
class Softmax : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v87SoftmaxE) [Softmax](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v8_1_1_softmax)operation with negative axis values.Public Functions

-
Softmax(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const int64_t axis = 1)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v87Softmax7SoftmaxERK6OutputI4NodeEK7int64_t) Constructs a softmax operation.

[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)`[d0, ...]`

- Parameters:
**arg**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)that produces the first input tensor.`[d0, ...]`

**axis**– The axis position (0-based) in range [-rank(arg), rank(arg) - 1] on which to calculate the softmax.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v87Softmax24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v87Softmax12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
Softmax(const