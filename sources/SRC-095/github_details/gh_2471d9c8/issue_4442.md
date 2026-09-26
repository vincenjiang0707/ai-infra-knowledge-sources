# [Issue #4442] [Bug] [history server] [collector] NODE_*_EVENT of restarted workers are flushed to the old session

source: https://github.com/ray-project/kuberay/issues/4442
state: open | updated: 2026-09-22T16:58:10Z
labels: bug, stale

## 正文

### Search before asking

- [x] I searched the [issues](https://github.com/ray-project/kuberay/issues) and found no similar issues.


### KubeRay Component

Others

### What happened + What you expected to happen

- Observation: The `NODE_DEFINITION_EVENT` and the first `NODE_LIFECYCLE_EVENT` of the restarted worker (triggered by `OOMKilled`) are flushed to the old session.
- Expected behavior: The new worker's `NODE_*_EVENT` should be flushed to the new session.

Considering a cluster session is the lifecycle of a cluster instance, the collector must flush events to the correct session to facilitate accurate post-mortem analysis.



### Reproduction script

Events can be created by:

1. Deploy a Ray cluster
2. Submit a Ray job to the cluster
3. Trigger `OOMKilled` on both the worker and head

Then, we can analyze the flushed events.

### Anything else

[node_event_new_sess.md](https://github.com/user-attachments/files/24880244/node_event_new_sess.md)
[node_event_old_sess.md](https://github.com/user-attachments/files/24880243/node_event_old_sess.md)

### Are you willing to submit a PR?

- [x] Yes I am willing to submit a PR!

## 评论 (3)

### JiangJiaWei1103 · 2026-01-27

Hi @Future-Outlier, 

The problem is in the `PersistEvents` function; you can assign this to me. I'll resolve this after finishing endpoint-related tasks. Thanks.

### JiangJiaWei1103 · 2026-03-29

I just revisited this issue and the following summarizes my new findings:

## Goal

The event collector is responsible for persisting Ray events across:

- Cluster session boundaries (e.g., GCS failures)
- Node restarts (head or worker)

Our goal is to ensure no event loss under these scenarios.

##  Current Flushing Triggers

The collector flushes buffered events under four conditions:

- Collector shutdown (see [here](https://github.com/ray-project/kuberay/blob/4b11aa1d0bcf0c51f3629c0638f07c05eba7a77b/historyserver/pkg/collector/eventcollector/eventcollector.go#L104))
- Node ID change (see [here](https://github.com/ray-project/kuberay/blob/4b11aa1d0bcf0c51f3629c0638f07c05eba7a77b/historyserver/pkg/collector/eventcollector/eventcollector.go#L180-L183))
- Session change (see [here](https://github.com/ray-project/kuberay/blob/4b11aa1d0bcf0c51f3629c0638f07c05eba7a77b/historyserver/pkg/collector/eventcollector/eventcollector.go#L264-L265))
- Periodic flushing (see [here](https://github.com/ray-project/kuberay/blob/4b11aa1d0bcf0c51f3629c0638f07c05eba7a77b/historyserver/pkg/collector/eventcollector/eventcollector.go#L98-L100))

## Problems

### Issue 1: Event Loss on Session Change

In `PersistEvents`, when a session change is detected, the first event is written to buffer then an early `return` exits the function. Hence, the remaining events in the batch are dropped.

To reproduce, we:

1. Deploy a RayCluster (1 head, 1 worker)
2. Kill the ray-head container using `OOMKilled` (start a new session)

Then, we observed the the node definition event is persisted, but the lifecycle event (ALIVE) is silently dropped.

### Issue 2: S3 Writes Are Not Append-Safe

The current implementation uses `PutObject`. If multiple flushes write to the same object, the later writes overwrite earlier persisted data.

This is not an S3 limitation, but a mismatch between:

- Append-style event generation (exported by Ray)
- Overwrite-style object storage (s3 storage writer)

## Observations on Flushing Behavior

From experiments, we observed that node ID change consistently triggers flushing before session change, most event boundaries are already covered by **node-based flushing**. However, session change may still be the only trigger in certain edge cases (e.g., GCS with fault tolerance (need verification)). If all cases can be covered by node-based flushing, we can consider removing session-based flushing in the future.

## Proposed Improvement 

### Event Ingestion

- Remove early `return` in `PersistEvents`
- Keep existing flushing triggers unchanged
  - Treat node ID change as primary flush boundary
  - Keep session change as a fallback safety mechanism

### Storage Layer

Survey better practice than read-merge-write due to scalability concerns.

### github-actions[bot] · 2026-09-22

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).
