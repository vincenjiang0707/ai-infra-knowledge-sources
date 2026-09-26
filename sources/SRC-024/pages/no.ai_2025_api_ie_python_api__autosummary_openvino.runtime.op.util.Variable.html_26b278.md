source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.op.util.Variable.html
lastmod: 

# openvino.runtime.op.util.Variable[#](https://docs.openvino.ai#openvino-runtime-op-util-variable)

-
*class*openvino.runtime.op.util.Variable[#](https://docs.openvino.ai#openvino.runtime.op.util.Variable) Bases:

`pybind11_object`

openvino.op.util.Variable wraps ov::op::util::Variable

-
__init__(
*self:*,[openvino._pyopenvino.op.util.Variable](https://docs.openvino.ai#openvino.runtime.op.util.Variable)*info:*) None[openvino._pyopenvino.op.util.VariableInfo](https://docs.openvino.ai/openvino.runtime.op.util.VariableInfo.html#openvino.runtime.op.util.VariableInfo)[#](https://docs.openvino.ai#openvino.runtime.op.util.Variable.__init__)

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

(self, info)`__init__`

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

(self)`__repr__`

(name, value, /)`__setattr__`

Implement setattr(self, name, value).

Size of object in memory, in bytes.

()`__str__`

Return str(self).

Abstract classes can override this to customize issubclass().

(self)`get_info`

(self, variable_info)`update`

Attributes

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino.runtime.op.util.Variable.__annotations__)

-
__class__
[#](https://docs.openvino.ai#openvino.runtime.op.util.Variable.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.runtime.op.util.Variable.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino.runtime.op.util.Variable.__dir__) Default dir() implementation.


-
__eq__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.runtime.op.util.Variable.__eq__) Return self==value.


-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino.runtime.op.util.Variable.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.runtime.op.util.Variable.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.runtime.op.util.Variable.__getattribute__) Return getattr(self, name).


-
__getstate__()
[#](https://docs.openvino.ai#openvino.runtime.op.util.Variable.__getstate__) Helper for pickle.


-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.runtime.op.util.Variable.__gt__) Return self>value.


-
__hash__()
[#](https://docs.openvino.ai#openvino.runtime.op.util.Variable.__hash__) Return hash(self).


-
__init__(
*self:*,[openvino._pyopenvino.op.util.Variable](https://docs.openvino.ai#openvino.runtime.op.util.Variable)*info:*) None[openvino._pyopenvino.op.util.VariableInfo](https://docs.openvino.ai/openvino.runtime.op.util.VariableInfo.html#openvino.runtime.op.util.VariableInfo)[#](https://docs.openvino.ai#id0)

-
__init_subclass__()
[#](https://docs.openvino.ai#openvino.runtime.op.util.Variable.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.runtime.op.util.Variable.__le__) Return self<=value.


-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.runtime.op.util.Variable.__lt__) Return self<value.


-
__ne__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.runtime.op.util.Variable.__ne__) Return self!=value.


-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino.runtime.op.util.Variable.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino.runtime.op.util.Variable.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino.runtime.op.util.Variable.__reduce_ex__) Helper for pickle.


-
__repr__(
*self:*) str[openvino._pyopenvino.op.util.Variable](https://docs.openvino.ai#openvino.runtime.op.util.Variable)[#](https://docs.openvino.ai#openvino.runtime.op.util.Variable.__repr__)

-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino.runtime.op.util.Variable.__setattr__) Implement setattr(self, name, value).


-
__sizeof__()
[#](https://docs.openvino.ai#openvino.runtime.op.util.Variable.__sizeof__) Size of object in memory, in bytes.


-
__str__()
[#](https://docs.openvino.ai#openvino.runtime.op.util.Variable.__str__) Return str(self).


-
__subclasshook__()
[#](https://docs.openvino.ai#openvino.runtime.op.util.Variable.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino.runtime.op.util.Variable._pybind11_conduit_v1_)

-
*property*info[#](https://docs.openvino.ai#openvino.runtime.op.util.Variable.info)

-
update(
*self:*,[openvino._pyopenvino.op.util.Variable](https://docs.openvino.ai#openvino.runtime.op.util.Variable)*variable_info:*) None[openvino._pyopenvino.op.util.VariableInfo](https://docs.openvino.ai/openvino.runtime.op.util.VariableInfo.html#openvino.runtime.op.util.VariableInfo)[#](https://docs.openvino.ai#openvino.runtime.op.util.Variable.update)

-
__init__(