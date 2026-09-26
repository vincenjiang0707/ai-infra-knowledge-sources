# [Issue #3154] [Feature] Layerwise Error Reporting

source: https://github.com/vllm-project/llm-compressor/issues/3154
state: open | updated: 2026-09-18T06:38:05Z
labels: enhancement

## 正文

## Background ##
When quantizing models, it can sometimes be difficult to measure the effect of quantization and to validate that a quantization was successful. While algorithms such as GPTQ will report the apparent local error from applying the algorithm, other algorithms do not, and local error reporting is not reflective of the effect on output activations.

Related to/ fixes https://github.com/vllm-project/llm-compressor/issues/2031

## Request ##
Add a `log_sequential_error` option to `oneshot`. This option, when enabled, reports the MSE/SQNR between layer outputs after each sequential subgraph is compressed.

This will involve
* Capturing [unquantized outputs](https://github.com/vllm-project/llm-compressor/blob/main/src/llmcompressor/pipelines/sequential/pipeline.py#L153) when enabled
* Comparing with [quantized outputs](https://github.com/vllm-project/llm-compressor/blob/main/src/llmcompressor/pipelines/sequential/pipeline.py#L173) when enabled

Remaining questions
* How do we filter the outputs to only include the main activation (maybe check the largest tensor?)
* How do we handle when the sequential target is a Linear layer rather than a Decoder layer?

## 评论 (2)

### dichn · 2026-09-09

@kylesayrs I'd like to work on this issue.

### kylesayrs · 2026-09-11

@dichn FYI I've updated this ticket to use SQNR because, as @HDCharles points out, KL-divergence is for comparing probability distributions, whereas here we're calculating differences in values
