# [Issue #2611] [Batch] Scale physical capacity of a running job to increase throughput

source: https://github.com/vllm-project/aibrix/issues/2611
state: open | updated: 2026-08-31T13:09:29Z
labels: kind/feature, area/batch

## 正文

## Problem

A running batch job can adapt request concurrency, but it cannot increase physical inference capacity when additional resources become available. The job therefore misses opportunities to improve throughput and finish earlier, even when it has a large backlog and eligible GPU capacity exists.

Client-side concurrency tuning alone cannot solve this problem because it only drives the already allocated backends harder.

## Expected outcome

AIBrix can add or release real inference capacity while a job is running. Newly available capacity processes remaining work, and capacity can be removed safely when demand falls or resources must be reclaimed.

The job remains one user-visible workload throughout these changes.

## Acceptance criteria

- A running job can increase its physical inference capacity without being restarted or resubmitted.
- Newly added capacity receives remaining work and produces a measurable increase in aggregate throughput.
- A running job can reduce physical capacity without losing committed results.
- Capacity removal, startup failure, or interruption causes unfinished work to be recovered automatically.
- Capacity changes do not create missing or duplicate committed output records.
- Job status exposes current capacity, requested capacity, observed throughput, and the reason for the latest capacity change.
- Scaling decisions respect job-level limits and completion constraints.
- The capability works for Kubernetes capacity and at least one externally provisioned GPU provider.
- The implementation demonstrably adds physical resources and does not report increased client concurrency as physical scale-out.

## Out of scope

This issue does not select the autoscaling signal, control algorithm, evaluation interval, or provider-specific scaling mechanism.

## 评论 (1)

### FeistyAryan · 2026-08-31

Hi Jeffwan,

This is an interesting problem. I’ve been looking closely at how dynamic capacity expansion works for long-running batch jobs without state loss or restarting workloads, and I'd love to contribute to this.

Before diving straight into implementation, I want to make sure I'm aligned with the core maintainers on the control loop design. I am planning to put together a brief proposal outlining:

1. How the reconciler will handle dynamic worker pool scaling without breaking active task leases.

2. State recovery mechanisms for when physical capacity is abruptly removed.

Could you please assign this issue to me, or let me know if there's an existing design doc/RFC for this that I should review first?
