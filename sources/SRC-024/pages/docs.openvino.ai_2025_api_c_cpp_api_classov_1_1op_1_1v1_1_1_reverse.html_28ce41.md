source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v1_1_1_reverse.html
lastmod: 

# Class ov::op::v1::Reverse[#](https://docs.openvino.ai#class-ov-op-v1-reverse)

-
class Reverse : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v17ReverseE) [Reverse](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_reverse)operation.Public Functions

-
Reverse(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &reversed_axes, const std::string &mode)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v17Reverse7ReverseERK6OutputI4NodeERK6OutputI4NodeERKNSt6stringE) Constructs a reverse operation.

- Parameters:
**data**– The input tensor, some of whose axes are to be reversed.**reversed_axes**– The axes to reverse in a form of a set of indices or boolean mask.**mode**– The way reversed_axes should be interpreted - a set or a mask.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v17Reverse24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
inline Mode get_mode() const
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v17Reverse8get_modeEv) - Returns:
The second input data interpretation mode.



-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v17Reverse12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
Reverse(const