# [Issue #1805] RFC: Add Leader Election Support for Active-Passive Architecture in Gateway plugin

source: https://github.com/vllm-project/aibrix/issues/1805
state: closed | updated: 2026-09-20T14:04:16Z
labels: kind/enhancement, area/gateway, priority/important-soon

## 正文

### 🚀 Feature Description and Motivation

Currently, the gateway plugin doesn't support leader election, which means all instances are active simultaneously. 

This can lead to:

- Inconsistent KV cache event processing across multiple instances
- Potential race conditions when handling shared resources
- No high availability with failover capabilities

### Use Case

high availability with failover capabilities

### Proposed Solution

Implement leader election support to enable an active-passive (leader-follower) architecture where only one instance is active at a time while others remain in standby mode.

## 评论 (5)

### googs1025 · 2025-11-26

I already have some initial ideas, and I will list them in the next few days.

### googs1025 · 2025-11-27

###  Implement Active-Passive (Leader-Follower) HA architecture:

- Only Leader instance processes business requests
- Follower instances remain in standby mode, not receiving traffic

###  Principle

- Only the Leader Pod's Readiness Probe returns SERVING
- Kubernetes Service automatically filters non-ready Pods, achieving traffic isolation

```yaml
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ Gateway Pod A   │    │ Gateway Pod B   │    │ Gateway Pod C   │
│ (Leader)        │    │ (Follower)      │    │ (Follower)      │
│                 │    │                 │    │                 │
│ Readiness:      │    │ Readiness:      │    │ Readiness:      │
│ SERVING         │    │ NOT_SERVING     │    │ NOT_SERVING     │
│                 │    │                 │    │                 │
│ Traffic:        │    │ Traffic:        │    │ Traffic:        │
│ ← ← ← ← ← ←     │    │ (No Traffic)    │    │ (No Traffic)    │
└───────┬─────────┘    └─────────┬───────┘    └─────────┬───────┘
        │                        │                        │
        │                        │                        │
        └───────────┬────────────┼────────────────────────┘
                    │            │
         ┌──────────v────────────v────────────┐
         │    Kubernetes Service/Endpoints    │
         │                                     │
         │    Ready Pods:                      │
         │    - Pod A (Leader)                │
         │                                     │
         └─────────────────────────────────────┘
                    │
                    v
            ┌───────────────┐
            │  Envoy/Client │
            │  (Sends       │
            │  Requests)    │
            └───────────────┘
```

TODO: 
-  Leader Election Integration
- gRPC Health Check Implementation


### penfree · 2026-01-14

but what if there are too many requests that a single gateway instance is not enough to process them

### googs1025 · 2026-01-16


Based on our offline discussion with @Jeffwan , I’d like to formalize the architectural considerations and design rationale behind choosing **leader election (active-passive)** over other HA approaches for the Gateway plugin. Here’s a summary for alignment:

---

### 1. Current Architecture

The typical deployment pattern is:
```
Envoy → Ext-Proc Plugin (Gateway) → Backend Pods
```
- **Ext-Proc (Gateway) plugin**: **Stateful** — it maintains in-memory KV cache state (e.g., prefix cache), watches model events, and coordinates with backend endpoints.
  
Because of this statefulness, **scaling the Gateway horizontally introduces consistency challenges** — especially around shared cache and event processing.

---

###  2. Evaluated HA Approaches

We considered three main strategies:

| Option | Description | Pros | Cons |
|-------|-------------|------|------|
| **1. Make Gateway stateless via event broadcasting** | All instances watch the same events and maintain identical in-memory state. | No leader needed; fully scalable. | Extremely hard to guarantee consistency (e.g., race on cache updates); high memory overhead; complex reconciliation. |
| **2. Externalize state (e.g., Redis)** | Offload KV cache to Redis or similar. | Enables true horizontal scaling. | Adds operational complexity; introduces latency; may not meet performance SLOs for low-latency LLM serving. |
| **3. Active-Passive with Leader Election**  | Only one Gateway instance is active (`SERVING`); others standby (`NOT_SERVING`). | Simple, reliable, minimal change; leverages Kubernetes readiness + service routing; preserves low-latency in-memory cache. | Limited horizontal scalability; failover depends on lease renewal interval (~seconds). |

> **Conclusion**: I suggest choosing **Option 3** as the most pragmatic path — it delivers **high availability with failover**, avoids external dependencies, and aligns with current usage patterns where **prefix cache locality matters** (i.e., requests for the same prompt should ideally hit the same cache instance).

---



### googs1025 · 2026-01-16

> but what if there are too many requests that a single gateway instance is not enough to process them

Great question. IIUC, the Gateway plugin is lightweight — it doesn’t do inference , so a single instance can handle very high request rates.
For now, active-passive gives us correctness + HA with minimal complexity — and covers more scenarios we’ve seen.
That said, if performance problem emerge in the future, we can explore active-active (multi-leader) or sharded architectures to enable horizontal scaling while preserving consistency where needed.

