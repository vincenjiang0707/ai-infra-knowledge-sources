# [Issue #1890] [CI] Four verified workflow config bugs: pr-gates miss the reusable runner, dead uv.lock change detection, push-event lanes silently skipped, shared non-PR concurrency group

source: https://github.com/NVIDIA/Model-Optimizer/issues/1890
state: closed | updated: 2026-07-05T12:04:46Z
labels: improvement, ci/cd

## 正文

## Describe the bug

Four verified defects in the CI workflow configs. Impact: should have — none block development, but two cause silent test-coverage gaps on merges and one fails a scheduled job. Found while auditing the workflows; each is confirmed either from this repo's own run history (via the GitHub API) or by reproducing the workflow steps locally. Sending one surgical PR per item.

**1. example_tests / gpu_tests pr-gate does not watch the reusable runner or the cache action.**
`example_tests.yml`'s pr-gate `files:` list includes `example_tests.yml` itself but not `.github/workflows/_example_tests_runner.yml` (the reusable workflow every example-test job executes through) or `.github/actions/cache-extensions/**` (used by the runner and by `gpu_tests.yml`). Reusable workflows run from the PR's ref, so a PR that changes only the runner merges with the very jobs it rewires never executed. Observed on PR #1651 (touched `_example_tests_runner.yml` + `cache-extensions/action.yml` + `gpu_tests.yml`): its example-tests run shows pr-gate success, then torch/trtllm-pr/megatron/onnx all skipped, and the required check green.

**2. bump_uv_lock.yml change detection is dead code; a no-update week fails the scheduled run.**
The torch-override step rewrites `pyproject.toml` with `toml.load`/`toml.dump`, which drops comments and reformats the whole file, so the later unscoped `git diff --quiet` is always dirty and `changed=false` is unreachable. When `uv lock --upgrade` changes nothing, the create-pull-request step stages nothing (`git add uv.lock`) and `git commit` exits 1 under `bash -e`, failing the run instead of no-oping. Reproduced locally by executing the workflow's steps against this repo's files: post-mutation `git diff --quiet` reports dirty with `uv.lock` byte-identical, and the commit step exits 1. Latent so far only because the lock has had upgrades every week.

**3. unit_tests.yml: on push events the file-change check outputs empty, silently skipping six lanes.**
In `check-file-changes`, the `non-pr` step runs only for `schedule`/`workflow_dispatch` and the `changed` step only for `pull_request`. For `push` neither runs, `any_changed` is empty, and the windows, multi-version, partial-install, launcher, mcp, and skills lanes all skip — despite the workflow-level push `paths:` filter listing `tools/launcher/**`, `tools/mcp/**`, `.agents/skills/**`, etc. Observed on the latest push run on main: check-file-changes success, linux success, all other lanes skipped. A push to main touching only `tools/launcher/**` runs the irrelevant modelopt suite and skips the launcher tests; `release/*`/`feature/*` branches get no coverage of these lanes at all (nightly only covers main).

**4. code_quality.yml: non-PR runs share one concurrency group and cancel each other.**
The group is `${{ github.workflow }}-${{ github.event.pull_request.number }}` with no `|| github.sha` fallback (unlike `unit_tests.yml`), so every nightly and manual dispatch shares the literal group `Code Quality-` with `cancel-in-progress: true` — a manual dispatch cancels an in-flight nightly and vice versa.

### Steps/Code to reproduce bug

- Item 1: compare `example_tests.yml` pr-gate `files:` with the `uses: ./.github/workflows/_example_tests_runner.yml` job wiring; see PR #1651's example-tests run for the observed skip.
- Item 2: run the workflow's steps locally in a clean checkout: apply the toml override snippet, then `git diff --quiet; echo $?` → 1 with `uv.lock` unchanged; `git add uv.lock && git commit -s -m x` → exit 1.
- Item 3: inspect any push-event run of Unit tests on main: `check-file-changes` succeeds with empty output and the gated lanes report skipped.
- Item 4: trigger workflow_dispatch of Code Quality while a nightly is in flight.

### Expected behavior

1. Changes to the test runner/cache action execute the example/GPU test jobs on the PR that changes them.
2. A no-update week no-ops (`changed=false`) instead of failing.
3. Push events run the lanes whose paths triggered the workflow.
4. Nightly and manual code-quality runs do not cancel each other.

### Who can help?

@kevalmorabia97

## System information

- Container used (if applicable): N/A (CI workflow configs)
- OS: N/A — reproductions done on Windows 11 (git steps) and via GitHub API run history
- CPU architecture / GPU: N/A
- Library versions: ModelOpt commit 4b9225bee (current main)
- Any other details that may help: sending four surgical PRs, one per item, referencing this issue

## 评论 (2)

### h-guo18 · 2026-07-05

Hi @kevalmorabia97 , seems like these bugs and PRs are related to CI/setup, could you take a look please. Thanks!

### kevalmorabia97 · 2026-07-05

Thanks for contributing these improvements. Related PRs merged
