# [Issue #2472] [Feature]: [Observability+Document Proposal] Auto-generate documentation for llm-d telemetry

source: https://github.com/llm-d/llm-d/issues/2472
state: open | updated: 2026-09-24T14:13:50Z
labels: enhancement

## 正文

### Feature Area

Documentation / Guides

### Problem Statement

**What would you like to be added**:

Adopt [OpenTelemetry Weaver](https://github.com/open-telemetry/weaver) as the single source of truth (SSOT) to manage, validate, and auto-generate documentation and Go code for all `llm-d` telemetry signals (metrics, trace spans, and shared attributes).

This issue serves as an umbrella proposal and follow-up to #708 (Embrace OTel GenAI Semantic Conventions) and #2503 (`pkg/telemetry`).


- **Eliminate Doc Drift**: `docs/metrics.md` currently contains ~600 lines of manually maintained tables. Changes to metrics, labels, types, and descriptions in Go code easily fall out of sync with documentation.
- **Span & Attribute Documentation**: While metrics are documented in markdown, router trace spans (EPP routing, scheduling, KV-cache operations) and their associated attributes lack a centralized, formal documentation catalog.
- **Shared Attributes Across Signals**: Attributes like `gen_ai.request.model`, `llm_d.fairness_id`, and `llm_d.priority` are shared across metrics and traces. Defining them centrally avoids duplicate definitions and naming mismatches.
- **OTel Upstream Alignment**: Defining custom `llm_d.*` telemetry in standard OTel semantic convention format makes it straightforward to propose general LLM inference conventions (e.g., KV-cache metrics) upstream to the OpenTelemetry GenAI SIG.





### Proposed Solution

I propose adopting **OpenTelemetry Weaver**, OTel's official schema and semantic convention engine:

1. **Schema Definition**: Define `llm_d` attributes, trace spans, and metrics in standard OTel semantic convention YAML registries.
2. **Auto-Generation**:
   - **Documentation**: Generate and update markdown documentation (`docs/metrics.md`, trace catalogs) automatically.
   - **Code**: Generate Go constants and typed helpers directly into `pkg/telemetry/`.
3. **CI Verification**: Use `weaver registry check` in presubmit to ensure code, documentation, and schema definitions never drift.

### Proposed Milestones

1. **Prototype Registry**: Set up initial Weaver YAML definitions and templates for existing `llm_d` metrics and trace spans.
2. **Doc & Code Generation**: Integrate Weaver generation into `Makefile`/`hack/` to generate `docs/metrics.md` and `pkg/telemetry/` constants.
3. **CI Guardrail**: Add a `make verify-telemetry-docs` presubmit check.
4. **Enhance telemetry description**: Telemetry owners are encouraged to improve the descriptions of existing signals



### Alternatives Considered

1. Add a generator script (e.g., `hack/update-metrics-docs.sh` / `hack/tools/metricsdocs`) to parse existing `compbasemetrics` declarations and generate the tables in `docs/metrics.md`.
2. Add a `make verify-metrics-docs` target and hook it into `make presubmit` so CI fails if code changes drift from `docs/metrics.md`.

Quicker but kinda short term solutions, only consider it if there is any objections on the OTLP tool

### Willingness to Contribute

Yes, I can submit a PR

### Additional Context


I am willing to contribute to the solution but sadly I cannot guarantee the timeline. 

### Questions / Maintainer Feedback

- Does the team agree with adopting OpenTelemetry Weaver as the overall approach for telemetry schema and documentation generation?
- Any preferences on registry location (e.g. `registry/` at repository root vs. `pkg/telemetry/registry/`)?

cc @gyliu513 @ahg-g 

## 评论 (2)

### PlateauGao · 2026-09-11

CC @gyliu513 

### gyliu513 · 2026-09-24

Thanks @PlateauGao, this is a great proposal and I'm +1 on the direction. Using Weaver as the single source of truth fits well with the semconv work from llm-d/llm-d-router#708 and llm-d/llm-d-router#2503.

A few things to sort out before we start:

**1. Start with attributes and spans, then metrics.** Traces and attributes are already OTel-native and centralized in the `semconv` package, so Weaver is a natural fit there. For phase 1 I'd suggest generating `llm_d.go` constants plus a trace span/attribute catalog. Metrics are harder: they are Prometheus metrics declared via `compbasemetrics` in about 15 places, many of them plugin-local, and they use Prometheus names (`llm_d_epp_*_seconds`) instead of OTel-style names. Before we move metrics over, we need to decide:
  - Do we generate the `compbasemetrics` declarations themselves with custom templates, or only generate docs from the registry?
  - How do we map OTel metric names and units to the Prometheus names we already expose, without breaking current series?
  - How do plugins own their own metric definitions?

 **2. Drift detection.** `weaver registry check` validates the registry itself, but it does not compare the registry against Go code. We only get a real guarantee if the code is generated from the registry (with a `make verify-*` that regenerates and diffs), or if we use `weaver registry live-check` against emitted telemetry. It would help if the milestones said which approach we will use for each signal type.

**3. Registry location.** I'd keep it in `llm-d-router`, close to the generated code, e.g. `pkg/common/observability/semconv/registry/` (or a top-level `semconv/` if other components will share it). Let's settle this in the first prototype PR. Then we can check how we can consolidate this across the whole llm-d org.

**4. Tooling.** Please pin the Weaver version (container image or binary) in `hack/` so local runs and CI produce the same output.

Suggested next step: a small prototype PR that covers only the `llm_d.*` attributes and a few EPP spans, with generated constants, a generated catalog doc, and a verify target. Then we can decide on metrics with something concrete to look at. Since the timeline is open, let's keep the phases small so others can pick up pieces, thoughts? 

/cc @ahg-g
