source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1_op_set.html
lastmod: 

# Class ov::OpSet[#](https://docs.openvino.ai#class-ov-opset)

-
class OpSet
[#](https://docs.openvino.ai#_CPPv4N2ov5OpSetE) Run-time opset information.

Public Functions

-
template<typename OP_TYPE>

inline void insert(const std::string &name)[#](https://docs.openvino.ai#_CPPv4I0EN2ov5OpSet6insertEvRKNSt6stringE) Insert OP_TYPE into the opset with a special name and the default factory.


-
template<typename OP_TYPE>

inline void insert()[#](https://docs.openvino.ai#_CPPv4I0EN2ov5OpSet6insertEvv) Insert OP_TYPE into the opset with the default name and factory.


-
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)*create_insensitive(const std::string &name) const[#](https://docs.openvino.ai#_CPPv4NK2ov5OpSet18create_insensitiveERKNSt6stringE) Create the op named name using it’s factory.


-
bool contains_type(const NodeTypeInfo &type_info) const
[#](https://docs.openvino.ai#_CPPv4NK2ov5OpSet13contains_typeERK12NodeTypeInfo) Return true if OP_TYPE is in the opset.


-
template<typename OP_TYPE>

inline bool contains_type() const[#](https://docs.openvino.ai#_CPPv4I0ENK2ov5OpSet13contains_typeEbv) Return true if OP_TYPE is in the opset.


-
bool contains_type(const std::string &name) const
[#](https://docs.openvino.ai#_CPPv4NK2ov5OpSet13contains_typeERKNSt6stringE) Return true if name is in the opset.


-
bool contains_type_insensitive(const std::string &name) const
[#](https://docs.openvino.ai#_CPPv4NK2ov5OpSet25contains_type_insensitiveERKNSt6stringE) Return true if name is in the opset.


-
template<typename OP_TYPE>