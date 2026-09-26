source: https://github.com/vllm-project/guidellm/pull/1102

# fix(metrics): preserve all cancellations in final scheduler counts - #1102

Open

[DivyamTalwar](https://github.com/DivyamTalwar)wants to merge 3 commits into

Open

[DivyamTalwar](https://github.com/DivyamTalwar) wants to merge 3 commits into

[DivyamTalwar](https://github.com/DivyamTalwar)wants to merge 3 commits into

## Conversation

Compile request outcome counts from the request accumulators so cancellations that never reached dispatch do not leak into report totals after a later terminal update. Generated-by: OpenAI Codex Signed-off-by: Divyam Talwar <divyamtalwar0@gmail.com>


**requested changes**

[sjmonson](https://github.com/sjmonson)Sep 8, 2026

[src/guidellm/benchmark/schemas/metrics.py](https://github.com/vllm-project/guidellm/pull/1102/files/7c2d3ed629b79ad3cb1e23d6f772ab2b45521525#diff-afc9e694b983a862e3aa3613a213c97508b3fd79ddc5280fa110f304b56f4672)

Address PR[vllm-project#1102]review feedback: scheduler requests_made includes every cancellation, with the shared incomplete field representing cancelled. Filtered measurement-window counts remain in metrics.request_totals. Compile scheduler outcomes from the final SchedulerState. The cached accumulator can be stale when the last event is a queued cancellation, because that event returns before updating scheduler metric counts. Document the distinction without changing the serialized field names. Regression evidence: restoring the original cached-count implementation produced 5 failures (four trailing-cancellation permutations and the all-queued-cancelled case). The corrected path passes all permutations of queued cancellation, started cancellation, and completion/error. Validation: - tox focused benchmark and worker checks: 153 passed, 12 deselected. - tox lint-check and type-check: passed (222 source files). - Broader benchmark/scheduler run: 700 passed, 16 xfailed, 5 failed. The five failures occur at multiprocessing.Manager startup in this sandbox. A representative case also fails with the original metrics implementation: PermissionError creating a socket, followed by EOFError. - git diff --check: passed. Generated-by: OpenAI Codex Signed-off-by: Divyam Talwar <divyamtalwar0@gmail.com>


[DivyamTalwar](https://github.com/DivyamTalwar)changed the title

Sep 8, 2026

9 tasks

### This branch has not been deployed

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

Scheduler request counts must include all cancellations, including requests cancelled before dispatch. The

`incomplete`

field represents cancelled requests because the scheduler reuses`StatusBreakdown`

; filtered benchmark totals belong in`metrics.request_totals`

.This revision addresses the review by preserving those semantics and fixing the remaining event-order bug: a queued cancellation returns before updating the cached scheduler metrics, so a final queued cancellation can be missing from the exported scheduler counts. Compile those counts from the final

`SchedulerState`

, and document the distinction between scheduler outcomes and filtered measurement-window totals.## Review follow-up

The original change incorrectly derived scheduler counts from the filtered request accumulators. That implementation has been replaced in commit

`db6ec4ee7d7b78ed7f1029c5977f2cd17492b842`

. Serialized field names remain compatible.## Validation

`uv run --frozen tox -e tests -- tests/unit/benchmark tests/unit/scheduler/test_worker.py -k 'not run_async_lifecycle and not run_with_timings' --tb=short`

: 153 passed, 12 deselected.`uv run --frozen tox -e lint-check,type-check`

: passed; mypy checked 222 source files.`multiprocessing.Manager`

startup. A representative failure was reproduced with the original metrics implementation: the sandbox rejects socket creation with`PermissionError`

, followed by`EOFError`

. This is not a clean full-suite result.`git diff --check`

: passed.## Use of AI

Implementation, tests, and documentation were assisted by OpenAI Codex and remain subject to maintainer review. The follow-up commit includes

`Generated-by: OpenAI Codex`

and the author's sign-off.## git log

commit

7c2d3edAuthor: Divyam Talwar divyamtalwar0@gmail.com

Date: Tue Sep 8 14:35:51 2026 +0530

commit

db6ec4eAuthor: Divyam Talwar divyamtalwar0@gmail.com

Date: Wed Sep 9 03:02:43 2026 +0530

Signed-off-by: Divyam Talwar divyamtalwar0@gmail.com