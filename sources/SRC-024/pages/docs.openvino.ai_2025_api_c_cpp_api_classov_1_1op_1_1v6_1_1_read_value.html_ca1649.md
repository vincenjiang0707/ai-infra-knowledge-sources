source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v6_1_1_read_value.html
lastmod: 

# Class ov::op::v6::ReadValue[#](https://docs.openvino.ai#class-ov-op-v6-readvalue)

-
class ReadValue : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[ReadValueBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_read_value_base.html#_CPPv4N2ov2op4util13ReadValueBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v69ReadValueE) [ReadValue](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v6_1_1_read_value)operation gets an input value from the variable with`variable_id`

and returns it as an output.Public Functions

Constructs a

[ReadValue](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v6_1_1_read_value)operation.- Parameters:
**variable**– Class for storing and synchronizing element types, shapes and identifiers between pairs of Assign/ReadValue nodes.


Constructs a

[ReadValue](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v6_1_1_read_value)operation.- Parameters:
**init_value**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)that produces the input tensor.**variable**– Class for storing and synchronizing element types, shapes and identifiers between pairs of Assign/ReadValue nodes.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v69ReadValue24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
inline virtual std::string get_variable_id() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v69ReadValue15get_variable_idEv) Returns the identifier of corresponding variable.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v69ReadValue12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.