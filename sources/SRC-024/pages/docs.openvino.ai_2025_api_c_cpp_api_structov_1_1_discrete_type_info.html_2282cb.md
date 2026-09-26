source: https://docs.openvino.ai/2025/api/c_cpp_api/structov_1_1_discrete_type_info.html
lastmod: 

# Struct ov::DiscreteTypeInfo[#](https://docs.openvino.ai#struct-ov-discretetypeinfo)

-
struct DiscreteTypeInfo
[#](https://docs.openvino.ai#_CPPv4N2ov16DiscreteTypeInfoE) Type information for a type system without inheritance; instances have exactly one type not related to any other type.

Supports three functions,

[ov::is_type<Type>](https://docs.openvino.ai/group__ov__transformation__common__api.html#namespaceov_1ad291be1aadbe791ff028cabafbb8c121),[ov::as_type<Type>](https://docs.openvino.ai/group__ov__transformation__common__api.html#namespaceov_1a256640280744d370491c0ee03009fb28), and[ov::as_type_ptr<Type>](https://docs.openvino.ai/group__ov__transformation__common__api.html#namespaceov_1a349526e15197857749ee1a488814e7ec)for type-safe dynamic conversions via static_cast/static_ptr_cast without using C++ RTTI. Type must have a static type_info member and a virtual get_type_info() member that returns a reference to its type_info member.