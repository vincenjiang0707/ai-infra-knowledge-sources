# [Issue #5611] [Issue]: Flash Attention -Triton / MI35X (1GPU) CI fails during building docker image

source: https://github.com/ROCm/aiter/issues/5611
state: open | updated: 2026-09-19T21:46:59Z
labels: 

## 正文

### Problem Description

## Summary

The **Flash Attention Integration** job **Flash Attention - Triton / MI35X (1 GPU)** failed at **Build Docker image (v2)** (~59s). The failure is a pip dependency resolution error: `flydsl==0.1.9.dev599` is not available on the index. No Flash Attention tests were run.

## Job

- **Workflow:** Flash Attention Integration
- **Job:** `Flash Attention - Triton / MI35X (1 GPU)`
- **Failed step:** `Build Docker image (v2)`
- **Note:** This is a Docker build / dependency install failure, not a kernel or accuracy failure.

## Error

```text
INFO: pip is looking at multiple versions of amd-aiter to determine which version is compatible with other requirements. This could take a while.
ERROR: Could not find a version that satisfies the requirement flydsl==0.1.9.dev599 (from versions: 0.0.1.dev951863, 0.1.1.dev409, 0.1.1.dev442, 0.1.1, 0.1.2, 0.1.3, 0.1.3.1, 0.1.4, 0.1.4.2, 0.1.5, 0.1.6, 0.1.7, 0.1.8, 0.2.0, 0.2.1, 0.2.2, 0.2.3, 0.2.4, 0.3.0, 0.3.1, 0.3.2.dev853, 0.3.2, 0.3.3.dev886, 0.3.3.dev889, 0.3.3.dev903)
ERROR: No matching distribution found for flydsl==0.1.9.dev599
```

## Context

CI builds `Dockerfile.triton` by cloning `Dao-AILab/flash-attention` (`FA_BRANCH=main`) and running:

```text
FLASH_ATTENTION_TRITON_AMD_ENABLE=TRUE pip install --no-build-isolation .
```

Flash Attention's `setup.py` installs its pinned AITER submodule. The log shows `amd-aiter==0.0.0` pulling `flydsl==0.1.9.dev599`. That version is not on the current index (no `0.1.9*`; available versions jump from `0.1.8` to `0.2.0`).

This happens **before** `COPY . /aiter` overrides with the PR AITER tree. AITER currently pins `flydsl==0.2.4`, so the stale FA submodule pin still blocks the image build.

## Impact

MI35X Triton Flash Attention integration cannot complete. The job never reaches test execution.

## Suggested next steps

1. Confirm whether FA `third_party/aiter` (or FA's own requirements) still pins `flydsl==0.1.9.dev599`.
2. Bump to a version that exists on the index (e.g. `0.2.4`, matching AITER) **or** install from the AMD extra index if that wheel is only published there.
3. Avoid installing FA's bundled AITER dependencies before overlaying the PR AITER checkout, so an outdated pin cannot fail the Docker build.

### Operating System

Ubuntu 24.04 LTS (inside CI Docker: rocm/pytorch:latest@sha256:683765a52c61341e1674fe730ab3be861a444a45a36c0a8caae7653a08a0e208; Python 3.12 venv at /opt/venv). Host is a GitHub Actions self-hosted runner (aiter-gfx1100).

### CPU

Unknown — not printed in the CI logs. Self-hosted GitHub Actions runner `aiter-gfx1100`.

### GPU

1 x AMD RDNA3 GPU (gfx1100), GitHub Actions runner `aiter-gfx1100` (job: Flash Attention - Triton / RDNA3 (1 GPU)).  The same flydsl pin failure also occurred on Flash Attention - Triton / MI35X (1 GPU) (`linux-aiter-mi35x-1`, AMD Instinct MI35X).

### ROCm Version

ROCm from the pinned `rocm/pytorch:latest` CI image (digest sha256:683765a52c61341e1674fe730ab3be861a444a45a36c0a8caae7653a08a0e208). Exact `rocminfo` version not printed because the job failed during Docker image build.

### Installation Method

Python wheels

### Installed ROCm Packages / Versions




### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of rocminfo --support

<details>
<summary>rocminfo --support output</summary>

```
Paste output here
```

</details>


### Additional Information

_No response_

## 评论 (3)

### gyohuangxin · 2026-09-17

@micmelesse The job failed because Flash Attention installed its pinned old third_party/aiter submodule before the PR AITER checkout was applied, and that old AITER version depends on unavailable flydsl==0.1.9.dev599. I opened a [PR](https://github.com/ROCm/aiter/pull/5620) to use the new AITER checkout when installing FA, but the AITER submodule in FA should also be updated regularly.

### micmelesse · 2026-09-19

I am working on a fix. Will post updates soon.

### micmelesse · 2026-09-19

I have a draft pr up at https://github.com/ROCm/aiter/pull/5687. I will update here when it is merged. 
