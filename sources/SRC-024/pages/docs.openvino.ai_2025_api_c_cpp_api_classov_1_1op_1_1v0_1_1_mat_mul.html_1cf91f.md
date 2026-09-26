source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v0_1_1_mat_mul.html
lastmod: 

# Class ov::op::v0::MatMul[#](https://docs.openvino.ai#class-ov-op-v0-matmul)

-
class MatMul : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v06MatMulE) Operator performing Matrix Multiplication.

Public Functions

-
MatMul(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &A, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &B, const bool &transpose_a = false, const bool &transpose_b = false)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v06MatMul6MatMulERK6OutputI4NodeERK6OutputI4NodeERKbRKb) Constructs an Matrix Multiplication operation.

- Parameters:
**A**– Matrix A**B**– Matrix B**transpose_a**– If matrix A should be transposed.**transpose_b**– If matrix B should be transposed.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v06MatMul24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v06MatMul12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
MatMul(const