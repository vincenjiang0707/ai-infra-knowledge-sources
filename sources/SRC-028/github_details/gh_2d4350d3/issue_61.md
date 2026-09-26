# [Issue #61] float division by zero in benchmark 

source: https://github.com/AI-Hypercomputer/JetStream/issues/61
state: open | updated: 2024-04-26T22:40:55Z
labels: 

## 正文

Command:

` python benchmarks/benchmark_serving.py --tokenizer /home//data/tokenizer.model --num-prompts 300  --dataset-path  /home//data/ShareGPT_V3_unfiltered_cleaned_split.json --dataset sharegpt --save-request-outputs`
 

Logs: 

> File "/home//JetStream/benchmarks/benchmark_serving.py", line 778, in <module>
>     main(parsed_args)
>   File "/home//JetStream/benchmarks/benchmark_serving.py", line 574, in main
>     benchmark_result, request_outputs = asyncio.run(
>   File "/usr/lib/python3.10/asyncio/runners.py", line 44, in run
>     return loop.run_until_complete(main)
>   File "/usr/lib/python3.10/asyncio/base_events.py", line 649, in run_until_complete
>     return future.result()
>   File "/home//JetStream/benchmarks/benchmark_serving.py", line 453, in benchmark
>     metrics = calculate_metrics(
>   File "/home//JetStream/benchmarks/benchmark_serving.py", line 343, in calculate_metrics
>     per_token_latencies.append(outputs[i].latency / output_len)
> ZeroDivisionError: float division by zero

## 评论 (2)

### FanhaiLu1 · 2024-04-25

More logs after skip zero output: 

only 2 of 300 had zero length
-------- output_len is zero for 238th request
-------- output_len is zero for 288th request



### JoeZijunZhou · 2024-04-26

Investigating internally.
