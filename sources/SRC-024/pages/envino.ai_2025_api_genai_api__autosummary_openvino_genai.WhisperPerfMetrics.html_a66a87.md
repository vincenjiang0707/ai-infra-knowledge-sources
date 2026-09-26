source: https://docs.openvino.ai/2025/api/genai_api/_autosummary/openvino_genai.WhisperPerfMetrics.html
lastmod: 

# openvino_genai.WhisperPerfMetrics[#](https://docs.openvino.ai#openvino-genai-whisperperfmetrics)

-
*class*openvino_genai.WhisperPerfMetrics[#](https://docs.openvino.ai#openvino_genai.WhisperPerfMetrics) Bases:

`PerfMetrics`

Structure with raw performance metrics for each generation before any statistics are calculated.

- Parameters:
**get_features_extraction_duration**(*MeanStdPair*) – Returns mean and standard deviation of features extraction duration in milliseconds**whisper_raw_metrics**– Whisper specific raw metrics


-
__init__(
*self:*) None[openvino_genai.py_openvino_genai.WhisperPerfMetrics](https://docs.openvino.ai#openvino_genai.WhisperPerfMetrics)[#](https://docs.openvino.ai#openvino_genai.WhisperPerfMetrics.__init__)

Methods

(self, metrics)`__add__`

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

(self, right)`__iadd__`

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

(self)`get_generate_duration`

(self)`get_grammar_compile_time`

(self)`get_inference_duration`

(self)`get_ipot`

(self)`get_load_time`

(self)`get_num_generated_tokens`

(self)`get_num_input_tokens`

(self)`get_throughput`

(self)`get_tpot`

(self)`get_ttft`

Attributes

-
__add__(
*self:*,[openvino_genai.py_openvino_genai.PerfMetrics](https://docs.openvino.ai/openvino_genai.PerfMetrics.html#openvino_genai.PerfMetrics)*metrics:*)[openvino_genai.py_openvino_genai.PerfMetrics](https://docs.openvino.ai/openvino_genai.PerfMetrics.html#openvino_genai.PerfMetrics)[openvino_genai.py_openvino_genai.PerfMetrics](https://docs.openvino.ai/openvino_genai.PerfMetrics.html#openvino_genai.PerfMetrics)[#](https://docs.openvino.ai#openvino_genai.WhisperPerfMetrics.__add__)

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino_genai.WhisperPerfMetrics.__annotations__)

-
__class__
[#](https://docs.openvino.ai#openvino_genai.WhisperPerfMetrics.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino_genai.WhisperPerfMetrics.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino_genai.WhisperPerfMetrics.__dir__) Default dir() implementation.


-
__eq__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.WhisperPerfMetrics.__eq__) Return self==value.


-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino_genai.WhisperPerfMetrics.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.WhisperPerfMetrics.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino_genai.WhisperPerfMetrics.__getattribute__) Return getattr(self, name).


-
__getstate__()
[#](https://docs.openvino.ai#openvino_genai.WhisperPerfMetrics.__getstate__) Helper for pickle.


-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.WhisperPerfMetrics.__gt__) Return self>value.


-
__hash__()
[#](https://docs.openvino.ai#openvino_genai.WhisperPerfMetrics.__hash__) Return hash(self).


-
__iadd__(
*self:*,[openvino_genai.py_openvino_genai.PerfMetrics](https://docs.openvino.ai/openvino_genai.PerfMetrics.html#openvino_genai.PerfMetrics)*right:*)[openvino_genai.py_openvino_genai.PerfMetrics](https://docs.openvino.ai/openvino_genai.PerfMetrics.html#openvino_genai.PerfMetrics)[openvino_genai.py_openvino_genai.PerfMetrics](https://docs.openvino.ai/openvino_genai.PerfMetrics.html#openvino_genai.PerfMetrics)[#](https://docs.openvino.ai#openvino_genai.WhisperPerfMetrics.__iadd__)

-
__init__(
*self:*) None[openvino_genai.py_openvino_genai.WhisperPerfMetrics](https://docs.openvino.ai#openvino_genai.WhisperPerfMetrics)[#](https://docs.openvino.ai#id0)

-
__init_subclass__()
[#](https://docs.openvino.ai#openvino_genai.WhisperPerfMetrics.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.WhisperPerfMetrics.__le__) Return self<=value.


-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.WhisperPerfMetrics.__lt__) Return self<value.


-
__ne__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.WhisperPerfMetrics.__ne__) Return self!=value.


-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino_genai.WhisperPerfMetrics.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino_genai.WhisperPerfMetrics.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino_genai.WhisperPerfMetrics.__reduce_ex__) Helper for pickle.


-
__repr__()
[#](https://docs.openvino.ai#openvino_genai.WhisperPerfMetrics.__repr__) Return repr(self).


-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.WhisperPerfMetrics.__setattr__) Implement setattr(self, name, value).


-
__sizeof__()
[#](https://docs.openvino.ai#openvino_genai.WhisperPerfMetrics.__sizeof__) Size of object in memory, in bytes.


-
__str__()
[#](https://docs.openvino.ai#openvino_genai.WhisperPerfMetrics.__str__) Return str(self).


-
__subclasshook__()
[#](https://docs.openvino.ai#openvino_genai.WhisperPerfMetrics.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino_genai.WhisperPerfMetrics._pybind11_conduit_v1_)

-
get_detokenization_duration(
*self:*) openvino_genai.py_openvino_genai.MeanStdPair[openvino_genai.py_openvino_genai.PerfMetrics](https://docs.openvino.ai/openvino_genai.PerfMetrics.html#openvino_genai.PerfMetrics)[#](https://docs.openvino.ai#openvino_genai.WhisperPerfMetrics.get_detokenization_duration)

-
get_features_extraction_duration(
*self:*) openvino_genai.py_openvino_genai.MeanStdPair[openvino_genai.py_openvino_genai.WhisperPerfMetrics](https://docs.openvino.ai#openvino_genai.WhisperPerfMetrics)[#](https://docs.openvino.ai#openvino_genai.WhisperPerfMetrics.get_features_extraction_duration)

-
get_generate_duration(
*self:*) openvino_genai.py_openvino_genai.MeanStdPair[openvino_genai.py_openvino_genai.PerfMetrics](https://docs.openvino.ai/openvino_genai.PerfMetrics.html#openvino_genai.PerfMetrics)[#](https://docs.openvino.ai#openvino_genai.WhisperPerfMetrics.get_generate_duration)

-
get_grammar_compile_time(
*self:*) openvino_genai.py_openvino_genai.SummaryStats[openvino_genai.py_openvino_genai.PerfMetrics](https://docs.openvino.ai/openvino_genai.PerfMetrics.html#openvino_genai.PerfMetrics)[#](https://docs.openvino.ai#openvino_genai.WhisperPerfMetrics.get_grammar_compile_time)

-
get_grammar_compiler_init_times(
*self:*) dict[str, float][openvino_genai.py_openvino_genai.PerfMetrics](https://docs.openvino.ai/openvino_genai.PerfMetrics.html#openvino_genai.PerfMetrics)[#](https://docs.openvino.ai#openvino_genai.WhisperPerfMetrics.get_grammar_compiler_init_times)

-
get_inference_duration(
*self:*) openvino_genai.py_openvino_genai.MeanStdPair[openvino_genai.py_openvino_genai.PerfMetrics](https://docs.openvino.ai/openvino_genai.PerfMetrics.html#openvino_genai.PerfMetrics)[#](https://docs.openvino.ai#openvino_genai.WhisperPerfMetrics.get_inference_duration)

-
get_ipot(
*self:*) openvino_genai.py_openvino_genai.MeanStdPair[openvino_genai.py_openvino_genai.PerfMetrics](https://docs.openvino.ai/openvino_genai.PerfMetrics.html#openvino_genai.PerfMetrics)[#](https://docs.openvino.ai#openvino_genai.WhisperPerfMetrics.get_ipot)

-
get_load_time(
*self:*) float[openvino_genai.py_openvino_genai.PerfMetrics](https://docs.openvino.ai/openvino_genai.PerfMetrics.html#openvino_genai.PerfMetrics)[#](https://docs.openvino.ai#openvino_genai.WhisperPerfMetrics.get_load_time)

-
get_num_generated_tokens(
*self:*) int[openvino_genai.py_openvino_genai.PerfMetrics](https://docs.openvino.ai/openvino_genai.PerfMetrics.html#openvino_genai.PerfMetrics)[#](https://docs.openvino.ai#openvino_genai.WhisperPerfMetrics.get_num_generated_tokens)

-
get_num_input_tokens(
*self:*) int[openvino_genai.py_openvino_genai.PerfMetrics](https://docs.openvino.ai/openvino_genai.PerfMetrics.html#openvino_genai.PerfMetrics)[#](https://docs.openvino.ai#openvino_genai.WhisperPerfMetrics.get_num_input_tokens)

-
get_throughput(
*self:*) openvino_genai.py_openvino_genai.MeanStdPair[openvino_genai.py_openvino_genai.PerfMetrics](https://docs.openvino.ai/openvino_genai.PerfMetrics.html#openvino_genai.PerfMetrics)[#](https://docs.openvino.ai#openvino_genai.WhisperPerfMetrics.get_throughput)

-
get_tokenization_duration(
*self:*) openvino_genai.py_openvino_genai.MeanStdPair[openvino_genai.py_openvino_genai.PerfMetrics](https://docs.openvino.ai/openvino_genai.PerfMetrics.html#openvino_genai.PerfMetrics)[#](https://docs.openvino.ai#openvino_genai.WhisperPerfMetrics.get_tokenization_duration)

-
get_tpot(
*self:*) openvino_genai.py_openvino_genai.MeanStdPair[openvino_genai.py_openvino_genai.PerfMetrics](https://docs.openvino.ai/openvino_genai.PerfMetrics.html#openvino_genai.PerfMetrics)[#](https://docs.openvino.ai#openvino_genai.WhisperPerfMetrics.get_tpot)

-
get_ttft(
*self:*) openvino_genai.py_openvino_genai.MeanStdPair[openvino_genai.py_openvino_genai.PerfMetrics](https://docs.openvino.ai/openvino_genai.PerfMetrics.html#openvino_genai.PerfMetrics)[#](https://docs.openvino.ai#openvino_genai.WhisperPerfMetrics.get_ttft)

-
*property*raw_metrics[#](https://docs.openvino.ai#openvino_genai.WhisperPerfMetrics.raw_metrics)

-
*property*whisper_raw_metrics[#](https://docs.openvino.ai#openvino_genai.WhisperPerfMetrics.whisper_raw_metrics)