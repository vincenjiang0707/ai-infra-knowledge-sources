source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v8_1_1_if.html
lastmod: 

# Class ov::op::v8::If[#](https://docs.openvino.ai#class-ov-op-v8-if)

-
class If : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[MultiSubGraphOp](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_multi_sub_graph_op.html#_CPPv4N2ov2op4util15MultiSubGraphOpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v82IfE) [If](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v8_1_1_if)operation.Public Functions

-
If(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &execution_condition)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v82If2IfERK6OutputI4NodeE) Constructs

[If](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v8_1_1_if)with condition.- Parameters:
**execution_condition**– condition node.


-
inline const std::shared_ptr<
[Model](https://docs.openvino.ai/classov_1_1_model.html#_CPPv4N2ov5ModelE)> &get_then_body() const[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v82If13get_then_bodyEv) gets then_body as

[ov::Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model).- Returns:
then_body as

[ov::Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model).


-
inline const std::shared_ptr<
[Model](https://docs.openvino.ai/classov_1_1_model.html#_CPPv4N2ov5ModelE)> &get_else_body() const[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v82If13get_else_bodyEv) gets else_body as

[ov::Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model).- Returns:
else_body as

[ov::Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model).


sets new

[ov::Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)as new then_body.- Parameters:
**body**– new body for ‘then’ branch.


sets new

[ov::Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)as new else_body.- Parameters:
**body**– new body for ‘else’ branch.


sets new input to the operation associated with parameters of each sub-graphs

- Parameters:
**value**– input to operation**then_parameter**– parameter for then_body or nullptr**else_parameter**– parameter for else_body or nullpt



sets new output from the operation associated with results of each sub-graphs

- Parameters:
**then_result**– result from then_body**else_parameter**– result from else_body

- Returns:
output from operation



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v82If24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
If(const