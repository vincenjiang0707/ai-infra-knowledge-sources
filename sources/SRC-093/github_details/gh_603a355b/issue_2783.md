# [Issue #2783] [Bug] PD router per-pod load state collides for same-named pods in different namespaces

source: https://github.com/vllm-project/aibrix/issues/2783
state: open | updated: 2026-09-23T02:07:17Z
labels: kind/bug, area/gateway

## 正文

### 🐛 Describe the bug

The PD router keeps per-pod load state on the router itself, in three trackers:

- `TokenLoadTracker` (the token_load / hybrid_cache_load ledger)
- `PrefillRequestTracker` (in-flight prefill counts)
- `PendingDecodeTracker` (pending decode counts)

There is one `pdRouter` instance for all models and namespaces, so this state is shared by every deployment the gateway routes to. It is keyed by the bare `pod.Name`, however, for example `AcquirePrefill(requestID, pod.Name, cost)` and `GetPriority(pod.Name)`.

When two deployments in different namespaces have pods with the same name, their accounting is merged onto one key. This happens when the same manifest is applied to two namespaces, or when generated StormService/RoleSet pod names coincide:

- each prefill pod carries the other's token load and in-flight count, so the scorer steers traffic away from an idle pod;
- the `pd_token_load_active_tokens` / `pd_token_load_kv_tokens` gauges publish one series for both pods, and when the janitor prunes one pod it deletes the other's series.

The gateway cache already keys per-pod state by `namespace/name` (`utils.GeneratePodKey`). The PD trackers are the exception.

### Steps to Reproduce

1. Deploy the same PD manifest into two namespaces, `team-a` and `team-b`, so that both have a prefill pod named `prefill-0` and each serves its own model.
2. Route PD traffic to the `team-a` model with `token_load` or `hybrid_cache_load`.
3. Observe `pd_token_load_active_tokens{pod_name="prefill-0"}`, or the prefill score of `team-b/prefill-0`: it reflects `team-a`'s load, although `team-b` is idle.

### Expected behavior

Load state is tracked per pod identity (`namespace/name`). Same-named pods in different namespaces do not affect each other's score or metrics.

### Environment

Current `main`. The behavior is independent of engine.

### Area

Gateway (PD routing)


## 评论 (1)

### github-actions[bot] · 2026-09-23

<!-- aibrix-bot-guide -->
Thanks for contributing to AIBrix! Please review the [contribution guide](https://github.com/vllm-project/aibrix/blob/main/CONTRIBUTING.md) and make sure this issue contains enough context for maintainers to reproduce or evaluate it.

