# [Issue #2256] Regarding metric chrf's implementation

source: https://github.com/EleutherAI/lm-evaluation-harness/issues/2256
state: closed | updated: 2026-08-27T12:38:52Z
labels: feature request, good first issue

## 正文

Hi,

In this repo, the `chrf` metric [implementation](https://github.com/EleutherAI/lm-evaluation-harness/blob/ebe7226ebfb8d11a9fb8d6b53eb65891f895c633/lm_eval/api/metrics.py#L92C1-L103C52) calls `sacrebleu.corpus_chrf()` with default [parameters](https://github.com/mjpost/sacrebleu/blob/0f351010b8b641aaa59fe75b98d7cc522bf221eb/sacrebleu/compat.py#L94): character order 6 and word order 0. Perhaps in `metric.py` it would be nice to include those two optional parameters so users can specify this in `task.yml`, for example to facilitate `chrf++` which uses word order 2?

Thanks!

## 评论 (6)

### baberabb · 2024-08-28

Hi! That sounds reasonable. Would you like to open a PR?

### JINO-ROHIT · 2024-10-12

Hi can i take this up?

### PinzhenChen · 2024-10-17

Hi @JINO-ROHIT , yes sure, I have not implemented this.

### DebjyotiRay · 2025-06-14

Yo @PinzhenChen !
if this is still open, can I take this up..?


### baberabb · 2025-06-16

> Yo [@PinzhenChen](https://github.com/PinzhenChen) ! if this is still open, can I take this up..?

yes! that would be great

### avgvi · 2025-10-23

I noticed that this feature hasn’t been implemented yet, so I went ahead and tried to solve it. Hope that’s okay!
