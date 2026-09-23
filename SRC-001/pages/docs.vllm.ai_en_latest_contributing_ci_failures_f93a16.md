source: https://docs.vllm.ai/en/latest/contributing/ci/failures/
lastmod: 2026-09-23

# CI Failures[¶](https://docs.vllm.ai#ci-failures)

What should I do when a CI job fails on my PR, but I don't think my PR caused the failure?

-
Check the dashboard of current CI test failures:


👉[CI Failures Dashboard](https://github.com/orgs/vllm-project/projects/20) -
If your failure

**is already listed**, it's likely unrelated to your PR. Help fixing it is always welcome!- Leave comments with links to additional instances of the failure.
- React with a 👍 to signal how many are affected.

-
If your failure

**is not listed**, you should**file an issue**.

## Filing a CI Test Failure Issue[¶](https://docs.vllm.ai#filing-a-ci-test-failure-issue)

-
**File a bug report:**

👉[New CI Failure Report](https://github.com/vllm-project/vllm/issues/new?template=450-ci-failure.yml) -
**Use this title format:** -
**For the environment field:** -
**In the description, include failing tests:**[FAILED failing/test.py:failing_test1 - Failure description](https://docs.vllm.ai#__codelineno-2-1)[FAILED failing/test.py:failing_test2 - Failure description](https://docs.vllm.ai#__codelineno-2-2)[https://github.com/orgs/vllm-project/projects/20](https://docs.vllm.ai#__codelineno-2-3)[https://github.com/vllm-project/vllm/issues/new?template=400-bug-report.yml](https://docs.vllm.ai#__codelineno-2-4)[FAILED failing/test.py:failing_test3 - Failure description](https://docs.vllm.ai#__codelineno-2-5) -
**Attach logs**(collapsible section example):## Logs:

[ERROR 05-20 03:26:38 [dump_input.py:68] Dumping input data](https://docs.vllm.ai#__codelineno-3-1)[--- Logging error ---](https://docs.vllm.ai#__codelineno-3-2)[Traceback (most recent call last):](https://docs.vllm.ai#__codelineno-3-3)[File "/usr/local/lib/python3.12/dist-packages/vllm/v1/engine/core.py", line 203, in execute_model](https://docs.vllm.ai#__codelineno-3-4)[return self.model_executor.execute_model(scheduler_output)](https://docs.vllm.ai#__codelineno-3-5)[...](https://docs.vllm.ai#__codelineno-3-6)[FAILED failing/test.py:failing_test1 - Failure description](https://docs.vllm.ai#__codelineno-3-7)[FAILED failing/test.py:failing_test2 - Failure description](https://docs.vllm.ai#__codelineno-3-8)[FAILED failing/test.py:failing_test3 - Failure description](https://docs.vllm.ai#__codelineno-3-9)

## Logs Wrangling[¶](https://docs.vllm.ai#logs-wrangling)

Logs are public; no Buildkite login needed. [ .buildkite/scripts/ci-fetch-log.sh](https://github.com/vllm-project/vllm/blob/main/.buildkite/scripts/ci-fetch-log.sh) saves each log as `ci-<build>-<job-name>.log`

, stripped of timestamps and ANSI codes:

# All failed jobs in a PR's latest build (current branch's PR if omitted):
.buildkite/scripts/ci-fetch-log.sh --pr <PR>
# All failed jobs in a build (--soft also includes soft-failed jobs;
# --all fetches every finished job):
.buildkite/scripts/ci-fetch-log.sh "https://buildkite.com/vllm/ci/builds/<N>"
# One job — `gh pr checks` URLs (#<job_uuid>) and web UI URLs (?sid=) both
# work; pass "-" as a second argument to stream to stdout:
.buildkite/scripts/ci-fetch-log.sh "https://buildkite.com/vllm/ci/builds/<N>#<job_uuid>"


To clean an already-downloaded log:

[ .buildkite/scripts/ci-clean-log.sh](https://github.com/vllm-project/vllm/blob/main/.buildkite/scripts/ci-clean-log.sh)

Use a tool [wl-clipboard](https://github.com/bugaevc/wl-clipboard) for quick copy-pasting:

## Investigating a CI Test Failure[¶](https://docs.vllm.ai#investigating-a-ci-test-failure)

- Go to 👉
[Buildkite main branch](https://buildkite.com/vllm/ci/builds?branch=main) - Bisect to find the first build that shows the issue.
- Add your findings to the GitHub issue.
- If you find a strong candidate PR, mention it in the issue and ping contributors.

## Reproducing a Failure[¶](https://docs.vllm.ai#reproducing-a-failure)

CI test failures may be flaky. Use a bash loop to run repeatedly:

[ .buildkite/scripts/rerun-test.sh](https://github.com/vllm-project/vllm/blob/main/.buildkite/scripts/rerun-test.sh)

## Submitting a PR[¶](https://docs.vllm.ai#submitting-a-pr)

If you submit a PR to fix a CI failure:

- Link the PR to the issue: Add
`Closes #12345`

to the PR description. - Add the
`ci-failure`

label: This helps track it in the[CI Failures GitHub Project](https://github.com/orgs/vllm-project/projects/20).

## Other Resources[¶](https://docs.vllm.ai#other-resources)

## Daily Triage[¶](https://docs.vllm.ai#daily-triage)

Use [Buildkite analytics (2-day view)](https://buildkite.com/organizations/vllm/analytics/suites/ci-1/tests?branch=main&period=2days) to:

- Identify recent test failures
**on**.`main`

- Exclude legitimate test failures on PRs.
- (Optional) Ignore tests with 0% reliability.

Compare to the [ CI Failures Dashboard](https://github.com/orgs/vllm-project/projects/20).