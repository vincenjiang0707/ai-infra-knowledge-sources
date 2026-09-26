# [Issue #2352] docs(epp): configuration reference documents the deprecated top-level `saturationDetector`, contradicting the schema and the shipped guide

source: https://github.com/llm-d/llm-d/issues/2352
state: closed | updated: 2026-08-28T06:48:18Z
labels: 

## 正文

**Area:** docs / EPP configuration reference
**Path:** Docs
**Severity:** high — the reference documents a deprecated field as the current one, in a call-out that states the opposite of the schema. Anyone following it configures a field the EPP ignores when the new one is also set, and gets no error either way.
**Build under test:** tag `v0.9.0` (commit `3291bca445be5bd309387fa78cc24f487f07003d`), which pins `ROUTER_EPP_VERSION=v0.10.0` in `guides/env.sh`

## Description

`docs/architecture/core/router/epp/configuration.md` presents `saturationDetector` as a top-level field of `EndpointPickerConfig`, and adds a NOTE specifically to emphasise it:

> While `saturationDetector` is presented here conceptually as part of Flow Control, it is a **top-level field** in the YAML schema, at the same level as `flowControl`.

In `llm-d-router` `v0.10.0` — the EPP version this release pins — the top-level field is deprecated in favour of the nested one:

```go
// apix/config/v1alpha1/endpointpickerconfig_types.go:67-71
// SaturationDetector specifies which saturation detector plugin to use.
//
// Deprecated: use flowControl.saturationDetector instead. If both are set, the new field is used.
// Tracked in https://github.com/llm-d/llm-d-router/issues/1308
SaturationDetector *SaturationDetectorConfig `json:"saturationDetector,omitempty"`
```

The repository's own manifest already uses the new form, so the docs and the shipped guide disagree with each other.

## Repro

1. `git checkout v0.9.0`
2. Read the `#### Saturation Detector` section of `docs/architecture/core/router/epp/configuration.md` — the example and the NOTE both put `saturationDetector` at the top level.
3. Read `guides/flow-control/router/flow-control.values.yaml` — `saturationDetector` is nested under `flowControl`:
   ```yaml
   flowControl:
     maxBytes: 10Gi
     maxRequests: 1k
     defaultRequestTTL: 60s
     saturationDetector:
       pluginRef: concurrency-detector
   ```
4. Check the schema in `llm-d-router` at the pinned version:
   `git show v0.10.0:apix/config/v1alpha1/endpointpickerconfig_types.go | grep -B4 'json:"saturationDetector'` — two declarations, the top-level one marked `Deprecated`.

## Expected

The configuration reference documents `flowControl.saturationDetector` as the current field, and marks the top-level one as deprecated with the precedence rule ("if both are set, the nested one wins").

## Actual

The reference documents only the top-level field and calls it out as the correct placement.

## Probable root cause

The docs predate the deprecation in llm-d-router#1308 and were not updated when the field moved.

## Suggested fix

In `docs/architecture/core/router/epp/configuration.md`, move the `saturationDetector` example under `flowControl`, and replace the NOTE with a deprecation note pointing at llm-d-router#1308.

## Scope

`guides/flow-control/tuning.md` also shows `saturationDetector` at the root of `EndpointPickerConfig`, so it needs the same change.

---
Found while building a documentation-derived knowledge base from the v0.9.0 tree and cross-checking every documented field against the EPP schema at the pinned version. No secrets in this report.


## 评论 (1)

### rishabhsinha17 · 2026-08-26

/assign
