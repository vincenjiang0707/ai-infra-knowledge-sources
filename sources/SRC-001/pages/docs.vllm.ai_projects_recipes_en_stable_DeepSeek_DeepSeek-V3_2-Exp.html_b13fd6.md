source: https://docs.vllm.ai/projects/recipes/en/stable/DeepSeek/DeepSeek-V3_2-Exp.html
lastmod: 2026-04-27

# DeepSeek-V3.2-Exp Usage Guide[¶](https://docs.vllm.ai#deepseek-v32-exp-usage-guide)

## Introduction[¶](https://docs.vllm.ai#introduction)

[DeepSeek-V3.2-Exp](https://huggingface.co/deepseek-ai/DeepSeek-V3.2-Exp) is a sparse attention model. The main architecture is similar to DeepSeek-V3.1, but with a sparse attention mechanism.

## Installing vLLM[¶](https://docs.vllm.ai#installing-vllm)

source .venv/bin/activate
uv pip install -U vllm --torch-backend auto
uv pip install git+https://github.com/deepseek-ai/[[email protected]](https://docs.vllm.ai/cdn-cgi/l/email-protection) --no-build-isolation # Other versions may also work. We recommend using the latest released version from https://github.com/deepseek-ai/DeepGEMM/releases


Note: DeepGEMM is used in two places: MoE and MQA logits computation. It is necessary for MQA logits computation. If you want to disable the MoE part, you can set `VLLM_USE_DEEP_GEMM=0`

in the environment variable. Some users reported that the performance is better with `VLLM_USE_DEEP_GEMM=0`

, e.g. on H20 GPUs. It might be also beneficial to disable DeepGEMM if you want to skip the long warmup.

## Launching DeepSeek-V3.2-Exp[¶](https://docs.vllm.ai#launching-deepseek-v32-exp)

### Serving on 8xH200 (or H20) GPUs (141GB × 8)[¶](https://docs.vllm.ai#serving-on-8xh200-or-h20-gpus-141gb-8)

Using the recommended EP/DP mode:

Using tensor parallel:

### Serving on 8xB200 GPUs[¶](https://docs.vllm.ai#serving-on-8xb200-gpus)

Same as the above.

Only Hopper and Blackwell data center GPUs are supported for now.

## Accuracy Benchmarking:[¶](https://docs.vllm.ai#accuracy-benchmarking)

lm-eval --model local-completions --tasks gsm8k --model_args model=deepseek-ai/DeepSeek-V3.2-Exp,base_url=http://127.0.0.1:8000/v1/completions,num_concurrent=100,max_retries=3,tokenized_requests=False


Results:

local-completions (model=deepseek-ai/DeepSeek-V3.2-Exp,base_url=http://127.0.0.1:8000/v1/completions,num_concurrent=100,max_retries=3,tokenized_requests=False), gen_kwargs: (None), limit: None, num_fewshot: None, batch_size: 1
|Tasks|Version| Filter |n-shot| Metric | |Value | |Stderr|
|-----|------:|----------------|-----:|-----------|---|-----:|---|-----:|
|gsm8k| 3|flexible-extract| 5|exact_match|↑ |0.9591|± |0.0055|
| | |strict-match | 5|exact_match|↑ |0.9591|± |0.0055|


GSM8K score `0.9591`

is pretty good!

And then we can use `num_fewshot=20`

to increase the context length, testing if the model can handle longer context:

lm-eval --model local-completions --tasks gsm8k --model_args model=deepseek-ai/DeepSeek-V3.2-Exp,base_url=http://127.0.0.1:8000/v1/completions,num_concurrent=100,max_retries=3,tokenized_requests=False --num_fewshot 20


Results:

local-completions (model=deepseek-ai/DeepSeek-V3.2-Exp,base_url=http://127.0.0.1:8000/v1/completions,num_concurrent=100,max_retries=3,tokenized_requests=False), gen_kwargs: (None), limit: None, num_fewshot: 20, batch_size: 1
|Tasks|Version| Filter |n-shot| Metric | |Value | |Stderr|
|-----|------:|----------------|-----:|-----------|---|-----:|---|-----:|
|gsm8k| 3|flexible-extract| 20|exact_match|↑ |0.9538|± |0.0058|
| | |strict-match | 20|exact_match|↑ |0.9530|± |0.0058|


GSM8K score `0.9538`

is also pretty good!

## Performance Tips[¶](https://docs.vllm.ai#performance-tips)

- The kernels are mainly optimized for TP=1, so it is recommended to run this model under EP/DP mode, i.e. DP=8, EP=8, TP=1 as shown above. If you hit any errors or hangs, try tensor parallel instead. Simple tensor parallel works and is more robust, but the performance is not optimal.
- The default config uses a custom
`fp8`

kvcache. You can also use`bfloat16`

kvcache by specifying`kv_cache_dtype=bfloat16`

. The default case allows more tokens to be cached in the kvcache, but incurs additional quantization/dequantization overhead. In general, we recommend using`bfloat16`

kvcache for short requests, and`fp8`

kvcache for long requests.

If you hit some errors like `CUDA error (flashmla-src/csrc/smxx/mla_combine.cu:201): invalid configuration argument`

, it might be caused by too large batchsize. Try with `--max-num-seqs 256`

or smaller (the default is 1024).

For other usage tips, such as enabling or disabling thinking mode, please refer to the DeepSeek-V3.1 Usage Guide.