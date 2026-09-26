source: https://docs.openvino.ai/2025/api/c_cpp_api/structov_1_1element_1_1_if_type_of.html
lastmod: 

# Struct ov::element::IfTypeOf[#](https://docs.openvino.ai#struct-ov-element-iftypeof)

-
template<
[Type_t](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7element6Type_tE)...>

struct IfTypeOf[#](https://docs.openvino.ai#_CPPv4I_Dp6Type_tEN2ov7element8IfTypeOfE) Primary template defines suppoted element types.

The list of element types is used to check if runtime value of element type is one in the list. Base on this check the Visitor::visit function is called for specific element type.

- Template Parameters:
**List**– of supported[ov::element](https://docs.openvino.ai/group__ov__transformation__common__api.html#namespaceov_1_1element)types.