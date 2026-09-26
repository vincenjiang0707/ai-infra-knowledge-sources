# [Issue #2462] [Feature]: [Observability] Grafana panel for metric-to-trace navigation via exemplars

source: https://github.com/llm-d/llm-d/issues/2462
state: open | updated: 2026-09-14T13:48:58Z
labels: enhancement

## 正文

### Feature Area

Observability / Monitoring

### Problem Statement

metrics tell you the fleet is slow, they don't tell you which request was slow.

an operator sees p99 jump on a dashboard and the only way to find an actual slow request is to guess a time range and scroll through traces by hand. the trace exists, there's just no path from the number to it.

llm-d/llm-d-router#2774 fixes the data side - the EPP now attaches the trace ID to llm_d_epp_request_duration_seconds as a prometheus exemplar and serves /metrics in openmetrics format so it survives the scrape. but nothing displays it yet, so the link is there and unusable.

### Proposed Solution

a panel under guides/recipes/observability/grafana/dashboards/ that shows the jump working.

what it needs:
- a latency panel (heatmap or p99 timeseries) over llm_d_epp_request_duration_seconds
- exemplars enabled on the prometheus datasource
- a datasource link from the exemplar's trace_id label to the traces datasource

end result: you see a spike, click the dot on it, and land on the trace for that exact request.

### Alternatives Considered

leaving it to operators to wire up themselves. the exemplars are exposed either way so this works, but the datasource link config isn't obvious and it's the kind of thing that's easier to ship once than to document.

adding it to an existing dashboard instead of a new panel - probably fine, whoever picks it up can decide. the diagnostic drilldown one might be the natural home.

### Willingness to Contribute

Yes, I can submit a PR

### Additional Context

follow up to llm-d/llm-d-router#2637, implemented in llm-d/llm-d-router#2774.

splitting it out because verifying it needs the whole stack running - an EPP serving real traffic, prometheus scraping it, a traces backend receiving spans, and grafana wired to both. i can't run that locally so i can't confirm the click-through actually works, only that the exemplar reaches the wire.

happy to write the panel json if someone with an environment can verify it, or hand it over entirely to whoever has the stack up.

one thing for whoever picks it up: prometheus needs exemplar storage on (--enable-feature=exemplar-storage) and has to request openmetrics on the scrape. without both, the exemplars get dropped in transit even though the EPP is emitting them correctly - and nothing errors, they just aren't there.

relates to SIG Observability.

## 评论 (6)

### sudoalok · 2026-09-09

/assign

### sudoalok · 2026-09-10

went through the recipe files properly. the panel is the small part of this.

i flagged exemplar storage at the bottom of the issue but it's worse than that - there are three things missing and none of them live in the dashboard json.

first one is the flag i already mentioned. `install-prometheus-grafana.sh` has no `enableFeatures` in `prometheusSpec` at all:

```yaml
prometheus:
  prometheusSpec:
    enableFeatures:
      - exemplar-storage
```

second, jaeger is never added to grafana as a datasource. the tracing script installs it, the prometheus script only registers prometheus. so even if the exemplar survives the scrape there's nothing for it to point at.

```yaml
- name: Jaeger
  type: jaeger
  uid: jaeger
  url: http://jaeger-collector.<ns>.svc.cluster.local:16686
  access: proxy
```

third, the prometheus datasource needs `exemplarTraceIdDestinations` or the trace_id label just sits there as text:

```yaml
jsonData:
  exemplarTraceIdDestinations:
    - name: trace_id
      datasourceUid: jaeger
```

the values file gets written twice in that script, once for central mode and once for individual, so the prometheus bits go in both.

and the tls branch already writes its own `jsonData` for `tlsSkipVerify`. add a second `jsonData` for the exemplar link and you've got a duplicate yaml key - one wins, the other quietly disappears. they have to be built into a single block before the heredoc.

the jaeger namespace is the bit i'm least sure about. tracing is optional and goes wherever the operator points `-n`, so hardcoding a namespace is wrong. i've got it detecting the `jaeger-collector` service and only wiring the link when it finds one, with `TRACING_NAMESPACE` to override. if you'd rather it was a flag that's easy to change.

on the panel - `llm-d-failure-saturation-dashboard.json` already has "Overall Latency P50/P90/P99" and that's the natural home. it's on `inference_objective_request_duration_seconds_bucket` though, and the exemplar is on `llm_d_epp_request_duration_seconds_bucket`. so it's a query change plus `"exemplar": true`, not a new panel.



### gyliu513 · 2026-09-10

@PlateauGao ^^

### PlateauGao · 2026-09-10

Thanks  @sudoalok for filing this proposal!

### 1. Feedback on Recipe Fixes

All points on `install-prometheus-grafana.sh` and the dashboard make sense to me.

Fully support landing this proposal to unblock the Prometheus recipe to address immediate need.

### 2. Longer-Term Architectural Perspective: Why OTLP Metrics Provides Better Correlation

While Prometheus exemplars solve the immediate need, looking forward across SIG-Observability, IMHO, OTLP metrics is where we get first-class trace-metric correlation with much less friction:

1. **Span-Level Precision (`trace_id` + `span_id`)**:
   - Prometheus/OpenMetrics exemplars generally only attach `trace_id`. Operators land on the root trace and must search through spans to find the relevant EPP decision.
   - The OTLP metrics data model natively captures **both `trace_id` and `span_id`**, allowing backends (Jaeger, Tempo, Cloud Monitoring) to deep-link directly to the specific span that observed the latency.

2. **Unified Telemetry Pipeline via OTel Collector**:
   - `llm-d` already deploys `otel-collector` (`install-otel-collector-jaeger.sh`) for OTLP traces.
   - Pushing OTLP metrics directly to the collector unifies metrics and traces into a single ingest path (rather than split push/pull architectures), and the collector can fan out to Prometheus (`prometheusremotewrite`), Tempo, or external backends.

3. **Consistency with Otlp GenAI Semantic Conventions**:
   - As we standardize GenAI semconv (https://github.com/llm-d/llm-d-router/issues/708)), OTel defines standardized GenAI metrics alongside spans. Native OTLP instrumentation keeps attributes and lifecycle semantics consistent across both signals.

### 3. Recommended Next Steps

- **Short term**: Proceed with this proposal to fix the Prometheus + Grafana recipe today.
- **Follow-up**: If we are aligned on the long term proposal, I can open an issue to explore adding an optional OTLP metrics exporter to EPP alongside `/metrics`, and adding a metrics pipeline in `otel-collector.yaml`.

Please let me know what you think :) 



### gyliu513 · 2026-09-14

Thanks @sudoalok for the detailed breakdown, and @PlateauGao for the longer-term view. Summarizing where I think we are so we can move:

**Short term: +1 to landing the recipe fix as proposed.** The three gaps (`exemplar-storage`, Jaeger datasource, `exemplarTraceIdDestinations`) are all real and all silent failures, so shipping them in the recipe is the right call. Auto-detecting `jaeger-collector` with a `TRACING_NAMESPACE` override is fine with me; no need for a separate flag. Reusing the existing P99 panel in `llm-d-failure-saturation-dashboard.json` instead of adding a new one also sounds right.

**Ordering.** llm-d/llm-d-router#2774 is still open. The recipe change in #2474 is harmless without it, but no dots will show up on the panel until the EPP image in the recipe includes #2774, so we should get the router PR reviewed and merged first, then do the end-to-end check against an EPP build that has it.

**Verification.** I check if I can do a end-to-end check: bring up the recipe with tracing, generate some traffic, and confirm that clicking an exemplar on the latency panel lands on the corresponding trace in Jaeger. One thing I'll also confirm while I'm there: that the Prometheus scrape actually negotiates OpenMetrics from the EPP (default `scrape_protocols` should prefer it, but worth seeing on the wire), since that is the other silent-drop path.

**Longer term (OTLP metrics).** @PlateauGao, agreed this is worth exploring, especially for `span_id`-level linking and a single ingest path through the collector. Please open a separate issue for it so we don't block this one. A couple of things to cover there: keeping `/metrics` as the default so existing Prometheus users are not affected, and how the collector's `prometheusremotewrite` path would preserve exemplars for people who stay on Prometheus + Grafana.

### gyliu513 · 2026-09-14

<img width="1395" height="956" alt="Image" src="https://github.com/user-attachments/assets/97253c94-80c5-48f2-b08c-2af64d5784a4" />

@sudoalok @PlateauGao I can see the metrics/tracing correlation works well with an e2e test, I will post some comments for your PR later. This will be a great feature for observability. Thanks!
