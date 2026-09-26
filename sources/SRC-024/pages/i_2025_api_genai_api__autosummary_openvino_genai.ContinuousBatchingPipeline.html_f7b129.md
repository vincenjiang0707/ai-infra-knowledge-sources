source: https://docs.openvino.ai/2025/api/genai_api/_autosummary/openvino_genai.ContinuousBatchingPipeline.html
lastmod: 

# openvino_genai.ContinuousBatchingPipeline[#](https://docs.openvino.ai#openvino-genai-continuousbatchingpipeline)

-
*class*openvino_genai.ContinuousBatchingPipeline[#](https://docs.openvino.ai#openvino_genai.ContinuousBatchingPipeline) Bases:

`pybind11_object`

This class is used for generation with LLMs with continuous batchig

-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino_genai.ContinuousBatchingPipeline.__init__) Overloaded function.

__init__(self: openvino_genai.py_openvino_genai.ContinuousBatchingPipeline, models_path: os.PathLike | str | bytes, scheduler_config: openvino_genai.py_openvino_genai.SchedulerConfig, device: str, properties: collections.abc.Mapping[str, object] = {}, tokenizer_properties: collections.abc.Mapping[str, object] = {}, vision_encoder_properties: collections.abc.Mapping[str, object] = {}) -> None

__init__(self: openvino_genai.py_openvino_genai.ContinuousBatchingPipeline, models_path: os.PathLike | str | bytes, tokenizer: openvino_genai.py_openvino_genai.Tokenizer, scheduler_config: openvino_genai.py_openvino_genai.SchedulerConfig, device: str,

[**](https://docs.openvino.ai#id1)kwargs) -> None


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

(*args, **kwargs)`add_request`

Overloaded function.

(self)`finish_chat`

(*args, **kwargs)`generate`

Overloaded function.

(self)`get_config`

(self)`get_metrics`

(self)`get_tokenizer`

(self[, system_message])`start_chat`

(self)`step`

Attributes

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino_genai.ContinuousBatchingPipeline.__annotations__)

-
__class__
[#](https://docs.openvino.ai#openvino_genai.ContinuousBatchingPipeline.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino_genai.ContinuousBatchingPipeline.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino_genai.ContinuousBatchingPipeline.__dir__) Default dir() implementation.


-
__eq__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.ContinuousBatchingPipeline.__eq__) Return self==value.


-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino_genai.ContinuousBatchingPipeline.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.ContinuousBatchingPipeline.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino_genai.ContinuousBatchingPipeline.__getattribute__) Return getattr(self, name).


-
__getstate__()
[#](https://docs.openvino.ai#openvino_genai.ContinuousBatchingPipeline.__getstate__) Helper for pickle.


-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.ContinuousBatchingPipeline.__gt__) Return self>value.


-
__hash__()
[#](https://docs.openvino.ai#openvino_genai.ContinuousBatchingPipeline.__hash__) Return hash(self).


-
__init__(
**args*,***kwargs*)[#](https://docs.openvino.ai#id0) Overloaded function.

__init__(self: openvino_genai.py_openvino_genai.ContinuousBatchingPipeline, models_path: os.PathLike | str | bytes, scheduler_config: openvino_genai.py_openvino_genai.SchedulerConfig, device: str, properties: collections.abc.Mapping[str, object] = {}, tokenizer_properties: collections.abc.Mapping[str, object] = {}, vision_encoder_properties: collections.abc.Mapping[str, object] = {}) -> None

__init__(self: openvino_genai.py_openvino_genai.ContinuousBatchingPipeline, models_path: os.PathLike | str | bytes, tokenizer: openvino_genai.py_openvino_genai.Tokenizer, scheduler_config: openvino_genai.py_openvino_genai.SchedulerConfig, device: str,

[**](https://docs.openvino.ai#id3)kwargs) -> None


-
__init_subclass__()
[#](https://docs.openvino.ai#openvino_genai.ContinuousBatchingPipeline.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.ContinuousBatchingPipeline.__le__) Return self<=value.


-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.ContinuousBatchingPipeline.__lt__) Return self<value.


-
__ne__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.ContinuousBatchingPipeline.__ne__) Return self!=value.


-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino_genai.ContinuousBatchingPipeline.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino_genai.ContinuousBatchingPipeline.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino_genai.ContinuousBatchingPipeline.__reduce_ex__) Helper for pickle.


-
__repr__()
[#](https://docs.openvino.ai#openvino_genai.ContinuousBatchingPipeline.__repr__) Return repr(self).


-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.ContinuousBatchingPipeline.__setattr__) Implement setattr(self, name, value).


-
__sizeof__()
[#](https://docs.openvino.ai#openvino_genai.ContinuousBatchingPipeline.__sizeof__) Size of object in memory, in bytes.


-
__str__()
[#](https://docs.openvino.ai#openvino_genai.ContinuousBatchingPipeline.__str__) Return str(self).


-
__subclasshook__()
[#](https://docs.openvino.ai#openvino_genai.ContinuousBatchingPipeline.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino_genai.ContinuousBatchingPipeline._pybind11_conduit_v1_)

-
add_request(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino_genai.ContinuousBatchingPipeline.add_request) Overloaded function.

add_request(self: openvino_genai.py_openvino_genai.ContinuousBatchingPipeline, request_id: typing.SupportsInt, input_ids: openvino._pyopenvino.Tensor, generation_config: openvino_genai.py_openvino_genai.GenerationConfig) -> openvino_genai.py_openvino_genai.GenerationHandle

add_request(self: openvino_genai.py_openvino_genai.ContinuousBatchingPipeline, request_id: typing.SupportsInt, prompt: str, generation_config: openvino_genai.py_openvino_genai.GenerationConfig) -> openvino_genai.py_openvino_genai.GenerationHandle

add_request(self: openvino_genai.py_openvino_genai.ContinuousBatchingPipeline, request_id: typing.SupportsInt, prompt: str, images: collections.abc.Sequence[openvino._pyopenvino.Tensor], videos: collections.abc.Sequence[openvino._pyopenvino.Tensor], generation_config: openvino_genai.py_openvino_genai.GenerationConfig) -> openvino_genai.py_openvino_genai.GenerationHandle

add_request(self: openvino_genai.py_openvino_genai.ContinuousBatchingPipeline, request_id: typing.SupportsInt, prompt: str, images: collections.abc.Sequence[openvino._pyopenvino.Tensor], generation_config: openvino_genai.py_openvino_genai.GenerationConfig) -> openvino_genai.py_openvino_genai.GenerationHandle



-
finish_chat(
*self:*) None[openvino_genai.py_openvino_genai.ContinuousBatchingPipeline](https://docs.openvino.ai#openvino_genai.ContinuousBatchingPipeline)[#](https://docs.openvino.ai#openvino_genai.ContinuousBatchingPipeline.finish_chat)

-
generate(
**args*,***kwargs*)[#](https://docs.openvino.ai#openvino_genai.ContinuousBatchingPipeline.generate) Overloaded function.

generate(self: openvino_genai.py_openvino_genai.ContinuousBatchingPipeline, input_ids: collections.abc.Sequence[openvino._pyopenvino.Tensor], generation_config: collections.abc.Sequence[openvino_genai.py_openvino_genai.GenerationConfig], streamer: collections.abc.Callable[[str], int | None] | openvino_genai.py_openvino_genai.StreamerBase | None = None) -> list[openvino_genai.py_openvino_genai.EncodedGenerationResult]

generate(self: openvino_genai.py_openvino_genai.ContinuousBatchingPipeline, prompts: collections.abc.Sequence[str], generation_config: collections.abc.Sequence[openvino_genai.py_openvino_genai.GenerationConfig], streamer: collections.abc.Callable[[str], int | None] | openvino_genai.py_openvino_genai.StreamerBase | None = None) -> list[openvino_genai.py_openvino_genai.GenerationResult]

generate(self: openvino_genai.py_openvino_genai.ContinuousBatchingPipeline, prompt: str, generation_config: openvino_genai.py_openvino_genai.GenerationConfig, streamer: collections.abc.Callable[[str], int | None] | openvino_genai.py_openvino_genai.StreamerBase | None = None) -> list[openvino_genai.py_openvino_genai.GenerationResult]

generate(self: openvino_genai.py_openvino_genai.ContinuousBatchingPipeline, prompts: collections.abc.Sequence[openvino_genai.py_openvino_genai.ChatHistory], generation_config: collections.abc.Sequence[openvino_genai.py_openvino_genai.GenerationConfig], streamer: collections.abc.Callable[[str], int | None] | openvino_genai.py_openvino_genai.StreamerBase | None = None) -> list[openvino_genai.py_openvino_genai.GenerationResult]

generate(self: openvino_genai.py_openvino_genai.ContinuousBatchingPipeline, prompts: collections.abc.Sequence[str], images: collections.abc.Sequence[collections.abc.Sequence[openvino._pyopenvino.Tensor]], videos: collections.abc.Sequence[collections.abc.Sequence[openvino._pyopenvino.Tensor]], generation_config: collections.abc.Sequence[openvino_genai.py_openvino_genai.GenerationConfig], streamer: collections.abc.Callable[[str], int | None] | openvino_genai.py_openvino_genai.StreamerBase | None = None) -> list[openvino_genai.py_openvino_genai.GenerationResult]

generate(self: openvino_genai.py_openvino_genai.ContinuousBatchingPipeline, prompts: collections.abc.Sequence[str], images: collections.abc.Sequence[collections.abc.Sequence[openvino._pyopenvino.Tensor]], generation_config: collections.abc.Sequence[openvino_genai.py_openvino_genai.GenerationConfig], streamer: collections.abc.Callable[[str], int | None] | openvino_genai.py_openvino_genai.StreamerBase | None = None) -> list[openvino_genai.py_openvino_genai.GenerationResult]

generate(self: openvino_genai.py_openvino_genai.ContinuousBatchingPipeline, prompts: collections.abc.Sequence[str], videos: collections.abc.Sequence[collections.abc.Sequence[openvino._pyopenvino.Tensor]], generation_config: collections.abc.Sequence[openvino_genai.py_openvino_genai.GenerationConfig], streamer: collections.abc.Callable[[str], int | None] | openvino_genai.py_openvino_genai.StreamerBase | None = None) -> list[openvino_genai.py_openvino_genai.GenerationResult]



-
get_config(
*self:*)[openvino_genai.py_openvino_genai.ContinuousBatchingPipeline](https://docs.openvino.ai#openvino_genai.ContinuousBatchingPipeline)[openvino_genai.py_openvino_genai.GenerationConfig](https://docs.openvino.ai/openvino_genai.GenerationConfig.html#openvino_genai.GenerationConfig)[#](https://docs.openvino.ai#openvino_genai.ContinuousBatchingPipeline.get_config)

-
get_metrics(
*self:*) openvino_genai.py_openvino_genai.PipelineMetrics[openvino_genai.py_openvino_genai.ContinuousBatchingPipeline](https://docs.openvino.ai#openvino_genai.ContinuousBatchingPipeline)[#](https://docs.openvino.ai#openvino_genai.ContinuousBatchingPipeline.get_metrics)

-
get_tokenizer(
*self:*)[openvino_genai.py_openvino_genai.ContinuousBatchingPipeline](https://docs.openvino.ai#openvino_genai.ContinuousBatchingPipeline)[openvino_genai.py_openvino_genai.Tokenizer](https://docs.openvino.ai/openvino_genai.Tokenizer.html#openvino_genai.Tokenizer)[#](https://docs.openvino.ai#openvino_genai.ContinuousBatchingPipeline.get_tokenizer)

-
has_non_finished_requests(
*self:*) bool[openvino_genai.py_openvino_genai.ContinuousBatchingPipeline](https://docs.openvino.ai#openvino_genai.ContinuousBatchingPipeline)[#](https://docs.openvino.ai#openvino_genai.ContinuousBatchingPipeline.has_non_finished_requests)

-
start_chat(
*self:*,[openvino_genai.py_openvino_genai.ContinuousBatchingPipeline](https://docs.openvino.ai#openvino_genai.ContinuousBatchingPipeline)*system_message: str = ''*) None[#](https://docs.openvino.ai#openvino_genai.ContinuousBatchingPipeline.start_chat)

-
step(
*self:*) None[openvino_genai.py_openvino_genai.ContinuousBatchingPipeline](https://docs.openvino.ai#openvino_genai.ContinuousBatchingPipeline)[#](https://docs.openvino.ai#openvino_genai.ContinuousBatchingPipeline.step)

-
__init__(