source: https://docs.vllm.ai/en/latest/api/vllm/benchmarks/serve/
lastmod: 2026-09-24

#

`vllm.benchmarks.serve`

[¶](https://docs.vllm.ai#vllm.benchmarks.serve)

Benchmark online serving throughput.

On the server side, run one of the following commands to launch the vLLM OpenAI API server: vllm serve

On the client side, run: vllm bench serve \ --backend

Classes:

-
–[DiffusionMetrics](https://docs.vllm.ai#vllm.benchmarks.serve.DiffusionMetrics)Diffusion (dLLM) decoding metrics from the server's Prometheus endpoint.

-
–[SpecDecodeMetrics](https://docs.vllm.ai#vllm.benchmarks.serve.SpecDecodeMetrics)Speculative decoding metrics from the server's Prometheus endpoint.


Functions:

-
–[calculate_metrics](https://docs.vllm.ai#vllm.benchmarks.serve.calculate_metrics)Calculate the metrics for the benchmark.

-
–[calculate_metrics_for_embeddings](https://docs.vllm.ai#vllm.benchmarks.serve.calculate_metrics_for_embeddings)Calculate the metrics for the embedding requests.

-
–[compute_result_filename](https://docs.vllm.ai#vllm.benchmarks.serve.compute_result_filename)Compute the result filename based on benchmark configuration.

-
–[fetch_diffusion_metrics](https://docs.vllm.ai#vllm.benchmarks.serve.fetch_diffusion_metrics)Fetch diffusion decoding metrics from the server's Prometheus endpoint.

-
–[fetch_spec_decode_metrics](https://docs.vllm.ai#vllm.benchmarks.serve.fetch_spec_decode_metrics)Fetch speculative decoding metrics from the server's Prometheus endpoint.

-
–[get_first_model_from_server](https://docs.vllm.ai#vllm.benchmarks.serve.get_first_model_from_server)Fetch the first model from the server's /v1/models endpoint.

-
–[get_request](https://docs.vllm.ai#vllm.benchmarks.serve.get_request)Asynchronously generates requests at a specified rate


##

`DiffusionMetrics`

`dataclass`

[¶](https://docs.vllm.ai#vllm.benchmarks.serve.DiffusionMetrics)

Diffusion (dLLM) decoding metrics from the server's Prometheus endpoint.

## Source code in `vllm/benchmarks/serve.py`


##

`SpecDecodeMetrics`

`dataclass`

[¶](https://docs.vllm.ai#vllm.benchmarks.serve.SpecDecodeMetrics)

Speculative decoding metrics from the server's Prometheus endpoint.

## Source code in `vllm/benchmarks/serve.py`


##

`_align_prompts_to_server_tokenizer(base_url, model_id, input_requests, ssl_context=None)`

`async`

[¶](https://docs.vllm.ai#vllm.benchmarks.serve._align_prompts_to_server_tokenizer)

Re-align prompts if local/server tokenizers disagree.

## Source code in `vllm/benchmarks/serve.py`


##

`_merge_overrides(base, override)`

[¶](https://docs.vllm.ai#vllm.benchmarks.serve._merge_overrides)

Shallow merge; per-request wins. Returns None if both are empty.

##

`calculate_metrics(input_requests, outputs, dur_s, tokenizer, selected_percentiles, goodput_config_dict)`

[¶](https://docs.vllm.ai#vllm.benchmarks.serve.calculate_metrics)

Calculate the metrics for the benchmark.

Parameters:

-

(`input_requests`

[¶](https://docs.vllm.ai#vllm.benchmarks.serve.calculate_metrics(input_requests))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[SampleRequest](https://docs.vllm.ai/datasets/#vllm.benchmarks.datasets.SampleRequest)]The input requests.

-

(`outputs`

[¶](https://docs.vllm.ai#vllm.benchmarks.serve.calculate_metrics(outputs))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[RequestFuncOutput](https://docs.vllm.ai/lib/endpoint_request_func/#vllm.benchmarks.lib.endpoint_request_func.RequestFuncOutput)]The outputs of the requests.

-

(`dur_s`

[¶](https://docs.vllm.ai#vllm.benchmarks.serve.calculate_metrics(dur_s))

) –[float](https://docs.python.org/3/builtins/functions.html#float)The duration of the benchmark.

-

(`tokenizer`

[¶](https://docs.vllm.ai#vllm.benchmarks.serve.calculate_metrics(tokenizer))`TokenizerLike | None`

) –The tokenizer to use.

-

(`selected_percentiles`

[¶](https://docs.vllm.ai#vllm.benchmarks.serve.calculate_metrics(selected_percentiles))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[float](https://docs.python.org/3/builtins/functions.html#float)]The percentiles to select.

-

(`goodput_config_dict`

[¶](https://docs.vllm.ai#vllm.benchmarks.serve.calculate_metrics(goodput_config_dict))

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[float](https://docs.python.org/3/builtins/functions.html#float)]The goodput configuration.


Returns:

-

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[BenchmarkMetrics,[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]]A tuple of the benchmark metrics and the actual output lengths.


## Source code in `vllm/benchmarks/serve.py`


|
|

##

`calculate_metrics_for_embeddings(outputs, dur_s, selected_percentiles)`

[¶](https://docs.vllm.ai#vllm.benchmarks.serve.calculate_metrics_for_embeddings)

Calculate the metrics for the embedding requests.

Parameters:

-

(`outputs`

[¶](https://docs.vllm.ai#vllm.benchmarks.serve.calculate_metrics_for_embeddings(outputs))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[RequestFuncOutput](https://docs.vllm.ai/lib/endpoint_request_func/#vllm.benchmarks.lib.endpoint_request_func.RequestFuncOutput)]The outputs of the requests.

-

(`dur_s`

[¶](https://docs.vllm.ai#vllm.benchmarks.serve.calculate_metrics_for_embeddings(dur_s))

) –[float](https://docs.python.org/3/builtins/functions.html#float)The duration of the benchmark.

-

(`selected_percentiles`

[¶](https://docs.vllm.ai#vllm.benchmarks.serve.calculate_metrics_for_embeddings(selected_percentiles))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[float](https://docs.python.org/3/builtins/functions.html#float)]The percentiles to select.


Returns:

-
`EmbedBenchmarkMetrics`

–The calculated benchmark metrics.


## Source code in `vllm/benchmarks/serve.py`


##

`compute_result_filename(args, model_id, label, current_dt)`

[¶](https://docs.vllm.ai#vllm.benchmarks.serve.compute_result_filename)

Compute the result filename based on benchmark configuration.

Parameters:

-

(`args`

[¶](https://docs.vllm.ai#vllm.benchmarks.serve.compute_result_filename(args))

) –[Namespace](https://docs.python.org/3/library/argparse.html#argparse.Namespace)Command line arguments containing result configuration

-

(`model_id`

[¶](https://docs.vllm.ai#vllm.benchmarks.serve.compute_result_filename(model_id))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The model identifier

-

(`label`

[¶](https://docs.vllm.ai#vllm.benchmarks.serve.compute_result_filename(label))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The benchmark label

-

(`current_dt`

[¶](https://docs.vllm.ai#vllm.benchmarks.serve.compute_result_filename(current_dt))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Current datetime string


Returns:

-

–[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneThe computed filename path or None if no result saving is requested


## Source code in `vllm/benchmarks/serve.py`


##

`fetch_diffusion_metrics(base_url, session)`

`async`

[¶](https://docs.vllm.ai#vllm.benchmarks.serve.fetch_diffusion_metrics)

Fetch diffusion decoding metrics from the server's Prometheus endpoint.

Returns None if the model is not a diffusion model or metrics are not available.

## Source code in `vllm/benchmarks/serve.py`


##

`fetch_spec_decode_metrics(base_url, session)`

`async`

[¶](https://docs.vllm.ai#vllm.benchmarks.serve.fetch_spec_decode_metrics)

Fetch speculative decoding metrics from the server's Prometheus endpoint.

Returns None if speculative decoding is not enabled or metrics are not available.

## Source code in `vllm/benchmarks/serve.py`


##

`get_first_model_from_server(base_url, headers=None, ssl_context=None)`

`async`

[¶](https://docs.vllm.ai#vllm.benchmarks.serve.get_first_model_from_server)

Fetch the first model from the server's /v1/models endpoint.

## Source code in `vllm/benchmarks/serve.py`


##

`get_request(input_requests, request_rate, burstiness=1.0, ramp_up_strategy=None, ramp_up_start_rps=None, ramp_up_end_rps=None, self_timed=False)`

`async`

[¶](https://docs.vllm.ai#vllm.benchmarks.serve.get_request)

Asynchronously generates requests at a specified rate with OPTIONAL burstiness and OPTIONAL ramp-up strategy.

Parameters:

-

(`input_requests`

[¶](https://docs.vllm.ai#vllm.benchmarks.serve.get_request(input_requests))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[SampleRequest](https://docs.vllm.ai/datasets/#vllm.benchmarks.datasets.SampleRequest)]A list of input requests, each represented as a SampleRequest.

-

(`self_timed`

[¶](https://docs.vllm.ai#vllm.benchmarks.serve.get_request(self_timed))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –If True, the requests carry their own arrival timing and no request rate, burstiness or ramp-up is applied.

-

(`request_rate`

[¶](https://docs.vllm.ai#vllm.benchmarks.serve.get_request(request_rate))

) –[float](https://docs.python.org/3/builtins/functions.html#float)The rate at which requests are generated (requests/s).

-

(`burstiness`

[¶](https://docs.vllm.ai#vllm.benchmarks.serve.get_request(burstiness))`optional`

, default:`1.0`

) –The burstiness factor of the request generation. Only takes effect when request_rate is not inf. Default value is 1, which follows a Poisson process. Otherwise, the request intervals follow a gamma distribution. A lower burstiness value (0 < burstiness < 1) results in more bursty requests, while a higher burstiness value (burstiness > 1) results in a more uniform arrival of requests.

-

(`ramp_up_strategy`

[¶](https://docs.vllm.ai#vllm.benchmarks.serve.get_request(ramp_up_strategy))`optional`

, default:`None`

) –The ramp-up strategy. Can be "linear" or "exponential". If None, uses constant request rate (specified by request_rate).

-

(`ramp_up_start_rps`

[¶](https://docs.vllm.ai#vllm.benchmarks.serve.get_request(ramp_up_start_rps))`optional`

, default:`None`

) –The starting request rate for ramp-up.

-

(`ramp_up_end_rps`

[¶](https://docs.vllm.ai#vllm.benchmarks.serve.get_request(ramp_up_end_rps))`optional`

, default:`None`

) –The ending request rate for ramp-up.


## Source code in `vllm/benchmarks/serve.py`


|
|