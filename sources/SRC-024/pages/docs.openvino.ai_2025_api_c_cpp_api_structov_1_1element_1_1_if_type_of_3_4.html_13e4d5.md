source: https://docs.openvino.ai/2025/api/c_cpp_api/structov_1_1element_1_1_if_type_of_3_4.html
lastmod: 

# Struct ov::element::IfTypeOf<>[#](https://docs.openvino.ai#struct-ov-element-iftypeof)

-
template<>

struct IfTypeOf<>[#](https://docs.openvino.ai#_CPPv4IEN2ov7element8IfTypeOfIEE) Applies visitor action for not supported

[ov::element](https://docs.openvino.ai/group__ov__transformation__common__api.html#namespaceov_1_1element)type.Public Static Functions

-
template<class Visitor, class ...Args>

static inline auto apply([Type_t](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7element6Type_tE)et,[Args](https://docs.openvino.ai#_CPPv4I0DpEN2ov7element8IfTypeOfIE5applyEN7Visitor11result_typeE6Type_tDpRR4Args)&&... args) -> typename[Visitor](https://docs.openvino.ai#_CPPv4I0DpEN2ov7element8IfTypeOfIE5applyEN7Visitor11result_typeE6Type_tDpRR4Args)::result_type[#](https://docs.openvino.ai#_CPPv4I0DpEN2ov7element8IfTypeOfIE5applyEN7Visitor11result_typeE6Type_tDpRR4Args) Applies visitor default action if input element type is not not supported by

[IfTypeOf](https://docs.openvino.ai/group__ov__transformation__common__api.html#structov_1_1element_1_1_if_type_of).Uses Visitor::visit non-template function.

- Template Parameters:
**Visitor**– Visitor class implementing visit function.**Args**– Types of visit parameters.

- Parameters:
**et**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)element type.**args**– Visitor arguments.

- Returns:
Value of result type returned by Visitor.



-
template<class Visitor, class ...Args>