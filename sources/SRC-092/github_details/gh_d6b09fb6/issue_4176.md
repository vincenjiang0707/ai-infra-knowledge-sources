# [Issue #4176] [RFC]: Separate TONE and ROCm E2E platform lifecycles

source: https://github.com/kvcache-ai/Mooncake/issues/4176
state: open | updated: 2026-09-17T07:45:57Z
labels: 

## 正文

## Motivation

TONE CUDA/ERDMA and self-hosted ROCm/RoCE currently share a controller and a large platform-dispatching `common.sh`. Their different device isolation, driver installation, process tracking and teardown policies make lifecycle changes difficult to review independently.

## Proposal

- Preserve the TONE entry under `scripts/tone_tests/` and introduce `scripts/rocm_tests/` with independent platform lifecycle implementations and test inventories.
- Keep reusable cases, assets, Python helpers and orchestration under `scripts/e2e/`, rather than duplicating two suites.
- Explicitly reference shared files through `E2E_DIR`; do not use symlinks. Mount platform directories at `/test_run` and shared sources read-only at `/test_run/e2e` on both nodes. Copy platform and shared directories with ordinary `rsync -a`.
- Refresh generated environment/wheels on setup and isolate each case in a subshell to prevent configuration/function leakage.
- Preserve ROCm allocation-scoped devices, pinned SSH, runtime caches, reset/postflight checks and stop-on-unhealthy-environment behavior.
- Update workflow paths, release wheel verification, ownership, labels and focused regression tests.

TONE uses the full inventory; ROCm uses the existing core-4gpu inventory. Running a suite requires a complete repository checkout, not a standalone copy of its directory.

## Alternatives and scope

Duplicating all test scripts would remove cross-platform branches but create two independently drifting test implementations. Keeping the current monolithic lifecycle retains the review and maintenance problem. This proposal splits platform policy while sharing test logic.

Related #4175 only extracts PR/nightly composite actions and explicitly excludes this E2E split. #3600 adds a parallel TENT TONE job and touches some of the same scripts; it will need coordination, but this proposal does not add TENT execution or alter its runtime. #3970 changes the release wheel build backend, not E2E lifecycle policy.

## Validation / rollout

CPU-only cleanup regression tests, six Python unit tests, shell syntax checks and PR-scoped prek hooks pass. Tests cover platform separation, explicit helper loading, no suite symlinks, remote preparation with environment round-tripping and per-case isolation. Actual two-node TONE/ROCm E2E validation and human line-by-line review remain outstanding; the implementation PR will be a draft until reviewed.

## AI assistance

Prepared with an OpenAI coding assistant in pi. Human technical review and end-to-end sign-off are pending.

## Revision after review

Removed the initial symlink implementation in favor of explicit shared paths. The PR now changes 29 files (+2,326 / -2,158), compared with 47 files (+3,277 / -3,083) in the initial version. Much of the displayed reduction comes from recognizing the test scripts as renames.


## 评论 (1)

### github-actions[bot] · 2026-09-17

Thanks for opening this issue, @Aionw!

| Field | Value |
|-------|-------|
| **Issue** | #4176 |
| **GitHub user ID** | `41376987` |
| **Reporter** | @Aionw |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.
