source: https://github.com/vllm-project/guidellm/pull/863

# Added registry setup for metrics, with accompanying CLI option - #863

Merged

[mergify[bot]](https://github.com/mergify[bot])merged 3 commits into

Merged

## Conversation

Generated-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Generated-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Signed-off-by: Jared O'Connell <joconnel@redhat.com>


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Jun 25, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)
Collaborator


There was a problem hiding this comment.

One abstract comment I'll pre-resolve, but I'm willing to take this as-is rather than complicating it.

(After/if this goes in, I'll update my CLI migration guide...)

[src/guidellm/benchmark/entrypoints.py](https://github.com/vllm-project/guidellm/pull/863/files/2af6e9f9a8a56a465b557b27a5e0a5943cc9cd79#diff-cd7a125f54c14282a282a288e2d13c374c8fda383484a936c3571c8d818a96a1)

Contributor

|
Queued — the merge queue status continues in |

[sjmonson](https://github.com/sjmonson)self-requested a review

June 26, 2026 00:05


**approved these changes**

[sjmonson](https://github.com/sjmonson)Jun 26, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)
Collaborator


There was a problem hiding this comment.

I would prefer moving `MetricsArgs`

to its own file but not really a blocker.

Contributor

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

34 tasks

[mergify](https://github.com/apps/mergify)Bot pushed a commit that referenced this pull request

Jun 26, 2026

## Summary Handles a bunch of missing pieces from the refactor. See individual commits below. ## Test Plan - Check that `--label`s are applied to output - ~Verify `--profile ...,sample_requests=#` results in a downsampling of requests in output~ Dropped in favor of[#863]- Check `guidellm run --help` to ensure that the new help messages exists and are helpful. ## Related Issues - Resolves[#728]--- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [ ] Includes code generated or substantially modified by an AI agent - [ ] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- # git log commit[Author: Samuel Monson <smonson@redhat.com> Date: Wed Jun 24 14:20:06 2026 -0400 Add help message to --override Assisted-by: GitHub Copilot GPT-4.1 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]bd35054[Author: Samuel Monson <smonson@redhat.com> Date: Wed Jun 24 15:18:41 2026 -0400 Add label CLI option Wires the label metadata field to the CLI. Assisted-by: GitHub Copilot GPT-4.1 Signed-off-by: Samuel Monson <smonson@redhat.com> --------- Assisted-by: GitHub Copilot GPT-4.1 Signed-off-by: Samuel Monson <smonson@redhat.com>]be46904

[SkiHatDuckie](https://github.com/SkiHatDuckie)pushed a commit to SkiHatDuckie/guidellm that referenced this pull request

Jul 2, 2026

[…project#863]) Creates a registry-based input for metrics. - The `kind` for the metrics input is `generative`, since it's designed to go with generative benchmarks. - Includes options for `sample_size` and `prefer_response_metrics`. - Example of the arg: `--metrics kind=generative,sample_size=2` Run a benchmark with a low sample size, and count them in the output. The `extract_conversation.py` script is a good one for this. --- - [x] "I certify that all code in this PR is my own, except as noted below." - [x] Includes code generated or substantially modified by an AI agent - [x] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- commit[Author: Jared O'Connell <joconnel@redhat.com> Date: Thu Jun 25 17:36:35 2026 -0400 Added registry setup for metrics, with accompanying CLI option Generated-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com> commit]b4c4335[Author: Jared O'Connell <joconnel@redhat.com> Date: Thu Jun 25 17:53:28 2026 -0400 Added docs for the sample size setting Generated-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com> commit]c50a786[Author: Jared O'Connell <joconnel@redhat.com> Date: Thu Jun 25 18:26:30 2026 -0400 Fix linter errors Signed-off-by: Jared O'Connell <joconnel@redhat.com> --------- Generated-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com>]2af6e9f

[SkiHatDuckie](https://github.com/SkiHatDuckie)pushed a commit to SkiHatDuckie/guidellm that referenced this pull request

Jul 2, 2026

## Summary Handles a bunch of missing pieces from the refactor. See individual commits below. ## Test Plan - Check that `--label`s are applied to output - ~Verify `--profile ...,sample_requests=#` results in a downsampling of requests in output~ Dropped in favor of[vllm-project#863]- Check `guidellm run --help` to ensure that the new help messages exists and are helpful. ## Related Issues - Resolves[vllm-project#728]--- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [ ] Includes code generated or substantially modified by an AI agent - [ ] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- # git log commit[Author: Samuel Monson <smonson@redhat.com> Date: Wed Jun 24 14:20:06 2026 -0400 Add help message to --override Assisted-by: GitHub Copilot GPT-4.1 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]bd35054[Author: Samuel Monson <smonson@redhat.com> Date: Wed Jun 24 15:18:41 2026 -0400 Add label CLI option Wires the label metadata field to the CLI. Assisted-by: GitHub Copilot GPT-4.1 Signed-off-by: Samuel Monson <smonson@redhat.com> --------- Assisted-by: GitHub Copilot GPT-4.1 Signed-off-by: Samuel Monson <smonson@redhat.com>]be46904

[SkiHatDuckie](https://github.com/SkiHatDuckie)pushed a commit to SkiHatDuckie/guidellm that referenced this pull request

Jul 6, 2026

[…project#863]) ## Summary Creates a registry-based input for metrics. ## Details - The `kind` for the metrics input is `generative`, since it's designed to go with generative benchmarks. - Includes options for `sample_size` and `prefer_response_metrics`. - Example of the arg: `--metrics kind=generative,sample_size=2` ## Test Plan Run a benchmark with a low sample size, and count them in the output. The `extract_conversation.py` script is a good one for this. --- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [x] Includes code generated or substantially modified by an AI agent - [x] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- # git log commit[Author: Jared O'Connell <joconnel@redhat.com> Date: Thu Jun 25 17:36:35 2026 -0400 Added registry setup for metrics, with accompanying CLI option Generated-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com> commit]b4c4335[Author: Jared O'Connell <joconnel@redhat.com> Date: Thu Jun 25 17:53:28 2026 -0400 Added docs for the sample size setting Generated-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com> commit]c50a786[Author: Jared O'Connell <joconnel@redhat.com> Date: Thu Jun 25 18:26:30 2026 -0400 Fix linter errors Signed-off-by: Jared O'Connell <joconnel@redhat.com> --------- Generated-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com>]2af6e9f

[SkiHatDuckie](https://github.com/SkiHatDuckie)pushed a commit to SkiHatDuckie/guidellm that referenced this pull request

Jul 6, 2026

## Summary Handles a bunch of missing pieces from the refactor. See individual commits below. ## Test Plan - Check that `--label`s are applied to output - ~Verify `--profile ...,sample_requests=#` results in a downsampling of requests in output~ Dropped in favor of[vllm-project#863]- Check `guidellm run --help` to ensure that the new help messages exists and are helpful. ## Related Issues - Resolves[vllm-project#728]--- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [ ] Includes code generated or substantially modified by an AI agent - [ ] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- # git log commit[Author: Samuel Monson <smonson@redhat.com> Date: Wed Jun 24 14:20:06 2026 -0400 Add help message to --override Assisted-by: GitHub Copilot GPT-4.1 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]bd35054[Author: Samuel Monson <smonson@redhat.com> Date: Wed Jun 24 15:18:41 2026 -0400 Add label CLI option Wires the label metadata field to the CLI. Assisted-by: GitHub Copilot GPT-4.1 Signed-off-by: Samuel Monson <smonson@redhat.com> --------- Assisted-by: GitHub Copilot GPT-4.1 Signed-off-by: Samuel Monson <smonson@redhat.com>]be46904

6 tasks

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

Creates a registry-based input for metrics.

## Details

`kind`

for the metrics input is`generative`

, since it's designed to go with generative benchmarks.`sample_size`

and`prefer_response_metrics`

.`--metrics kind=generative,sample_size=2`

## Test Plan

Run a benchmark with a low sample size, and count them in the output. The

`extract_conversation.py`

script is a good one for this.## Use of AI

## git log

commit

b4c4335Author: Jared O'Connell joconnel@redhat.com

Date: Thu Jun 25 17:36:35 2026 -0400

commit

c50a786Author: Jared O'Connell joconnel@redhat.com

Date: Thu Jun 25 17:53:28 2026 -0400

commit

2af6e9fAuthor: Jared O'Connell joconnel@redhat.com

Date: Thu Jun 25 18:26:30 2026 -0400

Generated-by: Cursor AI Claude Opus 4.6

Signed-off-by: Jared O'Connell joconnel@redhat.com