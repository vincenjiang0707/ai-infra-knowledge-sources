source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1_i_compiled_model.html
lastmod: 

# Class ov::ICompiledModel[#](https://docs.openvino.ai#class-ov-icompiledmodel)

-
class ICompiledModel : public std::enable_shared_from_this<
[ICompiledModel](https://docs.openvino.ai#_CPPv4N2ov14ICompiledModelE)>[#](https://docs.openvino.ai#_CPPv4N2ov14ICompiledModelE) OpenVINO

[ICompiledModel](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_i_compiled_model)interface.Public Functions

Constructor for

[ICompiledModel](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_i_compiled_model)interface.- Parameters:
**model**– OpenVINO model representation**plugin**– Pointer to plugin**task_executor**– Task executor (CPUStreamsExecutor by default)**callback_executor**– Callback executor (CPUStreamsExecutor by default)



Constructor for

[ICompiledModel](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_i_compiled_model)interface with remote context.- Parameters:
**model**– OpenVINO model representation**plugin**– Pointer to plugin**context**– Remote context**task_executor**– Task executor (CPUStreamsExecutor by default)**callback_executor**– Callback executor (CPUStreamsExecutor by default)



-
virtual const std::vector<
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)>> &outputs() const[#](https://docs.openvino.ai#_CPPv4NK2ov14ICompiledModel7outputsEv) Gets all outputs from compiled model.

- Returns:
model outputs



-
virtual const std::vector<
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)>> &inputs() const[#](https://docs.openvino.ai#_CPPv4NK2ov14ICompiledModel6inputsEv) Gets all inputs from compiled model.

- Returns:
model inputs



-
virtual std::shared_ptr<
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[IAsyncInferRequest](https://docs.openvino.ai/classov_1_1_i_async_infer_request.html#_CPPv4N2ov18IAsyncInferRequestE)> create_infer_request() const[#](https://docs.openvino.ai#_CPPv4NK2ov14ICompiledModel20create_infer_requestEv) Create infer request.

- Returns:
Asynchronous infer request interface



-
virtual void export_model(std::ostream &model) const = 0
[#](https://docs.openvino.ai#_CPPv4NK2ov14ICompiledModel12export_modelERNSt7ostreamE) Export compiled model to stream.

- Parameters:
**model**– output stream


-
virtual std::shared_ptr<const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Model](https://docs.openvino.ai/classov_1_1_model.html#_CPPv4N2ov5ModelE)> get_runtime_model() const = 0[#](https://docs.openvino.ai#_CPPv4NK2ov14ICompiledModel17get_runtime_modelEv) Returns runtime model.

- Returns:
OpenVINO

[Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)which represents runtime graph


-
virtual void set_property(const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::AnyMap &properties) = 0[#](https://docs.openvino.ai#_CPPv4N2ov14ICompiledModel12set_propertyERKN2ov6AnyMapE) Allows to set property.

- Parameters:
**properties**– new plugin properties


-
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[SoPtr](https://docs.openvino.ai/structov_1_1_so_ptr.html#_CPPv4I0EN2ov5SoPtrE)<[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[IRemoteContext](https://docs.openvino.ai/classov_1_1_i_remote_context.html#_CPPv4N2ov14IRemoteContextE)> get_context() const[#](https://docs.openvino.ai#_CPPv4NK2ov14ICompiledModel11get_contextEv) Creates device specific remote context.

- Returns:
OpenVINO

[RemoteContext](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_remote_context)


-
virtual void release_memory()
[#](https://docs.openvino.ai#_CPPv4N2ov14ICompiledModel14release_memoryEv) Release intermediate memory.