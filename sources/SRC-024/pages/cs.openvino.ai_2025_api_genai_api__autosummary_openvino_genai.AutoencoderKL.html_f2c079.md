source: https://docs.openvino.ai/2025/api/genai_api/_autosummary/openvino_genai.AutoencoderKL.html
lastmod: 

# openvino_genai.AutoencoderKL[#](https://docs.openvino.ai#openvino-genai-autoencoderkl)

-
*class*openvino_genai.AutoencoderKL[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL) Bases:

`pybind11_object`

AutoencoderKL class.

-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL.__init__) Overloaded function.

__init__(self: openvino_genai.py_openvino_genai.AutoencoderKL, vae_decoder_path: os.PathLike | str | bytes) -> None

AutoencoderKL class initialized only with decoder model. vae_decoder_path (os.PathLike): VAE decoder directory.

__init__(self: openvino_genai.py_openvino_genai.AutoencoderKL, vae_encoder_path: os.PathLike | str | bytes, vae_decoder_path: os.PathLike | str | bytes) -> None

AutoencoderKL class initialized with both encoder and decoder models. vae_encoder_path (os.PathLike): VAE encoder directory. vae_decoder_path (os.PathLike): VAE decoder directory.

__init__(self: openvino_genai.py_openvino_genai.AutoencoderKL, vae_decoder_path: os.PathLike | str | bytes, device: str,

[**](https://docs.openvino.ai#id1)kwargs) -> NoneAutoencoderKL class initialized only with decoder model. vae_decoder_path (os.PathLike): VAE decoder directory. device (str): Device on which inference will be done. kwargs: Device properties.

__init__(self: openvino_genai.py_openvino_genai.AutoencoderKL, vae_encoder_path: os.PathLike | str | bytes, vae_decoder_path: os.PathLike | str | bytes, device: str,

[**](https://docs.openvino.ai#id3)kwargs) -> NoneAutoencoderKL class initialized only with both encoder and decoder models. vae_encoder_path (os.PathLike): VAE encoder directory. vae_decoder_path (os.PathLike): VAE decoder directory. device (str): Device on which inference will be done. kwargs: Device properties.

__init__(self: openvino_genai.py_openvino_genai.AutoencoderKL, model: openvino_genai.py_openvino_genai.AutoencoderKL) -> None


- AutoencoderKL model
AutoencoderKL class. model (AutoencoderKL): AutoencoderKL model.



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

device on which inference will be done

(self, latent)`decode`

(self, image, generator)`encode`

(self, export_path)`export_model`

Exports compiled models to a specified directory.

(self)`get_config`

(self)`get_vae_scale_factor`

(self, batch_size, height, width)`reshape`

Attributes

-
*class*Config[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL.Config) Bases:

`pybind11_object`

This class is used for storing AutoencoderKL config.

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL.Config.__annotations__)

-
__class__
[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL.Config.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL.Config.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL.Config.__dir__) Default dir() implementation.


-
__eq__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL.Config.__eq__) Return self==value.


-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL.Config.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL.Config.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL.Config.__getattribute__) Return getattr(self, name).


-
__getstate__()
[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL.Config.__getstate__) Helper for pickle.


-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL.Config.__gt__) Return self>value.


-
__hash__()
[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL.Config.__hash__) Return hash(self).


-
__init__(
*self:*,[openvino_genai.py_openvino_genai.AutoencoderKL.Config](https://docs.openvino.ai#openvino_genai.AutoencoderKL.Config)*config_path: os.PathLike | str | bytes*) None[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL.Config.__init__)

-
__init_subclass__()
[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL.Config.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL.Config.__le__) Return self<=value.


-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL.Config.__lt__) Return self<value.


-
__ne__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL.Config.__ne__) Return self!=value.


-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL.Config.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL.Config.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL.Config.__reduce_ex__) Helper for pickle.


-
__repr__()
[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL.Config.__repr__) Return repr(self).


-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL.Config.__setattr__) Implement setattr(self, name, value).


-
__sizeof__()
[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL.Config.__sizeof__) Size of object in memory, in bytes.


-
__str__()
[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL.Config.__str__) Return str(self).


-
__subclasshook__()
[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL.Config.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL.Config._pybind11_conduit_v1_)

-
*property*block_out_channels[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL.Config.block_out_channels)

-
*property*in_channels[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL.Config.in_channels)

-
*property*latent_channels[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL.Config.latent_channels)

-
*property*out_channels[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL.Config.out_channels)

-
*property*scaling_factor[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL.Config.scaling_factor)

-
__annotations__

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL.__annotations__)

-
__class__
[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL.__dir__) Default dir() implementation.


-
__eq__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL.__eq__) Return self==value.


-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL.__getattribute__) Return getattr(self, name).


-
__getstate__()
[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL.__getstate__) Helper for pickle.


-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL.__gt__) Return self>value.


-
__hash__()
[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL.__hash__) Return hash(self).


-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#id0) Overloaded function.

__init__(self: openvino_genai.py_openvino_genai.AutoencoderKL, vae_decoder_path: os.PathLike | str | bytes) -> None

AutoencoderKL class initialized only with decoder model. vae_decoder_path (os.PathLike): VAE decoder directory.

__init__(self: openvino_genai.py_openvino_genai.AutoencoderKL, vae_encoder_path: os.PathLike | str | bytes, vae_decoder_path: os.PathLike | str | bytes) -> None

AutoencoderKL class initialized with both encoder and decoder models. vae_encoder_path (os.PathLike): VAE encoder directory. vae_decoder_path (os.PathLike): VAE decoder directory.

__init__(self: openvino_genai.py_openvino_genai.AutoencoderKL, vae_decoder_path: os.PathLike | str | bytes, device: str,

[**](https://docs.openvino.ai#id5)kwargs) -> NoneAutoencoderKL class initialized only with decoder model. vae_decoder_path (os.PathLike): VAE decoder directory. device (str): Device on which inference will be done. kwargs: Device properties.

__init__(self: openvino_genai.py_openvino_genai.AutoencoderKL, vae_encoder_path: os.PathLike | str | bytes, vae_decoder_path: os.PathLike | str | bytes, device: str,

[**](https://docs.openvino.ai#id7)kwargs) -> NoneAutoencoderKL class initialized only with both encoder and decoder models. vae_encoder_path (os.PathLike): VAE encoder directory. vae_decoder_path (os.PathLike): VAE decoder directory. device (str): Device on which inference will be done. kwargs: Device properties.

__init__(self: openvino_genai.py_openvino_genai.AutoencoderKL, model: openvino_genai.py_openvino_genai.AutoencoderKL) -> None


- AutoencoderKL model
AutoencoderKL class. model (AutoencoderKL): AutoencoderKL model.



-
__init_subclass__()
[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL.__le__) Return self<=value.


-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL.__lt__) Return self<value.


-
__ne__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL.__ne__) Return self!=value.


-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL.__reduce_ex__) Helper for pickle.


-
__repr__()
[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL.__repr__) Return repr(self).


-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL.__setattr__) Implement setattr(self, name, value).


-
__sizeof__()
[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL.__sizeof__) Size of object in memory, in bytes.


-
__str__()
[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL.__str__) Return str(self).


-
__subclasshook__()
[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL._pybind11_conduit_v1_)

-
compile(
*self:*,[openvino_genai.py_openvino_genai.AutoencoderKL](https://docs.openvino.ai#openvino_genai.AutoencoderKL)*device: str*,***kwargs*) None[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL.compile) - device on which inference will be done
Compiles the model. device (str): Device to run the model on (e.g., CPU, GPU). kwargs: Device properties.



-
decode(
*self:*,[openvino_genai.py_openvino_genai.AutoencoderKL](https://docs.openvino.ai#openvino_genai.AutoencoderKL)*latent:*)[openvino._pyopenvino.Tensor](https://docs.openvino.ai/ie_python_api/_autosummary/openvino.Tensor.html#openvino.Tensor)[openvino._pyopenvino.Tensor](https://docs.openvino.ai/ie_python_api/_autosummary/openvino.Tensor.html#openvino.Tensor)[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL.decode)

-
encode(
*self:*,[openvino_genai.py_openvino_genai.AutoencoderKL](https://docs.openvino.ai#openvino_genai.AutoencoderKL)*image:*,[openvino._pyopenvino.Tensor](https://docs.openvino.ai/ie_python_api/_autosummary/openvino.Tensor.html#openvino.Tensor)*generator:*)[openvino_genai.py_openvino_genai.Generator](https://docs.openvino.ai/openvino_genai.Generator.html#openvino_genai.Generator)[openvino._pyopenvino.Tensor](https://docs.openvino.ai/ie_python_api/_autosummary/openvino.Tensor.html#openvino.Tensor)[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL.encode)

-
export_model(
*self:*,[openvino_genai.py_openvino_genai.AutoencoderKL](https://docs.openvino.ai#openvino_genai.AutoencoderKL)*export_path: os.PathLike | str | bytes*) None[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL.export_model) Exports compiled models to a specified directory. Can significantly reduce model load time, especially for large models. export_path (os.PathLike): A path to a directory to export compiled models to.

Use blob_path property to load previously exported models.


-
get_config(
*self:*)[openvino_genai.py_openvino_genai.AutoencoderKL](https://docs.openvino.ai#openvino_genai.AutoencoderKL)[openvino_genai.py_openvino_genai.AutoencoderKL.Config](https://docs.openvino.ai#openvino_genai.AutoencoderKL.Config)[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL.get_config)

-
get_vae_scale_factor(
*self:*) int[openvino_genai.py_openvino_genai.AutoencoderKL](https://docs.openvino.ai#openvino_genai.AutoencoderKL)[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL.get_vae_scale_factor)

-
reshape(
*self:*,[openvino_genai.py_openvino_genai.AutoencoderKL](https://docs.openvino.ai#openvino_genai.AutoencoderKL)*batch_size: SupportsInt*,*height: SupportsInt*,*width: SupportsInt*)[openvino_genai.py_openvino_genai.AutoencoderKL](https://docs.openvino.ai#openvino_genai.AutoencoderKL)[#](https://docs.openvino.ai#openvino_genai.AutoencoderKL.reshape)

-
__init__(