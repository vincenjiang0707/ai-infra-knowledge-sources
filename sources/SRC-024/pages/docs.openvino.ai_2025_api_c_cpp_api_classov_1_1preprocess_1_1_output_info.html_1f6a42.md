source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1preprocess_1_1_output_info.html
lastmod: 

# Class ov::preprocess::OutputInfo[#](https://docs.openvino.ai#class-ov-preprocess-outputinfo)

-
class OutputInfo
[#](https://docs.openvino.ai#_CPPv4N2ov10preprocess10OutputInfoE) Class holding postprocessing information for one output From postprocessing pipeline perspective, each output can be represented as:

[Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)’s output info, ([OutputInfo::model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1preprocess_1_1_output_info_1ad8abcb4ef25a13f6e837fbca256ce0cd))Postprocessing steps applied to user’s input (

[OutputInfo::postprocess](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1preprocess_1_1_output_info_1a1cf736d81c686e8381e1492320ce9c79))User’s desired output parameter information, which is a final one after preprocessing (

[OutputInfo::tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1preprocess_1_1_output_info_1afd9f5eab957e75ce8b2b9a3f9e518342))

Public Functions

-
OutputInfo(
[OutputInfo](https://docs.openvino.ai#_CPPv4N2ov10preprocess10OutputInfo10OutputInfoERR10OutputInfo)&&other) noexcept[#](https://docs.openvino.ai#_CPPv4N2ov10preprocess10OutputInfo10OutputInfoERR10OutputInfo) Move constructor.


-
[OutputInfo](https://docs.openvino.ai#_CPPv4N2ov10preprocess10OutputInfoE)&operator=([OutputInfo](https://docs.openvino.ai#_CPPv4N2ov10preprocess10OutputInfoE)&&other) noexcept[#](https://docs.openvino.ai#_CPPv4N2ov10preprocess10OutputInfoaSERR10OutputInfo) Move assignment operator.


-
~OutputInfo()
[#](https://docs.openvino.ai#_CPPv4N2ov10preprocess10OutputInfoD0Ev) Default destructor.


-
[OutputModelInfo](https://docs.openvino.ai/classov_1_1preprocess_1_1_output_model_info.html#_CPPv4N2ov10preprocess15OutputModelInfoE)&model()[#](https://docs.openvino.ai#_CPPv4N2ov10preprocess10OutputInfo5modelEv) Get current output model information with ability to change original model’s output data.

- Returns:
Reference to current model’s output information structure



-
[PostProcessSteps](https://docs.openvino.ai/classov_1_1preprocess_1_1_post_process_steps.html#_CPPv4N2ov10preprocess16PostProcessStepsE)&postprocess()[#](https://docs.openvino.ai#_CPPv4N2ov10preprocess10OutputInfo11postprocessEv) Get current output post-process information with ability to add more post-processing steps.

- Returns:
Reference to current preprocess steps structure



-
[OutputTensorInfo](https://docs.openvino.ai/classov_1_1preprocess_1_1_output_tensor_info.html#_CPPv4N2ov10preprocess16OutputTensorInfoE)&tensor()[#](https://docs.openvino.ai#_CPPv4N2ov10preprocess10OutputInfo6tensorEv) Get current output tensor information with ability to change specific data.

- Returns:
Reference to current output tensor structure