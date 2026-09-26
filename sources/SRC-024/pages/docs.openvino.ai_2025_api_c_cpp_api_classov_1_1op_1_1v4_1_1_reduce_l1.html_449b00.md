source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v4_1_1_reduce_l1.html
lastmod: 

# Class ov::op::v4::ReduceL1[#](https://docs.openvino.ai#class-ov-op-v4-reducel1)

-
class ReduceL1 : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[ArithmeticReductionKeepDims](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_arithmetic_reduction_keep_dims.html#_CPPv4N2ov2op4util27ArithmeticReductionKeepDimsE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v48ReduceL1E) Reduction operation using L1 norm: L1(x) = sum(abs(x)) if all dimensions are specified for the normalisation.

Reduces the tensor, eliminating the specified reduction axes by taking the L1-norm.

Public Functions

-
ReduceL1() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v48ReduceL18ReduceL1Ev) Constructs a reducet L1-norm operation.


-
ReduceL1(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &reduction_axes, bool keep_dims = false)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v48ReduceL18ReduceL1ERK6OutputI4NodeERK6OutputI4NodeEb) Constructs a reduce L1-norm operation.

- Parameters:
**arg**– The tensor to be reduced.**reduction_axes**– The axis positions (0-based) to be eliminated.**keep_dims**– If set to true it holds axes that are used for reduction.



-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v48ReduceL112has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
ReduceL1() = default