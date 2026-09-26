source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_select_with_one_value_condition.html
lastmod: 

# Class ov::pass::SelectWithOneValueCondition[#](https://docs.openvino.ai#class-ov-pass-selectwithonevaluecondition)

-
class SelectWithOneValueCondition : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass27SelectWithOneValueConditionE) [SelectWithOneValueCondition](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_select_with_one_value_condition)transformation eliminates Select operation if the condition is constant and consists of al True or False elements.