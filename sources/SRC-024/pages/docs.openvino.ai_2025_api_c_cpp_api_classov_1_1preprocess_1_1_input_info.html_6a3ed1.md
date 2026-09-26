source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1preprocess_1_1_input_info.html
lastmod: 

# Class ov::preprocess::InputInfo[#](https://docs.openvino.ai#class-ov-preprocess-inputinfo)

-
class InputInfo
[#](https://docs.openvino.ai#_CPPv4N2ov10preprocess9InputInfoE) Class holding preprocessing information for one input From preprocessing pipeline perspective, each input can be represented as:

User’s input parameter info (

[InputInfo::tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1preprocess_1_1_input_info_1a7385ef9e3f1c61a87ddee256684638ae))Preprocessing steps applied to user’s input (

[InputInfo::preprocess](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1preprocess_1_1_input_info_1afaeba871501b27522b96f39a3d91f35e))[Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)’s input info, which is a final input’s info after preprocessing ([InputInfo::model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1preprocess_1_1_input_info_1a7a1ddc0dea4daa83998995e491adf667))

Public Functions

-
~InputInfo()
[#](https://docs.openvino.ai#_CPPv4N2ov10preprocess9InputInfoD0Ev) Default destructor.


-
[InputTensorInfo](https://docs.openvino.ai/classov_1_1preprocess_1_1_input_tensor_info.html#_CPPv4N2ov10preprocess15InputTensorInfoE)&tensor()[#](https://docs.openvino.ai#_CPPv4N2ov10preprocess9InputInfo6tensorEv) Get current input tensor information with ability to change specific data.

- Returns:
Reference to current input tensor structure



-
[PreProcessSteps](https://docs.openvino.ai/classov_1_1preprocess_1_1_pre_process_steps.html#_CPPv4N2ov10preprocess15PreProcessStepsE)&preprocess()[#](https://docs.openvino.ai#_CPPv4N2ov10preprocess9InputInfo10preprocessEv) Get current input preprocess information with ability to add more preprocessing steps.

- Returns:
Reference to current preprocess steps structure



-
[InputModelInfo](https://docs.openvino.ai/classov_1_1preprocess_1_1_input_model_info.html#_CPPv4N2ov10preprocess14InputModelInfoE)&model()[#](https://docs.openvino.ai#_CPPv4N2ov10preprocess9InputInfo5modelEv) Get current input model information with ability to change original model’s input data.

- Returns:
Reference to current model’s input information structure