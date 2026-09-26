source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1util_1_1_scatter_elements_update_base.html
lastmod: 

# Class ov::op::util::ScatterElementsUpdateBase[#](https://docs.openvino.ai#class-ov-op-util-scatterelementsupdatebase)

-
class ScatterElementsUpdateBase : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op4util25ScatterElementsUpdateBaseE) Subclassed by

[ov::op::v12::ScatterElementsUpdate](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v12_1_1_scatter_elements_update),[ov::op::v3::ScatterElementsUpdate](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_scatter_elements_update)Public Functions

-
ScatterElementsUpdateBase(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &indices, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &updates, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &axis)[#](https://docs.openvino.ai#_CPPv4N2ov2op4util25ScatterElementsUpdateBase25ScatterElementsUpdateBaseERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeE) The common base class for all ScatterElementsUpdate operator versions.

- Parameters:
**data**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)data**indices**– Data entry index that will be updated**updates**– Update values**axis**– Axis to scatter on



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op4util25ScatterElementsUpdateBase24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op4util25ScatterElementsUpdateBase12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
ScatterElementsUpdateBase(const