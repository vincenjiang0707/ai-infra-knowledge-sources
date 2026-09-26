# [Issue #311] question about --max-length parameter actually determine when training a draft model

source: https://github.com/SafeAILab/EAGLE/issues/311
state: closed | updated: 2026-01-14T06:57:01Z
labels: 

## 正文

What does the --max-length parameter actually determine when training a draft model? If I set --max-length 2048, does it mean that the maximum context length for the draft model (including during speculative decoding/acceleration) is always 2048 tokens? In other words, even if the target model supports longer sequences, the draft model’s context window for acceleration will still be capped at 2048? I want to confirm whether this understanding is correct. Thanks

## 评论 (1)

### hongyanz · 2026-01-14

Yes.
