# [Issue #4499] Add TurboQuant Support for KV Cache Quantization

source: https://github.com/InternLM/lmdeploy/issues/4499
state: closed | updated: 2026-04-16T11:05:40Z
labels: 

## 正文

### Motivation

TurboQuant - optimisation to run LLMs at lower VRAM requirements

### Related resources

Is there a plan for TurboQuant support in near future?

https://github.com/vllm-project/vllm/issues/38171
https://github.com/Alberto-Codes/turboquant-vllm

### Additional context

_No response_

## 评论 (1)

### windreamer · 2026-04-07

Thanks for your interest in TurboQuant!

We have been working on TurboQuant K4V2 (K=4bit, V=2bit mixed precision) implementation, and a prototype has been merged in my dev branch (quant_policy=42) https://github.com/windreamer/lmdeploy/tree/turboquant-integration.

However, after initial testing, we found that currently we cannot clearly see the advantage of TurboQuant MSE-based K4V2 quantization compared to the traditional 4-bit min-max quantization in terms of perplexity or accuracy. We are still verifying whether the current implementation is correct and whether there are any issues with the quantization process.

Additionally, we are considering whether we should further introduce QJL (Quantization Jacobian Learning) for Key quantization to improve the quality. This is something we need to investigate further.

We will continue to evaluate and optimize this implementation. If you have any insights or suggestions, please feel free to share!
