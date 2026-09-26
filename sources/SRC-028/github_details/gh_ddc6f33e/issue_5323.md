# [Issue #5323] Failed build: MaxText Package Tests

source: https://github.com/AI-Hypercomputer/maxtext/issues/5323
state: closed | updated: 2026-09-21T22:25:28Z
labels: build failed

## 正文

GitHub Actions workflow [MaxText Package Tests #8016](https://github.com/AI-Hypercomputer/maxtext/actions/runs/35648822353) failed.

Event: schedule
Branch: [main](https://github.com/AI-Hypercomputer/maxtext/tree/main)
Commit: [aae9791eb8770f1355f11460514353a576ba134a](https://github.com/AI-Hypercomputer/maxtext/commit/aae9791eb8770f1355f11460514353a576ba134a)

<sup><i>Created by [jayqi/failed-build-issue-action](https://github.com/jayqi/failed-build-issue-action)</i></sup>

## 评论 (2)

### github-actions[bot] · 2026-09-21

### 🤖 CI Failure Investigation Report

I have analyzed the recent test failures in the CI pipeline and identified the following:

#### 🔍 What Failed
* **Job/Matrix**: `TPU Pretrain Tests (tpu-integration) / Execute Tests (1) / tpu-integration`
* **Failing Test**: Container Startup (Infrastructure Setup Phase)
* **Error**: `Error: 14 UNAVAILABLE: Name resolution failed for target dns:...`

#### 🪵 Error Details & Stack Trace
```python
Error: 14 UNAVAILABLE: Name resolution failed for target dns:linux-x86-ct6e-180-4tpu-vshv2-runner-cd8q2-service:50051
Executing the custom container implementation failed. Please contact your self hosted runner administrator.
Error: backoff timeout
```

#### 💡 Root Cause Analysis & Context
**Confidence:** high (Confirmed Cause)

The failure is an **infrastructure/environment flake** and is **not a codebase regression**. 

The runner encountered a gRPC `14 UNAVAILABLE` Name Resolution Failure when attempting to connect to its helper service container (`linux-x86-ct6e-180-4tpu-vshv2-runner-cd8q2-service:50051`) on the self-hosted TPU node. This DNS lookup failure caused the GitHub Actions runner to timeout (`Error: backoff timeout`) and fail to spin up the Docker container for the test execution stage:
`Executing the custom container implementation failed. Please contact your self hosted runner administrator.`

Because the container failed to launch during the setup phase, no codebase test files or python code were executed. This is a transient network/DNS resolution issue on the self-hosted TPU runner cluster.

#### 🛠️ Recommended Action
No recommended code fix is needed as this is a transient infrastructure issue. A retry of the workflow run or a transient failure recovery on the self-hosted runner cluster will resolve this issue.

### Shuwen-Fang · 2026-09-21

reran workflow and passed:  https://github.com/AI-Hypercomputer/maxtext/actions/runs/35648822353?attempt=2 failure was transient
