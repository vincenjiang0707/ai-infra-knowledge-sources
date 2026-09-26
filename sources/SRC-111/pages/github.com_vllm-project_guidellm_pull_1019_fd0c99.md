source: https://github.com/vllm-project/guidellm/pull/1019

# merge queue: checking main (d3a6da9) and #800 together - #1019

Closed

[mergify[bot]](https://github.com/mergify[bot])wants to merge 4 commits into

Closed

[mergify[bot]](https://github.com/mergify[bot]) wants to merge 4 commits into

[mergify[bot]](https://github.com/mergify[bot])wants to merge 4 commits into

## Conversation

Generated-by: Claude claude-opus-4-6 Signed-off-by: RheagalFire <arishalam121@gmail.com>

- Bump minimum litellm version to >=1.83.0 (post supply-chain fix) - Remove <1.87.0 upper bound to allow latest releases - Regenerate uv.lock via tox run -e lock - Fix ruff formatting issues Signed-off-by: Aarish Alam <arishalam121@gmail.com>

…, __all__ in stub Signed-off-by: Aarish Alam <arishalam121@gmail.com>

11 tasks

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

⏳ The pull request #800 is queued for merge and currently being checked. ⏳Branch

main(d3a6da9) and #800 are queued together for merge.This pull request has been created by Mergify to check the mergeability of #800.

You don't need to do anything. Mergify will close this pull request automatically when it is complete.

Required conditions of queue rule`default`

for merge:`Merge Requirements`

]:`check-neutral = @github-actions/quality (3.10) / precommit-checks`

`check-skipped = @github-actions/quality (3.10) / precommit-checks`

`check-success = @github-actions/quality (3.10) / precommit-checks`

`Merge Requirements`

]:`check-neutral = @github-actions/quality (3.10) / quality-checks`

`check-skipped = @github-actions/quality (3.10) / quality-checks`

`check-success = @github-actions/quality (3.10) / quality-checks`

`Merge Requirements`

]:`check-neutral = @github-actions/tests (3.10) / integration-tests`

`check-skipped = @github-actions/tests (3.10) / integration-tests`

`check-success = @github-actions/tests (3.10) / integration-tests`

`Merge Requirements`

]:`check-neutral = @github-actions/tests (3.10) / unit-tests`

`check-skipped = @github-actions/tests (3.10) / unit-tests`

`check-success = @github-actions/tests (3.10) / unit-tests`

`Merge Requirements`

]:`check-neutral = @github-actions/update-description`

`check-skipped = @github-actions/update-description`

`check-success = @github-actions/update-description`

`github-review-approved`

[🛡 GitHub repository ruleset rule`Merge Requirements`

]`Merge Requirements`

]:`check-success = @github-actions/quality (3.10) / type-checks`

`check-neutral = @github-actions/quality (3.10) / type-checks`

`check-skipped = @github-actions/quality (3.10) / type-checks`

`Merge Requirements`

]:`check-success = @github-actions/tests (3.10) / e2e-tests`

`check-neutral = @github-actions/tests (3.10) / e2e-tests`

`check-skipped = @github-actions/tests (3.10) / e2e-tests`

Required conditions to stay in the queue:`#approved-reviews-by >= 1`

`#changes-requested-reviews-by = 0`

`-closed`

`-draft`

`check-success = DCO`

`check-success = update-description`