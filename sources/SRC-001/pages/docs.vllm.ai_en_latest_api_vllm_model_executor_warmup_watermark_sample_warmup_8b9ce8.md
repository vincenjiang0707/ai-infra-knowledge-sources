source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/warmup/watermark_sample_warmup/
lastmod: 2026-09-24

#

`vllm.model_executor.warmup.watermark_sample_warmup`

[¶](https://docs.vllm.ai#vllm.model_executor.warmup.watermark_sample_warmup)

Warm up the watermarked sampler's Triton kernel.

`_philox_gumbel_kernel`

is JIT-compiled once per (key, logits dtype, skip-mask, `USE_FP64`

) specialization. The generic sampler warmup samples with `SamplingParams.for_sampler_warmup()`

, whose feature-heavy logits processing forces the fp32 copy in `apply_sampling_params`

, so the first ordinary temperature-1.0 request is the first launch with model-dtype logits and pays the compilation inside inference. This pre-compiles every specialization the sampler path can launch for the configured watermark.

##

`_philox_key(watermarker)`

[¶](https://docs.vllm.ai#vllm.model_executor.warmup.watermark_sample_warmup._philox_key)

None when the watermarker takes the torch path and compiles no kernel.

## Source code in `vllm/model_executor/warmup/watermark_sample_warmup.py`


##

`_philox_sampler_keys(watermarker)`

[¶](https://docs.vllm.ai#vllm.model_executor.warmup.watermark_sample_warmup._philox_sampler_keys)

Philox keys the sampler launches the kernel with.