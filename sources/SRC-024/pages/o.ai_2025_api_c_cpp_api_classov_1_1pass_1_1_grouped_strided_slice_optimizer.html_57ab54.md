source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_grouped_strided_slice_optimizer.html
lastmod: 

# Class ov::pass::GroupedStridedSliceOptimizer[#](https://docs.openvino.ai#class-ov-pass-groupedstridedsliceoptimizer)

-
class GroupedStridedSliceOptimizer : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[ModelPass](https://docs.openvino.ai/classov_1_1pass_1_1_model_pass.html#_CPPv4N2ov4pass9ModelPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass28GroupedStridedSliceOptimizerE) [GroupedStridedSliceOptimizer](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_grouped_strided_slice_optimizer)transformation replaces group of StridedSlice operations with VariadicSplit. All StridedSlice operations must slice data with the same axis and stride = 1.