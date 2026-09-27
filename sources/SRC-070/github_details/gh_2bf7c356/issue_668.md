# [Issue #668] Question: Why did DeepEP v2 drop the double-buffer design in favor of explicit pre/post-sync barriers?

source: https://github.com/deepseek-ai/DeepEP/issues/668
state: open | updated: 2026-07-02T02:46:53Z
labels: 

## 正文

Hi,

I'm comparing DeepEP v1 (legacy) and v2, and noticed a major change in the synchronization and buffering strategy.

In v1, the `low_latency` path avoided the `notify` pre-sync kernels by using a double-buffer (ping-pong) design combined with in-kernel atomic/flag polling over NVLink to overlap communication and computation.

However, in v2, it seems this double-buffer design is dropped, and the implementation goes back to using explicit pre-sync and post-sync barriers.

Could you share the design trade-offs behind this change? Specifically:

1. Did the double-buffer design in v1 LL introduce bottleneck issues in practice (e.g., memory/L2 cache pressure, or NVLink congestion from atomic polling)?
2. Does v2's explicit barrier leverage Hopper/Blackwell hardware features (like `mbarrier` or cluster-level sync) to make the barrier overhead negligible?
3. How does v2 handle low-latency scenarios without the ping-pong overlap?

Thanks!


## 评论 (1)

### hiSandog · 2026-07-02

This is a good design question because the v1 double-buffer path and the v2 explicit barrier path optimize different failure modes. It would help if the answer separated correctness constraints from performance trade-offs: whether v2 dropped double-buffering because of resource pressure, harder deadlock/debuggability, weaker portability across RDMA/NVLink modes, or because overlap moved to a different layer. A short note in the docs would be useful for users comparing v1 low-latency behavior with v2.

