# [Issue #2422] [Question] Non-atomic window between pod selection and AddRequestCount causes burst routing to the same pod under concurrency

source: https://github.com/vllm-project/aibrix/issues/2422
state: closed | updated: 2026-09-18T20:00:28Z
labels: 

## 正文

While analyzing the routing flow, we identified a significant non-atomic window between the route decision and the counter update.

Location:

In gateway_req_body.go, there are ~30 lines of code between selectTargetPod() (line 77) and AddRequestCount() (line 106). During this window, the runningRequests values read by the routing algorithm are stale — the +1 hasn't happened yet.

Under concurrency:
T1: Request A reads runningRequests → Pod1=0, Pod2=0 → selects Pod1
T2: Request B reads runningRequests → Pod1=0, Pod2=0 → also selects Pod1 (A hasn't reached +1 yet)
T3: Request A executes AddRequestCount → Pod1.runningRequests=1
T4: Request B executes AddRequestCount → Pod1.runningRequests=2

This causes concurrent requests to all pile onto the same Pod, creating a cliff-like spike in request count.

Relevant existing TODOs in the code:
- cache_impl.go:180-181 — // Current implementation assumes AddRequestCount() will not be called concurrently.
- least_request.go:99-102 — // Note: Currently, gateway instance tracks active running requests for each pod locally... TODO: Support stateful information sync across gateway instances

Questions:
1. Are there plans to address the atomicity gap between routing and counting?
2. What's your recommended approach for multi-gateway-instance deployments? The "run on leader gateway" advice is quite limiting for HA scenarios.
3. Have you considered approaches like "speculative increment + rollback" or request batching?

## 评论 (2)

### varungup90 · 2026-07-07

Thanks for opening this issue and sharing your detailed analysis!

Regarding the specific concerns you raised, here is some context on why these aren't bottlenecks or issues in practice today:

### 1. The ~30 line window between `selectTargetPod()` and `AddRequestCount()`

For practical purposes, executing those ~30 lines of code takes only a few microseconds. The window is so small that it does not cause any noticeable burst routing or cliff-like spikes under real-world concurrent workloads.

### 2. Relevant TODO comments in the code

The code comments you referenced are actually outdated and no longer relevant to the current architecture:

* **`cache_impl.go:180-181`** (`// Current implementation assumes AddRequestCount() will not be called concurrently.`): `AddRequestCount` can absolutely be called concurrently safely now.
* **`least_request.go:99-102`** (`// Note: Currently, gateway instance tracks active running requests... TODO: Support stateful information sync...`): Stateful information sync across gateway instances has already been fully implemented.

---

### Recommended HA Architecture Setup

If you are deploying in a multi-gateway-instance scenario, you do not need to restrict yourself to a single leader gateway. You can run the gateway in full **High Availability (HA) mode**, where each instance actively shares its local state with other gateway replicas.

Here is the corrected markdown with the clean, direct link to the documentation:

To set this up, please follow the official deployment guide to enable Redis backends for multi-replica state syncing:
👉 https://aibrix.readthedocs.io/latest/production/gateway.html#enabling-redis-for-multi-replica-deployments

### varungup90 · 2026-09-18

Closing this out — the three questions were answered in the comment above. The select-then-increment window is not something we plan to change. Stale comments in cache_impl.go / least_request.go are leftover docs, not open work. Cross-gateway request-count accuracy continues in #2423.
