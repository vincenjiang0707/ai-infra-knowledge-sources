source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v0_1_1_l_r_n.html
lastmod: 

# Class ov::op::v0::LRN[#](https://docs.openvino.ai#class-ov-op-v0-lrn)

-
class LRN : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v03LRNE) Elementwise Local Response Normalization (

[LRN](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_l_r_n)) operation.*Inputs*Type

Description

`arg`

\(N[n, c, d_1,\dots,d_n]~(n \geq 0)\)

A tensor of any shape and numeric element type.

Type

Description

\(N[n, c, d_1,\dots,d_n]\)

The tensor \(T\), where \(T[n, c, d_1,\dots,d_n] = \frac{N[n,i,d_1,\dots,d_n]}{ (bias + alpha * (\sum_{i=max(0,(nsize-1)/2)}^{min(C, (nsize-1)/2)+1} N[n,i,d_1,\dots,d_n]^{2}) ^ {2})}\)

Public Functions

-
LRN(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, double alpha, double beta, double bias, size_t size)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v03LRN3LRNERK6OutputI4NodeEddd6size_t) Constructs a

[LRN](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_l_r_n)operation.- Parameters:
**arg**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)that produces the input tensor.


-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v03LRN24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
LRN(const