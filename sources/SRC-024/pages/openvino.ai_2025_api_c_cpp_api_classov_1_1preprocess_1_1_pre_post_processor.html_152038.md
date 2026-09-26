source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1preprocess_1_1_pre_post_processor.html
lastmod: 

# Class ov::preprocess::PrePostProcessor[#](https://docs.openvino.ai#class-ov-preprocess-prepostprocessor)

-
class PrePostProcessor
[#](https://docs.openvino.ai#_CPPv4N2ov10preprocess16PrePostProcessorE) Main class for adding pre- and post- processing steps to existing

[ov::Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model).This is a helper class for writing easy pre- and post- processing operations on

[ov::Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)object assuming that any preprocess operation takes one input and produces one output.For advanced preprocessing scenarios, like combining several functions with multiple inputs/outputs into one, client’s code can use transformation passes over

[ov::Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)Public Functions

Default constructor.

- Parameters:
**function**– Existing function representing loaded model


-
PrePostProcessor(
[PrePostProcessor](https://docs.openvino.ai#_CPPv4N2ov10preprocess16PrePostProcessor16PrePostProcessorERR16PrePostProcessor)&&) noexcept[#](https://docs.openvino.ai#_CPPv4N2ov10preprocess16PrePostProcessor16PrePostProcessorERR16PrePostProcessor) Default move constructor.


-
[PrePostProcessor](https://docs.openvino.ai#_CPPv4N2ov10preprocess16PrePostProcessorE)&operator=([PrePostProcessor](https://docs.openvino.ai#_CPPv4N2ov10preprocess16PrePostProcessorE)&&) noexcept[#](https://docs.openvino.ai#_CPPv4N2ov10preprocess16PrePostProcessoraSERR16PrePostProcessor) Default move assignment operator.


-
~PrePostProcessor()
[#](https://docs.openvino.ai#_CPPv4N2ov10preprocess16PrePostProcessorD0Ev) Default destructor.


-
[InputInfo](https://docs.openvino.ai/classov_1_1preprocess_1_1_input_info.html#_CPPv4N2ov10preprocess9InputInfoE)&input()[#](https://docs.openvino.ai#_CPPv4N2ov10preprocess16PrePostProcessor5inputEv) Gets input pre-processing data structure. Should be used only if model/function has only one input Using returned structure application’s code is able to set user’s tensor data (e.g layout), preprocess steps, target model’s data.

- Returns:
Reference to model’s input information structure



-
[InputInfo](https://docs.openvino.ai/classov_1_1preprocess_1_1_input_info.html#_CPPv4N2ov10preprocess9InputInfoE)&input(const std::string &tensor_name)[#](https://docs.openvino.ai#_CPPv4N2ov10preprocess16PrePostProcessor5inputERKNSt6stringE) Gets input pre-processing data structure for input identified by it’s tensor name.

- Parameters:
**tensor_name**–[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)name of specific input. Throws if tensor name is not associated with any input in a model- Returns:
Reference to model’s input information structure



-
[InputInfo](https://docs.openvino.ai/classov_1_1preprocess_1_1_input_info.html#_CPPv4N2ov10preprocess9InputInfoE)&input(size_t input_index)[#](https://docs.openvino.ai#_CPPv4N2ov10preprocess16PrePostProcessor5inputE6size_t) Gets input pre-processing data structure for input identified by it’s order in a model.

- Parameters:
**input_index**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)index of specific input. Throws if input index is out of range for associated function- Returns:
Reference to model’s input information structure



-
[OutputInfo](https://docs.openvino.ai/classov_1_1preprocess_1_1_output_info.html#_CPPv4N2ov10preprocess10OutputInfoE)&output()[#](https://docs.openvino.ai#_CPPv4N2ov10preprocess16PrePostProcessor6outputEv) Gets output post-processing data structure. Should be used only if model/function has only one output Using returned structure application’s code is able to set model’s output data, post-process steps, user’s tensor data (e.g layout)

- Returns:
Reference to model’s output information structure



-
[OutputInfo](https://docs.openvino.ai/classov_1_1preprocess_1_1_output_info.html#_CPPv4N2ov10preprocess10OutputInfoE)&output(const std::string &tensor_name)[#](https://docs.openvino.ai#_CPPv4N2ov10preprocess16PrePostProcessor6outputERKNSt6stringE) Gets output post-processing data structure for output identified by it’s tensor name.

- Parameters:
**tensor_name**–[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)name of specific output. Throws if tensor name is not associated with any input in a model- Returns:
Reference to model’s output information structure



-
[OutputInfo](https://docs.openvino.ai/classov_1_1preprocess_1_1_output_info.html#_CPPv4N2ov10preprocess10OutputInfoE)&output(size_t output_index)[#](https://docs.openvino.ai#_CPPv4N2ov10preprocess16PrePostProcessor6outputE6size_t) Gets output post-processing data structure for output identified by it’s order in a model.

- Parameters:
**output_index**–[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)index of specific output. Throws if output index is out of range for associated function- Returns:
Reference to model’s output information structure