source: https://github.com/vllm-project/guidellm/pull/825

# Restore startup logs and fix config environment variable support - #825

Merged

Merged

## Conversation

Assisted-by: GitHub Copilot GPT-4.1 Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>

Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com>

Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com>


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Jun 22, 2026

Contributor

|
Queued — the merge queue status continues in |


**approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Jun 23, 2026

Contributor

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

34 tasks

[SkiHatDuckie](https://github.com/SkiHatDuckie)pushed a commit to SkiHatDuckie/guidellm that referenced this pull request

Jun 23, 2026

[…m-project#825]) ## TODO - [ ] Fix documentation (waiting on[vllm-project#814]) ## Summary (Re-)adds startup logs and fixes ENV -> CLI support ## Details 1. Adds a bunch of startup messages pertaining to benchmark component creation 2. Re-implements environment variable support for benchmark arguments using pydantic-settings rather then click. This allows for setting nested fields. ## Test Plan Run CLI commands with various combinations of environment variables and CLI arguments. ## Related Issues - Resolves[vllm-project#504]--- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [x] Includes code generated or substantially modified by an AI agent - [x] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- # git log commit[Author: Samuel Monson <smonson@redhat.com> Date: Thu Jun 18 16:53:27 2026 -0400 Add/update resolve logs during startup Assisted-by: GitHub Copilot GPT-4.1 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]d969afd[Author: Samuel Monson <smonson@redhat.com> Date: Thu Jun 18 17:26:02 2026 -0400 Restore ENV message Signed-off-by: Samuel Monson <smonson@redhat.com> commit]be7bb06[Author: Samuel Monson <smonson@redhat.com> Date: Thu Jun 18 18:27:53 2026 -0400 Change BenchmarkScenario ENV deliminator Signed-off-by: Samuel Monson <smonson@redhat.com> commit]5fc9c99[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 22 14:07:07 2026 -0400 Handle str values in before validators Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]a58d70c[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 22 14:09:16 2026 -0400 Improve env validator to work with discriminated fields Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> --------- Assisted-by: GitHub Copilot GPT-4.1 Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com>]9aca8d7

[SkiHatDuckie](https://github.com/SkiHatDuckie)pushed a commit to SkiHatDuckie/guidellm that referenced this pull request

Jun 24, 2026

[…m-project#825]) ## TODO - [ ] Fix documentation (waiting on[vllm-project#814]) ## Summary (Re-)adds startup logs and fixes ENV -> CLI support ## Details 1. Adds a bunch of startup messages pertaining to benchmark component creation 2. Re-implements environment variable support for benchmark arguments using pydantic-settings rather then click. This allows for setting nested fields. ## Test Plan Run CLI commands with various combinations of environment variables and CLI arguments. ## Related Issues - Resolves[vllm-project#504]--- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [x] Includes code generated or substantially modified by an AI agent - [x] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- # git log commit[Author: Samuel Monson <smonson@redhat.com> Date: Thu Jun 18 16:53:27 2026 -0400 Add/update resolve logs during startup Assisted-by: GitHub Copilot GPT-4.1 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]d969afd[Author: Samuel Monson <smonson@redhat.com> Date: Thu Jun 18 17:26:02 2026 -0400 Restore ENV message Signed-off-by: Samuel Monson <smonson@redhat.com> commit]be7bb06[Author: Samuel Monson <smonson@redhat.com> Date: Thu Jun 18 18:27:53 2026 -0400 Change BenchmarkScenario ENV deliminator Signed-off-by: Samuel Monson <smonson@redhat.com> commit]5fc9c99[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 22 14:07:07 2026 -0400 Handle str values in before validators Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]a58d70c[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 22 14:09:16 2026 -0400 Improve env validator to work with discriminated fields Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> --------- Assisted-by: GitHub Copilot GPT-4.1 Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com>]9aca8d7

[SkiHatDuckie](https://github.com/SkiHatDuckie)pushed a commit to SkiHatDuckie/guidellm that referenced this pull request

Jul 6, 2026

[…m-project#825]) ## TODO - [ ] Fix documentation (waiting on[vllm-project#814]) ## Summary (Re-)adds startup logs and fixes ENV -> CLI support ## Details 1. Adds a bunch of startup messages pertaining to benchmark component creation 2. Re-implements environment variable support for benchmark arguments using pydantic-settings rather then click. This allows for setting nested fields. ## Test Plan Run CLI commands with various combinations of environment variables and CLI arguments. ## Related Issues - Resolves[vllm-project#504]--- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [x] Includes code generated or substantially modified by an AI agent - [x] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- # git log commit[Author: Samuel Monson <smonson@redhat.com> Date: Thu Jun 18 16:53:27 2026 -0400 Add/update resolve logs during startup Assisted-by: GitHub Copilot GPT-4.1 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]d969afd[Author: Samuel Monson <smonson@redhat.com> Date: Thu Jun 18 17:26:02 2026 -0400 Restore ENV message Signed-off-by: Samuel Monson <smonson@redhat.com> commit]be7bb06[Author: Samuel Monson <smonson@redhat.com> Date: Thu Jun 18 18:27:53 2026 -0400 Change BenchmarkScenario ENV deliminator Signed-off-by: Samuel Monson <smonson@redhat.com> commit]5fc9c99[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 22 14:07:07 2026 -0400 Handle str values in before validators Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]a58d70c[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 22 14:09:16 2026 -0400 Improve env validator to work with discriminated fields Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> --------- Assisted-by: GitHub Copilot GPT-4.1 Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com>]9aca8d7

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## TODO

## Summary

(Re-)adds startup logs and fixes ENV -> CLI support

## Details

## Test Plan

Run CLI commands with various combinations of environment variables and CLI arguments.

## Related Issues

## Use of AI

## git log

commit

d969afdAuthor: Samuel Monson smonson@redhat.com

Date: Thu Jun 18 16:53:27 2026 -0400

commit

be7bb06Author: Samuel Monson smonson@redhat.com

Date: Thu Jun 18 17:26:02 2026 -0400

commit

5fc9c99Author: Samuel Monson smonson@redhat.com

Date: Thu Jun 18 18:27:53 2026 -0400

commit

a58d70cAuthor: Samuel Monson smonson@redhat.com

Date: Mon Jun 22 14:07:07 2026 -0400

commit

9aca8d7Author: Samuel Monson smonson@redhat.com

Date: Mon Jun 22 14:09:16 2026 -0400

Assisted-by: GitHub Copilot GPT-4.1

Generated-by: claude-code Opus 4.6

Signed-off-by: Samuel Monson smonson@redhat.com