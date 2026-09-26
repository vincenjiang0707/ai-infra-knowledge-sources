# [Issue #4829] [Feature] Flush events properly on dashboard agents

source: https://github.com/ray-project/kuberay/issues/4829
state: open | updated: 2026-09-23T04:43:03Z
labels: enhancement, stale

## 正文

### Search before asking

- [x] I had searched in the [issues](https://github.com/ray-project/kuberay/issues) and found no similar feature requirement.


### Description

Disclaimer: this issue is related to ray core, but I think it's important to history server correctness and completeness, so I raise it here for feature tracking purpose. If the community thinks it improper, feel free to move around or close.

Behavior I've observed
When I was using RayJob with collector enabled, in a few times I don't see events collected at all.

History server collector collects ray events by setting up a HTTP server and receiving events sent by dashboard agent, which lives in each ray nodes. But currently in the agent, we don't have proper implementation for graceful shutdown, which synchronously flush all buffered events.

On SIGTERM (i.e., pod eviction), we don't flush buffered events https://github.com/ray-project/ray/blob/2d9c453f9f90cb7883a3c455bbc1be82f7b714d6/python/ray/dashboard/agent.py#L509-L521

On normal shutdown (i.e., RayJob finishes and ray cluster destructs), `AgentManager` sends un-actionable SIGKILL to dashboard agent https://github.com/ray-project/ray/blob/2d9c453f9f90cb7883a3c455bbc1be82f7b714d6/src/ray/raylet/agent_manager.cc#L114-L122
A followup question: should we also send SIGTERM to the process so we could implement termination hook, `waitpid` to block wait for a while before SIGKILL?

### Use case

Impact
- Not all the events are properly collected so users could view via history server
- For short jobs (in production, we have short jobs which runs for only several seconds in RayJob) I've seen situations where no events are collected at all


### Related issues

_No response_

### Are you willing to submit a PR?

- [ ] Yes I am willing to submit a PR!

## 评论 (3)

### 400Ping · 2026-05-13

I can try to work on this

### JiangJiaWei1103 · 2026-05-23

cc @chiayi to take a look. Thx!

### github-actions[bot] · 2026-09-23

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).
