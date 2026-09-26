source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1preprocess_1_1_input_model_info.html
lastmod: 

# Class ov::preprocess::InputModelInfo[#](https://docs.openvino.ai#class-ov-preprocess-inputmodelinfo)

-
class InputModelInfo
[#](https://docs.openvino.ai#_CPPv4N2ov10preprocess14InputModelInfoE) Information about model’s input tensor. If all information is already included to loaded model, this info may not be needed. However it can be set to specify additional information about model, like ‘layout’.

Example of usage of model ‘layout’: Support model has input parameter with shape {1, 3, 224, 224} and user needs to resize input image to model’s dimensions. It can be done like this

<model has input parameter with shape {1, 3, 224, 224}> auto proc = PrePostProcessor(function); proc.input().preprocess().resize(ResizeAlgorithm::RESIZE_LINEAR); proc.input().model().set_layout("NCHW");

Public Functions

-
~InputModelInfo()
[#](https://docs.openvino.ai#_CPPv4N2ov10preprocess14InputModelInfoD0Ev) Default destructor.


-
[InputModelInfo](https://docs.openvino.ai#_CPPv4N2ov10preprocess14InputModelInfoE)&set_layout(const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Layout](https://docs.openvino.ai/classov_1_1_layout.html#_CPPv4N2ov6LayoutE)&layout)[#](https://docs.openvino.ai#_CPPv4N2ov10preprocess14InputModelInfo10set_layoutERKN2ov6LayoutE) Set layout for model’s input tensor This version allows chaining for Lvalue objects.

- Parameters:
**layout**–[Layout](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_layout)for model’s input tensor.- Returns:
Reference to ‘this’ to allow chaining with other calls in a builder-like manner



-
~InputModelInfo()