source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1pattern_1_1op_1_1_optional.html
lastmod: 

# Class ov::pass::pattern::op::Optional[#](https://docs.openvino.ai#class-ov-pass-pattern-op-optional)

-
class Optional : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[pattern](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4pass7patternE)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4pass7pattern2opE)::[Pattern](https://docs.openvino.ai/classov_1_1pass_1_1pattern_1_1op_1_1_pattern.html#_CPPv4N2ov4pass7pattern2op7PatternE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass7pattern2op8OptionalE) A submatch on the graph value which contains optional op types defined in constructor.


pattern supports multi input operations. In this case the pattern checks inputs with optional node type or 1st input. The match is succeed in case of full graphs matching or extended by one of optional type graph or pattern. Otherwise fails.[Optional](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1pattern_1_1op_1_1_optional)Public Functions

-
inline Optional(const std::vector<
[DiscreteTypeInfo](https://docs.openvino.ai/structov_1_1_discrete_type_info.html#_CPPv4N2ov16DiscreteTypeInfoE)> &type_infos, const OutputVector &inputs = {})[#](https://docs.openvino.ai#_CPPv4N2ov4pass7pattern2op8Optional8OptionalERKNSt6vectorI16DiscreteTypeInfoEERK12OutputVector) creates an optional node matching one pattern. Add nodes to match list.

- Parameters:
**type_infos**–[Optional](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1pattern_1_1op_1_1_optional)operation types to exclude them from the matching in case the following op types do not exist in a pattern to match.**patterns**– The pattern to match a graph.



-
inline Optional(const std::vector<