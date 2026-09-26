# [Issue #2805] [Testing] Triage of red tests that still need a fix (90-day sweep)

source: https://github.com/vllm-project/aibrix/issues/2805
state: open | updated: 2026-09-25T16:34:27Z
labels: kind/bug, area/gateway, area/testing, area/website, area/runtime, area/cicd, area/kv-cache, area/orchestration, area/batch

## 正文

## Summary

A 90 day sweep of the Actions history (2026-06-26 to 2026-09-25) turned up 455 failed runs. Most of them are already fixed, tied to a PR branch that was still iterating, or environmental. This issue is about what is left: tests that are still going red and do not have a fix, with enough evidence attached that someone can pick one up without redoing the whole investigation.

Two of the items reproduce locally on main today (A). Four more keep showing up in CI across branches, where the mechanism is narrowed down but there is no local repro yet (B). The appendices cover the one-off flakes and the families that are already fixed, so nobody has to dig through them again.

The coverage side already has tracking issues (#2637, #2708, #2737); this list is a different axis, tests that are failing right now.

If you want to take one, please comment on the item first so two people do not end up on the same thing, and link the PR here when it is up. Small focused PRs are the easiest to review.

## Items

- [ ] A1. Gateway rate limiter windows follow the wall clock, and three tests flake on the bucket boundary.
- [ ] A2. Two tests have been skipped since April 2025, and both pass when re-enabled.
- [ ] B1. The SLO queue spec times out on the release path.
- [ ] B2. The RoleSet topology spec hits a 409 conflict.
- [ ] B3. Batch e2e: a restored job does not reach `completed` within the 60s budget.
- [ ] B4. The planner unit test hangs and trips the 10 minute package timeout.

Grading:

- A: reproduced locally on main (`544204ae`), with a measured failure rate over repeated runs.
- B: repeated red in CI on main or across branches; no local repro yet.
- Watch: seen once; kept for reference.
- Fixed: already covered by a merged PR; do not re-triage.

## A. Reproduced locally on main

### A1. Gateway rate limiter windows follow the wall clock

`pkg/plugins/gateway/ratelimiter/redis.go:77` builds the counter key as `name:key:<unix/window % 64>`, so the counter changes on wall-clock bucket boundaries. A pair of calls that should share one window can land in two buckets instead, and the second call gets a fresh counter and is admitted. The TTL side is already anchored to the first write (`incrAndExpireScript`), so the key rotation is the remaining race.

- Affected tests: `pkg/plugins/gateway/replica_rps_test.go:96` (`TestModelReplicaRPS_Half_AllowsOneRequestEveryTwoSeconds`), `pkg/plugins/gateway/replica_inflight_test.go:335` (`TestHandleRequestBody_ReplicaInflightCoexistsWithReplicaRPS`), and `pkg/plugins/gateway/gateway_ratelimit_test.go:270` (`TestEnforceModelRPS_RejectDoesNotPostponeNextWindow`, added with #2726).
- How often it fails on main (one process per run, `-count=1`): 3 red in 100 runs for the first pair, 14 red in 450 runs for the third test, so roughly one run in thirty. The failure messages are "a second request within the same 2s window should be rejected" and "immediate retry should be rejected by the still-open window".
- CI hit: [run 35654425095, job 106514390571](https://github.com/vllm-project/aibrix/actions/runs/35654425095/job/106514390571), Go Race Tests on 09-21, same assertion at `gateway_ratelimit_test.go:270`.
- Repro: `for i in $(seq 1 50); do go test ./pkg/plugins/gateway -run 'TestModelReplicaRPS_Half_AllowsOneRequestEveryTwoSeconds|TestHandleRequestBody_ReplicaInflightCoexistsWithReplicaRPS' -count=1; done`
- Two ways to fix it, and this is a real tradeoff: (1) anchor the window at the first write so every call in the same window computes the same key, which is what the tests already assume, at the cost of changing behavior at bucket boundaries; or (2) keep the wall-clock bucket and make the tests independent of it by injecting the clock, which is a smaller change but leaves the boundary burst in the product.

### A2. Two tests skipped since April 2025

- `pkg/utils/prefixcacheindexer/tree_test.go:33` (`Test_LPRadixCacheE2E`) and `:71` (`Test_RadixMatchPrefix`) have carried `t.SkipNow()` since `d546795a` (#933, April 2025). Removing the two lines makes both pass locally, in under 0.1s including subtests.
- `apps/console/api/resource_manager/provider/kubernetes/catalog_test.go:33` skips unconditionally with `t.Skip("skip for now")`, which also makes the kubeconfig checks below it dead code. Either delete the line or gate it on the environment with a stated reason.
- Repro: `go test ./pkg/utils/prefixcacheindexer -run 'Test_LPRadixCacheE2E|Test_RadixMatchPrefix' -v`

## B. Repeated red in CI, no local repro yet

### B1. SLO queue spec times out on the release path

- `pkg/plugins/gateway/algorithms/slo_test.go:253` ("Queue router should be blocked and released successfully") fails with `context deadline exceeded` at `:270`, after the 10s per spec budget.
- Hits since June: 06-28 `exclusive_topology`, 08-17 `route-dev` and `feat/align-job-time-window`, 09-05 `ui-aiconfigurator`, 09-09 `feat-pd-hybrid-cache-load`, 09-12 `roshpr/feat-stormservice-pooled-scale`, 09-20 `andreafeat/disable-gateway-rate-limiting` (race job). #2335 reported this spec in June and was closed after #2328 and #2353 merged, but it still recurs.
- A 150 run local loop is green, so it needs a CI style repro first. Fixing it likely means either making the assertion event driven or making the fixed wait budget explicit and generous.

### B2. RoleSet topology spec hits a 409 conflict

- `test/integration/controller/roleset_test.go:1062` ("applies topology policy updates only to newly created pods") fails at `:1118` with `Operation cannot be fulfilled on rolesets... the object has been modified; please apply your changes to the latest version and try again`. Latest hit: [35814726502](https://github.com/vllm-project/aibrix/actions/runs/35814726502) on main, 09-23, 89 of 90 specs passed. Two more on 08-04.
- The spec updates the RoleSet while a reconcile is in flight, so `retry.RetryOnConflict` around the update (or `Eventually`) should close the race. Test side, no product change expected.

### B3. Batch e2e: restored jobs do not reach `completed` within the 60s budget

- `python/aibrix/tests/batch/test_e2e_abnormal_job_behavior.py:697` (shared status helper), with a 60s wait in `complete_job_after_restart` (`wait_for_status(max_polls=120, poll_interval=0.5)`).
- Main hits: 08-19 ([32202827597](https://github.com/vllm-project/aibrix/actions/runs/32202827597), `test_job_restore_after_mds_crash_during_in_progress` and `test_job_cancellation_in_finalizing`) and 09-09 ([34399845960](https://github.com/vllm-project/aibrix/actions/runs/34399845960), `Expected status 'completed', got 'in_progress'`). The restore test has 5 hits in total, 2 on main and 3 on PR branches.
- The first question is whether recovery is genuinely slower than 60 seconds (a state machine issue) or the test budget is just too tight for the metastore path. The fixes differ, and iterating needs an MDS environment.

### B4. Planner test hangs and trips the 10 minute package timeout

- `apps/console/api/planner/impl` `TestProvisionFailureMarksFailed` (`planner_test.go:1189`) ran for 9m58s and then `panic: test timed out after 10m0s` on main ([32340454024](https://github.com/vllm-project/aibrix/actions/runs/32340454024), 08-20). The goroutine dump shows `Planner.Close` blocked in `planningLoop.Stop`, then `WorkerPool.Stop`, waiting on a `WaitGroup`, so a worker does not drain on the failure path.
- 30 local runs are green. Fix direction: make `Stop` converge after a failed provision, and add a regression test that `Close` returns in that state.

## Watch (seen once, kept for reference)

- Go integration one-offs: rayclusterreplicaset 5s timeout (07-07), stormservice in-place fallback 15s (07-28), stormservice webhook defaulting diff (08-23), podautoscaler batch timeouts (08-20), modelclaim `Expected success` (09-21), roleset drain 30s (09-02).
- Installation e2e branch reds: `TestPDDisaggregation*`, `TestPDFailure*`, `TestModelRouterLifecycle` (#2743), `TestVTCHighUtilizationFairness` (reappeared on two branches after #2083).
- If one of these shows up again, a comment with the run link here is enough.

## Fixed already (do not re-triage)

- KVCache pod-triggered reconciliation spec: #2669.
- `TestVTCHighUtilizationFairness` (original report): #2083.
- Installation e2e batch from 09-13/09-14 (readiness before cleanup assertions): #2721.
- `TestModelRouterLifecycle`: #2743.
- Gateway backend e2e batch from 09-21 (session affinity, config profile): #2764.
- Injected cache panic family (`TestNewServerWithOptionsUsesInjectedCache`): fixed during the #2725 iteration (09-14).
- `TestModelWarmup*`: handled in #2769, which is still open.

## Environmental red (turns CI red without being a test bug)

- `make test-race-condition` needs envtest 1.29.0 downloaded at runtime. When that download fails, every controller suite fails in `BeforeSuite` with `exec: "etcd": executable file not found in $PATH`, and `AfterSuite` then nil panics in `envtest.Environment.Stop`. Seen on main 09-21 ([35613389668](https://github.com/vllm-project/aibrix/actions/runs/35613389668)). Installing or caching envtest in the workflow would remove a whole class of red.
- ZMQ apt install flake: main 09-09, three Go jobs red, a rerun went green.
- Installation artifact download flake (`no artifact matches`): 09-02 and 09-09.
- Lint, codegen and bot jobs also have repeated red (114, 24 and 9 jobs in the window), which is a separate conversation from this list.

## How this list was built

- Window: 2026-06-26 to 2026-09-25 (the Actions log retention edge). 5068 runs total, 455 failed, 399 failed jobs, 276 job logs reviewed. Three June logs had expired and could not be included.
- "Still needs a fix" means the test was still red within the last 30 days, or repeated across branches, and no merged PR covers it directly. Everything fixed goes in the appendix above.
- Happy to share the extracted per-test data, or to dig further into any item, if that helps.


## 评论 (3)

### github-actions[bot] · 2026-09-24

<!-- aibrix-bot-guide -->
Thanks for contributing to AIBrix! Please review the [contribution guide](https://github.com/vllm-project/aibrix/blob/main/CONTRIBUTING.md) and make sure this issue contains enough context for maintainers to reproduce or evaluate it.


### DsThakurRawat · 2026-09-25

Opened #2815 addressing Item A2 (re-enabling `Test_LPRadixCacheE2E` and `Test_RadixMatchPrefix` in `pkg/utils/prefixcacheindexer/tree_test.go`). Both pass cleanly locally with zero regressions.

### qi-wutu · 2026-09-25

I’d like to take A1. I traced the boundary flake to the counter key changing with the wall-clock bucket while its TTL is anchored to the first write. My plan is to keep the key stable for that window and add regression coverage for requests across the boundary. Please let me know if you’d prefer a different direction.
