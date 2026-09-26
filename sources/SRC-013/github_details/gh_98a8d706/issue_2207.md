# [Issue #2207] guides: pin router chart to released v0.9.0 instead of the mutable v0 tag (env.sh)

source: https://github.com/llm-d/llm-d/issues/2207
state: open | updated: 2026-09-04T16:48:33Z
labels: 

## 正文

## What / Why

[`guides/env.sh:8`](https://github.com/llm-d/llm-d/blob/main/guides/env.sh#L8) sets `ROUTER_CHART_VERSION=v0`, the **mutable rolling** chart tag. Every guide (and the workload-autoscaling nightly) inherits this single source of truth, so they all install bleeding-edge chart and pick up regressions the moment they merge upstream before any release, with no way to pin or reproduce.

This just bit us. [llm-d-router#1681](https://github.com/llm-d/llm-d-router/pull/1681) (merged 2026-08-06) shipped straight into `v0` and broke `llm-d-router-standalone`: the EPP `-epp` Service is never created when `flowControl`/`monitoring` are enabled (`helm template` renders it and `helm install` reports `deployed`, but it never appears at runtime). That makes EPP metrics unscrapeable and breaks the queue-based KEDA+EPP autoscaling guide and its new nightly. The same #1681 also caused the EPP `--config-file` CrashLoop (fixed by [llm-d-router#2322](https://github.com/llm-d/llm-d-router/pull/2322)) and overlaps with the shell-var expansion fix in #2177. The underlying chart bug is tracked upstream as [llm-d-router#2323](https://github.com/llm-d/llm-d-router/issues/2323).

## Evidence - the released artifact is fine, only the rolling tag is broken

Identical standalone install (base + optimized-baseline + monitoring + flowControl values):

| chart version | EPP `-epp` Service | pod |
| --- | --- | --- |
| `v0` (rolling) | **not created** | Ready 2/2, `deployed` |
| `v0.9.0` (release) | **created** | Ready 2/2, `deployed` |

`git compare v0.9.0...main` confirms #1681 is not in `v0.9.0`.

## Proposal

Pin to the latest released chart in `guides/env.sh`, and bump deliberately on each router release:

```diff
-export ROUTER_CHART_VERSION=v0
+export ROUTER_CHART_VERSION=v0.9.0
```

This makes guide walkthroughs and CI reproducible instead of silently tracking `main`, and aligns standalone with how the `llm-d-router-gateway` path is already pinned to `v0.9.0`.

## Safety check (no guide depends on an unreleased feature)

Verified before proposing repo-wide: only two values keys were added on `main` since `v0.9.0` `additional_addresses` (standalone) and `podAnnotations` (routerlib) and **no guide sets either**. The chart features guides actually rely on (`featureGates: [flowControl]`, monitoring) are present and working in `v0.9.0`.

/kind bug


## 评论 (5)

### mamy-CS · 2026-08-07

cc: @ahg-g 

### yiwxng · 2026-08-12

Taking this if it's free. I'll check whether v0.9.0 is still the latest released router chart before opening the PR.

### RishabhSaini · 2026-08-12

Hey @yiwxng yes v0.9.0 is the latest

### LukeAVanDrie · 2026-08-19

Per the maintainer decision on #2263: `main` tracks the floating `v0` chart channel as the development branch, and version pinning happens on release branches at release time. Maybe a short comment in `guides/env.sh` next to `ROUTER_CHART_VERSION` documenting the policy could help? Else should we close this issue?


### mdsraihaniqbal1999 · 2026-09-04

if this issue is open would love to work on it :), I am contributing to open source for the first time, if anyone needs any help or any issues for beginners happy to pick it up
