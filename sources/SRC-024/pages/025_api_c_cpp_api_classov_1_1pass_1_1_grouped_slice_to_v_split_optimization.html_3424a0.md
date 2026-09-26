source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_grouped_slice_to_v_split_optimization.html
lastmod: 

# Class ov::pass::GroupedSliceToVSplitOptimization[#](https://docs.openvino.ai#class-ov-pass-groupedslicetovsplitoptimization)

-
class GroupedSliceToVSplitOptimization : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[ModelPass](https://docs.openvino.ai/classov_1_1pass_1_1_model_pass.html#_CPPv4N2ov4pass9ModelPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass32GroupedSliceToVSplitOptimizationE) [GroupedSliceToVSplitOptimization](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_grouped_slice_to_v_split_optimization)transformation replaces group of Slice operations with VariadicSplit. All Slice operations must slice data with the same axis and step = 1.