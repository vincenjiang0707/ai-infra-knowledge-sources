# [Issue #3696] [Serve] RayServe Pods Stuck in Unready State Causing API Outages

source: https://github.com/ray-project/kuberay/issues/3696
state: open | updated: 2026-09-26T16:22:29Z
labels: 

## 正文

### What happened + What you expected to happen

Predict APIs on one of our endpoints were consistently returning errors, leading to outages in one of our production workflows. The issue later extended to other API routes too, and thereby impacting other functionalities as well.

### Root Cause Analysis
- A particular type of app failed to schedule on the RayServe platform for multiple deployments
- Pods were consistently stuck in an **Unready** state with repeated errors in logs:
`runtime_env_agent_client.cc:369: Create runtime env for job 01000000`

- Although a single replica of one of the deployments was initially available, it was eventually terminated as well.
- Due to this, the **readinessProbe/livenessProbe** checks were intermittently failing on port `8000` for the `rayserve-worker` pods.
- Additionally, the **GCS health check** endpoint (`/api/gcs_healthz` on port `8265`) failed for the `ray-head` container in the **RayServe head pod**.

Observing the same log being printed again and again in the cpu-only worker pod which is Unready
```
2025-05-22T07:41:14.392669721Z ray-cpu-worker [2025-05-22 00:41:14,392 I 64 64] (raylet) runtime_env_agent_client.cc:369: Create runtime env for job 01000000
2025-05-22T07:41:14.392808161Z ray-cpu-worker [2025-05-22 00:41:14,392 I 64 64] (raylet) runtime_env_agent_client.cc:369: Create runtime env for job 01000000
2025-05-22T07:41:14.897660052Z ray-cpu-worker [2025-05-22 00:41:14,897 I 64 64] (raylet) runtime_env_agent_client.cc:369: Create runtime env for job 01000000
2025-05-22T07:41:14.897811652Z ray-cpu-worker [2025-05-22 00:41:14,897 I 64 64] (raylet) runtime_env_agent_client.cc:369: Create runtime env for job 01000000
2025-05-22T07:41:15.674839026Z ray-cpu-worker [2025-05-22 00:41:15,674 I 64 64] (raylet) runtime_env_agent_client.cc:369: Create runtime env for job 01000000
2025-05-22T07:41:15.674978757Z ray-cpu-worker [2025-05-22 00:41:15,674 I 64 64] (raylet) runtime_env_agent_client.cc:369: Create runtime env for job 01000000
2025-05-22T07:41:16.401727748Z ray-cpu-worker [2025-05-22 00:41:16,401 I 64 64] (raylet) runtime_env_agent_client.cc:369: Create runtime env for job 01000000
2025-05-22T07:41:16.401851197Z ray-cpu-worker [2025-05-22 00:41:16,401 I 64 64] (raylet) runtime_env_agent_client.cc:369: Create runtime env for job 01000000
2025-05-22T07:41:17.097810089Z ray-cpu-worker [2025-05-22 00:41:17,097 I 64 64] (raylet) runtime_env_agent_client.cc:369: Create runtime env for job 01000000
2025-05-22T07:41:17.097955459Z ray-cpu-worker [2025-05-22 00:41:17,097 I 64 64] (raylet) runtime_env_agent_client.cc:369: Create runtime env for job 01000000
2025-05-22T07:41:17.801948110Z ray-cpu-worker [2025-05-22 00:41:17,801 I 64 64] (raylet) runtime_env_agent_client.cc:369: Create runtime env for job 01000000
```

Runtime setup log (runtime_env_setup-01000000.log) also has repeated logs:
```
2025-05-22 00:42:29,997 INFO plugin.py:257 -- Runtime env pip pip://03b0b4b60765962f148fd91e395c8ad4f321e3bf is already installed and will be reused. Search all runtime_env_setup-*.log to find the corresponding setup log.      

2025-05-22 00:42:29,997 INFO uri_cache.py:71 -- Marked URI pip://03b0b4b60765962f148fd91e395c8ad4f321e3bf used.                                                                    

2025-05-22 00:42:30,719 INFO uri_cache.py:84 -- Added URI gs://pixelbin-ml-worker-queue/ray-applications/RayApplicationsCI-deploy.ray.view-detection.v13.1746474693.zip with size 187817                                                                                                                                                                              

2025-05-22 00:42:30,719 INFO plugin.py:257 -- Runtime env pip pip://03b0b4b60765962f148fd91e395c8ad4f321e3bf is already installed and will be reused. Search all runtime_env_setup-*.log to find the corresponding setup log.                                                                                                                                         

2025-05-22 00:42:30,719 INFO uri_cache.py:71 -- Marked URI pip://03b0b4b60765962f148fd91e395c8ad4f321e3bf used.                                                                    

2025-05-22 00:42:31,418 INFO uri_cache.py:84 -- Added URI gs://pixelbin-ml-worker-queue/ray-applications/RayApplicationsCI-deploy.ray.view-detection.v13.1746474693.zip with size 187817                                                                                                                                                                              

2025-05-22 00:42:31,418 INFO plugin.py:257 -- Runtime env pip pip://03b0b4b60765962f148fd91e395c8ad4f321e3bf is already installed and will be reused. Search all runtime_env_setup-*.log to find the corresponding setup log.                                                                                                                                         

2025-05-22 00:42:31,418 INFO uri_cache.py:71 -- Marked URI pip://03b0b4b60765962f148fd91e395c8ad4f321e3bf used.                                                                    

2025-05-22 00:42:32,125 INFO uri_cache.py:84 -- Added URI gs://pixelbin-ml-worker-queue/ray-applications/RayApplicationsCI-deploy.ray.view-detection.v13.1746474693.zip with size 187817                                                                                                                                                                              

2025-05-22 00:42:32,126 INFO plugin.py:257 -- Runtime env pip pip://03b0b4b60765962f148fd91e395c8ad4f321e3bf is already installed and will be reused. Search all runtime_env_setup-*.log to find the corresponding setup log.                                                                                                                                         

2025-05-22 00:42:32,126 INFO uri_cache.py:71 -- Marked URI pip://03b0b4b60765962f148fd91e395c8ad4f321e3bf used.
```

### Expected Behavior
Pods should successfully schedule and maintain readiness/liveness for predictable API availability. Runtime environment creation should not block pod readiness.

### Actual Behavior
Pods remain unready with repeated runtime environment creation failures, leading to API-level outages.

### Additional Context
Please let us know if further logs, configs, or metrics would help in identifying the root issue.

---

/cc @ray-project/serve


### Versions / Dependencies

### Environment Details
- Ray version: 2.10.0
- Python Version: 3.11.8
- Deployment type: K8s
- Platform: GKE

### Reproduction script

We were not able to reproduce the issue reliably in lower environments or test clusters. The failure appears to be intermittent or environment-specific, possibly related to scale, network conditions, or RayServe's internal runtime environment management.

### Issue Severity

High: It blocks me from completing my task.

## 评论 (2)

### github-actions[bot] · 2026-09-22

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).

### x-itm · 2026-09-26

The repeated `runtime_env_agent_client.cc:369: Create runtime env for job 01000000` logs and the GCS health check failures (`/api/gcs_healthz`) strongly suggest a deadlock in the runtime environment setup process. This typically occurs when the Raylet cannot resolve or reuse the pip-based runtime environment (as seen in `runtime_env_setup-*.log`), likely due to a race condition or misconfigured cache persistence for GCS URIs (e.g., `gs://pixelbin-ml-worker-queue/`).

**Actionable steps to diagnose/resolve:**
1. **Verify Runtime Environment Reuse**: Ensure the `runtime_env` is explicitly marked as reusable in your RayServe deployment YAML (e.g., `runtime_env: { type: pip, pip:
