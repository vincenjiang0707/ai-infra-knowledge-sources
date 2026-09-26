source: https://github.com/vllm-project/guidellm/pull/1140

# merge queue: checking #1115 on main (4cb753b) - #1140

Closed

[mergify[bot]](https://github.com/mergify[bot])wants to merge 11 commits into

Closed

[mergify[bot]](https://github.com/mergify[bot]) wants to merge 11 commits into

[mergify[bot]](https://github.com/mergify[bot])wants to merge 11 commits into

## Conversation

Assisted-by: OpenAI Codex Signed-off-by: Haozhe Jiang <162801044+provoke210@users.noreply.github.com>

Preserve upstream stderr redirection and require an explicit profile in console selection tests. Assisted-by: OpenAI Codex Signed-off-by: Haozhe Jiang <162801044+provoke210@users.noreply.github.com>

Use reference wording and remove the legacy progress alias mention as requested in review. Assisted-by: OpenAI Codex Signed-off-by: Haozhe Jiang <162801044+provoke210@users.noreply.github.com>

Add independent interval-limited INFO progress logging with queued-log cleanup and coverage for simultaneous Rich rendering, file logging, and disabled displays. Assisted-by: OpenAI Codex Signed-off-by: Haozhe Jiang <162801044+provoke210@users.noreply.github.com>

Enable interval-limited progress logging in the benchmark entrypoint alongside optional Rich output. Remove the opt-in console registry, simple display and logging CLI switch. Assisted-by: OpenAI Codex Signed-off-by: Haozhe Jiang <162801044+provoke210@users.noreply.github.com>

Make Benchmarker.run accept a list of progress observers. Separate logging from Rich rendering, await all callbacks before propagating failures, and finalize observers on exit. Assisted-by: OpenAI Codex Signed-off-by: Haozhe Jiang <162801044+provoke210@users.noreply.github.com>

Replace manual callback exception collection with TaskGroup lifecycle scopes. Preserve Python 3.10 support with the taskgroup backport and verify sibling cancellation and finalization. Assisted-by: OpenAI Codex Signed-off-by: Haozhe Jiang <162801044+provoke210@users.noreply.github.com>

Remove the outer try/finally as requested in review and update observer tests to expect initialization and scheduler failures to skip finalization. Assisted-by: OpenAI Codex Signed-off-by: Haozhe Jiang <162801044+provoke210@users.noreply.github.com>

Only release observer state during progress finalization, without calling the process-wide logger.complete method. Assisted-by: OpenAI Codex Signed-off-by: Haozhe Jiang <162801044+provoke210@users.noreply.github.com>

Revert only TaskGroup dispatch and its backport dependencies. Keep finalization on normal completion and leave process logger completion unchanged. Assisted-by: OpenAI Codex Signed-off-by: Haozhe Jiang <162801044+provoke210@users.noreply.github.com>

3 tasks

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

🎉 This pull request has been checked successfully and will be merged soon. 🎉#1115 is queued for merge on branch

main(4cb753b).This pull request has been created by Mergify to check the mergeability of #1115.

You don't need to do anything. Mergify will close this pull request automatically when it is complete.

Required conditions of queue rule`default`

for merge:`github-review-approved`

[🛡 GitHub repository ruleset rule`Merge Requirements`

]`Merge Requirements`

]:`check-success = @github-actions/quality (3.10) / type-checks`

`check-neutral = @github-actions/quality (3.10) / type-checks`

`check-skipped = @github-actions/quality (3.10) / type-checks`

`Merge Requirements`

]:`check-success = @github-actions/quality (3.10) / precommit-checks`

`check-neutral = @github-actions/quality (3.10) / precommit-checks`

`check-skipped = @github-actions/quality (3.10) / precommit-checks`

`Merge Requirements`

]:`check-success = @github-actions/quality (3.10) / quality-checks`

`check-neutral = @github-actions/quality (3.10) / quality-checks`

`check-skipped = @github-actions/quality (3.10) / quality-checks`

`Merge Requirements`

]:`check-success = @github-actions/tests (3.10) / e2e-tests`

`check-neutral = @github-actions/tests (3.10) / e2e-tests`

`check-skipped = @github-actions/tests (3.10) / e2e-tests`

`Merge Requirements`

]:`check-success = @github-actions/tests (3.10) / integration-tests`

`check-neutral = @github-actions/tests (3.10) / integration-tests`

`check-skipped = @github-actions/tests (3.10) / integration-tests`

`Merge Requirements`

]:`check-success = @github-actions/tests (3.10) / unit-tests`

`check-neutral = @github-actions/tests (3.10) / unit-tests`

`check-skipped = @github-actions/tests (3.10) / unit-tests`

`Merge Requirements`

]:`check-success = @github-actions/update-description`

`check-neutral = @github-actions/update-description`

`check-skipped = @github-actions/update-description`

Required conditions to stay in the queue:`#approved-reviews-by >= 1`

`#changes-requested-reviews-by = 0`

`-closed`

`-draft`

`check-success = DCO`

`check-success = update-description`