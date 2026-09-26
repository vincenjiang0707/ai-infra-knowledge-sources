source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1_type_relaxed.html
lastmod: 

# Class ov::op::TypeRelaxed[#](https://docs.openvino.ai#class-ov-op-typerelaxed)

-
template<typename BaseOp>

class TypeRelaxed : public[BaseOp](https://docs.openvino.ai#_CPPv4I0EN2ov2op11TypeRelaxedE), public[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[TypeRelaxedBase](https://docs.openvino.ai/classov_1_1op_1_1_type_relaxed_base.html#_CPPv4N2ov2op15TypeRelaxedBaseE)[#](https://docs.openvino.ai#_CPPv4I0EN2ov2op11TypeRelaxedE) Relaxes tensor element type requirements for BaseOp inputs and outputs This class template should be used with

[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)descendant class. Defines a new operation by extending the original BaseOp operation with ability to accept inputs and provide outputs with element type that is unusual for BaseOp. For example, TypeRelaxed<opset1::Add> can accept mixed-precision inputs and provide another type of output. New types are provided as inputs attributes for[TypeRelaxed](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1_type_relaxed)template and fixed. There is no any deduction logic for types are provided as a part of this class and it should be implemented outside if required.Public Functions

-
template<typename ...Args>

inline TypeRelaxed(const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[TypeVector](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7element10TypeVectorE)&_input_data_types, const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[TypeVector](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7element10TypeVectorE)&_output_data_types,[Args](https://docs.openvino.ai#_CPPv4IDpEN2ov2op11TypeRelaxed11TypeRelaxedERKN7element10TypeVectorERKN7element10TypeVectorEDpRR4Args)&&... args)[#](https://docs.openvino.ai#_CPPv4IDpEN2ov2op11TypeRelaxed11TypeRelaxedERKN7element10TypeVectorERKN7element10TypeVectorEDpRR4Args) Creating a new

[TypeRelaxed](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1_type_relaxed)operation by calling one of the original op ctors forwarding arguments directly.

-
template<typename ...Args>