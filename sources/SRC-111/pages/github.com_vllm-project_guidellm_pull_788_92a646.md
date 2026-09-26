source: https://github.com/vllm-project/guidellm/pull/788

# [v0.7 CLI Refactor] Misc Cleanup - #788

Merged

[mergify[bot]](https://github.com/mergify[bot])merged 4 commits into

Merged

## Conversation

[sjmonson](https://github.com/sjmonson)marked this pull request as draft

June 10, 2026 15:34

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/c7cbb332f18072fd0f521adf4fab37678e212d92..cec3bb0e1ee588ee1ab27068c5d6f0c6f5a28042)the refactor/schema/cleanup_1 branch 3 times, most recently from

[to](https://github.com/vllm-project/guidellm/commit/c7cbb332f18072fd0f521adf4fab37678e212d92)

`c7cbb33`


`cec3bb0`

[Compare](https://github.com/vllm-project/guidellm/compare/c7cbb332f18072fd0f521adf4fab37678e212d92..cec3bb0e1ee588ee1ab27068c5d6f0c6f5a28042)

June 11, 2026 20:04

Assisted-by: GitHub Copilot GPT-4.1 Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>

Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/cec3bb0e1ee588ee1ab27068c5d6f0c6f5a28042..dcf20a07bd4956e5d4164409c43a080ebdfcb2f3)the refactor/schema/cleanup_1 branch from

[to](https://github.com/vllm-project/guidellm/commit/cec3bb0e1ee588ee1ab27068c5d6f0c6f5a28042)

`cec3bb0`


`dcf20a0`

[Compare](https://github.com/vllm-project/guidellm/compare/cec3bb0e1ee588ee1ab27068c5d6f0c6f5a28042..dcf20a07bd4956e5d4164409c43a080ebdfcb2f3)

June 11, 2026 20:33

[sjmonson](https://github.com/sjmonson)marked this pull request as ready for review

June 11, 2026 20:34


**approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Jun 11, 2026

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)
Collaborator


There was a problem hiding this comment.

Looks good to me. It's nice to see the reduced redundancy.

15 tasks

Collaborator
Author

|
|

Contributor

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

[mergify](https://github.com/apps/mergify)Bot pushed a commit that referenced this pull request

Jun 17, 2026

Depends on[#788]## TODO Remaining items on this PR (in increasing priority) ### Tier 0 - [x] Fix tests - [x] Fully replace all references to `BenchmarkGenerativeText` - [x] Cleanup commits ### Tier 1 - [x] Fix built-in scenarios - [x] Adapter for multi-benchmark (overrides) to fall back to multi-rate ### Tier 2 - [ ] Cleanup field and model documentation - [ ] Update documentation with new format - [ ] Wire up metadata labels (per[#728]) ### Tier 3 - [ ] Add new CLI: `guidellm config` - [ ] Add new CLI: `guidellm explain` - [ ] Support for config layering. I.e. `guidellm run -c config_builtin -c my_custom.yaml --backend ...` - [ ] Migrate `guidellm benchmark from-file` to use new format ## Summary Implements the new internal format and `guidellm run` based off of[#724]. ## Details TODO ## Test Plan TODO ## Related Issues - Related to[#724]--- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [x] Includes code generated or substantially modified by an AI agent - [x] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- # git log commit[Author: Samuel Monson <smonson@redhat.com> Date: Thu Jun 4 15:40:27 2026 -0400 Rework entrypoint arguments spec Assisted-by: GitHub Copilot GPT-4.1 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]b6aecd2[Author: Samuel Monson <smonson@redhat.com> Date: Fri Jun 5 15:54:02 2026 -0400 Add a basic template for new run CLI Signed-off-by: Samuel Monson <smonson@redhat.com> commit]3fed00c[Author: Samuel Monson <smonson@redhat.com> Date: Fri Jun 12 14:11:40 2026 -0400 Explicitly lock typing-extensions We already use this a bunch of places and its currently pulled in implicitly so just switch it to explicitly required. Signed-off-by: Samuel Monson <smonson@redhat.com> commit]8a15a7d[Author: Samuel Monson <smonson@redhat.com> Date: Fri Jun 5 21:07:41 2026 +0000 Implement Pydantic -> click argument generation Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]3fd07c3[Author: Samuel Monson <smonson@redhat.com> Date: Fri Jun 12 14:18:40 2026 -0400 Move and improve Pydantic -> click error parsing Assisted-by: GitHub Copilot GPT-4.1 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]3c895b5[Author: Samuel Monson <smonson@redhat.com> Date: Fri Jun 12 19:28:10 2026 +0000 Detect field error name from argument_alias Signed-off-by: Samuel Monson <smonson@redhat.com> commit]76eb426[Author: Samuel Monson <smonson@redhat.com> Date: Fri Jun 12 16:44:16 2026 -0400 Attach new CLI to benchmark_generative_text Signed-off-by: Samuel Monson <smonson@redhat.com> commit]7bc150f[Author: Samuel Monson <smonson@redhat.com> Date: Fri Jun 5 15:03:47 2026 -0400 Update BenchmarkGenerativeTextArgs references Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]31932f2[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 15 16:58:48 2026 +0000 Move ProfileArgs to schemas Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]6a8cc64[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 15 11:00:39 2026 -0400 Clean up BenchmarkOutputArgs Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]548c7f6[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 15 17:13:11 2026 +0000 Fixup tests Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]346b91d[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 15 15:18:23 2026 -0400 Fix import ordering on nested pydantic registries Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]4cc2b94[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 15 15:19:41 2026 -0400 Fix e2e tests Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]3120b87[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 15 15:21:01 2026 -0400 Fix some typing issues Signed-off-by: Samuel Monson <smonson@redhat.com> commit]22d5913[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 15 18:44:58 2026 -0400 Bump some e2e timeouts Signed-off-by: Samuel Monson <smonson@redhat.com> commit]759e0dc[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 15 18:51:02 2026 -0400 Fix for buggy mypy Signed-off-by: Samuel Monson <smonson@redhat.com> commit]3d376cf[Author: Samuel Monson <smonson@redhat.com> Date: Tue Jun 16 17:25:58 2026 +0000 Hack to support multi-rate Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]20f3d08[Author: Samuel Monson <smonson@redhat.com> Date: Tue Jun 16 15:49:34 2026 -0400 Fix builtin scenarios Signed-off-by: Samuel Monson <smonson@redhat.com> commit]1b65bbf[Author: Samuel Monson <smonson@redhat.com> Date: Wed Jun 17 11:19:07 2026 -0400 Fix outputs default Signed-off-by: Samuel Monson <smonson@redhat.com> --------- Assisted-by: GitHub Copilot GPT-4.1 Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com>]e6fdcfe

[SkiHatDuckie](https://github.com/SkiHatDuckie)pushed a commit to SkiHatDuckie/guidellm that referenced this pull request

Jun 23, 2026

Depends on[vllm-project#788]## TODO Remaining items on this PR (in increasing priority) ### Tier 0 - [x] Fix tests - [x] Fully replace all references to `BenchmarkGenerativeText` - [x] Cleanup commits ### Tier 1 - [x] Fix built-in scenarios - [x] Adapter for multi-benchmark (overrides) to fall back to multi-rate ### Tier 2 - [ ] Cleanup field and model documentation - [ ] Update documentation with new format - [ ] Wire up metadata labels (per[vllm-project#728]) ### Tier 3 - [ ] Add new CLI: `guidellm config` - [ ] Add new CLI: `guidellm explain` - [ ] Support for config layering. I.e. `guidellm run -c config_builtin -c my_custom.yaml --backend ...` - [ ] Migrate `guidellm benchmark from-file` to use new format ## Summary Implements the new internal format and `guidellm run` based off of[vllm-project#724]. ## Details TODO ## Test Plan TODO ## Related Issues - Related to[vllm-project#724]--- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [x] Includes code generated or substantially modified by an AI agent - [x] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- # git log commit[Author: Samuel Monson <smonson@redhat.com> Date: Thu Jun 4 15:40:27 2026 -0400 Rework entrypoint arguments spec Assisted-by: GitHub Copilot GPT-4.1 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]b6aecd2[Author: Samuel Monson <smonson@redhat.com> Date: Fri Jun 5 15:54:02 2026 -0400 Add a basic template for new run CLI Signed-off-by: Samuel Monson <smonson@redhat.com> commit]3fed00c[Author: Samuel Monson <smonson@redhat.com> Date: Fri Jun 12 14:11:40 2026 -0400 Explicitly lock typing-extensions We already use this a bunch of places and its currently pulled in implicitly so just switch it to explicitly required. Signed-off-by: Samuel Monson <smonson@redhat.com> commit]8a15a7d[Author: Samuel Monson <smonson@redhat.com> Date: Fri Jun 5 21:07:41 2026 +0000 Implement Pydantic -> click argument generation Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]3fd07c3[Author: Samuel Monson <smonson@redhat.com> Date: Fri Jun 12 14:18:40 2026 -0400 Move and improve Pydantic -> click error parsing Assisted-by: GitHub Copilot GPT-4.1 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]3c895b5[Author: Samuel Monson <smonson@redhat.com> Date: Fri Jun 12 19:28:10 2026 +0000 Detect field error name from argument_alias Signed-off-by: Samuel Monson <smonson@redhat.com> commit]76eb426[Author: Samuel Monson <smonson@redhat.com> Date: Fri Jun 12 16:44:16 2026 -0400 Attach new CLI to benchmark_generative_text Signed-off-by: Samuel Monson <smonson@redhat.com> commit]7bc150f[Author: Samuel Monson <smonson@redhat.com> Date: Fri Jun 5 15:03:47 2026 -0400 Update BenchmarkGenerativeTextArgs references Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]31932f2[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 15 16:58:48 2026 +0000 Move ProfileArgs to schemas Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]6a8cc64[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 15 11:00:39 2026 -0400 Clean up BenchmarkOutputArgs Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]548c7f6[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 15 17:13:11 2026 +0000 Fixup tests Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]346b91d[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 15 15:18:23 2026 -0400 Fix import ordering on nested pydantic registries Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]4cc2b94[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 15 15:19:41 2026 -0400 Fix e2e tests Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]3120b87[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 15 15:21:01 2026 -0400 Fix some typing issues Signed-off-by: Samuel Monson <smonson@redhat.com> commit]22d5913[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 15 18:44:58 2026 -0400 Bump some e2e timeouts Signed-off-by: Samuel Monson <smonson@redhat.com> commit]759e0dc[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 15 18:51:02 2026 -0400 Fix for buggy mypy Signed-off-by: Samuel Monson <smonson@redhat.com> commit]3d376cf[Author: Samuel Monson <smonson@redhat.com> Date: Tue Jun 16 17:25:58 2026 +0000 Hack to support multi-rate Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]20f3d08[Author: Samuel Monson <smonson@redhat.com> Date: Tue Jun 16 15:49:34 2026 -0400 Fix builtin scenarios Signed-off-by: Samuel Monson <smonson@redhat.com> commit]1b65bbf[Author: Samuel Monson <smonson@redhat.com> Date: Wed Jun 17 11:19:07 2026 -0400 Fix outputs default Signed-off-by: Samuel Monson <smonson@redhat.com> --------- Assisted-by: GitHub Copilot GPT-4.1 Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com>]e6fdcfe

[SkiHatDuckie](https://github.com/SkiHatDuckie)pushed a commit to SkiHatDuckie/guidellm that referenced this pull request

Jun 24, 2026

Depends on[vllm-project#788]## TODO Remaining items on this PR (in increasing priority) ### Tier 0 - [x] Fix tests - [x] Fully replace all references to `BenchmarkGenerativeText` - [x] Cleanup commits ### Tier 1 - [x] Fix built-in scenarios - [x] Adapter for multi-benchmark (overrides) to fall back to multi-rate ### Tier 2 - [ ] Cleanup field and model documentation - [ ] Update documentation with new format - [ ] Wire up metadata labels (per[vllm-project#728]) ### Tier 3 - [ ] Add new CLI: `guidellm config` - [ ] Add new CLI: `guidellm explain` - [ ] Support for config layering. I.e. `guidellm run -c config_builtin -c my_custom.yaml --backend ...` - [ ] Migrate `guidellm benchmark from-file` to use new format ## Summary Implements the new internal format and `guidellm run` based off of[vllm-project#724]. ## Details TODO ## Test Plan TODO ## Related Issues - Related to[vllm-project#724]--- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [x] Includes code generated or substantially modified by an AI agent - [x] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- # git log commit[Author: Samuel Monson <smonson@redhat.com> Date: Thu Jun 4 15:40:27 2026 -0400 Rework entrypoint arguments spec Assisted-by: GitHub Copilot GPT-4.1 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]b6aecd2[Author: Samuel Monson <smonson@redhat.com> Date: Fri Jun 5 15:54:02 2026 -0400 Add a basic template for new run CLI Signed-off-by: Samuel Monson <smonson@redhat.com> commit]3fed00c[Author: Samuel Monson <smonson@redhat.com> Date: Fri Jun 12 14:11:40 2026 -0400 Explicitly lock typing-extensions We already use this a bunch of places and its currently pulled in implicitly so just switch it to explicitly required. Signed-off-by: Samuel Monson <smonson@redhat.com> commit]8a15a7d[Author: Samuel Monson <smonson@redhat.com> Date: Fri Jun 5 21:07:41 2026 +0000 Implement Pydantic -> click argument generation Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]3fd07c3[Author: Samuel Monson <smonson@redhat.com> Date: Fri Jun 12 14:18:40 2026 -0400 Move and improve Pydantic -> click error parsing Assisted-by: GitHub Copilot GPT-4.1 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]3c895b5[Author: Samuel Monson <smonson@redhat.com> Date: Fri Jun 12 19:28:10 2026 +0000 Detect field error name from argument_alias Signed-off-by: Samuel Monson <smonson@redhat.com> commit]76eb426[Author: Samuel Monson <smonson@redhat.com> Date: Fri Jun 12 16:44:16 2026 -0400 Attach new CLI to benchmark_generative_text Signed-off-by: Samuel Monson <smonson@redhat.com> commit]7bc150f[Author: Samuel Monson <smonson@redhat.com> Date: Fri Jun 5 15:03:47 2026 -0400 Update BenchmarkGenerativeTextArgs references Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]31932f2[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 15 16:58:48 2026 +0000 Move ProfileArgs to schemas Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]6a8cc64[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 15 11:00:39 2026 -0400 Clean up BenchmarkOutputArgs Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]548c7f6[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 15 17:13:11 2026 +0000 Fixup tests Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]346b91d[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 15 15:18:23 2026 -0400 Fix import ordering on nested pydantic registries Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]4cc2b94[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 15 15:19:41 2026 -0400 Fix e2e tests Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]3120b87[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 15 15:21:01 2026 -0400 Fix some typing issues Signed-off-by: Samuel Monson <smonson@redhat.com> commit]22d5913[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 15 18:44:58 2026 -0400 Bump some e2e timeouts Signed-off-by: Samuel Monson <smonson@redhat.com> commit]759e0dc[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 15 18:51:02 2026 -0400 Fix for buggy mypy Signed-off-by: Samuel Monson <smonson@redhat.com> commit]3d376cf[Author: Samuel Monson <smonson@redhat.com> Date: Tue Jun 16 17:25:58 2026 +0000 Hack to support multi-rate Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]20f3d08[Author: Samuel Monson <smonson@redhat.com> Date: Tue Jun 16 15:49:34 2026 -0400 Fix builtin scenarios Signed-off-by: Samuel Monson <smonson@redhat.com> commit]1b65bbf[Author: Samuel Monson <smonson@redhat.com> Date: Wed Jun 17 11:19:07 2026 -0400 Fix outputs default Signed-off-by: Samuel Monson <smonson@redhat.com> --------- Assisted-by: GitHub Copilot GPT-4.1 Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com>]e6fdcfe

[SkiHatDuckie](https://github.com/SkiHatDuckie)pushed a commit to SkiHatDuckie/guidellm that referenced this pull request

Jul 6, 2026

Depends on[vllm-project#788]## TODO Remaining items on this PR (in increasing priority) ### Tier 0 - [x] Fix tests - [x] Fully replace all references to `BenchmarkGenerativeText` - [x] Cleanup commits ### Tier 1 - [x] Fix built-in scenarios - [x] Adapter for multi-benchmark (overrides) to fall back to multi-rate ### Tier 2 - [ ] Cleanup field and model documentation - [ ] Update documentation with new format - [ ] Wire up metadata labels (per[vllm-project#728]) ### Tier 3 - [ ] Add new CLI: `guidellm config` - [ ] Add new CLI: `guidellm explain` - [ ] Support for config layering. I.e. `guidellm run -c config_builtin -c my_custom.yaml --backend ...` - [ ] Migrate `guidellm benchmark from-file` to use new format ## Summary Implements the new internal format and `guidellm run` based off of[vllm-project#724]. ## Details TODO ## Test Plan TODO ## Related Issues - Related to[vllm-project#724]--- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [x] Includes code generated or substantially modified by an AI agent - [x] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- # git log commit[Author: Samuel Monson <smonson@redhat.com> Date: Thu Jun 4 15:40:27 2026 -0400 Rework entrypoint arguments spec Assisted-by: GitHub Copilot GPT-4.1 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]b6aecd2[Author: Samuel Monson <smonson@redhat.com> Date: Fri Jun 5 15:54:02 2026 -0400 Add a basic template for new run CLI Signed-off-by: Samuel Monson <smonson@redhat.com> commit]3fed00c[Author: Samuel Monson <smonson@redhat.com> Date: Fri Jun 12 14:11:40 2026 -0400 Explicitly lock typing-extensions We already use this a bunch of places and its currently pulled in implicitly so just switch it to explicitly required. Signed-off-by: Samuel Monson <smonson@redhat.com> commit]8a15a7d[Author: Samuel Monson <smonson@redhat.com> Date: Fri Jun 5 21:07:41 2026 +0000 Implement Pydantic -> click argument generation Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]3fd07c3[Author: Samuel Monson <smonson@redhat.com> Date: Fri Jun 12 14:18:40 2026 -0400 Move and improve Pydantic -> click error parsing Assisted-by: GitHub Copilot GPT-4.1 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]3c895b5[Author: Samuel Monson <smonson@redhat.com> Date: Fri Jun 12 19:28:10 2026 +0000 Detect field error name from argument_alias Signed-off-by: Samuel Monson <smonson@redhat.com> commit]76eb426[Author: Samuel Monson <smonson@redhat.com> Date: Fri Jun 12 16:44:16 2026 -0400 Attach new CLI to benchmark_generative_text Signed-off-by: Samuel Monson <smonson@redhat.com> commit]7bc150f[Author: Samuel Monson <smonson@redhat.com> Date: Fri Jun 5 15:03:47 2026 -0400 Update BenchmarkGenerativeTextArgs references Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]31932f2[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 15 16:58:48 2026 +0000 Move ProfileArgs to schemas Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]6a8cc64[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 15 11:00:39 2026 -0400 Clean up BenchmarkOutputArgs Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]548c7f6[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 15 17:13:11 2026 +0000 Fixup tests Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]346b91d[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 15 15:18:23 2026 -0400 Fix import ordering on nested pydantic registries Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]4cc2b94[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 15 15:19:41 2026 -0400 Fix e2e tests Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]3120b87[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 15 15:21:01 2026 -0400 Fix some typing issues Signed-off-by: Samuel Monson <smonson@redhat.com> commit]22d5913[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 15 18:44:58 2026 -0400 Bump some e2e timeouts Signed-off-by: Samuel Monson <smonson@redhat.com> commit]759e0dc[Author: Samuel Monson <smonson@redhat.com> Date: Mon Jun 15 18:51:02 2026 -0400 Fix for buggy mypy Signed-off-by: Samuel Monson <smonson@redhat.com> commit]3d376cf[Author: Samuel Monson <smonson@redhat.com> Date: Tue Jun 16 17:25:58 2026 +0000 Hack to support multi-rate Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com> commit]20f3d08[Author: Samuel Monson <smonson@redhat.com> Date: Tue Jun 16 15:49:34 2026 -0400 Fix builtin scenarios Signed-off-by: Samuel Monson <smonson@redhat.com> commit]1b65bbf[Author: Samuel Monson <smonson@redhat.com> Date: Wed Jun 17 11:19:07 2026 -0400 Fix outputs default Signed-off-by: Samuel Monson <smonson@redhat.com> --------- Assisted-by: GitHub Copilot GPT-4.1 Generated-by: claude-code Opus 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com>]e6fdcfe

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

`benchmark/schema`

module## Use of AI

## git log

commit

b080739Author: Samuel Monson smonson@redhat.com

Date: Thu Jun 4 14:55:41 2026 -0400

commit

f48c5edAuthor: Samuel Monson smonson@redhat.com

Date: Fri Jun 5 14:59:11 2026 -0400

commit

2ffffa8Author: Samuel Monson smonson@redhat.com

Date: Thu Jun 4 19:29:35 2026 +0000

commit

dcf20a0Author: Samuel Monson smonson@redhat.com

Date: Thu Jun 11 15:47:01 2026 -0400

Assisted-by: GitHub Copilot GPT-4.1

Generated-by: claude-code Opus 4.6

Signed-off-by: Samuel Monson smonson@redhat.com