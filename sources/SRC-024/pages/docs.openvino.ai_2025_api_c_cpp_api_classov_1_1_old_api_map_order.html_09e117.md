source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1_old_api_map_order.html
lastmod: 

# Class ov::OldApiMapOrder[#](https://docs.openvino.ai#class-ov-oldapimaporder)

-
class OldApiMapOrder : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[RuntimeAttribute](https://docs.openvino.ai/classov_1_1_runtime_attribute.html#_CPPv4N2ov16RuntimeAttributeE)[#](https://docs.openvino.ai#_CPPv4N2ov14OldApiMapOrderE) [OldApiMapOrder](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_old_api_map_order)class represents runtime info attribute that stores order of the transpose that is required for obtaining IR in old API.[OldApiMapOrder](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_old_api_map_order)stores the following information. Parameter: Order of the transpose which should be applied to Parameter with old API layout to obtain Parameter with new API layout.Result: Order of the transpose which should be applied to Result with new API layout to obtain Result with old API layout.

Public Functions

-
OldApiMapOrder() = default
[#](https://docs.openvino.ai#_CPPv4N2ov14OldApiMapOrder14OldApiMapOrderEv) A default constructor


-
inline OldApiMapOrder(const std::vector<uint64_t> &value)
[#](https://docs.openvino.ai#_CPPv4N2ov14OldApiMapOrder14OldApiMapOrderERKNSt6vectorI8uint64_tEE) Constructs a new

[OldApiMapOrder](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_old_api_map_order)object.- Parameters:
**value**–**[in]**The object that stores values of[OldApiMapOrder](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_old_api_map_order).


-
OldApiMapOrder() = default