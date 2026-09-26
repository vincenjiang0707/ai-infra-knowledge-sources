# [Issue #2770] [Bug][ModelClaim] An engine takes most of the card at startup, before any KV limit is in force

source: https://github.com/vllm-project/aibrix/issues/2770
state: open | updated: 2026-09-23T21:15:30Z
labels: kind/bug, area/runtime, area/kv-cache, area/orchestration

## 正文

### 🐛 Describe the bug

When several ModelClaims share one GPU, each engine starts with its KV
allocator holding most of the card. The control plane pulls it down a few
seconds later, but until it does, two engines on the same card can each believe
they own most of it.

On one H20 that the runtime measures at 95.33 GiB usable, two vLLM engines
started together each reported a KV limit of about 76 GiB, which is roughly 80%
of the card each. They held that for about 12 seconds before the control plane
wrote the limits it had planned:

```
18:22:47  gate-a (engine booting, limit 76.1 GiB) | gate-b (engine booting, limit 76.0 GiB)
18:22:50  gate-a (engine active, ready, limit 76.1 GiB) | gate-b (engine active, ready, limit 76.0 GiB)
18:23:03  gate-a limit in force: 17.67 GiB
18:23:03  gate-b limit in force: 17.67 GiB
```

Nothing was overcommitted in that run. Neither engine was taking traffic yet,
and neither had mapped more than 0.7 GiB. The problem is that nothing prevents
it: the limit each engine starts under is chosen by its own KV allocator, which
has no way to know another engine is starting on the same card.

Two consequences beyond the window itself:

- Free HBM is not a safe admission signal while this is true. An engine that
  has just started reports a large limit and almost no mapped memory, so free
  memory says the card is empty while two engines are each entitled to most of
  it.
- An operator looking at the pool during those seconds sees numbers that do not
  add up, and there is nothing in the snapshot that says they are transient.

### Steps to Reproduce

1. Run a warm runtime pool with one GPU and `ENABLE_KVCACHED` set for the
   engines.
2. Create two ModelClaims at the same time, both selecting that pool, each
   small enough that both can start.
3. Poll the runtime snapshot while they boot:

```bash
kubectl get --raw "/api/v1/namespaces/<ns>/pods/<pool pod>:8080/proxy/v1/runtime/snapshot" \
  | jq '.models[] | {model_name, kv_capacity_bytes, kv_used_bytes}'
```

`kv_capacity_bytes` for each engine is most of the card from the moment the
engine appears until the control plane writes a limit. Summing
`kv_capacity_bytes` across the engines on the card exceeds the card during that
window.

### Expected behavior

An engine should start under a limit chosen by whoever knows what else is on
the card, rather than under a default that assumes the card is its own.

The runtime already builds the engine's kvcached environment in
`kvcached_env()`, so it is the natural place to pass an initial limit. A claim
that has been placed already has a figure to pass: the KV it was admitted
against. An engine started that way would never be entitled to memory that was
promised to something else, and the window above would not exist.

Failing that, an engine that has not yet been given a limit should be
distinguishable in the snapshot from one that has, so that nothing downstream
treats its allocator's default as a decision.

### Environment

- AIBrix: `main` at `b99bdecf`, plus the ModelClaim placement work in #2647.
- Kubernetes: v1.30.4
- GPU: 1x NVIDIA H20, 97871 MiB total, 95.33 GiB reported usable by the runtime
- Engine: vLLM 0.19.0, DeepSeek-R1-Distill-Qwen-1.5B, `--max-model-len 2048`
- kvcached: 0.1.5

### Area

Runtime

---

This sits under #2290. The placement work in #2647 avoids the problem for
admission by never reading free memory, and it reduces the window by writing a
limit as soon as the engine is ready, but it cannot remove the window: the
control plane only gets to act after the engine already exists.

## 评论 (2)

### github-actions[bot] · 2026-09-21

<!-- aibrix-bot-guide -->
Thanks for contributing to AIBrix! Please review the [contribution guide](https://github.com/vllm-project/aibrix/blob/main/CONTRIBUTING.md) and make sure this issue contains enough context for maintainers to reproduce or evaluate it.


### Zeyu-ZEYU · 2026-09-23

An update from #2647, which now carries the whole placement flow. Each new
instance is recorded with its planned KV limit before `Activate`, and its engine
stays off the route until that limit is in force.

A re-run on the same H20 shows that the window is still there. kvcached started
each engine at 80.0 GiB, and the controller pulled it down to its record within
about 10 seconds of the engine becoming ready. The engine was not routable in
between, so it took no traffic.

So #2647 narrows the window, and it makes the fix this issue asks for easier.
The controller now knows an engine's limit before it calls `Activate`, because
it records the limit in `status.instances[].kvLimitBytes` first. Passing that
figure to the runtime at start is the next step here, under #2290.
