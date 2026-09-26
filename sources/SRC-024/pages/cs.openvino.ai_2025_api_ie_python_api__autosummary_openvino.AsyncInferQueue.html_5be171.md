source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.AsyncInferQueue.html
lastmod: 

# openvino.AsyncInferQueue[#](https://docs.openvino.ai#openvino-asyncinferqueue)

-
*class*openvino.AsyncInferQueue[#](https://docs.openvino.ai#openvino.AsyncInferQueue) Bases:

`AsyncInferQueue`

AsyncInferQueue with a pool of asynchronous requests.

AsyncInferQueue represents a helper that creates a pool of asynchronous InferRequests and provides synchronization functions to control flow of a simple pipeline.

-
__init__(
*self: openvino._pyopenvino.AsyncInferQueue*,*model: openvino._pyopenvino.CompiledModel*,*jobs: SupportsInt = 0*) None[#](https://docs.openvino.ai#openvino.AsyncInferQueue.__init__) Creates AsyncInferQueue.

- Parameters:
**model**() – Model to be used to create InferRequests in a pool.*openvino.CompiledModel***jobs**– Number of InferRequests objects in a pool. If 0, jobs number


will be set automatically to the optimal number. Default: 0 :type jobs: int :rtype: openvino.AsyncInferQueue


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

(i)`__getitem__`

Gets InferRequest from the pool with given i id.

Helper for pickle.

(value, /)`__gt__`

Return self>value.

()`__hash__`

Return hash(self).

(self, model[, jobs])`__init__`

Creates AsyncInferQueue.

This method is called when a class is subclassed.

()`__iter__`

Allows to iterate over AsyncInferQueue.

(value, /)`__le__`

Return self<=value.

(self)`__len__`

Number of InferRequests in the pool.

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

(self)`get_idle_request_id`

Returns next free id of InferRequest from queue's pool.

(self)`is_ready`

One of 'flow control' functions.

(self, arg0)`set_callback`

Sets unified callback on all InferRequests from queue's pool.

([inputs, userdata, share_inputs])`start_async`

Run asynchronous inference using the next available InferRequest from the pool.

(self)`wait_all`

One of 'flow control' functions.

Attributes

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino.AsyncInferQueue.__annotations__)

-
__class__
[#](https://docs.openvino.ai#openvino.AsyncInferQueue.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.AsyncInferQueue.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino.AsyncInferQueue.__dir__) Default dir() implementation.


-
__eq__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.AsyncInferQueue.__eq__) Return self==value.


-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino.AsyncInferQueue.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.AsyncInferQueue.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.AsyncInferQueue.__getattribute__) Return getattr(self, name).


-
__getitem__(
*i: int*)[InferRequest](https://docs.openvino.ai/openvino.InferRequest.html#openvino.InferRequest)[#](https://docs.openvino.ai#openvino.AsyncInferQueue.__getitem__) Gets InferRequest from the pool with given i id.

Resulting object is guaranteed to work with read-only methods like getting tensors. Any mutating methods (e.g. start_async, set_callback) of a request will put the parent AsyncInferQueue object in an invalid state.

- Parameters:
**i**(*int*) – InferRequest id.- Returns:
InferRequests from the pool with given id.

- Return type:


-
__getstate__()
[#](https://docs.openvino.ai#openvino.AsyncInferQueue.__getstate__) Helper for pickle.


-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.AsyncInferQueue.__gt__) Return self>value.


-
__hash__()
[#](https://docs.openvino.ai#openvino.AsyncInferQueue.__hash__) Return hash(self).


-
__init__(
*self: openvino._pyopenvino.AsyncInferQueue*,*model: openvino._pyopenvino.CompiledModel*,*jobs: SupportsInt = 0*) None[#](https://docs.openvino.ai#id0) Creates AsyncInferQueue.

- Parameters:
**model**() – Model to be used to create InferRequests in a pool.*openvino.CompiledModel***jobs**– Number of InferRequests objects in a pool. If 0, jobs number


will be set automatically to the optimal number. Default: 0 :type jobs: int :rtype: openvino.AsyncInferQueue


-
__init_subclass__()
[#](https://docs.openvino.ai#openvino.AsyncInferQueue.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__iter__() Iterator[
[InferRequest](https://docs.openvino.ai/openvino.InferRequest.html#openvino.InferRequest)][#](https://docs.openvino.ai#openvino.AsyncInferQueue.__iter__) Allows to iterate over AsyncInferQueue.

Resulting objects are guaranteed to work with read-only methods like getting tensors. Any mutating methods (e.g. start_async, set_callback) of a single request will put the parent AsyncInferQueue object in an invalid state.

- Returns:
a generator that yields InferRequests.

- Return type:
collections.abc.Iterable[

[openvino.InferRequest](https://docs.openvino.ai/openvino.InferRequest.html#openvino.InferRequest)]


-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.AsyncInferQueue.__le__) Return self<=value.


-
__len__(
*self: openvino._pyopenvino.AsyncInferQueue*) int[#](https://docs.openvino.ai#openvino.AsyncInferQueue.__len__) Number of InferRequests in the pool.

- Return type:
int



-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.AsyncInferQueue.__lt__) Return self<value.


-
__ne__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.AsyncInferQueue.__ne__) Return self!=value.


-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino.AsyncInferQueue.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino.AsyncInferQueue.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino.AsyncInferQueue.__reduce_ex__) Helper for pickle.


-
__repr__(
*self: openvino._pyopenvino.AsyncInferQueue*) str[#](https://docs.openvino.ai#openvino.AsyncInferQueue.__repr__)

-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino.AsyncInferQueue.__setattr__) Implement setattr(self, name, value).


-
__sizeof__()
[#](https://docs.openvino.ai#openvino.AsyncInferQueue.__sizeof__) Size of object in memory, in bytes.


-
__str__()
[#](https://docs.openvino.ai#openvino.AsyncInferQueue.__str__) Return str(self).


-
__subclasshook__()
[#](https://docs.openvino.ai#openvino.AsyncInferQueue.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino.AsyncInferQueue._pybind11_conduit_v1_)

-
get_idle_request_id(
*self: openvino._pyopenvino.AsyncInferQueue*) int[#](https://docs.openvino.ai#openvino.AsyncInferQueue.get_idle_request_id) Returns next free id of InferRequest from queue’s pool. Function waits for any request to complete and then returns this request’s id.

GIL is released while running this function.

- Return type:
int



-
is_ready(
*self: openvino._pyopenvino.AsyncInferQueue*) bool[#](https://docs.openvino.ai#openvino.AsyncInferQueue.is_ready) One of ‘flow control’ functions. Returns True if any free request in the pool, otherwise False.

GIL is released while running this function.

- Returns:
If there is at least one free InferRequest in a pool, returns True.

- Return type:
bool



-
set_callback(
*self: openvino._pyopenvino.AsyncInferQueue*,*arg0: collections.abc.Callable*) None[#](https://docs.openvino.ai#openvino.AsyncInferQueue.set_callback) Sets unified callback on all InferRequests from queue’s pool. Signature of such function should have two arguments, where first one is InferRequest object and second one is userdata connected to InferRequest from the AsyncInferQueue’s pool.

def f(request, userdata): result = request.output_tensors[0] print(result + userdata) async_infer_queue.set_callback(f)

- Parameters:
**callback**(*function*) – Any Python defined function that matches callback’s requirements.


-
start_async(
*inputs: Any = None*,*userdata: Any = None*,*share_inputs: bool = False*) None[#](https://docs.openvino.ai#openvino.AsyncInferQueue.start_async) Run asynchronous inference using the next available InferRequest from the pool.

The allowed types of keys in the inputs dictionary are:

int

str

openvino.ConstOutput


The allowed types of values in the inputs are:

numpy.ndarray and all the types that are castable to it, e.g. torch.Tensor

openvino.Tensor


Can be called with only one openvino.Tensor or numpy.ndarray, it will work only with one-input models. When model has more inputs, function throws error.

- Parameters:
**inputs**(*Any**,**optional*) – Data to be set on input tensors of the next available InferRequest.**userdata**(*Any**,**optional*) – Any data that will be passed to a callback.**share_inputs**(*bool**,**optional*) –Enables share_inputs mode. Controls memory usage on inference’s inputs.

If set to False inputs the data dispatcher will safely copy data to existing Tensors (including up- or down-casting according to data type, resizing of the input Tensor). Keeps Tensor inputs “as-is”.

If set to True the data dispatcher tries to provide “zero-copy” Tensors for every input in form of: * numpy.ndarray and all the types that are castable to it, e.g. torch.Tensor Data that is going to be copied: * numpy.ndarray which are not C contiguous and/or not writable (WRITEABLE flag is set to False) * inputs which data types are mismatched from Infer Request’s inputs * inputs that should be in BF16 data type * scalar inputs (i.e. np.float_/str/bytes/int/float) * lists of simple data types (i.e. str/bytes/int/float) Keeps Tensor inputs “as-is”.

Note: Use with extra care, shared data can be modified during runtime! Note: Using share_inputs may result in extra memory overhead.

Default value: False




-
*property*userdata[#](https://docs.openvino.ai#openvino.AsyncInferQueue.userdata) - Returns:
list of all passed userdata. list is filled with None if the data wasn’t passed yet.

- Return type:
list[Any]



-
wait_all(
*self: openvino._pyopenvino.AsyncInferQueue*) None[#](https://docs.openvino.ai#openvino.AsyncInferQueue.wait_all) One of ‘flow control’ functions. Blocking call. Waits for all InferRequests in a pool to finish scheduled work.

GIL is released while running this function.


-
__init__(