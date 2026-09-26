source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v0_1_1_cum_sum.html
lastmod: 

# Class ov::op::v0::CumSum[#](https://docs.openvino.ai#class-ov-op-v0-cumsum)

-
class CumSum : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v06CumSumE) [Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)cumulative sum operation.Compute the cumulative sum of the input tensor along the axis specified.

Public Functions

-
CumSum() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v06CumSum6CumSumEv) Constructs a cumulative summation operation.


-
CumSum(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &axis, const bool exclusive = false, const bool reverse = false)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v06CumSum6CumSumERK6OutputI4NodeERK6OutputI4NodeEKbKb) Constructs a cumulative summation operation.

- Parameters:
**arg**– The tensor to be summed.**axis**– zero dimension tensor specifying axis position along which cumulative sum must be performed**exclusive**– if set to true, the top element is not included**reverse**– if set to true, will perform the sums in reverse direction



-
CumSum(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const bool exclusive = false, const bool reverse = false)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v06CumSum6CumSumERK6OutputI4NodeEKbKb) Constructs a cumulative summation operation with axis = 0.

- Parameters:
**arg**– The tensor to be summed


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v06CumSum12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v06CumSum24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
CumSum() = default