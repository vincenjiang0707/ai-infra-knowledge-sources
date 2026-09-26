source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v0_1_1_m_v_n.html
lastmod: 

# Class ov::op::v0::MVN[#](https://docs.openvino.ai#class-ov-op-v0-mvn)

-
class MVN : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v03MVNE) Operator performing Mean Variance Normalization.

Public Functions

-
MVN(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, bool across_channels = true, bool normalize_variance = true, double eps = 1e-9)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v03MVN3MVNERK6OutputI4NodeEbbd) Constructs an

[MVN](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_m_v_n)operation.- Parameters:
**data**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)tensor with data**normalize_variance**– flag that denotes whether to perform variance normalization.**across_channels**– flag that denotes if mean values are shared across channels.**eps**– the number to be added to the variance to avoid division by zero when normalizing the value



-
MVN(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data,[AxisSet](https://docs.openvino.ai/classov_1_1_axis_set.html#_CPPv4N2ov7AxisSetE)reduction_axes, bool normalize_variance = true, double eps = 1e-9)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v03MVN3MVNERK6OutputI4NodeE7AxisSetbd) Constructs an

[MVN](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_m_v_n)operation.- Parameters:
**data**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)tensor with data**reduction_axes**– A list of axes, along which to reduce.**normalize_variance**– flag that denotes whether to perform variance normalization.**eps**– the number to be added to the variance to avoid division by zero when normalizing the value



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v03MVN24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
MVN(const