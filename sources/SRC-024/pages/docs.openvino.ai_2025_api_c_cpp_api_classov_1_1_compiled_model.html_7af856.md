source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1_compiled_model.html
lastmod: 

# Class ov::CompiledModel[#](https://docs.openvino.ai#class-ov-compiledmodel)

-
class CompiledModel
[#](https://docs.openvino.ai#_CPPv4N2ov13CompiledModelE) This class represents a compiled model.

A model is compiled by a specific device by applying multiple optimization transformations, then mapping to compute kernels.

Public Functions

-
CompiledModel() = default
[#](https://docs.openvino.ai#_CPPv4N2ov13CompiledModel13CompiledModelEv) Default constructor.


-
~CompiledModel()
[#](https://docs.openvino.ai#_CPPv4N2ov13CompiledModelD0Ev) Destructor that preserves unloading order of an implementation object and reference to library.


-
std::shared_ptr<const
[Model](https://docs.openvino.ai/classov_1_1_model.html#_CPPv4N2ov5ModelE)> get_runtime_model() const[#](https://docs.openvino.ai#_CPPv4NK2ov13CompiledModel17get_runtime_modelEv) Gets runtime model information from a device. This object represents an internal device-specific model that is optimized for a particular accelerator. It contains device-specific nodes, runtime information and can be used only to understand how the source model is optimized and which kernels, element types, and layouts are selected for optimal inference.

- Returns:
A model containing Executable Graph Info.



-
const std::vector<
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)>> &inputs() const[#](https://docs.openvino.ai#_CPPv4NK2ov13CompiledModel6inputsEv) Gets all inputs of a compiled model. Inputs are represented as a vector of outputs of the

[ov::op::v0::Parameter](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_parameter)operations. They contain information about input tensors such as tensor shape, names, and element type.- Returns:
std::vector of model inputs.



-
const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &input() const[#](https://docs.openvino.ai#_CPPv4NK2ov13CompiledModel5inputEv) Gets a single input of a compiled model. The input is represented as an output of the

[ov::op::v0::Parameter](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_parameter)operation. The input contains information about input tensor such as tensor shape, names, and element type.Note

If a model has more than one input, this method throws

[ov::Exception](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_exception).- Returns:
Compiled model input.



-
const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &input(size_t i) const[#](https://docs.openvino.ai#_CPPv4NK2ov13CompiledModel5inputE6size_t) Gets input of a compiled model identified by

`i`

. The input contains information about input tensor such as tensor shape, names, and element type.Note

The method throws

[ov::Exception](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_exception)if input with the specified index`i`

is not found.- Parameters:
**i**– Index of input.- Returns:
Compiled model input.



-
const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &input(const std::string &tensor_name) const[#](https://docs.openvino.ai#_CPPv4NK2ov13CompiledModel5inputERKNSt6stringE) Gets input of a compiled model identified by

`tensor_name`

. The input contains information about input tensor such as tensor shape, names, and element type.Note

The method throws

[ov::Exception](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_exception)if input with the specified tensor name`tensor_name`

is not found.- Parameters:
**tensor_name**– The input tensor name.- Returns:
Compiled model input.



-
const std::vector<
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)>> &outputs() const[#](https://docs.openvino.ai#_CPPv4NK2ov13CompiledModel7outputsEv) Get all outputs of a compiled model. Outputs are represented as a vector of output from the

[ov::op::v0::Result](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_result)operations. Outputs contain information about output tensors such as tensor shape, names, and element type.- Returns:
std::vector of model outputs.



-
const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &output() const[#](https://docs.openvino.ai#_CPPv4NK2ov13CompiledModel6outputEv) Gets a single output of a compiled model. The output is represented as an output from the

[ov::op::v0::Result](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_result)operation. The output contains information about output tensor such as tensor shape, names, and element type.Note

If a model has more than one output, this method throws

[ov::Exception](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_exception).- Returns:
Compiled model output.



-
const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &output(size_t i) const[#](https://docs.openvino.ai#_CPPv4NK2ov13CompiledModel6outputE6size_t) Gets output of a compiled model identified by

`index`

. The output contains information about output tensor such as tensor shape, names, and element type.Note

The method throws

[ov::Exception](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_exception)if output with the specified index`index`

is not found.- Parameters:
**i**– Index of input.- Returns:
Compiled model output.



-
const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &output(const std::string &tensor_name) const[#](https://docs.openvino.ai#_CPPv4NK2ov13CompiledModel6outputERKNSt6stringE) Gets output of a compiled model identified by

`tensor_name`

. The output contains information about output tensor such as tensor shape, names, and element type.Note

The method throws

[ov::Exception](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_exception)if output with the specified tensor name`tensor_name`

is not found.- Parameters:
**tensor_name**–[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)tensor name.- Returns:
Compiled model output.



-
[InferRequest](https://docs.openvino.ai/classov_1_1_infer_request.html#_CPPv4N2ov12InferRequestE)create_infer_request()[#](https://docs.openvino.ai#_CPPv4N2ov13CompiledModel20create_infer_requestEv) Creates an inference request object used to infer the compiled model. The created request has allocated input and output tensors (which can be changed later).

- Returns:
[InferRequest](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_infer_request)object


-
void export_model(std::ostream &model_stream)
[#](https://docs.openvino.ai#_CPPv4N2ov13CompiledModel12export_modelERNSt7ostreamE) Exports the current compiled model to an output stream

`std::ostream`

. The exported model can also be imported via the[ov::Core::import_model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core_1a0d2853511bd7ba60cb591f4685b91884)method.See also

- Parameters:
**model_stream**–[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)stream to store the model to.


-
void set_property(const AnyMap &properties)
[#](https://docs.openvino.ai#_CPPv4N2ov13CompiledModel12set_propertyERK6AnyMap) Sets properties for the current compiled model.

- Parameters:
**properties**– Map of pairs: (property name, property value).


-
template<typename ...Properties>

inline[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4utilE)::EnableIfAllStringAny<void,[Properties](https://docs.openvino.ai#_CPPv4IDpEN2ov13CompiledModel12set_propertyEN4util20EnableIfAllStringAnyIvDp10PropertiesEEDpRR10Properties)...> set_property([Properties](https://docs.openvino.ai#_CPPv4IDpEN2ov13CompiledModel12set_propertyEN4util20EnableIfAllStringAnyIvDp10PropertiesEEDpRR10Properties)&&... properties)[#](https://docs.openvino.ai#_CPPv4IDpEN2ov13CompiledModel12set_propertyEN4util20EnableIfAllStringAnyIvDp10PropertiesEEDpRR10Properties) Sets properties for the current compiled model.

- Template Parameters:
**Properties**– Should be the pack of`std::pair<std::string,`

types.[ov::Any](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_any)>- Parameters:
**properties**– Optional pack of pairs: (property name, property value).


-
[Any](https://docs.openvino.ai/classov_1_1_any.html#_CPPv4N2ov3AnyE)get_property(const std::string &name) const[#](https://docs.openvino.ai#_CPPv4NK2ov13CompiledModel12get_propertyERKNSt6stringE) Gets properties for current compiled model.

The method is responsible for extracting information that affects compiled model inference. The list of supported configuration values can be extracted via

[CompiledModel::get_property](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_compiled_model_1a109d701ffe8b5de096961c7c98ff0bed)with the[ov::supported_properties](https://docs.openvino.ai/group__ov__runtime__cpp__prop__api.html#group__ov__runtime__cpp__prop__api_1ga097f1274f26f3f4e1aa4fc3928748592)key, but some of these keys cannot be changed dynamically, for example,[ov::device::id](https://docs.openvino.ai/group__ov__transformation__common__api.html#group__ov__runtime__cpp__prop__api_1ga433b8ea52e99c2b1fa8b26453485d75d)cannot be changed if a compiled model has already been compiled for a particular device.

-
template<typename T, PropertyMutability mutability>

inline[T](https://docs.openvino.ai#_CPPv4I0_18PropertyMutabilityENK2ov13CompiledModel12get_propertyE1TRKN2ov8PropertyI1T10mutabilityEE)get_property(const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Property](https://docs.openvino.ai/classov_1_1_property.html#_CPPv4I0_18PropertyMutabilityEN2ov8PropertyE)<[T](https://docs.openvino.ai#_CPPv4I0_18PropertyMutabilityENK2ov13CompiledModel12get_propertyE1TRKN2ov8PropertyI1T10mutabilityEE),[mutability](https://docs.openvino.ai#_CPPv4I0_18PropertyMutabilityENK2ov13CompiledModel12get_propertyE1TRKN2ov8PropertyI1T10mutabilityEE)> &property) const[#](https://docs.openvino.ai#_CPPv4I0_18PropertyMutabilityENK2ov13CompiledModel12get_propertyE1TRKN2ov8PropertyI1T10mutabilityEE) Gets properties related to device behaviour.

The method extracts information that can be set via the set_property method.

- Template Parameters:
**T**– Type of a returned value.- Parameters:
**property**–[Property](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_property)object.- Returns:
Value of property.



-
void release_memory()
[#](https://docs.openvino.ai#_CPPv4N2ov13CompiledModel14release_memoryEv) Release intermediate memory.

This method forces the Compiled model to release memory allocated for intermediate structures, e.g. caches, tensors, temporal buffers etc., when possible


-
[RemoteContext](https://docs.openvino.ai/classov_1_1_remote_context.html#_CPPv4N2ov13RemoteContextE)get_context() const[#](https://docs.openvino.ai#_CPPv4NK2ov13CompiledModel11get_contextEv) Returns pointer to device-specific shared context on a remote accelerator device that was used to create this

[CompiledModel](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_compiled_model).- Returns:
A context.



-
bool operator!() const noexcept
[#](https://docs.openvino.ai#_CPPv4NK2ov13CompiledModelntEv) Checks if the current

[CompiledModel](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_compiled_model)object is not initialized.- Returns:
`true`

if the current[CompiledModel](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_compiled_model)object is not initialized;`false`

, otherwise.


-
explicit operator bool() const noexcept
[#](https://docs.openvino.ai#_CPPv4NK2ov13CompiledModelcvbEv) Checks if the current

[CompiledModel](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_compiled_model)object is initialized.- Returns:
`true`

if the current[CompiledModel](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_compiled_model)object is initialized;`false`

, otherwise.


-
CompiledModel() = default