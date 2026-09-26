source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_binarize_weights.html
lastmod: 

# Class ov::pass::BinarizeWeights[#](https://docs.openvino.ai#class-ov-pass-binarizeweights)

-
class BinarizeWeights : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass15BinarizeWeightsE) This transformation converts weights to -1/+1 form and applies normalization factors to output low/high and after Convolution. For example, following graph.

is transformed to:.... .... out_low out_high weights .. .. out_low out_high | | | | | | | | | +--------------------------+ +--------------------------+ | FakeQuantize (levels==2) | | FakeQuantize (levels==2) | | (on activations) | | (on weights) | +--------------------------+ +--------------------------+ | | | | ----------------- ------------------- | | v v +-------------+ | Convolution | +-------------+ | v

Normalization factors are chosen based output_high value. If it’s zero - norm factor is equal to output_low and output_high otherwisenormalized normalized .... .... out_low out_high | | | | +--------------------------+ +--------------------------+ | FakeQuantize (levels==2) | | Constant | | (on activations) | | (with converted weights) | +--------------------------+ +--------------------------+ | | | | ----------------- ------------------- | | v v +-------------+ | Convolution | +-------------+ | v +------------+ +---------------------------------------------------------------+ | Multiply | <---| Constant (normalization factor coming from FQ on activations) | +------------+ +---------------------------------------------------------------+ | v +------------+ +-----------------------------------------------------------+ | Multiply | <---| Constant (normalization factor coming from FQ on weights) | +------------+ +------------------------------------------------------------ | v