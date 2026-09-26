source: https://docs.openvino.ai/2025/api/ie_python_api/_autosummary/openvino.runtime.op.util.SliceInputDescription.html
lastmod: 

# openvino.runtime.op.util.SliceInputDescription[#](https://docs.openvino.ai#openvino-runtime-op-util-sliceinputdescription)

-
*class*openvino.runtime.op.util.SliceInputDescription[#](https://docs.openvino.ai#openvino.runtime.op.util.SliceInputDescription) Bases:

`InputDescription`

openvino.impl.op.util.SliceInputDescription wraps ov::op::util::SliceInputDescription

-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino.runtime.op.util.SliceInputDescription.__init__) Overloaded function.

__init__(self: openvino._pyopenvino.op.util.SliceInputDescription) -> None

__init__(self: openvino._pyopenvino.op.util.SliceInputDescription, input_index: typing.SupportsInt, body_parameter_index: typing.SupportsInt, start: typing.SupportsInt, stride: typing.SupportsInt, part_size: typing.SupportsInt, end: typing.SupportsInt, axis: typing.SupportsInt) -> None



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
*= {}*[#](https://docs.openvino.ai#openvino.runtime.op.util.SliceInputDescription.__annotations__)

-
__class__
[#](https://docs.openvino.ai#openvino.runtime.op.util.SliceInputDescription.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.runtime.op.util.SliceInputDescription.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino.runtime.op.util.SliceInputDescription.__dir__) Default dir() implementation.


-
__eq__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.runtime.op.util.SliceInputDescription.__eq__) Return self==value.


-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino.runtime.op.util.SliceInputDescription.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.runtime.op.util.SliceInputDescription.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino.runtime.op.util.SliceInputDescription.__getattribute__) Return getattr(self, name).


-
__getstate__()
[#](https://docs.openvino.ai#openvino.runtime.op.util.SliceInputDescription.__getstate__) Helper for pickle.


-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.runtime.op.util.SliceInputDescription.__gt__) Return self>value.


-
__hash__()
[#](https://docs.openvino.ai#openvino.runtime.op.util.SliceInputDescription.__hash__) Return hash(self).


-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#id0) Overloaded function.

__init__(self: openvino._pyopenvino.op.util.SliceInputDescription) -> None

__init__(self: openvino._pyopenvino.op.util.SliceInputDescription, input_index: typing.SupportsInt, body_parameter_index: typing.SupportsInt, start: typing.SupportsInt, stride: typing.SupportsInt, part_size: typing.SupportsInt, end: typing.SupportsInt, axis: typing.SupportsInt) -> None



-
__init_subclass__()
[#](https://docs.openvino.ai#openvino.runtime.op.util.SliceInputDescription.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.runtime.op.util.SliceInputDescription.__le__) Return self<=value.


-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.runtime.op.util.SliceInputDescription.__lt__) Return self<value.


-
__ne__(
*value*,*/*)[#](https://docs.openvino.ai#openvino.runtime.op.util.SliceInputDescription.__ne__) Return self!=value.


-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino.runtime.op.util.SliceInputDescription.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino.runtime.op.util.SliceInputDescription.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino.runtime.op.util.SliceInputDescription.__reduce_ex__) Helper for pickle.


-
__repr__(
*self:*) str[openvino._pyopenvino.op.util.SliceInputDescription](https://docs.openvino.ai#openvino.runtime.op.util.SliceInputDescription)[#](https://docs.openvino.ai#openvino.runtime.op.util.SliceInputDescription.__repr__)

-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino.runtime.op.util.SliceInputDescription.__setattr__) Implement setattr(self, name, value).


-
__sizeof__()
[#](https://docs.openvino.ai#openvino.runtime.op.util.SliceInputDescription.__sizeof__) Size of object in memory, in bytes.


-
__str__()
[#](https://docs.openvino.ai#openvino.runtime.op.util.SliceInputDescription.__str__) Return str(self).


-
__subclasshook__()
[#](https://docs.openvino.ai#openvino.runtime.op.util.SliceInputDescription.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino.runtime.op.util.SliceInputDescription._pybind11_conduit_v1_)

-
*property*axis[#](https://docs.openvino.ai#openvino.runtime.op.util.SliceInputDescription.axis)

-
*property*body_parameter_index[#](https://docs.openvino.ai#openvino.runtime.op.util.SliceInputDescription.body_parameter_index)

-
copy(
*self:*) openvino._pyopenvino.op.util.InputDescription[openvino._pyopenvino.op.util.SliceInputDescription](https://docs.openvino.ai#openvino.runtime.op.util.SliceInputDescription)[#](https://docs.openvino.ai#openvino.runtime.op.util.SliceInputDescription.copy)

-
*property*end[#](https://docs.openvino.ai#openvino.runtime.op.util.SliceInputDescription.end)

-
get_type_info(
*self:*)[openvino._pyopenvino.op.util.SliceInputDescription](https://docs.openvino.ai#openvino.runtime.op.util.SliceInputDescription)[openvino._pyopenvino.DiscreteTypeInfo](https://docs.openvino.ai/openvino.DiscreteTypeInfo.html#openvino.DiscreteTypeInfo)[#](https://docs.openvino.ai#openvino.runtime.op.util.SliceInputDescription.get_type_info)

-
*property*input_index[#](https://docs.openvino.ai#openvino.runtime.op.util.SliceInputDescription.input_index)

-
*property*part_size[#](https://docs.openvino.ai#openvino.runtime.op.util.SliceInputDescription.part_size)

-
*property*start[#](https://docs.openvino.ai#openvino.runtime.op.util.SliceInputDescription.start)

-
*property*stride[#](https://docs.openvino.ai#openvino.runtime.op.util.SliceInputDescription.stride)

-
__init__(