# [Issue #2605] PD disaggregation routing: observed cross-roleset decode pod selection with concurrent multi-model workloads (not reproducible on current nightly)

source: https://github.com/vllm-project/aibrix/issues/2605
state: closed | updated: 2026-08-24T03:21:02Z
labels: 

## 正文

# PD disaggregation routing: observed cross-roleset decode pod selection with concurrent multi-model workloads (not reproducible on current nightly)

## Description

While running concurrent load against two PD-disaggregated models in the same namespace, I observed requests for one model being decoded by pods that belong to the other model's roleset. The selection result is reported by the backend pod itself (`pod_name` in the OpenAI-style response), so I trust the observation even though my gateway log snapshot did not cover the affected requests.

I was not able to reproduce the issue afterwards on the same cluster and same image, and my source read of the current routing path does not show an obvious cross-model contamination path. I'm filing this to (1) ask whether maintainers see a possible cache/event-ordering race, and (2) suggest a cheap defensive log/assertion that would make this class of issue observable when it happens.

## Environment

- Aibrix: `aibrix/gateway-plugins:nightly` (image tag; local source read at `v0.7.0` commit `c5465890951ad43d22241ab7ed964b929c5d4aba`, but the running nightly image may be newer)
- Kubernetes: k3s single-node on WSL2 Debian
- Test backend: custom fake OpenAI server pods (`fake-vllm`) managed by `StormService`/roleset, not real vLLM
- Routing: Envoy + `aibrix-gateway-plugins`, `routing-strategy: pd`
- Namespace: 3 PD models coexist, each with its own roleset:
  - `fake-pd-model-1p2d` → `fake-pd-1p2d-roleset-wdbbx` (1 prefill, 2 decode)
  - `fake-pd-model-2p2d` → `fake-pd-2p2d-roleset-bnm4k` (2 prefill, 2 decode)
  - `fake-pd-model-2p4d` → `fake-pd-2p4d-roleset-gngwp` (2 prefill, 4 decode)

## Observed anomaly

On 2026-08-22 I ran the 2p2d and 2p4d 50-request batches concurrently (their JSONL files finished within 170 ms of each other, and interleaved request timestamps confirm concurrency). Each request records the backend's self-reported `pod_name`.

Expected: requests for `fake-pd-model-2p2d` are decoded only by `fake-pd-2p2d-roleset-bnm4k-decode-*`, and requests for `fake-pd-model-2p4d` only by `fake-pd-2p4d-roleset-gngwp-decode-*`.

Actual:

| Requested model | Total requests | Cross-roleset decode | Offending decode pods |
|---|---:|---:|---|
| `fake-pd-model-2p2d` | 50 | 1 | `fake-pd-2p4d-roleset-gngwp-decode-h9ppk` |
| `fake-pd-model-2p4d` | 50 | 11 | `fake-pd-2p2d-roleset-bnm4k-decode-dlkgk` (6), `fake-pd-2p2d-roleset-bnm4k-decode-nbw8q` (5) |

Sample rows (backend-reported fields only):

```json
{"i":31,"model":"fake-pd-model-2p2d","decode_pod":"fake-pd-2p4d-roleset-gngwp-decode-h9ppk","prefill_pod_ip":"10.42.0.127"}
{"i":24,"model":"fake-pd-model-2p4d","decode_pod":"fake-pd-2p2d-roleset-bnm4k-decode-dlkgk","prefill_pod_ip":"10.42.0.123"}
{"i":26,"model":"fake-pd-model-2p4d","decode_pod":"fake-pd-2p2d-roleset-bnm4k-decode-dlkgk","prefill_pod_ip":"10.42.0.123"}
{"i":27,"model":"fake-pd-model-2p4d","decode_pod":"fake-pd-2p2d-roleset-bnm4k-decode-dlkgk","prefill_pod_ip":"10.42.0.122"}
{"i":28,"model":"fake-pd-model-2p4d","decode_pod":"fake-pd-2p2d-roleset-bnm4k-decode-nbw8q","prefill_pod_ip":"10.42.0.123"}
```

Important caveat: my gateway log for that run was collected with `kubectl logs --tail`, so it only covers the final few seconds. The 12 anomalous requests fall outside that window; I therefore do not have the gateway-side `selected prefill/decode pods` line for them.

## Reproduction attempts (all clean)

Afterwards, with the same topology, same image, and the same models, I could not reproduce it:

| Run | Mode | Requests | Cross-roleset |
|---|---|---:|---:|
| 1p2d serial | sequential | 50 | 0 |
| 2p2d serial | sequential | 50 | 0 |
| 2p4d serial | sequential | 50 | 0 |
| 2p2d+2p4d concurrent | interleaved | 100+100 | 0 |
| 2p2d+2p4d concurrent (2nd round) | interleaved | 150+150 | 0 |

For the 300-request concurrent round I captured the full gateway log (`--since`, not `--tail`) and verified 200 `selected prefill/decode pods` lines: every model received only pods from its own roleset.

## Source reading

Current `main` at `c546589`:

- `pkg/plugins/gateway/gateway_req_body.go` `validateModelAvailability()` calls `cache.ListPodsByModel(model)` and passes that pod list to routing.
- `pkg/cache/cache_impl.go` `ListPodsByModel()` returns only pods registered under that model in `metaModels`.
- `pkg/plugins/gateway/algorithms/pd_disaggregation.go` `collectAndBucketPods()` groups by the `roleset-name` label, so within the already model-scoped list it cannot introduce another model's pods.

In the steady state this path looks correctly isolated.

The suspicious window is pod churn: on the day of the anomaly, pod IPs were in `10.42.0.122-132`, while today they are different (`10.42.0.47` etc.), which means pods were recreated between the two experiments. If `ListPodsByModel()` returns a snapshot while an informer `OnUpdate`/`OnDelete` is mid-way through `deletePodAndModelMappingLocked`/`addPodAndModelMappingLocked` (the code is mutex-protected, but readers get the map as-is at that instant), or if a pod was briefly registered under the wrong model before labels stabilized, a transient wrong membership could be observed. I could not verify this from logs after the fact.

## Ask

1. Does anyone see an event-ordering race (or label-churn scenario) under `StormService`/roleset pod recreation that could briefly expose another model's pod through `ListPodsByModel()`?
2. If not reproducible, would maintainers accept a defensive debug log/metric in `Route()` or `validateModelAvailability()` whenever a selected pod's `model.aibrix.ai/name` label differs from the requested model? That would turn this from an unreproducible report into a diagnosable signal next time it occurs.

Happy to provide the full JSONL and full gateway logs if useful.


## 评论 (1)

### NeekChaw · 2026-08-24

C:\Users\neekchow\AppData\Local\Temp\issue2605_close.md
