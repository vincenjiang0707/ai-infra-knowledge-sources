source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.OVAny.html
lastmod: 

# openvino.OVAny[#](https://docs.openvino.ai#openvino-ovany)

-
*class*openvino.OVAny[#](https://docs.openvino.ai#openvino.OVAny) Bases:

`pybind11_object`

openvino.OVAny provides object wrapper for OpenVINOov::Any class. It allows to pass different types of objectsinto C++ based core of the project.

-
__init__(
*self:*,[openvino._pyopenvino.OVAny](https://docs.openvino.ai#openvino.OVAny)*arg0: object*) None[#](https://docs.openvino.ai#openvino.OVAny.__init__)

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

(self)`__get__`

(name, /)`__getattribute__`

Return getattr(self, name).

(self, arg0)`__getitem__`

Helper for pickle.

(value, /)`__gt__`

Return self>value.

(self)`__hash__`

(self, arg0)`__init__`

This method is called when a class is subclassed.

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

(self, arg0)`__set__`

(name, value, /)`__setattr__`

Implement setattr(self, name, value).

(*args, **kwargs)`__setitem__`

Overloaded function.

Size of object in memory, in bytes.

()`__str__`

Return str(self).

Abstract classes can override this to customize issubclass().

(self[, dtype])`aslist`

Returns runtime attribute as a list with specified data type.

(self, arg0)`astype`

Returns runtime attribute casted to defined data type.

(self)`get`

(self, arg0)`set`

Attributes

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino.OVAny.__annotations__)

-
__class__
[#](https://docs.openvino.ai#openvino.OVAny.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.OVAny.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino.OVAny.__dir__) Default dir() implementation.


-
__eq__(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.OVAny.__eq__) Overloaded function.

__eq__(self: openvino._pyopenvino.OVAny, arg0: openvino._pyopenvino.OVAny) -> bool

__eq__(self: openvino._pyopenvino.OVAny, arg0: object) -> bool



-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino.OVAny.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.OVAny.__ge__) Return self>=value.


-
__get__(
*self:*) object[openvino._pyopenvino.OVAny](https://docs.openvino.ai#openvino.OVAny)[#](https://docs.openvino.ai#openvino.OVAny.__get__)

-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.OVAny.__getattribute__) Return getattr(self, name).


-
__getitem__(
*self:*,[openvino._pyopenvino.OVAny](https://docs.openvino.ai#openvino.OVAny)*arg0: object*) object[#](https://docs.openvino.ai#openvino.OVAny.__getitem__)

-
__getstate__()
[#](https://docs.openvino.ai#openvino.OVAny.__getstate__) Helper for pickle.


-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.OVAny.__gt__) Return self>value.


-
__hash__(
*self:*) object[openvino._pyopenvino.OVAny](https://docs.openvino.ai#openvino.OVAny)[#](https://docs.openvino.ai#openvino.OVAny.__hash__)

-
__init__(
*self:*,[openvino._pyopenvino.OVAny](https://docs.openvino.ai#openvino.OVAny)*arg0: object*) None[#](https://docs.openvino.ai#id0)

-
__init_subclass__()
[#](https://docs.openvino.ai#openvino.OVAny.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.OVAny.__le__) Return self<=value.


-
__len__(
*self:*) object[openvino._pyopenvino.OVAny](https://docs.openvino.ai#openvino.OVAny)[#](https://docs.openvino.ai#openvino.OVAny.__len__)

-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.OVAny.__lt__) Return self<value.


-
__ne__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.OVAny.__ne__) Return self!=value.


-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino.OVAny.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino.OVAny.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino.OVAny.__reduce_ex__) Helper for pickle.


-
__repr__(
*self:*) str[openvino._pyopenvino.OVAny](https://docs.openvino.ai#openvino.OVAny)[#](https://docs.openvino.ai#openvino.OVAny.__repr__)

-
__set__(
*self:*,[openvino._pyopenvino.OVAny](https://docs.openvino.ai#openvino.OVAny)*arg0:*) None[openvino._pyopenvino.OVAny](https://docs.openvino.ai#openvino.OVAny)[#](https://docs.openvino.ai#openvino.OVAny.__set__)

-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino.OVAny.__setattr__) Implement setattr(self, name, value).


-
__setitem__(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.OVAny.__setitem__) Overloaded function.

__setitem__(self: openvino._pyopenvino.OVAny, arg0: object, arg1: str) -> None

__setitem__(self: openvino._pyopenvino.OVAny, arg0: object, arg1: typing.SupportsInt) -> None



-
__sizeof__()
[#](https://docs.openvino.ai#openvino.OVAny.__sizeof__) Size of object in memory, in bytes.


-
__str__()
[#](https://docs.openvino.ai#openvino.OVAny.__str__) Return str(self).


-
__subclasshook__()
[#](https://docs.openvino.ai#openvino.OVAny.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino.OVAny._pybind11_conduit_v1_)

-
aslist(
*self:*,[openvino._pyopenvino.OVAny](https://docs.openvino.ai#openvino.OVAny)*dtype: object = None*) object[#](https://docs.openvino.ai#openvino.OVAny.aslist) Returns runtime attribute as a list with specified data type.


-
astype(
*self:*,[openvino._pyopenvino.OVAny](https://docs.openvino.ai#openvino.OVAny)*arg0: object*) object[#](https://docs.openvino.ai#openvino.OVAny.astype) Returns runtime attribute casted to defined data type.

- Parameters:
**dtype**(*Union**[**bool**,**int**,**str**,**float**,**dict**]*) – Data type in which runtime attribute will be casted.- Returns:
A runtime attribute.

- Return type:
Any



-
get(
*self:*) object[openvino._pyopenvino.OVAny](https://docs.openvino.ai#openvino.OVAny)[#](https://docs.openvino.ai#openvino.OVAny.get) - Returns:
Value of this OVAny.

- Return type:
Any



-
set(
*self:*,[openvino._pyopenvino.OVAny](https://docs.openvino.ai#openvino.OVAny)*arg0: object*) None[#](https://docs.openvino.ai#openvino.OVAny.set) - Param:
Value to be set in OVAny.

- Type:
Any



-
*property*value[#](https://docs.openvino.ai#openvino.OVAny.value) - Returns:
Value of this OVAny.

- Return type:
Any



-
__init__(