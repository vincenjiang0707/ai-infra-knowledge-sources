source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v6_1_1_assign.html
lastmod: 

# Class ov::op::v6::Assign[#](https://docs.openvino.ai#class-ov-op-v6-assign)

-
class Assign : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[AssignBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_assign_base.html#_CPPv4N2ov2op4util10AssignBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v66AssignE) [Assign](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v6_1_1_assign)operation sets an input value to the variable with`variable_id`

Public Functions

Constructs an

[Assign](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v6_1_1_assign)operation.- Parameters:
**new_value**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)that produces the input tensor.**variable**– Class for storing and synchronizing element types, shapes and identifiers between pairs of Assign/ReadValue nodes.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v66Assign24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
inline virtual std::string get_variable_id() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v66Assign15get_variable_idEv) Returns the identifier of corresponding variable.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v66Assign12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.