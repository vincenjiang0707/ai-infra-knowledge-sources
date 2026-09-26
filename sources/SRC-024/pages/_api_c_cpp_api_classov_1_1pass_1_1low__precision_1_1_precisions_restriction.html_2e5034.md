source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1low__precision_1_1_precisions_restriction.html
lastmod: 

# Class ov::pass::low_precision::PrecisionsRestriction[#](https://docs.openvino.ai#class-ov-pass-low-precision-precisionsrestriction)

-
class PrecisionsRestriction
[#](https://docs.openvino.ai#_CPPv4N2ov4pass13low_precision21PrecisionsRestrictionE) [PrecisionsRestriction](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1low__precision_1_1_precisions_restriction)defines a set of precision restrictions for each input port Common precision restriction can be also set for several ports. In this case, an operation will have the same precision for mentioned.// One restriction for each port PrecisionsRestriction::create<ov::opset1::Convolution>({ {{0}, {

[ov::element::u8](https://docs.openvino.ai/group__ov__transformation__common__api.html#group__ov__element__cpp__api_1gaaf60c536d3e295285f6a899eb3d29e2f)}}, {{1}, {[ov::element::i8](https://docs.openvino.ai/group__ov__transformation__common__api.html#group__ov__element__cpp__api_1gaae12d14b28baf46d3c6f76c55b05fb42)}}, }),// Common precision restriction for several ports: // both inputs will have the same precision PrecisionsRestriction::create<ov::opset5::LSTMSequence>({ {{0, 1}, {

[ov::element::u8](https://docs.openvino.ai/group__ov__transformation__common__api.html#group__ov__element__cpp__api_1gaaf60c536d3e295285f6a899eb3d29e2f),[ov::element::i8](https://docs.openvino.ai/group__ov__transformation__common__api.html#group__ov__element__cpp__api_1gaae12d14b28baf46d3c6f76c55b05fb42)}} }),