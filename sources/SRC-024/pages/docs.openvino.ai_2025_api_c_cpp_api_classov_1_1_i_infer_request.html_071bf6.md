source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1_i_infer_request.html
lastmod: 

# Class ov::IInferRequest[#](https://docs.openvino.ai#class-ov-iinferrequest)

-
class IInferRequest
[#](https://docs.openvino.ai#_CPPv4N2ov13IInferRequestE) An internal API of inference request to be implemented by plugin.

Subclassed by

[ov::IAsyncInferRequest](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_i_async_infer_request),[ov::ISyncInferRequest](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_i_sync_infer_request)Public Functions

-
virtual void infer() = 0
[#](https://docs.openvino.ai#_CPPv4N2ov13IInferRequest5inferEv) Infers specified input(s) in synchronous mode.

Note

blocks all method of

[InferRequest](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_infer_request)while request is ongoing (running or waiting in queue)

-
virtual std::vector<
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[ProfilingInfo](https://docs.openvino.ai/structov_1_1_profiling_info.html#_CPPv4N2ov13ProfilingInfoE)> get_profiling_info() const = 0[#](https://docs.openvino.ai#_CPPv4NK2ov13IInferRequest18get_profiling_infoEv) Queries performance measures per layer to identify the most time consuming operation.

Note

Not all plugins provide meaningful data.

- Returns:
Vector of profiling information for operations in a model.



-
virtual
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[SoPtr](https://docs.openvino.ai/structov_1_1_so_ptr.html#_CPPv4I0EN2ov5SoPtrE)<[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::ITensor> get_tensor(const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &port) const = 0[#](https://docs.openvino.ai#_CPPv4NK2ov13IInferRequest10get_tensorERKN2ov6OutputIKN2ov4NodeEEE) Gets an input/output tensor for inference.

Note

If the tensor with the specified

`port`

is not found, an exception is thrown.- Parameters:
**port**– Port of the tensor to get.- Returns:
[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)for the port`port`

.


-
virtual void set_tensor(const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &port, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[SoPtr](https://docs.openvino.ai/structov_1_1_so_ptr.html#_CPPv4I0EN2ov5SoPtrE)<[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::ITensor> &tensor) = 0[#](https://docs.openvino.ai#_CPPv4N2ov13IInferRequest10set_tensorERKN2ov6OutputIKN2ov4NodeEEERKN2ov5SoPtrIN2ov7ITensorEEE) Sets an input/output tensor to infer.

- Parameters:
**port**– Port of the input or output tensor.**tensor**– Reference to a tensor. The element_type and shape of a tensor must match the model’s input/output element_type and size.



-
virtual std::vector<
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[SoPtr](https://docs.openvino.ai/structov_1_1_so_ptr.html#_CPPv4I0EN2ov5SoPtrE)<[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::ITensor>> get_tensors(const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &port) const = 0[#](https://docs.openvino.ai#_CPPv4NK2ov13IInferRequest11get_tensorsERKN2ov6OutputIKN2ov4NodeEEE) Gets a batch of tensors for input data to infer by input port.

[Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)input must have batch dimension, and the number of`tensors`

must match the batch size. The current version supports setting tensors to model inputs only. If`port`

is associated with output (or any other non-input node), an exception is thrown.- Parameters:
**port**– Port of the input tensor.**tensors**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)tensors for batched infer request. The type of each tensor must match the model input element type and shape (except batch dimension). Total size of tensors must match the input size.

- Returns:
vector of tensors



-
virtual void set_tensors(const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &port, const std::vector<[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[SoPtr](https://docs.openvino.ai/structov_1_1_so_ptr.html#_CPPv4I0EN2ov5SoPtrE)<[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::ITensor>> &tensors) = 0[#](https://docs.openvino.ai#_CPPv4N2ov13IInferRequest11set_tensorsERKN2ov6OutputIKN2ov4NodeEEERKNSt6vectorIN2ov5SoPtrIN2ov7ITensorEEEEE) Sets a batch of tensors for input data to infer by input port.

[Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)input must have batch dimension, and the number of`tensors`

must match the batch size. The current version supports setting tensors to model inputs only. If`port`

is associated with output (or any other non-input node), an exception is thrown.- Parameters:
**port**– Port of the input tensor.**tensors**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)tensors for batched infer request. The type of each tensor must match the model input element type and shape (except batch dimension). Total size of tensors must match the input size.



-
virtual std::vector<
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[SoPtr](https://docs.openvino.ai/structov_1_1_so_ptr.html#_CPPv4I0EN2ov5SoPtrE)<[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[IVariableState](https://docs.openvino.ai/group__ov__dev__api__variable__state__api.html#_CPPv4N2ov14IVariableStateE)>> query_state() const = 0[#](https://docs.openvino.ai#_CPPv4NK2ov13IInferRequest11query_stateEv) Gets state control interface for the given infer request.

State control essential for recurrent models.

- Returns:
Vector of Variable State objects.



-
virtual const std::shared_ptr<const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[ICompiledModel](https://docs.openvino.ai/classov_1_1_i_compiled_model.html#_CPPv4N2ov14ICompiledModelE)> &get_compiled_model() const = 0[#](https://docs.openvino.ai#_CPPv4NK2ov13IInferRequest18get_compiled_modelEv) Gets pointer to compiled model (usually synchronous request holds the compiled model)

- Returns:
Pointer to the compiled model



-
virtual void infer() = 0