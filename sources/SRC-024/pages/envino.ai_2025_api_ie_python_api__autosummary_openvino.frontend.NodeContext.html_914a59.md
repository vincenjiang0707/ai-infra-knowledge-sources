source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.frontend.NodeContext.html
lastmod: 

# openvino.frontend.NodeContext[#](https://docs.openvino.ai#openvino-frontend-nodecontext)

-
*class*openvino.frontend.NodeContext[#](https://docs.openvino.ai#openvino.frontend.NodeContext) Bases:

`pybind11_object`

-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.frontend.NodeContext.__init__)

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

(self, name[, default_value, dtype])`get_attribute`

(*args, **kwargs)`get_input`

Overloaded function.

(*args, **kwargs)`get_input_size`

Overloaded function.

(self, arg0)`get_op_type`

(self, idx[, ...])`get_values_from_const_input`

(self, arg0)`has_attribute`

Attributes

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino.frontend.NodeContext.__annotations__)

-
__class__
[#](https://docs.openvino.ai#openvino.frontend.NodeContext.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.frontend.NodeContext.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino.frontend.NodeContext.__dir__) Default dir() implementation.


-
__eq__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.frontend.NodeContext.__eq__) Return self==value.


-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino.frontend.NodeContext.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.frontend.NodeContext.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.frontend.NodeContext.__getattribute__) Return getattr(self, name).


-
__getstate__()
[#](https://docs.openvino.ai#openvino.frontend.NodeContext.__getstate__) Helper for pickle.


-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.frontend.NodeContext.__gt__) Return self>value.


-
__hash__()
[#](https://docs.openvino.ai#openvino.frontend.NodeContext.__hash__) Return hash(self).


-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#id0)

-
__init_subclass__()
[#](https://docs.openvino.ai#openvino.frontend.NodeContext.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.frontend.NodeContext.__le__) Return self<=value.


-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.frontend.NodeContext.__lt__) Return self<value.


-
__ne__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.frontend.NodeContext.__ne__) Return self!=value.


-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino.frontend.NodeContext.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino.frontend.NodeContext.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino.frontend.NodeContext.__reduce_ex__) Helper for pickle.


-
__repr__()
[#](https://docs.openvino.ai#openvino.frontend.NodeContext.__repr__) Return repr(self).


-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino.frontend.NodeContext.__setattr__) Implement setattr(self, name, value).


-
__sizeof__()
[#](https://docs.openvino.ai#openvino.frontend.NodeContext.__sizeof__) Size of object in memory, in bytes.


-
__str__()
[#](https://docs.openvino.ai#openvino.frontend.NodeContext.__str__) Return str(self).


-
__subclasshook__()
[#](https://docs.openvino.ai#openvino.frontend.NodeContext.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino.frontend.NodeContext._pybind11_conduit_v1_)

-
get_attribute(
*self:*,[openvino._pyopenvino.NodeContext](https://docs.openvino.ai#openvino.frontend.NodeContext)*name: str*,*default_value: object = None*,*dtype: object = None*) object[#](https://docs.openvino.ai#openvino.frontend.NodeContext.get_attribute)

-
get_input(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.frontend.NodeContext.get_input) Overloaded function.

get_input(self: openvino._pyopenvino.NodeContext, arg0: typing.SupportsInt) -> openvino._pyopenvino.Output

get_input(self: openvino._pyopenvino.NodeContext, arg0: str) -> openvino._pyopenvino.Output

get_input(self: openvino._pyopenvino.NodeContext, arg0: str, arg1: typing.SupportsInt) -> openvino._pyopenvino.Output



-
get_input_size(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.frontend.NodeContext.get_input_size) Overloaded function.

get_input_size(self: openvino._pyopenvino.NodeContext) -> int

get_input_size(self: openvino._pyopenvino.NodeContext, arg0: str) -> int



-
get_op_type(
*self:*,[openvino._pyopenvino.NodeContext](https://docs.openvino.ai#openvino.frontend.NodeContext)*arg0: str*) str[#](https://docs.openvino.ai#openvino.frontend.NodeContext.get_op_type)

-
get_values_from_const_input(
*self:*,[openvino._pyopenvino.NodeContext](https://docs.openvino.ai#openvino.frontend.NodeContext)*idx: SupportsInt*,*default_value: object = None*,*dtype: object = None*) object[#](https://docs.openvino.ai#openvino.frontend.NodeContext.get_values_from_const_input)

-
has_attribute(
*self:*,[openvino._pyopenvino.NodeContext](https://docs.openvino.ai#openvino.frontend.NodeContext)*arg0: str*) bool[#](https://docs.openvino.ai#openvino.frontend.NodeContext.has_attribute)

-
__init__(