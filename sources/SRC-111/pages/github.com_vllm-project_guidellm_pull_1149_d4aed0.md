source: https://github.com/vllm-project/guidellm/pull/1149

# Add Request Totals to Console output & Clear progress at the end of the benchmark - #1149

Merged

[mergify[bot]](https://github.com/mergify[bot])merged 5 commits into

Merged

## Conversation

Generated-by: Cursor Signed-off-by: Samuel Monson <smonson@redhat.com>

There is a race condition between when the live updates end and when the stderr/stdout redirection is removed. Setting the live display as "transient" ensures that we never hit this race condition. The numbers on the live display are an approximation over the last x amount of data so clearing it also helps avoid people looking at it for final status. Signed-off-by: Samuel Monson <smonson@redhat.com>

The new logger progress kinda makes this log redundent. Keeping the start logger because that is called pre-start while the logger progress one is called after the benchmark has "started". Signed-off-by: Samuel Monson <smonson@redhat.com>

Contributor

|
Queued — the merge queue status continues in |

E2E logs are expensive to run, lets avoid running tests for random pieces of the tool that don't matter a lot. Signed-off-by: Samuel Monson <smonson@redhat.com>

For testing purposes let the "transient" state be configurable at creation time. Signed-off-by: Samuel Monson <smonson@redhat.com>


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Sep 15, 2026


**approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Sep 15, 2026

Contributor

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

35 tasks

[PatilHrushikesh](https://github.com/PatilHrushikesh)pushed a commit to PatilHrushikesh/guidellm that referenced this pull request

Sep 21, 2026

…he benchmark ([vllm-project#1149]) ## Summary This could be separate PRs but each change is so small that its not really worth it. See commit messages for details. --- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [x] Includes code generated or substantially modified by an AI agent - [x] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- # git log commit[Author: Samuel Monson <smonson@redhat.com> Date: Tue Sep 15 18:52:24 2026 +0000 Add request counts to the console summary Generated-by: Cursor Signed-off-by: Samuel Monson <smonson@redhat.com> commit]afaafb1[Author: Samuel Monson <smonson@redhat.com> Date: Tue Sep 15 15:21:57 2026 -0400 Clear live display when benchmark ends There is a race condition between when the live updates end and when the stderr/stdout redirection is removed. Setting the live display as "transient" ensures that we never hit this race condition. The numbers on the live display are an approximation over the last x amount of data so clearing it also helps avoid people looking at it for final status. Signed-off-by: Samuel Monson <smonson@redhat.com> commit]db4a0e3[Author: Samuel Monson <smonson@redhat.com> Date: Tue Sep 15 15:52:57 2026 -0400 Remove benchmark complete log message The new logger progress kinda makes this log redundent. Keeping the start logger because that is called pre-start while the logger progress one is called after the benchmark has "started". Signed-off-by: Samuel Monson <smonson@redhat.com> commit]1b41bd8[Author: Samuel Monson <smonson@redhat.com> Date: Tue Sep 15 16:34:32 2026 -0400 Drop e2e logging test E2E logs are expensive to run, lets avoid running tests for random pieces of the tool that don't matter a lot. Signed-off-by: Samuel Monson <smonson@redhat.com> commit]9a46559[Author: Samuel Monson <smonson@redhat.com> Date: Tue Sep 15 16:39:15 2026 -0400 Allow console cleanup to be disabled For testing purposes let the "transient" state be configurable at creation time. Signed-off-by: Samuel Monson <smonson@redhat.com> --------- Generated-by: Cursor Signed-off-by: Samuel Monson <smonson@redhat.com>]7c71853

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

This could be separate PRs but each change is so small that its not really worth it. See commit messages for details.

## Use of AI

## git log

commit

afaafb1Author: Samuel Monson smonson@redhat.com

Date: Tue Sep 15 18:52:24 2026 +0000

commit

db4a0e3Author: Samuel Monson smonson@redhat.com

Date: Tue Sep 15 15:21:57 2026 -0400

commit

1b41bd8Author: Samuel Monson smonson@redhat.com

Date: Tue Sep 15 15:52:57 2026 -0400

commit

9a46559Author: Samuel Monson smonson@redhat.com

Date: Tue Sep 15 16:34:32 2026 -0400

commit

7c71853Author: Samuel Monson smonson@redhat.com

Date: Tue Sep 15 16:39:15 2026 -0400

Generated-by: Cursor

Signed-off-by: Samuel Monson smonson@redhat.com