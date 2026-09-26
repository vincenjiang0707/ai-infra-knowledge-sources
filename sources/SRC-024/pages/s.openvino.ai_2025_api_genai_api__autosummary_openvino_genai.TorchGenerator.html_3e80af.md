source: https://docs.openvino.ai/2025/api/genai_api/_autosummary/openvino_genai.TorchGenerator.html
lastmod: 

# openvino_genai.TorchGenerator[#](https://docs.openvino.ai#openvino-genai-torchgenerator)

-
*class*openvino_genai.TorchGenerator[#](https://docs.openvino.ai#openvino_genai.TorchGenerator) Bases:

`CppStdGenerator`

This class provides OpenVINO GenAI Generator wrapper for torch.Generator

-
__init__(
*self:*,[openvino_genai.py_openvino_genai.TorchGenerator](https://docs.openvino.ai#openvino_genai.TorchGenerator)*seed: SupportsInt*) None[#](https://docs.openvino.ai#openvino_genai.TorchGenerator.__init__)

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

(self, seed)`__init__`

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

(self)`next`

(self, shape)`randn_tensor`

(self, new_seed)`seed`

Attributes

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino_genai.TorchGenerator.__annotations__)

-
__class__
[#](https://docs.openvino.ai#openvino_genai.TorchGenerator.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino_genai.TorchGenerator.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino_genai.TorchGenerator.__dir__) Default dir() implementation.


-
__eq__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.TorchGenerator.__eq__) Return self==value.


-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino_genai.TorchGenerator.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.TorchGenerator.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino_genai.TorchGenerator.__getattribute__) Return getattr(self, name).


-
__getstate__()
[#](https://docs.openvino.ai#openvino_genai.TorchGenerator.__getstate__) Helper for pickle.


-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.TorchGenerator.__gt__) Return self>value.


-
__hash__()
[#](https://docs.openvino.ai#openvino_genai.TorchGenerator.__hash__) Return hash(self).


-
__init__(
*self:*,[openvino_genai.py_openvino_genai.TorchGenerator](https://docs.openvino.ai#openvino_genai.TorchGenerator)*seed: SupportsInt*) None[#](https://docs.openvino.ai#id0)

-
__init_subclass__()
[#](https://docs.openvino.ai#openvino_genai.TorchGenerator.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.TorchGenerator.__le__) Return self<=value.


-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.TorchGenerator.__lt__) Return self<value.


-
__ne__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.TorchGenerator.__ne__) Return self!=value.


-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino_genai.TorchGenerator.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino_genai.TorchGenerator.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino_genai.TorchGenerator.__reduce_ex__) Helper for pickle.


-
__repr__()
[#](https://docs.openvino.ai#openvino_genai.TorchGenerator.__repr__) Return repr(self).


-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.TorchGenerator.__setattr__) Implement setattr(self, name, value).


-
__sizeof__()
[#](https://docs.openvino.ai#openvino_genai.TorchGenerator.__sizeof__) Size of object in memory, in bytes.


-
__str__()
[#](https://docs.openvino.ai#openvino_genai.TorchGenerator.__str__) Return str(self).


-
__subclasshook__()
[#](https://docs.openvino.ai#openvino_genai.TorchGenerator.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino_genai.TorchGenerator._pybind11_conduit_v1_)

-
next(
*self:*) float[openvino_genai.py_openvino_genai.TorchGenerator](https://docs.openvino.ai#openvino_genai.TorchGenerator)[#](https://docs.openvino.ai#openvino_genai.TorchGenerator.next)

-
randn_tensor(
*self:*,[openvino_genai.py_openvino_genai.TorchGenerator](https://docs.openvino.ai#openvino_genai.TorchGenerator)*shape:*)[openvino._pyopenvino.Shape](https://docs.openvino.ai/ie_python_api/_autosummary/openvino.Shape.html#openvino.Shape)[openvino._pyopenvino.Tensor](https://docs.openvino.ai/ie_python_api/_autosummary/openvino.Tensor.html#openvino.Tensor)[#](https://docs.openvino.ai#openvino_genai.TorchGenerator.randn_tensor)

-
seed(
*self:*,[openvino_genai.py_openvino_genai.TorchGenerator](https://docs.openvino.ai#openvino_genai.TorchGenerator)*new_seed: SupportsInt*) None[#](https://docs.openvino.ai#openvino_genai.TorchGenerator.seed)

-
__init__(