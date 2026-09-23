source: https://docs.vllm.ai/en/latest/api/vllm/benchmarks/sweep/plot/
lastmod: 2026-09-23

#

`vllm.benchmarks.sweep.plot`

[¶](https://docs.vllm.ai#vllm.benchmarks.sweep.plot)

Classes:

##

`PlotBinner`

`dataclass`

[¶](https://docs.vllm.ai#vllm.benchmarks.sweep.plot.PlotBinner)

Methods:

-
–[apply](https://docs.vllm.ai#vllm.benchmarks.sweep.plot.PlotBinner.apply)Applies this binner to a DataFrame.


## Source code in `vllm/benchmarks/sweep/plot.py`


##

`PlotFilterBase`

`dataclass`

[¶](https://docs.vllm.ai#vllm.benchmarks.sweep.plot.PlotFilterBase)

Bases: [ABC](https://docs.python.org/3/library/abc.html#abc.ABC)

Methods:

-
–[apply](https://docs.vllm.ai#vllm.benchmarks.sweep.plot.PlotFilterBase.apply)Applies this filter to a DataFrame.


## Source code in `vllm/benchmarks/sweep/plot.py`


##

`_convert_inf_nan_strings(data)`

[¶](https://docs.vllm.ai#vllm.benchmarks.sweep.plot._convert_inf_nan_strings)

Convert string values "inf", "-inf", and "nan" to their float equivalents.

This handles the case where JSON serialization represents inf/nan as strings.