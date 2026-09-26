source: https://github.com/vllm-project/guidellm/pull/754

# [v0.7 CLI Refactor] Finish up data rework - #754

Merged

Merged

## Conversation

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/825eaba9433707aa7e581e73c43596c125cc1ee2..4b4eb40763cff3ca492c86c959601e63b55ce7da)the refactor/schema/data_2 branch from

[to](https://github.com/vllm-project/guidellm/commit/825eaba9433707aa7e581e73c43596c125cc1ee2)

`825eaba`


`4b4eb40`

[Compare](https://github.com/vllm-project/guidellm/compare/825eaba9433707aa7e581e73c43596c125cc1ee2..4b4eb40763cff3ca492c86c959601e63b55ce7da)

May 29, 2026 18:04


[sjmonson](https://github.com/sjmonson)added

[internal](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Ainternal)

[feature](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Afeature)

[cli](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Acli)

May 29, 2026


**previously approved these changes**

[dbutenhof](https://github.com/dbutenhof)Jun 2, 2026


**previously approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Jun 2, 2026

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)
Collaborator


There was a problem hiding this comment.

Looks good to me.

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/4b4eb40763cff3ca492c86c959601e63b55ce7da..8c7f54ba5db8b1d86c0a24059af1099402feb1f5)the refactor/schema/data_2 branch from

[to](https://github.com/vllm-project/guidellm/commit/4b4eb40763cff3ca492c86c959601e63b55ce7da)

`4b4eb40`


`8c7f54b`

[Compare](https://github.com/vllm-project/guidellm/compare/4b4eb40763cff3ca492c86c959601e63b55ce7da..8c7f54ba5db8b1d86c0a24059af1099402feb1f5)

June 2, 2026 19:32


**approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Jun 3, 2026

Collaborator
Author

|
|

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/96c9e2bea26716d5ceb22876b8be3d793cb1af2a..4dc2756bad3a3272d3e9c508761820f3e72ea692)the refactor/schema/data_2 branch from

[to](https://github.com/vllm-project/guidellm/commit/96c9e2bea26716d5ceb22876b8be3d793cb1af2a)

`96c9e2b`


`4dc2756`

[Compare](https://github.com/vllm-project/guidellm/compare/96c9e2bea26716d5ceb22876b8be3d793cb1af2a..4dc2756bad3a3272d3e9c508761820f3e72ea692)

June 3, 2026 18:34

Contributor

|
|

Contributor

## ✅ Branch has been successfully rebased |

Assisted-by: GitHub Copilot GPT-4.1 Signed-off-by: Samuel Monson <smonson@redhat.com>

Generated-by: claude-code Sonnet 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/4dc2756bad3a3272d3e9c508761820f3e72ea692..95d3ff61c8149976952f5d054cc3d3ef69f0d893)the refactor/schema/data_2 branch from

[to](https://github.com/vllm-project/guidellm/commit/4dc2756bad3a3272d3e9c508761820f3e72ea692)

`4dc2756`


`95d3ff6`

[Compare](https://github.com/vllm-project/guidellm/compare/4dc2756bad3a3272d3e9c508761820f3e72ea692..95d3ff61c8149976952f5d054cc3d3ef69f0d893)

June 3, 2026 19:41

Collaborator
Author

|
|

Contributor

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

[SkiHatDuckie](https://github.com/SkiHatDuckie)pushed a commit to SkiHatDuckie/guidellm that referenced this pull request

Jun 8, 2026

## Summary Move creation of various data objects out of DataLoader and into an entrypoint method. Also finish converting remaining data objects to use config registries (or remove the object entirely). ## Details - Created a `create_data_loader` entrypoint method which takes all data related config options and creates each object before creating the data loader rather then passing all the configs to the data loader `__init__`. - Renamed `processor` back to `tokenizer` and made it follow the config + create registry pattern. - Dropped `collator` configuration since it currently does not make sense to have a custom collator. - Dropped `sampler` configuration (except for shuffle mode) with the intent to revisit in a future release. ## Test Plan Run benchmarks, outer functionality should stay the same other then the random seed is distributed differently so any random dependent data will differ. ## Related Issues - Related to[vllm-project#724]--- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [x] Includes code generated or substantially modified by an AI agent - [x] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- # git log commit[Author: Samuel Monson <smonson@redhat.com> Date: Fri May 29 10:22:12 2026 -0400 Refactor data entrypoint + tokenizer Assisted-by: GitHub Copilot GPT-4.1 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]d5a4fe0[Author: Samuel Monson <smonson@redhat.com> Date: Fri May 29 11:26:51 2026 -0400 Fix unit tests Generated-by: claude-code Sonnet 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]586f439[Author: Samuel Monson <smonson@redhat.com> Date: Tue Jun 2 17:21:30 2026 -0400 Fix new lint error after rebase Signed-off-by: Samuel Monson <smonson@redhat.com> --------- Assisted-by: GitHub Copilot GPT-4.1 Generated-by: claude-code Sonnet 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>]95d3ff6

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

Move creation of various data objects out of DataLoader and into an entrypoint method. Also finish converting remaining data objects to use config registries (or remove the object entirely).

## Details

`create_data_loader`

entrypoint method which takes all data related config options and creates each object before creating the data loader rather then passing all the configs to the data loader`__init__`

.`processor`

back to`tokenizer`

and made it follow the config + create registry pattern.`collator`

configuration since it currently does not make sense to have a custom collator.`sampler`

configuration (except for shuffle mode) with the intent to revisit in a future release.## Test Plan

Run benchmarks, outer functionality should stay the same other then the random seed is distributed differently so any random dependent data will differ.

## Related Issues

## Use of AI

## git log

commit

d5a4fe0Author: Samuel Monson smonson@redhat.com

Date: Fri May 29 10:22:12 2026 -0400

commit

586f439Author: Samuel Monson smonson@redhat.com

Date: Fri May 29 11:26:51 2026 -0400

commit

95d3ff6Author: Samuel Monson smonson@redhat.com

Date: Tue Jun 2 17:21:30 2026 -0400

Assisted-by: GitHub Copilot GPT-4.1

Generated-by: claude-code Sonnet 4.6

Signed-off-by: Samuel Monson smonson@redhat.com