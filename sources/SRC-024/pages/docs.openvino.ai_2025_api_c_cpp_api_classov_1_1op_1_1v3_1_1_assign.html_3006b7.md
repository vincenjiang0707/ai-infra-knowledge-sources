source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v3_1_1_assign.html
lastmod: 

# Class ov::op::v3::Assign[#](https://docs.openvino.ai#class-ov-op-v3-assign)

-
class Assign : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[AssignBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_assign_base.html#_CPPv4N2ov2op4util10AssignBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v36AssignE) [Assign](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_assign)operation sets an input value to the variable with`variable_id`

Public Functions

-
Assign(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &new_value, const std::string &variable_id)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v36Assign6AssignERK6OutputI4NodeERKNSt6stringE) Constructs an

[Assign](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_assign)operation.- Parameters:
**new_value**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)that produces the input tensor.**variable_id**– identifier of the variable to be updated.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v36Assign24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
inline virtual std::string get_variable_id() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v36Assign15get_variable_idEv) Returns the identifier of corresponding variable.


-
Assign(const