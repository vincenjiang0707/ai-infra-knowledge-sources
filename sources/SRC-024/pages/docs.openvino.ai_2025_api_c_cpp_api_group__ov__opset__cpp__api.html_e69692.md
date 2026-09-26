source: https://docs.openvino.ai/2025/api/c_cpp_api/group__ov__opset__cpp__api.html
lastmod: 

# Group Operation sets[#](https://docs.openvino.ai#group-operation-sets)

-
*group*Operation sets OpenVINO C++ API to work with operation sets

Functions

- const OPENVINO_API OpSet & get_opset1 ()
Returns

[opset1](https://docs.openvino.ai/group__ov__transformation__common__api.html#namespaceov_1_1opset1).

- const OPENVINO_API OpSet & get_opset2 ()
Returns

[opset2](https://docs.openvino.ai/group__ov__transformation__common__api.html#namespaceov_1_1opset2).

- const OPENVINO_API OpSet & get_opset3 ()
Returns

[opset3](https://docs.openvino.ai/group__ov__transformation__common__api.html#namespaceov_1_1opset3).

- const OPENVINO_API OpSet & get_opset4 ()
Returns

[opset4](https://docs.openvino.ai/group__ov__transformation__common__api.html#namespaceov_1_1opset4).

- const OPENVINO_API OpSet & get_opset5 ()
Returns

[opset5](https://docs.openvino.ai/group__ov__transformation__common__api.html#namespaceov_1_1opset5).

- const OPENVINO_API OpSet & get_opset6 ()
Returns

[opset6](https://docs.openvino.ai/group__ov__transformation__common__api.html#namespaceov_1_1opset6).

- const OPENVINO_API OpSet & get_opset7 ()
Returns

[opset7](https://docs.openvino.ai/group__ov__transformation__common__api.html#namespaceov_1_1opset7).

- const OPENVINO_API OpSet & get_opset8 ()
Returns

[opset8](https://docs.openvino.ai/group__ov__transformation__common__api.html#namespaceov_1_1opset8).

- const OPENVINO_API OpSet & get_opset9 ()
Returns

[opset9](https://docs.openvino.ai/group__ov__transformation__common__api.html#namespaceov_1_1opset9).

- const OPENVINO_API OpSet & get_opset10 ()
Returns

[opset10](https://docs.openvino.ai/group__ov__transformation__common__api.html#namespaceov_1_1opset10).

- const OPENVINO_API OpSet & get_opset11 ()
Returns

[opset11](https://docs.openvino.ai/group__ov__transformation__common__api.html#namespaceov_1_1opset11).

- const OPENVINO_API OpSet & get_opset12 ()
Returns

[opset12](https://docs.openvino.ai/group__ov__transformation__common__api.html#namespaceov_1_1opset12).

- const OPENVINO_API OpSet & get_opset13 ()
Returns

[opset13](https://docs.openvino.ai/group__ov__transformation__common__api.html#namespaceov_1_1opset13).

- const OPENVINO_API OpSet & get_opset14 ()
Returns

[opset14](https://docs.openvino.ai/group__ov__transformation__common__api.html#namespaceov_1_1opset14).

- const OPENVINO_API OpSet & get_opset15 ()
Returns

[opset15](https://docs.openvino.ai/group__ov__transformation__common__api.html#namespaceov_1_1opset15).

- const OPENVINO_API OpSet & get_opset16 ()
Returns

[opset16](https://docs.openvino.ai/group__ov__transformation__common__api.html#namespaceov_1_1opset16).

- const OPENVINO_API std::map< std::string, std::function< const ov::OpSet &()> > & get_available_opsets ()
Returns map of available opsets.


-
class OpSet
[#](https://docs.openvino.ai#_CPPv4N2ov5OpSetE) *#include <opset.hpp>*Run-time opset information.

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