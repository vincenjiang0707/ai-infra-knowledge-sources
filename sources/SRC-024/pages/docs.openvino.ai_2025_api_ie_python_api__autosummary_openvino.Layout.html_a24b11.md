source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.Layout.html
lastmod: 

# openvino.Layout[#](https://docs.openvino.ai#openvino-layout)

-
*class*openvino.Layout[#](https://docs.openvino.ai#openvino.Layout) Bases:

`pybind11_object`

openvino.Layout wraps ov::Layout

-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.Layout.__init__) Overloaded function.

__init__(self: openvino._pyopenvino.Layout) -> None

__init__(self: openvino._pyopenvino.Layout, layout_str: str) -> None



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

Helper for pickle.

(value, /)`__gt__`

Return self>value.

(*args, **kwargs)`__init__`

Overloaded function.

This method is called when a class is subclassed.

(value, /)`__le__`

Return self<=value.

(value, /)`__lt__`

Return self<value.

(*args, **kwargs)`__ne__`

Overloaded function.

(**kwargs)`__new__`

Helper for pickle.

(protocol, /)`__reduce_ex__`

Helper for pickle.

(self)`__repr__`

(name, value, /)`__setattr__`

Implement setattr(self, name, value).

Size of object in memory, in bytes.

(self)`__str__`

Abstract classes can override this to customize issubclass().

(self, dimension_name)`get_index_by_name`

(self, dimension_name)`has_name`

()`scalar`

(self)`to_string`

Attributes

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino.Layout.__annotations__)

-
__class__
[#](https://docs.openvino.ai#openvino.Layout.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.Layout.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino.Layout.__dir__) Default dir() implementation.


-
__eq__(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.Layout.__eq__) Overloaded function.

__eq__(self: openvino._pyopenvino.Layout, arg0: openvino._pyopenvino.Layout) -> bool

__eq__(self: openvino._pyopenvino.Layout, arg0: str) -> bool



-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino.Layout.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.Layout.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.Layout.__getattribute__) Return getattr(self, name).


-
__getstate__()
[#](https://docs.openvino.ai#openvino.Layout.__getstate__) Helper for pickle.


-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.Layout.__gt__) Return self>value.


-
__hash__
*= None*[#](https://docs.openvino.ai#openvino.Layout.__hash__)

-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#id0) Overloaded function.

__init__(self: openvino._pyopenvino.Layout) -> None

__init__(self: openvino._pyopenvino.Layout, layout_str: str) -> None



-
__init_subclass__()
[#](https://docs.openvino.ai#openvino.Layout.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.Layout.__le__) Return self<=value.


-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.Layout.__lt__) Return self<value.


-
__ne__(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.Layout.__ne__) Overloaded function.

__ne__(self: openvino._pyopenvino.Layout, arg0: openvino._pyopenvino.Layout) -> bool

__ne__(self: openvino._pyopenvino.Layout, arg0: str) -> bool



-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino.Layout.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino.Layout.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino.Layout.__reduce_ex__) Helper for pickle.


-
__repr__(
*self:*) str[openvino._pyopenvino.Layout](https://docs.openvino.ai#openvino.Layout)[#](https://docs.openvino.ai#openvino.Layout.__repr__)

-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino.Layout.__setattr__) Implement setattr(self, name, value).


-
__sizeof__()
[#](https://docs.openvino.ai#openvino.Layout.__sizeof__) Size of object in memory, in bytes.


-
__str__(
*self:*) str[openvino._pyopenvino.Layout](https://docs.openvino.ai#openvino.Layout)[#](https://docs.openvino.ai#openvino.Layout.__str__)

-
__subclasshook__()
[#](https://docs.openvino.ai#openvino.Layout.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino.Layout._pybind11_conduit_v1_)

-
*property*empty[#](https://docs.openvino.ai#openvino.Layout.empty)

-
get_index_by_name(
*self:*,[openvino._pyopenvino.Layout](https://docs.openvino.ai#openvino.Layout)*dimension_name: str*) int[#](https://docs.openvino.ai#openvino.Layout.get_index_by_name)

-
has_name(
*self:*,[openvino._pyopenvino.Layout](https://docs.openvino.ai#openvino.Layout)*dimension_name: str*) bool[#](https://docs.openvino.ai#openvino.Layout.has_name)

-
scalar()
[openvino._pyopenvino.Layout](https://docs.openvino.ai#openvino.Layout)[#](https://docs.openvino.ai#openvino.Layout.scalar)

-
to_string(
*self:*) str[openvino._pyopenvino.Layout](https://docs.openvino.ai#openvino.Layout)[#](https://docs.openvino.ai#openvino.Layout.to_string)

-
__init__(