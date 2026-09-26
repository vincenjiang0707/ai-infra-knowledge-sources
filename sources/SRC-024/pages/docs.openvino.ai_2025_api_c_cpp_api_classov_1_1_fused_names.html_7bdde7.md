source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1_fused_names.html
lastmod: 

# Class ov::FusedNames[#](https://docs.openvino.ai#class-ov-fusednames)

-
class FusedNames : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[RuntimeAttribute](https://docs.openvino.ai/classov_1_1_runtime_attribute.html#_CPPv4N2ov16RuntimeAttributeE)[#](https://docs.openvino.ai#_CPPv4N2ov10FusedNamesE) FusedName class represents runtime info attribute that stores all operation names that was fully or partially fused into node.

Public Functions

-
FusedNames() = default
[#](https://docs.openvino.ai#_CPPv4N2ov10FusedNames10FusedNamesEv) A default constructor


-
inline explicit FusedNames(const std::string &name)
[#](https://docs.openvino.ai#_CPPv4N2ov10FusedNames10FusedNamesERKNSt6stringE) Constructs a new object consisting of a single name *.

- Parameters:
**name**–**[in]**The name


-
void fuseWith(const
[FusedNames](https://docs.openvino.ai#_CPPv4N2ov10FusedNamesE)&names)[#](https://docs.openvino.ai#_CPPv4N2ov10FusedNames8fuseWithERK10FusedNames) Unites current set of already fused names with another

[FusedNames](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_fused_names)object.- Parameters:
**names**–**[in]**Another object to fuse with


-
std::string getNames() const
[#](https://docs.openvino.ai#_CPPv4NK2ov10FusedNames8getNamesEv) return string with operation names separated by coma in alphabetical order


-
std::vector<std::string> getVectorNames() const
[#](https://docs.openvino.ai#_CPPv4NK2ov10FusedNames14getVectorNamesEv) return vector of fused names sorted in alphabetical order

- Returns:
vector if strings



-
virtual bool is_deterministic() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov10FusedNames16is_deterministicEv) If attribute is deterministic it should be included in cache hash computation.

- Returns:
true if deterministic otherwise false.



-
FusedNames() = default