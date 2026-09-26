source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v3_1_1_read_value.html
lastmod: 

# Class ov::op::v3::ReadValue[#](https://docs.openvino.ai#class-ov-op-v3-readvalue)

-
class ReadValue : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[ReadValueBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_read_value_base.html#_CPPv4N2ov2op4util13ReadValueBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v39ReadValueE) [ReadValue](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_read_value)operation creates the variable with`variable_id`

and returns value of this variable.Public Functions

-
ReadValue(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &init_value, const std::string &variable_id)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v39ReadValue9ReadValueERK6OutputI4NodeERKNSt6stringE) Constructs a

[ReadValue](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_read_value)operation.- Parameters:
**init_value**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)that produces the input tensor.**variable_id**– identificator of the variable to create.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v39ReadValue24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
inline virtual std::string get_variable_id() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v39ReadValue15get_variable_idEv) Returns the identifier of corresponding variable.


-
ReadValue(const