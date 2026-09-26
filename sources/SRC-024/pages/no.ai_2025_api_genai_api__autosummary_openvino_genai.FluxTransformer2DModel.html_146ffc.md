source: https://docs.openvino.ai/2025/api/genai_api/_autosummary/openvino_genai.FluxTransformer2DModel.html
lastmod: 

# openvino_genai.FluxTransformer2DModel[#](https://docs.openvino.ai#openvino-genai-fluxtransformer2dmodel)

-
*class*openvino_genai.FluxTransformer2DModel[#](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel) Bases:

`pybind11_object`

FluxTransformer2DModel class.

-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel.__init__) Overloaded function.

__init__(self: openvino_genai.py_openvino_genai.FluxTransformer2DModel, root_dir: os.PathLike | str | bytes) -> None

FluxTransformer2DModel class root_dir (os.PathLike): Model root directory.

__init__(self: openvino_genai.py_openvino_genai.FluxTransformer2DModel, root_dir: os.PathLike | str | bytes, device: str,

[**](https://docs.openvino.ai#id1)kwargs) -> NoneUNet2DConditionModel class root_dir (os.PathLike): Model root directory. device (str): Device on which inference will be done. kwargs: Device properties.

__init__(self: openvino_genai.py_openvino_genai.FluxTransformer2DModel, model: openvino_genai.py_openvino_genai.FluxTransformer2DModel) -> None


- FluxTransformer2DModel model
FluxTransformer2DModel class model (FluxTransformer2DModel): FluxTransformer2DModel model



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

(self)`get_config`

(self, latent, timestep)`infer`

(self, batch_size, height, width, ...)`reshape`

(self, tensor_name, ...)`set_hidden_states`

Attributes

-
*class*Config[#](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel.Config) Bases:

`pybind11_object`

This class is used for storing FluxTransformer2DModel config.

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel.Config.__annotations__)

-
__class__
[#](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel.Config.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel.Config.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel.Config.__dir__) Default dir() implementation.


-
__eq__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel.Config.__eq__) Return self==value.


-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel.Config.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel.Config.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel.Config.__getattribute__) Return getattr(self, name).


-
__getstate__()
[#](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel.Config.__getstate__) Helper for pickle.


-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel.Config.__gt__) Return self>value.


-
__hash__()
[#](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel.Config.__hash__) Return hash(self).


-
__init__(
*self:*,[openvino_genai.py_openvino_genai.FluxTransformer2DModel.Config](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel.Config)*config_path: os.PathLike | str | bytes*) None[#](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel.Config.__init__)

-
__init_subclass__()
[#](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel.Config.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel.Config.__le__) Return self<=value.


-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel.Config.__lt__) Return self<value.


-
__ne__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel.Config.__ne__) Return self!=value.


-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel.Config.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel.Config.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel.Config.__reduce_ex__) Helper for pickle.


-
__repr__()
[#](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel.Config.__repr__) Return repr(self).


-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel.Config.__setattr__) Implement setattr(self, name, value).


-
__sizeof__()
[#](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel.Config.__sizeof__) Size of object in memory, in bytes.


-
__str__()
[#](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel.Config.__str__) Return str(self).


-
__subclasshook__()
[#](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel.Config.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel.Config._pybind11_conduit_v1_)

-
*property*default_sample_size[#](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel.Config.default_sample_size)

-
*property*in_channels[#](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel.Config.in_channels)

-
__annotations__

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel.__annotations__)

-
__class__
[#](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel.__dir__) Default dir() implementation.


-
__eq__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel.__eq__) Return self==value.


-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel.__getattribute__) Return getattr(self, name).


-
__getstate__()
[#](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel.__getstate__) Helper for pickle.


-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel.__gt__) Return self>value.


-
__hash__()
[#](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel.__hash__) Return hash(self).


-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#id0) Overloaded function.

__init__(self: openvino_genai.py_openvino_genai.FluxTransformer2DModel, root_dir: os.PathLike | str | bytes) -> None

FluxTransformer2DModel class root_dir (os.PathLike): Model root directory.

__init__(self: openvino_genai.py_openvino_genai.FluxTransformer2DModel, root_dir: os.PathLike | str | bytes, device: str,

[**](https://docs.openvino.ai#id3)kwargs) -> NoneUNet2DConditionModel class root_dir (os.PathLike): Model root directory. device (str): Device on which inference will be done. kwargs: Device properties.

__init__(self: openvino_genai.py_openvino_genai.FluxTransformer2DModel, model: openvino_genai.py_openvino_genai.FluxTransformer2DModel) -> None


- FluxTransformer2DModel model
FluxTransformer2DModel class model (FluxTransformer2DModel): FluxTransformer2DModel model



-
__init_subclass__()
[#](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel.__le__) Return self<=value.


-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel.__lt__) Return self<value.


-
__ne__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel.__ne__) Return self!=value.


-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel.__reduce_ex__) Helper for pickle.


-
__repr__()
[#](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel.__repr__) Return repr(self).


-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel.__setattr__) Implement setattr(self, name, value).


-
__sizeof__()
[#](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel.__sizeof__) Size of object in memory, in bytes.


-
__str__()
[#](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel.__str__) Return str(self).


-
__subclasshook__()
[#](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel._pybind11_conduit_v1_)

-
compile(
*self:*,[openvino_genai.py_openvino_genai.FluxTransformer2DModel](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel)*device: str*,***kwargs*) None[#](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel.compile) Compiles the model. device (str): Device to run the model on (e.g., CPU, GPU). kwargs: Device properties.


-
get_config(
*self:*)[openvino_genai.py_openvino_genai.FluxTransformer2DModel](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel)[openvino_genai.py_openvino_genai.FluxTransformer2DModel.Config](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel.Config)[#](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel.get_config)

-
infer(
*self:*,[openvino_genai.py_openvino_genai.FluxTransformer2DModel](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel)*latent:*,[openvino._pyopenvino.Tensor](https://docs.openvino.ai/ie_python_api/_autosummary/openvino.Tensor.html#openvino.Tensor)*timestep:*)[openvino._pyopenvino.Tensor](https://docs.openvino.ai/ie_python_api/_autosummary/openvino.Tensor.html#openvino.Tensor)[openvino._pyopenvino.Tensor](https://docs.openvino.ai/ie_python_api/_autosummary/openvino.Tensor.html#openvino.Tensor)[#](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel.infer)

-
reshape(
*self:*,[openvino_genai.py_openvino_genai.FluxTransformer2DModel](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel)*batch_size: SupportsInt*,*height: SupportsInt*,*width: SupportsInt*,*tokenizer_model_max_length: SupportsInt*)[openvino_genai.py_openvino_genai.FluxTransformer2DModel](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel)[#](https://docs.openvino.ai#openvino_genai.FluxTransformer2DModel.reshape)

-
__init__(