source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.CompiledModel.html
lastmod: 

# openvino.CompiledModel[#](https://docs.openvino.ai#openvino-compiledmodel)

-
*class*openvino.CompiledModel(*other: CompiledModel*,*weights: bytes | None = None*)[#](https://docs.openvino.ai#openvino.CompiledModel) Bases:

`CompiledModel`

CompiledModel class.

CompiledModel represents Model that is compiled for a specific device by applying multiple optimization transformations, then mapping to compute kernels.

-
__init__(
*self: openvino._pyopenvino.CompiledModel*,*other: openvino._pyopenvino.CompiledModel*) None[#](https://docs.openvino.ai#openvino.CompiledModel.__init__)

Methods

([inputs, share_inputs, ...])`__call__`

Callable infer wrapper for CompiledModel.

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

Creates an inference request object used to infer the compiled model.

(*args, **kwargs)`export_model`

Overloaded function.

(self, property)`get_property`

Gets properties for current compiled model.

(self)`get_runtime_model`

Gets runtime model information from a device.

([inputs])`infer_new_request`

Infers specified input(s) in synchronous mode.

(*args, **kwargs)`input`

Overloaded function.

(*args, **kwargs)`output`

Overloaded function.

Gets state control interface for the underlaying infer request.

(self)`release_memory`

Release intermediate memory.

Resets all internal variable states of the underlaying infer request.

(*args, **kwargs)`set_property`

Overloaded function.

Attributes

Gets all inputs of a compiled model.

Gets all outputs of a compiled model.

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino.CompiledModel.__annotations__)

-
__call__(
*inputs: Any = None*,*share_inputs: bool = True*,*share_outputs: bool = False*,***,*decode_strings: bool = True*) OVDict[#](https://docs.openvino.ai#openvino.CompiledModel.__call__) Callable infer wrapper for CompiledModel.

Infers specified input(s) in synchronous mode.

Blocks all methods of CompiledModel while request is running.

Method creates new temporary InferRequest and run inference on it. It is advised to use a dedicated InferRequest class for performance, optimizing workflows, and creating advanced pipelines.

This method stores created InferRequest inside CompiledModel object, which can be later reused in consecutive calls.

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

Default value: True

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
Dictionary of results from output tensors with port/int/str as keys.

- Return type:
OVDict



-
__class__
[#](https://docs.openvino.ai#openvino.CompiledModel.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.CompiledModel.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino.CompiledModel.__dir__) Default dir() implementation.


-
__eq__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.CompiledModel.__eq__) Return self==value.


-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino.CompiledModel.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.CompiledModel.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.CompiledModel.__getattribute__) Return getattr(self, name).


-
__getstate__()
[#](https://docs.openvino.ai#openvino.CompiledModel.__getstate__) Helper for pickle.


-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.CompiledModel.__gt__) Return self>value.


-
__hash__()
[#](https://docs.openvino.ai#openvino.CompiledModel.__hash__) Return hash(self).


-
__init__(
*self: openvino._pyopenvino.CompiledModel*,*other: openvino._pyopenvino.CompiledModel*) None[#](https://docs.openvino.ai#id0)

-
__init_subclass__()
[#](https://docs.openvino.ai#openvino.CompiledModel.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.CompiledModel.__le__) Return self<=value.


-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.CompiledModel.__lt__) Return self<value.


-
__ne__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.CompiledModel.__ne__) Return self!=value.


-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino.CompiledModel.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino.CompiledModel.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino.CompiledModel.__reduce_ex__) Helper for pickle.


-
__repr__(
*self: openvino._pyopenvino.CompiledModel*) str[#](https://docs.openvino.ai#openvino.CompiledModel.__repr__)

-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino.CompiledModel.__setattr__) Implement setattr(self, name, value).


-
__sizeof__()
[#](https://docs.openvino.ai#openvino.CompiledModel.__sizeof__) Size of object in memory, in bytes.


-
__str__()
[#](https://docs.openvino.ai#openvino.CompiledModel.__str__) Return str(self).


-
__subclasshook__()
[#](https://docs.openvino.ai#openvino.CompiledModel.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino.CompiledModel._pybind11_conduit_v1_)

-
create_infer_request()
[InferRequest](https://docs.openvino.ai/openvino.InferRequest.html#openvino.InferRequest)[#](https://docs.openvino.ai#openvino.CompiledModel.create_infer_request) Creates an inference request object used to infer the compiled model.

The created request has allocated input and output tensors.

- Returns:
New InferRequest object.

- Return type:


-
export_model(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.CompiledModel.export_model) Overloaded function.

export_model(self: openvino._pyopenvino.CompiledModel) -> object

Exports the compiled model to bytes/output stream.

GIL is released while running this function.

- return:
Bytes object that contains this compiled model.

- rtype:
bytes


user_stream = compiled.export_model() with open('./my_model', 'wb') as f: f.write(user_stream) # ... new_compiled = core.import_model(user_stream, "CPU")

export_model(self: openvino._pyopenvino.CompiledModel, model_stream: object) -> None

Exports the compiled model to bytes/output stream.

Advanced version of export_model. It utilizes, streams from the standard Python library io.

Function performs flushing of the stream, writes to it, and then rewinds the stream to the beginning (using seek(0)).

GIL is released while running this function.

- param model_stream:
A stream object to which the model will be serialized.

- type model_stream:
io.BytesIO

- rtype:
None


user_stream = io.BytesIO() compiled.export_model(user_stream) with open('./my_model', 'wb') as f: f.write(user_stream.getvalue()) # or read() if seek(0) was applied before # ... new_compiled = core.import_model(user_stream, "CPU")



-
get_property(
*self: openvino._pyopenvino.CompiledModel*,*property: str*) object[#](https://docs.openvino.ai#openvino.CompiledModel.get_property) Gets properties for current compiled model.

- Parameters:
**name**(*str*) – Property name.- Return type:
Any



-
get_runtime_model(
*self: openvino._pyopenvino.CompiledModel*) openvino._pyopenvino.Model[#](https://docs.openvino.ai#openvino.CompiledModel.get_runtime_model) Gets runtime model information from a device.

This object (returned model) represents the internal device-specific model which is optimized for the particular accelerator. It contains device-specific nodes, runtime information, and can be used only to understand how the source model is optimized and which kernels, element types, and layouts are selected.

- Returns:
Model, containing Executable Graph information.

- Return type:


-
infer_new_request(
*inputs: Any = None*) OVDict[#](https://docs.openvino.ai#openvino.CompiledModel.infer_new_request) Infers specified input(s) in synchronous mode.

Blocks all methods of CompiledModel while request is running.

Method creates new temporary InferRequest and run inference on it. It is advised to use a dedicated InferRequest class for performance, optimizing workflows, and creating advanced pipelines.

The allowed types of keys in the inputs dictionary are:

int

str

openvino.ConstOutput


The allowed types of values in the inputs are:

numpy.ndarray and all the types that are castable to it, e.g. torch.Tensor

openvino.Tensor


Can be called with only one openvino.Tensor or numpy.ndarray, it will work only with one-input models. When model has more inputs, function throws error.

- Parameters:
**inputs**(*Any**,**optional*) – Data to be set on input tensors.- Returns:
Dictionary of results from output tensors with port/int/str keys.

- Return type:
OVDict



-
input(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.CompiledModel.input) Overloaded function.

input(self: openvino._pyopenvino.CompiledModel) -> openvino._pyopenvino.ConstOutput

Gets a single input of a compiled model. If a model has more than one input, this method throws an exception.

- return:
A compiled model input.

- rtype:
openvino.ConstOutput


input(self: openvino._pyopenvino.CompiledModel, index: typing.SupportsInt) -> openvino._pyopenvino.ConstOutput

Gets input of a compiled model identified by an index. If the input with given index is not found, this method throws an exception.

- param index:
An input index.

- type index:
int

- return:
A compiled model input.

- rtype:
openvino.ConstOutput


input(self: openvino._pyopenvino.CompiledModel, tensor_name: str) -> openvino._pyopenvino.ConstOutput

Gets input of a compiled model identified by a tensor_name. If the input with given tensor name is not found, this method throws an exception.

- param tensor_name:
An input tensor name.

- type tensor_name:
str

- return:
A compiled model input.

- rtype:
openvino.ConstOutput




-
*property*inputs[#](https://docs.openvino.ai#openvino.CompiledModel.inputs) Gets all inputs of a compiled model.

- Returns:
Inputs of a compiled model.

- Return type:
list[

[openvino.ConstOutput](https://docs.openvino.ai/openvino.ConstOutput.html#openvino.ConstOutput)]


-
output(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.CompiledModel.output) Overloaded function.

output(self: openvino._pyopenvino.CompiledModel) -> openvino._pyopenvino.ConstOutput

Gets a single output of a compiled model. If the model has more than one output, this method throws an exception.

- return:
A compiled model output.

- rtype:
openvino.ConstOutput


output(self: openvino._pyopenvino.CompiledModel, index: typing.SupportsInt) -> openvino._pyopenvino.ConstOutput

Gets output of a compiled model identified by an index. If the output with given index is not found, this method throws an exception.

- param index:
An output index.

- type index:
int

- return:
A compiled model output.

- rtype:
openvino.ConstOutput


output(self: openvino._pyopenvino.CompiledModel, tensor_name: str) -> openvino._pyopenvino.ConstOutput

Gets output of a compiled model identified by a tensor_name. If the output with given tensor name is not found, this method throws an exception.

- param tensor_name:
An output tensor name.

- type tensor_name:
str

- return:
A compiled model output.

- rtype:
openvino.ConstOutput




-
*property*outputs[#](https://docs.openvino.ai#openvino.CompiledModel.outputs) Gets all outputs of a compiled model.

- Returns:
Outputs of a compiled model.

- Return type:
list[

[openvino.ConstOutput](https://docs.openvino.ai/openvino.ConstOutput.html#openvino.ConstOutput)]


-
query_state() None
[#](https://docs.openvino.ai#openvino.CompiledModel.query_state) Gets state control interface for the underlaying infer request.

- Returns:
list of VariableState objects.

- Return type:
list[openvino.VariableState]



-
release_memory(
*self: openvino._pyopenvino.CompiledModel*) None[#](https://docs.openvino.ai#openvino.CompiledModel.release_memory) Release intermediate memory.

This method forces the Compiled model to release memory allocated for intermediate structures, e.g. caches, tensors, temporal buffers etc., when possible


-
reset_state() None
[#](https://docs.openvino.ai#openvino.CompiledModel.reset_state) Resets all internal variable states of the underlaying infer request.

Resets all internal variable states to a value specified as default for the corresponding ReadValue node.


-
set_property(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.CompiledModel.set_property) Overloaded function.

set_property(self: openvino._pyopenvino.CompiledModel, properties: collections.abc.Mapping[str, object]) -> None

Sets properties for current compiled model.

- param properties:
dict of pairs: (property name, property value)

- type properties:
dict

- rtype:
None


set_property(self: openvino._pyopenvino.CompiledModel, property: tuple[str, object]) -> None

Sets properties for current compiled model.

- param property:
tuple of (property name, matching property value).

- type property:
tuple




-
__init__(