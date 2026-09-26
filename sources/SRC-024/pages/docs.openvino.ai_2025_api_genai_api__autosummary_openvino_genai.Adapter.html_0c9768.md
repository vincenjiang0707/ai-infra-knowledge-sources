source: https://docs.openvino.ai/2025/api/genai_api/_autosummary/openvino_genai.Adapter.html
lastmod: 

# openvino_genai.Adapter[#](https://docs.openvino.ai#openvino-genai-adapter)

-
*class*openvino_genai.Adapter[#](https://docs.openvino.ai#openvino_genai.Adapter) Bases:

`pybind11_object`

Immutable LoRA Adapter that carries the adaptation matrices and serves as unique adapter identifier.

-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino_genai.Adapter.__init__) Overloaded function.

__init__(self: openvino_genai.py_openvino_genai.Adapter) -> None

__init__(self: openvino_genai.py_openvino_genai.Adapter, path: os.PathLike | str | bytes) -> None

Immutable LoRA Adapter that carries the adaptation matrices and serves as unique adapter identifier. path (os.PathLike): Path to adapter file in safetensors format.

__init__(self: openvino_genai.py_openvino_genai.Adapter, safetensor: openvino._pyopenvino.Tensor) -> None

Immutable LoRA Adapter that carries the adaptation matrices and serves as unique adapter identifier. safetensor (ov.Tensor): Pre-read LoRA Adapter safetensor.



Methods

(self)`__bool__`

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
*= {}*[#](https://docs.openvino.ai#openvino_genai.Adapter.__annotations__)

-
__bool__(
*self:*) bool[openvino_genai.py_openvino_genai.Adapter](https://docs.openvino.ai#openvino_genai.Adapter)[#](https://docs.openvino.ai#openvino_genai.Adapter.__bool__)

-
__class__
[#](https://docs.openvino.ai#openvino_genai.Adapter.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino_genai.Adapter.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino_genai.Adapter.__dir__) Default dir() implementation.


-
__eq__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.Adapter.__eq__) Return self==value.


-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino_genai.Adapter.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.Adapter.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino_genai.Adapter.__getattribute__) Return getattr(self, name).


-
__getstate__()
[#](https://docs.openvino.ai#openvino_genai.Adapter.__getstate__) Helper for pickle.


-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.Adapter.__gt__) Return self>value.


-
__hash__()
[#](https://docs.openvino.ai#openvino_genai.Adapter.__hash__) Return hash(self).


-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#id0) Overloaded function.

__init__(self: openvino_genai.py_openvino_genai.Adapter) -> None

__init__(self: openvino_genai.py_openvino_genai.Adapter, path: os.PathLike | str | bytes) -> None

Immutable LoRA Adapter that carries the adaptation matrices and serves as unique adapter identifier. path (os.PathLike): Path to adapter file in safetensors format.

__init__(self: openvino_genai.py_openvino_genai.Adapter, safetensor: openvino._pyopenvino.Tensor) -> None

Immutable LoRA Adapter that carries the adaptation matrices and serves as unique adapter identifier. safetensor (ov.Tensor): Pre-read LoRA Adapter safetensor.



-
__init_subclass__()
[#](https://docs.openvino.ai#openvino_genai.Adapter.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.Adapter.__le__) Return self<=value.


-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.Adapter.__lt__) Return self<value.


-
__ne__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.Adapter.__ne__) Return self!=value.


-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino_genai.Adapter.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino_genai.Adapter.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino_genai.Adapter.__reduce_ex__) Helper for pickle.


-
__repr__()
[#](https://docs.openvino.ai#openvino_genai.Adapter.__repr__) Return repr(self).


-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.Adapter.__setattr__) Implement setattr(self, name, value).


-
__sizeof__()
[#](https://docs.openvino.ai#openvino_genai.Adapter.__sizeof__) Size of object in memory, in bytes.


-
__str__()
[#](https://docs.openvino.ai#openvino_genai.Adapter.__str__) Return str(self).


-
__subclasshook__()
[#](https://docs.openvino.ai#openvino_genai.Adapter.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino_genai.Adapter._pybind11_conduit_v1_)

-
__init__(