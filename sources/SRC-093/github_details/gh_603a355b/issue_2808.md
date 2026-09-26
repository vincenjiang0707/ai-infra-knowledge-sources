# [Issue #2808] [Feature][ModelClaim] Answer 503 with Retry-After for a model whose claim is not placed yet

source: https://github.com/vllm-project/aibrix/issues/2808
state: open | updated: 2026-09-24T23:28:29Z
labels: area/gateway, kind/feature

## 正文

### 🚀 Feature Description and Motivation

Related: #2290.

The gateway learns about a ModelClaim only from the annotations the controller writes on warm pods. A claim that is not placed yet has no pod. So a request for its model gets 400, "model ... does not exist". That is the answer for a model that nobody serves (#526).

But the model does exist, and it is on its way. Once the claim is placed, the same request gets 503 with `Retry-After` while the engine starts. Before that, the client is told to give up.

### Use Case

A user applies a ModelClaim and sends requests right away. Today, the first answers say the model does not exist, until the claim is placed. With this change, they say the model is pending, and give the controller's reason, such as `NoMatchingPods`. They also ask the client to retry in 10 seconds.

### Proposed Solution

- **Watch ModelClaim objects.** In the gateway, the Kubernetes discovery provider watches ModelClaims too. The cache keeps one record per claim: the name it serves, its phase, and the controller's reason. The reason comes from its `Scheduled` condition while it waits, or from its `Ready` condition once it has failed. A claim being deleted is forgotten.
- **Answer 503 for a claimed model with no pod yet.** The message reads like `model qwen is pending (NoMatchingPods); retry shortly`, with `Retry-After: 10`. A claim that waiting does not help gets no `Retry-After`. That is one that has to be changed first, such as one with `InvalidEngineConfig`, or one whose engine failed for good (`EngineFailed`). Other refusals get it, a failed activation included, since the controller tries it again. A model that no claim serves still gets 400.
- **Keep the message short.** It carries only the condition's reason. The condition's full message names pods and card figures, which a client does not need.
- **Grant read access.** The gateway's role can get, list and watch ModelClaims, in the kustomize config and the Helm chart. The gateway lists claims once when it starts. On Forbidden or NotFound, it says so once in its log and does not watch them. Such a model is then answered with 400, as before.

There is no API change.

The change is in #2809. It does not depend on the other ModelClaim changes.

### Area

Gateway


## 评论 (1)

### github-actions[bot] · 2026-09-24

<!-- aibrix-bot-guide -->
Thanks for contributing to AIBrix! Please review the [contribution guide](https://github.com/vllm-project/aibrix/blob/main/CONTRIBUTING.md) and make sure this issue contains enough context for maintainers to reproduce or evaluate it.

