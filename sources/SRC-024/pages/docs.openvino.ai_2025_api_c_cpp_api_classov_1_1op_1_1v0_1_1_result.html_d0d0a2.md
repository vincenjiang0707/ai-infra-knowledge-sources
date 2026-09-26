source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v0_1_1_result.html
lastmod: 

# Class ov::op::v0::Result[#](https://docs.openvino.ai#class-ov-op-v0-result)

-
class Result : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v06ResultE) [Result](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_result)operation.The

[Result](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_result)output tensor is special, it shares tensor with[Result](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_result)’s input but requires to have dedicated properties like:tensor names.


Setting/adding

[Result](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_result)’s output names modify this specific tensor names.[Result](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_result)’s specific tensor names are added to input descriptor and transferred to new descriptor if[Result](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_result)’s input has been replaced.Examples 1: No specific names on

[Result](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_result)’s outputset output names: [N1] ↓ |————-—| [names: N1] |————–—| |

[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)|—————————>|[Result](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_result)| ->[Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)output names: N1 |————-—| |————–—|Examples 2:

[Result](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_result)’s has got specific namesset output names: set output names: [N1] [R1, R2] ↓ ↓ |————-—| [names: N1, R1, R2] |————–—| |

[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)|—————————>|[Result](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_result)| ->[Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)output names: R1, R2 |————-—| |————–—|Examples 3:

[Result](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_result)from example 2 connected to new nodeset output names: set output names: [N2] [R1, R2] ↓ ↓ |————-—| [names: N2, R1, R2] |————–—| |

[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)|—————————>|[Result](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_result)| ->[Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)output names: R1, R2 |————-—| |————–—|set output names: [N1] ↓ |————-—| [names: N1] |

[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)|————–—> |————-—|Public Functions

-
Result() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v06Result6ResultEv) Allows a value to be used as a function result.


-
Result(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v06Result6ResultERK6OutputI4NodeE) Allows a value to be used as a function result.

- Parameters:
**arg**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)that produces the input tensor.


-
Result(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, bool use_input_names)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v06Result6ResultERK6OutputI4NodeEb) Allows a value to be used as a function result.


-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v06Result24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool evaluate(
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::TensorVector &outputs, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::TensorVector &inputs) const override[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v06Result8evaluateERN2ov12TensorVectorERKN2ov12TensorVectorE) Evaluates the op on input_values putting results in output_values.

- Parameters:
**output_values**– Tensors for the outputs to compute. One for each result**input_values**– Tensors for the inputs. One for each inputs.

- Returns:
true if successful



-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v06Result12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.