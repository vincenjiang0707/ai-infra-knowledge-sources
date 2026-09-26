source: https://github.com/vllm-project/guidellm/pull/1146

# merge queue: checking #1142 on main (2c0bb2b) - #1146

Closed

[mergify[bot]](https://github.com/mergify[bot])wants to merge 2 commits into

Closed

[mergify[bot]](https://github.com/mergify[bot]) wants to merge 2 commits into

[mergify[bot]](https://github.com/mergify[bot])wants to merge 2 commits into

## Conversation

`generic_error_handler` logged unhandled exceptions with `logger.error("Unhandled exception: {}", exception)`. The `logger` is a stdlib `logging.Logger`, which expects `%s`-style placeholders, not `{}`. Every unhandled exception therefore raised a secondary `TypeError` from inside the logging module itself, burying the real traceback under logging-internals noise. Change `{}` to `%s` so the exception logs cleanly. Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com> Generated-by: Claude Sonnet 5 Signed-off-by: Tayo Ogunbiyi <eyitayoogunbiyi@gmail.com>

5 tasks

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

🎉 This pull request has been checked successfully and will be merged soon. 🎉#1142 is queued for merge on branch

main(2c0bb2b).This pull request has been created by Mergify to check the mergeability of #1142.

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