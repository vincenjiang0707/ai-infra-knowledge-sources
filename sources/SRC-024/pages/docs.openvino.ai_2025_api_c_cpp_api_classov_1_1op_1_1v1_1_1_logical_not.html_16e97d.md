source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v1_1_1_logical_not.html
lastmod: 

# Class ov::op::v1::LogicalNot[#](https://docs.openvino.ai#class-ov-op-v1-logicalnot)

-
class LogicalNot : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v110LogicalNotE) Elementwise logical negation operation.

Public Functions

-
LogicalNot() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v110LogicalNot10LogicalNotEv) Constructs a logical negation operation.


-
LogicalNot(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v110LogicalNot10LogicalNotERK6OutputI4NodeE) Constructs a logical negation operation.

- Parameters:
**arg**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)that produces the input tensor.


-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v110LogicalNot24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v110LogicalNot12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
LogicalNot() = default