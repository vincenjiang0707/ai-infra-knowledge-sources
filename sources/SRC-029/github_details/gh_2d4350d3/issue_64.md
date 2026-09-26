# [Issue #64] Detokenize error

source: https://github.com/AI-Hypercomputer/JetStream/issues/64
state: closed | updated: 2024-04-29T22:07:59Z
labels: 

## 正文

There might be a bug in the client detokenize operation.

Command
```
python JetStream/benchmarks/benchmark_serving.py \
--tokenizer maxtext/assets/tokenizer.llama2 \
--model llama2-7b \
--num-prompts 1000  \
--dataset sharegpt \
--dataset-path ~/ShareGPT_V3_unfiltered_cleaned_split.json \
--max-output-length 1024 \
--request-rate 5 \
--warmup-first true \
--save-result \
--save-request-outputs \
--run-eval true
```
Error
```
Traceback (most recent call last):
  File "/home/yeandy/JetStream/benchmarks/benchmark_serving.py", line 782, in <module>
    main(parsed_args)
  File "/home/yeandy/JetStream/benchmarks/benchmark_serving.py", line 565, in main
    benchmark_result, request_outputs = asyncio.run(
  File "/usr/lib/python3.10/asyncio/runners.py", line 44, in run
    return loop.run_until_complete(main)
  File "/usr/lib/python3.10/asyncio/base_events.py", line 649, in run_until_complete
    return future.result()
  File "/home/yeandy/JetStream/benchmarks/benchmark_serving.py", line 450, in benchmark
    outputs = await asyncio.gather(*tasks)
  File "/home/yeandy/JetStream/benchmarks/benchmark_serving.py", line 407, in send_request
    generated_token_list, ttft, latency = await grpc_async_request(
  File "/home/yeandy/JetStream/benchmarks/benchmark_serving.py", line 384, in grpc_async_request
    token_list.extend(sample_list.response[0].token_ids)
AttributeError: 'str' object has no attribute 'token_ids'
```

## 评论 (2)

### yeandy · 2024-04-29

cc: @JoeZijunZhou 

### JoeZijunZhou · 2024-04-29

Can you run `pip install -e .` with JetStream, `AttributeError: 'str' object has no attribute 'token_ids'` this is becuz the jetstream the latest version is not installed in your local with your jetstream maxtext server.
