source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_de_reshape_fully_connected.html
lastmod: 

# Class ov::pass::DeReshapeFullyConnected[#](https://docs.openvino.ai#class-ov-pass-dereshapefullyconnected)

-
class DeReshapeFullyConnected : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass23DeReshapeFullyConnectedE) Transformation uses symbol information to optimize out Reshape operations surrounding special cases of MatMul. It checks that surrounding Reshapes are only manipulating with batch dimensions of tensor in a do-undo kind of way. The difference with previous optimization is that this case has Reshape only on one input of MatMul and the other input is strictly 2D. Such MatMuls are also called FullyConnected.

Example: Before: [A,B,4096] -> Reshape -> [A*B,4096] MatMul [A*B,4608] -> Reshape -> [A,B,4608] [4096,4608]

After: [A,B,4096] -> MatMul -> [A,B,4608] [4096,4608] ->