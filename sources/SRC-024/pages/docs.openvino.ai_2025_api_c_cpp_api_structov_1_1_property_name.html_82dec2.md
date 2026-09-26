source: https://docs.openvino.ai/2025/api/c_cpp_api/structov_1_1_property_name.html
lastmod: 

# Struct ov::PropertyName[#](https://docs.openvino.ai#struct-ov-propertyname)

-
struct PropertyName : public std::string
[#](https://docs.openvino.ai#_CPPv4N2ov12PropertyNameE) This class is used to return property name and its mutability attribute.

Public Functions

-
inline PropertyName(const std::string &str, PropertyMutability mutability = PropertyMutability::RW)
[#](https://docs.openvino.ai#_CPPv4N2ov12PropertyName12PropertyNameERKNSt6stringE18PropertyMutability) Constructs property name object.

- Parameters:
**str**– property name**mutability**– property mutability



-
inline bool is_mutable() const
[#](https://docs.openvino.ai#_CPPv4NK2ov12PropertyName10is_mutableEv) check property mutability

- Returns:
true if property is mutable



-
inline PropertyName(const std::string &str, PropertyMutability mutability = PropertyMutability::RW)