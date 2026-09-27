# [Issue #8072] [Feature] Benchmark with audio input

source: https://github.com/sgl-project/sglang/issues/8072
state: open | updated: 2026-09-26T06:50:55Z
labels: good first issue, help wanted, Multi-modal

## 正文

### Checklist

- [ ] 1. If the issue you raised is not a feature but a question, please raise a discussion at https://github.com/sgl-project/sglang/discussions/new/choose Otherwise, it will be closed.
- [ ] 2. Please use English, otherwise it will be closed.

### Motivation

We need scripts to bench audio input for supported MLLM like minicpmo and gemma3n.

### Related resources

https://github.com/vllm-project/vllm/issues/16354

## 评论 (5)

### Dsantra92 · 2025-07-17

Can I have go at it?

### JustinTong0323 · 2025-07-20

> Can I have go at it?

Absolutely! Just go for it! Thanks a in advance! :)

### vincentzed · 2025-08-22

#9476 does it, but it might need a bit of work

### sasindharan · 2026-03-25

Can i try to solve the issue?

### PansaLegrand · 2026-09-26

@Jenson97 @JustinTong0323 I’d like to help finish the audio-input benchmark support requested here. I reviewed #27448 and noticed it was closed for inactivity. @Jenson97, are you planning to resume that work?

I have a local implementation using the current benchmark interfaces: synthetic WAV inputs through `sglang-oai-chat`, server-reported input-token counts, and CPU tests covering streaming, non-streaming, warmup, and result accounting. I plan to validate it against a real audio model before submitting a PR, with attribution to the earlier work.

Happy to coordinate to avoid duplicating an active effort.

