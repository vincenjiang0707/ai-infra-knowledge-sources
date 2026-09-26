source: https://docs.openvino.ai/2025/api/genai_api/_autosummary/openvino_genai.CLIPTextModel.html
lastmod: 

# openvino_genai.CLIPTextModel[#](https://docs.openvino.ai#openvino-genai-cliptextmodel)

-
*class*openvino_genai.CLIPTextModel[#](https://docs.openvino.ai#openvino_genai.CLIPTextModel) Bases:

`pybind11_object`

CLIPTextModel class.

-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino_genai.CLIPTextModel.__init__) Overloaded function.

__init__(self: openvino_genai.py_openvino_genai.CLIPTextModel, root_dir: os.PathLike | str | bytes) -> None

CLIPTextModel class root_dir (os.PathLike): Model root directory.

__init__(self: openvino_genai.py_openvino_genai.CLIPTextModel, root_dir: os.PathLike | str | bytes, device: str,

[**](https://docs.openvino.ai#id1)kwargs) -> NoneCLIPTextModel class root_dir (os.PathLike): Model root directory. device (str): Device on which inference will be done. kwargs: Device properties.

__init__(self: openvino_genai.py_openvino_genai.CLIPTextModel, model: openvino_genai.py_openvino_genai.CLIPTextModel) -> None


- CLIPText model
CLIPTextModel class model (CLIPTextModel): CLIPText model



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

(self, export_path)`export_model`

Exports compiled model to a specified directory.

(self)`get_config`

(self, idx)`get_output_tensor`

(self, pos_prompt, neg_prompt, ...)`infer`

(self, batch_size)`reshape`

(self, adapters)`set_adapters`

Attributes

-
*class*Config[#](https://docs.openvino.ai#openvino_genai.CLIPTextModel.Config) Bases:

`pybind11_object`

This class is used for storing CLIPTextModel config.

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino_genai.CLIPTextModel.Config.__annotations__)

-
__class__
[#](https://docs.openvino.ai#openvino_genai.CLIPTextModel.Config.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino_genai.CLIPTextModel.Config.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino_genai.CLIPTextModel.Config.__dir__) Default dir() implementation.


-
__eq__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.CLIPTextModel.Config.__eq__) Return self==value.


-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino_genai.CLIPTextModel.Config.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.CLIPTextModel.Config.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino_genai.CLIPTextModel.Config.__getattribute__) Return getattr(self, name).


-
__getstate__()
[#](https://docs.openvino.ai#openvino_genai.CLIPTextModel.Config.__getstate__) Helper for pickle.


-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.CLIPTextModel.Config.__gt__) Return self>value.


-
__hash__()
[#](https://docs.openvino.ai#openvino_genai.CLIPTextModel.Config.__hash__) Return hash(self).


-
__init__(
*self:*,[openvino_genai.py_openvino_genai.CLIPTextModel.Config](https://docs.openvino.ai/openvino_genai.CLIPTextModelWithProjection.html#openvino_genai.CLIPTextModelWithProjection.Config)*config_path: os.PathLike | str | bytes*) None[#](https://docs.openvino.ai#openvino_genai.CLIPTextModel.Config.__init__)

-
__init_subclass__()
[#](https://docs.openvino.ai#openvino_genai.CLIPTextModel.Config.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.CLIPTextModel.Config.__le__) Return self<=value.


-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.CLIPTextModel.Config.__lt__) Return self<value.


-
__ne__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.CLIPTextModel.Config.__ne__) Return self!=value.


-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino_genai.CLIPTextModel.Config.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino_genai.CLIPTextModel.Config.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino_genai.CLIPTextModel.Config.__reduce_ex__) Helper for pickle.


-
__repr__()
[#](https://docs.openvino.ai#openvino_genai.CLIPTextModel.Config.__repr__) Return repr(self).


-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.CLIPTextModel.Config.__setattr__) Implement setattr(self, name, value).


-
__sizeof__()
[#](https://docs.openvino.ai#openvino_genai.CLIPTextModel.Config.__sizeof__) Size of object in memory, in bytes.


-
__str__()
[#](https://docs.openvino.ai#openvino_genai.CLIPTextModel.Config.__str__) Return str(self).


-
__subclasshook__()
[#](https://docs.openvino.ai#openvino_genai.CLIPTextModel.Config.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino_genai.CLIPTextModel.Config._pybind11_conduit_v1_)

-
*property*max_position_embeddings[#](https://docs.openvino.ai#openvino_genai.CLIPTextModel.Config.max_position_embeddings)

-
__annotations__

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino_genai.CLIPTextModel.__annotations__)

-
__class__
[#](https://docs.openvino.ai#openvino_genai.CLIPTextModel.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino_genai.CLIPTextModel.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino_genai.CLIPTextModel.__dir__) Default dir() implementation.


-
__eq__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.CLIPTextModel.__eq__) Return self==value.


-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino_genai.CLIPTextModel.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.CLIPTextModel.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino_genai.CLIPTextModel.__getattribute__) Return getattr(self, name).


-
__getstate__()
[#](https://docs.openvino.ai#openvino_genai.CLIPTextModel.__getstate__) Helper for pickle.


-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.CLIPTextModel.__gt__) Return self>value.


-
__hash__()
[#](https://docs.openvino.ai#openvino_genai.CLIPTextModel.__hash__) Return hash(self).


-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#id0) Overloaded function.

__init__(self: openvino_genai.py_openvino_genai.CLIPTextModel, root_dir: os.PathLike | str | bytes) -> None

CLIPTextModel class root_dir (os.PathLike): Model root directory.

__init__(self: openvino_genai.py_openvino_genai.CLIPTextModel, root_dir: os.PathLike | str | bytes, device: str,

[**](https://docs.openvino.ai#id3)kwargs) -> NoneCLIPTextModel class root_dir (os.PathLike): Model root directory. device (str): Device on which inference will be done. kwargs: Device properties.

__init__(self: openvino_genai.py_openvino_genai.CLIPTextModel, model: openvino_genai.py_openvino_genai.CLIPTextModel) -> None


- CLIPText model
CLIPTextModel class model (CLIPTextModel): CLIPText model



-
__init_subclass__()
[#](https://docs.openvino.ai#openvino_genai.CLIPTextModel.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.CLIPTextModel.__le__) Return self<=value.


-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.CLIPTextModel.__lt__) Return self<value.


-
__ne__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.CLIPTextModel.__ne__) Return self!=value.


-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino_genai.CLIPTextModel.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino_genai.CLIPTextModel.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino_genai.CLIPTextModel.__reduce_ex__) Helper for pickle.


-
__repr__()
[#](https://docs.openvino.ai#openvino_genai.CLIPTextModel.__repr__) Return repr(self).


-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.CLIPTextModel.__setattr__) Implement setattr(self, name, value).


-
__sizeof__()
[#](https://docs.openvino.ai#openvino_genai.CLIPTextModel.__sizeof__) Size of object in memory, in bytes.


-
__str__()
[#](https://docs.openvino.ai#openvino_genai.CLIPTextModel.__str__) Return str(self).


-
__subclasshook__()
[#](https://docs.openvino.ai#openvino_genai.CLIPTextModel.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino_genai.CLIPTextModel._pybind11_conduit_v1_)

-
compile(
*self:*,[openvino_genai.py_openvino_genai.CLIPTextModel](https://docs.openvino.ai#openvino_genai.CLIPTextModel)*device: str*,***kwargs*) None[#](https://docs.openvino.ai#openvino_genai.CLIPTextModel.compile) Compiles the model. device (str): Device to run the model on (e.g., CPU, GPU). kwargs: Device properties.


-
export_model(
*self:*,[openvino_genai.py_openvino_genai.CLIPTextModel](https://docs.openvino.ai#openvino_genai.CLIPTextModel)*export_path: os.PathLike | str | bytes*) None[#](https://docs.openvino.ai#openvino_genai.CLIPTextModel.export_model) Exports compiled model to a specified directory. Can significantly reduce model load time, especially for large models. export_path (os.PathLike): A path to a directory to export compiled model to.

Use blob_path property to load previously exported models.


-
get_config(
*self:*)[openvino_genai.py_openvino_genai.CLIPTextModel](https://docs.openvino.ai#openvino_genai.CLIPTextModel)[openvino_genai.py_openvino_genai.CLIPTextModel.Config](https://docs.openvino.ai/openvino_genai.CLIPTextModelWithProjection.html#openvino_genai.CLIPTextModelWithProjection.Config)[#](https://docs.openvino.ai#openvino_genai.CLIPTextModel.get_config)

-
get_output_tensor(
*self:*,[openvino_genai.py_openvino_genai.CLIPTextModel](https://docs.openvino.ai#openvino_genai.CLIPTextModel)*idx: SupportsInt*)[openvino._pyopenvino.Tensor](https://docs.openvino.ai/ie_python_api/_autosummary/openvino.Tensor.html#openvino.Tensor)[#](https://docs.openvino.ai#openvino_genai.CLIPTextModel.get_output_tensor)

-
infer(
*self:*,[openvino_genai.py_openvino_genai.CLIPTextModel](https://docs.openvino.ai#openvino_genai.CLIPTextModel)*pos_prompt: str*,*neg_prompt: str*,*do_classifier_free_guidance: bool*)[openvino._pyopenvino.Tensor](https://docs.openvino.ai/ie_python_api/_autosummary/openvino.Tensor.html#openvino.Tensor)[#](https://docs.openvino.ai#openvino_genai.CLIPTextModel.infer)

-
reshape(
*self:*,[openvino_genai.py_openvino_genai.CLIPTextModel](https://docs.openvino.ai#openvino_genai.CLIPTextModel)*batch_size: SupportsInt*)[openvino_genai.py_openvino_genai.CLIPTextModel](https://docs.openvino.ai#openvino_genai.CLIPTextModel)[#](https://docs.openvino.ai#openvino_genai.CLIPTextModel.reshape)

-
set_adapters(
*self:*,[openvino_genai.py_openvino_genai.CLIPTextModel](https://docs.openvino.ai#openvino_genai.CLIPTextModel)*adapters:*) None[openvino_genai.py_openvino_genai.AdapterConfig](https://docs.openvino.ai/openvino_genai.AdapterConfig.html#openvino_genai.AdapterConfig)| None[#](https://docs.openvino.ai#openvino_genai.CLIPTextModel.set_adapters)

-
__init__(