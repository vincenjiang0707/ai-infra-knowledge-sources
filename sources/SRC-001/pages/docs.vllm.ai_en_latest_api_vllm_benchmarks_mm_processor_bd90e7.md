source: https://docs.vllm.ai/en/latest/api/vllm/benchmarks/mm_processor/
lastmod: 2026-09-23

#

`vllm.benchmarks.mm_processor`

[¶](https://docs.vllm.ai#vllm.benchmarks.mm_processor)

Benchmark multimodal processor latency.

This benchmark measures the latency of the mm processor module using multimodal prompts from datasets. MM processor stats are automatically enabled.

## Run

vllm bench mm-processor \ --model

Functions:

-
–[add_cli_args](https://docs.vllm.ai#vllm.benchmarks.mm_processor.add_cli_args)Add CLI arguments for the multimodal processor benchmark.

-
–[benchmark_multimodal_processor](https://docs.vllm.ai#vllm.benchmarks.mm_processor.benchmark_multimodal_processor)Run the multimodal processor benchmark.

-
–[calculate_mm_processor_metrics](https://docs.vllm.ai#vllm.benchmarks.mm_processor.calculate_mm_processor_metrics)Calculate aggregate metrics from stats by stage.

-
–[collect_mm_processor_stats](https://docs.vllm.ai#vllm.benchmarks.mm_processor.collect_mm_processor_stats)Collect multimodal processor timing stats.

-
–[get_timing_stats_from_engine](https://docs.vllm.ai#vllm.benchmarks.mm_processor.get_timing_stats_from_engine)Get all multimodal timing stats from the LLM engine.

-
–[main](https://docs.vllm.ai#vllm.benchmarks.mm_processor.main)Main entry point for the multimodal processor benchmark.

-
–[validate_args](https://docs.vllm.ai#vllm.benchmarks.mm_processor.validate_args)Validate command-line arguments for mm_processor benchmark.


##

`add_cli_args(parser)`

[¶](https://docs.vllm.ai#vllm.benchmarks.mm_processor.add_cli_args)

Add CLI arguments for the multimodal processor benchmark.

## Source code in `vllm/benchmarks/mm_processor.py`


|
|

##

`benchmark_multimodal_processor(args)`

[¶](https://docs.vllm.ai#vllm.benchmarks.mm_processor.benchmark_multimodal_processor)

Run the multimodal processor benchmark.

## Source code in `vllm/benchmarks/mm_processor.py`


|
|

##

`calculate_mm_processor_metrics(stats_by_stage, selected_percentiles, *, unit='ms')`

[¶](https://docs.vllm.ai#vllm.benchmarks.mm_processor.calculate_mm_processor_metrics)

Calculate aggregate metrics from stats by stage.

## Source code in `vllm/benchmarks/mm_processor.py`


##

`collect_mm_processor_stats(llm_engine)`

[¶](https://docs.vllm.ai#vllm.benchmarks.mm_processor.collect_mm_processor_stats)

Collect multimodal processor timing stats. Returns a dictionary mapping stage names to lists of timing values (in seconds).

## Source code in `vllm/benchmarks/mm_processor.py`


##

`get_timing_stats_from_engine(llm_engine)`

[¶](https://docs.vllm.ai#vllm.benchmarks.mm_processor.get_timing_stats_from_engine)

Get all multimodal timing stats from the LLM engine.

Collects both preprocessing stats (HF processor, hashing, cache lookup, prompt update) and encoder forward pass timing, merged by request_id.

Parameters:

Returns:

-

–[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[float](https://docs.python.org/3/builtins/functions.html#float)]]Dictionary mapping request_id to merged stats dict containing

-

–[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[float](https://docs.python.org/3/builtins/functions.html#float)]]both preprocessing and encoder timing metrics.


## Example

{ 'request-123': { 'get_mm_hashes_secs': 0.02, 'get_cache_missing_items_secs': 0.01, 'apply_hf_processor_secs': 0.45, 'merge_mm_kwargs_secs': 0.01, 'apply_prompt_updates_secs': 0.03, 'preprocessor_total_secs': 0.51, 'encoder_forward_secs': 0.23, 'num_encoder_calls': 1 } }

## Source code in `vllm/benchmarks/mm_processor.py`


##

`main(args)`

[¶](https://docs.vllm.ai#vllm.benchmarks.mm_processor.main)

Main entry point for the multimodal processor benchmark.

## Source code in `vllm/benchmarks/mm_processor.py`


|
|

##

`validate_args(args)`

[¶](https://docs.vllm.ai#vllm.benchmarks.mm_processor.validate_args)

Validate command-line arguments for mm_processor benchmark.