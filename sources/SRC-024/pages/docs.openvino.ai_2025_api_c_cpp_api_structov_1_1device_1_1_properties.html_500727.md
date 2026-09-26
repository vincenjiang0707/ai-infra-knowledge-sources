source: https://docs.openvino.ai/2025/api/c_cpp_api/structov_1_1device_1_1_properties.html
lastmod: 

# Struct ov::device::Properties[#](https://docs.openvino.ai#struct-ov-device-properties)

-
struct Properties : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Property](https://docs.openvino.ai/classov_1_1_property.html#_CPPv4I0_18PropertyMutabilityEN2ov8PropertyE)<std::map<std::string, std::map<std::string,[Any](https://docs.openvino.ai/classov_1_1_any.html#_CPPv4N2ov3AnyE)>>>[#](https://docs.openvino.ai#_CPPv4N2ov6device10PropertiesE) Type for property to pass set of properties to specified device.

Public Functions

-
inline std::pair<std::string,
[Any](https://docs.openvino.ai/classov_1_1_any.html#_CPPv4N2ov3AnyE)> operator()(const AnyMap &config) const[#](https://docs.openvino.ai#_CPPv4NK2ov6device10PropertiesclERK6AnyMap) Constructs property.

- Parameters:
**configs**– set of property values with names- Returns:
Pair of string key representation and type erased property value.



-
inline std::pair<std::string,
[Any](https://docs.openvino.ai/classov_1_1_any.html#_CPPv4N2ov3AnyE)> operator()(const std::string &device_name, const AnyMap &config) const[#](https://docs.openvino.ai#_CPPv4NK2ov6device10PropertiesclERKNSt6stringERK6AnyMap) Constructs property.

- Parameters:
**device_name**– device plugin alias**config**– set of property values with names

- Returns:
Pair of string key representation and type erased property value.



-
template<typename ...Properties>

inline[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4utilE)::EnableIfAllStringAny<std::pair<std::string,[Any](https://docs.openvino.ai/classov_1_1_any.html#_CPPv4N2ov3AnyE)>,[Properties](https://docs.openvino.ai#_CPPv4IDpENK2ov6device10PropertiesclEN4util20EnableIfAllStringAnyINSt4pairINSt6stringE3AnyEEDp10PropertiesEERKNSt6stringEDpRR10Properties)...> operator()(const std::string &device_name,[Properties](https://docs.openvino.ai#_CPPv4IDpENK2ov6device10PropertiesclEN4util20EnableIfAllStringAnyINSt4pairINSt6stringE3AnyEEDp10PropertiesEERKNSt6stringEDpRR10Properties)&&... configs) const[#](https://docs.openvino.ai#_CPPv4IDpENK2ov6device10PropertiesclEN4util20EnableIfAllStringAnyINSt4pairINSt6stringE3AnyEEDp10PropertiesEERKNSt6stringEDpRR10Properties) Constructs property.

- Template Parameters:
**Properties**– Should be the pack of`std::pair<std::string,`

types[ov::Any](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_any)>- Parameters:
**device_name**– device plugin alias**configs**– Optional pack of pairs: (config parameter name, config parameter value)

- Returns:
Pair of string key representation and type erased property value.



-
inline std::pair<std::string,