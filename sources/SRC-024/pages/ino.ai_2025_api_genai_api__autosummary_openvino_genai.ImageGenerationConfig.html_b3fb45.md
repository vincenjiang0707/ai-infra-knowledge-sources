source: https://docs.openvino.ai/2025/api/genai_api/_autosummary/openvino_genai.ImageGenerationConfig.html
lastmod: 

# openvino_genai.ImageGenerationConfig[#](https://docs.openvino.ai#openvino-genai-imagegenerationconfig)

-
*class*openvino_genai.ImageGenerationConfig[#](https://docs.openvino.ai#openvino_genai.ImageGenerationConfig) Bases:

`pybind11_object`

This class is used for storing generation config for image generation pipeline.

-
__init__(
*self:*) None[openvino_genai.py_openvino_genai.ImageGenerationConfig](https://docs.openvino.ai#openvino_genai.ImageGenerationConfig)[#](https://docs.openvino.ai#openvino_genai.ImageGenerationConfig.__init__)

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

(self)`__init__`

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

(self, **kwargs)`update_generation_config`

(self)`validate`

Attributes

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino_genai.ImageGenerationConfig.__annotations__)

-
__class__
[#](https://docs.openvino.ai#openvino_genai.ImageGenerationConfig.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino_genai.ImageGenerationConfig.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino_genai.ImageGenerationConfig.__dir__) Default dir() implementation.


-
__eq__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.ImageGenerationConfig.__eq__) Return self==value.


-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino_genai.ImageGenerationConfig.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.ImageGenerationConfig.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino_genai.ImageGenerationConfig.__getattribute__) Return getattr(self, name).


-
__getstate__()
[#](https://docs.openvino.ai#openvino_genai.ImageGenerationConfig.__getstate__) Helper for pickle.


-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.ImageGenerationConfig.__gt__) Return self>value.


-
__hash__()
[#](https://docs.openvino.ai#openvino_genai.ImageGenerationConfig.__hash__) Return hash(self).


-
__init__(
*self:*) None[openvino_genai.py_openvino_genai.ImageGenerationConfig](https://docs.openvino.ai#openvino_genai.ImageGenerationConfig)[#](https://docs.openvino.ai#id0)

-
__init_subclass__()
[#](https://docs.openvino.ai#openvino_genai.ImageGenerationConfig.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.ImageGenerationConfig.__le__) Return self<=value.


-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.ImageGenerationConfig.__lt__) Return self<value.


-
__ne__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.ImageGenerationConfig.__ne__) Return self!=value.


-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino_genai.ImageGenerationConfig.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino_genai.ImageGenerationConfig.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino_genai.ImageGenerationConfig.__reduce_ex__) Helper for pickle.


-
__repr__()
[#](https://docs.openvino.ai#openvino_genai.ImageGenerationConfig.__repr__) Return repr(self).


-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.ImageGenerationConfig.__setattr__) Implement setattr(self, name, value).


-
__sizeof__()
[#](https://docs.openvino.ai#openvino_genai.ImageGenerationConfig.__sizeof__) Size of object in memory, in bytes.


-
__str__()
[#](https://docs.openvino.ai#openvino_genai.ImageGenerationConfig.__str__) Return str(self).


-
__subclasshook__()
[#](https://docs.openvino.ai#openvino_genai.ImageGenerationConfig.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino_genai.ImageGenerationConfig._pybind11_conduit_v1_)

-
*property*adapters[#](https://docs.openvino.ai#openvino_genai.ImageGenerationConfig.adapters)

-
*property*generator[#](https://docs.openvino.ai#openvino_genai.ImageGenerationConfig.generator)

-
*property*guidance_scale[#](https://docs.openvino.ai#openvino_genai.ImageGenerationConfig.guidance_scale)

-
*property*height[#](https://docs.openvino.ai#openvino_genai.ImageGenerationConfig.height)

-
*property*max_sequence_length[#](https://docs.openvino.ai#openvino_genai.ImageGenerationConfig.max_sequence_length)

-
*property*negative_prompt[#](https://docs.openvino.ai#openvino_genai.ImageGenerationConfig.negative_prompt)

-
*property*negative_prompt_2[#](https://docs.openvino.ai#openvino_genai.ImageGenerationConfig.negative_prompt_2)

-
*property*negative_prompt_3[#](https://docs.openvino.ai#openvino_genai.ImageGenerationConfig.negative_prompt_3)

-
*property*num_images_per_prompt[#](https://docs.openvino.ai#openvino_genai.ImageGenerationConfig.num_images_per_prompt)

-
*property*num_inference_steps[#](https://docs.openvino.ai#openvino_genai.ImageGenerationConfig.num_inference_steps)

-
*property*prompt_2[#](https://docs.openvino.ai#openvino_genai.ImageGenerationConfig.prompt_2)

-
*property*prompt_3[#](https://docs.openvino.ai#openvino_genai.ImageGenerationConfig.prompt_3)

-
*property*rng_seed[#](https://docs.openvino.ai#openvino_genai.ImageGenerationConfig.rng_seed)

-
*property*strength[#](https://docs.openvino.ai#openvino_genai.ImageGenerationConfig.strength)

-
update_generation_config(
*self:*,[openvino_genai.py_openvino_genai.ImageGenerationConfig](https://docs.openvino.ai#openvino_genai.ImageGenerationConfig)***kwargs*) None[#](https://docs.openvino.ai#openvino_genai.ImageGenerationConfig.update_generation_config)

-
validate(
*self:*) None[openvino_genai.py_openvino_genai.ImageGenerationConfig](https://docs.openvino.ai#openvino_genai.ImageGenerationConfig)[#](https://docs.openvino.ai#openvino_genai.ImageGenerationConfig.validate)

-
*property*width[#](https://docs.openvino.ai#openvino_genai.ImageGenerationConfig.width)

-
__init__(