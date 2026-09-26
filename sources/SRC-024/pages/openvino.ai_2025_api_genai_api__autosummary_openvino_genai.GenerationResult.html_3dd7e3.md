source: https://docs.openvino.ai/2025/api/genai_api/_autosummary/openvino_genai.GenerationResult.html
lastmod: 

# openvino_genai.GenerationResult[#](https://docs.openvino.ai#openvino-genai-generationresult)

-
*class*openvino_genai.GenerationResult[#](https://docs.openvino.ai#openvino_genai.GenerationResult) Bases:

`pybind11_object`

GenerationResult stores resulting batched tokens and scores.

Parameters: request_id: obsolete when handle API is approved as handle will connect results with prompts. generation_ids: in a generic case we have multiple generation results per initial prompt

depending on sampling parameters (e.g. beam search or parallel sampling).

scores: scores. status: status of generation. The following values are possible:

RUNNING = 0 - Default status for ongoing generation. FINISHED = 1 - Status set when generation has been finished. IGNORED = 2 - Status set when generation run into out-of-memory condition and could not be continued. CANCEL = 3 - Status set when generation handle is cancelled. The last prompt and all generated tokens will be dropped from history, KV cache will include history but last step. STOP = 4 - Status set when generation handle is stopped. History will be kept, KV cache will include the last prompt and generated tokens. DROPPED_BY_HANDLE = STOP - Status set when generation handle is dropped. Deprecated. Please, use STOP instead.

perf_metrics: Performance metrics for each generation result. extended_perf_metrics: performance pipeline specifics metrics,

applicable for pipelines with implemented extended metrics: SpeculativeDecoding Pipeline.

-
__init__(
*self:*) None[openvino_genai.py_openvino_genai.GenerationResult](https://docs.openvino.ai#openvino_genai.GenerationResult)[#](https://docs.openvino.ai#openvino_genai.GenerationResult.__init__)

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

(self)`__repr__`

(name, value, /)`__setattr__`

Implement setattr(self, name, value).

Size of object in memory, in bytes.

()`__str__`

Return str(self).

Abstract classes can override this to customize issubclass().

(self)`get_generation_ids`

Attributes

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino_genai.GenerationResult.__annotations__)

-
__class__
[#](https://docs.openvino.ai#openvino_genai.GenerationResult.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino_genai.GenerationResult.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino_genai.GenerationResult.__dir__) Default dir() implementation.


-
__eq__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.GenerationResult.__eq__) Return self==value.


-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino_genai.GenerationResult.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.GenerationResult.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino_genai.GenerationResult.__getattribute__) Return getattr(self, name).


-
__getstate__()
[#](https://docs.openvino.ai#openvino_genai.GenerationResult.__getstate__) Helper for pickle.


-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.GenerationResult.__gt__) Return self>value.


-
__hash__()
[#](https://docs.openvino.ai#openvino_genai.GenerationResult.__hash__) Return hash(self).


-
__init__(
*self:*) None[openvino_genai.py_openvino_genai.GenerationResult](https://docs.openvino.ai#openvino_genai.GenerationResult)[#](https://docs.openvino.ai#id0)

-
__init_subclass__()
[#](https://docs.openvino.ai#openvino_genai.GenerationResult.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.GenerationResult.__le__) Return self<=value.


-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.GenerationResult.__lt__) Return self<value.


-
__ne__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.GenerationResult.__ne__) Return self!=value.


-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino_genai.GenerationResult.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino_genai.GenerationResult.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino_genai.GenerationResult.__reduce_ex__) Helper for pickle.


-
__repr__(
*self:*) str[openvino_genai.py_openvino_genai.GenerationResult](https://docs.openvino.ai#openvino_genai.GenerationResult)[#](https://docs.openvino.ai#openvino_genai.GenerationResult.__repr__)

-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.GenerationResult.__setattr__) Implement setattr(self, name, value).


-
__sizeof__()
[#](https://docs.openvino.ai#openvino_genai.GenerationResult.__sizeof__) Size of object in memory, in bytes.


-
__str__()
[#](https://docs.openvino.ai#openvino_genai.GenerationResult.__str__) Return str(self).


-
__subclasshook__()
[#](https://docs.openvino.ai#openvino_genai.GenerationResult.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino_genai.GenerationResult._pybind11_conduit_v1_)

-
*property*extended_perf_metrics[#](https://docs.openvino.ai#openvino_genai.GenerationResult.extended_perf_metrics)

-
get_generation_ids(
*self:*) list[str][openvino_genai.py_openvino_genai.GenerationResult](https://docs.openvino.ai#openvino_genai.GenerationResult)[#](https://docs.openvino.ai#openvino_genai.GenerationResult.get_generation_ids)

-
*property*m_generation_ids[#](https://docs.openvino.ai#openvino_genai.GenerationResult.m_generation_ids)

-
*property*m_request_id[#](https://docs.openvino.ai#openvino_genai.GenerationResult.m_request_id)

-
*property*m_scores[#](https://docs.openvino.ai#openvino_genai.GenerationResult.m_scores)

-
*property*m_status[#](https://docs.openvino.ai#openvino_genai.GenerationResult.m_status)

-
*property*perf_metrics[#](https://docs.openvino.ai#openvino_genai.GenerationResult.perf_metrics)

-
__init__(