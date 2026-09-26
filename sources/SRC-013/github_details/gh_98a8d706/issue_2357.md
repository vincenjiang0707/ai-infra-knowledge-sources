# [Issue #2357] guides(wva): README shipped in v0.9.0 describes 0.9.0 as a future release (CRD removal, saturation engine v2 default)

source: https://github.com/llm-d/llm-d/issues/2357
state: open | updated: 2026-08-25T09:06:03Z
labels: 

## 正文

**Area:** guides / workload-autoscaling (WVA)
**Path:** Docs
**Severity:** medium — the guide describes the release it ships in as a future event, so a reader on v0.9.0 cannot tell whether the CRD they are about to use still exists or whether the engine they are enabling manually is already the default.
**Build under test:** tag `v0.9.0` (commit `3291bca445be5bd309387fa78cc24f487f07003d`)

## Description

`guides/workload-autoscaling/wva/README.md` talks about 0.9.0 in the future tense, inside the 0.9.0 tag:

- line 5: "The VariantAutoscaling CRD **will be removed in 0.9.0**."
- line 129: "Saturation engine v2 **will be the default in the next release (0.9.0)**, but for now it must be enabled manually. The v1 saturation engine will be deprecated in 0.9.0 and removed in 0.10.0."

A reader on this tag is left with two unanswered questions: is `VariantAutoscaling` still available in the version they are running, and does enabling saturation engine v2 by hand still apply?

## Repro

1. `git checkout v0.9.0`
2. `grep -n '0\.9\.0' guides/workload-autoscaling/wva/README.md`
3. Both statements refer to 0.9.0 as upcoming.

## Expected

At the 0.9.0 tag, the guide states the current state: whether the CRD was removed, and whether v2 is now the default.

## Actual

Statements written for a pre-0.9.0 reader, shipped unchanged in 0.9.0.

## Probable root cause

Release-cycle text written during 0.8.x and not revisited at the 0.9.0 cut.

## Suggested fix

Reword to the state of this release, and prefer explicit version comparisons ("as of 0.9.0, X") over "the next release", which goes stale silently at every cut.

## Scope

Related drift in the same area: `docs/architecture/advanced/autoscaling/hpa-wva.md` opens with a deprecation notice for the VariantAutoscaling approach, so a reader gets the deprecation from one page and the removal timeline from another, neither anchored to the version they are on.

---
Found while building a documentation-derived knowledge base from the v0.9.0 tree, by reading every version claim against the tag it ships in. No secrets in this report.


## 评论 (1)

### Neha-dot-Yadav · 2026-08-25

/assign
