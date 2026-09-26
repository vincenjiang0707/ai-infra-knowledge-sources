source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1pattern_1_1_matcher.html
lastmod: 

# Class ov::pass::pattern::Matcher[#](https://docs.openvino.ai#class-ov-pass-pattern-matcher)

-
class Matcher
[#](https://docs.openvino.ai#_CPPv4N2ov4pass7pattern7MatcherE) [Matcher](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1pattern_1_1_matcher)looks for node patterns in a computation graph. The patterns are described by an automaton that is described by an extended computation graph. The matcher executes by attempting to match the start node of the pattern to a computation graph value (output of a[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)). In addition to determing if a match occurs, a pattern node may add graph nodes to a list of matched nodes, associate nodes with graph values, and start submatches. Submatches add match state changes to the enclosing match if the submatch succeeds; otherwise the state is reverted.The default match behavior of a pattern node with a graph nodes is that the computation graph value is added to the end of the matched value list and the match succeeds if the node/pattern types match and the input values match. In the case of a commutative node, the inputs can match in any order. If the matcher is in strict mode, the graph value element type and shape must also match.

Pattern nodes that have different match behavior are in

[ov::pass::pattern::op](https://docs.openvino.ai/group__ov__transformation__common__api.html#namespaceov_1_1pass_1_1pattern_1_1op)and have descriptions of their match behavior.Public Functions

-
inline Matcher(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &pattern_node, const std::string &name, bool strict_mode)[#](https://docs.openvino.ai#_CPPv4N2ov4pass7pattern7Matcher7MatcherERK6OutputI4NodeERKNSt6stringEb) Constructs a

[Matcher](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1pattern_1_1_matcher)object.- Parameters:
**pattern_node**– is a pattern sub graph that will be matched against input graphs**name**– is a string which is used for logging and disabling a matcher**strict_mode**– forces a matcher to consider shapes and ET of nodes



-
bool match(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &graph_value)[#](https://docs.openvino.ai#_CPPv4N2ov4pass7pattern7Matcher5matchERK6OutputI4NodeE) Matches a pattern to

`graph_node`

.- Parameters:
**graph_value**– is an input graph to be matched against


-
bool match(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &graph_value, const[PatternMap](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4pass7pattern10PatternMapE)&previous_matches)[#](https://docs.openvino.ai#_CPPv4N2ov4pass7pattern7Matcher5matchERK6OutputI4NodeERK10PatternMap) Matches a pattern to

`graph_node`

.- Parameters:
**graph_value**– is an input graph to be matched against**previous_matches**– contains previous mappings from labels to nodes to use



-
size_t add_node(
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> node)[#](https://docs.openvino.ai#_CPPv4N2ov4pass7pattern7Matcher8add_nodeE6OutputI4NodeE) Low-level helper to match recurring patterns.

- Parameters:
**graph**– is a graph to be matched against**pattern**– is a recurring pattern**rpattern**– specifies a node to recur from next**patterns**– a map from labels to matches



-
[MatcherState](https://docs.openvino.ai/classov_1_1pass_1_1pattern_1_1_matcher_state.html#_CPPv4N2ov4pass7pattern12MatcherStateE)start_match()[#](https://docs.openvino.ai#_CPPv4N2ov4pass7pattern7Matcher11start_matchEv) Try a match.


-
inline Matcher(const