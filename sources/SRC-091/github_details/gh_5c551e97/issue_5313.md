# [Issue #5313] [good-first-issue] tests: stabilize flaky CI tests from recent PRs

source: https://github.com/LMCache/LMCache/issues/5313
state: open | updated: 2026-09-24T05:26:55Z
labels: good first issue, help wanted, Testing, onboarding-2026

## 正文

Part of #3372. This is a community tracker for small, independently claimable improvements to flaky tests.

## The problem

Recent PR CI contains assertions that race background work and an intermittent hang that can occupy a runner for almost six hours. These failures consume contributor time and make unrelated PRs harder to validate.

The initial triage reviewed GitHub Actions `Test` runs from September 13-23, 2026 and recent `k3-unit-tests` failures. These are selected examples, not a complete inventory or a measured repository-wide flake rate. The test code was checked against `dev` at [21571dae80c6](https://github.com/LMCache/LMCache/commit/21571dae80c64ab4d141be571744494995270160).

The initial tasks cover:

- **Health-monitor exit:** a fixed 200 ms sleep precedes a thread-exit assertion; two PRs have same-checkout failed/passed attempts.
- **Health-monitor fallback/recovery:** a fixed 200 ms sleep precedes a state assertion; failure logs show fallback completing after the assertion.
- **RESP wait diagnostics:** a same-checkout rerun passes after an almost-six-hour hang near the RESP test boundary. The exact blocked operation remains unproven; this task adds bounded waits and diagnostics, not a speculative production fix.

## Initial tasks

- [ ] #5314: Synchronize health-monitor exception-driven exit
- [ ] #5315: Synchronize health-monitor fallback/recovery phases
- [ ] #5316: Bound RESP waits and add stalled-operation diagnostics

## Claim one sub-issue

Use the native **Sub-issues** list below. Start with either health-monitor task if this is your first test contribution; the RESP task benefits from familiarity with Python futures and event loops.

These tasks are primarily meant to help new contributors learn the LMCache contribution workflow. Please claim **only one sub-issue at a time**. If you already have an assigned task or an open PR in this tracker, finish that one before taking another, and leave the remaining tasks for other new contributors.

1. Pick one unassigned sub-issue and check its comments for an existing claim.
2. Comment `/claim` or "I'd like to work on this" **on that sub-issue**, so a maintainer can coordinate assignment. Please do not claim the parent tracker itself.
3. Keep one task per PR, target `dev`, and follow [the onboarding guide](https://github.com/LMCache/LMCache/issues/3372) and [CONTRIBUTING.md](https://github.com/LMCache/LMCache/blob/dev/CONTRIBUTING.md).
4. Sign off every commit (`git commit -s`), run `pre-commit run --all-files`, and include exact test commands and results in the PR.

## Shared CPU test setup

These tasks do not require a GPU, model download, or external Redis server. Use Linux x86_64 with Git, a C/C++ build toolchain, FFmpeg, and Python 3.12 with venv support. The RESP tests use an in-memory mocked client. Allow sufficient disk space for PyTorch/vLLM dependencies. The full pre-commit checks also need Rust/Cargo with rustfmt and clippy.

Run this in a fresh working directory. The explicit revision is the **triage reference**; make the actual PR against current `dev`.

```bash
git clone https://github.com/LMCache/LMCache.git
cd LMCache
git checkout 21571dae80c64ab4d141be571744494995270160
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install 'vllm==0.30.0' 'torch==2.13.0'
python -m pip install -r requirements/build.txt -r requirements/test.txt -r requirements/common.txt
NO_GPU_EXT=1 python -m pip install -e . --no-build-isolation
python -m pip install pre-commit
export PYTHONHASHSEED=0
python -m pip freeze > ci-repro-requirements.txt
```

This follows the dependency/build approach of the [CPU workflow](https://github.com/LMCache/LMCache/blob/21571dae80c64ab4d141be571744494995270160/.github/workflows/test.yml#L102), with explicit build requirements and runtime versions. It is a starting environment, not a fully locked historical environment or a claim of local reproduction. September 16-17 evidence used vLLM 0.29.0 and torch 2.13.0; September 22 evidence used vLLM 0.30.0 and torch 2.13.0. Use a fresh venv with the relevant Python/vLLM version when investigating historical runs, and record `pip freeze` and the actual checkout SHA.

Each child supplies focused commands. To check the surrounding CPU suite after the targeted change:

```bash
python -m pytest -m 'not (cuda or musa or xpu or npu or neuron)'
pre-commit run --all-files
```

Passing once does not establish that a timing race is fixed. Add a controlled scheduling/delay regression case, repeat the relevant test, and report the repetition count. Preserve the behavior assertions; blanket retries, larger fixed sleeps, and removing assertions do not establish synchronization.

## Related work already in progress

Coordinate with existing authors instead of opening duplicate fixes:

- #5135 / #5136: distributed-storage tests observe L2 visibility before L1 locks are released.
- #4566 / #4568 / #4707: `extra_stats` throughput tests mix synthetic timestamps with the real pruning clock.
- #4944: MQ test port isolation. A shutdown symptom also appeared during triage, but was not promoted to a new beginner task without stronger isolation from ongoing MQ work.
- #4489: executor shutdown/deadlock report, relevant to the RESP investigation.
- #5227: merged benchmark retries mitigate disruption; retries alone do not prove the underlying instability is resolved.

Missing generated protobuf modules, stale imports/API expectations, dependency incompatibilities, and cancelled superseded runs were not classified as flakes just because CI was red.

## Completion

Close this tracker when the initial child tasks are merged and their validation evidence is linked. For the diagnostic task, distinguish completed test hardening from any remaining production root-cause investigation.


## 评论 (5)

### VinsmokeSanji33 · 2026-09-23

/claim


### Zhou-Kan · 2026-09-24

Could I work on this ticket? @maobaolong 

### maobaolong · 2026-09-24

@Zhou-Kan Yeah you can claim a sub task.

### maobaolong · 2026-09-24

@VinsmokeSanji33 Thanks for interested in this issue, but this is an umbrella issue, you can claim a sub issue.

### maobaolong · 2026-09-24

Thanks for the interest here! A quick coordination note: please claim a specific child issue from the Sub-issues list rather than the parent tracker, and please take only one sub-issue at a time. These good-first tasks are mainly meant to help new contributors go through the LMCache issue-to-PR workflow, so we want to leave the remaining tasks open for other newcomers.
