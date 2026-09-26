source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1_infer_request.html
lastmod: 

# Class ov::InferRequest[#](https://docs.openvino.ai#class-ov-inferrequest)

-
class InferRequest
[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequestE) This is a class of infer request that can be run in asynchronous or synchronous manners.

Public Functions

-
InferRequest() = default
[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequest12InferRequestEv) Default constructor.


-
InferRequest(const
[InferRequest](https://docs.openvino.ai#_CPPv4N2ov12InferRequest12InferRequestERK12InferRequest)&other) = default[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequest12InferRequestERK12InferRequest) Default copy constructor.

- Parameters:
**other**– Another[InferRequest](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_infer_request)object.


-
[InferRequest](https://docs.openvino.ai#_CPPv4N2ov12InferRequestE)&operator=(const[InferRequest](https://docs.openvino.ai#_CPPv4N2ov12InferRequestE)&other) = default[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequestaSERK12InferRequest) Default copy assignment operator.

- Parameters:
**other**– Another[InferRequest](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_infer_request)object.- Returns:
Reference to the current object.



-
InferRequest(
[InferRequest](https://docs.openvino.ai#_CPPv4N2ov12InferRequest12InferRequestERR12InferRequest)&&other) = default[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequest12InferRequestERR12InferRequest) Default move constructor.

- Parameters:
**other**– Another[InferRequest](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_infer_request)object.


-
[InferRequest](https://docs.openvino.ai#_CPPv4N2ov12InferRequestE)&operator=([InferRequest](https://docs.openvino.ai#_CPPv4N2ov12InferRequestE)&&other) = default[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequestaSERR12InferRequest) Default move assignment operator.

- Parameters:
**other**– Another[InferRequest](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_infer_request)object.- Returns:
Reference to the current object.



-
~InferRequest()
[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequestD0Ev) Destructor that preserves unloading order of implementation object and reference to the library.

Note

To preserve destruction order inside the default generated assignment operator,

`_impl`

is stored before`_so`

. Use the destructor to remove implementation object before referencing to the library explicitly.

-
void set_tensor(const std::string &tensor_name, const
[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)&tensor)[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequest10set_tensorERKNSt6stringERK6Tensor) Sets an input/output tensor to infer on.

- Parameters:
**tensor_name**– Name of the input or output tensor.**tensor**– Reference to the tensor. The element_type and shape of the tensor must match the model’s input/output element_type and size.



-
void set_tensor(const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &port, const[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)&tensor)[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequest10set_tensorERKN2ov6OutputIKN2ov4NodeEEERK6Tensor) Sets an input/output tensor to infer.

- Parameters:
**port**– Port of the input or output tensor. Use the following methods to get the ports:**tensor**– Reference to a tensor. The element_type and shape of a tensor must match the model’s input/output element_type and size.



-
void set_tensor(const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &port, const[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)&tensor)[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequest10set_tensorERKN2ov6OutputIN2ov4NodeEEERK6Tensor) Sets an input/output tensor to infer.

- Parameters:
**port**– Port of the input or output tensor. Use the following methods to get the ports:**tensor**– Reference to a tensor. The element_type and shape of a tensor must match the model’s input/output element_type and size.



-
void set_tensors(const std::string &tensor_name, const std::vector<
[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)> &tensors)[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequest11set_tensorsERKNSt6stringERKNSt6vectorI6TensorEE) Sets a batch of tensors for input data to infer by tensor name.

[Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)input must have batch dimension, and the number of`tensors`

must match the batch size. The current version supports setting tensors to model inputs only. If`tensor_name`

is associated with output (or any other non-input node), an exception is thrown.- Parameters:
**tensor_name**– Name of the input tensor.**tensors**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)tensors for batched infer request. The type of each tensor must match the model input element type and shape (except batch dimension). Total size of tensors must match the input size.



-
void set_tensors(const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &port, const std::vector<[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)> &tensors)[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequest11set_tensorsERKN2ov6OutputIKN2ov4NodeEEERKNSt6vectorI6TensorEE) Sets a batch of tensors for input data to infer by input port.

[Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)input must have batch dimension, and the number of`tensors`

must match the batch size. The current version supports setting tensors to model inputs only. If`port`

is associated with output (or any other non-input node), an exception is thrown.- Parameters:
**port**– Port of the input tensor.**tensors**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)tensors for batched infer request. The type of each tensor must match the model input element type and shape (except batch dimension). Total size of tensors must match the input size.



-
void set_input_tensor(size_t idx, const
[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)&tensor)[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequest16set_input_tensorE6size_tRK6Tensor) Sets an input tensor to infer.

- Parameters:
**idx**– Index of the input tensor. If`idx`

is greater than the number of model inputs, an exception is thrown.**tensor**– Reference to the tensor. The element_type and shape of the tensor must match the model’s input/output element_type and size.



-
void set_input_tensor(const
[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)&tensor)[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequest16set_input_tensorERK6Tensor) Sets an input tensor to infer models with single input.

Note

If model has several inputs, an exception is thrown.

- Parameters:
**tensor**– Reference to the input tensor.


-
void set_input_tensors(const std::vector<
[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)> &tensors)[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequest17set_input_tensorsERKNSt6vectorI6TensorEE) Sets a batch of tensors for single input data.

[Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)input must have batch dimension, and the number of`tensors`

must match the batch size.- Parameters:
**tensors**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)tensors for batched infer request. The type of each tensor must match the model input element type and shape (except batch dimension). Total size of tensors must match the input size.


-
void set_input_tensors(size_t idx, const std::vector<
[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)> &tensors)[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequest17set_input_tensorsE6size_tRKNSt6vectorI6TensorEE) Sets a batch of tensors for input data to infer by input name.

[Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)input must have batch dimension, and number of`tensors`

must match the batch size.- Parameters:
**idx**– Name of the input tensor.**tensors**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)tensors for batched infer request. The type of each tensor must match the model input element type and shape (except batch dimension). Total size of tensors must match the input size.



-
void set_output_tensor(size_t idx, const
[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)&tensor)[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequest17set_output_tensorE6size_tRK6Tensor) Sets an output tensor to infer.

Note

Index of the input preserved accross

[ov::Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model),[ov::CompiledModel](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_compiled_model), and[ov::InferRequest](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_infer_request).- Parameters:
**idx**– Index of the output tensor.**tensor**– Reference to the output tensor. The type of the tensor must match the model output element type and shape.



-
void set_output_tensor(const
[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)&tensor)[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequest17set_output_tensorERK6Tensor) Sets an output tensor to infer models with single output.

Note

If model has several outputs, an exception is thrown.

- Parameters:
**tensor**– Reference to the output tensor.


-
[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)get_tensor(const std::string &tensor_name)[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequest10get_tensorERKNSt6stringE) Gets an input/output tensor for inference by tensor name.

- Parameters:
**tensor_name**– Name of a tensor to get.- Returns:
The tensor with name

`tensor_name`

. If the tensor is not found, an exception is thrown.


-
[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)get_tensor(const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &port)[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequest10get_tensorERKN2ov6OutputIKN2ov4NodeEEE) Gets an input/output tensor for inference.

Note

If the tensor with the specified

`port`

is not found, an exception is thrown.- Parameters:
**port**– Port of the tensor to get.- Returns:
[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)for the port`port`

.


-
[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)get_tensor(const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &port)[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequest10get_tensorERKN2ov6OutputIN2ov4NodeEEE) Gets an input/output tensor for inference.

Note

If the tensor with the specified

`port`

is not found, an exception is thrown.- Parameters:
**port**– Port of the tensor to get.- Returns:
[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)for the port`port`

.


-
[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)get_input_tensor(size_t idx)[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequest16get_input_tensorE6size_t) Gets an input tensor for inference.

- Parameters:
**idx**– Index of the tensor to get.- Returns:
[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)with the input index`idx`

. If the tensor with the specified`idx`

is not found, an exception is thrown.


-
[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)get_input_tensor()[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequest16get_input_tensorEv) Gets an input tensor for inference.

- Returns:
The input tensor for the model. If model has several inputs, an exception is thrown.



-
[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)get_output_tensor(size_t idx)[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequest17get_output_tensorE6size_t) Gets an output tensor for inference.

- Parameters:
**idx**– Index of the tensor to get.- Returns:
[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)with the output index`idx`

. If the tensor with the specified`idx`

is not found, an exception is thrown.


-
[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)get_output_tensor()[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequest17get_output_tensorEv) Gets an output tensor for inference.

- Returns:
[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)tensor for the model. If model has several outputs, an exception is thrown.


-
void infer()
[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequest5inferEv) Infers specified input(s) in synchronous mode.

Note

It blocks all methods of

[InferRequest](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_infer_request)while request is ongoing (running or waiting in a queue). Calling any method leads to throwing the[ov::Busy](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_busy)exception.

-
void cancel()
[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequest6cancelEv) Cancels inference request.


-
std::vector<
[ProfilingInfo](https://docs.openvino.ai/structov_1_1_profiling_info.html#_CPPv4N2ov13ProfilingInfoE)> get_profiling_info() const[#](https://docs.openvino.ai#_CPPv4NK2ov12InferRequest18get_profiling_infoEv) Queries performance measures per layer to identify the most time consuming operation.

Note

Not all plugins provide meaningful data.

- Returns:
Vector of profiling information for operations in a model.



-
void start_async()
[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequest11start_asyncEv) Starts inference of specified input(s) in asynchronous mode.

Note

It returns immediately. Inference starts also immediately. Calling any method while the request in a running state leads to throwing the

[ov::Busy](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_busy)exception.

-
void wait()
[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequest4waitEv) Waits for the result to become available. Blocks until the result becomes available.


-
bool wait_for(const std::chrono::milliseconds timeout)
[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequest8wait_forEKNSt6chrono12millisecondsE) Waits for the result to become available. Blocks until the specified timeout has elapsed or the result becomes available, whichever comes first.

- Parameters:
**timeout**– Maximum duration, in milliseconds, to block for.- Returns:
True if inference request is ready and false, otherwise.



-
void set_callback(std::function<void(std::exception_ptr)> callback)
[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequest12set_callbackENSt8functionIFvNSt13exception_ptrEEEE) Sets a callback std::function that is called on success or failure of an asynchronous request.

Warning

Do not capture strong references to OpenVINO runtime objects into callback. Following objects should not be captured like:

ov::ExecutableNetwork

[ov::Core](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core)As specified objects implement shared reference concept do not capture this objects by value. It can lead to memory leaks or undefined behaviour! Try to use weak references or pointers.

- Parameters:
**callback**– callback object which will be called on when inference finish.


-
std::vector<
[VariableState](https://docs.openvino.ai/classov_1_1_variable_state.html#_CPPv4N2ov13VariableStateE)> query_state()[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequest11query_stateEv) Gets state control interface for the given infer request.

State control essential for recurrent models.

- Returns:
Vector of Variable State objects.



-
void reset_state()
[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequest11reset_stateEv) Resets all internal variable states for relevant infer request to a value specified as default for the corresponding

`ReadValue`

node.

-
[CompiledModel](https://docs.openvino.ai/classov_1_1_compiled_model.html#_CPPv4N2ov13CompiledModelE)get_compiled_model()[#](https://docs.openvino.ai#_CPPv4N2ov12InferRequest18get_compiled_modelEv) Returns a compiled model that creates this inference request.

- Returns:
Compiled model object.



-
bool operator!() const noexcept
[#](https://docs.openvino.ai#_CPPv4NK2ov12InferRequestntEv) Checks if the current

[InferRequest](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_infer_request)object is not initialized.- Returns:
True if the current

[InferRequest](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_infer_request)object is not initialized; false, otherwise.


-
explicit operator bool() const noexcept
[#](https://docs.openvino.ai#_CPPv4NK2ov12InferRequestcvbEv) Checks if the current

[InferRequest](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_infer_request)object is initialized.- Returns:
True if the current

[InferRequest](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_infer_request)object is initialized; false, otherwise.


-
bool operator!=(const
[InferRequest](https://docs.openvino.ai#_CPPv4N2ov12InferRequestE)&other) const noexcept[#](https://docs.openvino.ai#_CPPv4NK2ov12InferRequestneERK12InferRequest) Compares whether this request wraps the same impl underneath.

- Parameters:
**other**– Another inference request.- Returns:
True if the current

[InferRequest](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_infer_request)object does not wrap the same impl as the operator’s arg.


-
bool operator==(const
[InferRequest](https://docs.openvino.ai#_CPPv4N2ov12InferRequestE)&other) const noexcept[#](https://docs.openvino.ai#_CPPv4NK2ov12InferRequesteqERK12InferRequest) Compares whether this request wraps the same impl underneath.

- Parameters:
**other**– Another inference request.- Returns:
True if the current

[InferRequest](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_infer_request)object wraps the same impl as the operator’s arg.


-
InferRequest() = default