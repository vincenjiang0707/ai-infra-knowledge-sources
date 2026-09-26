# [Issue #410] Wide range of metrics (rpm,e2el) compared to other solutions

source: https://github.com/triton-inference-server/perf_analyzer/issues/410
state: open | updated: 2025-07-22T21:07:12Z
labels: 

## 正文

I compared benchmarks of the same model with different tools: llmperf, genaiperf and vllm/benchmarks. And I got different rpm results everywhere. 

The spread, especially on 50 threads, is very large. And then it doesn't seem to decrease, which seems strange.

Qwen2.5-72b-awq model was started on its my server.

Genai-perf 
Request Throughput (per sec),2.83
RPM = 2.83 * 60 = ~170

LLMPerf
 "results_num_completed_requests_per_min": 95.78302671905037,

vllm/benchmarks
Request throughput (req/s):              2.30
RPM = 2.3 * 60 = ~138

Datasets were used by sonnet, as it is in tools. input tokens = 300, output tokens = 200, stddev = 0, duration_sec = 60, MAX_NUM_COMPLETED_REQUESTS=600

```bash
# vllm, DATASET_NAME=sonnet
    python benchmark_serving.py \
        --backend openai-chat \
        --model "${MODEL}" \
        --host ${LLM_HOST} \
        --port ${LLM_PORT} \
        --endpoint /v1/chat/completions \
        --dataset-name ${DATASET_NAME} \
        --dataset-path ./sonnet.txt \
        --max-concurrency 50 \
        --save-result \
        --save-detailed \
        --result-dir "${OUTPUT_DIR}/${folder}" \
        --percentile-metrics ttft,tpot,itl,e2el \
        --metric-percentiles "50,90,95,99" \
        --${DATASET_NAME}-input-len $INPUT_SEQUENCE_LENGTH \
        --${DATASET_NAME}-output-len $OUTPUT_SEQUENCE_LENGTH \
        --num-prompts ${MAX_NUM_COMPLETED_REQUESTS} \
        --ignore-eos \
        --goodput e2el:${DURATION_MSEC}

# llmperf
    python token_benchmark_ray.py \
        --model "${MODEL}" \
        --mean-input-tokens ${INPUT_SEQUENCE_LENGTH} --stddev-input-tokens ${STDDEV} \
        --mean-output-tokens ${OUTPUT_SEQUENCE_LENGTH} --stddev-output-tokens ${STDDEV} \
        --max-num-completed-requests ${MAX_NUM_COMPLETED_REQUESTS} \
        --num-concurrent-requests 50 \
        --timeout ${DURATION_SEC} \
        --results-dir "${OUTPUT_DIR}/${folder}" \
        --llm-api openai \
        --additional-sampling-params '{"ignore_eos": true}'

# genaiperf, MAX_NUM_COMPLETED_REQUESTS=100
      genai-perf analyze --random-seed ${seed}
      --service-kind openai --endpoint-type chat --streaming
      --url ${llm_host} -m ${model}
      --extra-inputs ignore_eos:true
      --extra-inputs max_tokens:${output_sequence_length}
      --extra-inputs min_tokens:${output_sequence_length}
      --output-tokens-mean ${output_sequence_length} --output-tokens-stddev ${stddev}
      --synthetic-input-tokens-mean ${input_sequence_length} --synthetic-input-tokens-stddev ${stddev}
      -v --measurement-interval ${duration_msec}
      --warmup-request-count 10
      --num-dataset-entries ${MAX_NUM_COMPLETED_REQUESTS}
      --profile-export-file ${input_sequence_length}_${output_sequence_length}.json
      --sweep-type concurrency --sweep-list 50,100
```

Qwen3 - without thinking (concurrency=1,3,5,8,13,21,34,55,89,144, MAX_NUM_COMPLETED_REQUESTS=100):

![Image](https://github.com/user-attachments/assets/63b3ae68-7f59-4006-aefb-0210a825aee9)

At the same time, the vlm service counters show 135 revolutions per minute, when 143 requests were processed during the processing of the service. llmperf counts 35 rpm at the same time. genai-perf writes 102 rpm at 144 and vllm - 109 in graphane. That is, it seems genai-perf seems to give out more truthful values, but I still don't understand - I compared them using formulas and implementations. It seems that there should be no such differences.
Formula: `rate(vllm:request_success_total[$__rate_interval]) * 60`

![Image](https://github.com/user-attachments/assets/1ade6c60-5fd8-47d9-b328-81ab6e82b4b8)

Can you tell me what this could be related to?

## 评论 (3)

### psydok · 2025-07-03

At same time, response time increases for all tools. therefore, decrease in rpm from llmperf seems to justify it. but vllm's rpm does not change (if you do not look at what metrics inside vllm-service give out), while genai-perf's rpm, on the contrary, is still growing. This is all about same dataset (sonnet) and size of input and output tokens.

![Image](https://github.com/user-attachments/assets/72b55447-7019-44b4-a006-cb22d9013dc6)



### psydok · 2025-07-20

Sorry, more indicative RPM chart turned out to be 300/200 = input/output tokens.

Problem is that I don't understand why this is happening. If you don't control --num-dataset-returns, you get a red line that is significantly superior to other tests. But if --num-dataset-returns is set to a number higher than the expected number of completed queries, then a green line will be obtained, which is significantly lower than all other tests obtained by other tools. 

I don't understand how to justify/prove to myself that other tools are lying, or do I somehow misunderstand genai-perf?

![Image](https://github.com/user-attachments/assets/4d0b85a0-915d-43cc-9a4c-7ce6d4fcbd1d)

### debermudez · 2025-07-22

hey @psydok. sorry for the delayed response.

Can you please provide the command lines that generated the profiles for the red and green lines above? I am having a hard time understanding fully the command that generated your results in the graph.

