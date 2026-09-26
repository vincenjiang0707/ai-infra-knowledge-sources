source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.preprocess.OutputTensorInfo.html
lastmod: 

# openvino.preprocess.OutputTensorInfo[#](https://docs.openvino.ai#openvino-preprocess-outputtensorinfo)

-
*class*openvino.preprocess.OutputTensorInfo[#](https://docs.openvino.ai#openvino.preprocess.OutputTensorInfo) Bases:

`pybind11_object`

openvino.preprocess.OutputTensorInfo wraps ov::preprocess::OutputTensorInfo

-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.preprocess.OutputTensorInfo.__init__)

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

(self, type)`set_element_type`

Set client's output tensor element type.

(self, layout)`set_layout`

Set layout for output tensor info

Attributes

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino.preprocess.OutputTensorInfo.__annotations__)

-
__class__
[#](https://docs.openvino.ai#openvino.preprocess.OutputTensorInfo.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.preprocess.OutputTensorInfo.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino.preprocess.OutputTensorInfo.__dir__) Default dir() implementation.


-
__eq__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.preprocess.OutputTensorInfo.__eq__) Return self==value.


-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino.preprocess.OutputTensorInfo.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.preprocess.OutputTensorInfo.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.preprocess.OutputTensorInfo.__getattribute__) Return getattr(self, name).


-
__getstate__()
[#](https://docs.openvino.ai#openvino.preprocess.OutputTensorInfo.__getstate__) Helper for pickle.


-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.preprocess.OutputTensorInfo.__gt__) Return self>value.


-
__hash__()
[#](https://docs.openvino.ai#openvino.preprocess.OutputTensorInfo.__hash__) Return hash(self).


-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#id0)

-
__init_subclass__()
[#](https://docs.openvino.ai#openvino.preprocess.OutputTensorInfo.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.preprocess.OutputTensorInfo.__le__) Return self<=value.


-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.preprocess.OutputTensorInfo.__lt__) Return self<value.


-
__ne__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.preprocess.OutputTensorInfo.__ne__) Return self!=value.


-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino.preprocess.OutputTensorInfo.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino.preprocess.OutputTensorInfo.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino.preprocess.OutputTensorInfo.__reduce_ex__) Helper for pickle.


-
__repr__()
[#](https://docs.openvino.ai#openvino.preprocess.OutputTensorInfo.__repr__) Return repr(self).


-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino.preprocess.OutputTensorInfo.__setattr__) Implement setattr(self, name, value).


-
__sizeof__()
[#](https://docs.openvino.ai#openvino.preprocess.OutputTensorInfo.__sizeof__) Size of object in memory, in bytes.


-
__str__()
[#](https://docs.openvino.ai#openvino.preprocess.OutputTensorInfo.__str__) Return str(self).


-
__subclasshook__()
[#](https://docs.openvino.ai#openvino.preprocess.OutputTensorInfo.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino.preprocess.OutputTensorInfo._pybind11_conduit_v1_)

-
set_element_type(
*self:*,[openvino._pyopenvino.preprocess.OutputTensorInfo](https://docs.openvino.ai#openvino.preprocess.OutputTensorInfo)*type:*)[openvino._pyopenvino.Type](https://docs.openvino.ai/openvino.Type.html#openvino.Type)[openvino._pyopenvino.preprocess.OutputTensorInfo](https://docs.openvino.ai#openvino.preprocess.OutputTensorInfo)[#](https://docs.openvino.ai#openvino.preprocess.OutputTensorInfo.set_element_type) Set client’s output tensor element type. If type is not the same as model’s element type, conversion of element type will be done automatically.

- Parameters:
**type**() – Client’s output tensor element type.*openvino.Type*- Returns:
Reference to itself to allow chaining of calls in client’s code in a builder-like manner.

- Return type:


-
set_layout(
*self:*,[openvino._pyopenvino.preprocess.OutputTensorInfo](https://docs.openvino.ai#openvino.preprocess.OutputTensorInfo)*layout:*)[openvino._pyopenvino.Layout](https://docs.openvino.ai/openvino.Layout.html#openvino.Layout)[openvino._pyopenvino.preprocess.OutputTensorInfo](https://docs.openvino.ai#openvino.preprocess.OutputTensorInfo)[#](https://docs.openvino.ai#openvino.preprocess.OutputTensorInfo.set_layout) Set layout for output tensor info

- Parameters:
**layout**(*Union**[**str**,**openvino.Layout**]*) – layout to be set


-
__init__(