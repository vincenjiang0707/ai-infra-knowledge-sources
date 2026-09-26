source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.Shape.html
lastmod: 

# openvino.Shape[#](https://docs.openvino.ai#openvino-shape)

-
*class*openvino.Shape[#](https://docs.openvino.ai#openvino.Shape) Bases:

`pybind11_object`

openvino.Shape wraps ov::Shape

-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.Shape.__init__) Overloaded function.

__init__(self: openvino._pyopenvino.Shape) -> None

__init__(self: openvino._pyopenvino.Shape, axis_lengths: collections.abc.Sequence[typing.SupportsInt]) -> None

__init__(self: openvino._pyopenvino.Shape, axis_lengths: openvino._pyopenvino.Shape) -> None

__init__(self: openvino._pyopenvino.Shape, shape: str) -> None



Methods

(name, /)`__delattr__`

Implement delattr(self, name).

()`__dir__`

Default dir() implementation.

(*args, **kwargs)`__eq__`

Overloaded function.

(format_spec, /)`__format__`

Default object formatter.

(value, /)`__ge__`

Return self>=value.

(name, /)`__getattribute__`

Return getattr(self, name).

(*args, **kwargs)`__getitem__`

Overloaded function.

Helper for pickle.

(value, /)`__gt__`

Return self>value.

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

(*args, **kwargs)`__setitem__`

Overloaded function.

Size of object in memory, in bytes.

(self)`__str__`

Abstract classes can override this to customize issubclass().

(self)`to_string`

Attributes

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino.Shape.__annotations__)

-
__class__
[#](https://docs.openvino.ai#openvino.Shape.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.Shape.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino.Shape.__dir__) Default dir() implementation.


-
__eq__(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.Shape.__eq__) Overloaded function.

__eq__(self: openvino._pyopenvino.Shape, arg0: openvino._pyopenvino.Shape) -> bool

__eq__(self: openvino._pyopenvino.Shape, arg0: tuple) -> bool

__eq__(self: openvino._pyopenvino.Shape, arg0: list) -> bool



-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino.Shape.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.Shape.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.Shape.__getattribute__) Return getattr(self, name).


-
__getitem__(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.Shape.__getitem__) Overloaded function.

__getitem__(self: openvino._pyopenvino.Shape, arg0: typing.SupportsInt) -> int

__getitem__(self: openvino._pyopenvino.Shape, arg0: slice) -> openvino._pyopenvino.Shape



-
__getstate__()
[#](https://docs.openvino.ai#openvino.Shape.__getstate__) Helper for pickle.


-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.Shape.__gt__) Return self>value.


-
__hash__
*= None*[#](https://docs.openvino.ai#openvino.Shape.__hash__)

-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#id0) Overloaded function.

__init__(self: openvino._pyopenvino.Shape) -> None

__init__(self: openvino._pyopenvino.Shape, axis_lengths: collections.abc.Sequence[typing.SupportsInt]) -> None

__init__(self: openvino._pyopenvino.Shape, axis_lengths: openvino._pyopenvino.Shape) -> None

__init__(self: openvino._pyopenvino.Shape, shape: str) -> None



-
__init_subclass__()
[#](https://docs.openvino.ai#openvino.Shape.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__iter__(
*self:*) collections.abc.Iterator[int][openvino._pyopenvino.Shape](https://docs.openvino.ai#openvino.Shape)[#](https://docs.openvino.ai#openvino.Shape.__iter__)

-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.Shape.__le__) Return self<=value.


-
__len__(
*self:*) int[openvino._pyopenvino.Shape](https://docs.openvino.ai#openvino.Shape)[#](https://docs.openvino.ai#openvino.Shape.__len__)

-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.Shape.__lt__) Return self<value.


-
__ne__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.Shape.__ne__) Return self!=value.


-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino.Shape.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino.Shape.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino.Shape.__reduce_ex__) Helper for pickle.


-
__repr__(
*self:*) str[openvino._pyopenvino.Shape](https://docs.openvino.ai#openvino.Shape)[#](https://docs.openvino.ai#openvino.Shape.__repr__)

-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino.Shape.__setattr__) Implement setattr(self, name, value).


-
__setitem__(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.Shape.__setitem__) Overloaded function.

__setitem__(self: openvino._pyopenvino.Shape, arg0: typing.SupportsInt, arg1: typing.SupportsInt) -> None

__setitem__(self: openvino._pyopenvino.Shape, arg0: typing.SupportsInt, arg1: openvino._pyopenvino.Dimension) -> None



-
__sizeof__()
[#](https://docs.openvino.ai#openvino.Shape.__sizeof__) Size of object in memory, in bytes.


-
__str__(
*self:*) str[openvino._pyopenvino.Shape](https://docs.openvino.ai#openvino.Shape)[#](https://docs.openvino.ai#openvino.Shape.__str__)

-
__subclasshook__()
[#](https://docs.openvino.ai#openvino.Shape.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino.Shape._pybind11_conduit_v1_)

-
to_string(
*self:*) str[openvino._pyopenvino.Shape](https://docs.openvino.ai#openvino.Shape)[#](https://docs.openvino.ai#openvino.Shape.to_string)

-
__init__(