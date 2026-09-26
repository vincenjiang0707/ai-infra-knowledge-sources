source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_grouped_gather_elimination.html
lastmod: 

# Class ov::pass::GroupedGatherElimination[#](https://docs.openvino.ai#class-ov-pass-groupedgatherelimination)

-
class GroupedGatherElimination : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass24GroupedGatherEliminationE) [GroupedGatherElimination](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_grouped_gather_elimination)transformation replaces group of Gather operations with the first Gather in this group and updated indices input in case all Gathers in the group are consumed by the same Concat in incremental order.