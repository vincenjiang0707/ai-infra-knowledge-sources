source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v6_1_1_m_v_n.html
lastmod: 

# Class ov::op::v6::MVN[#](https://docs.openvino.ai#class-ov-op-v6-mvn)

-
class MVN : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v63MVNE) Operator performing Mean Variance Normalization.

Public Functions

-
MVN(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &reduction_axes, bool normalize_variance, float eps,[MVNEpsMode](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op10MVNEpsModeE)eps_mode)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v63MVN3MVNERK6OutputI4NodeERK6OutputI4NodeEbf10MVNEpsMode) Constructs an

[MVN](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v6_1_1_m_v_n)operation.- Parameters:
**data**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)tensor with data**reduction_axes**– A list of axes, along which to reduce.**normalize_variance**– flag that denotes whether to perform variance normalization.**eps**– the number to be added to the variance to avoid division by zero when normalizing the value**eps_mode**– the mode of applying epsilon



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v63MVN24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool evaluate(
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::TensorVector &output_values, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::TensorVector &input_values) const override[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v63MVN8evaluateERN2ov12TensorVectorERKN2ov12TensorVectorE) Evaluates the op on input_values putting results in output_values.

- Parameters:
**output_values**– Tensors for the outputs to compute. One for each result**input_values**– Tensors for the inputs. One for each inputs.

- Returns:
true if successful



-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v63MVN12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
MVN(const