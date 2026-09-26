# [Issue #1548] [CI/CD] Add daily Slack report for nightly test status

source: https://github.com/llm-d/llm-d/issues/1548
state: closed | updated: 2026-09-24T20:09:39Z
labels: enhancement, release/v0.9

## 正文

## Summary

Add a daily Slack report summarizing the status of all nightly CI workflows. This improves operational visibility into CI health and helps teams quickly identify failing tests requiring attention.

## Proposed Solution

Create `.github/workflows/nightly-status-report.yaml` that runs daily at 12:00 UTC (after all nightlies complete) and posts a Slack message summarizing results.

**Implementation:**
1. Create Slack incoming webhook for `#llm-d-ci` (or similar channel)
2. Add `SLACK_NIGHTLY_WEBHOOK` to GitHub secrets
3. Create workflow that:
   - Fetches last run status for each nightly workflow
   - Aggregates results (passed/failed counts)
   - Formats Slack message with links to failed runs
   - Posts via webhook

**Future enhancements:**
- Track consecutive failures (add emoji for chronic issues)
- Compare today vs yesterday (trend indicators)
- Alert on-call when critical tests fail
- Weekly summary with pass rate graphs

## Deliverables

- [ ] `.github/workflows/nightly-status-report.yaml` - Daily summary workflow
- [ ] Documentation in CONTRIBUTING.md about Slack bot
- [ ] Slack webhook configured (org admin task)
- [ ] Test run and validate message format

## Related Issues

- #1518 - Document CI system (this adds operational visibility)
- #1520 - v0.8 Release Goals (sig-cicd: solidify CI coverage and operations)

## Labels

`release/v0.8`, `sig-cicd`, `enhancement`, `good first issue`

## DRI

TBD (volunteer welcome!)


## 评论 (3)

### diegocastanibm · 2026-07-10

Picking this up from the CI/CD side. Before we build the "fetch last run status + aggregate" logic from scratch, I want to propose reusing what we already maintain, and I want to be explicit about the semantics so the Slack message isn't misleading.

We already have a single source of truth for nightly status: the matrix in release/README.md.

That matrix (between the <!-- NIGHTLY-MATRIX-START --> / <!-- NIGHTLY-MATRIX-END --> sentinels) enumerates every guide × provider (IBM/CKS/GKE/AMD/Intel) × accelerator (GPU/TPU/ROCm/XPU) combination we care about, and:

- It's kept in sync automatically by scripts/sync-nightly-matrix.py (discovers the nightly-e2e-* workflows and regenerates the table), so the list of what to report on is already curated and self-maintaining.
- Each cell's badge resolves to a live status JSON at https://llm-d.github.io/llm-d/badges/{badge_name}.json → {"message": "passing"|"failing"}, produced daily by the consolidate-status-* workflows at 10:00 UTC.


I would add something else → **Owner tagging on chronic failures**

On top of the snapshot: when a cell is failing, we'll @-tag the responsible guide owner in Slack so it's clear whose responsibility the fix is. Owners come straight from the per-guide OWNERS files (e.g. guides/optimized-baseline/OWNERS → approvers), which we already maintain. We will need a mapping: Slack mentions need Slack member IDs, and we don't have a GitHub-username → Slack-ID mapping in the repo today. So I'll a small mapping file manually.

Proposed implementation

1. Parse the matrix between the sentinels in release/README.md (or reuse sync-nightly-matrix.py's discovery) to get the grid + badge_name per cell.
2. Fetch https://llm-d.github.io/llm-d/badges/{badge_name}.json for each and read message.
3. Build the Slack message: pass/fail counts with links to the failing workflows.
4. For each failing cell, resolve the guide's OWNERS → Slack ID and @-tag them in the message.
5. Post via SLACK_NIGHTLY_WEBHOOK. Schedule at 12:00 UTC (after the 10:00 UTC consolidation refresh).

What do you think?
cc. @maugustosilva 

### diegocastanibm · 2026-08-20

FYI, this issue has been implemented but, instead of using a specific workflow to post in Slack, the `GitHub` app in Slack has been used to subscribe the channels to their corresponding workflows. List of the channels and their corresponding workflows below:
```
=== #sig-pd-disaggregation ===
/github subscribe llm-d/llm-d workflows:{name:"Nightly - PD Disaggregation E2E (AMD ROCM)"}
/github subscribe llm-d/llm-d workflows:{name:"Nightly - PD Disaggregation E2E (CKS GPU)"}
/github subscribe llm-d/llm-d workflows:{name:"Nightly - PD Disaggregation E2E (GKE GPU)"}
/github subscribe llm-d/llm-d workflows:{name:"Nightly - PD Disaggregation E2E (GKE TPU)"}
/github subscribe llm-d/llm-d workflows:{name:"Nightly - PD Disaggregation E2E (OCP GPU)"}

=== #sig-autoscaling ===
/github subscribe llm-d/llm-d workflows:{name:"Nightly - Workload Autoscaling E2E (CKS GPU)"}
/github subscribe llm-d/llm-d workflows:{name:"Nightly - Workload Autoscaling E2E (OCP GPU)"}
/github subscribe llm-d/llm-d workflows:{name:"Nightly - Workload Autoscaling KEDA+EPP Queue E2E (OCP GPU)"}

=== #sig-router (precise prefix cache routing, predicted latency routing, flow control) ===
/github subscribe llm-d/llm-d workflows:{name:"Nightly - Precise Prefix Cache Routing E2E (AMD ROCM)"}
/github subscribe llm-d/llm-d workflows:{name:"Nightly - Precise Prefix Cache Routing E2E (CKS GPU)"}
/github subscribe llm-d/llm-d workflows:{name:"Nightly - Precise Prefix Cache Routing E2E (GKE GPU)"}
/github subscribe llm-d/llm-d workflows:{name:"Nightly - Precise Prefix Cache E2E (GKE TPU)"}
/github subscribe llm-d/llm-d workflows:{name:"Nightly - Precise Prefix Cache Routing E2E (OCP GPU)"}
/github subscribe llm-d/llm-d workflows:{name:"Nightly - Predicted Latency Routing E2E (AMD ROCM)"}
/github subscribe llm-d/llm-d workflows:{name:"Nightly - Predicted Latency Routing E2E (CKS GPU)"}
/github subscribe llm-d/llm-d workflows:{name:"Nightly - Predicted Latency Routing E2E (GKE GPU)"}
/github subscribe llm-d/llm-d workflows:{name:"Nightly - Predicted Latency Routing E2E (OCP GPU)"}
/github subscribe llm-d/llm-d workflows:{name:"Nightly - Optimized Baseline E2E (AMD ROCM)"}
/github subscribe llm-d/llm-d workflows:{name:"Nightly - Optimized Baseline E2E (CKS GPU)"}
/github subscribe llm-d/llm-d workflows:{name:"Nightly - Optimized Baseline E2E (GKE GPU)"}
/github subscribe llm-d/llm-d workflows:{name:"Nightly - Optimized Baseline E2E (GKE GPU TensorRT-LLM)"}
/github subscribe llm-d/llm-d workflows:{name:"Nightly - Optimized Baseline E2E (GKE TPU)"}
/github subscribe llm-d/llm-d workflows:{name:"Nightly - Optimized Baseline E2E (OCP GPU)"}
/github subscribe llm-d/llm-d workflows:{name:"Nightly - Flow Control E2E (GKE GPU)"}

=== #sig-kv-disaggregation (tiered prefix cache / KV offloading) ===
/github subscribe llm-d/llm-d workflows:{name:"Nightly - Tiered Prefix Cache CPU Offloading LMCache E2E (GKE GPU)"}
/github subscribe llm-d/llm-d workflows:{name:"Nightly - Tiered Prefix Cache CPU Offloading E2E (GKE GPU)"}
/github subscribe llm-d/llm-d workflows:{name:"Nightly - Tiered Prefix Cache E2E (GKE TPU)"}
/github subscribe llm-d/llm-d workflows:{name:"Nightly - Tiered Prefix Cache CPU Offloading E2E (OCP GPU)"}
/github subscribe llm-d/llm-d workflows:{name:"Nightly - Wide EP LWS E2E (CKS GPU)"}
/github subscribe llm-d/llm-d workflows:{name:"Nightly - Wide EP LWS E2E (GKE GPU)"}
/github subscribe llm-d/llm-d workflows:{name:"Nightly - Wide EP LWS E2E (OCP GPU)"}

=== #sglang-collab (workflows backend SGLang) ===
/github subscribe llm-d/llm-d workflows:{name:"Nightly - Optimized Baseline E2E (GKE GPU SGLang)"}
/github subscribe llm-d/llm-d workflows:{name:"Nightly - PD Disaggregation E2E (GKE GPU SGLang)"}

=== #llm-d-intel (workflows Intel XPU) ===
/github subscribe llm-d/llm-d workflows:{name:"Nightly - Optimized Baseline E2E (Intel XPU)"}
/github subscribe llm-d/llm-d workflows:{name:"Nightly - PD Disaggregation E2E (Intel XPU)"}
/github subscribe llm-d/llm-d workflows:{name:"Nightly - Precise Prefix Cache Routing E2E (Intel XPU)"}
/github subscribe llm-d/llm-d workflows:{name:"Nightly - Tiered Prefix Cache CPU Offloading LMCache E2E (Intel XPU)"}
/github subscribe llm-d/llm-d workflows:{name:"Nightly - Tiered Prefix Cache CPU Offloading E2E (Intel XPU)"}
/github subscribe llm-d/llm-d workflows:{name:"Nightly - Wide EP LWS E2E (Intel XPU)"}

==== # fast-model-actuation =====
/github subscribe llm-d/llm-d workflows:{name:"Nightly - Fast Model Actuation E2E (OCP GPU)"}

=== NOT ASSIGNED YET ===
- Nightly - Multimodal Serving Aggregation E2E (GKE GPU)
- Nightly - Multimodal Serving Aggregation E2E (GKE TPU)
- Nightly - Multimodal Serving E-Disaggregation E2E (GKE GPU)

```
IMO, the issue can be closed

### diegocastanibm · 2026-08-25

I have removed the subscriptions described above because the `/github` app in Slack showed important limitations.
New proposal in #2366 : notifications in Slack are generated by the nightlies workflows
