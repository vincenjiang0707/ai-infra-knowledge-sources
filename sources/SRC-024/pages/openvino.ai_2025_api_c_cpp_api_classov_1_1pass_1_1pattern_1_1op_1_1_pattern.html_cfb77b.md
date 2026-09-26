source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1pattern_1_1op_1_1_pattern.html
lastmod: 

# Class ov::pass::pattern::op::Pattern[#](https://docs.openvino.ai#class-ov-pass-pattern-op-pattern)

-
class Pattern : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass7pattern2op7PatternE) Subclassed by

[ov::pass::pattern::op::Any](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1pattern_1_1op_1_1_any),[ov::pass::pattern::op::AnyOf](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1pattern_1_1op_1_1_any_of),[ov::pass::pattern::op::AnyOutput](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1pattern_1_1op_1_1_any_output),[ov::pass::pattern::op::Block](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1pattern_1_1op_1_1_block),[ov::pass::pattern::op::Label](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1pattern_1_1op_1_1_label),[ov::pass::pattern::op::Optional](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1pattern_1_1op_1_1_optional),[ov::pass::pattern::op::Or](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1pattern_1_1op_1_1_or),[ov::pass::pattern::op::True](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1pattern_1_1op_1_1_true),[ov::pass::pattern::op::WrapType](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1pattern_1_1op_1_1_wrap_type)Public Functions

-
Pattern(const OutputVector &patterns, const
[Predicate](https://docs.openvino.ai/classov_1_1pass_1_1pattern_1_1op_1_1_predicate.html#_CPPv4N2ov4pass7pattern2op9PredicateE)&pred)[#](https://docs.openvino.ai#_CPPv4N2ov4pass7pattern2op7Pattern7PatternERK12OutputVectorRK9Predicate) A base class for all the utility operators used to describe a pattern to match.


-
virtual std::ostream &write_description(std::ostream &out, uint32_t depth) const override
[#](https://docs.openvino.ai#_CPPv4NK2ov4pass7pattern2op7Pattern17write_descriptionERNSt7ostreamE8uint32_t) Writes a description of a node to a stream.

- Parameters:
**os**– The stream; should be returned**depth**– How many levels of inputs to describe

- Returns:
The stream os



-
Pattern(const OutputVector &patterns, const