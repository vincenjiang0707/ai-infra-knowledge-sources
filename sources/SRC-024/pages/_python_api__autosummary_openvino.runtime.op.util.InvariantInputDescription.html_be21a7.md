source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.op.util.InvariantInputDescription.html
lastmod: 

# openvino.runtime.op.util.InvariantInputDescription[#](https://docs.openvino.ai#openvino-runtime-op-util-invariantinputdescription)

-
*class*openvino.runtime.op.util.InvariantInputDescription[#](https://docs.openvino.ai#openvino.runtime.op.util.InvariantInputDescription) Bases:

`InputDescription`

openvino.impl.op.util.InvariantInputDescription wraps ov::op::util::InvariantInputDescription

-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.runtime.op.util.InvariantInputDescription.__init__) Overloaded function.

__init__(self: openvino._pyopenvino.op.util.InvariantInputDescription) -> None

__init__(self: openvino._pyopenvino.op.util.InvariantInputDescription, input_index: typing.SupportsInt, body_parameter_index: typing.SupportsInt) -> None



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

(self)`copy`

(self)`get_type_info`

Attributes

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino.runtime.op.util.InvariantInputDescription.__annotations__)

-
__class__
[#](https://docs.openvino.ai#openvino.runtime.op.util.InvariantInputDescription.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.runtime.op.util.InvariantInputDescription.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino.runtime.op.util.InvariantInputDescription.__dir__) Default dir() implementation.


-
__eq__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.runtime.op.util.InvariantInputDescription.__eq__) Return self==value.


-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino.runtime.op.util.InvariantInputDescription.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.runtime.op.util.InvariantInputDescription.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.runtime.op.util.InvariantInputDescription.__getattribute__) Return getattr(self, name).


-
__getstate__()
[#](https://docs.openvino.ai#openvino.runtime.op.util.InvariantInputDescription.__getstate__) Helper for pickle.


-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.runtime.op.util.InvariantInputDescription.__gt__) Return self>value.


-
__hash__()
[#](https://docs.openvino.ai#openvino.runtime.op.util.InvariantInputDescription.__hash__) Return hash(self).


-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#id0) Overloaded function.

__init__(self: openvino._pyopenvino.op.util.InvariantInputDescription) -> None

__init__(self: openvino._pyopenvino.op.util.InvariantInputDescription, input_index: typing.SupportsInt, body_parameter_index: typing.SupportsInt) -> None



-
__init_subclass__()
[#](https://docs.openvino.ai#openvino.runtime.op.util.InvariantInputDescription.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.runtime.op.util.InvariantInputDescription.__le__) Return self<=value.


-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.runtime.op.util.InvariantInputDescription.__lt__) Return self<value.


-
__ne__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.runtime.op.util.InvariantInputDescription.__ne__) Return self!=value.


-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino.runtime.op.util.InvariantInputDescription.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino.runtime.op.util.InvariantInputDescription.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino.runtime.op.util.InvariantInputDescription.__reduce_ex__) Helper for pickle.


-
__repr__(
*self:*) str[openvino._pyopenvino.op.util.InvariantInputDescription](https://docs.openvino.ai#openvino.runtime.op.util.InvariantInputDescription)[#](https://docs.openvino.ai#openvino.runtime.op.util.InvariantInputDescription.__repr__)

-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino.runtime.op.util.InvariantInputDescription.__setattr__) Implement setattr(self, name, value).


-
__sizeof__()
[#](https://docs.openvino.ai#openvino.runtime.op.util.InvariantInputDescription.__sizeof__) Size of object in memory, in bytes.


-
__str__()
[#](https://docs.openvino.ai#openvino.runtime.op.util.InvariantInputDescription.__str__) Return str(self).


-
__subclasshook__()
[#](https://docs.openvino.ai#openvino.runtime.op.util.InvariantInputDescription.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino.runtime.op.util.InvariantInputDescription._pybind11_conduit_v1_)

-
*property*body_parameter_index[#](https://docs.openvino.ai#openvino.runtime.op.util.InvariantInputDescription.body_parameter_index)

-
copy(
*self:*) openvino._pyopenvino.op.util.InputDescription[openvino._pyopenvino.op.util.InvariantInputDescription](https://docs.openvino.ai#openvino.runtime.op.util.InvariantInputDescription)[#](https://docs.openvino.ai#openvino.runtime.op.util.InvariantInputDescription.copy)

-
get_type_info(
*self:*)[openvino._pyopenvino.op.util.InvariantInputDescription](https://docs.openvino.ai#openvino.runtime.op.util.InvariantInputDescription)[openvino._pyopenvino.DiscreteTypeInfo](https://docs.openvino.ai/openvino.DiscreteTypeInfo.html#openvino.DiscreteTypeInfo)[#](https://docs.openvino.ai#openvino.runtime.op.util.InvariantInputDescription.get_type_info)

-
*property*input_index[#](https://docs.openvino.ai#openvino.runtime.op.util.InvariantInputDescription.input_index)

-
__init__(