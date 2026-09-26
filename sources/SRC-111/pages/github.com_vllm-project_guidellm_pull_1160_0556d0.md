source: https://github.com/vllm-project/guidellm/pull/1160

# merge queue: checking #1086 on main (118c87a) - #1160

Closed

[mergify[bot]](https://github.com/mergify[bot])wants to merge 2 commits into

Closed

[mergify[bot]](https://github.com/mergify[bot]) wants to merge 2 commits into

[mergify[bot]](https://github.com/mergify[bot])wants to merge 2 commits into

## Conversation

Declaring objectives answers whether one load level meets them. This adds a profile that searches for the highest level that does, which is the capacity-planning question behind issue[#197]. The search doubles concurrency until a level misses the target attainment, then bisects between the highest passing and lowest failing level, stopping once the answer is known to within a relative tolerance. Bisecting to an exact integer would cost a probe per halving regardless of scale. Concurrency is the control variable rather than request rate because every concurrency level settles into a steady state, whereas a rate above what the server sustains grows an unbounded backlog and measurements taken there describe the backlog rather than the server. Each level is judged on attainment rather than on the goodput rate. Attainment is a ratio over the requests measured, so it does not vary with how much of the measurement window the server spent filling its pipeline. Each probe's attainment carries a Wilson score interval. When that interval straddles the target the probe was too short to decide, and the search reports that rather than a number that looks precise. A descent that reaches a single stream on such probes is reported as indeterminate rather than as objectives that cannot be met. A probe stopped mid-run by a constraint is recorded but never becomes a search bound, since the cancelled requests it excludes can leave the completed remainder looking conforming. Two generic hooks carry this without profile-specific code in shared paths. Profiles may publish what they concluded once every strategy has run, which the report collects into a conclusions list so a run using several profiles keeps them separate. Each benchmark's config is captured before that benchmark executes, so it can never hold the final probe; reading the conclusion after the run is the only point at which the answer exists. Profile arguments may also reject a metrics configuration they cannot work with, which lets the goodput search require latency objectives at validation rather than after its first probe has run. Assisted-by: Claude Code claude-opus-5 Signed-off-by: QHarshil <harshil_c@hotmail.com>

11 tasks

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

🎉 This pull request has been checked successfully and will be merged soon. 🎉#1086 is queued for merge on branch

main(118c87a).This pull request has been created by Mergify to check the mergeability of #1086.

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