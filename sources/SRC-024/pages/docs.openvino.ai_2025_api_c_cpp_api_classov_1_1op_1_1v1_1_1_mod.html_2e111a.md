source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v1_1_1_mod.html
lastmod: 

# Class ov::op::v1::Mod[#](https://docs.openvino.ai#class-ov-op-v1-mod)

-
class Mod : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[BinaryElementwiseArithmetic](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_binary_elementwise_arithmetic.html#_CPPv4N2ov2op4util27BinaryElementwiseArithmeticE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v13ModE) [Mod](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_mod)returns an element-wise division reminder with two given tensors applying multi-directional broadcast rules.Public Functions

-
Mod(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &A, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &B, const[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)&auto_broadcast =[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)([AutoBroadcastType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastTypeE)::[NUMPY](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastType5NUMPYE)))[#](https://docs.openvino.ai#_CPPv4N2ov2op2v13Mod3ModERK6OutputI4NodeERK6OutputI4NodeERK17AutoBroadcastSpec) - Parameters:
**A**– - Dividend tensor**B**– - Divisor tensor**auto_broadcast**– Auto broadcast specification



-
virtual bool evaluate(
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::TensorVector &outputs, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::TensorVector &inputs) const override[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v13Mod8evaluateERN2ov12TensorVectorERKN2ov12TensorVectorE) Evaluates the op on input_values putting results in output_values.

- Parameters:
**output_values**– Tensors for the outputs to compute. One for each result**input_values**– Tensors for the inputs. One for each inputs.

- Returns:
true if successful



-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v13Mod12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
Mod(const