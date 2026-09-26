source: https://github.com/vllm-project/guidellm/pull/630

# Add merge policies - #630

Merged

Merged

## Conversation

Signed-off-by: Samuel Monson <smonson@redhat.com>

Contributor

## Merge ProtectionsYour pull request matches the following merge protections and will not be merged until they are valid. ## 🟢 📃 Configuration Change Requirements## Wonderful, this rule succeeded.Mergify configuration change
|

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/6fd23b1c1ab10d0e560a0ae7946e23f6a9518684..b38b6c0abed9f3bdcccd28b54de1dcb79d9e0a72)the ci/pr_policy branch 2 times, most recently from

[to](https://github.com/vllm-project/guidellm/commit/6fd23b1c1ab10d0e560a0ae7946e23f6a9518684)

`6fd23b1`


`b38b6c0`

[Compare](https://github.com/vllm-project/guidellm/compare/6fd23b1c1ab10d0e560a0ae7946e23f6a9518684..b38b6c0abed9f3bdcccd28b54de1dcb79d9e0a72)

March 12, 2026 21:13

Signed-off-by: Samuel Monson <smonson@redhat.com>


**previously approved these changes**

[dbutenhof](https://github.com/dbutenhof)Mar 13, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)
Collaborator


There was a problem hiding this comment.

Very cool. We should consider setting up a Mergify merge queue to minimize the chance of conflicting logic ... although with their greater scale I'm a little surprised vLLM isn't already using this. (Unless they're already using native GitHub merge queues, I suppose. I can't see their settings.)

I also kinda like vLLM's implicit labeling, at least `documentation`

and `build`

... but we can debate that another time.

None of my comments are blocking: this looks like a great addition.

[.github/mergify.yml](https://github.com/vllm-project/guidellm/pull/630/files/f715bea867e84c47de0c271c5c8d16c574d150e9#diff-dcdc7e558c3de57ed664315abfe65892d731523da4d59d992f324b891453c430)Outdated

[.github/mergify.yml](https://github.com/vllm-project/guidellm/pull/630/files/f715bea867e84c47de0c271c5c8d16c574d150e9#diff-dcdc7e558c3de57ed664315abfe65892d731523da4d59d992f324b891453c430)Outdated

[.github/mergify.yml](https://github.com/vllm-project/guidellm/pull/630/files/f715bea867e84c47de0c271c5c8d16c574d150e9#diff-dcdc7e558c3de57ed664315abfe65892d731523da4d59d992f324b891453c430)Outdated

[.github/workflows/development.yml](https://github.com/vllm-project/guidellm/pull/630/files/f715bea867e84c47de0c271c5c8d16c574d150e9#diff-73aefd4c5a252c08017de5edafa094a95ee6031e37832d96a4ff247563a57833)

[.github/mergify.yml](https://github.com/vllm-project/guidellm/pull/630/files/f715bea867e84c47de0c271c5c8d16c574d150e9#diff-dcdc7e558c3de57ed664315abfe65892d731523da4d59d992f324b891453c430)

Signed-off-by: Samuel Monson <smonson@redhat.com>

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

vLLM uses Mergify to configure various policy checks. Since we already have access to the app through the project, this PR adopts a few of vLLM's checks.

## Details

Adds PR notifications for:

Also configures automatic rebase for PRs that are far behind.

## Test Plan

Review enforcement across new PRs. Mergify is currently non-blocking in CI which can be changed after we finish evaluating it.

## Use of AI

`## WRITTEN BY AI ##`

)