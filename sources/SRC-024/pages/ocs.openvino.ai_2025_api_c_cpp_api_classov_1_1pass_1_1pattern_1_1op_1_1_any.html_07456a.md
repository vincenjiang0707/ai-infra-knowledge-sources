source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1pattern_1_1op_1_1_any.html
lastmod: 

# Class ov::pass::pattern::op::Any[#](https://docs.openvino.ai#class-ov-pass-pattern-op-any)

-
class Any : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[pattern](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4pass7patternE)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4pass7pattern2opE)::[Pattern](https://docs.openvino.ai/classov_1_1pass_1_1pattern_1_1op_1_1_pattern.html#_CPPv4N2ov4pass7pattern2op7PatternE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass7pattern2op3AnyE) The graph value is to the matched value list. If the predicate is true for the node and the arguments match, the match succeeds.

Public Functions

-
template<typename TPredicate>

inline Any(const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&type, const[PartialShape](https://docs.openvino.ai/classov_1_1_partial_shape.html#_CPPv4N2ov12PartialShapeE)&s, const[TPredicate](https://docs.openvino.ai#_CPPv4I0EN2ov4pass7pattern2op3Any3AnyERKN7element4TypeERK12PartialShapeRK10TPredicateRK12OutputVector)&pred, const OutputVector &wrapped_values)[#](https://docs.openvino.ai#_CPPv4I0EN2ov4pass7pattern2op3Any3AnyERKN7element4TypeERK12PartialShapeRK10TPredicateRK12OutputVector) creates a

[Any](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1pattern_1_1op_1_1_any)node containing a sub-pattern described bySee also

type and

See also

shape.


-
template<typename TPredicate>

inline Any(const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &node, const[TPredicate](https://docs.openvino.ai#_CPPv4I0EN2ov4pass7pattern2op3Any3AnyERK6OutputI4NodeERK10TPredicateRK12OutputVector)&pred, const OutputVector &wrapped_values)[#](https://docs.openvino.ai#_CPPv4I0EN2ov4pass7pattern2op3Any3AnyERK6OutputI4NodeERK10TPredicateRK12OutputVector) creates a

[Any](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1pattern_1_1op_1_1_any)node containing a sub-pattern described by the type and shape ofSee also

node.


-
template<typename TPredicate>