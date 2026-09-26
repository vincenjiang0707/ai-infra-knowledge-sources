source: https://docs.openvino.ai/2025/api/genai_api/_autosummary/openvino_genai.PerfMetrics.html
lastmod: 

# openvino_genai.PerfMetrics[#](https://docs.openvino.ai#openvino-genai-perfmetrics)

-
*class*openvino_genai.PerfMetrics[#](https://docs.openvino.ai#openvino_genai.PerfMetrics) Bases:

`pybind11_object`

Holds performance metrics for each generate call.

PerfMetrics holds the following metrics with mean and standard deviations: - Time To the First Token (TTFT), ms - Time per Output Token (TPOT), ms/token - Inference time per Output Token (IPOT), ms/token - Generate total duration, ms - Inference duration, ms - Tokenization duration, ms - Detokenization duration, ms - Throughput, tokens/s

Additional metrics include: - Load time, ms - Number of generated tokens - Number of tokens in the input prompt - Time to initialize grammar compiler for each backend, ms - Time to compile grammar, ms

Preferable way to access metrics is via getter methods. Getter methods calculate mean and std values from raw_metrics and return pairs. If mean and std were already calculated, getters return cached values.

- Parameters:
**get_load_time**(*float*) – Returns the load time in milliseconds.**get_num_generated_tokens**(*int*) – Returns the number of generated tokens.**get_num_input_tokens**(*int*) – Returns the number of tokens in the input prompt.**get_ttft**(*MeanStdPair*) – Returns the mean and standard deviation of TTFT in milliseconds.**get_tpot**(*MeanStdPair*) – Returns the mean and standard deviation of TPOT in milliseconds.**get_ipot**(*MeanStdPair*) – Returns the mean and standard deviation of IPOT in milliseconds.**get_throughput**(*MeanStdPair*) – Returns the mean and standard deviation of throughput in tokens per second.**get_inference_duration**(*MeanStdPair*) – Returns the mean and standard deviation of the time spent on model inference during generate call in milliseconds.**get_generate_duration**(*MeanStdPair*) – Returns the mean and standard deviation of generate durations in milliseconds.**get_tokenization_duration**(*MeanStdPair*) – Returns the mean and standard deviation of tokenization durations in milliseconds.**get_detokenization_duration**(*MeanStdPair*) – Returns the mean and standard deviation of detokenization durations in milliseconds.**get_grammar_compiler_init_times**(*dict**[**str**,**float**]*) – Returns a map with the time to initialize the grammar compiler for each backend in milliseconds.**get_grammar_compile_time**(*SummaryStats*) – Returns the mean, standard deviation, min, and max of grammar compile times in milliseconds.**raw_metrics**() – A structure of RawPerfMetrics type that holds raw metrics.*RawPerfMetrics*


-
__init__(
*self:*) None[openvino_genai.py_openvino_genai.PerfMetrics](https://docs.openvino.ai#openvino_genai.PerfMetrics)[#](https://docs.openvino.ai#openvino_genai.PerfMetrics.__init__)

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
*self:*,[openvino_genai.py_openvino_genai.PerfMetrics](https://docs.openvino.ai#openvino_genai.PerfMetrics)*metrics:*)[openvino_genai.py_openvino_genai.PerfMetrics](https://docs.openvino.ai#openvino_genai.PerfMetrics)[openvino_genai.py_openvino_genai.PerfMetrics](https://docs.openvino.ai#openvino_genai.PerfMetrics)[#](https://docs.openvino.ai#openvino_genai.PerfMetrics.__add__)

-
__annotations__
*= {}*[#](https://docs.openvino.ai#openvino_genai.PerfMetrics.__annotations__)

-
__class__
[#](https://docs.openvino.ai#openvino_genai.PerfMetrics.__class__) alias of

`pybind11_type`


-
__delattr__(
*name*,*/*)[#](https://docs.openvino.ai#openvino_genai.PerfMetrics.__delattr__) Implement delattr(self, name).


-
__dir__()
[#](https://docs.openvino.ai#openvino_genai.PerfMetrics.__dir__) Default dir() implementation.


-
__eq__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.PerfMetrics.__eq__) Return self==value.


-
__format__(
*format_spec*,*/*)[#](https://docs.openvino.ai#openvino_genai.PerfMetrics.__format__) Default object formatter.

Return str(self) if format_spec is empty. Raise TypeError otherwise.


-
__ge__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.PerfMetrics.__ge__) Return self>=value.


-
__getattribute__(
*name*,*/*)[#](https://docs.openvino.ai#openvino_genai.PerfMetrics.__getattribute__) Return getattr(self, name).


-
__getstate__()
[#](https://docs.openvino.ai#openvino_genai.PerfMetrics.__getstate__) Helper for pickle.


-
__gt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.PerfMetrics.__gt__) Return self>value.


-
__hash__()
[#](https://docs.openvino.ai#openvino_genai.PerfMetrics.__hash__) Return hash(self).


-
__iadd__(
*self:*,[openvino_genai.py_openvino_genai.PerfMetrics](https://docs.openvino.ai#openvino_genai.PerfMetrics)*right:*)[openvino_genai.py_openvino_genai.PerfMetrics](https://docs.openvino.ai#openvino_genai.PerfMetrics)[openvino_genai.py_openvino_genai.PerfMetrics](https://docs.openvino.ai#openvino_genai.PerfMetrics)[#](https://docs.openvino.ai#openvino_genai.PerfMetrics.__iadd__)

-
__init__(
*self:*) None[openvino_genai.py_openvino_genai.PerfMetrics](https://docs.openvino.ai#openvino_genai.PerfMetrics)[#](https://docs.openvino.ai#id0)

-
__init_subclass__()
[#](https://docs.openvino.ai#openvino_genai.PerfMetrics.__init_subclass__) This method is called when a class is subclassed.

The default implementation does nothing. It may be overridden to extend subclasses.


-
__le__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.PerfMetrics.__le__) Return self<=value.


-
__lt__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.PerfMetrics.__lt__) Return self<value.


-
__ne__(
*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.PerfMetrics.__ne__) Return self!=value.


-
__new__(
***kwargs*)[#](https://docs.openvino.ai#openvino_genai.PerfMetrics.__new__)

-
__reduce__()
[#](https://docs.openvino.ai#openvino_genai.PerfMetrics.__reduce__) Helper for pickle.


-
__reduce_ex__(
*protocol*,*/*)[#](https://docs.openvino.ai#openvino_genai.PerfMetrics.__reduce_ex__) Helper for pickle.


-
__repr__()
[#](https://docs.openvino.ai#openvino_genai.PerfMetrics.__repr__) Return repr(self).


-
__setattr__(
*name*,*value*,*/*)[#](https://docs.openvino.ai#openvino_genai.PerfMetrics.__setattr__) Implement setattr(self, name, value).


-
__sizeof__()
[#](https://docs.openvino.ai#openvino_genai.PerfMetrics.__sizeof__) Size of object in memory, in bytes.


-
__str__()
[#](https://docs.openvino.ai#openvino_genai.PerfMetrics.__str__) Return str(self).


-
__subclasshook__()
[#](https://docs.openvino.ai#openvino_genai.PerfMetrics.__subclasshook__) Abstract classes can override this to customize issubclass().

This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).


-
_pybind11_conduit_v1_()
[#](https://docs.openvino.ai#openvino_genai.PerfMetrics._pybind11_conduit_v1_)

-
get_detokenization_duration(
*self:*) openvino_genai.py_openvino_genai.MeanStdPair[openvino_genai.py_openvino_genai.PerfMetrics](https://docs.openvino.ai#openvino_genai.PerfMetrics)[#](https://docs.openvino.ai#openvino_genai.PerfMetrics.get_detokenization_duration)

-
get_generate_duration(
*self:*) openvino_genai.py_openvino_genai.MeanStdPair[openvino_genai.py_openvino_genai.PerfMetrics](https://docs.openvino.ai#openvino_genai.PerfMetrics)[#](https://docs.openvino.ai#openvino_genai.PerfMetrics.get_generate_duration)

-
get_grammar_compile_time(
*self:*) openvino_genai.py_openvino_genai.SummaryStats[openvino_genai.py_openvino_genai.PerfMetrics](https://docs.openvino.ai#openvino_genai.PerfMetrics)[#](https://docs.openvino.ai#openvino_genai.PerfMetrics.get_grammar_compile_time)

-
get_grammar_compiler_init_times(
*self:*) dict[str, float][openvino_genai.py_openvino_genai.PerfMetrics](https://docs.openvino.ai#openvino_genai.PerfMetrics)[#](https://docs.openvino.ai#openvino_genai.PerfMetrics.get_grammar_compiler_init_times)

-
get_inference_duration(
*self:*) openvino_genai.py_openvino_genai.MeanStdPair[openvino_genai.py_openvino_genai.PerfMetrics](https://docs.openvino.ai#openvino_genai.PerfMetrics)[#](https://docs.openvino.ai#openvino_genai.PerfMetrics.get_inference_duration)

-
get_ipot(
*self:*) openvino_genai.py_openvino_genai.MeanStdPair[openvino_genai.py_openvino_genai.PerfMetrics](https://docs.openvino.ai#openvino_genai.PerfMetrics)[#](https://docs.openvino.ai#openvino_genai.PerfMetrics.get_ipot)

-
get_load_time(
*self:*) float[openvino_genai.py_openvino_genai.PerfMetrics](https://docs.openvino.ai#openvino_genai.PerfMetrics)[#](https://docs.openvino.ai#openvino_genai.PerfMetrics.get_load_time)

-
get_num_generated_tokens(
*self:*) int[openvino_genai.py_openvino_genai.PerfMetrics](https://docs.openvino.ai#openvino_genai.PerfMetrics)[#](https://docs.openvino.ai#openvino_genai.PerfMetrics.get_num_generated_tokens)

-
get_num_input_tokens(
*self:*) int[openvino_genai.py_openvino_genai.PerfMetrics](https://docs.openvino.ai#openvino_genai.PerfMetrics)[#](https://docs.openvino.ai#openvino_genai.PerfMetrics.get_num_input_tokens)

-
get_throughput(
*self:*) openvino_genai.py_openvino_genai.MeanStdPair[openvino_genai.py_openvino_genai.PerfMetrics](https://docs.openvino.ai#openvino_genai.PerfMetrics)[#](https://docs.openvino.ai#openvino_genai.PerfMetrics.get_throughput)

-
get_tokenization_duration(
*self:*) openvino_genai.py_openvino_genai.MeanStdPair[openvino_genai.py_openvino_genai.PerfMetrics](https://docs.openvino.ai#openvino_genai.PerfMetrics)[#](https://docs.openvino.ai#openvino_genai.PerfMetrics.get_tokenization_duration)

-
get_tpot(
*self:*) openvino_genai.py_openvino_genai.MeanStdPair[openvino_genai.py_openvino_genai.PerfMetrics](https://docs.openvino.ai#openvino_genai.PerfMetrics)[#](https://docs.openvino.ai#openvino_genai.PerfMetrics.get_tpot)

-
get_ttft(
*self:*) openvino_genai.py_openvino_genai.MeanStdPair[openvino_genai.py_openvino_genai.PerfMetrics](https://docs.openvino.ai#openvino_genai.PerfMetrics)[#](https://docs.openvino.ai#openvino_genai.PerfMetrics.get_ttft)

-
*property*raw_metrics[#](https://docs.openvino.ai#openvino_genai.PerfMetrics.raw_metrics)