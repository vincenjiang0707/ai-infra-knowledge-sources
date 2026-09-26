# [Issue #2952] GPTQ: Hessian inversion fails on every module of a looped/weight-shared architecture (NanbeigeForCausalLM) — silent RTN fallback

source: https://github.com/vllm-project/llm-compressor/issues/2952
state: closed | updated: 2026-08-26T22:03:29Z
labels: 

## 正文

## Summary
Running GPTQModifier (llm-compressor 0.12.0, transformers <=5.10.1) against `Nanbeige/Nanbeige4.2-3B` — a looped transformer (`num_loops=2`: 22 physical layers, each executed twice per forward) — fails Hessian inversion on **all 154 Linear modules** ("Failed to invert hessian"), silently falling back to RTN for every one. The output artifact is RTN-equivalent while appearing to be GPTQ.

## What I ruled out
- **Calibration activations are clean** (no NaN/inf, sane ranges — probed at the hook).
- **A manually-computed H from the same activations is well-conditioned and inverts fine.**
- **The double-fire hook is not the cause mathematically**: because the layer runs twice per forward, the observer hook fires 2x per sample, but the running-mean accumulation is invocation-count-agnostic — verified against the source. The doubled sample count alone cannot make H singular.
- Dampening increases did not help.

## Repro
Looped arch + standard GPTQ oneshot recipe (any scheme, INT4/NVFP4 alike):
```python
# trust_remote_code model with num_loops=2; GPTQModifier(scheme=..., targets="Linear", ignore=["lm_head"])
```
198/198 calibration samples, default pipeline. Every module logs a Hessian inversion failure; run completes "successfully".

## Context
Looped/weight-shared (recurrent-depth) models are an emerging small-model architecture and are unusually quantization-sensitive (error compounds across passes), i.e. exactly the models where GPTQ-class compensation would help most. As far as I can tell no public report covers GPTQ on this architecture class; the known Hessian-failure issues (#1019, #966, #1003, #1152) have different causes (softcapping, rank-deficient activations).

Two asks: (1) any pointer on where inversion actually goes wrong given the ruled-out causes above — happy to run instrumented builds; (2) consider making the RTN fallback loud (summary count at end of run) — 154 silent fallbacks looked like a successful GPTQ run.


## 评论 (0)
