source: https://docs.openvino.ai/2025/api/genai_api/_autosummary/openvino_genai.Text2ImagePipeline.html
lastmod: 

# openvino_genai.Text2ImagePipeline[#](https://docs.openvino.ai#openvino-genai-text2imagepipeline)

-
*class*openvino_genai.Text2ImagePipeline[#](https://docs.openvino.ai#openvino_genai.Text2ImagePipeline) Bases:

`pybind11_object`

This class is used for generation with text-to-image models.

-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino_genai.Text2ImagePipeline.__init__) Overloaded function.

__init__(self: openvino_genai.py_openvino_genai.Text2ImagePipeline, models_path: os.PathLike | str | bytes) -> None

Text2ImagePipeline class constructor. models_path (os.PathLike): Path to the folder with exported model files.

__init__(self: openvino_genai.py_openvino_genai.Text2ImagePipeline, models_path: os.PathLike | str | bytes, device: str,

[**](https://docs.openvino.ai#id1)kwargs) -> NoneText2ImagePipeline class constructor. models_path (os.PathLike): Path with exported model files. device (str): Device to run the model on (e.g., CPU, GPU). kwargs: Text2ImagePipeline properties

__init__(self: openvino_genai.py_openvino_genai.Text2ImagePipeline, pipe: openvino_genai.py_openvino_genai.Image2ImagePipeline) -> None

__init__(self: openvino_genai.py_openvino_genai.Text2ImagePipeline, pipe: openvino_genai.py_openvino_genai.InpaintingPipeline) -> None



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

(*args, **kwargs)`compile`

Overloaded function.

(self, latent)`decode`

(self, export_path)`export_model`

Exports compiled models to a specified directory.

(scheduler, clip_text_model, ...)`flux`

(self, prompt, **kwargs)`generate`

Generates images for text-to-image models.

(self)`get_generation_config`

(self)`get_performance_metrics`

(scheduler, ...)`latent_consistency_model`

(self, num_images_per_prompt, height, ...)`reshape`

(self, config)`set_generation_config`

(self, scheduler)`set_scheduler`

(scheduler, clip_text_model, ...)`stable_diffusion`

(*args, **kwargs)`stable_diffusion_3`

Overloaded function.

(scheduler, ...)`stable_diffusion_xl`

Attributes

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino_genai.Text2ImagePipeline.__annotations__)

-
__class__
[#](https://docs.openvino.ai#openvino_genai.Text2ImagePipeline.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino_genai.Text2ImagePipeline.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino_genai.Text2ImagePipeline.__dir__) Default dir() implementation.


-
__eq__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.Text2ImagePipeline.__eq__) Return self==value.


-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino_genai.Text2ImagePipeline.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.Text2ImagePipeline.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino_genai.Text2ImagePipeline.__getattribute__) Return getattr(self, name).


-
__getstate__()
[#](https://docs.openvino.ai#openvino_genai.Text2ImagePipeline.__getstate__) Helper for pickle.


-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.Text2ImagePipeline.__gt__) Return self>value.


-
__hash__()
[#](https://docs.openvino.ai#openvino_genai.Text2ImagePipeline.__hash__) Return hash(self).


-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#id0) Overloaded function.

__init__(self: openvino_genai.py_openvino_genai.Text2ImagePipeline, models_path: os.PathLike | str | bytes) -> None

Text2ImagePipeline class constructor. models_path (os.PathLike): Path to the folder with exported model files.

__init__(self: openvino_genai.py_openvino_genai.Text2ImagePipeline, models_path: os.PathLike | str | bytes, device: str,

[**](https://docs.openvino.ai#id3)kwargs) -> NoneText2ImagePipeline class constructor. models_path (os.PathLike): Path with exported model files. device (str): Device to run the model on (e.g., CPU, GPU). kwargs: Text2ImagePipeline properties

__init__(self: openvino_genai.py_openvino_genai.Text2ImagePipeline, pipe: openvino_genai.py_openvino_genai.Image2ImagePipeline) -> None

__init__(self: openvino_genai.py_openvino_genai.Text2ImagePipeline, pipe: openvino_genai.py_openvino_genai.InpaintingPipeline) -> None



-
__init_subclass__()
[#](https://docs.openvino.ai#openvino_genai.Text2ImagePipeline.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.Text2ImagePipeline.__le__) Return self<=value.


-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.Text2ImagePipeline.__lt__) Return self<value.


-
__ne__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.Text2ImagePipeline.__ne__) Return self!=value.


-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino_genai.Text2ImagePipeline.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino_genai.Text2ImagePipeline.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino_genai.Text2ImagePipeline.__reduce_ex__) Helper for pickle.


-
__repr__()
[#](https://docs.openvino.ai#openvino_genai.Text2ImagePipeline.__repr__) Return repr(self).


-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.Text2ImagePipeline.__setattr__) Implement setattr(self, name, value).


-
__sizeof__()
[#](https://docs.openvino.ai#openvino_genai.Text2ImagePipeline.__sizeof__) Size of object in memory, in bytes.


-
__str__()
[#](https://docs.openvino.ai#openvino_genai.Text2ImagePipeline.__str__) Return str(self).


-
__subclasshook__()
[#](https://docs.openvino.ai#openvino_genai.Text2ImagePipeline.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino_genai.Text2ImagePipeline._pybind11_conduit_v1_)

-
compile(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino_genai.Text2ImagePipeline.compile) Overloaded function.

compile(self: openvino_genai.py_openvino_genai.Text2ImagePipeline, device: str,

[**](https://docs.openvino.ai#id5)kwargs) -> NoneCompiles the model. device (str): Device to run the model on (e.g., CPU, GPU). kwargs: Device properties.

compile(self: openvino_genai.py_openvino_genai.Text2ImagePipeline, text_encode_device: str, denoise_device: str, vae_device: str,

[**](https://docs.openvino.ai#id7)kwargs) -> NoneCompiles the model. text_encode_device (str): Device to run the text encoder(s) on (e.g., CPU, GPU). denoise_device (str): Device to run denoise steps on. vae_device (str): Device to run vae decoder on. kwargs: Device properties.



-
decode(
*self:*,[openvino_genai.py_openvino_genai.Text2ImagePipeline](https://docs.openvino.ai#openvino_genai.Text2ImagePipeline)*latent:*)[openvino._pyopenvino.Tensor](https://docs.openvino.ai/ie_python_api/_autosummary/openvino.Tensor.html#openvino.Tensor)[openvino._pyopenvino.Tensor](https://docs.openvino.ai/ie_python_api/_autosummary/openvino.Tensor.html#openvino.Tensor)[#](https://docs.openvino.ai#openvino_genai.Text2ImagePipeline.decode)

-
export_model(
*self:*,[openvino_genai.py_openvino_genai.Text2ImagePipeline](https://docs.openvino.ai#openvino_genai.Text2ImagePipeline)*export_path: os.PathLike | str | bytes*) None[#](https://docs.openvino.ai#openvino_genai.Text2ImagePipeline.export_model) Exports compiled models to a specified directory. Can significantly reduce model load time, especially for large models. export_path (os.PathLike): A path to a directory to export compiled models to.

Use blob_path property to load previously exported models.


-
*static*flux(*scheduler:*,[openvino_genai.py_openvino_genai.Scheduler](https://docs.openvino.ai/openvino_genai.Scheduler.html#openvino_genai.Scheduler)*clip_text_model:*,[openvino_genai.py_openvino_genai.CLIPTextModel](https://docs.openvino.ai/openvino_genai.CLIPTextModel.html#openvino_genai.CLIPTextModel)*t5_encoder_model:*,[openvino_genai.py_openvino_genai.T5EncoderModel](https://docs.openvino.ai/openvino_genai.T5EncoderModel.html#openvino_genai.T5EncoderModel)*transformer:*,[openvino_genai.py_openvino_genai.FluxTransformer2DModel](https://docs.openvino.ai/openvino_genai.FluxTransformer2DModel.html#openvino_genai.FluxTransformer2DModel)*vae:*)[openvino_genai.py_openvino_genai.AutoencoderKL](https://docs.openvino.ai/openvino_genai.AutoencoderKL.html#openvino_genai.AutoencoderKL)[openvino_genai.py_openvino_genai.Text2ImagePipeline](https://docs.openvino.ai#openvino_genai.Text2ImagePipeline)[#](https://docs.openvino.ai#openvino_genai.Text2ImagePipeline.flux)

-
generate(
*self:*,[openvino_genai.py_openvino_genai.Text2ImagePipeline](https://docs.openvino.ai#openvino_genai.Text2ImagePipeline)*prompt: str*,***kwargs*)[openvino._pyopenvino.Tensor](https://docs.openvino.ai/ie_python_api/_autosummary/openvino.Tensor.html#openvino.Tensor)[#](https://docs.openvino.ai#openvino_genai.Text2ImagePipeline.generate) Generates images for text-to-image models.

- Parameters:
**prompt**(*str*) – input prompt**kwargs**– arbitrary keyword arguments with keys corresponding to generate params.


Expected parameters list: prompt_2: str - second prompt, prompt_3: str - third prompt, negative_prompt: str - negative prompt, negative_prompt_2: str - second negative prompt, negative_prompt_3: str - third negative prompt, num_images_per_prompt: int - number of images, that should be generated per prompt, guidance_scale: float - guidance scale, generation_config: GenerationConfig, height: int - height of resulting images, width: int - width of resulting images, num_inference_steps: int - number of inference steps, rng_seed: int - a seed for random numbers generator, generator: openvino_genai.TorchGenerator, openvino_genai.CppStdGenerator or class inherited from openvino_genai.Generator - random generator, adapters: LoRA adapters, strength: strength for image to image generation. 1.0f means initial image is fully noised, max_sequence_length: int - length of t5_encoder_model input

- Returns:
ov.Tensor with resulting images

- Return type:
ov.Tensor



-
get_generation_config(
*self:*)[openvino_genai.py_openvino_genai.Text2ImagePipeline](https://docs.openvino.ai#openvino_genai.Text2ImagePipeline)[openvino_genai.py_openvino_genai.ImageGenerationConfig](https://docs.openvino.ai/openvino_genai.ImageGenerationConfig.html#openvino_genai.ImageGenerationConfig)[#](https://docs.openvino.ai#openvino_genai.Text2ImagePipeline.get_generation_config)

-
get_performance_metrics(
*self:*)[openvino_genai.py_openvino_genai.Text2ImagePipeline](https://docs.openvino.ai#openvino_genai.Text2ImagePipeline)[openvino_genai.py_openvino_genai.ImageGenerationPerfMetrics](https://docs.openvino.ai/openvino_genai.ImageGenerationPerfMetrics.html#openvino_genai.ImageGenerationPerfMetrics)[#](https://docs.openvino.ai#openvino_genai.Text2ImagePipeline.get_performance_metrics)

-
*static*latent_consistency_model(*scheduler:*,[openvino_genai.py_openvino_genai.Scheduler](https://docs.openvino.ai/openvino_genai.Scheduler.html#openvino_genai.Scheduler)*clip_text_model:*,[openvino_genai.py_openvino_genai.CLIPTextModel](https://docs.openvino.ai/openvino_genai.CLIPTextModel.html#openvino_genai.CLIPTextModel)*unet:*,[openvino_genai.py_openvino_genai.UNet2DConditionModel](https://docs.openvino.ai/openvino_genai.UNet2DConditionModel.html#openvino_genai.UNet2DConditionModel)*vae:*)[openvino_genai.py_openvino_genai.AutoencoderKL](https://docs.openvino.ai/openvino_genai.AutoencoderKL.html#openvino_genai.AutoencoderKL)[openvino_genai.py_openvino_genai.Text2ImagePipeline](https://docs.openvino.ai#openvino_genai.Text2ImagePipeline)[#](https://docs.openvino.ai#openvino_genai.Text2ImagePipeline.latent_consistency_model)

-
reshape(
*self:*,[openvino_genai.py_openvino_genai.Text2ImagePipeline](https://docs.openvino.ai#openvino_genai.Text2ImagePipeline)*num_images_per_prompt: SupportsInt*,*height: SupportsInt*,*width: SupportsInt*,*guidance_scale: SupportsFloat*) None[#](https://docs.openvino.ai#openvino_genai.Text2ImagePipeline.reshape)

-
set_generation_config(
*self:*,[openvino_genai.py_openvino_genai.Text2ImagePipeline](https://docs.openvino.ai#openvino_genai.Text2ImagePipeline)*config:*) None[openvino_genai.py_openvino_genai.ImageGenerationConfig](https://docs.openvino.ai/openvino_genai.ImageGenerationConfig.html#openvino_genai.ImageGenerationConfig)[#](https://docs.openvino.ai#openvino_genai.Text2ImagePipeline.set_generation_config)

-
set_scheduler(
*self:*,[openvino_genai.py_openvino_genai.Text2ImagePipeline](https://docs.openvino.ai#openvino_genai.Text2ImagePipeline)*scheduler:*) None[openvino_genai.py_openvino_genai.Scheduler](https://docs.openvino.ai/openvino_genai.Scheduler.html#openvino_genai.Scheduler)[#](https://docs.openvino.ai#openvino_genai.Text2ImagePipeline.set_scheduler)

-
*static*stable_diffusion(*scheduler:*,[openvino_genai.py_openvino_genai.Scheduler](https://docs.openvino.ai/openvino_genai.Scheduler.html#openvino_genai.Scheduler)*clip_text_model:*,[openvino_genai.py_openvino_genai.CLIPTextModel](https://docs.openvino.ai/openvino_genai.CLIPTextModel.html#openvino_genai.CLIPTextModel)*unet:*,[openvino_genai.py_openvino_genai.UNet2DConditionModel](https://docs.openvino.ai/openvino_genai.UNet2DConditionModel.html#openvino_genai.UNet2DConditionModel)*vae:*)[openvino_genai.py_openvino_genai.AutoencoderKL](https://docs.openvino.ai/openvino_genai.AutoencoderKL.html#openvino_genai.AutoencoderKL)[openvino_genai.py_openvino_genai.Text2ImagePipeline](https://docs.openvino.ai#openvino_genai.Text2ImagePipeline)[#](https://docs.openvino.ai#openvino_genai.Text2ImagePipeline.stable_diffusion)

-
*static*stable_diffusion_3(**args*,***kwargs*)[#](https://docs.openvino.ai#openvino_genai.Text2ImagePipeline.stable_diffusion_3) Overloaded function.

stable_diffusion_3(scheduler: openvino_genai.py_openvino_genai.Scheduler, clip_text_model_1: openvino_genai.py_openvino_genai.CLIPTextModelWithProjection, clip_text_model_2: openvino_genai.py_openvino_genai.CLIPTextModelWithProjection, t5_encoder_model: openvino_genai.py_openvino_genai.T5EncoderModel, transformer: openvino_genai.py_openvino_genai.SD3Transformer2DModel, vae: openvino_genai.py_openvino_genai.AutoencoderKL) -> openvino_genai.py_openvino_genai.Text2ImagePipeline

stable_diffusion_3(scheduler: openvino_genai.py_openvino_genai.Scheduler, clip_text_model_1: openvino_genai.py_openvino_genai.CLIPTextModelWithProjection, clip_text_model_2: openvino_genai.py_openvino_genai.CLIPTextModelWithProjection, transformer: openvino_genai.py_openvino_genai.SD3Transformer2DModel, vae: openvino_genai.py_openvino_genai.AutoencoderKL) -> openvino_genai.py_openvino_genai.Text2ImagePipeline



-
*static*stable_diffusion_xl(*scheduler:*,[openvino_genai.py_openvino_genai.Scheduler](https://docs.openvino.ai/openvino_genai.Scheduler.html#openvino_genai.Scheduler)*clip_text_model:*,[openvino_genai.py_openvino_genai.CLIPTextModel](https://docs.openvino.ai/openvino_genai.CLIPTextModel.html#openvino_genai.CLIPTextModel)*clip_text_model_with_projection:*,[openvino_genai.py_openvino_genai.CLIPTextModelWithProjection](https://docs.openvino.ai/openvino_genai.CLIPTextModelWithProjection.html#openvino_genai.CLIPTextModelWithProjection)*unet:*,[openvino_genai.py_openvino_genai.UNet2DConditionModel](https://docs.openvino.ai/openvino_genai.UNet2DConditionModel.html#openvino_genai.UNet2DConditionModel)*vae:*)[openvino_genai.py_openvino_genai.AutoencoderKL](https://docs.openvino.ai/openvino_genai.AutoencoderKL.html#openvino_genai.AutoencoderKL)[openvino_genai.py_openvino_genai.Text2ImagePipeline](https://docs.openvino.ai#openvino_genai.Text2ImagePipeline)[#](https://docs.openvino.ai#openvino_genai.Text2ImagePipeline.stable_diffusion_xl)

-
__init__(