# [Issue #5079] [Feature]: Add dynamic per-token FC2 act scaling for TRTLLM FP8 per-channel MoE

source: https://github.com/flashinfer-ai/flashinfer/issues/5079
state: closed | updated: 2026-09-26T05:58:23Z
labels: feature request, needs-triage

## 正文

### Before submitting

- [x] I have searched existing issues and this request has not been filed yet.

### Problem

https://github.com/flashinfer-ai/flashinfer/issues/2419 requested FP8 MoE support with static per-channel weight scales and dynamic per-token act scales. https://github.com/flashinfer-ai/flashinfer/pull/2809 added the per-channel weight plumbing + new cubin with support from NVIDIA.

However the resulting implementation does not apply per-token quantization to the post-activation FC1 output consumed by FC2. The initial FC1 activation uses a per-token scale, but the intermediate activation is quantized using a single static scale and `userPerTokenScalingGemm2` is disabled.

The checkpoint semantics do not match this which I discovered while working on https://github.com/sgl-project/sglang/pull/38579 -- there are nice performance gains but the accuracy drops because the actual kernel is different. We need cubins for
- Routed/fused FC1, BF16 output, with both scale inputs
- Identity FC2, BF16 output, with both per-channel weight and per-token act scales.

### Requested outcome

Add support for FP8 MoE with static per-output-channel weight scales and dynamic per-token act scales for *both* FC1 and FC2 in TRTLLM backend. 
I am happy to do the wiring and plumbing changes but I will need support to get the new cubins.

### Target hardware

SM100 (B200, GB200)

### Inference engine

vLLM, SGLang

### Affected model or model family

Example: RedHatAI/Qwen3-30B-A3B-FP8-dynamic: https://huggingface.co/RedHatAI/Qwen3-30B-A3B-FP8-dynamic. Also applicable to   RedHatAI/Llama-4-Scout-17B-16E-Instruct-FP8-dynamic: https://huggingface.co/RedHatAI/Llama-4-Scout-17B-16E-Instruct-FP8-dynamic

### Workload and configuration

- Data type and quantization: E4M3 expert weights with static FP32 per-output channeel scales; E4M3 activations with dynamic FP32 per-token scales; BF16 model & mOE support
- Batch size or request concurrency: reasonable batch sizes (powers of 2)
- Sequence lengths or token counts: reasonable, should not matter
- Parallelism: TP / EP / DP / PP / disaggregated -- should not matter
- Relevant shapes: heads, head dimension, hidden size, experts, top-k, page size, or other -- should support reasonable MoE shapes etc
- Environment: output of `python -m flashinfer.collect_env` -- will get this later


### Current workaround

We use SGLang Triton MoE backend which dynamically quantizes the FC2 act per token. But you can see in my SGLang PR there are performance benefits starting from BS4 for using TRT-LLM backend. 

### Impact

Latency, Missing model or hardware support

### Acceptance criteria

Works for all reasonable shapes, we should probably be able to get very similar accuracy on relevant evals or something is wrong with the kernel again. But we probably need an updated cuin to start with.

### Related work, dependencies, or suggested scope

Linked earlier, it looks like this was overlooked earlier in my changes. I will open a PR for the plumbing changes alongside this issue.

### Timing or release need

_No response_

## 评论 (5)

### raayandhar · 2026-09-10

cc @Aneureka 

### Aneureka · 2026-09-14

Will look into this one.

### Aneureka · 2026-09-15

Added required cubins in #5149.

### raayandhar · 2026-09-16

Thanks, will update and test shortly.

### Aneureka · 2026-09-26

Closed as #5149 merged.
