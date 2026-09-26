source: https://github.com/vllm-project/guidellm/pull/974

# Make plot path behave like others - #974

Merged

Merged

## Conversation

The PLOT output PR was handled in parallel with the addition of `GUIDELLM__DEFAULT_RESULTS_DIR` and didn't get that change. I'm really tempted to take this further and merge basedir + name + suffix intelligently; but for now I'll settle for bringing this up to par with the others. Signed-off-by: David Butenhof <dbutenho@redhat.com>


[dbutenhof](https://github.com/dbutenhof)added

[bug](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Abug)

[escape](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Aescape)

Jul 29, 2026


**approved these changes**

[sjmonson](https://github.com/sjmonson)Jul 30, 2026

Contributor

|
Queued — the merge queue status continues in |


**approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Jul 30, 2026

Contributor

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

35 tasks

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

The PLOT output kind path default doesn't use "default results dir".

## Details

The timing of merges meant that the PLOT output path missed the introduction of

`GUIDELLM__DEFAULT_RESULTS_DIR`

.(I'm really tempted to take this further and merge basedir + name + suffix intelligently; but for now I'll settle for bringing this up to par with the others.)

## Test Plan

`GUIDELLM__DEFAULT_RESULTS_DIR=/tmp guidellm export --output kind=plot`

should write`/tmp/benchmarks.png`

## Related Issues

N/A

## Use of AI

## git log

commit

04e693bAuthor: David Butenhof dbutenho@redhat.com

Date: Wed Jul 29 16:26:49 2026 -0400

Signed-off-by: David Butenhof dbutenho@redhat.com