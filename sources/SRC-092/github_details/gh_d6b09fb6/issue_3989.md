# [Issue #3989] [CI] cuda-toolkit network install flakes on NVIDIA apt mirror sync (ubuntu2404 Packages size mismatch)

source: https://github.com/kvcache-ai/Mooncake/issues/3989
state: open | updated: 2026-09-18T05:41:31Z
labels: 

## 正文

## Symptom
`test-wheel-ubuntu` (and other jobs using `Jimver/cuda-toolkit` with `method: network`) fail during **Install CUDA Toolkit** before any Mooncake tests run.

Seen on PR #3969 run https://github.com/kvcache-ai/Mooncake/actions/runs/34425688979/job/102715019979

## Log excerpt
```
E: Failed to fetch http://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86_64/Packages
File has unexpected size (1799720 != 1817210). Mirror sync in progress? [IP: …]
##[error]Error: The process '/usr/bin/sudo' failed with exit code 100
```
Also warns CUDA apt source is configured twice (`archive_uri-…noble.list` + `cuda-ubuntu2404-x86_64.list`).

## Context
- `ci.yml` pins `Jimver/cuda-toolkit@v0.2.24`
- `_build-efa-wheel.yaml` already uses `@v0.2.29`
- Failure is infra/mirror, not product code; CI Gate then fails because `test-wheel-ubuntu` failed

## Proposed fix (separate PR)
1. Retry the Install CUDA Toolkit step (2–3×) on apt size-mismatch / exit 100
2. Bump `Jimver/cuda-toolkit` in `ci.yml` toward the version already used by efa wheel (or newer), and avoid duplicate apt sources if still present
3. Optional: document that empty re-run is OK for this flake

Happy to send a small CI-only PR.

## 评论 (2)

### github-actions[bot] · 2026-09-10

Thanks for opening this issue, @quantz8a!

| Field | Value |
|-------|-------|
| **Issue** | #3989 |
| **GitHub user ID** | `3152505` |
| **Reporter** | @quantz8a |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.

### quantz8a · 2026-09-18

Opened https://github.com/kvcache-ai/Mooncake/pull/4216 with the proposed bump + one retry on 	est-wheel-ubuntu.
