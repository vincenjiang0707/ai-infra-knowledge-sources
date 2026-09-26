# [Issue #2198] [SGLang] GLM-5.2

source: https://github.com/llm-d/llm-d/issues/2198
state: open | updated: 2026-09-23T11:40:23Z
labels: 

## 正文

This issue tracks the llm-d and SGLang work to add recipes for serving GLM-5.2 agentic workloads with WideEP.

The [vLLM GLM-5.2 deployment](https://llm-d.ai/blog/serving-glm-5-2-agentic-workloads-on-llm-d) can serve as a deployment reference, but the SGLang work does not target topology or feature parity.

## Goals

- [ ] Benchmark the agentic workload on the target hardware and publish the results.
- [ ] Address the main llm-d and SGLang integration issues needed by the selected WideEP deployment.
- [ ] Add an llm-d SGLang WideEP recipe

## Related integration work

These issues and PRs cover endpoint and routing work relevant to this deployment. They are not a general llm-d and SGLang roadmap.

| # | Category | Item | Issue | PR | Status |
| --- | --- | --- | --- | --- | --- |
| 1 | DP | Support multi-node per-DP-rank endpoints | llm-d/llm-d-router#2296 | sgl-project/sglang#34430, port layout only | ✅ Done |
| 2 | P/D | Support SGLang `/generate` requests | — | llm-d/llm-d-router#2525 | ✅ Done |
| 3 | OAI | Disaggregate preprocessing | sgl-project/sglang#28669 | sgl-project/sglang#36234 | ✅ Done |
| 4 | OAI | Add sglang renderer backend | llm-d/llm-d-router#2982 | — | ⬜ TBD |
| 5 | OAI | Support SGLang chat and completions requests | — | — | 🚧 WIP |
| 6 | Metrics | Expose `/metrics` from every SGLang Rust DP server | — | — | ⬜ TBD |
| 7 | KV | Track KV-cache ownership per DP rank for shared endpoints | llm-d/llm-d-router#2306 | llm-d/llm-d-router#2379, adapter propagation only | ⬜ TBD |
| 8 | KV | Fix SGLang event decoding for map payloads | llm-d/llm-d-router#2944 | llm-d/llm-d-router#2966 | 🚧 WIP |
| 9 | Recipe | Wire llm-d & SGlang WideEP recipe | #2554 | — | 🚧 WIP |

General SGLang WideEP guide support is tracked in [llm-d/llm-d#2040](https://github.com/llm-d/llm-d/issues/2040).

## QA

**Why can't llm-d use SGLang as it is today?**

SGLang can serve WideEP on its own. The gap appears because llm-d treats each DP rank as a separate model-server endpoint.
This requires:
- A serving IP and port for each rank.
- P/D support on every rank.
- Per-rank load metrics.
- Cache updates that identify which rank owns the data.

Without these, llm-d cannot reliably use P/D, load-aware routing, or cache-aware routing.

**Why not route all DP ranks through one SGLang frontend?**

We could, but it would require significant SGLang-specific changes in llm-d for a Python frontend that SGLang plans to deprecate in the coming months as it moves to Rust. That integration would be short-lived.

The Rust server already exposes one port per DP rank, which matches how llm-d routes today. Completing the Rust path is the smaller and longer-term solution.

## References

- [Serving GLM-5.2 for Agentic Workloads on llm-d](https://www.lmsys.org/blog/2026-07-13-glm52-optimization)
- [Serving GLM5.2 NVFP4 Agentic Workload with SGLang: Reaching 500 TPS in 2 Weeks](https://llm-d.ai/blog/serving-glm-5-2-agentic-workloads-on-llm-d)

cc @alexnails @JustinTong0323 @Kangyan-Zhou @Jiminator @wisclmy0611 @BHZ-BER @ahg-g @vMaroon @rahulgurnani @nilig @michalmalka @kfirtoledo


## 评论 (2)

### sagearc · 2026-08-27

Updated with the remaining sglang and llm-d work.

cc @rainj-me @merrymercy

### zetxqx · 2026-09-22

Sycned with @sagearc , I'll start with a sglang-wideEP guides/receipe using the generate path and rust frontend to proceed. Here is a tracking issue: https://github.com/llm-d/llm-d/issues/2554
