source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.AxisSet.html
lastmod: 

# openvino.AxisSet[#](https://docs.openvino.ai#openvino-axisset)

-
*class*openvino.AxisSet[#](https://docs.openvino.ai#openvino.AxisSet) Bases:

`pybind11_object`

openvino.AxisSet wraps ov::AxisSet

-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.AxisSet.__init__) Overloaded function.

__init__(self: openvino._pyopenvino.AxisSet, axes: collections.abc.Set[typing.SupportsInt]) -> None

__init__(self: openvino._pyopenvino.AxisSet, axes: collections.abc.Sequence[typing.SupportsInt]) -> None

__init__(self: openvino._pyopenvino.AxisSet, axes: openvino._pyopenvino.AxisSet) -> None



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

Overloaded function.

This method is called when a class is subclassed.

(self)`__iter__`

(value, /)`__le__`

Return self<=value.

(self)`__len__`

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

Attributes

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino.AxisSet.__annotations__)

-
__class__
[#](https://docs.openvino.ai#openvino.AxisSet.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.AxisSet.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino.AxisSet.__dir__) Default dir() implementation.


-
__eq__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.AxisSet.__eq__) Return self==value.


-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino.AxisSet.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.AxisSet.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.AxisSet.__getattribute__) Return getattr(self, name).


-
__getstate__()
[#](https://docs.openvino.ai#openvino.AxisSet.__getstate__) Helper for pickle.


-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.AxisSet.__gt__) Return self>value.


-
__hash__()
[#](https://docs.openvino.ai#openvino.AxisSet.__hash__) Return hash(self).


-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#id0) Overloaded function.

__init__(self: openvino._pyopenvino.AxisSet, axes: collections.abc.Set[typing.SupportsInt]) -> None

__init__(self: openvino._pyopenvino.AxisSet, axes: collections.abc.Sequence[typing.SupportsInt]) -> None

__init__(self: openvino._pyopenvino.AxisSet, axes: openvino._pyopenvino.AxisSet) -> None



-
__init_subclass__()
[#](https://docs.openvino.ai#openvino.AxisSet.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__iter__(
*self:*) collections.abc.Iterator[int][openvino._pyopenvino.AxisSet](https://docs.openvino.ai#openvino.AxisSet)[#](https://docs.openvino.ai#openvino.AxisSet.__iter__)

-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.AxisSet.__le__) Return self<=value.


-
__len__(
*self:*) int[openvino._pyopenvino.AxisSet](https://docs.openvino.ai#openvino.AxisSet)[#](https://docs.openvino.ai#openvino.AxisSet.__len__)

-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.AxisSet.__lt__) Return self<value.


-
__ne__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.AxisSet.__ne__) Return self!=value.


-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino.AxisSet.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino.AxisSet.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino.AxisSet.__reduce_ex__) Helper for pickle.


-
__repr__(
*self:*) str[openvino._pyopenvino.AxisSet](https://docs.openvino.ai#openvino.AxisSet)[#](https://docs.openvino.ai#openvino.AxisSet.__repr__)

-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino.AxisSet.__setattr__) Implement setattr(self, name, value).


-
__sizeof__()
[#](https://docs.openvino.ai#openvino.AxisSet.__sizeof__) Size of object in memory, in bytes.


-
__str__()
[#](https://docs.openvino.ai#openvino.AxisSet.__str__) Return str(self).


-
__subclasshook__()
[#](https://docs.openvino.ai#openvino.AxisSet.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino.AxisSet._pybind11_conduit_v1_)

-
__init__(