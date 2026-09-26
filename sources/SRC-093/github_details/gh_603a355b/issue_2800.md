# [Issue #2800] [Bug] Gateway per-pod state still keyed by bare pod name outside the PD trackers

source: https://github.com/vllm-project/aibrix/issues/2800
state: open | updated: 2026-09-24T08:00:31Z
labels: area/gateway, kind/misc, area/orchestration

## 正文

## Summary

#2785 moves the PD router's load trackers to `namespace/name` keys (#2783). An audit of the rest of the gateway found more per-pod state keyed by the bare pod name. When two pods share a name in different namespaces, their entries overwrite each other.

Pods with the same name are common when a controller names pods by index, for example StatefulSet or LeaderWorkerSet. Deployment pods get a random suffix, so they rarely collide.

Line numbers refer to main at 8f44dea8.

The findings are grouped by severity below. Each one says whether the state is shared across requests or rebuilt for every request.

## High

### Rate history for gateway-tracked counters (shared, all models)

- `pkg/cache/utils.go:236`: `calculateRate1m` keys the process-wide `rateCalculator.history` (`pkg/cache/cache_metrics.go:229`) by `pod.Name + "//" + metric`. The key has no namespace and no model.
- Two same-named pods in any two namespaces feed one history, and it does not matter which models they serve. Their counters are not related, so the history mixes two series:
  - A rate can be computed against a base snapshot taken from the other pod.
  - When that delta is negative, the code treats it as a counter reset and uses the full current value as the delta.
  - Either way, the reported rate is wrong, and it can be too high or too low.
- This affects:
  - `RealtimeRunningRequestsDrainRate1m`, which the PD decode drain-rate scoring uses (`pkg/plugins/gateway/algorithms/pd_disaggregation.go:785`)
  - `RealtimeOutputTokenRateEWMA`, the capacity estimate of the load-balance router

The mechanism is easiest to show with `calculatePerSecondRate` (see Medium below). It shares the same history and has no snapshot throttle, but it needs the same model name on both pods:
1. Record a counter of 100000 for `team-a/decode-0`.
2. Record 500 for `team-b/decode-0`.
3. Record 100100 for `team-a/decode-0`, 200 ms after step 1.

The rate reported for `team-a/decode-0` in step 3 is about 994,000/s. The true rate is about 500/s.

`calculateRate1m` has a 5 s snapshot throttle and a 10 s minimum window, so the numbers differ from this example. It goes through the same reset branch, where the rate becomes the pod's whole counter value divided by the window. Its key has no model, so it also collides across models.

## Medium

### Per-model rate history (shared)

- `pkg/cache/utils.go:181`: `calculatePerSecondRate` keys the same history by `pod.Name/model/metric`.
- A collision needs the same model name in two namespaces.
- This affects `AvgPromptThroughputToksPerS` and `AvgGenerationThroughputToksPerS`. The PD decode scoring reads the latter (`pd_disaggregation.go:738`).

### Rate history purge on pod delete (shared)

- `pkg/cache/informers.go:281` calls `rateCalculator.PurgeEntriesForPod(name)`, which matches on the name prefix only.
- Deleting `team-a/decode-0` also drops the history of `team-b/decode-0`.

### Prefix hash index (shared, synced across gateway replicas)

- `pkg/utils/prefixcacheindexer/hash.go:69`: `modelToPods` maps a model to bare pod names.
- It is written with `targetPod.Name` in two places:
  - the `prefix-cache` router (`prefix_cache.go:462`, `prefix_cache.go:509`)
  - the PD router (`pd_disaggregation.go:1133`)
- `MatchPrefix` is then filtered by a name-keyed ready set.
- A collision needs the same model name in two namespaces. When it happens, a prefix cached on one pod is credited to both, so requests can be sent to the pod that does not hold the cache.
- The KV-event sync indexer (`prefix_cache.go:533`, `prefix_cache.go:868`) already uses `namespace/name`.

## Low

### Per-request maps and name lookups

In these places, one candidate list for a request can hold two same-named pods, which needs one model name served from two namespaces. When it does, one pod's entry overwrites the other's. `utils.FilterPodByName` then returns the first match, so the pod that gets routed may not be the pod that was scored.

- PD:
  - `pd/trackers.go:107`: the map returned by `GetPrefillRequestCountsForPods` is keyed by name. After #2785 the lookup uses the pod key, but the result is still keyed by name.
  - The prefill imbalance selection (`pd_disaggregation.go:624`, `pd_disaggregation.go:650`).
  - `matchedPods` in the prefill scorers (`pd/prefill_scorer.go:188`, `322`, `631`).
  - The decode score maps `podRequestCounts`, `podThroughputs`, `podFreeGpuUsage` and `metricsReadyByPod` (`pd_disaggregation.go:726`–`1004`).
  - `prefillScores` is keyed by roleset name (`pd_disaggregation.go:906`), which also has no namespace. RoleSet names get a random suffix, so this one is unlikely to collide.
- Other routers:
  - `least_request.go:150`, `158`, `254`, `290`
  - `throughput.go:112`
  - `load_balance.go:432`
  - `prefix_cache.go:422`, `565`, `977`

### Preble router

- `pkg/utils/prefixcacheindexer/tree.go:47` (`modelToPods`)
- `prefix_cache_preble.go:65`–`66` (`currentDecodeLengthsPerPod`, `avgTimePerTokenPerPod`)

These are keyed by pod name on a router instance shared by all models. The two histogram maps are not read by the scoring path today, so the practical effect is small.

### PD selection counter

- `pd_disaggregation.go:194`, `pd_disaggregation.go:1137`: `selectionCounts` is keyed by pod name. Nothing reads it outside tests.

## Suggested fix

- Key the rate history by `namespace/name` (`utils.GeneratePodKey`) and purge by the same key. This is the High item and is self-contained.
- Store `namespace/name` in the prefix hash index and in its ready set.
- For the per-request maps, key by `namespace/name` or by pod pointer, and stop resolving the selected pod back through `FilterPodByName`.


## 评论 (2)

### github-actions[bot] · 2026-09-24

<!-- aibrix-bot-guide -->
Thanks for contributing to AIBrix! Please review the [contribution guide](https://github.com/vllm-project/aibrix/blob/main/CONTRIBUTING.md) and make sure this issue contains enough context for maintainers to reproduce or evaluate it.


### bolubo · 2026-09-24

I ran the same sweep outside the gateway as well (tests excluded, on 8f44dea8), and only one more live site came back.

`pkg/utils/pod_array.go:122` `ListPortsForPod` keys by the pod name and appends the lists together (`:132`), so two same-named pods of one model end up sharing a single port list. The map is built from `PodArray`, which is a flat slice; the registry it comes from does keep `namespace/name` (`pkg/cache/model.go:30`, `pkg/cache/informers.go:468`), so this looks like the spot where the namespace gets dropped. Ports come from the pod's own label and the `data-parallel-size` env (`pkg/utils/util.go:216`), so the two pods can expose different sets, and the shared list can then be read for the wrong pod:

- `least_request.go:97` (the DP path): the counts are keyed `pod/port` (`:295`), so the two pods overwrite each other's entries, and the pod is looked up by name again (`:156`) once the choice is made.
- `power_of_two.go:105` and `router.go:420`: both go through `selectTargetPortForPodWithLeastRequestCount` (`least_request.go:211`), which reads the shared list (`:215`). A port that only the other pod serves has no metric and counts as 0 (`:227`), so it can win the minimum, and the request can end up on `podIP:port` (`pkg/types/router_context.go:342`) for a port this pod does not serve.
- Same-named single-port pods are affected as well: once the list has two entries, they no longer use the pod-level live count path (`:271`).

Keying this map by `utils.GeneratePodKey` should keep the two apart, if that is worth doing with the rest.

Two small things on the Preble entry, in case they help. `tree.go:47` looks live to me: `modelToPods` is written with the bare pod name in `PostRouteUpdate` (`prefix_cache_preble.go:613`) and read by Route (`:501`, `:519`), ScoreAll (`:659`), `getPodLoad` (`:716`) and the cost model (`:381`, used at `:562` and `:700`). Also, `readyPodsByName` (`:454`) and `collectMatchedReadyPods` (`:462`) look like two more name-keyed spots in the same file that are not on the list yet. On the two histogram maps, `currentDecodeLengthsPerPod` seems to be written but never read; `avgTimePerTokenPerPod` is read by `getNodeCost` (`:360`), but as far as I can tell nothing populates it outside the tests, so it stays at the default.

The rest of the tree looks clean: the remaining hits are either `namespace/name` keys (`utils.GeneratePodKey`), lists already scoped to one namespace (`client.InNamespace`, `informers.WithNamespace`), test-only, or not pod-keyed maps at all.

