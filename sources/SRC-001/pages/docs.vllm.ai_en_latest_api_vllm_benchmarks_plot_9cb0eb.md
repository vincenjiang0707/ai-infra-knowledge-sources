source: https://docs.vllm.ai/en/latest/api/vllm/benchmarks/plot/
lastmod: 2026-09-24

#

`vllm.benchmarks.plot`

[¶](https://docs.vllm.ai#vllm.benchmarks.plot)

Generate plots for benchmark results.

Functions:

-
–[construct_timeline_data](https://docs.vllm.ai#vllm.benchmarks.plot.construct_timeline_data)Construct timeline data from request results.

-
–[generate_dataset_stats_plot](https://docs.vllm.ai#vllm.benchmarks.plot.generate_dataset_stats_plot)Generate a matplotlib figure with dataset statistics.

-
–[generate_timeline_plot](https://docs.vllm.ai#vllm.benchmarks.plot.generate_timeline_plot)Generate an HTML timeline plot from benchmark results.


##

`construct_timeline_data(requests_data, itl_thresholds, labels)`

[¶](https://docs.vllm.ai#vllm.benchmarks.plot.construct_timeline_data)

Construct timeline data from request results.

Parameters:

-

(`requests_data`

[¶](https://docs.vllm.ai#vllm.benchmarks.plot.construct_timeline_data(requests_data))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)]]List of per-request result dictionaries

-

(`itl_thresholds`

[¶](https://docs.vllm.ai#vllm.benchmarks.plot.construct_timeline_data(itl_thresholds))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[float](https://docs.python.org/3/builtins/functions.html#float)]ITL thresholds in seconds

-

(`labels`

[¶](https://docs.vllm.ai#vllm.benchmarks.plot.construct_timeline_data(labels))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]Labels for ITL categories


Returns:

## Source code in `vllm/benchmarks/plot.py`


|
|

##

`generate_dataset_stats_plot(results, output_path)`

[¶](https://docs.vllm.ai#vllm.benchmarks.plot.generate_dataset_stats_plot)

Generate a matplotlib figure with dataset statistics.

Creates a figure with 4 subplots: - Top-left: Prompt tokens distribution (histogram) - Top-right: Output tokens distribution (histogram) - Bottom-left: Prompt+output tokens distribution (histogram) - Bottom-right: Stacked bar chart (request_id vs tokens)

Parameters:

-

(`results`

[¶](https://docs.vllm.ai#vllm.benchmarks.plot.generate_dataset_stats_plot(results))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)]]List of per-request result dictionaries containing: - prompt_len: Number of prompt tokens - output_tokens: Number of output tokens

-

(`output_path`

[¶](https://docs.vllm.ai#vllm.benchmarks.plot.generate_dataset_stats_plot(output_path))

) –[Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path)Path where the figure will be saved


## Source code in `vllm/benchmarks/plot.py`


|
|

##

`generate_timeline_plot(results, output_path, colors=None, itl_thresholds=None, labels=None)`

[¶](https://docs.vllm.ai#vllm.benchmarks.plot.generate_timeline_plot)

Generate an HTML timeline plot from benchmark results.

Parameters:

-

(`results`

[¶](https://docs.vllm.ai#vllm.benchmarks.plot.generate_timeline_plot(results))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)]]List of per-request result dictionaries containing: - start_time: Request start time (seconds) - ttft: Time to first token (seconds) - itl: List of inter-token latencies (seconds) - latency: Total request latency (seconds) - prompt_len: Number of prompt tokens - output_tokens: Number of output tokens

-

(`output_path`

[¶](https://docs.vllm.ai#vllm.benchmarks.plot.generate_timeline_plot(output_path))

) –[Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path)Path where the HTML file will be saved

-

(`colors`

[¶](https://docs.vllm.ai#vllm.benchmarks.plot.generate_timeline_plot(colors))

, default:[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)] | None`None`

) –List of colors for ITL categories (default: green, orange, red, black)

-

(`itl_thresholds`

[¶](https://docs.vllm.ai#vllm.benchmarks.plot.generate_timeline_plot(itl_thresholds))

, default:[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[float](https://docs.python.org/3/builtins/functions.html#float)] | None`None`

) –ITL thresholds in seconds (default: [1.0, 4.0, 6.0])

-

(`labels`

[¶](https://docs.vllm.ai#vllm.benchmarks.plot.generate_timeline_plot(labels))

, default:[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)] | None`None`

) –Labels for ITL categories (default based on thresholds)