# [Issue #3861] CI: gate nightly vLLM before using it as the LMCache test baseline

source: https://github.com/LMCache/LMCache/issues/3861
state: closed | updated: 2026-09-27T01:56:39Z
labels: Testing, stale, ci/cd, RFC, vllm, mp_mode

## 正文

## Background

Our CI integration tests against vLLM use the `nightly` build of vLLM.
The problem is that vLLM nightly is not always healthy: sometimes it has bugs, sometimes it breaks compatibility with LMCache. When that happens, every LMCache PR running CI on top of that broken nightly will fail, even though the LMCache change itself is fine.

We need a way to figure out, every day, whether today's vLLM nightly actually works with LMCache. Only the versions that pass should be used as the baseline for LMCache CI.

## Proposal

Add a small "gate" job that runs once a day. It picks the latest vLLM nightly, runs a minimum set of LMCache + vLLM e2e tests, and if those pass, it records this nightly version as a "known good" version. Other
CI jobs then use this known good version instead of always grabbing the freshest (possibly broken) one.

If the gate fails, we don't update the known good version, and we open or update a sticky issue so people know nightly is broken today.

## Scope for this first iteration

- Focus on **MP (multi-process) mode** of LMCache + vLLM. 
- Run on **GPU** (we will add CPU coverage in a later PR, so the workflow should be easy to extend).
- Use a small model so the run stays cheap. Plan: `Qwen2.5-0.5B-Instruct`.
- Cadence: **daily** for the basic gate; once per week we additionally run a heavier MP smoke to catch regressions the small daily run might miss.
- On failure: open / update a **sticky GitHub issue** (no email / Slack  for now, can add later).

## How it fits together

1. **GitHub Actions** workflow (`.github/workflows/nightly-vllm-gate.yml`)
   runs on a daily cron. It triggers a Buildkite build on a dedicated
   pipeline using the `BUILD_KITE_API_TOKEN` repo secret.
2. **Buildkite pipeline** `lmcache-nightly-gate` loads
   `.buildkite/k3_tests/multiprocess/nightly-gate-pipeline.yml`, which
   installs the latest vLLM nightly, runs the MP e2e check
   (`run_nightly_gate.sh`), and on success writes the nightly version
   string to an artifact (`nightly-vllm-good.txt`).
3. The GitHub Actions job downloads that artifact. On success it
   commits/updates a `nightly-vllm-good.txt` file (or pins it as a repo
   variable) that other CI jobs can read to decide which vLLM nightly
   to install. On failure it opens / updates a sticky issue with the
   failing version + log link.

## Why this design

- Keeps the actual GPU run inside Buildkite where the agents are, so we
  don't need GPU runners on GitHub Actions side.
- Keeps the scheduling / issue-management on GitHub Actions side, which
  is the natural place for cron + issue API.
- The pipeline file lives in the repo (not in Buildkite UI), so changes
  go through PR review.
- The gate is opt-in for other jobs: nothing breaks if we turn the gate
  off; jobs simply fall back to "latest nightly" as today.

## Out of scope (follow-ups)

- CPU gate (planned next PR).
- In-process `LMCacheConnectorV1` gate.

Happy to take feedback on the scope and the small-model choice before
the PR lands.


## Related PRs
- https://github.com/LMCache/LMCache/pull/3920/
- https://github.com/LMCache/LMCache/pull/3910
- https://github.com/LMCache/LMCache/blob/buildkite_latest_tested_vllm/latest_tested_vllm.txt

## 评论 (4)

### maobaolong · 2026-06-24

@ApostaC What do you think of this proposal? If this looks good to you, I'd like you to help me create a BuildKite pipeline. 

The creation process is outlined below (my account doesn't have the necessary permissions).

```shell
export ORG_SLUG="lmcache"
export REPO_URL="git@github.com:LMCache/LMCache.git"
export CLUSTER_ID="6c0dcbe3-fd42-4c65-94b1-a43dcc93441d"
export  BK_TOKEN="bkua_<YOUR_BUILD_KITE_API_TOKEN>"
curl -sS -X POST \
  -H "Authorization: Bearer ${BK_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "lmcache-nightly-gate",
    "repository": "'"${REPO_URL}"'",
    "default_branch": "dev",
    "cluster_id": "'"${CLUSTER_ID}"'",
    "skip_intermediate_builds": false,
    "provider_settings": {"trigger_mode": "none"},
    "steps": [{
      "type": "script",
      "name": ":pipeline: load gate",
      "command": "buildkite-agent pipeline upload .buildkite/k3_tests/multiprocess/nightly-gate-pipeline.yml",
      "agent_query_rules": ["queue=k8s"]
    }]
  }' \
  "https://api.buildkite.com/v2/organizations/${ORG_SLUG}/pipelines"

{"message":"Validation Failed","errors":[{"field":"cluster_id","code":"User not authorized to add this pipeline to cluster","value":"6c0dcbe3-fd42-4c65-94b1-a43dcc93441d"}]}
```

### ApostaC · 2026-06-25

A potential simpler solution: we use the vllm latest stable (instead of nightly) in the e2e tests

The code that installs vllm in each test is here: https://github.com/LMCache/LMCache/blob/5836a3e2254287c23f3a96c6529523adcc483ffa/.buildkite/k3_harness/setup-env.sh#L51-L59

### github-actions[bot] · 2026-08-27

This issue has been automatically marked as stale because it has not had activity within 60 days. It will be automatically closed if no further activity occurs within 30 days.

### github-actions[bot] · 2026-09-27

This issue has been automatically closed due to inactivity. Please feel free to reopen if you feel it is still relevant!
