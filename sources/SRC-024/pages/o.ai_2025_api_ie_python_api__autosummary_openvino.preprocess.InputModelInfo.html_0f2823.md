source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.preprocess.InputModelInfo.html
lastmod: 

# openvino.preprocess.InputModelInfo[#](https://docs.openvino.ai#openvino-preprocess-inputmodelinfo)

-
*class*openvino.preprocess.InputModelInfo[#](https://docs.openvino.ai#openvino.preprocess.InputModelInfo) Bases:

`pybind11_object`

openvino.preprocess.InputModelInfo wraps ov::preprocess::InputModelInfo

-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.preprocess.InputModelInfo.__init__)

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

(self, layout)`set_layout`

Set layout for input model :param layout: layout to be set :type layout: Union[str, openvino.Layout]

Attributes

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino.preprocess.InputModelInfo.__annotations__)

-
__class__
[#](https://docs.openvino.ai#openvino.preprocess.InputModelInfo.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.preprocess.InputModelInfo.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino.preprocess.InputModelInfo.__dir__) Default dir() implementation.


-
__eq__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.preprocess.InputModelInfo.__eq__) Return self==value.


-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino.preprocess.InputModelInfo.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.preprocess.InputModelInfo.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.preprocess.InputModelInfo.__getattribute__) Return getattr(self, name).


-
__getstate__()
[#](https://docs.openvino.ai#openvino.preprocess.InputModelInfo.__getstate__) Helper for pickle.


-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.preprocess.InputModelInfo.__gt__) Return self>value.


-
__hash__()
[#](https://docs.openvino.ai#openvino.preprocess.InputModelInfo.__hash__) Return hash(self).


-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#id0)

-
__init_subclass__()
[#](https://docs.openvino.ai#openvino.preprocess.InputModelInfo.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.preprocess.InputModelInfo.__le__) Return self<=value.


-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.preprocess.InputModelInfo.__lt__) Return self<value.


-
__ne__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.preprocess.InputModelInfo.__ne__) Return self!=value.


-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino.preprocess.InputModelInfo.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino.preprocess.InputModelInfo.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino.preprocess.InputModelInfo.__reduce_ex__) Helper for pickle.


-
__repr__()
[#](https://docs.openvino.ai#openvino.preprocess.InputModelInfo.__repr__) Return repr(self).


-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino.preprocess.InputModelInfo.__setattr__) Implement setattr(self, name, value).


-
__sizeof__()
[#](https://docs.openvino.ai#openvino.preprocess.InputModelInfo.__sizeof__) Size of object in memory, in bytes.


-
__str__()
[#](https://docs.openvino.ai#openvino.preprocess.InputModelInfo.__str__) Return str(self).


-
__subclasshook__()
[#](https://docs.openvino.ai#openvino.preprocess.InputModelInfo.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino.preprocess.InputModelInfo._pybind11_conduit_v1_)

-
set_layout(
*self:*,[openvino._pyopenvino.preprocess.InputModelInfo](https://docs.openvino.ai#openvino.preprocess.InputModelInfo)*layout:*)[openvino._pyopenvino.Layout](https://docs.openvino.ai/openvino.Layout.html#openvino.Layout)[openvino._pyopenvino.preprocess.InputModelInfo](https://docs.openvino.ai#openvino.preprocess.InputModelInfo)[#](https://docs.openvino.ai#openvino.preprocess.InputModelInfo.set_layout) Set layout for input model :param layout: layout to be set :type layout: Union[str, openvino.Layout]


-
__init__(