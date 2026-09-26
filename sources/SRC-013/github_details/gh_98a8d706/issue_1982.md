# [Issue #1982] [Observability][Feature]: Per-guide observability troubleshooting for well-lit paths

source: https://github.com/llm-d/llm-d/issues/1982
state: open | updated: 2026-09-24T23:42:33Z
labels: 

## 正文

## Summary

Add **per-guide observability** sections to well-lit path guides in llm-d. This complements the observability work delivered in **#1685**, which establishes **`llm-d/llm-d` as the single user-facing home** for all observability assets (stack install, scrape manifests, alerts, dashboards, metric reference, and runbooks).

#1685 answers: *How do I enable monitoring?* (prerequisites → stack → scrape → dashboards)

This issue answers: *I'm running this guide as an operator — what should I be looking at, and why?*

> **Example:** When running **P/D disaggregation**, which metrics matter for diagnosing prefill/decode imbalance, KV transfer issues, or latency regressions?

## Motivation

- Each well-lit path has different failure modes and key signals; operators need **path-specific troubleshooting guidance**, not only generic metric catalogs.
- Per [proposals/observability-integration.md](https://github.com/llm-d/llm-d/blob/main/proposals/observability-integration.md) (#1685), observability docs and runbooks must live in **`llm-d/llm-d`** so they render on llm-d.ai and users only need to clone one repo.
- Per-guide observability extends that model: troubleshooting content for each well-lit path also lives in **`llm-d/llm-d`**, alongside the existing shared docs under `docs/operations/observability/`.

## Architectural context (#1685 — authoritative)

Per #1685, observability has **two homes**, split by audience:

| Home | Repo | What lives here |
|------|------|-----------------|
| **User-facing** | **`llm-d/llm-d`** | Everything a user deploys, follows, or reads: Prometheus/Grafana install, **all** scrape manifests, **all** alerts, **all** Grafana dashboards, tracing config, **metric reference**, **runbooks**, and every "enable monitoring" / troubleshooting guide. |
| **Source / definition** | Each **component** repo | Metric names/types/labels the code emits (`docs/metrics.md`), plus dev/CI monitoring manifests for that repo's own testing — **not** a user deployment surface. |

**Key rules from #1685:**

- **If a user deploys it or follows it, it lives in `llm-d/llm-d`.**
- Component `deploy/` folders are dev/CI scaffolding — not where we point operators.
- Metric definitions stay with the code; the **user-facing reference** in `llm-d/llm-d` is kept in sync in the same PR.

```text
llm-d/llm-d (user-facing home — single clone)
  guides/*/README.md ............... "enable monitoring" + per-guide troubleshooting
  guides/recipes/observability/ .... stack, dashboards, tracing
  guides/recipes/.../monitoring/ ... PodMonitor / ServiceMonitor / PrometheusRule
  docs/operations/observability/ ... metric reference + runbooks (llm-d.ai)
        ↑ syncs metric names with component docs/metrics.md
llm-d-router, WVA, llm-d-kv-cache, IPP, … (source / definition only)
  code emits metrics; docs/metrics.md is definitional; dev/CI manifests stay local
```

## Scope

| In scope (all in `llm-d/llm-d`) | Out of scope |
|---------------------------------|--------------|
| Per-guide **Observability / Troubleshooting** sections in `guides/*/README.md` | Re-documenting the four-step "Enable monitoring" flow (#1685 already defines this) |
| Path-specific metric guidance in `docs/operations/observability/` (e.g. per-path PromQL, troubleshooting runbooks) | Asking operators to clone component repos for scrape/dashboards/runbooks |
| Short overviews + links in `docs/well-lit-paths/` | Duplicating metric **definitions** — those stay in component `docs/metrics.md` |
| User-facing assets for any component used by a guide (router/EPP, WVA, kv-cache, IPP) under llm-d recipes/docs | Component dev/CI monitoring manifests |

Each well-lit path should eventually have troubleshooting guidance. Prioritize by operator impact and deployment frequency.

## Component coverage (all user-facing content in llm-d)

Per #1685, operators never hunt across repos. For each component a guide uses, **llm-d** carries the deployable assets and docs; component repos carry only metric definitions.

| Component | Metric source (definition only) | User-facing home in `llm-d/llm-d` |
|-----------|--------------------------------|-------------------------------------|
| Model servers | vLLM/SGLang upstream | `guides/recipes/modelserver/components/monitoring/`; [docs/operations/observability/metrics.md](https://github.com/llm-d/llm-d/blob/main/docs/operations/observability/metrics.md) |
| Router / EPP | [llm-d-router docs/metrics.md](https://github.com/llm-d/llm-d-router/blob/main/docs/metrics.md) | `guides/recipes/router/features/monitoring.values.yaml` + scrape/alerts recipes; metric reference + runbook under `docs/operations/observability/` |
| WVA | WVA `docs/metrics.md` | scrape, dashboards, enable-monitoring docs in llm-d recipes/docs |
| KV cache | llm-d-kv-cache metric definitions | scrape, dashboards, docs in llm-d |
| IPP | llm-d-inference-payload-processor metric definitions | scrape, dashboards, docs in llm-d (when IPP is used by a guide) |

### EPP (router) — cross-cutting

EPP appears in nearly every well-lit path. Per-guide troubleshooting should highlight **path-relevant EPP metrics** (with full reference in `docs/operations/observability/`), for example:

- **P/D disaggregation** → scheduler e2e latency, prefill/decode scheduling behavior
- **Precise prefix cache routing** → prefix indexer size, hit ratio
- **Flow control** → flow control queue depth / bytes
- **Workload autoscaling** → EPP queue depth alongside model server waiting/running requests

### IPP — when a guide deploys it

IPP is not in all well-lit paths today. When a guide uses IPP:

- User-facing scrape, dashboards, metric reference, and runbook belong in **`llm-d/llm-d`** (per #1685)
- IPP repo keeps `docs/metrics.md` as the definitional source, synced into llm-d in the same PR
- The guide's troubleshooting section covers path-relevant IPP signals (e.g. model selector attempts, plugin latency, request TTFT by model)

Guides that do **not** deploy IPP omit an IPP section.

## Proposed content per guide

Add an **Observability / Troubleshooting** subsection **after** the existing four-step "Enable monitoring" section (#1685 guide checklist):

1. **Key metrics** — the most important signals for that path (model server, EPP, WVA, kv-cache, IPP as relevant)
2. **Why they matter** — how each metric relates to the path's architecture and common failure modes
3. **What to check when things go wrong** — practical troubleshooting flows (e.g. high TTFT, prefill backlog, decode starvation, low prefix hit rate, missing scrape data)
4. **Links** — [docs/operations/observability/](https://github.com/llm-d/llm-d/tree/main/docs/operations/observability) (setup, metrics, [PromQL](https://github.com/llm-d/llm-d/blob/main/docs/operations/observability/promql.md), tracing) — all within llm-d, no cross-repo runbook hops

### Suggested locations

| Location | Content |
|----------|---------|
| `docs/well-lit-paths/foundations/*.md` | Short overview + link to guide troubleshooting section |
| `docs/well-lit-paths/workloads/*.md` | Same for workload narratives |
| `guides/*/README.md` | Detailed per-guide observability / troubleshooting section |
| `docs/operations/observability/` | Shared + path-specific metric reference, PromQL, and runbooks (rendered on llm-d.ai) |

## Initial paths to prioritize

**Phase 1 — high-traffic foundations:**

- [x] P/D disaggregation (`guides/pd-disaggregation`, `docs/well-lit-paths/foundations/pd-disaggregation.md`) https://github.com/llm-d/llm-d/pull/2128
- [x] Optimized baseline https://github.com/llm-d/llm-d/pull/2129
- [x] Workload autoscaling (WVA + EPP + model server composed signals) https://github.com/llm-d/llm-d/pull/2130

**Phase 2 — KV-cache & routing:**

- [ ] Tiered prefix cache
- [ ] Precise prefix cache routing
- [ ] Predicted latency routing

**Phase 3 — remaining foundations + workloads:**

- [ ] Wide expert-parallelism, Flow control, Rollouts
- [ ] Agentic serving, Multimodal serving, Batch serving

**Parallel work in llm-d (per #1685, not in component repos):**

- [ ] Ensure user-facing metric reference and runbooks for router/EPP, WVA, kv-cache, and IPP (when applicable) are complete under `docs/operations/observability/` and kept in sync with component `docs/metrics.md`
- [ ] Ensure deployable scrape manifests, alerts, and dashboards for each component used by prioritized guides exist in llm-d recipes

**Experimental guides** (lower priority): async processing, batch gateway, encode disaggregation.

## Template & acceptance criteria

- [ ] Reusable template: one complete example guide (P/D disaggregation) + contributor note
- [ ] Troubleshooting content lives entirely in **`llm-d/llm-d`** — operators clone only llm-d
- [ ] Per-guide sections link to `docs/operations/observability/` (not component-repo runbooks)
- [ ] Metric references in llm-d stay in sync with component `docs/metrics.md` (#1685 review expectation)
- [ ] `docs/well-lit-paths/` pages link down to guide troubleshooting sections

## Related work

- **#1685** — [Observability integration across the llm-d stack](https://github.com/llm-d/llm-d/pull/1685) (merged; authoritative model — `llm-d/llm-d` is the single user-facing home)
- [proposals/observability-integration.md](https://github.com/llm-d/llm-d/blob/main/proposals/observability-integration.md)
- [docs/operations/observability/](https://github.com/llm-d/llm-d/tree/main/docs/operations/observability/) — shared setup, metrics, PromQL, tracing
- #1670 — original discussion (superseded by #1685 for asset placement)

/cc @robertgshaw2-redhat

### Feature Area

Observability / Monitoring

### Willingness to Contribute

Yes, I can submit a PR

## 评论 (6)

### gyliu513 · 2026-07-28

NOTE: I will use a template below for the documents:

## Per-guide Observability & Troubleshooting: contributor template

This is the reusable template for the per-guide observability sections tracked in this issue. The completed reference example is the [P/D Disaggregation guide](https://github.com/llm-d/llm-d/tree/main/guides/pd-disaggregation#4-observability--troubleshooting).

**Placement**

Add the section to `guides/<path>/README.md` right after the four-step "Enable Monitoring" section, as the next numbered step. Add a short pointer to it from the matching `docs/well-lit-paths/**/<path>.md` overview page.

**Rules (from #1685)**

- All user-facing content lives in `llm-d/llm-d`. Never point operators at component `deploy/` folders or component-repo runbooks.
- Link, do not duplicate. Reference the shared [metrics](https://github.com/llm-d/llm-d/blob/main/docs/operations/observability/metrics.md), [PromQL](https://github.com/llm-d/llm-d/blob/main/docs/operations/observability/promql.md), and [alerting](https://github.com/llm-d/llm-d/blob/main/docs/operations/observability/alerting.md) docs instead of re-listing metric definitions. The per-guide section only adds path-specific interpretation.
- Metric names must match the component's `docs/metrics.md`; keep them in sync in the same PR if they change.
- Cover only the components the guide actually deploys (model server, EPP, and WVA / kv-cache / IPP as relevant). Omit sections for components the path does not use.

**Template**

````markdown
### N. Observability & Troubleshooting

<!-- One or two sentences: what makes this path distinct to operate, and which
     signals to watch together because of that architecture. -->

#### Key metrics for this path

| Signal | Why it matters for <path> | Where to look |
|--------|---------------------------|---------------|
| <metric> | <how it maps to this path's architecture / failure modes> | link to shared metrics/PromQL refs |

#### Common failure modes

* **<symptom>**: <likely cause>, <what to check first>.
* **<symptom>**: <likely cause>, <what to check first>.

For alert rules covering these signals, see the Alerting doc.
````

**Per-guide PR checklist**

- [ ] Section added after "Enable Monitoring" in `guides/<path>/README.md`
- [ ] Overview pointer added in the matching `docs/well-lit-paths/**/<path>.md`
- [ ] Metrics link to the shared references; no metric definitions duplicated
- [ ] Only components the guide deploys are covered
- [ ] Metric names verified against the component `docs/metrics.md`

### cyclinder · 2026-08-24

Hi, I'd like to help with the Phase 2 work for precise prefix cache routing. Is anyone already working on that part? If not, could you assign it to me?

I’m thinking of adding some practical troubleshooting guidance around cache hit rate, prefix index metrics, router latency/queue signals, and where to look in traces. Happy to adjust the scope based on your suggestions.

### gyliu513 · 2026-08-24

@cyclinder we do not have issue opened yet for phase2 yet, can you open an issue for that and assign to yourself? Thanks

### malamsyah · 2026-09-11

I'd like to take the Phase 2 predicted-latency slice of this issue.

Plan:
- Add an Observability & Troubleshooting section to `guides/predicted-latency-routing/README.md` after Enable monitoring, following the P/D / optimized-baseline template.
- Fold the existing Troubleshooting table at the bottom of that README into that section (predicted-vs-actual drift, empty prediction metrics, `streamingMode`, fallback to heuristic scoring).
- Cite the series already documented in `docs/architecture/advanced/latency-predictor.md` and `docs/operations/observability/metrics.md` (Predicted Latency & SLO). No new PromQL.
- Add a short Observability paragraph on `docs/well-lit-paths/foundations/predicted-latency.md` that links down to the guide section.

Not taking tiered-prefix or precise-prefix (#2369) in this PR.

### k21993 · 2026-09-13

I'd like to take the Phase 2 tiered prefix cache slice.

Plan:
- Add an Observability & Troubleshooting section to `guides/tiered-prefix-cache/README.md` after "(Optional) Enable monitoring", following the P/D and optimized-baseline sections.
- Cover what is specific to offloading: CPU tier store/load activity from vLLM's `OffloadingConnector` (`vllm:kv_offload_*`), the EPP's per-tier prefix index (`llm_d_epp_prefix_indexer_*` split by `plugin_name`, GPU vs CPU producer), and TTFT against an HBM-only baseline. SGLang HiCache and LMCache get the equivalent series where they exist.
- Add the offload series to `docs/operations/observability/metrics.md` and a few queries to `promql.md`, since neither covers offloading today.
- Add a short Observability paragraph to `docs/well-lit-paths/foundations/tiered-prefix-cache.md` that links to the guide section.

Not taking precise prefix (#2369) or predicted latency.


### k21993 · 2026-09-24

Now that the tiered prefix cache section has merged (#2485), I'd like to take the wide expert parallelism slice of Phase 3.

Plan:
- Add an Observability & Troubleshooting section to `guides/wide-ep/README.md` after "3. (Optional) Enable Monitoring", following the P/D, optimized-baseline and tiered prefix cache sections.
- Cover what is specific to this path: per DP rank signals (the guide's monitoring overlay scrapes rank0 to rank7 as separate targets), prefill and decode balance across the `DisaggregatedSet`, NIXL KV transfer health between the roles, and the DeepEP dispatch/combine requirements that surface at startup rather than in metrics.
- Reuse the shared metric and PromQL references, adding wide-EP queries to `docs/operations/observability/promql.md` where the existing P/D ones do not cover the per-rank breakdown.
- Add a short Observability paragraph to `docs/well-lit-paths/foundations/wide-expert-parallelism.md`.

Not taking flow control or rollouts in this PR.

