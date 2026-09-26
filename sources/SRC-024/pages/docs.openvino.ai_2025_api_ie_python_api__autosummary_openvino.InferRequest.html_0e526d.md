source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.InferRequest.html
lastmod: 

# openvino.InferRequest[#](https://docs.openvino.ai#openvino-inferrequest)

-
*class*openvino.InferRequest(*other: InferRequest*)[#](https://docs.openvino.ai#openvino.InferRequest) Bases:

`_InferRequestWrapper`

InferRequest class represents infer request which can be run in asynchronous or synchronous manners.

-
__init__(
*self: openvino._pyopenvino.InferRequest*,*other: openvino._pyopenvino.InferRequest*) None[#](https://docs.openvino.ai#openvino.InferRequest.__init__)

Methods

(name, /)`__delattr__`

Implement delattr(self, name).

()`__dir__`

Default dir() implementation.

(value, /)`__eq__`

Return self==value.

(format_spec, /)`__format__`

Default object formatter.

(value, /)`__ge__`

Return self>=value.

(name, /)`__getattribute__`

Return getattr(self, name).

Helper for pickle.

(value, /)`__gt__`

Return self>value.

()`__hash__`

Return hash(self).

(self, other)`__init__`

This method is called when a class is subclassed.

(value, /)`__le__`

Return self<=value.

(value, /)`__lt__`

Return self<value.

(value, /)`__ne__`

Return self!=value.

(**kwargs)`__new__`

Helper for pickle.

(protocol, /)`__reduce_ex__`

Helper for pickle.

(self)`__repr__`

(name, value, /)`__setattr__`

Implement setattr(self, name, value).

Size of object in memory, in bytes.

()`__str__`

Return str(self).

Abstract classes can override this to customize issubclass().

(self)`cancel`

Cancels inference request.

Gets the compiled model this InferRequest is using.

(*args, **kwargs)`get_input_tensor`

Overloaded function.

(*args, **kwargs)`get_output_tensor`

Overloaded function.

(self)`get_profiling_info`

Queries performance is measured per layer to get feedback on what is the most time-consuming operation, not all plugins provide meaningful data.

(*args, **kwargs)`get_tensor`

Overloaded function.

([inputs, share_inputs, share_outputs, ...])`infer`

Infers specified input(s) in synchronous mode.

(self)`query_state`

Gets state control interface for given infer request.

(self)`reset_state`

Resets all internal variable states for relevant infer request to a value specified as default for the corresponding ReadValue node

(self, callback, userdata)`set_callback`

Sets a callback function that will be called on success or failure of asynchronous InferRequest.

(*args, **kwargs)`set_input_tensor`

Overloaded function.

(*args, **kwargs)`set_input_tensors`

Overloaded function.

(*args, **kwargs)`set_output_tensor`

Overloaded function.

(self, outputs)`set_output_tensors`

Set output tensors using given indexes.

(*args, **kwargs)`set_tensor`

Overloaded function.

(*args, **kwargs)`set_tensors`

Overloaded function.

([inputs, userdata, share_inputs])`start_async`

Starts inference of specified input(s) in asynchronous mode.

(self)`wait`

Waits for the result to become available.

(self, timeout)`wait_for`

Waits for the result to become available.

Attributes

Gets all input tensors of this InferRequest.

Gets latency of this InferRequest.

Gets all inputs of a compiled model which was used to create this InferRequest.

Gets all outputs of a compiled model which was used to create this InferRequest.

Gets all output tensors of this InferRequest.

Performance is measured per layer to get feedback on the most time-consuming operation.

Gets all outputs tensors of this InferRequest.

Gets currently held userdata.

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino.InferRequest.__annotations__)

-
__class__
[#](https://docs.openvino.ai#openvino.InferRequest.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.InferRequest.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino.InferRequest.__dir__) Default dir() implementation.


-
__eq__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.InferRequest.__eq__) Return self==value.


-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino.InferRequest.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.InferRequest.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.InferRequest.__getattribute__) Return getattr(self, name).


-
__getstate__()
[#](https://docs.openvino.ai#openvino.InferRequest.__getstate__) Helper for pickle.


-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.InferRequest.__gt__) Return self>value.


-
__hash__()
[#](https://docs.openvino.ai#openvino.InferRequest.__hash__) Return hash(self).


-
__init__(
*self: openvino._pyopenvino.InferRequest*,*other: openvino._pyopenvino.InferRequest*) None[#](https://docs.openvino.ai#id0)

-
__init_subclass__()
[#](https://docs.openvino.ai#openvino.InferRequest.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.InferRequest.__le__) Return self<=value.


-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.InferRequest.__lt__) Return self<value.


-
__ne__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.InferRequest.__ne__) Return self!=value.


-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino.InferRequest.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino.InferRequest.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino.InferRequest.__reduce_ex__) Helper for pickle.


-
__repr__(
*self: openvino._pyopenvino.InferRequest*) str[#](https://docs.openvino.ai#openvino.InferRequest.__repr__)

-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino.InferRequest.__setattr__) Implement setattr(self, name, value).


-
__sizeof__()
[#](https://docs.openvino.ai#openvino.InferRequest.__sizeof__) Size of object in memory, in bytes.


-
__str__()
[#](https://docs.openvino.ai#openvino.InferRequest.__str__) Return str(self).


-
__subclasshook__()
[#](https://docs.openvino.ai#openvino.InferRequest.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_is_single_input() bool
[#](https://docs.openvino.ai#openvino.InferRequest._is_single_input)

-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino.InferRequest._pybind11_conduit_v1_)

-
cancel(
*self: openvino._pyopenvino.InferRequest*) None[#](https://docs.openvino.ai#openvino.InferRequest.cancel) Cancels inference request.


-
get_compiled_model()
[CompiledModel](https://docs.openvino.ai/openvino.CompiledModel.html#openvino.CompiledModel)[#](https://docs.openvino.ai#openvino.InferRequest.get_compiled_model) Gets the compiled model this InferRequest is using.

- Returns:
a CompiledModel object

- Return type:


-
get_input_tensor(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.InferRequest.get_input_tensor) Overloaded function.

get_input_tensor(self: openvino._pyopenvino.InferRequest, index: typing.SupportsInt) -> openvino._pyopenvino.Tensor

Gets input tensor of InferRequest.

- param idx:
An index of tensor to get.

- type idx:
int

- return:
An input Tensor with index idx for the model. If a tensor with specified idx is not found,


an exception is thrown. :rtype: openvino.Tensor

get_input_tensor(self: openvino._pyopenvino.InferRequest) -> openvino._pyopenvino.Tensor

Gets input tensor of InferRequest.

- return:
An input Tensor for the model. If model has several inputs, an exception is thrown.

- rtype:
openvino.Tensor




-
get_output_tensor(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.InferRequest.get_output_tensor) Overloaded function.

get_output_tensor(self: openvino._pyopenvino.InferRequest, index: typing.SupportsInt) -> openvino._pyopenvino.Tensor

Gets output tensor of InferRequest.

- param idx:
An index of tensor to get.

- type idx:
int

- return:
An output Tensor with index idx for the model. If a tensor with specified idx is not found, an exception is thrown.

- rtype:
openvino.Tensor


get_output_tensor(self: openvino._pyopenvino.InferRequest) -> openvino._pyopenvino.Tensor

Gets output tensor of InferRequest.

- return:
An output Tensor for the model. If model has several outputs, an exception is thrown.

- rtype:
openvino.Tensor




-
get_profiling_info(
*self: openvino._pyopenvino.InferRequest*) list[[openvino._pyopenvino.ProfilingInfo](https://docs.openvino.ai/openvino.ProfilingInfo.html#openvino.ProfilingInfo)][#](https://docs.openvino.ai#openvino.InferRequest.get_profiling_info) Queries performance is measured per layer to get feedback on what is the most time-consuming operation, not all plugins provide meaningful data.

GIL is released while running this function.

- Returns:
list of profiling information for operations in model.

- Return type:
list[

[openvino.ProfilingInfo](https://docs.openvino.ai/openvino.ProfilingInfo.html#openvino.ProfilingInfo)]


-
get_tensor(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.InferRequest.get_tensor) Overloaded function.

get_tensor(self: openvino._pyopenvino.InferRequest, name: str) -> openvino._pyopenvino.Tensor

Gets input/output tensor of InferRequest.

- param name:
Name of tensor to get.

- type name:
str

- return:
A Tensor object with given name.

- rtype:
openvino.Tensor


get_tensor(self: openvino._pyopenvino.InferRequest, port: openvino._pyopenvino.ConstOutput) -> openvino._pyopenvino.Tensor

Gets input/output tensor of InferRequest.

- param port:
Port of tensor to get.

- type port:
openvino.ConstOutput

- return:
A Tensor object for the port.

- rtype:
openvino.Tensor


get_tensor(self: openvino._pyopenvino.InferRequest, port: openvino._pyopenvino.Output) -> openvino._pyopenvino.Tensor

Gets input/output tensor of InferRequest.

- param port:
Port of tensor to get.

- type port:
openvino.Output

- return:
A Tensor object for the port.

- rtype:
openvino.Tensor




-
infer(
*inputs: Any = None*,*share_inputs: bool = False*,*share_outputs: bool = False*,***,*decode_strings: bool = True*) OVDict[#](https://docs.openvino.ai#openvino.InferRequest.infer) Infers specified input(s) in synchronous mode.

Blocks all methods of InferRequest while request is running. Calling any method will lead to throwing exceptions.

The allowed types of keys in the inputs dictionary are:

int

str

openvino.ConstOutput


The allowed types of values in the inputs are:

numpy.ndarray and all the types that are castable to it, e.g. torch.Tensor

openvino.Tensor


Can be called with only one openvino.Tensor or numpy.ndarray, it will work only with one-input models. When model has more inputs, function throws error.

- Parameters:
**inputs**(*Any**,**optional*) – Data to be set on input tensors.**share_inputs**(*bool**,**optional*) –Enables share_inputs mode. Controls memory usage on inference’s inputs.

If set to False inputs the data dispatcher will safely copy data to existing Tensors (including up- or down-casting according to data type, resizing of the input Tensor). Keeps Tensor inputs “as-is”.

If set to True the data dispatcher tries to provide “zero-copy” Tensors for every input in form of: * numpy.ndarray and all the types that are castable to it, e.g. torch.Tensor Data that is going to be copied: * numpy.ndarray which are not C contiguous and/or not writable (WRITEABLE flag is set to False) * inputs which data types are mismatched from Infer Request’s inputs * inputs that should be in BF16 data type * scalar inputs (i.e. np.float_/str/bytes/int/float) * lists of simple data types (i.e. str/bytes/int/float) Keeps Tensor inputs “as-is”.

Note: Use with extra care, shared data can be modified during runtime! Note: Using share_inputs may result in extra memory overhead.

Default value: False

**share_outputs**(*bool**,**optional*) –Enables share_outputs mode. Controls memory usage on inference’s outputs.

If set to False outputs will safely copy data to numpy arrays.

If set to True the data will be returned in form of views of output Tensors. This mode still returns the data in format of numpy arrays but lifetime of the data is connected to OpenVINO objects.

Note: Use with extra care, shared data can be modified or lost during runtime! Note: String/textual data will always be copied!

Default value: False

**decode_strings**(*bool**,**optional**,**keyword-only*) –Controls decoding outputs of textual based data.

If set to True string outputs will be returned as numpy arrays of U kind.

If set to False string outputs will be returned as numpy arrays of S kind.

Default value: True


- Returns:
Dictionary of results from output tensors with port/int/str keys.

- Return type:
OVDict



-
*property*input_tensors[#](https://docs.openvino.ai#openvino.InferRequest.input_tensors) Gets all input tensors of this InferRequest.

- Return type:
list[

[openvino.Tensor](https://docs.openvino.ai/openvino.Tensor.html#openvino.Tensor)]


-
*property*latency[#](https://docs.openvino.ai#openvino.InferRequest.latency) Gets latency of this InferRequest.

- Return type:
float



-
*property*model_inputs[#](https://docs.openvino.ai#openvino.InferRequest.model_inputs) Gets all inputs of a compiled model which was used to create this InferRequest.

- Return type:
list[

[openvino.ConstOutput](https://docs.openvino.ai/openvino.ConstOutput.html#openvino.ConstOutput)]


-
*property*model_outputs[#](https://docs.openvino.ai#openvino.InferRequest.model_outputs) Gets all outputs of a compiled model which was used to create this InferRequest.

- Return type:
list[

[openvino.ConstOutput](https://docs.openvino.ai/openvino.ConstOutput.html#openvino.ConstOutput)]


-
*property*output_tensors[#](https://docs.openvino.ai#openvino.InferRequest.output_tensors) Gets all output tensors of this InferRequest.

- Return type:
list[

[openvino.Tensor](https://docs.openvino.ai/openvino.Tensor.html#openvino.Tensor)]


-
*property*profiling_info[#](https://docs.openvino.ai#openvino.InferRequest.profiling_info) Performance is measured per layer to get feedback on the most time-consuming operation. Not all plugins provide meaningful data!

GIL is released while running this function.

- Returns:
Inference time.

- Return type:
list[

[openvino.ProfilingInfo](https://docs.openvino.ai/openvino.ProfilingInfo.html#openvino.ProfilingInfo)]


-
query_state(
*self: openvino._pyopenvino.InferRequest*) list[openvino._pyopenvino.VariableState][#](https://docs.openvino.ai#openvino.InferRequest.query_state) Gets state control interface for given infer request.

GIL is released while running this function.

- Returns:
list of VariableState objects.

- Return type:
list[openvino.VariableState]



-
reset_state(
*self: openvino._pyopenvino.InferRequest*) None[#](https://docs.openvino.ai#openvino.InferRequest.reset_state) Resets all internal variable states for relevant infer request to a value specified as default for the corresponding ReadValue node


-
*property*results*: OVDict*[#](https://docs.openvino.ai#openvino.InferRequest.results) Gets all outputs tensors of this InferRequest.

- Returns:
Dictionary of results from output tensors with ports as keys.

- Return type:
dict[

[openvino.ConstOutput](https://docs.openvino.ai/openvino.ConstOutput.html#openvino.ConstOutput), numpy.array]


-
set_callback(
*self: openvino._pyopenvino.InferRequest*,*callback: collections.abc.Callable*,*userdata: object*) None[#](https://docs.openvino.ai#openvino.InferRequest.set_callback) Sets a callback function that will be called on success or failure of asynchronous InferRequest.

- Parameters:
**callback**(*function*) – Function defined in Python.**userdata**(*Any*) – Any data that will be passed inside callback call.



-
set_input_tensor(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.InferRequest.set_input_tensor) Overloaded function.

set_input_tensor(self: openvino._pyopenvino.InferRequest, index: typing.SupportsInt, tensor: openvino._pyopenvino.Tensor) -> None

Sets input tensor of InferRequest.

- param idx:
Index of input tensor. If idx is greater than number of model’s inputs, an exception is thrown.

- type idx:
int

- param tensor:
Tensor object. The element_type and shape of a tensor must match the model’s input element_type and shape.

- type tensor:
openvino.Tensor


set_input_tensor(self: openvino._pyopenvino.InferRequest, tensor: openvino._pyopenvino.Tensor) -> None

Sets input tensor of InferRequest with single input. If model has several inputs, an exception is thrown.

- param tensor:
Tensor object. The element_type and shape of a tensor must match the model’s input element_type and shape.

- type tensor:
openvino.Tensor




-
set_input_tensors(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.InferRequest.set_input_tensors) Overloaded function.

set_input_tensors(self: openvino._pyopenvino.InferRequest, inputs: dict) -> None

Set input tensors using given indexes.

- param inputs:
Data to set on output tensors.

- type inputs:
dict[int, openvino.Tensor]


set_input_tensors(self: openvino._pyopenvino.InferRequest, tensors: openvino._pyopenvino.TensorVector) -> None

Sets batch of tensors for single input data. Model input needs to have batch dimension and the number of tensors needs to match with batch size.

- param tensors:
Input tensors for batched infer request. The type of each tensor must match the model input element type and shape (except batch dimension). Total size of tensors needs to match with input’s size.

- type tensors:
openvino.TensorVector


set_input_tensors(self: openvino._pyopenvino.InferRequest, tensors: list) -> None

Sets batch of tensors for single input data. Model input needs to have batch dimension and the number of tensors needs to match with batch size.

- param tensors:
Input tensors for batched infer request. The type of each tensor must match the model input element type and shape (except batch dimension). Total size of tensors needs to match with input’s size.

- type tensors:
list[openvino.Tensor]


set_input_tensors(self: openvino._pyopenvino.InferRequest, idx: typing.SupportsInt, tensors: openvino._pyopenvino.TensorVector) -> None

Sets batch of tensors for single input data to infer by index. Model input needs to have batch dimension and the number of tensors needs to match with batch size.

- param idx:
Index of input tensor.

- type idx:
int

- param tensors:
Input tensors for batched infer request. The type of each tensor must match the model input element type and shape (except batch dimension). Total size of tensors needs to match with input’s size.

- type tensors:
openvino.TensorVector


set_input_tensors(self: openvino._pyopenvino.InferRequest, idx: typing.SupportsInt, tensors: list) -> None

Sets batch of tensors for single input data to infer by index. Model input needs to have batch dimension and the number of tensors needs to match with batch size.

- param idx:
Index of input tensor.

- type idx:
int

- param tensors:
Input tensors for batched infer request. The type of each tensor must match the model input element type and shape (except batch dimension). Total size of tensors needs to match with input’s size.

- type tensors:
list[openvino.Tensor]




-
set_output_tensor(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.InferRequest.set_output_tensor) Overloaded function.

set_output_tensor(self: openvino._pyopenvino.InferRequest, index: typing.SupportsInt, tensor: openvino._pyopenvino.Tensor) -> None

Sets output tensor of InferRequest.

- param idx:
Index of output tensor.

- type idx:
int

- param tensor:
Tensor object. The element_type and shape of a tensor must match the model’s output element_type and shape.

- type tensor:
openvino.Tensor


set_output_tensor(self: openvino._pyopenvino.InferRequest, tensor: openvino._pyopenvino.Tensor) -> None

Sets output tensor of InferRequest with single output. If model has several outputs, an exception is thrown.

- param tensor:
Tensor object. The element_type and shape of a tensor must match the model’s output element_type and shape.

- type tensor:
openvino.Tensor




-
set_output_tensors(
*self: openvino._pyopenvino.InferRequest*,*outputs: dict*) None[#](https://docs.openvino.ai#openvino.InferRequest.set_output_tensors) Set output tensors using given indexes.

- Parameters:
**outputs**(*dict**[**int**,**openvino.Tensor**]*) – Data to set on output tensors.


-
set_tensor(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.InferRequest.set_tensor) Overloaded function.

set_tensor(self: openvino._pyopenvino.InferRequest, name: str, tensor: openvino._pyopenvino.RemoteTensor) -> None

Sets input/output tensor of InferRequest.

- param name:
Name of input/output tensor.

- type name:
str

- param tensor:
RemoteTensor object. The element_type and shape of a tensor must match the model’s input/output element_type and shape.

- type tensor:
openvino.RemoteTensor


set_tensor(self: openvino._pyopenvino.InferRequest, name: str, tensor: openvino._pyopenvino.Tensor) -> None

Sets input/output tensor of InferRequest.

- param name:
Name of input/output tensor.

- type name:
str

- param tensor:
Tensor object. The element_type and shape of a tensor must match the model’s input/output element_type and shape.

- type tensor:
openvino.Tensor


set_tensor(self: openvino._pyopenvino.InferRequest, port: openvino._pyopenvino.ConstOutput, tensor: openvino._pyopenvino.Tensor) -> None

Sets input/output tensor of InferRequest.

- param port:
Port of input/output tensor.

- type port:
openvino.ConstOutput

- param tensor:
Tensor object. The element_type and shape of a tensor must match the model’s input/output element_type and shape.

- type tensor:
openvino.Tensor


set_tensor(self: openvino._pyopenvino.InferRequest, port: openvino._pyopenvino.Output, tensor: openvino._pyopenvino.Tensor) -> None

Sets input/output tensor of InferRequest.

- param port:
Port of input/output tensor.

- type port:
openvino.Output

- param tensor:
Tensor object. The element_type and shape of a tensor must match the model’s input/output element_type and shape.

- type tensor:
openvino.Tensor




-
set_tensors(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.InferRequest.set_tensors) Overloaded function.

set_tensors(self: openvino._pyopenvino.InferRequest, inputs: dict) -> None

Set tensors using given keys.

- param inputs:
Data to set on tensors.

- type inputs:
dict[Union[int, str, openvino.ConstOutput], openvino.Tensor]


set_tensors(self: openvino._pyopenvino.InferRequest, tensor_name: str, tensors: openvino._pyopenvino.TensorVector) -> None

Sets batch of tensors for input data to infer by tensor name. Model input needs to have batch dimension and the number of tensors needs to be matched with batch size. Current version supports set tensors to model inputs only. In case if tensor_name is associated with output (or any other non-input node), an exception will be thrown.

- param tensor_name:
Name of input tensor.

- type tensor_name:
str

- param tensors:
Input tensors for batched infer request. The type of each tensor must match the model input element type and shape (except batch dimension). Total size of tensors needs to match with input’s size.

- type tensors:
openvino.TensorVector


set_tensors(self: openvino._pyopenvino.InferRequest, tensor_name: str, tensors: list) -> None

Sets batch of tensors for input data to infer by tensor name. Model input needs to have batch dimension and the number of tensors needs to be matched with batch size. Current version supports set tensors to model inputs only. In case if tensor_name is associated with output (or any other non-input node), an exception will be thrown.

- param tensor_name:
Name of input tensor.

- type tensor_name:
str

- param tensors:
Input tensors for batched infer request. The type of each tensor must match the model input element type and shape (except batch dimension). Total size of tensors needs to match with input’s size.

- type tensors:
list[openvino.Tensor]


set_tensors(self: openvino._pyopenvino.InferRequest, port: openvino._pyopenvino.ConstOutput, tensors: openvino._pyopenvino.TensorVector) -> None

Sets a batch of tensors for input data to infer by input port. Model input needs to have batch dimension and the number of tensors needs to be matched with batch size. Current version supports set tensors to model inputs only. In case if port is associated with output (or any other non-input node), an exception will be thrown.

- param port:
Port of input tensor.

- type port:
openvino.ConstOutput

- param tensors:
Input tensors for batched infer request. The type of each tensor must match the model input element type and shape (except batch dimension). Total size of tensors needs to match with input’s size.

- type tensors:
openvino.TensorVector

- rtype:
None


set_tensors(self: openvino._pyopenvino.InferRequest, port: openvino._pyopenvino.ConstOutput, tensors: list) -> None

Sets a batch of tensors for input data to infer by input port. Model input needs to have batch dimension and the number of tensors needs to be matched with batch size. Current version supports set tensors to model inputs only. In case if port is associated with output (or any other non-input node), an exception will be thrown.

- param port:
Port of input tensor.

- type port:
openvino.ConstOutput

- param tensors:
Input tensors for batched infer request. The type of each tensor must match the model input element type and shape (except batch dimension). Total size of tensors needs to match with input’s size.

- type tensors:
list[openvino.Tensor]

- rtype:
None




-
start_async(
*inputs: Any = None*,*userdata: Any = None*,*share_inputs: bool = False*) None[#](https://docs.openvino.ai#openvino.InferRequest.start_async) Starts inference of specified input(s) in asynchronous mode.

Returns immediately. Inference starts also immediately. Calling any method on the InferRequest object while the request is running will lead to throwing exceptions.

The allowed types of keys in the inputs dictionary are:

int

str

openvino.ConstOutput


The allowed types of values in the inputs are:

numpy.ndarray and all the types that are castable to it, e.g. torch.Tensor

openvino.Tensor


Can be called with only one openvino.Tensor or numpy.ndarray, it will work only with one-input models. When model has more inputs, function throws error.

- Parameters:
**inputs**(*Any**,**optional*) – Data to be set on input tensors.**userdata**(*Any*) – Any data that will be passed inside the callback.**share_inputs**(*bool**,**optional*) –Enables share_inputs mode. Controls memory usage on inference’s inputs.

If set to False inputs the data dispatcher will safely copy data to existing Tensors (including up- or down-casting according to data type, resizing of the input Tensor). Keeps Tensor inputs “as-is”.

If set to True the data dispatcher tries to provide “zero-copy” Tensors for every input in form of: * numpy.ndarray and all the types that are castable to it, e.g. torch.Tensor Data that is going to be copied: * numpy.ndarray which are not C contiguous and/or not writable (WRITEABLE flag is set to False) * inputs which data types are mismatched from Infer Request’s inputs * inputs that should be in BF16 data type * scalar inputs (i.e. np.float_/str/bytes/int/float) * lists of simple data types (i.e. str/bytes/int/float) Keeps Tensor inputs “as-is”.

Note: Use with extra care, shared data can be modified during runtime! Note: Using share_inputs may result in extra memory overhead.

Default value: False




-
*property*userdata[#](https://docs.openvino.ai#openvino.InferRequest.userdata) Gets currently held userdata.

- Return type:
Any



-
wait(
*self: openvino._pyopenvino.InferRequest*) None[#](https://docs.openvino.ai#openvino.InferRequest.wait) Waits for the result to become available. Blocks until the result becomes available.

GIL is released while running this function.


-
wait_for(
*self: openvino._pyopenvino.InferRequest*,*timeout: SupportsInt*) bool[#](https://docs.openvino.ai#openvino.InferRequest.wait_for) Waits for the result to become available. Blocks until specified timeout has elapsed or the result becomes available, whichever comes first.

GIL is released while running this function.

- Parameters:
**timeout**(*int*) – Maximum duration in milliseconds (ms) of blocking call.- Returns:
True if InferRequest is ready, False otherwise.

- Return type:
bool



-
__init__(