# [Issue #4484] [Feature]: Define empty KV attention semantics for output and LSE

source: https://github.com/flashinfer-ai/flashinfer/issues/4484
state: open | updated: 2026-09-21T04:45:35Z
labels: feature request, needs-triage

## 正文

### Before submitting

- [x] I have searched existing issues and this request has not been filed yet.

### Problem

Problem: 

DCP computes attention with glocal Q and local KV, then combines the partial output w/ LSE. In the local attention, effective KV for a query row can be empty because:
* The rank holds empty KV: `kv_len == 0`
* local KV exists, but causal or explicit masking excludes every key for that query

For online-softmax merging to treat the empty attention result as a neutral element, it requires LSE = -inf, and, ideally, output = 0.

### Requested outcome

For every query head whose effective attention set is empty:

  LSE MUST be -inf.
  Output SHOULD be zero.

This should apply consistently to attention APIs that return LSE, particularly MLA decode and prefill backends.

### Target hardware

Hardware-independent

### Inference engine

vLLM

### Affected model or model family

_No response_

### Workload and configuration




### Current workaround

https://github.com/vllm-project/vllm/blob/main/vllm/v1/attention/ops/common.py#L9-L34

### Impact

_No response_

### Acceptance criteria

_No response_

### Related work, dependencies, or suggested scope

cc. @kmrao-nv  

### Timing or release need

_No response_

## 评论 (2)

### anjoj0 · 2026-08-23

Our distributed attention and prefill/decode experiments suggest treating an empty local attention result as a first-class neutral element is important for correctness. In particular, the contract should be explicit for both `kv_len == 0` and rows where causal or explicit masking removes every key:

- output should be zero;
- LSE should be `-inf` in the documented base;
- merging this partial result with a non-empty rank must leave the non-empty result unchanged.

A useful regression matrix would include an empty-KV rank, fully masked rows mixed with valid rows in the same batch, zero-length requests under paged tables, and repeated CUDA-graph replay with the metadata updated in place. The same tests should verify both output and LSE, since an incorrect finite LSE can contaminate cross-rank online-softmax merging even when the output buffer appears harmless.

We can help review the semantic test cases from the perspective of multi-device execution and state-transfer boundaries.

### modelpath-dev · 2026-09-13

I will take this issue. Please assign it to me.

The problem is with the attention computation when the effective KV set is empty. The LSE should be set to -inf, and the output should ideally be zero. I will start by examining the attention computation logic in `vllm/v1/attention/ops/common.py`, focusing on how it handles empty KV situations. I will ensure that the APIs consistently apply the requested semantics for both MLA decode and prefill backends. A small fix will involve adjusting the conditions to set LSE and output correctly when KV is empty.

