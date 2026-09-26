source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1frontend_1_1_decoder_transformation_extension.html
lastmod: 

# Class ov::frontend::DecoderTransformationExtension[#](https://docs.openvino.ai#class-ov-frontend-decodertransformationextension)

-
class DecoderTransformationExtension : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Extension](https://docs.openvino.ai/classov_1_1_extension.html#_CPPv4N2ov9ExtensionE)[#](https://docs.openvino.ai#_CPPv4N2ov8frontend30DecoderTransformationExtensionE) Holds a transformation that is applied just after the original model graph is decoded. This class is a holder for transformation. The transformation can be specified as FunctionPass or MathcerPass derivatives or as a function that can be used to build corresponding FunctionPass or MatcherPass object. The type of the extension is determined in the moment of creation by calling corresponding ctor.

Public Functions

Create a custom functional pass where code of the pass is implemented as a function.


-
explicit DecoderTransformationExtension(const std::function<void(
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[MatcherPass](https://docs.openvino.ai/classov_1_1pass_1_1_matcher_pass.html#_CPPv4N2ov4pass11MatcherPassE)*)> &matcher_pass_initializer)[#](https://docs.openvino.ai#_CPPv4N2ov8frontend30DecoderTransformationExtension30DecoderTransformationExtensionERKNSt8functionIFvPN2ov4pass11MatcherPassEEEE) Create a custom matcher pass where the code of matcher pass initialization is a given function.


-
template<typename Transformation, typename std::enable_if<std::is_base_of<
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[PassBase](https://docs.openvino.ai/classov_1_1pass_1_1_pass_base.html#_CPPv4N2ov4pass8PassBaseE),[Transformation](https://docs.openvino.ai#_CPPv4I0_NSt9enable_ifINSt10is_base_ofIN2ov4pass8PassBaseE14TransformationE5valueEbE4typeEEN2ov8frontend30DecoderTransformationExtension30DecoderTransformationExtensionERK14Transformation)>::value, bool>::type = true>

inline explicit DecoderTransformationExtension(const[Transformation](https://docs.openvino.ai#_CPPv4I0_NSt9enable_ifINSt10is_base_ofIN2ov4pass8PassBaseE14TransformationE5valueEbE4typeEEN2ov8frontend30DecoderTransformationExtension30DecoderTransformationExtensionERK14Transformation)&transformation)[#](https://docs.openvino.ai#_CPPv4I0_NSt9enable_ifINSt10is_base_ofIN2ov4pass8PassBaseE14TransformationE5valueEbE4typeEEN2ov8frontend30DecoderTransformationExtension30DecoderTransformationExtensionERK14Transformation) Register existing transformation object which will be copied and kept for further registration.