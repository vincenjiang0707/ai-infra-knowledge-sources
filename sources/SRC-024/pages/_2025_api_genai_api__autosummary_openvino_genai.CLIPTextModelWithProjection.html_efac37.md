source: https://docs.openvino.ai/2025/api/genai_api/_autosummary/openvino_genai.CLIPTextModelWithProjection.html
lastmod: 

# openvino_genai.CLIPTextModelWithProjection[#](https://docs.openvino.ai#openvino-genai-cliptextmodelwithprojection)

-
*class*openvino_genai.CLIPTextModelWithProjection[#](https://docs.openvino.ai#openvino_genai.CLIPTextModelWithProjection) Bases:

`CLIPTextModel`

CLIPTextModelWithProjection class.

-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino_genai.CLIPTextModelWithProjection.__init__) Overloaded function.

__init__(self: openvino_genai.py_openvino_genai.CLIPTextModelWithProjection, root_dir: os.PathLike | str | bytes) -> None

CLIPTextModelWithProjection class root_dir (os.PathLike): Model root directory.

__init__(self: openvino_genai.py_openvino_genai.CLIPTextModelWithProjection, root_dir: os.PathLike | str | bytes, device: str,

[**](https://docs.openvino.ai#id1)kwargs) -> NoneCLIPTextModelWithProjection class root_dir (os.PathLike): Model root directory. device (str): Device on which inference will be done. kwargs: Device properties.

__init__(self: openvino_genai.py_openvino_genai.CLIPTextModelWithProjection, model: openvino_genai.py_openvino_genai.CLIPTextModelWithProjection) -> None


- CLIPText model
CLIPTextModelWithProjection class model (CLIPTextModelWithProjection): CLIPText model with projection



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
*class*Config[#](https://docs.openvino.ai#openvino_genai.CLIPTextModelWithProjection.Config) Bases:

`pybind11_object`

This class is used for storing CLIPTextModel config.

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino_genai.CLIPTextModelWithProjection.Config.__annotations__)

-
__class__
[#](https://docs.openvino.ai#openvino_genai.CLIPTextModelWithProjection.Config.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino_genai.CLIPTextModelWithProjection.Config.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino_genai.CLIPTextModelWithProjection.Config.__dir__) Default dir() implementation.


-
__eq__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.CLIPTextModelWithProjection.Config.__eq__) Return self==value.


-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino_genai.CLIPTextModelWithProjection.Config.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.CLIPTextModelWithProjection.Config.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino_genai.CLIPTextModelWithProjection.Config.__getattribute__) Return getattr(self, name).


-
__getstate__()
[#](https://docs.openvino.ai#openvino_genai.CLIPTextModelWithProjection.Config.__getstate__) Helper for pickle.


-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.CLIPTextModelWithProjection.Config.__gt__) Return self>value.


-
__hash__()
[#](https://docs.openvino.ai#openvino_genai.CLIPTextModelWithProjection.Config.__hash__) Return hash(self).


-
__init__(
*self:*,[openvino_genai.py_openvino_genai.CLIPTextModel.Config](https://docs.openvino.ai#openvino_genai.CLIPTextModelWithProjection.Config)*config_path: os.PathLike | str | bytes*) None[#](https://docs.openvino.ai#openvino_genai.CLIPTextModelWithProjection.Config.__init__)

-
__init_subclass__()
[#](https://docs.openvino.ai#openvino_genai.CLIPTextModelWithProjection.Config.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.CLIPTextModelWithProjection.Config.__le__) Return self<=value.


-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.CLIPTextModelWithProjection.Config.__lt__) Return self<value.


-
__ne__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.CLIPTextModelWithProjection.Config.__ne__) Return self!=value.


-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino_genai.CLIPTextModelWithProjection.Config.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino_genai.CLIPTextModelWithProjection.Config.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino_genai.CLIPTextModelWithProjection.Config.__reduce_ex__) Helper for pickle.


-
__repr__()
[#](https://docs.openvino.ai#openvino_genai.CLIPTextModelWithProjection.Config.__repr__) Return repr(self).


-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.CLIPTextModelWithProjection.Config.__setattr__) Implement setattr(self, name, value).


-
__sizeof__()
[#](https://docs.openvino.ai#openvino_genai.CLIPTextModelWithProjection.Config.__sizeof__) Size of object in memory, in bytes.


-
__str__()
[#](https://docs.openvino.ai#openvino_genai.CLIPTextModelWithProjection.Config.__str__) Return str(self).


-
__subclasshook__()
[#](https://docs.openvino.ai#openvino_genai.CLIPTextModelWithProjection.Config.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino_genai.CLIPTextModelWithProjection.Config._pybind11_conduit_v1_)

-
*property*max_position_embeddings[#](https://docs.openvino.ai#openvino_genai.CLIPTextModelWithProjection.Config.max_position_embeddings)

-
__annotations__

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino_genai.CLIPTextModelWithProjection.__annotations__)

-
__class__
[#](https://docs.openvino.ai#openvino_genai.CLIPTextModelWithProjection.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino_genai.CLIPTextModelWithProjection.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino_genai.CLIPTextModelWithProjection.__dir__) Default dir() implementation.


-
__eq__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.CLIPTextModelWithProjection.__eq__) Return self==value.


-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino_genai.CLIPTextModelWithProjection.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.CLIPTextModelWithProjection.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino_genai.CLIPTextModelWithProjection.__getattribute__) Return getattr(self, name).


-
__getstate__()
[#](https://docs.openvino.ai#openvino_genai.CLIPTextModelWithProjection.__getstate__) Helper for pickle.


-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.CLIPTextModelWithProjection.__gt__) Return self>value.


-
__hash__()
[#](https://docs.openvino.ai#openvino_genai.CLIPTextModelWithProjection.__hash__) Return hash(self).


-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#id0) Overloaded function.

__init__(self: openvino_genai.py_openvino_genai.CLIPTextModelWithProjection, root_dir: os.PathLike | str | bytes) -> None

CLIPTextModelWithProjection class root_dir (os.PathLike): Model root directory.

__init__(self: openvino_genai.py_openvino_genai.CLIPTextModelWithProjection, root_dir: os.PathLike | str | bytes, device: str,

[**](https://docs.openvino.ai#id3)kwargs) -> NoneCLIPTextModelWithProjection class root_dir (os.PathLike): Model root directory. device (str): Device on which inference will be done. kwargs: Device properties.

__init__(self: openvino_genai.py_openvino_genai.CLIPTextModelWithProjection, model: openvino_genai.py_openvino_genai.CLIPTextModelWithProjection) -> None


- CLIPText model
CLIPTextModelWithProjection class model (CLIPTextModelWithProjection): CLIPText model with projection



-
__init_subclass__()
[#](https://docs.openvino.ai#openvino_genai.CLIPTextModelWithProjection.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.CLIPTextModelWithProjection.__le__) Return self<=value.


-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.CLIPTextModelWithProjection.__lt__) Return self<value.


-
__ne__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.CLIPTextModelWithProjection.__ne__) Return self!=value.


-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino_genai.CLIPTextModelWithProjection.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino_genai.CLIPTextModelWithProjection.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino_genai.CLIPTextModelWithProjection.__reduce_ex__) Helper for pickle.


-
__repr__()
[#](https://docs.openvino.ai#openvino_genai.CLIPTextModelWithProjection.__repr__) Return repr(self).


-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.CLIPTextModelWithProjection.__setattr__) Implement setattr(self, name, value).


-
__sizeof__()
[#](https://docs.openvino.ai#openvino_genai.CLIPTextModelWithProjection.__sizeof__) Size of object in memory, in bytes.


-
__str__()
[#](https://docs.openvino.ai#openvino_genai.CLIPTextModelWithProjection.__str__) Return str(self).


-
__subclasshook__()
[#](https://docs.openvino.ai#openvino_genai.CLIPTextModelWithProjection.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino_genai.CLIPTextModelWithProjection._pybind11_conduit_v1_)

-
compile(
*self:*,[openvino_genai.py_openvino_genai.CLIPTextModel](https://docs.openvino.ai/openvino_genai.CLIPTextModel.html#openvino_genai.CLIPTextModel)*device: str*,***kwargs*) None[#](https://docs.openvino.ai#openvino_genai.CLIPTextModelWithProjection.compile) Compiles the model. device (str): Device to run the model on (e.g., CPU, GPU). kwargs: Device properties.


-
export_model(
*self:*,[openvino_genai.py_openvino_genai.CLIPTextModel](https://docs.openvino.ai/openvino_genai.CLIPTextModel.html#openvino_genai.CLIPTextModel)*export_path: os.PathLike | str | bytes*) None[#](https://docs.openvino.ai#openvino_genai.CLIPTextModelWithProjection.export_model) Exports compiled model to a specified directory. Can significantly reduce model load time, especially for large models. export_path (os.PathLike): A path to a directory to export compiled model to.

Use blob_path property to load previously exported models.


-
get_config(
*self:*)[openvino_genai.py_openvino_genai.CLIPTextModel](https://docs.openvino.ai/openvino_genai.CLIPTextModel.html#openvino_genai.CLIPTextModel)[openvino_genai.py_openvino_genai.CLIPTextModel.Config](https://docs.openvino.ai#openvino_genai.CLIPTextModelWithProjection.Config)[#](https://docs.openvino.ai#openvino_genai.CLIPTextModelWithProjection.get_config)

-
get_output_tensor(
*self:*,[openvino_genai.py_openvino_genai.CLIPTextModel](https://docs.openvino.ai/openvino_genai.CLIPTextModel.html#openvino_genai.CLIPTextModel)*idx: SupportsInt*)[openvino._pyopenvino.Tensor](https://docs.openvino.ai/ie_python_api/_autosummary/openvino.Tensor.html#openvino.Tensor)[#](https://docs.openvino.ai#openvino_genai.CLIPTextModelWithProjection.get_output_tensor)

-
infer(
*self:*,[openvino_genai.py_openvino_genai.CLIPTextModel](https://docs.openvino.ai/openvino_genai.CLIPTextModel.html#openvino_genai.CLIPTextModel)*pos_prompt: str*,*neg_prompt: str*,*do_classifier_free_guidance: bool*)[openvino._pyopenvino.Tensor](https://docs.openvino.ai/ie_python_api/_autosummary/openvino.Tensor.html#openvino.Tensor)[#](https://docs.openvino.ai#openvino_genai.CLIPTextModelWithProjection.infer)

-
reshape(
*self:*,[openvino_genai.py_openvino_genai.CLIPTextModel](https://docs.openvino.ai/openvino_genai.CLIPTextModel.html#openvino_genai.CLIPTextModel)*batch_size: SupportsInt*)[openvino_genai.py_openvino_genai.CLIPTextModel](https://docs.openvino.ai/openvino_genai.CLIPTextModel.html#openvino_genai.CLIPTextModel)[#](https://docs.openvino.ai#openvino_genai.CLIPTextModelWithProjection.reshape)

-
set_adapters(
*self:*,[openvino_genai.py_openvino_genai.CLIPTextModel](https://docs.openvino.ai/openvino_genai.CLIPTextModel.html#openvino_genai.CLIPTextModel)*adapters:*) None[openvino_genai.py_openvino_genai.AdapterConfig](https://docs.openvino.ai/openvino_genai.AdapterConfig.html#openvino_genai.AdapterConfig)| None[#](https://docs.openvino.ai#openvino_genai.CLIPTextModelWithProjection.set_adapters)

-
__init__(