source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_broadcast_elementwise_fusion.html
lastmod: 

# Class ov::pass::BroadcastElementwiseFusion[#](https://docs.openvino.ai#class-ov-pass-broadcastelementwisefusion)

-
class BroadcastElementwiseFusion : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass26BroadcastElementwiseFusionE) Removing Broadcast OP before ElementWise if output shape of Broadcast are equal neighboring input shape of ElementWise.


Site Navigation

Section Navigation

Removing Broadcast OP before ElementWise if output shape of Broadcast are equal neighboring input shape of ElementWise.