# [Issue #2806] [Feature][ModelClaim] Back off from claims that cannot be placed, and say when one can never fit

source: https://github.com/vllm-project/aibrix/issues/2806
state: open | updated: 2026-09-24T23:29:38Z
labels: kind/feature, area/orchestration

## 正文

### 🚀 Feature Description and Motivation

Part of #2290 (admission when a GPU is oversubscribed).

With #2647, a claim that no card can hold stays `Pending` with `NoMatchingPods`. It is tried again every 10 seconds, and again whenever a pool pod changes. Each try reads the runtime of every candidate pod, one after another. It also lists the claims from the API server. This causes two problems.

- **The tries are costly.** One runtime read takes about 120 ms on our H20 pod with one engine. Each read measures the card and scrapes the engine's metrics. The controller has only one worker. In a pool of eight pods, each waiting claim takes about one second of that worker every 10 seconds. Ten waiting claims would keep the worker busy almost all the time. The health checks of placed claims would then wait behind them.
- **A claim that can never fit looks like one that is waiting.** A model bigger than every card stays `NoMatchingPods` forever. Nobody is told that it will never fit.

### Use Case

A pool has eight pods with 80 GiB cards. All the cards are busy, and two claims are waiting. Today, each claim is tried every 10 seconds. Each try reads all eight runtimes. With this change, the tries slow down to once a minute. When a neighbour is deleted, both claims are tried again at once.

A third claim needs 90 GiB per card. Today, it waits forever. With this change, it is told at once that no card in the pool can hold it.

### Proposed Solution

- **Back off.** Each refusal in a row doubles the wait: 10, 20, 40, then at most 60 seconds. A try checks its wait before it reads any runtime. The wait is kept in the controller's memory. After a restart, every waiting claim is tried once right away. Placing or deleting the claim clears its wait.
- **Try again at once when room may have appeared.** These events wake the waiting claims:
  - another claim is deleted, scaled down, or fails;
  - another claim's declaration shrinks;
  - a pod joins the pool;
  - the waiting claim's own spec changes.

  Some room appears without any event, for example when an engine gives back KV memory. That room is found at the next try, within a minute.
- **Say when no card could ever hold it.** If every candidate card is measured, and each is too small even when empty, `Scheduled` becomes `TooLargeForAnyCard`. The message names the largest card. As with `NoMatchingPods`, an Event is raised only when the refusal changes. The claim keeps trying with the same backoff. A larger pod may join later, or the claim's declaration may shrink. So only those two wake it. Room freed on a card cannot help it.

Why not use the work queue's rate limiter? It only paces reconciles that return an error or `Requeue`. Conflict retries also return `Requeue`, so slowing the limiter would slow them too. The limiter also does not apply to reconciles started by events. So the wait is kept by the reconciler instead.

There is no API change. Out of scope: making room by squeezing busy neighbours, or by putting idle ones to sleep. Both are on the #2290 list.

The code is written and tested on an H20. It builds on #2647 and on the PR for #2795. That PR is not open yet. I will open the PR for this issue after both are merged. Until then, the four commits are here: https://github.com/Zeyu-ZEYU/AIBrix/compare/zeyu-pr2-online-kv...zeyu-pr3-placement-backoff

### Area

Orchestration (controllers, CRDs)


## 评论 (1)

### github-actions[bot] · 2026-09-24

<!-- aibrix-bot-guide -->
Thanks for contributing to AIBrix! Please review the [contribution guide](https://github.com/vllm-project/aibrix/blob/main/CONTRIBUTING.md) and make sure this issue contains enough context for maintainers to reproduce or evaluate it.

