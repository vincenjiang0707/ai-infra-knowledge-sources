# [Issue #2807] [Feature][ModelClaim] Route a new engine within seconds of being ready

source: https://github.com/vllm-project/aibrix/issues/2807
state: open | updated: 2026-09-24T23:29:39Z
labels: kind/feature, area/orchestration

## 正文

### 🚀 Feature Description and Motivation

Related: #2290.

With #2647, a claim is reconciled every 10 seconds. An engine on a GPU takes traffic only once it is held to its KV limit. The controller writes that limit in the pass that finds the engine ready. It sees the limit in force, and routes the engine, only in the next pass. So a new engine waits up to about 20 seconds after it is ready.

On our H20, one engine was ready 22 seconds after its claim was placed. It took traffic 21 seconds after that. The wait was almost as long as the boot.

### Use Case

A user applies a ModelClaim and sends requests once the model is up. Today, the gateway answers 503 for up to about 20 more seconds. With this change, the engine takes traffic within about 2 seconds of being ready. The same holds when an engine restarts and comes back.

### Proposed Solution

- **Confirm the limit in the same pass.** After writing the limit of an engine that is coming up, read it back at once. If it is in force, route the engine in this pass. An engine that was routed and then lost its limit still leaves the route first. So `KVLimitNotHeld` is still raised.
- **Look again after 2 seconds while an engine boots.** The runtime reports such an engine alive but not yet ready. A boot longer than 5 minutes goes back to 10 seconds. The same holds for an engine that is ready but not held to its limit, and for a runtime that does not answer. Looking sooner would not help them.

Such a pass reads only the runtimes of the claim's own instances. The other steps keep their own pace. A card is divided at most once a round, unless its engines change. A pool policy runs at most once every 10 seconds. A claim waiting for a card keeps its backoff (#2806). One runtime read takes about 120 ms. So while an engine boots, it costs the controller's single worker about 6% of its time, for at most 5 minutes.

Why not 1 second? It saves half a second on average, and doubles the cost. Engines take tens of seconds to boot.

Out of scope: waking a sleeping model. The gateway wakes the runtime directly, and the claim stays `Sleeping` until the next pass. Waking through the controller is on the #2290 list.

There is no API change.

The code is written and tested on an H20. There, an engine took traffic 3 seconds after it was ready, down from 21. It builds on #2647, and on the PRs for #2795 and #2806. Those two PRs are not open yet. I will open the PR for this issue after all three are merged. Until then, the three commits are here: https://github.com/Zeyu-ZEYU/AIBrix/compare/zeyu-pr3-placement-backoff...zeyu-pr4-faster-readiness

### Area

Orchestration (controllers, CRDs)


## 评论 (1)

### github-actions[bot] · 2026-09-24

<!-- aibrix-bot-guide -->
Thanks for contributing to AIBrix! Please review the [contribution guide](https://github.com/vllm-project/aibrix/blob/main/CONTRIBUTING.md) and make sure this issue contains enough context for maintainers to reproduce or evaluate it.

