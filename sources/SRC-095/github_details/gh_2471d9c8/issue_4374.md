# [Issue #4374] [Epic][Feature][history server] Web Server + Event Processor

source: https://github.com/ray-project/kuberay/issues/4374
state: open | updated: 2026-09-22T16:57:54Z
labels: stale

## 正文

follow-ups from this PR: https://github.com/ray-project/kuberay/pull/4329

We need to use the following events to reconstruct ray dashboard's endpoint.

| # | eventType | nestedKey | Has jobId? | AQAAAA== | AgAAAA== | node_events | Total |
|---|-----------|-----------|------------|----------|----------|-------------|-------|
| 1 | DRIVER_JOB_DEFINITION_EVENT | `driverJobDefinitionEvent` | ✅ Yes | 0 | 1 | 0 | 1 |
| 2 | DRIVER_JOB_LIFECYCLE_EVENT | `driverJobLifecycleEvent` | ✅ Yes | 0 | 2 | 0 | 2 |
| 3 | TASK_DEFINITION_EVENT | `taskDefinitionEvent` | ✅ Yes | 1 | 3 | 0 | 4 |
| 4 | TASK_LIFECYCLE_EVENT | `taskLifecycleEvent` | ⚠️ Sometimes empty | 0 | 4 | 2 | 6 |
| 5 | TASK_PROFILE_EVENT | `taskProfileEvents` | ✅ Yes | 3 | 1 | 0 | 4 |
| 6 | ACTOR_DEFINITION_EVENT | `actorDefinitionEvent` | ✅ Yes | 1 | 1 | 0 | 2 |
| 7 | ACTOR_TASK_DEFINITION_EVENT | `actorTaskDefinitionEvent` | ✅ Yes | 0 | 2 | 0 | 2 |
| 8 | NODE_DEFINITION_EVENT | `nodeDefinitionEvent` | ❌ No | 0 | 0 | 2 | 2 |
| 9 | NODE_LIFECYCLE_EVENT | `nodeLifecycleEvent` | ❌ No | 0 | 0 | 3 | 3 |
| 10 | ACTOR_LIFECYCLE_EVENT | `actorLifecycleEvent` | ❌ No | 0 | 0 | 4 | 4 |
| | **Total** | | | **5** | **14** | **11** | **30** |




## 评论 (1)

### github-actions[bot] · 2026-09-22

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).
