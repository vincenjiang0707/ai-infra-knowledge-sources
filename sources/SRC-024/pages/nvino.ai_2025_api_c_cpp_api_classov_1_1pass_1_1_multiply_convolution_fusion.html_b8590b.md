source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_multiply_convolution_fusion.html
lastmod: 

# Class ov::pass::MultiplyConvolutionFusion[#](https://docs.openvino.ai#class-ov-pass-multiplyconvolutionfusion)

-
class MultiplyConvolutionFusion : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass25MultiplyConvolutionFusionE) Multiply->Convolution fusion replaces following graph:

+—-—+ +——-—+ |

[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)| | Constant | +—-—+ +——-—+ | |

| | v v +——-

—+ +———+ | Multiply | | Weights | +——-—+ +———+ | |

| | v v +————-

—+ | Convolution Op | +————-—+to following:

where ‘Convolution Op’ is one of:+---------+ +----------+ | Weights | | Constant | +---------+ +----------+ | | ------ ------ | | v v +-------+ +----------+ | Input | | Multiply | +-------+ +----------+ | | ----------- ---------- | | v v +----------------+ | Convolution Op | +----------------+

Convolution

ConvolutionBackpropData

GroupConvolution

GroupConvolutionBackpropData


Restrictions:

weights’ shape is static

if the constant input to Multiply has the same rank as weights, the constant first dimension has to be 1

constant input to Multiply has to be broadcastable to weights when ‘Convolution Op’ is either Convolution or GroupConvolution

shape of a constant input to Multiply has to be in one of following forms: (1), (1, 1, …, 1), (C, 1, …, 1), (1, C, 1, …, 1) when ‘Convolution Op’ is either ConvolutionBackpropData or GroupConvolutionBackpropData