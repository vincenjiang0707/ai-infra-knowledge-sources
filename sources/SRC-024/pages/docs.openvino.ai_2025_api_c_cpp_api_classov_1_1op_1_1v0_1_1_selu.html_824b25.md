source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v0_1_1_selu.html
lastmod: 

# Class ov::op::v0::Selu[#](https://docs.openvino.ai#class-ov-op-v0-selu)

-
class Selu : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v04SeluE) Performs a SELU activation function on all elements of the input node.

Public Functions

-
Selu(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &alpha, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &lambda)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v04Selu4SeluERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeE) Constructs a

[Selu](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_selu)node.- Parameters:
**data**– -[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing the input tensor**alpha**– - Alpha coefficient of SELU operation**lambda**– - Lambda coefficient of SELU operation



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v04Selu24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
Selu(const