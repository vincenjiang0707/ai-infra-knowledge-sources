# [Issue #604] Stop multi-rate benchmarks after first failure threshold

source: https://github.com/vllm-project/guidellm/issues/604
state: closed | updated: 2026-07-14T19:32:43Z
labels: 

## 正文

### Problem Statement

When running multi-rate benchmark profiles (`constant`, `poisson`, `concurrent`, and the async phase of `sweep`), benchmarking continues at higher rates even after a lower rate has already hit a failure constraint (for example over-saturation or excessive errors).

This wastes benchmark time, adds low-signal data at clearly unsustainable rates, and can place unnecessary load on the target system.



### Proposed Solution

- Treat scheduler constraints with `request_processing=stop_all` as terminal for rate escalation.
- Sort configured rates/streams ascending for deterministic escalation.
- For multi-rate profiles, stop generating higher-rate strategies after the first terminal failure.
- Keep normal completion constraints (`stop_local`, e.g. max duration/max requests) non-terminal so progression continues.
- In `sweep`, always run `synchronous` and `throughput`, then apply early-exit logic only during the async-rate phase.

### Alternatives Considered

_No response_

### Usage Examples

```markdown

```

### Additional Context

_No response_

## 评论 (2)

### dreamer-89 · 2026-06-25

@ushaket Thanks for creating this task; I would be happy to work on this one. Please let me know if this is still available to grab. 

### ushaket · 2026-06-28

@dreamer-89 I started working on this in #605 but didn't have the capacity to take it to the finish line and it slipped off my radar.

I'd be more than happy if you want to pick up where I left off, but I don't mind if you'd prefer a fresh implementation either.

Let me know if you plan to take this on, if not, I'll try to carve out some time to get it done.

Thanks for looking into this!
