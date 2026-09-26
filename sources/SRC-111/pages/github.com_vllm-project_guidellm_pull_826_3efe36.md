source: https://github.com/vllm-project/guidellm/pull/826

# Revert Pydantic Registry parameters back to single value fields - #826

Merged

[mergify[bot]](https://github.com/mergify[bot])merged 3 commits into

Merged

## Conversation

Chnages the CLI format for arguments based on pydantic registries back to the interim single arg-string format. This works better in a lot of cases where only the discriminator needs to be set. Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>

Without this errors are still caught but this gives a nicer error message that includes possible discriminator values. Generated-by: claude-code Sonnet 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com>


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Jun 22, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)
Collaborator


There was a problem hiding this comment.

Pulled it -- it works.

Contributor

|
Queued — the merge queue status continues in |

Contributor

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

34 tasks

[SkiHatDuckie](https://github.com/SkiHatDuckie)pushed a commit to SkiHatDuckie/guidellm that referenced this pull request

Jun 23, 2026

[…-project#826]) ## Summary Changes the `--profile async rate=10` format back to `--profile kind=async,rate=10` for all arguments based on Pydantic Registries. ## Details After trialing the `nargs=2` format for a while, we have concluded that its a little too cumbersome in edge-cases were only `kind` is needed. Before this change, such cases would need a blank string. E.g. `--profile sweep ''`. Now that string is unnecessary at the cost of a few extra characters for every option. ## Test Plan Run common CLI commands ## Related Issues - Related to[vllm-project#789]--- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [x] Includes code generated or substantially modified by an AI agent - [x] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- # git log commit[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 22 15:59:04 2026 -0400 Revert to nargs=1 registry args format Chnages the CLI format for arguments based on pydantic registries back to the interim single arg-string format. This works better in a lot of cases where only the discriminator needs to be set. Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]7deaf7d[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 22 16:03:04 2026 -0400 Sort `--config` flag at the top of help Signed-off-by: Samuel Monson <smonson@redhat.com> commit]ba40a24[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 22 16:22:24 2026 -0400 Re-add validator for schema_discriminator Without this errors are still caught but this gives a nicer error message that includes possible discriminator values. Generated-by: claude-code Sonnet 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> --------- Generated-by: claude-code Opus 4.6 Generated-by: claude-code Sonnet 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com>]7d10128

[SkiHatDuckie](https://github.com/SkiHatDuckie)pushed a commit to SkiHatDuckie/guidellm that referenced this pull request

Jun 24, 2026

[…-project#826]) ## Summary Changes the `--profile async rate=10` format back to `--profile kind=async,rate=10` for all arguments based on Pydantic Registries. ## Details After trialing the `nargs=2` format for a while, we have concluded that its a little too cumbersome in edge-cases were only `kind` is needed. Before this change, such cases would need a blank string. E.g. `--profile sweep ''`. Now that string is unnecessary at the cost of a few extra characters for every option. ## Test Plan Run common CLI commands ## Related Issues - Related to[vllm-project#789]--- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [x] Includes code generated or substantially modified by an AI agent - [x] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- # git log commit[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 22 15:59:04 2026 -0400 Revert to nargs=1 registry args format Chnages the CLI format for arguments based on pydantic registries back to the interim single arg-string format. This works better in a lot of cases where only the discriminator needs to be set. Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]7deaf7d[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 22 16:03:04 2026 -0400 Sort `--config` flag at the top of help Signed-off-by: Samuel Monson <smonson@redhat.com> commit]ba40a24[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 22 16:22:24 2026 -0400 Re-add validator for schema_discriminator Without this errors are still caught but this gives a nicer error message that includes possible discriminator values. Generated-by: claude-code Sonnet 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> --------- Generated-by: claude-code Opus 4.6 Generated-by: claude-code Sonnet 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com>]7d10128

[SkiHatDuckie](https://github.com/SkiHatDuckie)pushed a commit to SkiHatDuckie/guidellm that referenced this pull request

Jul 6, 2026

[…-project#826]) ## Summary Changes the `--profile async rate=10` format back to `--profile kind=async,rate=10` for all arguments based on Pydantic Registries. ## Details After trialing the `nargs=2` format for a while, we have concluded that its a little too cumbersome in edge-cases were only `kind` is needed. Before this change, such cases would need a blank string. E.g. `--profile sweep ''`. Now that string is unnecessary at the cost of a few extra characters for every option. ## Test Plan Run common CLI commands ## Related Issues - Related to[vllm-project#789]--- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [x] Includes code generated or substantially modified by an AI agent - [x] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- # git log commit[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 22 15:59:04 2026 -0400 Revert to nargs=1 registry args format Chnages the CLI format for arguments based on pydantic registries back to the interim single arg-string format. This works better in a lot of cases where only the discriminator needs to be set. Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]7deaf7d[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 22 16:03:04 2026 -0400 Sort `--config` flag at the top of help Signed-off-by: Samuel Monson <smonson@redhat.com> commit]ba40a24[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 22 16:22:24 2026 -0400 Re-add validator for schema_discriminator Without this errors are still caught but this gives a nicer error message that includes possible discriminator values. Generated-by: claude-code Sonnet 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> --------- Generated-by: claude-code Opus 4.6 Generated-by: claude-code Sonnet 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com>]7d10128

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

Changes the

`--profile async rate=10`

format back to`--profile kind=async,rate=10`

for all arguments based on Pydantic Registries.## Details

After trialing the

`nargs=2`

format for a while, we have concluded that its a little too cumbersome in edge-cases were only`kind`

is needed. Before this change, such cases would need a blank string. E.g.`--profile sweep ''`

. Now that string is unnecessary at the cost of a few extra characters for every option.## Test Plan

Run common CLI commands

## Related Issues

## Use of AI

## git log

commit

7deaf7dAuthor: Samuel Monson smonson@redhat.com

Date: Mon Jun 22 15:59:04 2026 -0400

commit

ba40a24Author: Samuel Monson smonson@redhat.com

Date: Mon Jun 22 16:03:04 2026 -0400

commit

7d10128Author: Samuel Monson smonson@redhat.com

Date: Mon Jun 22 16:22:24 2026 -0400

Generated-by: claude-code Opus 4.6

Generated-by: claude-code Sonnet 4.6

Signed-off-by: Samuel Monson smonson@redhat.com