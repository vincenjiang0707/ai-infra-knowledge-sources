source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v1_1_1_reduce_sum.html
lastmod: 

# Class ov::op::v1::ReduceSum[#](https://docs.openvino.ai#class-ov-op-v1-reducesum)

-
class ReduceSum : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[ArithmeticReductionKeepDims](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_arithmetic_reduction_keep_dims.html#_CPPv4N2ov2op4util27ArithmeticReductionKeepDimsE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v19ReduceSumE) [Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)sum operation.Element-wise sums the input tensor, eliminating the specified reduction axes. For example:

\[\begin{split} \mathit{sum}\left(\{0\}, \left[ \begin{array}{ccc} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{array} \right]\right) = \left[ (1 + 3 + 5), (2 + 4 + 6) \right] = \left[ 9, 12 \right]~~~\text{(dimension 0 (rows) is eliminated)} \end{split}\]\[\begin{split} \mathit{sum}\left(\{1\}, \left[ \begin{array}{ccc} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{array} \right]\right) = \left[ (1 + 2), (3 + 4), (5 + 6) \right] = \left[ 3, 7, 11 \right]~~~\text{(dimension 1 (columns) is eliminated)} \end{split}\]\[\begin{split} \mathit{sum}\left(\{0,1\}, \left[ \begin{array}{ccc} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{array} \right]\right) = (1 + 2) + (3 + 4) + (5 + 6) = 21~~~\text{(both dimensions (rows and columns) are eliminated)} \end{split}\]*Parameters*Description

`reduction_axes`

The axes to eliminate through summation.

`keep_dims`

If set to 1 it holds axes that are used for reduction.

*Inputs*Type

Description

`arg`

\(N[d_1,\dots,d_n]~(n \geq 0)\)

An input tensor of any shape and numeric element type.

Type

Description

\(N[\textit{delete}(A,d_1,\dots,d_n)]\)

The tensor \(T\), where \(T\) is the input tensor with the

`reduction_axes`

\(A\) eliminated by summation.Public Functions

-
ReduceSum() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v19ReduceSum9ReduceSumEv) Constructs a summation operation.


-
ReduceSum(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &reduction_axes, bool keep_dims = false)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v19ReduceSum9ReduceSumERK6OutputI4NodeERK6OutputI4NodeEb) Constructs a summation operation.

- Parameters:
**arg**– The tensor to be summed.**reduction_axes**– The axis positions (0-based) to be eliminated.**keep_dims**– If set to 1 it holds axes that are used for reduction.



-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v19ReduceSum12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
ReduceSum() = default