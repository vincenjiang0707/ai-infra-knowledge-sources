source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.Symbol.html
lastmod: 

# openvino.Symbol[#](https://docs.openvino.ai#openvino-symbol)

-
*class*openvino.Symbol[#](https://docs.openvino.ai#openvino.Symbol) Bases:

`pybind11_object`

openvino.Symbol wraps ov::Symbol

-
__init__(
*self:*) None[openvino._pyopenvino.Symbol](https://docs.openvino.ai#openvino.Symbol)[#](https://docs.openvino.ai#openvino.Symbol.__init__)

Methods

(self)`__bool__`

Check whether the symbol is meaningful

(name, /)`__delattr__`

Implement delattr(self, name).

()`__dir__`

Default dir() implementation.

(self, arg0)`__eq__`

(format_spec, /)`__format__`

Default object formatter.

(value, /)`__ge__`

Return self>=value.

(name, /)`__getattribute__`

Return getattr(self, name).

Helper for pickle.

(value, /)`__gt__`

Return self>value.

(self)`__hash__`

(self)`__init__`

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

Attributes

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino.Symbol.__annotations__)

-
__bool__(
*self:*) bool[openvino._pyopenvino.Symbol](https://docs.openvino.ai#openvino.Symbol)[#](https://docs.openvino.ai#openvino.Symbol.__bool__) Check whether the symbol is meaningful


-
__class__
[#](https://docs.openvino.ai#openvino.Symbol.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.Symbol.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino.Symbol.__dir__) Default dir() implementation.


-
__eq__(
*self:*,[openvino._pyopenvino.Symbol](https://docs.openvino.ai#openvino.Symbol)*arg0:*) bool[openvino._pyopenvino.Symbol](https://docs.openvino.ai#openvino.Symbol)[#](https://docs.openvino.ai#openvino.Symbol.__eq__)

-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino.Symbol.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.Symbol.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.Symbol.__getattribute__) Return getattr(self, name).


-
__getstate__()
[#](https://docs.openvino.ai#openvino.Symbol.__getstate__) Helper for pickle.


-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.Symbol.__gt__) Return self>value.


-
__hash__(
*self:*) int[openvino._pyopenvino.Symbol](https://docs.openvino.ai#openvino.Symbol)[#](https://docs.openvino.ai#openvino.Symbol.__hash__)

-
__init__(
*self:*) None[openvino._pyopenvino.Symbol](https://docs.openvino.ai#openvino.Symbol)[#](https://docs.openvino.ai#id0)

-
__init_subclass__()
[#](https://docs.openvino.ai#openvino.Symbol.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.Symbol.__le__) Return self<=value.


-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.Symbol.__lt__) Return self<value.


-
__ne__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.Symbol.__ne__) Return self!=value.


-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino.Symbol.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino.Symbol.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino.Symbol.__reduce_ex__) Helper for pickle.


-
__repr__()
[#](https://docs.openvino.ai#openvino.Symbol.__repr__) Return repr(self).


-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino.Symbol.__setattr__) Implement setattr(self, name, value).


-
__sizeof__()
[#](https://docs.openvino.ai#openvino.Symbol.__sizeof__) Size of object in memory, in bytes.


-
__str__()
[#](https://docs.openvino.ai#openvino.Symbol.__str__) Return str(self).


-
__subclasshook__()
[#](https://docs.openvino.ai#openvino.Symbol.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino.Symbol._pybind11_conduit_v1_)

-
__init__(