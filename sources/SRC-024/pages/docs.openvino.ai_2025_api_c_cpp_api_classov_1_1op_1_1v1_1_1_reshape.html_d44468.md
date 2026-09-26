source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v1_1_1_reshape.html
lastmod: 

# Class ov::op::v1::Reshape[#](https://docs.openvino.ai#class-ov-op-v1-reshape)

-
class Reshape : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v17ReshapeE) [Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)dynamic reshape operation.“Converts” an input tensor into a new shape with the same number of elements. This op does not touch the actual data. If needed, use

[Transpose](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_transpose)for that purpose.Public Functions

-
Reshape(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &shape_pattern, bool special_zero)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v17Reshape7ReshapeERK6OutputI4NodeERK6OutputI4NodeEb) Constructs a dynamic reshape operation. This operation does not perform transpose.

- Parameters:
**arg**– The tensor to be reshaped.**shape_pattern**– The node that defines output shape shape_pattern. If the input shape is \((a_0,\dots,a_{k-1})\) then the output shape must be of the form \((b_0,\dots,b_{j-1})\) where \(\Pi(a_i) = \Pi(b_i)\). A value of -1 is allowed for at most one dimension, in which case the dimension size is inferred based on element count of input tensor.**special_zero**– Treats zeros in`shape_pattern`

as wildcard flags indicating a copy from input shape at the same index.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v17Reshape24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool evaluate(
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::TensorVector &outputs, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::TensorVector &inputs) const override[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v17Reshape8evaluateERN2ov12TensorVectorERKN2ov12TensorVectorE) Evaluates the op on input_values putting results in output_values.

- Parameters:
**output_values**– Tensors for the outputs to compute. One for each result**input_values**– Tensors for the inputs. One for each inputs.

- Returns:
true if successful



-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v17Reshape12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
Reshape(const