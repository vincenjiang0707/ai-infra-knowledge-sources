source: https://docs.openvino.ai/2025/api/genai_api/_autosummary/openvino_genai.UNet2DConditionModel.html
lastmod: 

# openvino_genai.UNet2DConditionModel[#](https://docs.openvino.ai#openvino-genai-unet2dconditionmodel)

-
*class*openvino_genai.UNet2DConditionModel[#](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel) Bases:

`pybind11_object`

UNet2DConditionModel class.

-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel.__init__) Overloaded function.

__init__(self: openvino_genai.py_openvino_genai.UNet2DConditionModel, root_dir: os.PathLike | str | bytes) -> None

UNet2DConditionModel class root_dir (os.PathLike): Model root directory.

__init__(self: openvino_genai.py_openvino_genai.UNet2DConditionModel, root_dir: os.PathLike | str | bytes, device: str,

[**](https://docs.openvino.ai#id1)kwargs) -> NoneUNet2DConditionModel class root_dir (os.PathLike): Model root directory. device (str): Device on which inference will be done. kwargs: Device properties.

__init__(self: openvino_genai.py_openvino_genai.UNet2DConditionModel, model: openvino_genai.py_openvino_genai.UNet2DConditionModel) -> None


- UNet2DConditionModel model
UNet2DConditionModel class model (UNet2DConditionModel): UNet2DConditionModel model



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

(self, guidance_scale)`do_classifier_free_guidance`

(self, export_path)`export_model`

Exports compiled model to a specified directory.

(self)`get_config`

(self, sample, timestep)`infer`

(self, batch_size, height, width, ...)`reshape`

(self, adapters)`set_adapters`

(self, tensor_name, ...)`set_hidden_states`

Attributes

-
*class*Config[#](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel.Config) Bases:

`pybind11_object`

This class is used for storing UNet2DConditionModel config.

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel.Config.__annotations__)

-
__class__
[#](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel.Config.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel.Config.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel.Config.__dir__) Default dir() implementation.


-
__eq__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel.Config.__eq__) Return self==value.


-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel.Config.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel.Config.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel.Config.__getattribute__) Return getattr(self, name).


-
__getstate__()
[#](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel.Config.__getstate__) Helper for pickle.


-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel.Config.__gt__) Return self>value.


-
__hash__()
[#](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel.Config.__hash__) Return hash(self).


-
__init__(
*self:*,[openvino_genai.py_openvino_genai.UNet2DConditionModel.Config](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel.Config)*config_path: os.PathLike | str | bytes*) None[#](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel.Config.__init__)

-
__init_subclass__()
[#](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel.Config.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel.Config.__le__) Return self<=value.


-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel.Config.__lt__) Return self<value.


-
__ne__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel.Config.__ne__) Return self!=value.


-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel.Config.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel.Config.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel.Config.__reduce_ex__) Helper for pickle.


-
__repr__()
[#](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel.Config.__repr__) Return repr(self).


-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel.Config.__setattr__) Implement setattr(self, name, value).


-
__sizeof__()
[#](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel.Config.__sizeof__) Size of object in memory, in bytes.


-
__str__()
[#](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel.Config.__str__) Return str(self).


-
__subclasshook__()
[#](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel.Config.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel.Config._pybind11_conduit_v1_)

-
*property*in_channels[#](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel.Config.in_channels)

-
*property*sample_size[#](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel.Config.sample_size)

-
*property*time_cond_proj_dim[#](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel.Config.time_cond_proj_dim)

-
__annotations__

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel.__annotations__)

-
__class__
[#](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel.__dir__) Default dir() implementation.


-
__eq__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel.__eq__) Return self==value.


-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel.__getattribute__) Return getattr(self, name).


-
__getstate__()
[#](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel.__getstate__) Helper for pickle.


-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel.__gt__) Return self>value.


-
__hash__()
[#](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel.__hash__) Return hash(self).


-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#id0) Overloaded function.

__init__(self: openvino_genai.py_openvino_genai.UNet2DConditionModel, root_dir: os.PathLike | str | bytes) -> None

UNet2DConditionModel class root_dir (os.PathLike): Model root directory.

__init__(self: openvino_genai.py_openvino_genai.UNet2DConditionModel, root_dir: os.PathLike | str | bytes, device: str,

[**](https://docs.openvino.ai#id3)kwargs) -> NoneUNet2DConditionModel class root_dir (os.PathLike): Model root directory. device (str): Device on which inference will be done. kwargs: Device properties.

__init__(self: openvino_genai.py_openvino_genai.UNet2DConditionModel, model: openvino_genai.py_openvino_genai.UNet2DConditionModel) -> None


- UNet2DConditionModel model
UNet2DConditionModel class model (UNet2DConditionModel): UNet2DConditionModel model



-
__init_subclass__()
[#](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel.__le__) Return self<=value.


-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel.__lt__) Return self<value.


-
__ne__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel.__ne__) Return self!=value.


-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel.__reduce_ex__) Helper for pickle.


-
__repr__()
[#](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel.__repr__) Return repr(self).


-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel.__setattr__) Implement setattr(self, name, value).


-
__sizeof__()
[#](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel.__sizeof__) Size of object in memory, in bytes.


-
__str__()
[#](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel.__str__) Return str(self).


-
__subclasshook__()
[#](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel._pybind11_conduit_v1_)

-
compile(
*self:*,[openvino_genai.py_openvino_genai.UNet2DConditionModel](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel)*device: str*,***kwargs*) None[#](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel.compile) Compiles the model. device (str): Device to run the model on (e.g., CPU, GPU). kwargs: Device properties.


-
do_classifier_free_guidance(
*self:*,[openvino_genai.py_openvino_genai.UNet2DConditionModel](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel)*guidance_scale: SupportsFloat*) bool[#](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel.do_classifier_free_guidance)

-
export_model(
*self:*,[openvino_genai.py_openvino_genai.UNet2DConditionModel](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel)*export_path: os.PathLike | str | bytes*) None[#](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel.export_model) Exports compiled model to a specified directory. Can significantly reduce model load time, especially for large models. export_path (os.PathLike): A path to a directory to export compiled model to.

Use blob_path property to load previously exported models.


-
get_config(
*self:*)[openvino_genai.py_openvino_genai.UNet2DConditionModel](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel)[openvino_genai.py_openvino_genai.UNet2DConditionModel.Config](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel.Config)[#](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel.get_config)

-
infer(
*self:*,[openvino_genai.py_openvino_genai.UNet2DConditionModel](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel)*sample:*,[openvino._pyopenvino.Tensor](https://docs.openvino.ai/ie_python_api/_autosummary/openvino.Tensor.html#openvino.Tensor)*timestep:*)[openvino._pyopenvino.Tensor](https://docs.openvino.ai/ie_python_api/_autosummary/openvino.Tensor.html#openvino.Tensor)[openvino._pyopenvino.Tensor](https://docs.openvino.ai/ie_python_api/_autosummary/openvino.Tensor.html#openvino.Tensor)[#](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel.infer)

-
reshape(
*self:*,[openvino_genai.py_openvino_genai.UNet2DConditionModel](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel)*batch_size: SupportsInt*,*height: SupportsInt*,*width: SupportsInt*,*tokenizer_model_max_length: SupportsInt*)[openvino_genai.py_openvino_genai.UNet2DConditionModel](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel)[#](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel.reshape)

-
set_adapters(
*self:*,[openvino_genai.py_openvino_genai.UNet2DConditionModel](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel)*adapters:*) None[openvino_genai.py_openvino_genai.AdapterConfig](https://docs.openvino.ai/openvino_genai.AdapterConfig.html#openvino_genai.AdapterConfig)| None[#](https://docs.openvino.ai#openvino_genai.UNet2DConditionModel.set_adapters)

-
__init__(