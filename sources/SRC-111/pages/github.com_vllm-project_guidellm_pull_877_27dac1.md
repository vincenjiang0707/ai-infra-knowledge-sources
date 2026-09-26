source: https://github.com/vllm-project/guidellm/pull/877

# Support for per sub-benchmark constraints - #877

Merged

[mergify[bot]](https://github.com/mergify[bot])merged 3 commits into

Merged

## Conversation


[sjmonson](https://github.com/sjmonson)changed the title

Jul 1, 2026

Assisted-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com>

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/da354a2eae3363d6995cd8df002b9ac49a3b611d..d6716e0f71c8b066fc1fb6db596f0c427b76f28d)the feat/per_bench_constraints branch 2 times, most recently from

[to](https://github.com/vllm-project/guidellm/commit/da354a2eae3363d6995cd8df002b9ac49a3b611d)

`da354a2`


`d6716e0`

[Compare](https://github.com/vllm-project/guidellm/compare/da354a2eae3363d6995cd8df002b9ac49a3b611d..d6716e0f71c8b066fc1fb6db596f0c427b76f28d)

July 1, 2026 21:05

Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com>

Because some constraints tick up an internal counter for each resolve and treat that as an index for the current benchmark, resolving in the scheduler desyncs this counter from the current benchmark. The original behavior is not even necessary without distributed benchmarking, and may not be necessary even for that. So just drop the resolve for now and pass through the constraints untouched. Signed-off-by: Samuel Monson <smonson@redhat.com>

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/d6716e0f71c8b066fc1fb6db596f0c427b76f28d..e4f6aafe0c031f265a721f90f46fd1d07247e931)the feat/per_bench_constraints branch from

[to](https://github.com/vllm-project/guidellm/commit/d6716e0f71c8b066fc1fb6db596f0c427b76f28d)

`d6716e0`


`e4f6aaf`

[Compare](https://github.com/vllm-project/guidellm/compare/d6716e0f71c8b066fc1fb6db596f0c427b76f28d..e4f6aafe0c031f265a721f90f46fd1d07247e931)

July 1, 2026 21:07


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Jul 1, 2026

Collaborator


There was a problem hiding this comment.

`uv run guidellm run --backend kind=openai_http,target=http://*.example.com --profile kind=concurrent --constraint kind=max_duration,seconds=10 --data "kind=synthetic_text,prompt_tokens=128" --override 'constraints[0].seconds' 4,8,12 --override profile.streams 10,12,16`

works as expected -- 10, 12, and 16 concurrent stream strategies, capped at 4, 8, and 12 seconds.

Contributor

|
Queued — the merge queue status continues in |

Collaborator

Yeah, I was thinking of pointing out documentation -- but in my eagerness to get it done, I forgot. Then again, I think we forgot to add anything about |

Contributor

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

34 tasks

11 tasks

[SkiHatDuckie](https://github.com/SkiHatDuckie)pushed a commit to SkiHatDuckie/guidellm that referenced this pull request

Jul 2, 2026

Support for per sub-benchmark constraints for a subset of the constraints. `max_requests`, `max_duration`, `max_errors`, and `max_error_rate` have all had hidden support for being specified per sub-benchmark. This PR wires that support up to the new CLI. Currently the entrypoint code is all an ugly hack so that will have to be replaced in an upcoming release. Test with multiple different constraint values: ```sh guidellm run ... --constraint kind=max_duration --override 'constraints[0].seconds' 5,10,15,20 guidellm run ... --constraint kind=max_requests --override 'constraints[0].count' 5,10,15,20 guidellm run ... --constraint kind=max_error --override 'constraints[0].count' 5,10,15,20 ``` and in combination with other overrides: ```sh guidellm run ... \ --profile kind=constant \ --constraint kind=max_duration \ --override "profile.rate" 1,2,4,5 \ --override "constraints[0].seconds" 5,10,15,20 ``` and multi constraint: ```sh guidellm run ... \ --constraint kind=max_error \ --override "constraints[0].count" 5,10,15,20 \ --constraint kind=max_duration \ --override "constraints[1].seconds" 5,10,15,20 ``` - Resolves[vllm-project#451]- Resolves[vllm-project#253]--- - [x] "I certify that all code in this PR is my own, except as noted below." - [x] Includes code generated or substantially modified by an AI agent - [ ] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- commit[Author: Samuel Monson <smonson@redhat.com> Date: Wed Jul 1 15:23:28 2026 -0400 Fix constraint resolve ordering Assisted-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]6e39986[Author: Samuel Monson <smonson@redhat.com> Date: Wed Jul 1 15:24:54 2026 -0400 Add adaptor from multivalue capable constraints Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]f6c8c31[Author: Samuel Monson <smonson@redhat.com> Date: Wed Jul 1 16:36:39 2026 -0400 Drop constraint resolve from core scheduler Because some constraints tick up an internal counter for each resolve and treat that as an index for the current benchmark, resolving in the scheduler desyncs this counter from the current benchmark. The original behavior is not even necessary without distributed benchmarking, and may not be necessary even for that. So just drop the resolve for now and pass through the constraints untouched. Signed-off-by: Samuel Monson <smonson@redhat.com> --------- Assisted-by: claude-code Opus 4.6 Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com>]e4f6aaf

3 tasks

[mergify](https://github.com/apps/mergify)Bot pushed a commit that referenced this pull request

Jul 2, 2026

## Summary Adds some integration tests to catch any breakage in constraint overrides. ## Details - Tests the assembling of the constraints, and tests advancing the index. ## Test Plan - Just ensure it passes CI. ## Related Issues[#877]--- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [ ] Includes code generated or substantially modified by an AI agent - [x] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- # git log commit[Author: Jared O'Connell <joconnel@redhat.com> Date: Thu Jul 2 15:41:05 2026 -0400 Added integration tests for constraint overrides Generated-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com> --------- Generated-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com>]2febfd0

[SkiHatDuckie](https://github.com/SkiHatDuckie)pushed a commit to SkiHatDuckie/guidellm that referenced this pull request

Jul 6, 2026

## Summary Support for per sub-benchmark constraints for a subset of the constraints. ## Details `max_requests`, `max_duration`, `max_errors`, and `max_error_rate` have all had hidden support for being specified per sub-benchmark. This PR wires that support up to the new CLI. Currently the entrypoint code is all an ugly hack so that will have to be replaced in an upcoming release. ## Test Plan Test with multiple different constraint values: ```sh # Duration guidellm run ... --constraint kind=max_duration --override 'constraints[0].seconds' 5,10,15,20 # Requests guidellm run ... --constraint kind=max_requests --override 'constraints[0].count' 5,10,15,20 # Errors guidellm run ... --constraint kind=max_error --override 'constraints[0].count' 5,10,15,20 ``` and in combination with other overrides: ```sh guidellm run ... \ --profile kind=constant \ --constraint kind=max_duration \ --override "profile.rate" 1,2,4,5 \ --override "constraints[0].seconds" 5,10,15,20 ``` and multi constraint: ```sh guidellm run ... \ --constraint kind=max_error \ --override "constraints[0].count" 5,10,15,20 \ --constraint kind=max_duration \ --override "constraints[1].seconds" 5,10,15,20 ``` ## Related Issues - Resolves[vllm-project#451]- Resolves[vllm-project#253]--- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [x] Includes code generated or substantially modified by an AI agent - [ ] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- # git log commit[Author: Samuel Monson <smonson@redhat.com> Date: Wed Jul 1 15:23:28 2026 -0400 Fix constraint resolve ordering Assisted-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]6e39986[Author: Samuel Monson <smonson@redhat.com> Date: Wed Jul 1 15:24:54 2026 -0400 Add adaptor from multivalue capable constraints Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]f6c8c31[Author: Samuel Monson <smonson@redhat.com> Date: Wed Jul 1 16:36:39 2026 -0400 Drop constraint resolve from core scheduler Because some constraints tick up an internal counter for each resolve and treat that as an index for the current benchmark, resolving in the scheduler desyncs this counter from the current benchmark. The original behavior is not even necessary without distributed benchmarking, and may not be necessary even for that. So just drop the resolve for now and pass through the constraints untouched. Signed-off-by: Samuel Monson <smonson@redhat.com> --------- Assisted-by: claude-code Opus 4.6 Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com>]e4f6aaf

[SkiHatDuckie](https://github.com/SkiHatDuckie)pushed a commit to SkiHatDuckie/guidellm that referenced this pull request

Jul 6, 2026

## Summary Adds some integration tests to catch any breakage in constraint overrides. ## Details - Tests the assembling of the constraints, and tests advancing the index. ## Test Plan - Just ensure it passes CI. ## Related Issues[vllm-project#877]--- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [ ] Includes code generated or substantially modified by an AI agent - [x] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- # git log commit[Author: Jared O'Connell <joconnel@redhat.com> Date: Thu Jul 2 15:41:05 2026 -0400 Added integration tests for constraint overrides Generated-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com> --------- Generated-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com>]2febfd0

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

Support for per sub-benchmark constraints for a subset of the constraints.

## Details

`max_requests`

,`max_duration`

,`max_errors`

, and`max_error_rate`

have all had hidden support for being specified per sub-benchmark. This PR wires that support up to the new CLI. Currently the entrypoint code is all an ugly hack so that will have to be replaced in an upcoming release.## Test Plan

Test with multiple different constraint values:

and in combination with other overrides:

and multi constraint:

## Related Issues

## Use of AI

## git log

commit

6e39986Author: Samuel Monson smonson@redhat.com

Date: Wed Jul 1 15:23:28 2026 -0400

commit

f6c8c31Author: Samuel Monson smonson@redhat.com

Date: Wed Jul 1 15:24:54 2026 -0400

commit

e4f6aafAuthor: Samuel Monson smonson@redhat.com

Date: Wed Jul 1 16:36:39 2026 -0400

Assisted-by: claude-code Opus 4.6

Generated-by: claude-code Opus 4.6

Signed-off-by: Samuel Monson smonson@redhat.com