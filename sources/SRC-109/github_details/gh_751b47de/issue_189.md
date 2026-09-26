# [Issue #189] KeyError: 'delta'

source: https://github.com/triton-inference-server/perf_analyzer/issues/189
state: closed | updated: 2024-12-17T20:35:18Z
labels: 

## 正文

I am using the image `nvcr.io/nvidia/tritonserver:24.10-py3-sdk`. I am using the following command:
```
genai-perf profile -m starcoder --url http://vllm-starcoder2-7b:8080 --service-kind openai --endpoint-type completions --backend vllm --streaming --extra-inputs stream:true  --extra-inputs max_tokens:10 --synthetic-input-tokens-mean 21 --synthetic-input-tokens-stddev 0 --output-tokens-mean 21 --output-tokens-stddev 0 --tokenizer bigcode/starcoder2-7b --verbose
```


However, I am getting the following error occasionally:
```
2024-11-21 03:14 [INFO] genai_perf.parser:83 - Profiling these models: starcoder
2024-11-21 03:14 [INFO] genai_perf.wrapper:162 - Running Perf Analyzer : 'perf_analyzer -m starcoder --async --input-data artifacts/starcoder-openai-completions-concurrency1/inputs.json -i http --concurrency-range 1 --endpoint v1/completions --service-kind openai -u http://vllm-starcoder2-7b:8080 --measurement-interval 10000 --stability-percentage 999 --profile-export-file artifacts/starcoder-openai-completions-concurrency1/profile_export.json --verbose'
 Successfully read data for 1 stream/streams with 100 step/steps.
*** Measurement Settings ***
  Service Kind: OPENAI
  Using "time_windows" mode for stabilization
  Stabilizing using average throughput
  Measurement window: 10000 msec
  Using asynchronous calls for inference

Request concurrency: 1
  Client:
    Request count: 271
    Throughput: 7.52739 infer/sec
    Avg latency: 132018 usec (standard deviation 3683 usec)
    p50 latency: 130863 usec
    p90 latency: 136896 usec
    p95 latency: 139360 usec
    p99 latency: 141404 usec
    Avg HTTP time: 132667 usec (send/recv 100849 usec + response wait 31818 usec)
Inferences/Second vs. Client Average Batch Latency
Concurrency: 1, throughput: 7.52739 infer/sec, latency 132018 usec
Traceback (most recent call last):
  File "/usr/local/lib/python3.10/dist-packages/genai_perf/main.py", line 214, in main
    run()
  File "/usr/local/lib/python3.10/dist-packages/genai_perf/main.py", line 206, in run
    data_parser = calculate_metrics(args, tokenizer)
  File "/usr/local/lib/python3.10/dist-packages/genai_perf/main.py", line 142, in calculate_metrics
    return LLMProfileDataParser(
  File "/usr/local/lib/python3.10/dist-packages/genai_perf/profile_data_parser/llm_profile_data_parser.py", line 75, in __init__
    super().__init__(filename, goodput_constraints)
  File "/usr/local/lib/python3.10/dist-packages/genai_perf/profile_data_parser/profile_data_parser.py", line 62, in __init__
    self._parse_profile_data(data)
  File "/usr/local/lib/python3.10/dist-packages/genai_perf/profile_data_parser/profile_data_parser.py", line 125, in _parse_profile_data
    metrics = self._parse_requests(requests)
  File "/usr/local/lib/python3.10/dist-packages/genai_perf/profile_data_parser/llm_profile_data_parser.py", line 94, in _parse_requests
    self._preprocess_response(res_timestamps, res_outputs)
  File "/usr/local/lib/python3.10/dist-packages/genai_perf/profile_data_parser/llm_profile_data_parser.py", line 208, in _preprocess_response
    merged_response["choices"][0]["delta"].get("content", None)
KeyError: 'delta'
2024-11-21 03:15 [ERROR] genai_perf.main:218 - 'delta'
```

## 评论 (4)

### ganeshku1 · 2024-11-21

@tjandy98  Can you please provide the reproduction steps to reproduce this on our end to debug this further.

### tjandy98 · 2024-11-21

> ```
> genai-perf profile -m starcoder --url http://vllm-starcoder2-7b:8080 --service-kind openai --endpoint-type completions --backend vllm --streaming --extra-inputs stream:true  --extra-inputs max_tokens:10 --synthetic-input-tokens-mean 21 --synthetic-input-tokens-stddev 0 --output-tokens-mean 21 --output-tokens-stddev 0 --tokenizer bigcode/starcoder2-7b --verbose
> ```

Hi @ganeshku1 , I provided the command used in the description. Please let me know if you need more information. Thank you.

### the-david-oy · 2024-11-21

Can you provide your server start command, so that we can check what's going on? If it's not an open-source server, is it conforming to the OpenAI standard?

Providing the profile export file would be helpful as well. The delta field is missing from it, so we could see what schema it's using instead.

### the-david-oy · 2024-12-17

Closing due to inactivity. If you would like to reopen the ticket, let us know.
