source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1preprocess_1_1_output_tensor_info.html
lastmod: 

# Class ov::preprocess::OutputTensorInfo[#](https://docs.openvino.ai#class-ov-preprocess-outputtensorinfo)

-
class OutputTensorInfo
[#](https://docs.openvino.ai#_CPPv4N2ov10preprocess16OutputTensorInfoE) Information about user’s desired output tensor. By default, it will be initialized to same data (type/shape/etc) as model’s output parameter. User application can override particular parameters (like ‘element_type’) according to application’s data and specify appropriate conversions in post-processing steps.

auto proc = PrePostProcessor(function); auto& output = proc.output(); output.postprocess().<add steps + conversion to user's output element type>; output.tensor().set_element_type(ov::element::u8); function = proc.build();

Public Functions

-
~OutputTensorInfo()
[#](https://docs.openvino.ai#_CPPv4N2ov10preprocess16OutputTensorInfoD0Ev) Default destructor.


-
[OutputTensorInfo](https://docs.openvino.ai#_CPPv4N2ov10preprocess16OutputTensorInfoE)&set_element_type(const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&type)[#](https://docs.openvino.ai#_CPPv4N2ov10preprocess16OutputTensorInfo16set_element_typeERKN2ov7element4TypeE) Set element type for user’s desired output tensor.

- Parameters:
**type**– Element type for user’s output tensor.- Returns:
Reference to ‘this’ to allow chaining with other calls in a builder-like manner.



-
[OutputTensorInfo](https://docs.openvino.ai#_CPPv4N2ov10preprocess16OutputTensorInfoE)&set_layout(const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Layout](https://docs.openvino.ai/classov_1_1_layout.html#_CPPv4N2ov6LayoutE)&layout)[#](https://docs.openvino.ai#_CPPv4N2ov10preprocess16OutputTensorInfo10set_layoutERKN2ov6LayoutE) Set layout for user’s output tensor.

- Parameters:
**layout**–[Layout](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_layout)for user’s output tensor.- Returns:
Reference to ‘this’ to allow chaining with other calls in a builder-like manner



-
~OutputTensorInfo()