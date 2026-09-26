# [Issue #393] How are metrics calculated? (request count, rps, output token throughput)

source: https://github.com/triton-inference-server/perf_analyzer/issues/393
state: open | updated: 2025-07-20T17:54:00Z
labels: 

## 正文

How did you get 7 requests with concurrency=1, latency of 5 seconds and Measurement window=10 sec? Why didn't it turn out to be 2, and is there any way to set it up?

I don't write in C++, so could you help me find a piece of code that considers this and explain why?

```bash
docker run -it --net=host -p 8002:8002 --gpus all nvcr.io/nvidia/tritonserver:25.01-py3-sdk 

genai-perf profile  --random-seed 20250522  \
  -m Qwen/Qwen3-14B --service-kind openai --endpoint-type chat \
  --url myhost:8000 --streaming   \
    --output-tokens-mean 200  --synthetic-input-tokens-mean 4000 \
  -v --measurement-interval 10000 

2025-05-22 17:02 [INFO] genai_perf.parser:115 - Profiling these models: Qwen/Qwen3-14B
2025-05-22 17:02 [INFO] genai_perf.parser:416 - Model name 'Qwen/Qwen3-14B' cannot be used to create artifact directory. Instead, 'Qwen_Qwen3-14B' will be used.
2025-05-22 17:02 [INFO] genai_perf.subcommand.common:208 - Running Perf Analyzer : 'perf_analyzer -m Qwen/Qwen3-14B --async --input-data artifacts/Qwen_Qwen3-14B-openai-chat-concurrency1/inputs.json -i http --concurrency-range 1 --endpoint v1/chat/completions --service-kind openai -u myhost:8000 --request-count 0 --warmup-request-count 0 --verbose --profile-export-file artifacts/Qwen_Qwen3-14B-openai-chat-concurrency1/profile_export.json --measurement-interval 10000 --stability-percentage 999'
 Successfully read data for 1 stream/streams with 100 step/steps.
*** Measurement Settings ***
  Service Kind: OPENAI
  Using "time_windows" mode for stabilization
  Stabilizing using average throughput
  Measurement window: 10000 msec
  Using asynchronous calls for inference
Request concurrency: 1
  Client: 
    Request count: 7
    Throughput: 0.194439 infer/sec
    Avg latency: 4916707 usec (standard deviation 25716 usec)
    p50 latency: 4907654 usec
    p90 latency: 4919616 usec
    p95 latency: 4972587 usec
    p99 latency: 4972587 usec
    Avg HTTP time: 4920204 usec (send/recv 3732874 usec + response wait 1187330 usec)
Inferences/Second vs. Client Average Batch Latency
Concurrency: 1, throughput: 0.194439 infer/sec, latency 4916707 usec
                                    NVIDIA GenAI-Perf | LLM Metrics                                    
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━┓
┃                         Statistic ┃      avg ┃      min ┃      max ┃      p99 ┃      p90 ┃      p75 ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━┩
│          Time To First Token (ms) │ 1,193.02 │ 1,172.79 │ 1,245.92 │ 1,242.80 │ 1,214.77 │ 1,192.33 │
│         Time To Second Token (ms) │    18.08 │    16.88 │    18.89 │    18.88 │    18.74 │    18.42 │
│              Request Latency (ms) │ 4,916.71 │ 4,897.99 │ 4,972.59 │ 4,969.41 │ 4,940.80 │ 4,916.48 │
│          Inter Token Latency (ms) │    17.05 │    16.56 │    17.72 │    17.68 │    17.38 │    17.12 │
│   Output Sequence Length (tokens) │   219.43 │   211.00 │   226.00 │   225.76 │   223.60 │   221.00 │
│    Input Sequence Length (tokens) │ 3,999.86 │ 3,999.00 │ 4,000.00 │ 4,000.00 │ 4,000.00 │ 4,000.00 │
│ Output Token Throughput (per sec) │    44.63 │      N/A │      N/A │      N/A │      N/A │      N/A │
│      Request Throughput (per sec) │     0.20 │      N/A │      N/A │      N/A │      N/A │      N/A │
│             Request Count (count) │     7.00 │      N/A │      N/A │      N/A │      N/A │      N/A │
└───────────────────────────────────┴──────────┴──────────┴──────────┴──────────┴──────────┴──────────┘
2025-05-22 17:03 [INFO] genai_perf.export_data.json_exporter:62 - Generating artifacts/Qwen_Qwen3-14B-openai-chat-concurrency1/profile_export_genai_perf.json
2025-05-22 17:03 [INFO] genai_perf.export_data.csv_exporter:73 - Generating artifacts/Qwen_Qwen3-14B-openai-chat-concurrency1/profile_export_genai_perf.csv
```

## 评论 (8)

### debermudez · 2025-05-27

Hey @psydok. It would work something like this:

Lets assume 5 second latency for easier numbers

time window 1:
0: request
5: response - send new request
10: response - send new request
 
time window 2:
0: request outstanding
5: response - send new request
10: response - send new request

time window 3:
0: request
5: response - send new request
10: response - send new request

so requests are sent at 0, 5, 10, 15, 20, 25, 30 for a total of 7 requests.

If you want to control the number of requests, we recommend moving to --request-count.


### psydok · 2025-06-16


@debermudez  Thank you for your reply!
Could you please tell me why the time window was 3? Is there any way to control this?
I have suspicions about `--stability-percentage`, but I don't understand how to set it correctly if the default is 999.
Or do I need to set `--request-count 1`, then there will only be 1 time window?

### psydok · 2025-06-19

According to the code, it seemed necessary to set stability-percentage to 0 in order not to take into account the stabilization of measurements, but this returns an error:

```bash
genai-perf profile  --random-seed 12345 \
    -m Qwen/Qwen2.5-72B-Instruct-AWQ --service-kind openai --endpoint-type chat \
    --url ${LLM_HOST} --streaming   \
    --output-tokens-mean $OUTPUT_SEQUENCE_LENGTH  --output-tokens-stddev ${STDDEV} \
    --extra-inputs max_tokens:$OUTPUT_SEQUENCE_LENGTH \
    --extra-inputs min_tokens:$OUTPUT_SEQUENCE_LENGTH \
    --extra-inputs ignore_eos:true \
    --synthetic-input-tokens-mean $INPUT_SEQUENCE_LENGTH --synthetic-input-tokens-stddev ${STDDEV} \
    -v --measurement-interval ${DURATION_MSEC} \
    --profile-export-file ${INPUT_SEQUENCE_LENGTH}_${OUTPUT_SEQUENCE_LENGTH}_s0.json \
    --concurrency 1 \
    --stability-percentage 0 \
    --generate-plots

...
Failed to obtain stable measurement within 10 measurement windows for concurrency 1. Please try to increase the --measurement-interval.
Failed to obtain stable measurement.
```

image: nvcr.io/nvidia/tritonserver:25.03-py3-sdk

### psydok · 2025-06-19

I have another similar question about iterating through the parameters. I have not found an explanation for some limitations of the parameters in any article. I'll ask right here...
Do you know why I can't iterate through the concurrency in increments of 10, why do the values have to be in degrees?


```
genai-perf analyze ...  --sweep-type concurrency --sweep-range 50:100:10
...
  File "/usr/local/lib/python3.12/dist-packages/genai_perf/parser.py", line 324, in _process_sweep_args
    _check_sweep_range(args)
  File "/usr/local/lib/python3.12/dist-packages/genai_perf/parser.py", line 364, in _check_sweep_range
    raise argparse.ArgumentTypeError(
argparse.ArgumentTypeError: --sweep-range min/max values must be powers of 2 when sweeping concurrency
2025-06-19 11:20 [ERROR] genai_perf.main:58 - --sweep-range min/max values must be powers of 2 when sweeping concurrency
```

However, it works: --sweep-list 50,60,70,80,90,100

### debermudez · 2025-06-24

> Could you please tell me why the time window was 3? Is there any way to control this?

There is no way to control this. We use 3 to try to avoid a single request that might throw off the data.

I have suspicions about --stability-percentage, but I don't understand how to set it correctly if the default is 999.
>Or do I need to set --request-count 1, then there will only be 1 time window?

If you use `request-count`, we only worry about the number of requests. There is no notion of a window.


Stability percentage is defined in the options like this:

```

The allowed variation in latency measurements when determining if a result is stable. The measurement is considered as stable if the ratio of max / min from the recent 3 measurements is within (stability percentage) in terms of both infer per second and latency. (default: 999)
```
It is the ratio from max to min in the window timings. 
It is a relic of an older way of doing things, where 999 basically turns it off. 0 would make it basically impossible to reach stability and thus leads to the stability error you are seeing.


> genai-perf analyze ...  --sweep-type concurrency --sweep-range 50:100:10

Originally, users were only iterating via powers of two for concurrency so that was the feature implemented. 
But 
>--sweep-list 50,60,70,80,90,100
will give you what you want in behavior


### psydok · 2025-07-07

Thanks, it became clearer!

But I have one more question right there. I wrote `max_tokens: 200` wherever I could, but in the `Output Token Throughput (per sec)`it gives me `410.43`, while `Output Sequence Length (tokens),241.75'.
Output Token Throughput (per sec) - according to the description in the documentation, these are tokens for each thread (users), but in my tests I always got about 7-10 tokens per thread.
Can you tell me how to understand this?

I get strong discrepancies in the genaiperf metrics compared to other tools. I suspect that I'm missing something again...
I tried taking prompts like in genai perf and running other load tools on them. max_tokens was respected. But in genai perf, is it ignored, or is it not considered correctly?

```bash
# output_sequence_length=200
      genai-perf analyze --random-seed ${seed}
      --service-kind openai --endpoint-type chat --streaming
      --url ${llm_host} -m ${model}
      --extra-inputs ignore_eos:true
      --extra-inputs seed:${seed}
      --extra-inputs temperature:0
      --extra-inputs "{\"chat_template_kwargs\":{\"enable_thinking\":false}}"  
      --extra-inputs max_tokens:${output_sequence_length}
      --extra-inputs min_tokens:${output_sequence_length}
      --output-tokens-mean ${output_sequence_length} --output-tokens-stddev ${stddev}
      --synthetic-input-tokens-mean ${input_sequence_length} --synthetic-input-tokens-stddev ${stddev}
      -v --measurement-interval ${duration_msec}
      --warmup-request-count 10
      --num-dataset-entries ${max_number_of_unique_payloads}
      --profile-export-file ${input_sequence_length}_${output_sequence_length}.json
      --sweep-type concurrency --sweep-list ${threads} --generate-plots
```

P.S. I tried to specify `--extra-input"{\"stream_options\":{\"include_usage\":true}}"`, genaiperf could not summarize:
```
  File "/usr/local/lib/python3.12/dist-packages/genai_perf/profile_data_parser/llm_profile_data_parser.py", line 441, in _extract_openai_text_output
    completions = data["choices"][0]
                  ~~~~~~~~~~~~~~~^^^
IndexError: list index out of range
```

### psydok · 2025-07-07

There was immediately a question about RPS... Due to the fact that other solutions produce different results, I am trying to understand how the rps was obtained. According to the articles, I see that RPS is equal to `number of successful requests` divided by `(time of receiving last response - time of sending first request)`.
However, now I don't understand how `RPS = 0.2` turned out in my first example:
```
# ok?
Request count = 7 / 3 = 2
RPS = 2 / 10 sec = 0.23
```

But:
```
# --measurement-interval 60000 --request-count 500 --concurrency 144
Metric,avg,min,max,p99,p95,p90,p75,p50,p25
Time To First Token (ms),"32,688.40",936.53,"69,427.64","66,402.05","59,014.50","49,160.43","45,225.75","35,425.56","21,652.69"
Time To Second Token (ms),416.23,45.65,508.75,507.90,506.08,505.20,486.09,470.73,443.92
Request Latency (ms),"71,107.96","31,121.97","102,848.43","101,001.72","97,763.79","93,740.16","84,627.27","72,280.39","57,505.44"
Inter Token Latency (ms),159.59,121.85,257.25,239.76,214.06,205.23,184.28,144.32,134.63
Output Sequence Length (tokens),241.75,225.00,265.00,259.48,255.00,251.00,246.00,241.00,236.00
Input Sequence Length (tokens),"4,000.03","3,999.00","4,001.00","4,001.00","4,000.00","4,000.00","4,000.00","4,000.00","4,000.00"

Metric,Value
Output Token Throughput (per sec),410.43
Request Throughput (per sec),1.70
Request Count (count),353.00
```
Then (60s - approximately):
```
# no? in table - rps=1.7
Request count = 353 / 3 = 117
RPS = 117 / 60 = 1.96

# ???
RPS = 353 / 60 = 5,8
```


### psydok · 2025-07-20

@debermudez 
I'm very sorry, but could you take a look at this issue with graphs, maybe you know how to justify this behavior of genai-perf? And what things should other tools pay more attention to in order to better understand their difference from genai-perf?

I tried to compare approaches to formulas and the methods used to send requests, but I don't find anything critical.

https://github.com/triton-inference-server/perf_analyzer/issues/410#issuecomment-3094674770
