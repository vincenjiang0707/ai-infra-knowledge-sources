source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_proposal1_scales.html
lastmod: 

# Class ov::pass::Proposal1Scales[#](https://docs.openvino.ai#class-ov-pass-proposal1scales)

-
class Proposal1Scales : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass15Proposal1ScalesE) ProposalScales transformation helps to silently avoid reshape issues on the scale-input of Proposal layer.

Expected sub-graph looks like: Parameter [batch, 3 or 4] -> Reshape [-1] -(in: 3)-> PriorBox

PriorBox operation accepts 3 or 4 values as scales from specification standpoint PriorBox uses first set (batch) of scale values to proceed in the plugins According to this we explicitly take first batch of scales with StridedSlice operation

Resulting sub-graph: Parameter [batch, 3 or 4] -> Reshape [-1] -> StridedSlice[0: 3 or 4] -(in: 3)-> PriorBox