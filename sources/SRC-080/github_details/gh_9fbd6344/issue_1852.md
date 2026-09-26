# [Issue #1852] Do not getting access to Nemotron-Pretraining-SFT-v1 (needed for a mintron distillation tutorial)

source: https://github.com/NVIDIA/Model-Optimizer/issues/1852
state: open | updated: 2026-08-02T22:08:48Z
labels: question, investigating

## 正文

I am going over [minitron distillation tutorial](https://github.com/NVIDIA/Model-Optimizer/tree/main/examples/megatron_bridge/tutorials/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16#data-blend)

It requires access to [Nemotron-Pretraining-SFT-v1 ](https://huggingface.co/datasets/nvidia/Nemotron-Pretraining-SFT-v1)dataset. I asked for it on HF and still waiting (3 days):

```
Your request to access this repository has been submitted and is awaiting a review from the repository authors. You can check the status of all your access requests in [your settings](https://huggingface.co/settings/gated-repos).
```

How long is it to wait for it? Could you specify in the tutorial how long is it to wait?

## 评论 (5)

### github-actions[bot] · 2026-07-20

Issue has not received an update in over 14 days. Adding stale label.

### danielkorzekwa · 2026-07-22

I got access, but still I propose to clarify modelopt distillation tutorial(s)

### ChenhanYu · 2026-08-02

Software Release Triage
release: ModelOpt v0.46.0
fingerprint: 8087c3e9c3428dc9997d55f25ca4ebf550d9c8dedf62c2dcc924b6130404ce1a

This open issue is in the ModelOpt release sweep. Owner: confirm release impact, linked fix/validation, or that it is non-blocking for this release.

### ChenhanYu · 2026-08-02

Software Release Triage
release: ModelOpt v0.46.0
fingerprint: bdcaa2366f495219bab9b6c9f9233d2b249944f0e24518edcf5d4ccd298f4205

This open issue is in the ModelOpt release sweep. Owner: confirm release impact, linked fix/validation, or that it is non-blocking for this release.

### ChenhanYu · 2026-08-02

Software Release Triage
release: ModelOpt v0.46.0
fingerprint: 22faa20606668a0706c1255038e08e1433f52ede260c972c9ae2ad0fce7eca13

Release follow-up: this open ModelOpt issue needs release relevance confirmed. Link its planned fix/validation, or confirm it is not a v0.46.0 blocker.
