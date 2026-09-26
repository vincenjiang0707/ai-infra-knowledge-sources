# [Issue #374] image_url in OpenAI API benchmarks

source: https://github.com/triton-inference-server/perf_analyzer/issues/374
state: open | updated: 2025-06-17T00:39:50Z
labels: 

## 正文

What will be genai-perf command to send such requests with predefined concurrency?

```bash
curl http://localhost:8333/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "llava-hf/llava-1.5-7b-hf",
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "What is in this image?"
          },
          {
            "type": "image_url",
            "image_url": {
              "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
            }
          }
        ]
      }
    ],
    "max_tokens": 300
  }'
```

This curl is based on API chat definition with image example:

https://platform.openai.com/docs/api-reference/chat/create


You can start vLLM with this endpoint to run this request:

```
vllm serve llava-hf/llava-1.5-7b-hf --port 8333
```


## 评论 (7)

### piotrm-nvidia · 2025-05-08

The image_url passing is not supported but you can use synthetic image generator in ``genai-perf`` with these parameters:

```bash
    --endpoint-type vision \
    --image-width-mean 640 \
    --image-height-mean 424 \
    --image-width-stddev 0 \
    --image-height-stddev 0 \
```
The mean and stddev can be adjusted to generate different image sizes and vision endpoints can be used with ``genai-perf``.


This will produce request with synthetic image encoded as data URI similar to example below:

```json
    "messages": [
            {
              "role": "user",
              "content": [
                {
                  "type": "text",
                  "text": "uth had not provoked him to it The King had cut off my head with my brothers What are there no posts dispatched for Ireland How shall we do for money for these wars Come sistercousin I would say pray pardon me Go fellow get thee home provide all this Condem"
                },
                {
                  "type": "image_url",
                  "image_url": {
                    "url": "data:image/png;base64,iVBORw0KGgoAAAANSUhEU..."
                }
            }
```

The full benchmark script can be found here:

```bash
genai-perf profile -m llava-hf/llava-1.5-7b-hf \
    --tokenizer llava-hf/llava-1.5-7b-hf \
    --service-kind openai \
    --endpoint-type vision \
    --image-width-mean 640 \
    --image-height-mean 424 \
    --image-width-stddev 0 \
    --image-height-stddev 0 \
    --endpoint v1/chat/completions \
    --url 127.0.0.1:8333 \
    --streaming --concurrency 16 \
    --num-dataset-entries 64 \
    --warmup-request-count 32 \
    --request-count 32 \
    --synthetic-input-tokens-mean 3000 \
    --synthetic-input-tokens-stddev 0 \
    --output-tokens-mean 150 \
    --output-tokens-stddev 0 \
    --extra-inputs min_tokens:150 \
    --extra-inputs max_tokens:150 \
    --extra-inputs ignore_eos:true \
    --random-seed 0 \
    --artifact-dir llava1.6_7B_vision_640x424/vllm_tp1dp1/concurrency_16 \
    --profile-export-file profile_export_concurrency_16.json \
    -- --max-threads 64
```

This will produce results similar to below:

```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━┓
┃                         Statistic ┃      avg ┃      min ┃      max ┃      p99 ┃      p90 ┃      p75 ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━┩
│          Time To First Token (ms) │   939.24 │   182.51 │ 1,690.35 │ 1,686.18 │ 1,582.01 │ 1,324.19 │
│         Time To Second Token (ms) │   766.25 │    21.14 │ 1,521.64 │ 1,520.21 │ 1,409.15 │ 1,145.33 │
│              Request Latency (ms) │ 4,330.32 │ 4,322.60 │ 4,337.91 │ 4,337.83 │ 4,337.15 │ 4,336.76 │
│          Inter Token Latency (ms) │    22.62 │    17.64 │    27.65 │    27.63 │    26.89 │    25.13 │
│   Output Sequence Length (tokens) │   150.91 │   150.00 │   151.00 │   151.00 │   151.00 │   151.00 │
│    Input Sequence Length (tokens) │ 3,000.09 │ 3,000.00 │ 3,001.00 │ 3,001.00 │ 3,000.00 │ 3,000.00 │
│ Output Token Throughput (per sec) │   557.49 │      N/A │      N/A │      N/A │      N/A │      N/A │
│      Request Throughput (per sec) │     3.69 │      N/A │      N/A │      N/A │      N/A │      N/A │
│             Request Count (count) │    32.00 │      N/A │      N/A │      N/A │      N/A │      N/A │
└───────────────────────────────────┴──────────┴──────────┴──────────┴──────────┴──────────┴──────────┘
```


### piotrm-nvidia · 2025-05-08

I found those parameters in this document:

https://github.com/triton-inference-server/perf_analyzer/blob/ff8a4ad9dc4b043515d304855c6010fd83086a55/genai-perf/docs/multi_modal.md

It is not merged into main branch.

### nv-hwoo · 2025-05-08

You can find the doc in the main branch as well: https://github.com/triton-inference-server/perf_analyzer/blob/main/genai-perf/docs/multi_modal.md

### nzarif · 2025-05-14

Hi,

Thanks @piotrm-nvidia and @nv-hwoo for the guidelines and tips on profiling VLMs with `genai-perf`. I am trying to profile a variation of internVL that I am serving with Triton. My Triton package includes an ensemble that has been generated following the steps here: https://github.com/triton-inference-server/tensorrtllm_backend/blob/main/docs/multimodal.md
I can use a curl command like the one below to send requests to my model:

`curl -X POST localhost:8000/v2/models/vlm/generate -d '{"text_input":"MY_PROMPT", "max_tokens":64, "image_url_input": "URL_TO_IMG"}'`

In order to profile my model with genai-perf I am launching it through the Triton server [OpenAI-Compatible Frontend](https://github.com/triton-inference-server/server/tree/main/python/openai) and I am using TensorrtLLM as backend.

I used a `genai-perf` command similar to what @piotrm-nvidia suggested. I  can see the input.json file generated by genai-perf meets the formatting suggested above. But when `genai-perf` calls `perf_analyzer` the command fails and model return 400 error:

```
Running Perf Analyzer : 'perf_analyzer -m vlm--async               common.py:184
                               --stability-percentage 999 --warmup-request-count 32 --request-count 32 -i http -u                     
                               0.0.0.0:9000 --concurrency-range 16 --service-kind openai --endpoint v1/chat/completions               
                               --max-threads 64 --input-data                                                                          
                               artifacts/vlm-openai-vision-concurrency16/inputs.json                            
                               --profile-export-file                                                                                  
                               artifacts/vlm-openai-vision-concurrency16/profile_export.json'                   
Failed to retrieve results from inference request.
Thread [0] had error: OpenAI response returns HTTP code 400: {"detail":"only text message is supported, but got image_url"}
```

I thought this may be a problem with Triton's OpenAI-Compatible frontend so I tried launching directly with Triton, no frontend. In that scenario I provide the correct url and endpoint to `genai-perf` as:
`--endpoint v2/models/vlm/generate     --url 0.0.0.0:8000 `
The `perf_analyzer` call fails here too. Again 400 error, without any extra explanation:
```
Running Perf Analyzer : 'perf_analyzer -m vlm --async               common.py:184
                               --stability-percentage 999 --warmup-request-count 32 --request-count 32 -i http -u                     
                               0.0.0.0:8000 --concurrency-range 16 --service-kind openai --endpoint                                   
                               v2/models/vlm/generate --max-threads 64 --input-data                             
                               artifacts/vlm-openai-vision-concurrency16/inputs.json                            
                               --profile-export-file                                                                                  
                               artifacts/vlm-openai-vision-concurrency16/profile_export.json'                   
Failed to retrieve results from inference request.
Thread [0] had error: OpenAI response returns HTTP code 400:
```

Can you please help me with profiling a VLM when it's launched as a Triton ensemble using the trtllm-backend?


### nv-hwoo · 2025-05-15

Hi @nzarif, could you create a separate issue and add a minimal repro? This would allow us to take a closer look at it.

### nzarif · 2025-05-15

> Hi [@nzarif](https://github.com/nzarif), could you create a separate issue and add a minimal repro? This would allow us to take a closer look at it.

Thank for your quick response. Sure, I will create a new issue.

### huijiao1120 · 2025-06-17

Hi, wondering is it possible to support multiple images per request? currently only 1 image per request is supported. thanks!
