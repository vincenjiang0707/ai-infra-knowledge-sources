# [Issue #3968] [Feature] Allow configuring --metrics-agent-port to avoid conflict with fixed gRPC port 52365

source: https://github.com/ray-project/kuberay/issues/3968
state: open | updated: 2026-09-22T16:56:31Z
labels: stale

## 正文

## Root Cause

In Ray worker pods:

- dashboard_agent_grpc always binds to the fixed port 52365.
- dashboard_agent_http uses a random port if --metrics-agent-port is not specified.
- This randomness can cause port conflicts when it overlaps with the fixed 52365.

<img width="1116" height="113" alt="Image" src="https://github.com/user-attachments/assets/f7fd5351-51d1-4f6a-8f35-c9be8447c4e8" />

## Current Workaround

`spec:
  workerGroupSpecs:
  - groupName: small-group
    rayStartParams:
      metrics-agent-port: "52366"`


## Proposed Solution

- Document this clearly as a recommended configuration (so users don’t rely on random assignment).
- Optionally, provide a default non-random value (e.g., 52366) for metrics-agent-port, while keeping it overridable via rayStartParams.
- Ensure dashboard_agent_grpc (52365) and dashboard_agent_http (default 52366) do not overlap.



## 评论 (1)

### github-actions[bot] · 2026-09-22

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).
