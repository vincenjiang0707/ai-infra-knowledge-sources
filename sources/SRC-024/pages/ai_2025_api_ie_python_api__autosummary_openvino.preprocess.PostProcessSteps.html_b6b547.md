source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.preprocess.PostProcessSteps.html
lastmod: 

# openvino.preprocess.PostProcessSteps[#](https://docs.openvino.ai#openvino-preprocess-postprocesssteps)

-
*class*openvino.preprocess.PostProcessSteps[#](https://docs.openvino.ai#openvino.preprocess.PostProcessSteps) Bases:

`pybind11_object`

openvino.preprocess.PostprocessSteps wraps ov::preprocess::PostProcessSteps

-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.preprocess.PostProcessSteps.__init__)

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

(*args, **kwargs)`__init__`

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

()`__repr__`

Return repr(self).

(name, value, /)`__setattr__`

Implement setattr(self, name, value).

Size of object in memory, in bytes.

()`__str__`

Return str(self).

Abstract classes can override this to customize issubclass().

(self[, type])`convert_element_type`

Converts tensor element type to specified type.

(*args, **kwargs)`convert_layout`

Overloaded function.

(self, operation)`custom`

Adds custom postprocessing operation.

Attributes

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino.preprocess.PostProcessSteps.__annotations__)

-
__class__
[#](https://docs.openvino.ai#openvino.preprocess.PostProcessSteps.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.preprocess.PostProcessSteps.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino.preprocess.PostProcessSteps.__dir__) Default dir() implementation.


-
__eq__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.preprocess.PostProcessSteps.__eq__) Return self==value.


-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino.preprocess.PostProcessSteps.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.preprocess.PostProcessSteps.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.preprocess.PostProcessSteps.__getattribute__) Return getattr(self, name).


-
__getstate__()
[#](https://docs.openvino.ai#openvino.preprocess.PostProcessSteps.__getstate__) Helper for pickle.


-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.preprocess.PostProcessSteps.__gt__) Return self>value.


-
__hash__()
[#](https://docs.openvino.ai#openvino.preprocess.PostProcessSteps.__hash__) Return hash(self).


-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#id0)

-
__init_subclass__()
[#](https://docs.openvino.ai#openvino.preprocess.PostProcessSteps.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.preprocess.PostProcessSteps.__le__) Return self<=value.


-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.preprocess.PostProcessSteps.__lt__) Return self<value.


-
__ne__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.preprocess.PostProcessSteps.__ne__) Return self!=value.


-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino.preprocess.PostProcessSteps.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino.preprocess.PostProcessSteps.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino.preprocess.PostProcessSteps.__reduce_ex__) Helper for pickle.


-
__repr__()
[#](https://docs.openvino.ai#openvino.preprocess.PostProcessSteps.__repr__) Return repr(self).


-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino.preprocess.PostProcessSteps.__setattr__) Implement setattr(self, name, value).


-
__sizeof__()
[#](https://docs.openvino.ai#openvino.preprocess.PostProcessSteps.__sizeof__) Size of object in memory, in bytes.


-
__str__()
[#](https://docs.openvino.ai#openvino.preprocess.PostProcessSteps.__str__) Return str(self).


-
__subclasshook__()
[#](https://docs.openvino.ai#openvino.preprocess.PostProcessSteps.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino.preprocess.PostProcessSteps._pybind11_conduit_v1_)

-
convert_element_type(
*self:*,[openvino._pyopenvino.preprocess.PostProcessSteps](https://docs.openvino.ai#openvino.preprocess.PostProcessSteps)*type:*)[openvino._pyopenvino.Type](https://docs.openvino.ai/openvino.Type.html#openvino.Type)= openvino.Type.dynamic[openvino._pyopenvino.preprocess.PostProcessSteps](https://docs.openvino.ai#openvino.preprocess.PostProcessSteps)[#](https://docs.openvino.ai#openvino.preprocess.PostProcessSteps.convert_element_type) Converts tensor element type to specified type. Tensor must have openvino.Type data type.

- Parameters:
**type**() – Destination type. If not specified, type will be taken from model output’s element type.*openvino.Type*- Returns:
Reference to itself to allow chaining of calls in client’s code in a builder-like manner.

- Return type:


-
convert_layout(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.preprocess.PostProcessSteps.convert_layout) Overloaded function.

convert_layout(self: openvino._pyopenvino.preprocess.PostProcessSteps, dst_layout: openvino._pyopenvino.Layout) -> openvino._pyopenvino.preprocess.PostProcessSteps

convert_layout(self: openvino._pyopenvino.preprocess.PostProcessSteps, dims: collections.abc.Sequence[typing.SupportsInt]) -> openvino._pyopenvino.preprocess.PostProcessSteps



-
custom(
*self:*,[openvino._pyopenvino.preprocess.PostProcessSteps](https://docs.openvino.ai#openvino.preprocess.PostProcessSteps)*operation: collections.abc.Callable*)[openvino._pyopenvino.preprocess.PostProcessSteps](https://docs.openvino.ai#openvino.preprocess.PostProcessSteps)[#](https://docs.openvino.ai#openvino.preprocess.PostProcessSteps.custom) Adds custom postprocessing operation.

- Parameters:
**operation**(*function*) – Python’s function which takes openvino.Output as input argument and returns`openvino.Output`.- Returns:
Reference to itself, allows chaining of calls in client’s code in a builder-like manner.

- Return type:


-
__init__(