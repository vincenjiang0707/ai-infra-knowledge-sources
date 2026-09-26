source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1_enum_names.html
lastmod: 

Class ov::EnumNames# template<typename EnumType>class EnumNames# Uses a pairings defined by EnumTypes::get() to convert between strings and enum values. Public Static Functions static inline EnumType as_enum(const std::string &name)# Converts strings to enum values. static inline const std::string &as_string(EnumType e)# Converts enum values to strings.