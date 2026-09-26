source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1preprocess_1_1_post_process_steps.html
lastmod: 

# Class ov::preprocess::PostProcessSteps[#](https://docs.openvino.ai#class-ov-preprocess-postprocesssteps)

-
class PostProcessSteps
[#](https://docs.openvino.ai#_CPPv4N2ov10preprocess16PostProcessStepsE) Postprocessing steps. Each step typically intends adding of some operation to output parameter User application can specify sequence of postprocessing steps in a builder-like manner.

auto proc = PrePostProcessor(function); proc.output().postprocess().convert_element_type(element::u8); function = proc.build();

Public Types

-
using CustomPostprocessOp = std::function<
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)>(const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &node)>[#](https://docs.openvino.ai#_CPPv4N2ov10preprocess16PostProcessSteps19CustomPostprocessOpE) Signature for custom postprocessing operation. Custom postprocessing operation takes one output node and produces one output node. For more advanced cases, client’s code can use transformation passes over

[ov::Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)directly.- Param node:
[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)node for custom post-processing operation- Return:
New node after applying custom post-processing operation



Public Functions

-
~PostProcessSteps()
[#](https://docs.openvino.ai#_CPPv4N2ov10preprocess16PostProcessStepsD0Ev) Default destructor.


-
[PostProcessSteps](https://docs.openvino.ai#_CPPv4N2ov10preprocess16PostProcessStepsE)&clamp(double min_value, double max_value)[#](https://docs.openvino.ai#_CPPv4N2ov10preprocess16PostProcessSteps5clampEdd) Add clamp postprocess operation. Clamp each element of input to the specified range [min_value,max_value].

- Parameters:
**min_value**– Minimum value to clamp to.**max_value**– Maximum value to clamp to.

- Returns:
Reference to ‘this’ to allow chaining with other calls in a builder-like manner



-
[PostProcessSteps](https://docs.openvino.ai#_CPPv4N2ov10preprocess16PostProcessStepsE)&convert_element_type(const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&type = {})[#](https://docs.openvino.ai#_CPPv4N2ov10preprocess16PostProcessSteps20convert_element_typeERKN2ov7element4TypeE) Add convert element type post-process operation.

- Parameters:
**type**– Desired type of output. If not specified, type will be obtained from ‘tensor’ output information- Returns:
Reference to ‘this’ to allow chaining with other calls in a builder-like manner



-
[PostProcessSteps](https://docs.openvino.ai#_CPPv4N2ov10preprocess16PostProcessStepsE)&convert_layout(const[Layout](https://docs.openvino.ai/classov_1_1_layout.html#_CPPv4N2ov6LayoutE)&dst_layout = {})[#](https://docs.openvino.ai#_CPPv4N2ov10preprocess16PostProcessSteps14convert_layoutERK6Layout) Add ‘convert layout’ operation to specified layout.

Adds appropriate ‘transpose’ operation between model layout and user’s desired layout. Current implementation requires source and destination layout to have same number of dimensions

Example: when model data has output in ‘NCHW’ layout ([1, 3, 224, 224]) but user needs interleaved output image (‘NHWC’, [1, 224, 224, 3]). Post-processing may look like this:

auto proc = PrePostProcessor(function); proc.output().model(OutputTensorInfo().set_layout("NCHW"); // model output is NCHW proc.output().postprocess().convert_layout("NHWC"); // User needs output as NHWC

- Parameters:
**dst_layout**– New layout after conversion. If not specified - destination layout is obtained from appropriate tensor output properties.- Returns:
Reference to ‘this’ to allow chaining with other calls in a builder-like manner.



-
[PostProcessSteps](https://docs.openvino.ai#_CPPv4N2ov10preprocess16PostProcessStepsE)&convert_layout(const std::vector<uint64_t> &dims)[#](https://docs.openvino.ai#_CPPv4N2ov10preprocess16PostProcessSteps14convert_layoutERKNSt6vectorI8uint64_tEE) Add convert layout operation by direct specification of transposed dimensions.

Example: model produces output with shape [1, 3, 480, 640] and user’s needs interleaved output image [1, 480, 640, 3]. Post-processing may look like this:

auto proc = PrePostProcessor(function); proc.output().postprocess().convert_layout({0, 2, 3, 1}); function = proc.build();

- Parameters:
**dims**– Dimensions array specifying places for new axis. If not empty, array size (N) must match to input shape rank. Array values shall contain all values from 0 to N-1. If empty, no actual conversion will be added.- Returns:
Reference to ‘this’ to allow chaining with other calls in a builder-like manner.



-
[PostProcessSteps](https://docs.openvino.ai#_CPPv4N2ov10preprocess16PostProcessStepsE)&custom(const[CustomPostprocessOp](https://docs.openvino.ai#_CPPv4N2ov10preprocess16PostProcessSteps19CustomPostprocessOpE)&postprocess_cb)[#](https://docs.openvino.ai#_CPPv4N2ov10preprocess16PostProcessSteps6customERK19CustomPostprocessOp) Add custom post-process operation. Client application can specify callback function for custom action.

- Parameters:
**postprocess_cb**– Client’s custom postprocess operation.- Returns:
Reference to ‘this’ to allow chaining with other calls in a builder-like manner



-
[PostProcessSteps](https://docs.openvino.ai#_CPPv4N2ov10preprocess16PostProcessStepsE)&convert_color(const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[preprocess](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov10preprocessE)::[ColorFormat](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov10preprocess11ColorFormatE)&dst_format)[#](https://docs.openvino.ai#_CPPv4N2ov10preprocess16PostProcessSteps13convert_colorERKN2ov10preprocess11ColorFormatE) Converts color format for user’s output tensor. Requires destinantion color format to be specified by OutputTensorInfo::set_color_format.

- Parameters:
**dst_format**– Destination color format of input image- Returns:
Reference to ‘this’ to allow chaining with other calls in a builder-like manner



-
using CustomPostprocessOp = std::function<