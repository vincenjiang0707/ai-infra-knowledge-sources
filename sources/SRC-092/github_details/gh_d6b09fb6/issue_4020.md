# [Issue #4020] [RFC]: Reproducing Table 1 hit rates on the released trace, consistent +4-6pp offset

source: https://github.com/kvcache-ai/Mooncake/issues/4020
state: open | updated: 2026-09-14T04:02:28Z
labels: RFC

## 正文

### Changes proposed

I've been reproducing your Table 1 cache hit rates on arxiv-trace/mooncake_trace.jsonl using LRU, and I get the same curve shape but a systematic offset at every capacity:

| blocks | 1k        | 10k     | 30k    | 50k     | 100k  | infiniti |
|--------|-------|-------|-------|-------|-------|-------|
| paper   | 0.30   | 0.40   | 0.48   | 0.50   | 0.51    | 0.51    |
| mine    | 0.341  | 0.460 | 0.537 | 0.551 | 0.552 | 0.553 |

I compute hit rate as (sum of longest-resident-prefix blocks) / (sum of all blocks requested), replaying in timestamp order. Since the infinite-cache case is policy-free, I'd expect it to be reproducible from the trace alone, but I get 0.553 against your 0.51.

I've tried five denominator definitions (blocks vs input_length tokens, excluding the partial tail block, per-request averaging) and none closes the gap. Is the released trace the same one used for Table 1, or is there a detail in the hit-rate definition I'm missing?

Repro: https://github.com/gauravapiscean/agentic-kv-cache

### Before submitting a new issue...

- [x] Make sure you already searched for relevant issues and read the [documentation](https://kvcache-ai.github.io/Mooncake/)

## 评论 (1)

### github-actions[bot] · 2026-09-10

Thanks for opening this issue, @gauravapiscean!

| Field | Value |
|-------|-------|
| **Issue** | #4020 |
| **GitHub user ID** | `10956383` |
| **Reporter** | @gauravapiscean |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.
