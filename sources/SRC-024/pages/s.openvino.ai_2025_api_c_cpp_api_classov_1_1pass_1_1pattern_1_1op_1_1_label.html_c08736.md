source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1pattern_1_1op_1_1_label.html
lastmod: 

# Class ov::pass::pattern::op::Label[#](https://docs.openvino.ai#class-ov-pass-pattern-op-label)

-
class Label : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[pattern](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4pass7patternE)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4pass7pattern2opE)::[Pattern](https://docs.openvino.ai/classov_1_1pass_1_1pattern_1_1op_1_1_pattern.html#_CPPv4N2ov4pass7pattern2op7PatternE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass7pattern2op5LabelE) Fails if the predicate returns false on the graph value.

The graph value is added to the matched values list. If the

[Label](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1pattern_1_1op_1_1_label)is already associated with a value, the match succeeds if the value is the same as the graph value. Otherwise, the label is associated with the graph value and the match succeeds if the pattern input matches the graph value.DEPRECATED: If no inputs are given to

[Label](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1pattern_1_1op_1_1_label), a[True](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1pattern_1_1op_1_1_true)node is serves as the input. If more than one inputs are given, an[Or](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1pattern_1_1op_1_1_or)pattern of the inputs serves as the input.Public Functions

-
template<typename TPredicate, typename TArg = OutputVector>

inline Label(const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&type, const[PartialShape](https://docs.openvino.ai/classov_1_1_partial_shape.html#_CPPv4N2ov12PartialShapeE)&s, const[TPredicate](https://docs.openvino.ai#_CPPv4I00EN2ov4pass7pattern2op5Label5LabelERKN7element4TypeERK12PartialShapeRK10TPredicateRK4TArg)&pred, const[TArg](https://docs.openvino.ai#_CPPv4I00EN2ov4pass7pattern2op5Label5LabelERKN7element4TypeERK12PartialShapeRK10TPredicateRK4TArg)&wrapped_values = OutputVector{})[#](https://docs.openvino.ai#_CPPv4I00EN2ov4pass7pattern2op5Label5LabelERKN7element4TypeERK12PartialShapeRK10TPredicateRK4TArg) creates a

[Label](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1pattern_1_1op_1_1_label)node containing a sub-pattern described bythis

[Label](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1pattern_1_1op_1_1_label)node can be bound only to the nodes in the input graph that match the pattern specified bySee also

type and

See also

shape.

See also

wrapped_nodes Example:

auto add = a + b; // a and b are op::Parameter in this example auto label = std::make_shared<pattern::op::Label>(element::f32, PartialShape{2,2}, nullptr, OutputVector{add});


-
template<typename TPredicate, typename TArg = OutputVector>

inline Label(const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &value, const[TPredicate](https://docs.openvino.ai#_CPPv4I00EN2ov4pass7pattern2op5Label5LabelERK6OutputI4NodeERK10TPredicateRK4TArg)&pred, const[TArg](https://docs.openvino.ai#_CPPv4I00EN2ov4pass7pattern2op5Label5LabelERK6OutputI4NodeERK10TPredicateRK4TArg)&wrapped_values = OutputVector{})[#](https://docs.openvino.ai#_CPPv4I00EN2ov4pass7pattern2op5Label5LabelERK6OutputI4NodeERK10TPredicateRK4TArg) creates a

[Label](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1pattern_1_1op_1_1_label)node containing a sub-pattern described by the type and shape ofthis

[Label](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1pattern_1_1op_1_1_label)node can be bound only to the nodes in the input graph that match the pattern specified bySee also

node.

See also

wrapped_values Example:

auto add = a + b; // a and b are op::Parameter in this example auto label = std::make_shared<pattern::op::Label>(add, nullptr, OutputVector{add});


-
template<typename TPredicate, typename TArg = OutputVector>