source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_depth_to_space_fusion.html
lastmod: 

# Class ov::pass::DepthToSpaceFusion[#](https://docs.openvino.ai#class-ov-pass-depthtospacefusion)

-
class DepthToSpaceFusion : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass18DepthToSpaceFusionE) [DepthToSpaceFusion](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_depth_to_space_fusion)transformation detects Reshape-Transpose-Reshape pattern and tries to fuse it into a single DepthToSpace layer.[DepthToSpaceFusion](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_depth_to_space_fusion)transformation is optional and disabled by default. The transformation can be enabled with callback using setCallback method. See the example below.Callback example:

// This callback enables DepthToSpaceFusion transformation auto callback = [](const std::shared_ptr<const ov::Node> & node) -> bool { return ov::as_type_ptr<const ov::opset3::DepthToSpace>(node) != nullptr; }; auto p = ov::pass::DepthToSpaceFusion(); p.setCallback(callback); p.run_on_function(f);