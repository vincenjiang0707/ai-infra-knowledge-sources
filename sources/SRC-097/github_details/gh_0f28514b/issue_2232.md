# [Issue #2232] [RFC] GPUNetIO backend improvements and roadmap

source: https://github.com/ai-dynamo/nixl/issues/2232
state: open | updated: 2026-09-24T04:24:06Z
labels: 

## 正文

# [RFC] GPUNetIO backend improvements and roadmap

## Current status

We've been working on GPUNetIO for multi-rank GPU transfers, including peer-owned memory, descriptor-heavy READ/WRITE requests, and concurrent transfers. The work is split into focused correctness fixes and separate performance proposals.

Following [CONTRIBUTING.md](https://github.com/ai-dynamo/nixl/blob/main/CONTRIBUTING.md#contributing-process), I'd like feedback on the review split below before extending the backend further. Small fixes can proceed independently; this is not a request to merge the whole stack.

Status carried over from the September 9, 2026 draft. Checkboxes track upstream landing, not whether a PR has been submitted.

## Matched GPUNetIO vs UCX result

On the fixed H20 P/D diagnostic used in [#2172](https://github.com/ai-dynamo/nixl/pull/2172), the optimized GPUNetIO direct-row/two-SGE sender path was compared with the UCX pack-and-bulk sender path under the same workload:

| Sender phase | UCX | Optimized GPUNetIO | Change |
|---|---:|---:|---:|
| KV issue | 15.377 ms | 4.029 ms | -73.8% |
| Worker total | 16.217 ms | 5.307 ms | -67.3% |

This is a matched **sender-component** result, not a generic GPUNetIO-vs-UCX transport benchmark: the two paths also differ in data preparation and placement. A separate historical five-pair serving A/B on the same DeepSeek-V2-Lite P/D workload reported median TTFT of 86.191 ms with UCX and 80.651 ms with GPUNetIO (paired median improvement 4.764 ms; correctness 10/10). That serving run predates the final control-path hardening commits, so the component result above is the primary evidence used in this roadmap.

## Correctness and platform support

- [ ] Support explicit RoCE GID/OOB configuration and DOCA compatibility — [#2052](https://github.com/ai-dynamo/nixl/pull/2052).
- [ ] Isolate rank-local OOB endpoints and per-QP route state — [#2174](https://github.com/ai-dynamo/nixl/pull/2174).
- [ ] Expose GID/OOB options in NIXLBench — [#2173](https://github.com/ai-dynamo/nixl/pull/2173), after #2052/#2174.
- [ ] Fix multi-chunk construction, ring reuse, and whole-request completion — [#2175](https://github.com/ai-dynamo/nixl/pull/2175).
- [ ] Fix notification slots and propagate completion errors — [#2177](https://github.com/ai-dynamo/nixl/pull/2177).
- [ ] Fix metadata/MR/QP ownership and teardown — [#2178](https://github.com/ai-dynamo/nixl/pull/2178).

## Transfer efficiency and progress

- [ ] Coalesce contiguous same-key READ ranges within each input chunk — [#2176](https://github.com/ai-dynamo/nixl/pull/2176), depends on #2175.
- [ ] Extend eligible READ coalescing across input-chunk boundaries — [#2188](https://github.com/ai-dynamo/nixl/pull/2188), depends on #2176.
- [ ] Support peer-owned GPU memory and eligible two-SGE WRITEs without a gather buffer — [#2172](https://github.com/ai-dynamo/nixl/pull/2172). Restack the integration draft as focused fixes land.
- [ ] Add optional multi-QP WRITE striping — [#2215](https://github.com/ai-dynamo/nixl/pull/2215), depends on #2172; one QP remains the default.
- [ ] Progress independent QPs with CPU-local completion reporting — [#2222](https://github.com/ai-dynamo/nixl/pull/2222), depends on #2175.

#2215 adds WRITE QPs; #2222 changes completion progress across existing QPs. The latter preserves per-QP FIFO retirement and whole-request completion. CPU-local reporting alone is not a destination-GPU visibility guarantee.

## Device API follow-up

- [ ] Agree on the scope and completion/lifetime contract for a first GPUNetIO implementation behind the common Device API. https://github.com/ai-dynamo/nixl/issues/2233

This needs a separate design discussion, coordinated with [#2147](https://github.com/ai-dynamo/nixl/pull/2147), [#2111](https://github.com/ai-dynamo/nixl/pull/2111), and the CPU-proxy work [#2225](https://github.com/ai-dynamo/nixl/pull/2225)/[#2226](https://github.com/ai-dynamo/nixl/pull/2226)/[#2223](https://github.com/ai-dynamo/nixl/pull/2223). These are upstream coordination references, not part of this GPUNetIO series or prerequisites for the fixes above.

## Additional component evidence and limits

The GPUNetIO-only optimizations also have matched baseline/candidate component results:

- **Contiguous READ:** #2188 reports 18.506 -> 21.979 GB/s over #2176 for 4,096 x 4 KiB contiguous descriptors. This is not a fragmented-READ result.
- **Mixed requests:** #2222 reports small-request p99 of 113.439 -> 29.251 us with independent 2 MiB and 4 KiB transfers. Single-active-QP 4 KiB WRITE p50/p99 regress by about 4%.

The PRs contain revisions, baselines, timing definitions, and reproduction details. These are not new measurements or an aggregate serving-speedup claim. Each patch needs its own regression tests; performance changes also need matched controls. Runtime overlays are separate from implementation dependencies.

## Feedback requested

1. Is this review split appropriate, or should peer-memory registration and two-SGE WRITE in #2172 be separated further?
2. For #2222, is per-QP FIFO retirement with whole-request completion the right ordering boundary? Should CPU-local completion reporting be reviewed separately?

cc @e-ago @ovidiusm @brminich 


## 评论 (3)

### e-ago · 2026-09-21

Thanks for your suggestion, I'll review all the material and come back to you soon

### foraxe · 2026-09-22

> Thanks for your suggestion, I'll review all the material and come back to you soon

Thanks, @e-ago! Looking forward to your feedback.

### foraxe · 2026-09-24

update Sep,24th.
https://github.com/ai-dynamo/nixl/pull/2284 fixed the nixlbench bandwidth issue when source=destiniation=same gpu
