# [Issue #58] Benchmark serving: Failed to connect to remote host

source: https://github.com/AI-Hypercomputer/JetStream/issues/58
state: closed | updated: 2024-04-29T22:07:08Z
labels: 

## 正文

Several requests can be made at first, but then I see failed connection.



My command
```
python JetStream/benchmarks/benchmark_serving.py --tokenizer maxtext/assets/tokenizer.llama2 --model llama2-7b --num-prompts 1000 --dataset sharegpt --dataset-path /home/ml-auto-solutions/ShareGPT_V3_unfiltered_cleaned_split.json --max-output-length 1024 --request-rate 5 --warmup-first true --save-result --save-request-outputs --run-eval true
```
Console output
```
Making request
Making request
Making request
Making request
Making request
Making request
Making request
Making request
Making request
Making request
Making request
Making request
Making request
Making request
Traceback (most recent call last):
  File "/home/ml-auto-solutions/JetStream/benchmarks/benchmark_serving.py", line 775, in <module>
    main(parsed_args)
  File "/home/ml-auto-solutions/JetStream/benchmarks/benchmark_serving.py", line 558, in main
    benchmark_result, request_outputs = asyncio.run(
  File "/usr/lib/python3.10/asyncio/runners.py", line 44, in run
    return loop.run_until_complete(main)
  File "/usr/lib/python3.10/asyncio/base_events.py", line 649, in run_until_complete
    return future.result()
  File "/home/ml-auto-solutions/JetStream/benchmarks/benchmark_serving.py", line 443, in benchmark
    outputs = await asyncio.gather(*tasks)
  File "/home/ml-auto-solutions/JetStream/benchmarks/benchmark_serving.py", line 402, in send_request
    generated_token_list, ttft, latency = await grpc_async_request(
  File "/home/ml-auto-solutions/JetStream/benchmarks/benchmark_serving.py", line 377, in grpc_async_request
    async for token in response:
  File "/home/ml-auto-solutions/.env/lib/python3.10/site-packages/grpc/aio/_call.py", line 356, in _fetch_stream_responses
    await self._raise_for_status()
  File "/home/ml-auto-solutions/.env/lib/python3.10/site-packages/grpc/aio/_call.py", line 263, in _raise_for_status
    raise _create_rpc_error(
 grpc.aio._call.AioRpcError: <AioRpcError of RPC that terminated with:
	status = StatusCode.UNAVAILABLE
	details = "failed to connect to all addresses; last error: UNKNOWN: ipv4:0.0.0.0:9000: Failed to connect to remote host: Connection refused"
	debug_error_string = "UNKNOWN:Error received from peer  {created_time:"2024-04-25T20:07:40.338475547+00:00", grpc_status:14, grpc_message:"failed to connect to all addresses; last error: UNKNOWN: ipv4:0.0.0.0:9000: Failed to connect to remote host: Connection refused"}"
```

## 评论 (1)

### JoeZijunZhou · 2024-04-25

Would you also paste the server side log? Thanks!
