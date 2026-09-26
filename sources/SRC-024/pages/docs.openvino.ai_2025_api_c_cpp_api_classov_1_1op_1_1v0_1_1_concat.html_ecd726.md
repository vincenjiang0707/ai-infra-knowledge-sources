source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v0_1_1_concat.html
lastmod: 

# Class ov::op::v0::Concat[#](https://docs.openvino.ai#class-ov-op-v0-concat)

-
class Concat : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v06ConcatE) Concatenation operation.

Public Functions

-
Concat() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v06Concat6ConcatEv) Constructs a concatenation operation.


-
Concat(const OutputVector &args, int64_t axis)
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v06Concat6ConcatERK12OutputVector7int64_t) Constructs a concatenation operation.

- Parameters:
**args**– The outputs producing the input tensors.**axis**– The axis along which to concatenate the input tensors.



-
Concat(const NodeVector &args, int64_t axis)
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v06Concat6ConcatERK10NodeVector7int64_t) Constructs a concatenation operation.

- Parameters:
**args**– The nodes producing the input tensors.**axis**– The axis along which to concatenate the input tensors.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v06Concat24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
inline int64_t get_axis() const
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v06Concat8get_axisEv) - Returns:
The concatenation axis.



-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v06Concat12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
Concat() = default