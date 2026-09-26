source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1descriptor_1_1_tensor.html
lastmod: 

# Class ov::descriptor::Tensor[#](https://docs.openvino.ai#class-ov-descriptor-tensor)

-
class Tensor
[#](https://docs.openvino.ai#_CPPv4N2ov10descriptor6TensorE) Compile-time descriptor of a first-class value that is a tensor.

Public Functions

-
Tensor(const
[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&element_type, const[PartialShape](https://docs.openvino.ai/classov_1_1_partial_shape.html#_CPPv4N2ov12PartialShapeE)&pshape, const std::unordered_set<std::string> &names = {})[#](https://docs.openvino.ai#_CPPv4N2ov10descriptor6Tensor6TensorERKN7element4TypeERK12PartialShapeRKNSt13unordered_setINSt6stringEEE) Creates

[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1descriptor_1_1_tensor)descriptor.- Parameters:
**element_type**– Element type**pshape**– Partial shape of tensor**names**–[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1descriptor_1_1_tensor)names (optional default empty).



-
const std::string &get_any_name() const
[#](https://docs.openvino.ai#_CPPv4NK2ov10descriptor6Tensor12get_any_nameEv) Gets any tensor name. Throws if tensor has no names.


-
const std::unordered_set<std::string> &get_names() const
[#](https://docs.openvino.ai#_CPPv4NK2ov10descriptor6Tensor9get_namesEv) Gets tensor names.


-
void set_names(const std::unordered_set<std::string> &names)
[#](https://docs.openvino.ai#_CPPv4N2ov10descriptor6Tensor9set_namesERKNSt13unordered_setINSt6stringEEE) Set new names.

- Parameters:
**names**– Names to set.


-
void add_names(const std::unordered_set<std::string> &names)
[#](https://docs.openvino.ai#_CPPv4N2ov10descriptor6Tensor9add_namesERKNSt13unordered_setINSt6stringEEE) Adds new names to tensor.

- Parameters:
**names**– new names to be added.


-
void set_value_symbol(const TensorSymbol &value_symbol)
[#](https://docs.openvino.ai#_CPPv4N2ov10descriptor6Tensor16set_value_symbolERK12TensorSymbol) sets value symbol description


-
void invalidate_values()
[#](https://docs.openvino.ai#_CPPv4N2ov10descriptor6Tensor17invalidate_valuesEv) unsets bound value descriptions


-
const
[PartialShape](https://docs.openvino.ai/classov_1_1_partial_shape.html#_CPPv4N2ov12PartialShapeE)&get_partial_shape() const[#](https://docs.openvino.ai#_CPPv4NK2ov10descriptor6Tensor17get_partial_shapeEv) Gets partial shape.


-
TensorSymbol get_value_symbol() const
[#](https://docs.openvino.ai#_CPPv4NK2ov10descriptor6Tensor16get_value_symbolEv) gets symbol value description


-
bool has_and_set_bound() const
[#](https://docs.openvino.ai#_CPPv4NK2ov10descriptor6Tensor17has_and_set_boundEv) checks if lower and upper bound are set and point to the same

[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1descriptor_1_1_tensor)

-
RTMap &get_rt_info()
[#](https://docs.openvino.ai#_CPPv4N2ov10descriptor6Tensor11get_rt_infoEv) Gets runtime informations.

- Returns:
Runtime information map which can be modified.



-
const RTMap &get_rt_info() const
[#](https://docs.openvino.ai#_CPPv4NK2ov10descriptor6Tensor11get_rt_infoEv) Gets runtime informations.

- Returns:
Read only runtime information map.



-
Tensor(const