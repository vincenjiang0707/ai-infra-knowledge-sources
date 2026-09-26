source: https://docs.openvino.ai/2025/api/genai_api/_autosummary/openvino_genai.RawPerfMetrics.html
lastmod: 

# openvino_genai.RawPerfMetrics[#](https://docs.openvino.ai#openvino-genai-rawperfmetrics)

-
*class*openvino_genai.RawPerfMetrics[#](https://docs.openvino.ai#openvino_genai.RawPerfMetrics) Bases:

`pybind11_object`

Structure with raw performance metrics for each generation before any statistics are calculated.

- Parameters:
**generate_durations**(*list**[**float**]*) – Durations for each generate call in milliseconds.**tokenization_durations**(*list**[**float**]*) – Durations for the tokenization process in milliseconds.**detokenization_durations**(*list**[**float**]*) – Durations for the detokenization process in milliseconds.**m_times_to_first_token**(*list**[**float**]*) – Times to the first token for each call in milliseconds.**m_new_token_times**(*list**[**double**]*) – Timestamps of generation every token or batch of tokens in milliseconds.


:param token_infer_durations : Inference time for each token in milliseconds. :type batch_sizes: list[float]

- Parameters:
**m_batch_sizes**(*list**[**int**]*) – Batch sizes for each generate call.**m_durations**(*list**[**float**]*) – Total durations for each generate call in milliseconds.


:param inference_durations : Total inference duration for each generate call in milliseconds. :type batch_sizes: list[float]

- Parameters:
**grammar_compile_times**(*list**[**float**]*) – Time to compile the grammar in milliseconds.

-
__init__(
*self:*) None[openvino_genai.py_openvino_genai.RawPerfMetrics](https://docs.openvino.ai#openvino_genai.RawPerfMetrics)[#](https://docs.openvino.ai#openvino_genai.RawPerfMetrics.__init__)

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

Attributes

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino_genai.RawPerfMetrics.__annotations__)

-
__class__
[#](https://docs.openvino.ai#openvino_genai.RawPerfMetrics.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino_genai.RawPerfMetrics.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino_genai.RawPerfMetrics.__dir__) Default dir() implementation.


-
__eq__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.RawPerfMetrics.__eq__) Return self==value.


-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino_genai.RawPerfMetrics.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.RawPerfMetrics.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino_genai.RawPerfMetrics.__getattribute__) Return getattr(self, name).


-
__getstate__()
[#](https://docs.openvino.ai#openvino_genai.RawPerfMetrics.__getstate__) Helper for pickle.


-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.RawPerfMetrics.__gt__) Return self>value.


-
__hash__()
[#](https://docs.openvino.ai#openvino_genai.RawPerfMetrics.__hash__) Return hash(self).


-
__init__(
*self:*) None[openvino_genai.py_openvino_genai.RawPerfMetrics](https://docs.openvino.ai#openvino_genai.RawPerfMetrics)[#](https://docs.openvino.ai#id0)

-
__init_subclass__()
[#](https://docs.openvino.ai#openvino_genai.RawPerfMetrics.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.RawPerfMetrics.__le__) Return self<=value.


-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.RawPerfMetrics.__lt__) Return self<value.


-
__ne__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.RawPerfMetrics.__ne__) Return self!=value.


-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino_genai.RawPerfMetrics.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino_genai.RawPerfMetrics.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino_genai.RawPerfMetrics.__reduce_ex__) Helper for pickle.


-
__repr__()
[#](https://docs.openvino.ai#openvino_genai.RawPerfMetrics.__repr__) Return repr(self).


-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.RawPerfMetrics.__setattr__) Implement setattr(self, name, value).


-
__sizeof__()
[#](https://docs.openvino.ai#openvino_genai.RawPerfMetrics.__sizeof__) Size of object in memory, in bytes.


-
__str__()
[#](https://docs.openvino.ai#openvino_genai.RawPerfMetrics.__str__) Return str(self).


-
__subclasshook__()
[#](https://docs.openvino.ai#openvino_genai.RawPerfMetrics.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino_genai.RawPerfMetrics._pybind11_conduit_v1_)

-
*property*detokenization_durations[#](https://docs.openvino.ai#openvino_genai.RawPerfMetrics.detokenization_durations)

-
*property*generate_durations[#](https://docs.openvino.ai#openvino_genai.RawPerfMetrics.generate_durations)

-
*property*grammar_compile_times[#](https://docs.openvino.ai#openvino_genai.RawPerfMetrics.grammar_compile_times)

-
*property*inference_durations[#](https://docs.openvino.ai#openvino_genai.RawPerfMetrics.inference_durations)

-
*property*m_batch_sizes[#](https://docs.openvino.ai#openvino_genai.RawPerfMetrics.m_batch_sizes)

-
*property*m_durations[#](https://docs.openvino.ai#openvino_genai.RawPerfMetrics.m_durations)

-
*property*m_new_token_times[#](https://docs.openvino.ai#openvino_genai.RawPerfMetrics.m_new_token_times)

-
*property*m_times_to_first_token[#](https://docs.openvino.ai#openvino_genai.RawPerfMetrics.m_times_to_first_token)

-
*property*token_infer_durations[#](https://docs.openvino.ai#openvino_genai.RawPerfMetrics.token_infer_durations)

-
*property*tokenization_durations[#](https://docs.openvino.ai#openvino_genai.RawPerfMetrics.tokenization_durations)