# [Issue #4539] [Feature] Support AWQ models quantized with 'llm-compressor' framework

source: https://github.com/InternLM/lmdeploy/issues/4539
state: closed | updated: 2026-04-24T03:15:08Z
labels: 

## 正文

### Motivation

Currently only AWQ models quantized with 'AutoAWQ' framework [1] are supported by 'lmdeploy'.
The AutoAWQ framework is deprecated, so many recent AWQ models on HF model repo are quantized with its successor 'llm-compressor' [2].
For example, the Qwen3-VL models by 'cynkiwi' (e.g. the 4B model [3]) are all quantized with 'llm-compressor'.
One can see which framework was used in the 'config.json' of the downloaded model, in key 'quant_method'.
For new 'llm-compressor' framework, its value is 'compressed-tensors'.

So it would be great if llmdeploy could support also AWQ models quantized with 'llm-compressor' framework.

References:
[1] https://docs.vllm.ai/en/latest/features/quantization/auto_awq/
[2] https://github.com/vllm-project/llm-compressor
[3] https://huggingface.co/cyankiwi/Qwen3-VL-4B-Instruct-AWQ-4bit/

### Related resources

_No response_

### Additional context

_No response_

## 评论 (3)

### lvhan028 · 2026-04-21

Hope the following guide can provide some help.
https://lmdeploy.readthedocs.io/en/latest/quantization/llm_compressor.html

### hfassold · 2026-04-21

Oh, I see so it is already supported (partially?). But the AWQ model at [1] doesn’t load with TurboMindEngine.

[1] https://huggingface.co/cyankiwi/Qwen3-VL-4B-Instruct-AWQ-4bit/

### lvhan028 · 2026-04-23

Not all models quantized with llm-compressor are currently supported by the TurboMind engine. LMDeploy will continue to follow up and expand support for the llm-compressor project.
