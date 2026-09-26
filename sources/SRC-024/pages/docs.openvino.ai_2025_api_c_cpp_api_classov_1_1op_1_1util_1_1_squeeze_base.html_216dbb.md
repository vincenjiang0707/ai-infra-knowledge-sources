source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1util_1_1_squeeze_base.html
lastmod: 

# Class ov::op::util::SqueezeBase[#](https://docs.openvino.ai#class-ov-op-util-squeezebase)

-
class SqueezeBase : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op4util11SqueezeBaseE) Squeeze operation.

Subclassed by

[ov::op::v0::Squeeze](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_squeeze),[ov::op::v15::Squeeze](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v15_1_1_squeeze)Public Functions

-
SqueezeBase(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data)[#](https://docs.openvino.ai#_CPPv4N2ov2op4util11SqueezeBase11SqueezeBaseERK6OutputI4NodeE) Constructs a squeeze operation.

- Parameters:
**data**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)tensor with data


-
SqueezeBase(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &axes)[#](https://docs.openvino.ai#_CPPv4N2ov2op4util11SqueezeBase11SqueezeBaseERK6OutputI4NodeERK6OutputI4NodeE) Constructs a squeeze operation.

- Parameters:
**data**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)tensor with data**axis**– The axis along which to squeeze the input tensor.



-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op4util11SqueezeBase12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
SqueezeBase(const