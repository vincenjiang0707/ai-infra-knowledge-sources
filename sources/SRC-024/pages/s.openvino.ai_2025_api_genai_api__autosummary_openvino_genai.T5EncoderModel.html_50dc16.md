source: https://docs.openvino.ai/2025/api/genai_api/_autosummary/openvino_genai.T5EncoderModel.html
lastmod: 

# openvino_genai.T5EncoderModel[#](https://docs.openvino.ai#openvino-genai-t5encodermodel)

-
*class*openvino_genai.T5EncoderModel[#](https://docs.openvino.ai#openvino_genai.T5EncoderModel) Bases:

`pybind11_object`

T5EncoderModel class.

-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino_genai.T5EncoderModel.__init__) Overloaded function.

__init__(self: openvino_genai.py_openvino_genai.T5EncoderModel, root_dir: os.PathLike | str | bytes) -> None

T5EncoderModel class root_dir (os.PathLike): Model root directory.

__init__(self: openvino_genai.py_openvino_genai.T5EncoderModel, root_dir: os.PathLike | str | bytes, device: str,

[**](https://docs.openvino.ai#id1)kwargs) -> NoneT5EncoderModel class root_dir (os.PathLike): Model root directory. device (str): Device on which inference will be done. kwargs: Device properties.

__init__(self: openvino_genai.py_openvino_genai.T5EncoderModel, model: openvino_genai.py_openvino_genai.T5EncoderModel) -> None


- T5EncoderModel model
T5EncoderModel class model (T5EncoderModel): T5EncoderModel model



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

()`__repr__`

Return repr(self).

(name, value, /)`__setattr__`

Implement setattr(self, name, value).

Size of object in memory, in bytes.

()`__str__`

Return str(self).

Abstract classes can override this to customize issubclass().

(self, device, **kwargs)`compile`

Compiles the model.

(self, idx)`get_output_tensor`

(self, pos_prompt, neg_prompt, ...)`infer`

(self, batch_size, max_sequence_length)`reshape`

Attributes

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino_genai.T5EncoderModel.__annotations__)

-
__class__
[#](https://docs.openvino.ai#openvino_genai.T5EncoderModel.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino_genai.T5EncoderModel.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino_genai.T5EncoderModel.__dir__) Default dir() implementation.


-
__eq__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.T5EncoderModel.__eq__) Return self==value.


-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino_genai.T5EncoderModel.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.T5EncoderModel.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino_genai.T5EncoderModel.__getattribute__) Return getattr(self, name).


-
__getstate__()
[#](https://docs.openvino.ai#openvino_genai.T5EncoderModel.__getstate__) Helper for pickle.


-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.T5EncoderModel.__gt__) Return self>value.


-
__hash__()
[#](https://docs.openvino.ai#openvino_genai.T5EncoderModel.__hash__) Return hash(self).


-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#id0) Overloaded function.

__init__(self: openvino_genai.py_openvino_genai.T5EncoderModel, root_dir: os.PathLike | str | bytes) -> None

T5EncoderModel class root_dir (os.PathLike): Model root directory.

__init__(self: openvino_genai.py_openvino_genai.T5EncoderModel, root_dir: os.PathLike | str | bytes, device: str,

[**](https://docs.openvino.ai#id3)kwargs) -> NoneT5EncoderModel class root_dir (os.PathLike): Model root directory. device (str): Device on which inference will be done. kwargs: Device properties.

__init__(self: openvino_genai.py_openvino_genai.T5EncoderModel, model: openvino_genai.py_openvino_genai.T5EncoderModel) -> None


- T5EncoderModel model
T5EncoderModel class model (T5EncoderModel): T5EncoderModel model



-
__init_subclass__()
[#](https://docs.openvino.ai#openvino_genai.T5EncoderModel.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.T5EncoderModel.__le__) Return self<=value.


-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.T5EncoderModel.__lt__) Return self<value.


-
__ne__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.T5EncoderModel.__ne__) Return self!=value.


-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino_genai.T5EncoderModel.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino_genai.T5EncoderModel.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino_genai.T5EncoderModel.__reduce_ex__) Helper for pickle.


-
__repr__()
[#](https://docs.openvino.ai#openvino_genai.T5EncoderModel.__repr__) Return repr(self).


-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.T5EncoderModel.__setattr__) Implement setattr(self, name, value).


-
__sizeof__()
[#](https://docs.openvino.ai#openvino_genai.T5EncoderModel.__sizeof__) Size of object in memory, in bytes.


-
__str__()
[#](https://docs.openvino.ai#openvino_genai.T5EncoderModel.__str__) Return str(self).


-
__subclasshook__()
[#](https://docs.openvino.ai#openvino_genai.T5EncoderModel.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino_genai.T5EncoderModel._pybind11_conduit_v1_)

-
compile(
*self:*,[openvino_genai.py_openvino_genai.T5EncoderModel](https://docs.openvino.ai#openvino_genai.T5EncoderModel)*device: str*,***kwargs*) None[#](https://docs.openvino.ai#openvino_genai.T5EncoderModel.compile) Compiles the model. device (str): Device to run the model on (e.g., CPU, GPU). kwargs: Device properties.


-
get_output_tensor(
*self:*,[openvino_genai.py_openvino_genai.T5EncoderModel](https://docs.openvino.ai#openvino_genai.T5EncoderModel)*idx: SupportsInt*)[openvino._pyopenvino.Tensor](https://docs.openvino.ai/ie_python_api/_autosummary/openvino.Tensor.html#openvino.Tensor)[#](https://docs.openvino.ai#openvino_genai.T5EncoderModel.get_output_tensor)

-
infer(
*self:*,[openvino_genai.py_openvino_genai.T5EncoderModel](https://docs.openvino.ai#openvino_genai.T5EncoderModel)*pos_prompt: str*,*neg_prompt: str*,*do_classifier_free_guidance: bool*,*max_sequence_length: SupportsInt*)[openvino._pyopenvino.Tensor](https://docs.openvino.ai/ie_python_api/_autosummary/openvino.Tensor.html#openvino.Tensor)[#](https://docs.openvino.ai#openvino_genai.T5EncoderModel.infer)

-
reshape(
*self:*,[openvino_genai.py_openvino_genai.T5EncoderModel](https://docs.openvino.ai#openvino_genai.T5EncoderModel)*batch_size: SupportsInt*,*max_sequence_length: SupportsInt*)[openvino_genai.py_openvino_genai.T5EncoderModel](https://docs.openvino.ai#openvino_genai.T5EncoderModel)[#](https://docs.openvino.ai#openvino_genai.T5EncoderModel.reshape)

-
__init__(