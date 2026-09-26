source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1pattern_1_1op_1_1_or.html
lastmod: 

A submatch on the graph value is performed on each input to the [Or](group__ov__transformation__common__api.html#classov_1_1pass_1_1pattern_1_1op_1_1_or); the match succeeds on the first match. Otherwise the match fails.

Public Functions

-
inline Or(const OutputVector &patterns)

creates an [Or](group__ov__transformation__common__api.html#classov_1_1pass_1_1pattern_1_1op_1_1_or) node matching one of several sub-patterns in order. Does not add node to match list.

- Parameters:
**patterns** – The patterns to try for matching