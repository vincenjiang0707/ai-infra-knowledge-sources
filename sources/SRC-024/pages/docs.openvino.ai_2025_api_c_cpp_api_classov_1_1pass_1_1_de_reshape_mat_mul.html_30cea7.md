source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_de_reshape_mat_mul.html
lastmod: 

# Class ov::pass::DeReshapeMatMul[#](https://docs.openvino.ai#class-ov-pass-dereshapematmul)

-
class DeReshapeMatMul : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass15DeReshapeMatMulE) Transformation uses symbol information to optimize out Reshape operations surrounding MatMul. It checks that surrounding Reshapes are only manipulating with batch dimensions of tensor in a do-undo kind of way.

Example: Before: [A,B,C,D] -> Reshape -> [A*B,C,D] MatMul [A*B,C,E] -> Reshape -> [A,B,C,E] [A,B,D,E] -> Reshape -> [A*B,D,E]

After: [A,B,C,D] -> MatMul -> [A,B,C,E] [A,B,D,E] ->

Transformation allows slightly different variations of the pattern on inputs of MatMul.

Simplest pattern contains only Reshape operation on MatMul input: Reshape -> MatMul

The next acceptable variation is Concat of two inputs on MatMul input: Reshape -[-> Concat -]-> MatMul This variation would be transformed with realignment of the other input of Concat and the other outputs of Concat with the help of Reshape operations

The most complex variation on the MatMul input pattern is with Binary Elementwise Operation with scalar second input: Reshape -[-> Concat -]-[-> BEA (scalar) -]-> MatMul


Additionally, transformation supports variation of the pattern on output of MatMul. It allows for Binary Elementwise Arithmetic operation without second input scalar restriction. MatMul -[-> BEA -]-> Reshape this pattern variation is only applicable for the case when input reshapes are 4D -> 3D and output reshape is 3D -> 4D. Additionally, shape symbols on output of MatMul should be equal to the input shape symbols of the last Reshape, meaning that this Binary Elementwise Arithmetic doesn’t perform any broadcasting of input coming from MatMul — only other input may be broadcasted to the MatMul input of this BEA. This effect (equality of MatMul output shape symbols and output shape of BEA) is being handled by

[LabelResolvingThroughSelect](https://docs.openvino.ai/group__ov__dev__exec__model.html#classov_1_1pass_1_1_label_resolving_through_select)transformation in the particular models that this variation targets.Full pattern this transformation searches for: -> Reshape -[-> Concat -]-[-> BEA (scalar) -]-> MatMul -[-> BEA -]-> Reshape -> -> Reshape -[-> Concat -]-[-> BEA (scalar) -]->

NOTE: input branches could be (and in observed model cases are) asymmetrical, meaning that the presence of Concat on one input of MatMul doesn’t require the other input to also have Concat