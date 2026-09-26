source: https://docs.openvino.ai/2025/api/genai_api/_autosummary/openvino_genai.DecodedResults.html
lastmod: 

# openvino_genai.DecodedResults[#](https://docs.openvino.ai#openvino-genai-decodedresults)

-
*class*openvino_genai.DecodedResults[#](https://docs.openvino.ai#openvino_genai.DecodedResults) Bases:

`pybind11_object`

Structure to store resulting batched text outputs and scores for each batch. The first num_return_sequences elements correspond to the first batch element.

Parameters: texts: vector of resulting sequences. scores: scores for each sequence. metrics: performance metrics with tpot, ttft, etc. of type ov::genai::PerfMetrics. extended_perf_metrics: performance pipeline specifics metrics,

applicable for pipelines with implemented extended metrics: SpeculativeDecoding Pipeline.

-
__init__(
*self:*) None[openvino_genai.py_openvino_genai.DecodedResults](https://docs.openvino.ai#openvino_genai.DecodedResults)[#](https://docs.openvino.ai#openvino_genai.DecodedResults.__init__)

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

(self)`__str__`

Abstract classes can override this to customize issubclass().

Attributes

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino_genai.DecodedResults.__annotations__)

-
__class__
[#](https://docs.openvino.ai#openvino_genai.DecodedResults.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino_genai.DecodedResults.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino_genai.DecodedResults.__dir__) Default dir() implementation.


-
__eq__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.DecodedResults.__eq__) Return self==value.


-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino_genai.DecodedResults.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.DecodedResults.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino_genai.DecodedResults.__getattribute__) Return getattr(self, name).


-
__getstate__()
[#](https://docs.openvino.ai#openvino_genai.DecodedResults.__getstate__) Helper for pickle.


-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.DecodedResults.__gt__) Return self>value.


-
__hash__()
[#](https://docs.openvino.ai#openvino_genai.DecodedResults.__hash__) Return hash(self).


-
__init__(
*self:*) None[openvino_genai.py_openvino_genai.DecodedResults](https://docs.openvino.ai#openvino_genai.DecodedResults)[#](https://docs.openvino.ai#id0)

-
__init_subclass__()
[#](https://docs.openvino.ai#openvino_genai.DecodedResults.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.DecodedResults.__le__) Return self<=value.


-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.DecodedResults.__lt__) Return self<value.


-
__ne__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.DecodedResults.__ne__) Return self!=value.


-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino_genai.DecodedResults.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino_genai.DecodedResults.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino_genai.DecodedResults.__reduce_ex__) Helper for pickle.


-
__repr__()
[#](https://docs.openvino.ai#openvino_genai.DecodedResults.__repr__) Return repr(self).


-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.DecodedResults.__setattr__) Implement setattr(self, name, value).


-
__sizeof__()
[#](https://docs.openvino.ai#openvino_genai.DecodedResults.__sizeof__) Size of object in memory, in bytes.


-
__str__(
*self:*) str[openvino_genai.py_openvino_genai.DecodedResults](https://docs.openvino.ai#openvino_genai.DecodedResults)[#](https://docs.openvino.ai#openvino_genai.DecodedResults.__str__)

-
__subclasshook__()
[#](https://docs.openvino.ai#openvino_genai.DecodedResults.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino_genai.DecodedResults._pybind11_conduit_v1_)

-
*property*extended_perf_metrics[#](https://docs.openvino.ai#openvino_genai.DecodedResults.extended_perf_metrics)

-
*property*parsed[#](https://docs.openvino.ai#openvino_genai.DecodedResults.parsed)

-
*property*perf_metrics[#](https://docs.openvino.ai#openvino_genai.DecodedResults.perf_metrics)

-
*property*scores[#](https://docs.openvino.ai#openvino_genai.DecodedResults.scores)

-
*property*texts[#](https://docs.openvino.ai#openvino_genai.DecodedResults.texts)

-
__init__(