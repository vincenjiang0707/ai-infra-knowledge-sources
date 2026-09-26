# [Issue #2615] [Bug] Optimizer-based autoscaling samples are broken: metric fetch always fails and scale-down annotation is ignored

source: https://github.com/vllm-project/aibrix/issues/2615
state: closed | updated: 2026-08-26T20:50:46Z
labels: 

## 正文

### 🐛 Describe the bug


The optimizer-based autoscaling samples (`samples/autoscaling/optimizer-kpa.yaml` and the heterogeneous GPU samples that use the same setup) no longer work. There are two separate problems.

**Problem 1: the metric can never be fetched (regression from #1487).**

The samples tell the PodAutoscaler to read `vllm:deployment_replicas` from the GPU optimizer. This worked when the samples were written, but the metrics fetcher refactor in #1487 changed how external metrics are fetched, and two things broke:

- The fetcher now only accepts metrics that are listed in the central metric registry (`pkg/metrics/metrics.go`). `vllm:deployment_replicas` is not in the registry, so every fetch fails immediately with:
  `metric vllm:deployment_replicas not found in central registry`
  (see `FetchTypedMetric` in `pkg/metrics/engine_fetcher.go`)
- The fetcher ignores the `path` field from the spec and always calls `http://<endpoint>/metrics`. But the GPU optimizer only serves `/metrics/{namespace}/{deployment}` (`gpu_optimizer/app.py`), so even a registered metric would get a 404. Note that the controller *requires* `path` to be set for external sources, then never uses it.

The result: the PodAutoscaler reconciles, logs a metric fetch error every cycle, and never changes the replica count. The GPU optimizer side works fine; only the hand-off into the PodAutoscaler is broken. The heterogeneous GPU feature depends on this same hand-off, so it is affected too.

**Problem 2: the scale-down annotation is dead.**

The samples set `kpa.autoscaling.aibrix.ai/scale-down-delay: 0s`. The controller no longer reads keys with the `kpa.` prefix; it only reads `autoscaling.aibrix.ai/scale-down-cooldown-window` (see `pkg/controller/podautoscaler/types/annotations.go`). The old key is silently ignored, so scale-down always waits the default 300 seconds. The `kpa.` keys were parsed before the layered autoscaler refactor (#1575) but are leftovers now. 14 YAML files in the repo still carry the dead key.

The samples also use `metricSourceType: domain`, which is marked deprecated in favor of `external`.

### Steps to Reproduce

1. Follow the optimizer-based autoscaling docs and deploy the GPU optimizer.
2. Apply `samples/autoscaling/optimizer-kpa.yaml`.
3. Watch the controller logs: every reconcile cycle logs `metric vllm:deployment_replicas not found in central registry`.
4. Send load. The replica count never changes, even though `curl http://<optimizer>:8080/metrics/default/deepseek-r1-distill-llama-8b` returns the metric correctly.

### Expected behavior

- Applying the sample gives a PodAutoscaler that reads the replica recommendation from the GPU optimizer and scales the deployment.
- The scale-down delay set in the sample annotation is actually honored.

### Environment

- AIBrix version: main 59fa2feabc112e668bb9d7f9811486f4722f18b9
- Deployment environment: Kubernetes
- LLM(s) being used: any (sample uses deepseek-r1-distill-llama-8b)

## 评论 (2)

### bakhovaddinov · 2026-08-26

hi! I've run into the same issue just yesterday, GPU optimization is blocked by Problem 1. Are you fixing both of them in same PR? If there is any part of this I can do to help you merge a fix faster, let me know!

### yaojiejia · 2026-08-26

> hi! I've run into the same issue just yesterday, GPU optimization is blocked by Problem 1. Are you fixing both of them in same PR? If there is any part of this I can do to help you merge a fix faster, let me know!

Hey! Yes I have both fixes included in the same PR
