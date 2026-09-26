# [Issue #382] genai_perf not working with sglang pd disaggregation.

source: https://github.com/triton-inference-server/perf_analyzer/issues/382
state: closed | updated: 2025-05-16T12:11:38Z
labels: 

## 正文

When I use genai-perf to test the pd disaggregation feature of the sglang framework, the program hangs during the `perf_analyzer` phase.
Additionally, genai-perf performs well with sglang when using pd aggregation or in non-streaming mode. 
here is the command and some logger info.
`genai-perf profile -m qwen --service-kind openai --url 0.0.0.0:8890 --input-file /data/calibrate_text_1024.json --endpoint-type chat --tokenizer /models           --extra-inputs max_tokens:512 --extra-inputs top_p:1 --streaming --measurement-interval 1000 --artifact-dir /artifacts/h200-1p1d-32b-1024 --concurrency 4
root@msxf-hpc-37-2-ai:/artifacts# genai-perf profile -m qwen --url 0.0.0.0:8890 --input-file /data/calibrate_text_1024.json --endpoint-type chat --tokenizer /models           --extra-inputs max_tokens:512 --extra-inputs top_p:1 --streaming --measurement-interval 1000 --artifact-dir /artifacts/h200-1p1d-32b-1024 --concurrency 4
[2025-05-16 11:24:21] DEBUG    Input source is the following path: /data/calibrate_text_1024.json                                                                                                                                                                          config_input.py:190
[2025-05-16 11:24:21] INFO     Profiling these models: qwen                                                                                                                                                                                                                create_config.py:57
[2025-05-16 11:24:21] INFO     args.fun                                                                                                                                                                                                                                             main.py:45
[2025-05-16 11:24:23] INFO     Running Perf Analyzer : 'perf_analyzer -m qwen --async --stability-percentage 999 --warmup-request-count 0 --measurement-interval 1000 -i http -u 0.0.0.0:8890 --concurrency-range 4 --service-kind openai --endpoint v1/chat/completions         common.py:184
                               --input-data /artifacts/h200-1p1d-32b-1024/qwen-openai-chat-concurrency4/inputs.json --profile-export-file /artifacts/h200-1p1d-32b-1024/qwen-openai-chat-concurrency4/profile_export.json'
WARNING: Pass contained only one request, so sample latency standard deviation will be infinity (UINT64_MAX).`

Finally, I noticed that the JSON output from sglang with pd disaggregation ends with \n instead of \n\n, which seems to be a formatting issue. I have already fixed that, but the program still hangs and does not proceed to the result parsing step.








## 评论 (1)

### soyail · 2025-05-16

Finally I solved this issue. please modify sglang/srt/disaggregation/mini_lb.py
`async for chunk in decode_response.content:
     if chunk==b"\n":
         continue
     if chunk.startswith(b"data:") and not chunk.endswith(b"\n\n"):
         chunk = chunk.rstrip(b"\n")+b"\n\n"
    yield chunk`

