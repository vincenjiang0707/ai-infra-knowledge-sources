# [Issue #2269] llm-d SIG-Observability: open work inventory

source: https://github.com/llm-d/llm-d/issues/2269
state: open | updated: 2026-09-22T14:11:53Z
labels: 

## 正文

This is a work inventory generated with claude code, I will go through the list this and next week and consolidate what should be contained in next release and update here. 

@nicolexin @JeffLuoo @ahg-g ^^

# llm-d SIG-Observability: open work inventory

_Swept 2026-08-12 across all active repos in the `llm-d` org; re-swept 2026-08-27 and 2026-09-21. Every ref below was re-verified against GitHub on 2026-09-21._

**98 open items** across 11 repos: **62 issues**, **36 PRs** (7 of them drafts). 36 items are new since the 2026-08-27 re-sweep (tagged `new`). 10 items have been idle 60+ days. 88 items from the previous inventory were closed or merged since 2026-08-12; they are listed per theme in the collapsed "Resolved" blocks.

## Summary by theme

| Theme | Issues | PRs | Total | New |
|---|---:|---:|---:|---:|
| Tracing and OpenTelemetry | 12 | 8 | 20 | 8 |
| Metrics instrumentation and coverage | 19 | 11 | 30 | 8 |
| Logs and trace-log correlation | 7 | 2 | 9 | 3 |
| Dashboards, alerts, and monitoring assets | 8 | 3 | 11 | 3 |
| Semantic conventions and standardization | 2 | 2 | 4 | 4 |
| Documentation, guides, and blogs | 3 | 4 | 7 | 2 |
| Adjacent: metric consumers and signal quality | 11 | 6 | 17 | 8 |
| **Total** | **62** | **36** | **98** | **36** |

## What changed since 2026-08-27

1. **The semconv anchor is done.** [router#708](https://github.com/llm-d/llm-d-router/issues/708) closed after [router#2503](https://github.com/llm-d/llm-d-router/pull/2503) (2026-09-01) and [router#2516](https://github.com/llm-d/llm-d-router/pull/2516) (2026-09-11) merged; [async#413](https://github.com/llm-d/llm-d-async/issues/413) and [kv-cache#651](https://github.com/llm-d/llm-d-kv-cache/issues/651) closed on the back of it.
2. **All legacy EPP metric families are gone.** [router#1070](https://github.com/llm-d/llm-d-router/issues/1070) closed via [router#2675](https://github.com/llm-d/llm-d-router/pull/2675), [#2821](https://github.com/llm-d/llm-d-router/pull/2821), [#2826](https://github.com/llm-d/llm-d-router/pull/2826): `inference_extension_*`, `inference_objective_*`, and `llm_d_inference_scheduler_*` are no longer emitted; only `llm_d_epp_*` remains. First consumer breakage is already filed: [async#460](https://github.com/llm-d/llm-d-async/issues/460).
3. **WVA is deprecated.** `llm-d-workload-variant-autoscaler` was renamed `llm-d-autoscaling`; the controller moved to `legacy/` on 2026-09-14 ([autoscaling#1563](https://github.com/llm-d/llm-d-autoscaling/pull/1563)) and KEDA reading vLLM/EPP metrics from Prometheus is the autoscaling engine. On 2026-09-16 the maintainers closed 120 issues in a triage reset. **22 WVA issues in this inventory were closed by that reset, not fixed**, and all seven open WVA PRs were closed unmerged, including the trace-log correlation fix ([#1506](https://github.com/llm-d/llm-d-autoscaling/pull/1506)), the optimization-pipeline tracing ([#1508](https://github.com/llm-d/llm-d-autoscaling/pull/1508)), the silent-scrape-failure fix ([#1543](https://github.com/llm-d/llm-d-autoscaling/pull/1543)), the stale-series eviction ([#1464](https://github.com/llm-d/llm-d-autoscaling/pull/1464)), and the ServiceMonitor serverName fix ([#1524](https://github.com/llm-d/llm-d-autoscaling/pull/1524)). Only two WVA items remain open here.
4. **Tracing backlog mostly merged.** OTLP/HTTP exporter ([router#2573](https://github.com/llm-d/llm-d-router/pull/2573)), tokenization and kvevents spans ([router#2272](https://github.com/llm-d/llm-d-router/pull/2272)), prefix-cache filter span ([router#2594](https://github.com/llm-d/llm-d-router/pull/2594)), trace-log correlation ([router#2271](https://github.com/llm-d/llm-d-router/pull/2271)), explicit SDK config ([router#2298](https://github.com/llm-d/llm-d-router/pull/2298)), IPP traceparent re-parenting (ipp#159).
5. **Coordinator metrics shipped.** [router#2435](https://github.com/llm-d/llm-d-router/pull/2435) and the spec [router#2277](https://github.com/llm-d/llm-d-router/pull/2277) merged; [router#2616](https://github.com/llm-d/llm-d-router/pull/2616) carries the remainder.
6. **Assets and docs.** Batch-gateway dashboards and alerts moved into llm-d/llm-d ([llm-d#2390](https://github.com/llm-d/llm-d/pull/2390)); NIXL transfer metrics documented ([llm-d#2368](https://github.com/llm-d/llm-d/pull/2368)); router monitoring added to every well-lit path guide ([llm-d#1777](https://github.com/llm-d/llm-d/issues/1777) closed); the tracing blog is live ([web#469](https://github.com/llm-d/llm-d.github.io/pull/469)); router JSON logs now follow the OTel Logs Data Model (router#2643, #2813).
7. **New threads opened this cycle** (all tagged `new` below): Prometheus exemplars for metric-to-trace navigation ([router#2637](https://github.com/llm-d/llm-d-router/issues/2637), [llm-d#2462](https://github.com/llm-d/llm-d/issues/2462)), tenant attribution on spans ([router#2793](https://github.com/llm-d/llm-d-router/issues/2793)) and on cost metrics ([router#2741](https://github.com/llm-d/llm-d-router/issues/2741)), OTel Weaver as the telemetry source of truth ([llm-d#2472](https://github.com/llm-d/llm-d/issues/2472)), opt-in OTel GenAI metrics ([router#2906](https://github.com/llm-d/llm-d-router/issues/2906)), `kvcache_*` alias deprecation ([router#2943](https://github.com/llm-d/llm-d-router/pull/2943)/[#2942](https://github.com/llm-d/llm-d-router/pull/2942)), and the cross-repo `OTEL_TRACES_EXPORTER=none|otlp|console` alignment ([ipp#305](https://github.com/llm-d/llm-d-inference-payload-processor/issues/305), [kv-cache#715](https://github.com/llm-d/llm-d-kv-cache/pull/715)).

## What to act on first

1. **Decide the fate of the WVA monitoring assets.** [autoscaling#1466](https://github.com/llm-d/llm-d-autoscaling/issues/1466), [llm-d#2363](https://github.com/llm-d/llm-d/pull/2363) (conflicting, no reviews since 09-03), and [autoscaling#1556](https://github.com/llm-d/llm-d-autoscaling/pull/1556) all move dashboards for a controller that is now in `legacy/`. Either merge them as legacy-only or close them and re-scope [llm-d#1983](https://github.com/llm-d/llm-d/issues/1983) to KEDA-era assets (see [llm-d#1767](https://github.com/llm-d/llm-d/issues/1767)).
2. **Audit consumers of the removed legacy metric names.** [async#460](https://github.com/llm-d/llm-d-async/issues/460) stalls dispatch on any EPP that only exports `llm_d_epp_*`. Dashboards and alerts under `guides/`, the KEDA blueprints in llm-d-autoscaling, llm-d-benchmark, and the latency predictor should be grepped for `inference_extension_`, `inference_objective_`, and `llm_d_inference_scheduler_` before the release.
3. **Five SIG PRs have zero reviews.** [router#2774](https://github.com/llm-d/llm-d-router/pull/2774) (exemplars, conflicting, 11d), [router#2843](https://github.com/llm-d/llm-d-router/pull/2843) (tenant attribution, conflicting, 6d), [llm-d#2474](https://github.com/llm-d/llm-d/pull/2474) (exemplar panel, 9d), [ipp#306](https://github.com/llm-d/llm-d-inference-payload-processor/pull/306) and [kv-cache#715](https://github.com/llm-d/llm-d-kv-cache/pull/715) (`OTEL_TRACES_EXPORTER`, 20d each). They need a named reviewer.
4. **Two SIG-lead PRs are conflicting and old.** [router#1677](https://github.com/llm-d/llm-d-router/pull/1677) (96d; [router#2755](https://github.com/llm-d/llm-d-router/issues/2755) reports gaps against it) and [ipp#165](https://github.com/llm-d/llm-d-inference-payload-processor/pull/165) (99d). Rebase and land, or close.
5. **Sequence the `kvcache_*` alias removal.** [router#2943](https://github.com/llm-d/llm-d-router/pull/2943) (declare) can merge now; [router#2942](https://github.com/llm-d/llm-d-router/pull/2942) (remove) must wait for v0.12.0 under the N+2 policy.
6. **Four design decisions are waiting on the SIG.** [llm-d#2472](https://github.com/llm-d/llm-d/issues/2472) (Weaver registry as SSOT), [router#2906](https://github.com/llm-d/llm-d-router/issues/2906) (opt-in OTel GenAI metrics; vLLM has a parallel RFC, vllm#51186), [router#2840](https://github.com/llm-d/llm-d-router/issues/2840) (JSON log severity contract), and [router#1981](https://github.com/llm-d/llm-d-router/pull/1981) (opt-in GenAI payload capture, size/XXL, 69d without a maintainer review).
7. **Closable now.** [kv-cache#639](https://github.com/llm-d/llm-d-kv-cache/issues/639) (router#2272 merged), [batch-gw#619](https://github.com/llm-d/llm-d-batch-gateway/issues/619) (llm-d#2390 merged), [router#2674](https://github.com/llm-d/llm-d-router/issues/2674) and [router#2470](https://github.com/llm-d/llm-d-router/issues/2470) (implementing PRs merged), [router#1089](https://github.com/llm-d/llm-d-router/issues/1089) (its PR was closed as "already addressed"; verify), [benchmark#1701](https://github.com/llm-d/llm-d-benchmark/issues/1701) and [benchmark#1719](https://github.com/llm-d/llm-d-benchmark/pull/1719) (fixed by #1757 per @UgaTheDev), [deployer#357](https://github.com/llm-d/llm-d-deployer/pull/357) and [model-svc#166](https://github.com/llm-d/llm-d-model-service/issues/166) (archived repos), [llm-d#1959](https://github.com/llm-d/llm-d/pull/1959) and [router#1953](https://github.com/llm-d/llm-d-router/pull/1953) (stale/rotten drafts).
8. **Quick wins with no reviewer.** [router#2947](https://github.com/llm-d/llm-d-router/pull/2947) (transposed `model_name`/`target_model_name` labels, size/M), [router#2884](https://github.com/llm-d/llm-d-router/issues/2884) (coordinator step timings DPANIC, one-line fix), [router#2397](https://github.com/llm-d/llm-d-router/pull/2397) (mergeable since 08-31).

---

## Tracing and OpenTelemetry

_12 issues, 8 PRs. Span coverage, context propagation, exporters, and SDK setup. Most of the August backlog merged (router#2272, #2298, #2573, #2594, ipp#159); what remains is the cross-repo `OTEL_TRACES_EXPORTER` alignment, exemplars, tenant attribution, and the overhead measurement._

| Type | Ref | Title | By | Age | Idle | Signals |
|---|---|---|---|---:|---:|---|
| issue | [llm-d#1108](https://github.com/llm-d/llm-d/issues/1108) | Capture GenAI prompts and completions as events or attributes <br>`PR router#1981` | @JeffLuoo | 165d | 35d | `enhancement`, `observability`, `triage-accepted` |
| issue | [router#1485](https://github.com/llm-d/llm-d-router/issues/1485) | P/D sidecar observability: add Prometheus /metrics, wire trace propagation, document enablement <br>`PR #1677; gaps reported in #2755` | @gyliu513 | 108d | 7d | `needs-triage`, `area/telemetry` |
| issue | [kv-cache#639](https://github.com/llm-d/llm-d-kv-cache/issues/639) | Add OpenTelemetry span for kvevents raw message processing <br>`router#2272 merged; closeable` | @larainema | 107d | 24d |  |
| issue | [router#1500](https://github.com/llm-d/llm-d-router/issues/1500) | Observability and tracing for LoRA adapter routing (cache hit vs miss) <br>`see draft PR #2792` | @wseaton | 107d | 10d | `kind/feature`, `area/epp`, `area/telemetry` |
| issue | [ipp#163](https://github.com/llm-d/llm-d-inference-payload-processor/issues/163) | Add fine-grained OpenTelemetry spans for the plugin pipeline and model selector <br>`PR #165` | @gyliu513 | 100d | 8d | `kind/feature`, `triage/accepted`, `sig/observability` |
| issue | [router#1632](https://github.com/llm-d/llm-d-router/issues/1632) | Tracing initialization is not production ready (TLS/auth, default exporter, sampler support, env mutation) | @gyliu513 | 100d | **90d** | `needs-triage`, `area/telemetry` |
| issue | [llm-d#2389](https://github.com/llm-d/llm-d/issues/2389) | Measure observability (tracing) performance overhead across llm-d projects <br>`child router#2665; harness fix router#2725 merged` | @gyliu513 | 25d | 10d |  |
| issue | [router#2578](https://github.com/llm-d/llm-d-router/issues/2578) | [Coordinator]Add tracing | @gyliu513 | 25d | 25d | `area/telemetry` |
| issue | [ipp#305](https://github.com/llm-d/llm-d-inference-payload-processor/issues/305) | tracing: OTEL_TRACES_EXPORTER=none is silently treated as console <br>`PR #306` | @gyliu513 | 20d | 20d | `new`, `needs-triage` |
| issue | [router#2637](https://github.com/llm-d/llm-d-router/issues/2637) | Link metrics to traces with Prometheus exemplars <br>`PR #2774; panel in llm-d#2462` | @sudoalok | 19d | 12d | `new`, `needs-triage` |
| issue | [router#2665](https://github.com/llm-d/llm-d-router/issues/2665) | Measure observability (tracing) performance overhead for llm-d-router <br>`child of llm-d#2389; PR #2725 merged` | @nicolexin | 18d | 18d | `new`, `needs-triage` |
| issue | [router#2793](https://github.com/llm-d/llm-d-router/issues/2793) | Add tenant identity and provenance attributes to EPP request spans <br>`PR #2843` | @madhugoutham | 11d | 10d | `new` |
| PR | [deployer#357](https://github.com/llm-d/llm-d-deployer/pull/357) | WIP: DO NOT REVIEW: Tracing <br>`close it` | @sallyom | 445d | **445d** | `draft`, `archived repo` |
| PR | [ipp#165](https://github.com/llm-d/llm-d-inference-payload-processor/pull/165) | feat(observability): add fine-grained OTel spans for the plugin pipeline and model selector <br>`closes #163; conflicting, awaiting review` | @gyliu513 | 99d | 12d | `kind/feature`, `size/L` |
| PR | [router#1981](https://github.com/llm-d/llm-d-router/pull/1981) | feat: add opt-in GenAI payload capture (PayloadStore Phase 1) <br>`closes llm-d#1108` | @nickaggarwal | 69d | 11d | `size/XXL`, `area/observability` |
| PR | [llm-d#2388](https://github.com/llm-d/llm-d/pull/2388) | proposal: selective tracing for llm-d <br>`1 approval, needs maintainer` | @gyliu513 | 25d | 19d |  |
| PR | [kv-cache#715](https://github.com/llm-d/llm-d-kv-cache/pull/715) | fix(telemetry): support OTEL_TRACES_EXPORTER=none in InitTracing <br>`aligns with llm-d#2388` | @gyliu513 | 20d | 20d | `new`, `size/L` |
| PR | [ipp#306](https://github.com/llm-d/llm-d-inference-payload-processor/pull/306) | tracing: support OTEL_TRACES_EXPORTER=none\|otlp\|console <br>`fixes #305; no reviews` | @gyliu513 | 20d | 20d | `new`, `kind/feature`, `size/L` |
| PR | [router#2774](https://github.com/llm-d/llm-d-router/pull/2774) | feat(metrics): link metrics to traces with Prometheus exemplars <br>`for #2637; conflicting, no reviews` | @sudoalok | 11d | 9d | `new`, `size/L`, `area/epp`, `area/observability` |
| PR | [router#2843](https://github.com/llm-d/llm-d-router/pull/2843) | feat(observability): add tenant trace attribution <br>`for #2793; conflicting, no reviews` | @madhugoutham | 6d | 4d | `new`, `size/XL`, `area/epp`, `area/telemetry`, `area/scheduling`, `area/observability` |

<details>
<summary>Resolved since 2026-08-12 (11)</summary>

| Type | Ref | Title | Outcome |
|---|---|---|---|
| issue | [router#2297](https://github.com/llm-d/llm-d-router/issues/2297) | tracing: configure the SDK explicitly instead of mutating process environment | closed 2026-08-21 |
| PR | [router#2298](https://github.com/llm-d/llm-d-router/pull/2298) | tracing: configure SDK explicitly instead of mutating process env | merged 2026-08-21 |
| issue | [ipp#157](https://github.com/llm-d/llm-d-inference-payload-processor/issues/157) | IPP: extract upstream traceparent at ext_proc ingress, re-parent span, and inject traceparent on egress | closed 2026-08-28 |
| issue | [kv-cache#644](https://github.com/llm-d/llm-d-kv-cache/issues/644) | Extend OTel Tracing Coverage (kvevents + tokenization) | closed 2026-08-28 |
| PR | [router#2272](https://github.com/llm-d/llm-d-router/pull/2272) | feat: add OpenTelemetry spans for tokenization and KV-cache event processing | merged 2026-09-02 |
| issue | [router#2567](https://github.com/llm-d/llm-d-router/issues/2567) | tracing: support OTLP/HTTP as an alternative to the gRPC exporter | closed 2026-09-02 |
| PR | [router#2573](https://github.com/llm-d/llm-d-router/pull/2573) | tracing: support OTLP/HTTP as an alternative to the gRPC exporter | merged 2026-09-02 |
| PR | [router#2594](https://github.com/llm-d/llm-d-router/pull/2594) | feat(epp): add OTel span to prefix cache affinity filter decisions | merged 2026-09-09 |
| issue | [autoscaling#1272](https://github.com/llm-d/llm-d-autoscaling/issues/1272) | Add OpenTelemetry tracing for the reconcile/optimization pipeline | closed 2026-09-16 (WVA triage reset, not fixed) |
| PR | [autoscaling#1508](https://github.com/llm-d/llm-d-autoscaling/pull/1508) | feat(observability): add OpenTelemetry tracing for the optimization pipeline | closed unmerged 2026-09-16 (WVA deprecation) |
| issue | [kv-cache#521](https://github.com/llm-d/llm-d-kv-cache/issues/521) | Telemetry to capture additional details for KV cache calls | closed 2026-08-26 (not planned / stale bot) |

</details>


## Metrics instrumentation and coverage

_19 issues, 11 PRs. New counters and histograms, gaps where failures are currently silent, plus the plumbing around scraping. Coordinator metrics landed (router#2435); the sidecar metrics PR (router#1677) is still the oldest open SIG PR._

| Type | Ref | Title | By | Age | Idle | Signals |
|---|---|---|---|---:|---:|---|
| issue | [router#964](https://github.com/llm-d/llm-d-router/issues/964) | Improve datalayer observability <br>`parent of ipp#162` | @elevran | 141d | **82d** | `help wanted`, `needs-triage`, `area/telemetry` |
| issue | [router#1089](https://github.com/llm-d/llm-d-router/issues/1089) | An EPP metric that reports inflight tokens and requests <br>`PR #1697 closed as "already addressed"; verify and close` | @ahg-g | 130d | **93d** | `help wanted`, `needs-triage`, `area/telemetry` |
| issue | [ipp#115](https://github.com/llm-d/llm-d-inference-payload-processor/issues/115) | Track actual token usage of the inference requests | @davidbreitgand | 124d | 6d | `enhancement`, `lifecycle/stale`, `sig/observability` |
| issue | [kv-cache#617](https://github.com/llm-d/llm-d-kv-cache/issues/617) | Improve llm-d-kv-cache Observability for Metrics, Tracing Coverage, Alerting, and Dashboards | @gyliu513 | 115d | 11d |  |
| issue | [ipp#162](https://github.com/llm-d/llm-d-inference-payload-processor/issues/162) | Data layer has no metrics: silent event drops, untracked collector/extractor errors <br>`aligned with router#964` | @gyliu513 | 100d | 1d | `kind/feature`, `lifecycle/stale`, `triage/accepted`, `sig/observability` |
| issue | [router#1964](https://github.com/llm-d/llm-d-router/issues/1964) | Precise prefix cache indexer observability metrics <br>`PR #1965` | @SachinVarghese | 72d | **72d** | `needs-triage` |
| issue | [ipp#235](https://github.com/llm-d/llm-d-inference-payload-processor/issues/235) | llmd-router-metrics-collector to collect metrics from inference pools <br>`PR #215 closed rotten` | @Mohammad-nassar10 | 70d | **70d** | `triage/accepted` |
| issue | [router#2045](https://github.com/llm-d/llm-d-router/issues/2045) | Hot-reload the metrics/models scrape client cert on rotation <br>`PR #2151 closed for inactivity` | @hexfusion | 67d | **65d** |  |
| issue | [router#2025](https://github.com/llm-d/llm-d-router/issues/2025) | token-producer: saturated render endpoint stalls every request with no metric or error log | @nilig | 67d | **67d** |  |
| issue | [router#2059](https://github.com/llm-d/llm-d-router/issues/2059) | Migrate to generic endpoint attribute filter/scorer and deprecate legacy  metrics code | @liu-cong | 66d | 7d | `needs-triage` |
| issue | [autoscaling#1428](https://github.com/llm-d/llm-d-autoscaling/issues/1428) | feat: add scale-up/scale-down event metrics to benchmark report <br>`WVA deprecated; likely moot` | @asm582 | 66d | 37d | `needs-triage` |
| issue | [router#2276](https://github.com/llm-d/llm-d-router/issues/2276) | [Coordinator] Add metrics <br>`spec #2277 merged; PR #2616` | @revit13 | 47d | 25d | `area/telemetry` |
| issue | [router#2370](https://github.com/llm-d/llm-d-router/issues/2370) | Chart ships no RBAC for the EPP's authenticated /metrics endpoint (anonymous scrapes 401, token scrapes 500) | @LukeAVanDrie | 39d | 26d | `needs-triage`, `kind/bug`, `area/dev` |
| issue | [router#2447](https://github.com/llm-d/llm-d-router/issues/2447) | Accurate Cached Token Usage Metrics in P/D Setup | @robertgshaw2-redhat | 33d | 28d |  |
| issue | [router#2482](https://github.com/llm-d/llm-d-router/issues/2482) | Add native Coordinator pipeline metrics <br>`#2435 merged; PR #2616` | @zhouyou9505 | 31d | 22d | `needs-triage` |
| issue | [router#2755](https://github.com/llm-d/llm-d-router/issues/2755) | sidecar: stage metrics missing on several disaggregation connector paths <br>`against open PR #1677` | @gyliu513 | 12d | 12d | `new`, `needs-triage`, `kind/bug` |
| issue | [router#2741](https://github.com/llm-d/llm-d-router/issues/2741) | Additional metrics needed for inference cost attribution <br>`PR #2834` | @simanadler | 12d | 3d | `new` |
| issue | [router#2896](https://github.com/llm-d/llm-d-router/issues/2896) | Report the prefix-cache hit the router predicted for the endpoint it selected <br>`PR #2897` | @asharkhan3101 | 3d | 3d | `new`, `needs-triage` |
| issue | [router#2955](https://github.com/llm-d/llm-d-router/issues/2955) | Add endpoint-role label to prefix-cache prediction metrics for P/D setups <br>`follow-up of #2897` | @JaredTan95 | 0d | 0d | `new` |
| PR | [router#1677](https://github.com/llm-d/llm-d-router/pull/1677) | feat(sidecar): expose Prometheus /metrics on the P/D sidecar <br>`closes #1485; conflicting; see #2755` | @gyliu513 | 96d | 11d | `kind/feature`, `kind/bug`, `kind/documentation`, `area/sidecar`, `size/L`, `kind/cleanup`, `area/observability` |
| PR | [router#1949](https://github.com/llm-d/llm-d-router/pull/1949) | add toolcalling telemetry to EPP <br>`ahg-g asked status 09-08` | @Gregory-Pereira | 73d | 11d | `draft`, `kind/feature`, `size/XL`, `area/observability` |
| PR | [router#1953](https://github.com/llm-d/llm-d-router/pull/1953) | Add tool-calling preservation telemetry to routing sidecar <br>`rotten` | @Gregory-Pereira | 73d | 12d | `draft`, `lifecycle/rotten`, `area/sidecar`, `size/L` |
| PR | [router#1965](https://github.com/llm-d/llm-d-router/pull/1965) | Adding precise prefix cache indexer observability metrics <br>`closes #1964; stale` | @SachinVarghese | 72d | 11d | `kind/feature`, `kind/bug`, `kind/documentation`, `size/L`, `kind/cleanup`, `area/kvcache`, `area/observability` |
| PR | [router#2067](https://github.com/llm-d/llm-d-router/pull/2067) | Add support for ZMQ metrics updates <br>`no longer draft; SGLang first on ZMQ path` | @azamikram | 65d | 5d | `kind/feature`, `size/XXL`, `area/epp`, `area/datalayer` |
| PR | [llm-d#2293](https://github.com/llm-d/llm-d/pull/2293) | NIXL handshake hash metric (nixl_config_info) <br>`WIP, empty body; pins vLLM fork` | @dagrayvid | 37d | 32d |  |
| PR | [router#2397](https://github.com/llm-d/llm-d-router/pull/2397) | feat(metrics): extract vLLM kv_offload_tiering_chunk_* metrics and add storage tier weight <br>`mergeable, no reviewer` | @zdtsw | 35d | 4d | `kind/feature`, `size/L`, `area/epp`, `area/scheduling`, `area/kvcache`, `area/datalayer` |
| PR | [router#2616](https://github.com/llm-d/llm-d-router/pull/2616) | feat(coordinator): add pipeline amplification and media metrics <br>`closes #2482; part of #2276` | @zhouyou9505 | 22d | 17d | `new`, `kind/feature`, `size/XL`, `area/coordinator` |
| PR | [router#2834](https://github.com/llm-d/llm-d-router/pull/2834) | Design for tenant, workload and user based inference cost attribution <br>`closes #2741` | @simanadler | 6d | 3d | `new`, `size/XXL`, `area/docs` |
| PR | [router#2897](https://github.com/llm-d/llm-d-router/pull/2897) | Record prefix-cache hit predicted for the selected endpoint <br>`closes #2896; 1 approval` | @asharkhan3101 | 3d | 0d | `new`, `kind/feature`, `size/XL`, `area/epp`, `area/scheduling`, `area/docs` |
| PR | [router#2947](https://github.com/llm-d/llm-d-router/pull/2947) | fix(predictedlatency): correct transposed model name labels | @malamsyah | 0d | 0d | `new`, `kind/bug`, `size/M`, `area/epp`, `area/scheduling` |

<details>
<summary>Resolved since 2026-08-12 (34)</summary>

| Type | Ref | Title | Outcome |
|---|---|---|---|
| PR | [sim#620](https://github.com/llm-d/llm-d-inference-sim/pull/620) | implement vllm:request_time_per_output_token_seconds metrics | merged 2026-08-13 |
| issue | [router#1913](https://github.com/llm-d/llm-d-router/issues/1913) | feat(datalayer): Add spoke-epp engine type for cluster metrics extraction | closed 2026-08-13 |
| issue | [router#1192](https://github.com/llm-d/llm-d-router/issues/1192) | Resolve EPP Metrics Verification Flakiness in E2E Test Suites | closed 2026-08-15 |
| PR | [router#1697](https://github.com/llm-d/llm-d-router/pull/1697) | Add EPP in-flight requests and tokens metrics (#1089) | closed unmerged 2026-08-19 |
| issue | [router#2323](https://github.com/llm-d/llm-d-router/issues/2323) | router-standalone: EPP Service not created when EPP flowControl/monitoring config is enabled | closed 2026-08-19 |
| PR | [router#2435](https://github.com/llm-d/llm-d-router/pull/2435) | feat(coordinator): expose Prometheus metrics | merged 2026-08-29 |
| issue | [async#344](https://github.com/llm-d/llm-d-async/issues/344) | Token Throughput counter (input + output tokens processed) | closed 2026-08-31 |
| issue | [async#345](https://github.com/llm-d/llm-d-async/issues/345) | Deadline Proximity histogram (time-to-deadline of queued items) | closed 2026-08-31 |
| PR | [router#2277](https://github.com/llm-d/llm-d-router/pull/2277) | docs: add coordinator metrics specification | merged 2026-09-08 |
| PR | [router#2476](https://github.com/llm-d/llm-d-router/pull/2476) | feat(metrics): add ATOM as a built-in engine | merged 2026-09-11 |
| issue | [router#1070](https://github.com/llm-d/llm-d-router/issues/1070) | Deprecate old metrics | closed 2026-09-15 |
| PR | [router#2151](https://github.com/llm-d/llm-d-router/pull/2151) | datalayer: hot-reload scrape client certificate on rotation | closed unmerged 2026-09-15 |
| PR | [ipp#215](https://github.com/llm-d/llm-d-inference-payload-processor/pull/215) | llmd router metrics collector plugin. | closed unmerged 2026-08-24 (rotten) |
| PR | [router#793](https://github.com/llm-d/llm-d-router/pull/793) | feat: add disaggregation decider evaluation metrics | closed unmerged 2026-08-14 (rotten) |
| PR | [ipp#258](https://github.com/llm-d/llm-d-inference-payload-processor/pull/258) | Proposal to collect additional metrics needed for cost monitoring | closed unmerged 2026-09-06 (rotten) |
| issue | [autoscaling#198](https://github.com/llm-d/llm-d-autoscaling/issues/198) | Expose load and performance predicated WVA metrics to Prometheus | closed 2026-09-16 (WVA triage reset, not fixed) |
| issue | [autoscaling#236](https://github.com/llm-d/llm-d-autoscaling/issues/236) | feat: Report TTFT and ITL predictions of model analyzer to Prometheus | closed 2026-09-16 (WVA triage reset, not fixed) |
| issue | [autoscaling#320](https://github.com/llm-d/llm-d-autoscaling/issues/320) | FEAT: Add support for direct vLLM metrics scraping (bypassing Prometheus) | closed 2026-09-16 (WVA triage reset, not fixed) |
| issue | [autoscaling#360](https://github.com/llm-d/llm-d-autoscaling/issues/360) | Fix silent failure in metrics collection | closed 2026-09-16 (WVA triage reset, not fixed) |
| issue | [autoscaling#426](https://github.com/llm-d/llm-d-autoscaling/issues/426) | refactor: Move optimizer-specific Prometheus queries from collector to optimizer | closed 2026-09-16 (WVA triage reset, not fixed) |
| issue | [autoscaling#690](https://github.com/llm-d/llm-d-autoscaling/issues/690) | bug: Scale-to-zero Prometheus queries fail due to missing metric labels | closed 2026-09-16 (WVA triage reset, not fixed) |
| issue | [autoscaling#978](https://github.com/llm-d/llm-d-autoscaling/issues/978) | e2e flaky query external metric tests | closed 2026-09-16 (WVA triage reset, not fixed) |
| issue | [autoscaling#1072](https://github.com/llm-d/llm-d-autoscaling/issues/1072) | metrics: use Kubernetes labels to associate metrics to variants instead of pod_name traversal | closed 2026-09-16 (WVA triage reset, not fixed) |
| issue | [autoscaling#1151](https://github.com/llm-d/llm-d-autoscaling/issues/1151) | Bug: in checking errors from Prometheus query | closed 2026-09-16 (WVA triage reset, not fixed) |
| issue | [autoscaling#1426](https://github.com/llm-d/llm-d-autoscaling/issues/1426) | fix(coordinator): Include namespace label in Prometheus queue metric queries to prevent cross-namespace collision | closed 2026-09-16 (WVA triage reset, not fixed) |
| issue | [autoscaling#1427](https://github.com/llm-d/llm-d-autoscaling/issues/1427) | fix(coordinator): Queue metric noise causes constant maxReplicas flipping and pod churn during scale-up | closed 2026-09-16 (WVA triage reset, not fixed) |
| issue | [autoscaling#1459](https://github.com/llm-d/llm-d-autoscaling/issues/1459) | fix(metrics): replica gauges and accel-tracking map never evicted on variant removal — stale series report dead variants | closed 2026-09-16 (WVA triage reset, not fixed) |
| issue | [autoscaling#1484](https://github.com/llm-d/llm-d-autoscaling/issues/1484) | fix(metrics): saturation/capacity gauges also leak on variant removal — extend the #1464 removal hook | closed 2026-09-16 (WVA triage reset, not fixed) |
| issue | [autoscaling#1514](https://github.com/llm-d/llm-d-autoscaling/issues/1514) | ServiceMonitor TLS serverName hardcoded to wva-system, silently breaks metric scraping in any other namespace | closed 2026-09-16 (WVA triage reset, not fixed) |
| PR | [autoscaling#1464](https://github.com/llm-d/llm-d-autoscaling/pull/1464) | fix(metrics): evict stale replica-gauge series on variant removal | closed unmerged 2026-09-05 (WVA deprecation) |
| PR | [autoscaling#1489](https://github.com/llm-d/llm-d-autoscaling/pull/1489) | Feat/rescale beta observability and hysteresis | closed unmerged 2026-09-04 (WVA deprecation) |
| PR | [autoscaling#1524](https://github.com/llm-d/llm-d-autoscaling/pull/1524) | fix(openshift): derive ServiceMonitor serverName from the deploy namespace | closed unmerged 2026-09-13 (WVA deprecation) |
| issue | [ipp#79](https://github.com/llm-d/llm-d-inference-payload-processor/issues/79) | design solution for high availability (HA) when using stateful metrics | closed 2026-09-19 (not planned / stale bot) |
| issue | [router#1075](https://github.com/llm-d/llm-d-router/issues/1075) | feat: Support port role specification in InferencePool (serving, metrics, health) | closed 2026-09-17 (not planned / stale bot) |

</details>


## Logs and trace-log correlation

_7 issues, 2 PRs. The trace_id/span_id defect is closed in router, kv-cache, and IPP. Router logs now follow the OTel Logs Data Model (router#2643, #2813); one severity-contract question remains._

| Type | Ref | Title | By | Age | Idle | Signals |
|---|---|---|---|---:|---:|---|
| issue | [model-svc#166](https://github.com/llm-d/llm-d-model-service/issues/166) | Improve log levels <br>`close it` | @jgchn | 495d | **495d** | `archived repo` |
| issue | [benchmark#1701](https://github.com/llm-d/llm-d-benchmark/issues/1701) | nok8s: On a vLLM readiness timeout, nok8s standup captures Envoy's logs instead of the failing vLLM worker's <br>`reported fixed by #1757; closeable` | @UgaTheDev | 52d | 52d |  |
| issue | [ipp#280](https://github.com/llm-d/llm-d-inference-payload-processor/issues/280) | datalayer.Model serializes as {} in structured logs in picker/selector <br>`PR #281` | @davidbreitgand | 47d | 47d | `kind/bug`, `needs-triage` |
| issue | [router#2470](https://github.com/llm-d/llm-d-router/issues/2470) | perf(epp): hot-path allocation and logging hygiene in the core framework <br>`sub-PRs merged; closeable` | @LukeAVanDrie | 32d | 32d | `needs-triage`, `area/epp` |
| issue | [router#2674](https://github.com/llm-d/llm-d-router/issues/2674) | Standardize JSON logs on the OTel Logs Data Model with trace_id/span_id <br>`PRs #2643, #2813 merged; closeable` | @den-rgb | 17d | 10d | `new`, `needs-triage` |
| issue | [router#2840](https://github.com/llm-d/llm-d-router/issues/2840) | Define the OpenTelemetry JSON stdout severity contract <br>`follow-up of merged PR #2813` | @den-rgb | 6d | 6d | `new` |
| issue | [router#2884](https://github.com/llm-d/llm-d-router/issues/2884) | coordinator: pipeline step timings log DPANICs, step names never logged | @804533125 | 4d | 0d | `new` |
| PR | [benchmark#1719](https://github.com/llm-d/llm-d-benchmark/pull/1719) | fix: nok8s readiness timeout dumps Envoy logs instead of the failing container <br>`closes #1701; superseded by #1757, CI red` | @elinacse | 50d | 12d |  |
| PR | [ipp#281](https://github.com/llm-d/llm-d-inference-payload-processor/pull/281) | Render datalayer.Model and ScoredModel in structured logs <br>`closes #280; rotten` | @davidbreitgand | 46d | 6d | `kind/bug`, `lifecycle/rotten`, `size/L` |

<details>
<summary>Resolved since 2026-08-12 (7)</summary>

| Type | Ref | Title | Outcome |
|---|---|---|---|
| PR | [router#2248](https://github.com/llm-d/llm-d-router/pull/2248) | fix(observability): inject trace_id/span_id into request loggers | closed unmerged 2026-08-14 |
| issue | [router#1630](https://github.com/llm-d/llm-d-router/issues/1630) | Logs are not correlated with traces: trace_id/span_id never injected into the logger | closed 2026-08-25 |
| PR | [router#2271](https://github.com/llm-d/llm-d-router/pull/2271) | tracing: correlate logs with traces at request entry points | merged 2026-08-25 |
| issue | [kv-cache#665](https://github.com/llm-d/llm-d-kv-cache/issues/665) | Logs are not correlated with traces: trace_id/span_id never injected into the logger | closed 2026-08-28 |
| issue | [autoscaling#1273](https://github.com/llm-d/llm-d-autoscaling/issues/1273) | Inject trace_id/span_id into structured logs for trace-log correlation | closed 2026-09-16 (WVA triage reset, not fixed) |
| issue | [autoscaling#1317](https://github.com/llm-d/llm-d-autoscaling/issues/1317) | Structured per-cycle log lines for analyzer and optimizer decisions | closed 2026-09-16 (WVA triage reset, not fixed) |
| PR | [autoscaling#1506](https://github.com/llm-d/llm-d-autoscaling/pull/1506) | fix: Inject trace_id/span_id into structured logs | closed unmerged 2026-09-05 (WVA deprecation) |

</details>


## Dashboards, alerts, and monitoring assets

_8 issues, 3 PRs. Grafana dashboards, Prometheus alert rules, and the consolidation of user-facing monitoring assets into llm-d/llm-d. Batch-gateway assets have moved; the WVA move needs a decision now that WVA is deprecated._

| Type | Ref | Title | By | Age | Idle | Signals |
|---|---|---|---|---:|---:|---|
| issue | [kv-cache#642](https://github.com/llm-d/llm-d-kv-cache/issues/642) | Operational Grafana Dashboard for Core Library | @gyliu513 | 106d | 14d | `lifecycle/stale` |
| issue | [kv-cache#664](https://github.com/llm-d/llm-d-kv-cache/issues/664) | Add Prometheus alerting rules for KV-cache metrics <br>`#676 and router#2330 closed; nothing in flight` | @gyliu513 | 100d | 2d | `lifecycle/stale` |
| issue | [llm-d#1983](https://github.com/llm-d/llm-d/issues/1983) | Consolidate observability assets for llm-d <br>`parent of the three moves below` | @gyliu513 | 82d | 8d | `enhancement` |
| issue | [batch-gw#619](https://github.com/llm-d/llm-d-batch-gateway/issues/619) | Move batch-gateway scrape manifests, alerts, and dashboards to llm-d/llm-d <br>`llm-d#2390 merged; closeable` | @gyliu513 | 58d | 58d | `enhancement` |
| issue | [kv-cache#708](https://github.com/llm-d/llm-d-kv-cache/issues/708) | Move llmd_fs_backend monitoring manifests and runbook to llm-d/llm-d <br>`nothing in flight` | @gyliu513 | 58d | 36d |  |
| issue | [autoscaling#1466](https://github.com/llm-d/llm-d-autoscaling/issues/1466) | Move user-facing monitoring assets to llm-d/llm-d <br>`PR llm-d#2363, docs PR #1556; WVA deprecated, re-scope` | @gyliu513 | 58d | 11d | `needs-triage` |
| issue | [llm-d#2157](https://github.com/llm-d/llm-d/issues/2157) | TPU Observability <br>`PodMonitor llm-d#2190 merged; dashboard PR #2487` | @nicolexin | 52d | 51d | `enhancement` |
| issue | [llm-d#2462](https://github.com/llm-d/llm-d/issues/2462) | Grafana panel for metric-to-trace navigation via exemplars <br>`PR #2474` | @sudoalok | 11d | 6d | `new`, `enhancement` |
| PR | [llm-d#2363](https://github.com/llm-d/llm-d/pull/2363) | docs(observability): add WVA dashboards and alerts to llm-d <br>`closes autoscaling#1466; conflicting, no reviews` | @SrikarChittemsetty | 28d | 17d |  |
| PR | [llm-d#2474](https://github.com/llm-d/llm-d/pull/2474) | Wire metric-to-trace navigation for EPP exemplars (Prometheus exemplar-storage, Jaeger datasource) <br>`closes #2462; depends on router#2774` | @sudoalok | 9d | 9d | `new` |
| PR | [llm-d#2487](https://github.com/llm-d/llm-d/pull/2487) | Add GKE TPU overview Grafana dashboard <br>`for #2157` | @bzsuni | 6d | 0d | `new` |

<details>
<summary>Resolved since 2026-08-12 (10)</summary>

| Type | Ref | Title | Outcome |
|---|---|---|---|
| PR | [llm-d#1629](https://github.com/llm-d/llm-d/pull/1629) | Add Grafana dashboard setup documentation for flow control | merged 2026-08-13 |
| PR | [kv-cache#676](https://github.com/llm-d/llm-d-kv-cache/pull/676) | Add Prometheus alerting rules for KV-cache metrics | closed unmerged 2026-08-14 |
| PR | [router#2368](https://github.com/llm-d/llm-d-router/pull/2368) | fix(charts): emit leading document separators in monitoring partials | merged 2026-08-14 |
| PR | [router#2330](https://github.com/llm-d/llm-d-router/pull/2330) | Add Prometheus alerting rules for KV-cache and EPP health | closed unmerged 2026-08-15 |
| issue | [llm-d#1777](https://github.com/llm-d/llm-d/issues/1777) | Add monitoring for llm-d-router to monitoring section in all well lit path guides | closed 2026-08-31 |
| PR | [llm-d#2215](https://github.com/llm-d/llm-d/pull/2215) | fix(observability): honor selected kubeconfig | merged 2026-08-31 |
| PR | [llm-d#2309](https://github.com/llm-d/llm-d/pull/2309) | Cover prometheus-operated in the Prometheus serving certificate | merged 2026-08-31 |
| PR | [llm-d#2390](https://github.com/llm-d/llm-d/pull/2390) | docs(observability): add batch-gateway dashboards and alerts to llm-d | merged 2026-09-11 |
| issue | [ipp#101](https://github.com/llm-d/llm-d-inference-payload-processor/issues/101) | create grafana dashboard for ipp metrics | closed 2026-09-13 |
| issue | [benchmark#1350](https://github.com/llm-d/llm-d-benchmark/issues/1350) | prometheusAdapter 5.3.0 -> kube-prometheus-stack-85.2.0 | closed 2026-09-19 (not planned / stale bot) |

</details>


## Semantic conventions and standardization

_2 issues, 2 PRs. router#708 is closed (router#2503, #2516 merged). The next-generation questions are code generation from a Weaver registry, opt-in OTel GenAI metrics, and the `kvcache_*` alias removal._

| Type | Ref | Title | By | Age | Idle | Signals |
|---|---|---|---|---:|---:|---|
| issue | [llm-d#2472](https://github.com/llm-d/llm-d/issues/2472) | Auto-generate llm-d telemetry docs and Go code from an OTel Weaver registry | @PlateauGao | 10d | 9d | `new`, `enhancement` |
| issue | [router#2906](https://github.com/llm-d/llm-d-router/issues/2906) | Add opt-in OpenTelemetry GenAI semantic convention metrics compatibility | @nicole-lihui | 3d | 3d | `new`, `needs-triage` |
| PR | [router#2943](https://github.com/llm-d/llm-d-router/pull/2943) | metrics: declare deprecation of kvcache_* metric aliases <br>`pair with #2942` | @804533125 | 0d | 0d | `new`, `size/S`, `area/kvcache`, `area/docs` |
| PR | [router#2942](https://github.com/llm-d/llm-d-router/pull/2942) | metrics: remove deprecated kvcache_* metric aliases <br>`depends on #2943; not before v0.12.0` | @804533125 | 0d | 0d | `new`, `size/L`, `area/kvcache`, `area/docs` |

<details>
<summary>Resolved since 2026-08-12 (8)</summary>

| Type | Ref | Title | Outcome |
|---|---|---|---|
| issue | [ipp#160](https://github.com/llm-d/llm-d-inference-payload-processor/issues/160) | Standardize OTel service and instrumentation scope naming | closed 2026-08-13 |
| PR | [kv-cache#654](https://github.com/llm-d/llm-d-kv-cache/pull/654) | feat(telemetry): standardize OTel instrumentation scope and span names | closed unmerged 2026-08-14 |
| PR | [router#2164](https://github.com/llm-d/llm-d-router/pull/2164) | feat(telemetry): align kvcache OTel scope and span names with router standard | merged 2026-08-19 |
| issue | [router#708](https://github.com/llm-d/llm-d-router/issues/708) | Embrace otel GenAI Semantic Convention for inference observability | closed 2026-09-01 |
| PR | [router#2503](https://github.com/llm-d/llm-d-router/pull/2503) | llm-d observability: align OpenTelemetry GenAI semconv and refactor telemetry usages | merged 2026-09-01 |
| issue | [async#413](https://github.com/llm-d/llm-d-async/issues/413) | tracing: align span attributes with OTel GenAI semconv and the llm_d.* namespace (router#708) | closed 2026-09-08 |
| PR | [router#2516](https://github.com/llm-d/llm-d-router/pull/2516) | llm-d observability: finish remaining OpenTelemetry GenAI semconv and telemetry refactoring | merged 2026-09-11 |
| issue | [kv-cache#651](https://github.com/llm-d/llm-d-kv-cache/issues/651) | Standardize OpenTelemetry instrumentation scope and span naming | closed 2026-09-14 |

</details>


## Documentation, guides, and blogs

_3 issues, 4 PRs. User-facing material. The tracing blog and per-guide troubleshooting for the optimized baseline shipped; the remaining guides need their observability sections._

| Type | Ref | Title | By | Age | Idle | Signals |
|---|---|---|---|---:|---:|---|
| issue | [kv-cache#643](https://github.com/llm-d/llm-d-kv-cache/issues/643) | Observability Documentation | @gyliu513 | 106d | 2d | `lifecycle/stale` |
| issue | [llm-d#1982](https://github.com/llm-d/llm-d/issues/1982) | Per-guide observability troubleshooting for well-lit paths <br>`#2129 merged; PR #2485 in flight` | @gyliu513 | 82d | 8d |  |
| issue | [llm-d#2369](https://github.com/llm-d/llm-d/issues/2369) | Add troubleshooting guidance for precise prefix cache routing | @cyclinder | 27d | 27d |  |
| PR | [llm-d#1959](https://github.com/llm-d/llm-d/pull/1959) | Add program-aware fairness scheduling and OTel trace replay benchmark to agentic-serving guide <br>`stale draft` | @pavanipenumalla | 87d | 41d | `draft`, `lifecycle/stale` |
| PR | [async#415](https://github.com/llm-d/llm-d-async/pull/415) | docs: split the user guide into per-topic pages under docs/ (adds docs/observability.md) | @shimib | 24d | 2d | `draft`, `lifecycle/stale` |
| PR | [autoscaling#1556](https://github.com/llm-d/llm-d-autoscaling/pull/1556) | docs: relabel the in-repo monitoring guide as development and CI <br>`part of #1466; conflicting` | @SrikarChittemsetty | 10d | 10d | `new` |
| PR | [llm-d#2485](https://github.com/llm-d/llm-d/pull/2485) | Tiered prefix cache guide: add observability and troubleshooting section <br>`part of #1982` | @k21993 | 7d | 3d | `new` |

<details>
<summary>Resolved since 2026-08-12 (5)</summary>

| Type | Ref | Title | Outcome |
|---|---|---|---|
| PR | [llm-d#2129](https://github.com/llm-d/llm-d/pull/2129) | docs(observability): add per-guide troubleshooting for the optimizedbaseline | merged 2026-08-14 |
| PR | [llm-d#2249](https://github.com/llm-d/llm-d/pull/2249) | docs: update flow control configuration and observability | merged 2026-08-14 |
| issue | [web#331](https://github.com/llm-d/llm-d.github.io/issues/331) | Create a blog for tracing observability | closed 2026-08-26 |
| PR | [web#469](https://github.com/llm-d/llm-d.github.io/pull/469) | add llm-d tracing blog | merged 2026-08-26 |
| PR | [llm-d#2368](https://github.com/llm-d/llm-d/pull/2368) | docs(observability): document NIXL transfer metrics | merged 2026-08-31 |

</details>


## Adjacent: metric consumers and signal quality

_11 issues, 6 PRs. Not SIG-owned, but they consume the signals the SIG defines. The legacy metric removal (router#1070) already broke one consumer (async#460); the rest of this list is where the next break will show up._

| Type | Ref | Title | By | Age | Idle | Signals |
|---|---|---|---|---:|---:|---|
| issue | [benchmark#482](https://github.com/llm-d/llm-d-benchmark/issues/482) | Define workload and SLO standards for GenAI applications and enterprise use cases | @jgchn | 326d | **219d** | `lifecycle/stale` |
| issue | [router#1182](https://github.com/llm-d/llm-d-router/issues/1182) | [Flow Control] Tenant Fairness: Virtual Token Count (VTC) and Dispersion Metrics <br>`rotten` | @LukeAVanDrie | 126d | 5d | `needs-triage`, `lifecycle/rotten` |
| issue | [llm-d#1767](https://github.com/llm-d/llm-d/issues/1767) | Migrate all autoscaling guides to KEDA (prometheus-adapter deprecated) <br>`PR #1773 closed` | @lionelvillard | 102d | 11d | `enhancement`, `lifecycle/stale` |
| issue | [router#2173](https://github.com/llm-d/llm-d-router/issues/2173) | Utilization detector: reconsider pool aggregation (average vs max) <br>`PR #2066` | @ruocco | 58d | 48d |  |
| issue | [router#2441](https://github.com/llm-d/llm-d-router/issues/2441) | perf(epp): reduce scrape overhead by filtering unused metric families <br>`PR #2442 (draft)` | @muchengl | 33d | 6d | `needs-triage`, `kind/performance` |
| issue | [router#2475](https://github.com/llm-d/llm-d-router/issues/2475) | Per-stage stale endpoint accounting for stage-aware saturation <br>`RFC #2786` | @loicmarchal | 31d | 31d | `needs-triage` |
| issue | [router#2514](https://github.com/llm-d/llm-d-router/issues/2514) | flowcontrol: warn when metrics refresh interval exceeds staleness threshold <br>`PR #2645` | @todayim | 29d | 19d |  |
| issue | [async#419](https://github.com/llm-d/llm-d-async/issues/419) | Feedback-based dispatch control (aimd pool gate driven by response feedback) <br>`proposal #379 approved; impl #382 on hold` | @jtechapps | 20d | 2d | `new`, `enhancement` |
| issue | [router#2822](https://github.com/llm-d/llm-d-router/issues/2822) | Scorers reading core metrics rank a never-scraped endpoint as the best candidate <br>`PR #2848` | @MicheleCampi | 7d | 6d | `new` |
| issue | [router#2890](https://github.com/llm-d/llm-d-router/issues/2890) | Expose per-metric presence and freshness from the core metrics extractor <br>`from review of #2833` | @albertoperdomo2 | 4d | 4d | `new`, `needs-triage` |
| issue | [async#460](https://github.com/llm-d/llm-d-async/issues/460) | prometheus-budget gate queries deprecated EPP metric names; stalls on llm_d_epp_*-only EPPs <br>`fallout of router#1070` | @jtechapps | 0d | 0d | `new` |
| PR | [llm-d#1926](https://github.com/llm-d/llm-d/pull/1926) | Inference cost tracking guide (OpenCost) - phase 1 | @simanadler | 88d | 2d |  |
| PR | [router#2442](https://github.com/llm-d/llm-d-router/pull/2442) | perf(epp): parse only metric families consumed by extractors <br>`closes #2441` | @muchengl | 33d | 10d | `draft`, `kind/feature`, `size/XL`, `area/datalayer` |
| PR | [router#2645](https://github.com/llm-d/llm-d-router/pull/2645) | fix: warn when refresh-metrics-interval exceeds metricsStalenessThreshold <br>`closes #2514; awaiting re-review` | @varad-ahirwadkar | 19d | 4d | `new`, `kind/bug`, `size/L`, `area/dev`, `area/epp`, `area/scheduling`, `area/flowcontrol` |
| PR | [router#2848](https://github.com/llm-d/llm-d-router/pull/2848) | fix(scheduling): omit never-scraped endpoints from metric scorers <br>`closes #2822` | @apurv-1 | 6d | 2d | `new`, `kind/bug`, `size/L`, `area/epp`, `area/scheduling` |
| PR | [router#2939](https://github.com/llm-d/llm-d-router/pull/2939) | epp: register a built-in metric mapping for the tokenspeed engine <br>`for llm-d#2022` | @0z5a | 0d | 0d | `new`, `kind/feature`, `size/L`, `area/epp`, `area/datalayer` |
| PR | [sim#728](https://github.com/llm-d/llm-d-inference-sim/pull/728) | Allow enabling fake vLLM metrics via POST /admin/config at runtime | @jland-redhat | 0d | 0d | `new`, `draft` |

<details>
<summary>Resolved since 2026-08-12 (13)</summary>

| Type | Ref | Title | Outcome |
|---|---|---|---|
| PR | [llm-d#2265](https://github.com/llm-d/llm-d/pull/2265) | refactor(recipes): add shared KEDA OCP metrics-reader auth component | merged 2026-08-13 |
| issue | [autoscaling#901](https://github.com/llm-d/llm-d-autoscaling/issues/901) | VLLM experiments and metrics analysis for the Throughput Analyzer | closed 2026-08-28 |
| issue | [router#2294](https://github.com/llm-d/llm-d-router/issues/2294) | [SGLang] Read current SGLang cache-capacity metrics | closed 2026-08-31 |
| issue | [router#2408](https://github.com/llm-d/llm-d-router/issues/2408) | flowcontrol: discuss configurable handling for stale endpoint metrics | closed 2026-09-09 |
| PR | [router#2492](https://github.com/llm-d/llm-d-router/pull/2492) | feat(flowcontrol): make stale-metrics scoring configurable | merged 2026-09-09 |
| issue | [autoscaling#1202](https://github.com/llm-d/llm-d-autoscaling/issues/1202) | Assess impact of llm-d-router EPP metrics rename (router#1071) on WVA scaling signals | closed 2026-09-14 |
| issue | [autoscaling#405](https://github.com/llm-d/llm-d-autoscaling/issues/405) | Define readiness for Pods based on fetched saturation-based metrics | closed 2026-09-16 (WVA triage reset, not fixed) |
| issue | [autoscaling#662](https://github.com/llm-d/llm-d-autoscaling/issues/662) | Better understanding of the kv_cache_usage_perc and num_requests_running metrics can be used to refine the saturation-based algorithm | closed 2026-09-16 (WVA triage reset, not fixed) |
| issue | [autoscaling#1016](https://github.com/llm-d/llm-d-autoscaling/issues/1016) | Align WVA Saturation Detection with EPP Metrics | closed 2026-09-16 (WVA triage reset, not fixed) |
| issue | [autoscaling#1455](https://github.com/llm-d/llm-d-autoscaling/issues/1455) | Metric-based analyzer interface | closed 2026-09-16 (WVA triage reset, not fixed) |
| issue | [autoscaling#1475](https://github.com/llm-d/llm-d-autoscaling/issues/1475) | Derive instances-per-unit from metrics topology for pending-replica capacity (saturation_v2 + throughput) | closed 2026-09-16 (WVA triage reset, not fixed) |
| PR | [autoscaling#1517](https://github.com/llm-d/llm-d-autoscaling/pull/1517) | Add KEDA autoscaling setup script for vLLM metrics | closed unmerged 2026-09-16 (WVA deprecation) |
| PR | [autoscaling#1543](https://github.com/llm-d/llm-d-autoscaling/pull/1543) | fix(saturation): treat missing KV/queue metrics as saturated, not empty | closed unmerged 2026-09-16 (WVA deprecation) |

</details>



## 评论 (6)

### UgaTheDev · 2026-08-13

@gyliu513 useful sweep. One correction and one offer.

The `benchmark#1701` row under logs is stale. It was fixed by #1757, which added a rollback to the nok8s readiness-failure path that dumps every launched container's logs before removing them, so the failing vLLM worker's logs are captured today rather than only Envoy's. I verified by applying the regression test from the open PR #1719 on top of current main with no source changes and it passes. So that row can come off the list, and #1719 is mostly superseded, which I have noted on the PR.

On the offer: `wva#360`, fix silent failure in metrics collection, has been open 253 days with no assignee and is the kind of defect I keep working on. Missing KV-cache metrics defaulting to 0 means a saturated pod reads as empty, so the autoscaler acts confidently on a wrong number. That is worse than an error, because nothing surfaces.

The code change is small. The real question is the semantics, whether a pod with missing metrics should be excluded from the capacity calculation or defaulted conservatively rather than to 0, and those give different scaling behaviour under partial scrape failure. If the SIG has a preference I will implement it, and if not I can write up the two options with the failure mode for each and let you pick.

For context, 12 of my merges are in llm-d-benchmark, plus fixes in the Kubernetes SIG inference-routing repo and vLLM.


### gyliu513 · 2026-08-13

Thanks @UgaTheDev , I will go through the list above and consolidate that soon, thanks for the update.

### cyclinder · 2026-08-24

Hi, I noticed the P/D coordinator dashboard already has panels for the vLLM NIXL metrics, but those metrics aren’t covered in the main metrics or PromQL docs yet.

Would a small PR adding the NIXL transfer metrics and a few useful queries be helpful? I’d be happy to work on it if it isn’t already covered elsewhere.

### gyliu513 · 2026-08-24

> Would a small PR adding the NIXL transfer metrics and a few useful queries be helpful? I’d be happy to work on it if it isn’t already covered elsewhere.

@cyclinder Yes, please go ahead.

### SrikarChittemsetty · 2026-08-27

@gyliu513 — you mentioned going through this list to consolidate for the next release. I re-verified the six "what to act on first" items against current state, since the sweep is two weeks old and most of them have moved. Four of six are resolved.

| # | Item | Status now |
|---|---|---|
| 1 | Two PRs for `router#1630` (`router#2248` / `#2271`) | **Resolved.** #2271 merged, #2248 closed, #1630 closed. |
| 2 | Two PRs adding KV-cache alert rules (`kv-cache#676` / `router#2330`) | **Resolved.** Both closed. |
| 3 | `kv-cache#654` approved and sitting | **Resolved.** Closed 14 Aug at your request; work moved to `router#2164`, **merged 19 Aug**. The semconv work it was gating in other repos is unblocked. |
| 4 | `router#708` semconv anchor untriaged | Still `needs-triage`. |
| 5 | Asset consolidation had no PRs | **Partly moving.** `llm-d#2363` is open for the WVA slice of `wva#1466` (dashboards, alerts, docs). The other children — `batch-gw#619`, `kv-cache#708` — still have nothing in flight. |
| 6 | Closable now | **Both still open.** See below. |

On item 6, both are still sitting and both look safely closable:

- **`deployer#357`** — draft, `WIP: DO NOT REVIEW: Tracing`, last touched **2 July 2025**. `llm-d-deployer` is archived (`archived: true`, last push 22 July 2025), so it cannot be merged from where it is.
- **`wva#236`** — this one is an *issue*, not a PR (the inventory lists it under PRs). Already labelled `duplicate` and `lifecycle/stale`, last touched 14 Feb, and `wva#198` — the issue it duplicates — is still open and is the one to keep.

Two smaller corrections for the next sweep, so the numbers stay trustworthy:

- The tracing table lists `wva#1272` with `PR #1508`; that PR is against **this** repo (`llm-d/llm-d-workload-variant-autoscaler#1508`), not the router, which is easy to misread in a cross-repo table.
- `wva#236` is an issue, as above.

Happy to keep this refreshed periodically if that's useful — it's cheap to re-verify and saves you the re-sweep. I'm not proposing any of the closes myself since they're your call, but items 1–3 look safe to tick off now.


### UgaTheDev · 2026-08-27

Closing the loop on my offer above: the wva#360 write-up is done and the fix is implemented.

- The two options (exclude the pod from the capacity calc vs. default it conservatively), with the scaling behavior each produces under partial scrape failure, are laid out on [wva#360](https://github.com/llm-d/llm-d-workload-variant-autoscaler/issues/360#issuecomment-5399377972) — short version: defaulting to "assume saturated" biases every downstream decision in the same direction the failure mode requires (block scale-down, allow scale-up), and reuses the existing `MinNonSaturatedReplicasForScaleDown` gate instead of new bookkeeping.
- The implementation is open as [wva#1543](https://github.com/llm-d/llm-d-workload-variant-autoscaler/pull/1543) — regression tests fail against the pre-fix behavior (a saturated pod with a failed scrape flipping a 2-replica scale-down to "safe"), CI is green.

A review from whoever owns the WVA side would let that one come off the inventory. Happy to adjust if the SIG prefers option A.

