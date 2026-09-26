source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_conv_to_binary_conv.html
lastmod: 

# Class ov::pass::ConvToBinaryConv[#](https://docs.openvino.ai#class-ov-pass-convtobinaryconv)

-
class ConvToBinaryConv : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass16ConvToBinaryConvE) This transformation converts Convolution to BinaryConvolution under following conditions:

first input to Convolution is a FakeQuantize with levels==2 with output low,high being either (0, 1) or (-1, 1)

second input (weights) is a constant with values -1 or 1 The transformation also converts weights to binary Constant (with ‘u1’ type) For example, when output_low is equal to 0 and output_high is equal to 1, following graph

is transformed to:.... .... out_low out_high | | | | +--------------------------+ +-------------------------------------+ | FakeQuantize (levels==2) | | Constant | | (on activations) | | (weights containing -1 or 1 values) | +--------------------------+ +-------------------------------------+ | | | | ----------------- ------------------- | | v v +-------------+ | Convolution | +-------------+ | v

.... .... out_low out_high | | | | +--------------------------+ +---------------------------------+ | FakeQuantize (levels==2) | | Constant (with u1 type) | | (on activations) | | (with u1 type - binary weights) | +--------------------------+ +---------------------------------+ | | | | ----------------- ------------------- | | v v +-------------------+ | BinaryConvolution | +-------------------+ | v +------------+ +----------------------------------------------------+ | | | Constant | | Add | <---| (weights from original graph, | | | | sum-reduced over [1,..., len(weights.shape)] axes | +------------+ +----------------------------------------------------+ | v +------------+ +-----+ | Multiply | <---| 0.5 | +------------+ +-----+ | v