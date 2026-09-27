# [Issue #608] Hybrid_EP Abnormal performance on B300 (2-node dispatch ~40GB/s) reveals hardcoded DEF_IB_TC; request env-based configurability (align with NVSHMEM)

source: https://github.com/deepseek-ai/DeepEP/issues/608
state: open | updated: 2026-05-09T04:18:37Z
labels: 

## 正文


**Description:**

In the current Hybrid EP implementation, the InfiniBand Traffic Class is hardcoded as:

```cpp
constexpr int32_t DEF_IB_TC = 0;
```

This makes the IB traffic class fixed at compile time and prevents users from tuning QoS / traffic prioritization dynamically based on deployment environments.

In contrast, NVSHMEM provides environment variable support (e.g., `NVSHMEM_IB_TC`) to configure the traffic class at runtime, which is very useful for performance tuning and congestion control in RDMA-based communication.

**Problem:**

* `DEF_IB_TC` cannot be adjusted without recompilation
* No flexibility for different cluster QoS configurations
* Inconsistent behavior compared to NVSHMEM and other RDMA-based stacks

**Suggestion:**
Introduce an environment variable (e.g., `HybridEP_IB_TC`) to override the default value. For example:

```cpp
int32_t get_ib_tc() {
    const char* env = std::getenv("HybridEP_IB_TC");
    if (env != nullptr) {
        return std::atoi(env);
    }
    return DEF_IB_TC;
}
```

Then use `get_ib_tc()` instead of the compile-time constant.

**Benefits:**

* Enables runtime tuning without recompilation
* Aligns with NVSHMEM and common RDMA practices
* Improves flexibility for performance optimization under different network conditions


Would it be possible to add this support for better configurability?


## 评论 (1)

### Autumn1998 · 2026-05-09

Thanks! we will consider this in the next version.
