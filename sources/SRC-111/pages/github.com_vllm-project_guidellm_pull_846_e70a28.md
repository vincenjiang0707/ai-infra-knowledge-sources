source: https://github.com/vllm-project/guidellm/pull/846

# Add `--label`

argument - #846

Merged

[mergify[bot]](https://github.com/mergify[bot])merged 2 commits into

Merged

[Add ](https://github.com#top)`--label`

argument #846

[Add](https://github.com#top)#846

`--label`

argument ## Conversation

[sjmonson](https://github.com/sjmonson)marked this pull request as ready for review

June 25, 2026 17:54


**previously approved these changes**

[dbutenhof](https://github.com/dbutenhof)Jun 25, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)
Collaborator


There was a problem hiding this comment.

Reluctantly, since it beats blocking the option entirely...

Contributor

|
Queued — the merge queue status continues in |


**previously approved these changes**

[dbutenhof](https://github.com/dbutenhof)Jun 25, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)
Collaborator


There was a problem hiding this comment.

OK, so `sample_requests = benchmark_args.profile.sample_size`

is a little weird; but that's all internal so no big deal.


**requested changes**

[jaredoconnell](https://github.com/jaredoconnell)Jun 26, 2026

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)
Collaborator


There was a problem hiding this comment.

This can now be rebased such that only the label changes remain.

Assisted-by: GitHub Copilot GPT-4.1 Signed-off-by: Samuel Monson <smonson@redhat.com>

Wires the label metadata field to the CLI. Assisted-by: GitHub Copilot GPT-4.1 Signed-off-by: Samuel Monson <smonson@redhat.com>

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/56b612f4410e865ffb603738cc2108fa2c7eabbd..be469044350839138e1b5d0c8ddec423b124e01b)the refactor/schema/cleanup_2 branch from

[to](https://github.com/vllm-project/guidellm/commit/56b612f4410e865ffb603738cc2108fa2c7eabbd)

`56b612f`


`be46904`

[Compare](https://github.com/vllm-project/guidellm/compare/56b612f4410e865ffb603738cc2108fa2c7eabbd..be469044350839138e1b5d0c8ddec423b124e01b)

June 26, 2026 19:09

Collaborator
Author

|
|


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Jun 26, 2026


**approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Jun 26, 2026

Contributor

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

[SkiHatDuckie](https://github.com/SkiHatDuckie)pushed a commit to SkiHatDuckie/guidellm that referenced this pull request

Jul 2, 2026

## Summary Handles a bunch of missing pieces from the refactor. See individual commits below. ## Test Plan - Check that `--label`s are applied to output - ~Verify `--profile ...,sample_requests=#` results in a downsampling of requests in output~ Dropped in favor of[vllm-project#863]- Check `guidellm run --help` to ensure that the new help messages exists and are helpful. ## Related Issues - Resolves[vllm-project#728]--- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [ ] Includes code generated or substantially modified by an AI agent - [ ] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- # git log commit[Author: Samuel Monson <smonson@redhat.com> Date: Wed Jun 24 14:20:06 2026 -0400 Add help message to --override Assisted-by: GitHub Copilot GPT-4.1 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]bd35054[Author: Samuel Monson <smonson@redhat.com> Date: Wed Jun 24 15:18:41 2026 -0400 Add label CLI option Wires the label metadata field to the CLI. Assisted-by: GitHub Copilot GPT-4.1 Signed-off-by: Samuel Monson <smonson@redhat.com> --------- Assisted-by: GitHub Copilot GPT-4.1 Signed-off-by: Samuel Monson <smonson@redhat.com>]be46904

[SkiHatDuckie](https://github.com/SkiHatDuckie)pushed a commit to SkiHatDuckie/guidellm that referenced this pull request

Jul 6, 2026

## Summary Handles a bunch of missing pieces from the refactor. See individual commits below. ## Test Plan - Check that `--label`s are applied to output - ~Verify `--profile ...,sample_requests=#` results in a downsampling of requests in output~ Dropped in favor of[vllm-project#863]- Check `guidellm run --help` to ensure that the new help messages exists and are helpful. ## Related Issues - Resolves[vllm-project#728]--- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [ ] Includes code generated or substantially modified by an AI agent - [ ] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- # git log commit[Author: Samuel Monson <smonson@redhat.com> Date: Wed Jun 24 14:20:06 2026 -0400 Add help message to --override Assisted-by: GitHub Copilot GPT-4.1 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]bd35054[Author: Samuel Monson <smonson@redhat.com> Date: Wed Jun 24 15:18:41 2026 -0400 Add label CLI option Wires the label metadata field to the CLI. Assisted-by: GitHub Copilot GPT-4.1 Signed-off-by: Samuel Monson <smonson@redhat.com> --------- Assisted-by: GitHub Copilot GPT-4.1 Signed-off-by: Samuel Monson <smonson@redhat.com>]be46904

6 tasks

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

Handles a bunch of missing pieces from the refactor. See individual commits below.

## Test Plan

`--label`

s are applied to output~~Verify~~Dropped in favor of Added registry setup for metrics, with accompanying CLI option #863`--profile ...,sample_requests=#`

results in a downsampling of requests in output`guidellm run --help`

to ensure that the new help messages exists and are helpful.## Related Issues

## Use of AI

## git log

commit

bd35054Author: Samuel Monson smonson@redhat.com

Date: Wed Jun 24 14:20:06 2026 -0400

commit

be46904Author: Samuel Monson smonson@redhat.com

Date: Wed Jun 24 15:18:41 2026 -0400

Assisted-by: GitHub Copilot GPT-4.1

Signed-off-by: Samuel Monson smonson@redhat.com