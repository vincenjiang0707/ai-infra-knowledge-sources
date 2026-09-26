source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_fake_quantize_reshape_fusion.html
lastmod: 

# Class ov::pass::FakeQuantizeReshapeFusion[#](https://docs.openvino.ai#class-ov-pass-fakequantizereshapefusion)

-
class FakeQuantizeReshapeFusion : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass25FakeQuantizeReshapeFusionE) This transformation looks for a FQ + Reshape pair in the graph and moves the Reshape operation above the FQ node. Shapes of limit inputs are updated following FQ broadcasting semantics.