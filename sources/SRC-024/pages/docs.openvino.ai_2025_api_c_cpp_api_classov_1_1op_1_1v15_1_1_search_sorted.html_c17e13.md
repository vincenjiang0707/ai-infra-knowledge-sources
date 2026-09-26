source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v15_1_1_search_sorted.html
lastmod: 

# Class ov::op::v15::SearchSorted[#](https://docs.openvino.ai#class-ov-op-v15-searchsorted)

-
class SearchSorted : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1512SearchSortedE) [SearchSorted](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v15_1_1_search_sorted)operation.Public Functions

-
SearchSorted(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &sorted_sequence, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &values, bool right_mode = false, const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&output_type =[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[i64](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7element3i64EN6Type_t3i64E))[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1512SearchSorted12SearchSortedERK6OutputI4NodeERK6OutputI4NodeEbRKN7element4TypeE) Constructs a

[SearchSorted](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v15_1_1_search_sorted)operation.- Parameters:
**sorted_sequence**– Sorted sequence to search in.**values**– Values to search indexs for.**right_mode**– If False, return the first suitable index that is found for given value. If True, return the last such index.**output_type**– The element type of the output tensor. This is purely an implementation flag, which is used to convert the output type for CPU plugin in ConvertPrecision transformation (and potentially other plugins as well). Setting this flag to[element::i32](https://docs.openvino.ai/group__ov__transformation__common__api.html#group__ov__element__cpp__api_1ga53dd97bfbd724cee3266cc80d758f323)will result in the output tensor of i32 element type. Setting this flag to[element::i64](https://docs.openvino.ai/group__ov__transformation__common__api.html#group__ov__element__cpp__api_1ga6c86a9a54d44fc205ad9cbf28ca556a6)will generally not give any effect, since it will be converted to i32 anyway, at least for CPU plugin.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1512SearchSorted24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
SearchSorted(const