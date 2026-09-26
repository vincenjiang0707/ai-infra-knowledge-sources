source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v12_1_1_scatter_elements_update.html
lastmod: 

# Class ov::op::v12::ScatterElementsUpdate[#](https://docs.openvino.ai#class-ov-op-v12-scatterelementsupdate)

-
class ScatterElementsUpdate : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[ScatterElementsUpdateBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_scatter_elements_update_base.html#_CPPv4N2ov2op4util25ScatterElementsUpdateBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1221ScatterElementsUpdateE) Public Types

Public Functions

-
ScatterElementsUpdate(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &indices, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &updates, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &axis, const[Reduction](https://docs.openvino.ai#_CPPv4N2ov2op3v1221ScatterElementsUpdate9ReductionE)reduction =[Reduction](https://docs.openvino.ai#_CPPv4N2ov2op3v1221ScatterElementsUpdate9ReductionE)::[NONE](https://docs.openvino.ai#_CPPv4N2ov2op3v1221ScatterElementsUpdate9Reduction4NONEE), const bool use_init_val = true)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1221ScatterElementsUpdate21ScatterElementsUpdateERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeEK9ReductionKb) Constructs a

[ScatterElementsUpdate](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v12_1_1_scatter_elements_update)node.- Parameters:
**data**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)data**indices**– Data entry index that will be updated**updates**– Update values**axis**– Axis to scatter on



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1221ScatterElementsUpdate24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op3v1221ScatterElementsUpdate12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
ScatterElementsUpdate(const