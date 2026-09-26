source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.RTMap.html
lastmod: 

# openvino.RTMap[#](https://docs.openvino.ai#openvino-rtmap)

-
*class*openvino.RTMap[#](https://docs.openvino.ai#openvino.RTMap) Bases:

`pybind11_object`

openvino.RTMap makes bindings for std::map<std::string, ov::Any>, which can later be used as ov::Node::RTMap

-
__init__(
*self:*) None[openvino._pyopenvino.RTMap](https://docs.openvino.ai#openvino.RTMap)[#](https://docs.openvino.ai#openvino.RTMap.__init__)

Methods

(self)`__bool__`

Check whether the map is nonempty

(self, arg0)`__contains__`

(name, /)`__delattr__`

Implement delattr(self, name).

(self, arg0)`__delitem__`

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

(self, arg0)`__getitem__`

Helper for pickle.

(value, /)`__gt__`

Return self>value.

()`__hash__`

Return hash(self).

(self)`__init__`

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

()`__str__`

Return str(self).

Abstract classes can override this to customize issubclass().

(self)`items`

(self)`keys`

(self)`values`

Attributes

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino.RTMap.__annotations__)

-
__bool__(
*self:*) bool[openvino._pyopenvino.RTMap](https://docs.openvino.ai#openvino.RTMap)[#](https://docs.openvino.ai#openvino.RTMap.__bool__) Check whether the map is nonempty


-
__class__
[#](https://docs.openvino.ai#openvino.RTMap.__class__) alias of

`pybind11_type`


-
__contains__(
*self:*,[openvino._pyopenvino.RTMap](https://docs.openvino.ai#openvino.RTMap)*arg0: str*) bool[#](https://docs.openvino.ai#openvino.RTMap.__contains__)

-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.RTMap.__delattr__) Implement delattr(self, name).


-
__delitem__(
*self:*,[openvino._pyopenvino.RTMap](https://docs.openvino.ai#openvino.RTMap)*arg0: str*) None[#](https://docs.openvino.ai#openvino.RTMap.__delitem__)

-
__dir__()
[#](https://docs.openvino.ai#openvino.RTMap.__dir__) Default dir() implementation.


-
__eq__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.RTMap.__eq__) Return self==value.


-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino.RTMap.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.RTMap.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.RTMap.__getattribute__) Return getattr(self, name).


-
__getitem__(
*self:*,[openvino._pyopenvino.RTMap](https://docs.openvino.ai#openvino.RTMap)*arg0: str*) object[#](https://docs.openvino.ai#openvino.RTMap.__getitem__)

-
__getstate__()
[#](https://docs.openvino.ai#openvino.RTMap.__getstate__) Helper for pickle.


-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.RTMap.__gt__) Return self>value.


-
__hash__()
[#](https://docs.openvino.ai#openvino.RTMap.__hash__) Return hash(self).


-
__init__(
*self:*) None[openvino._pyopenvino.RTMap](https://docs.openvino.ai#openvino.RTMap)[#](https://docs.openvino.ai#id0)

-
__init_subclass__()
[#](https://docs.openvino.ai#openvino.RTMap.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__iter__(
*self:*) collections.abc.Iterator[str][openvino._pyopenvino.RTMap](https://docs.openvino.ai#openvino.RTMap)[#](https://docs.openvino.ai#openvino.RTMap.__iter__)

-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.RTMap.__le__) Return self<=value.


-
__len__(
*self:*) int[openvino._pyopenvino.RTMap](https://docs.openvino.ai#openvino.RTMap)[#](https://docs.openvino.ai#openvino.RTMap.__len__)

-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.RTMap.__lt__) Return self<value.


-
__ne__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.RTMap.__ne__) Return self!=value.


-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino.RTMap.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino.RTMap.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino.RTMap.__reduce_ex__) Helper for pickle.


-
__repr__(
*self:*) str[openvino._pyopenvino.RTMap](https://docs.openvino.ai#openvino.RTMap)[#](https://docs.openvino.ai#openvino.RTMap.__repr__)

-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino.RTMap.__setattr__) Implement setattr(self, name, value).


-
__setitem__(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.RTMap.__setitem__) Overloaded function.

__setitem__(self: openvino._pyopenvino.RTMap, arg0: str, arg1: str) -> None

__setitem__(self: openvino._pyopenvino.RTMap, arg0: str, arg1: typing.SupportsInt) -> None



-
__sizeof__()
[#](https://docs.openvino.ai#openvino.RTMap.__sizeof__) Size of object in memory, in bytes.


-
__str__()
[#](https://docs.openvino.ai#openvino.RTMap.__str__) Return str(self).


-
__subclasshook__()
[#](https://docs.openvino.ai#openvino.RTMap.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino.RTMap._pybind11_conduit_v1_)

-
items(
*self: object*) openvino._pyopenvino.Iterator[#](https://docs.openvino.ai#openvino.RTMap.items)

-
keys(
*self:*) collections.abc.Iterator[str][openvino._pyopenvino.RTMap](https://docs.openvino.ai#openvino.RTMap)[#](https://docs.openvino.ai#openvino.RTMap.keys)

-
values(
*self: object*) openvino._pyopenvino.Iterator[#](https://docs.openvino.ai#openvino.RTMap.values)

-
__init__(