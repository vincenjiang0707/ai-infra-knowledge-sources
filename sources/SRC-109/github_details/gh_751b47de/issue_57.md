# [Issue #57] Streaming always enabled for genai-perf

source: https://github.com/triton-inference-server/perf_analyzer/issues/57
state: closed | updated: 2024-08-27T17:57:02Z
labels: 

## 正文

Upon triggering genai-perf, streaming option is always enabled while making calling for triton service. 

Even without the --streaming flag, 
```
genai-perf \
                -m bls\
                -v \
                --service-kind triton \
                --backend tensorrtllm \
                --num-prompts 100 \
                --random-seed 1234 \
                --synthetic-input-tokens-mean 4000 \
                --synthetic-input-tokens-stddev 0 \
                --output-tokens-mean 32\
                --output-tokens-stddev 0 \
                --output-tokens-mean-deterministic \
                --concurrency 1 \
                --extra-inputs max_tokens:32 \
                --extra-inputs return_log_probs:false \
                --extra-inputs return_context_logits:false \
                --extra-inputs return_generation_logits:false \
                --extra-inputs beam_width:1 \
                --extra-inputs top_k:1 \
                --extra-inputs stream:false \
                --extra-inputs num_draft_tokens:4 \
                --measurement-interval 120000 \
                --tokenizer meta-llama/Meta-Llama-3-8B-Instruct \
                --url localhost:8001
```

Outputs the the command in the logs: 

`
perf_analyzer -m bls --async --input-data artifacts/bls-triton-tensorrtllm-concurrency1/llm_inputs.json --service-kind triton -u localhost:8001 --measurement-interval 120000 --stability-percentage 999 --profile-export-file artifacts/bls-triton-tensorrtllm-concurrency1/profile_export.json --verbose -i grpc --streaming --shape max_tokens:1 --shape text_input:1 --concurrency-range 1
`
(note the --streaming flag in perf_analyzer) 

This is because of this line of code which always adds --streaming in case the service is triton: 

https://github.com/triton-inference-server/perf_analyzer/blob/main/genai-perf/genai_perf/wrapper.py#L47

## 评论 (2)

### debermudez · 2024-08-27

@dhruvmullick that is very observant but is intentional.

Some background here to provide context:
GenAI-Perf builds on top of perf_analyzer (PA). PA had a streaming flag prior to the design of GenAI-Perf that controls which client methods are used at a lower level. In PA when profiling triton via grpc, we need that flag. 
The streaming flag from the context of GenAI-Perf controls whether or not to include streaming in the API payload and enables streaming behavior for the endpoint.

This overloading of the streaming flag is an complexity we need to improve on but should be operating correctly based on our testing. I would not expect this to affect the behavior of your profiling. However, if you are seeing issues, please let me know and we can investigate further. 

Thanks for using the tool!

### dhruvmullick · 2024-08-27

@debermudez, I see. Thanks for the note! 
