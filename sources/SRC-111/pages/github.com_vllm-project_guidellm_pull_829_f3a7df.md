source: https://github.com/vllm-project/guidellm/pull/829

# Trace File Refactor - #829

## Conversation

|
Hi |

|
Sorry, messed up the rebase. Give me a minute while I clean up the history. |

[SkiHatDuckie](https://github.com/SkiHatDuckie)

[force-pushed](https://github.com/vllm-project/guidellm/compare/52e2b60abc595fa155ff41e0a998154cceb8c6aa..7a1e3c5b3708ee7ca320f5a9f4034432a0107e94)the trace-merge branch from

[to](https://github.com/vllm-project/guidellm/commit/52e2b60abc595fa155ff41e0a998154cceb8c6aa)

`52e2b60`


`7a1e3c5`

[Compare](https://github.com/vllm-project/guidellm/compare/52e2b60abc595fa155ff41e0a998154cceb8c6aa..7a1e3c5b3708ee7ca320f5a9f4034432a0107e94)

June 23, 2026 21:02


**reviewed**

[dbutenhof](https://github.com/dbutenhof)Jun 23, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

Just logging a few doc comments I caught in a quick scan. I'll get to the code tomorrow morning...

[docs/getting-started/benchmark.md](https://github.com/vllm-project/guidellm/pull/829/files#diff-814d89ed16bd4644a4a05515d85d58e412ef428e6611c8e4fff8c3b667947dc2)Outdated

[docs/getting-started/benchmark.md](https://github.com/vllm-project/guidellm/pull/829/files#diff-814d89ed16bd4644a4a05515d85d58e412ef428e6611c8e4fff8c3b667947dc2)Outdated

[docs/getting-started/benchmark.md](https://github.com/vllm-project/guidellm/pull/829/files#diff-814d89ed16bd4644a4a05515d85d58e412ef428e6611c8e4fff8c3b667947dc2)Outdated

[docs/guides/datasets.md](https://github.com/vllm-project/guidellm/pull/829/files#diff-25d387359ef26d847e440becb4ffc0825e3dbf562df2d7e5b3cc1d49b1e6a43e)Outdated

[docs/guides/datasets.md](https://github.com/vllm-project/guidellm/pull/829/files#diff-25d387359ef26d847e440becb4ffc0825e3dbf562df2d7e5b3cc1d49b1e6a43e)Outdated

[docs/guides/trace_file_formats.md](https://github.com/vllm-project/guidellm/pull/829/files#diff-2a281a5e77aa41f08b23c97ebb20fb506fb5ce01cba47653bf0574dcf0233114)Outdated

[docs/guides/trace_file_formats.md](https://github.com/vllm-project/guidellm/pull/829/files#diff-2a281a5e77aa41f08b23c97ebb20fb506fb5ce01cba47653bf0574dcf0233114)Outdated

[docs/guides/trace_file_formats.md](https://github.com/vllm-project/guidellm/pull/829/files#diff-2a281a5e77aa41f08b23c97ebb20fb506fb5ce01cba47653bf0574dcf0233114)Outdated

|
Hi |

[SkiHatDuckie](https://github.com/SkiHatDuckie)

[force-pushed](https://github.com/vllm-project/guidellm/compare/3aab3ac07b040cc050aad2ed043c4213c22b8c95..283cfff6c90765b539ea67e3aa75b3cb10cbb2d5)the trace-merge branch from

[to](https://github.com/vllm-project/guidellm/commit/3aab3ac07b040cc050aad2ed043c4213c22b8c95)

`3aab3ac`


`283cfff`

[Compare](https://github.com/vllm-project/guidellm/compare/3aab3ac07b040cc050aad2ed043c4213c22b8c95..283cfff6c90765b539ea67e3aa75b3cb10cbb2d5)

June 24, 2026 13:52

|
Congrats on breaking the |

[mergify](https://github.com/apps/mergify)Bot pushed a commit that referenced this pull request

Jun 25, 2026

[…#855]) ## Summary This is a separate PR for the bug fix contained in[#829], if we instead wish to just get the bug fix in for v0.7.0. This will be closed if the trace file refactor is merged, or after the release of v0.7.0. ## Details - Fixed a bug with Mooncake format not working with multiprocessing ## Related Issues - This is also fixed with[#829]--- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [ ] Includes code generated or substantially modified by an AI agent - [ ] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- # git log commit[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Thu Jun 25 11:54:24 2026 -0400 Hotfix: Add relative_timestamp column to output in Mooncake deserializer Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]3b89ec2[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Thu Jun 25 12:59:10 2026 -0400 Move `timestamps` outside the loop Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> --------- Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>]8d2cba0


**reviewed**

[sjmonson](https://github.com/sjmonson)Jun 29, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)

There was a problem hiding this comment.

My bad, meant to post this morning. This PR also needs another rebase (hopefully the last one) and also some tests are failing.

[src/guidellm/data/deserializers/trace_common.py](https://github.com/vllm-project/guidellm/pull/829/files#diff-9d2c1103f2619806501e3c62df0a9871188fe22415a2dc5a8875e7855b5e2a8c)Outdated

Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>

Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>

Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>

Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>

Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>

Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>

Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>

Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>

Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>

Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>

Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>

Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>

Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>

Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>

Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>

Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>

Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>

Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>

Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>

Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>

Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>

Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>

Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>


**requested changes**

[sjmonson](https://github.com/sjmonson)Jun 30, 2026

[src/guidellm/data/deserializers/trace_minimal.py](https://github.com/vllm-project/guidellm/pull/829/files/f32a01ec1300724df7e11d3236b5c9ca3d811f00#diff-210024703b902d346a589025f019771314cd5f09d39b74a850fc920606e81629)Outdated

Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>

[SkiHatDuckie](https://github.com/SkiHatDuckie)marked this pull request as draft

June 30, 2026 15:59


**reviewed**

[dbutenhof](https://github.com/dbutenhof)Jun 30, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

There's a broken .md link after you renamed a header: that should be fixed. I don't think any of the other comments are pressing...

[docs/getting-started/benchmark.md](https://github.com/vllm-project/guidellm/pull/829/files/9edb490c939d03768369148061d208adb0d468c5#diff-814d89ed16bd4644a4a05515d85d58e412ef428e6611c8e4fff8c3b667947dc2)Outdated

[docs/getting-started/benchmark.md](https://github.com/vllm-project/guidellm/pull/829/files/9edb490c939d03768369148061d208adb0d468c5#diff-814d89ed16bd4644a4a05515d85d58e412ef428e6611c8e4fff8c3b667947dc2)Outdated

[src/guidellm/data/deserializers/trace_common.py](https://github.com/vllm-project/guidellm/pull/829/files/9edb490c939d03768369148061d208adb0d468c5#diff-9d2c1103f2619806501e3c62df0a9871188fe22415a2dc5a8875e7855b5e2a8c)Outdated

[src/guidellm/data/deserializers/trace_common.py](https://github.com/vllm-project/guidellm/pull/829/files/9edb490c939d03768369148061d208adb0d468c5#diff-9d2c1103f2619806501e3c62df0a9871188fe22415a2dc5a8875e7855b5e2a8c)

[src/guidellm/data/deserializers/trace_common.py](https://github.com/vllm-project/guidellm/pull/829/files/9edb490c939d03768369148061d208adb0d468c5#diff-9d2c1103f2619806501e3c62df0a9871188fe22415a2dc5a8875e7855b5e2a8c)Outdated

[src/guidellm/data/deserializers/trace_common.py](https://github.com/vllm-project/guidellm/pull/829/files/9edb490c939d03768369148061d208adb0d468c5#diff-9d2c1103f2619806501e3c62df0a9871188fe22415a2dc5a8875e7855b5e2a8c)Outdated

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)

There was a problem hiding this comment.

Looks ready for merging once Dave's comments are addressed.

Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>

[SkiHatDuckie](https://github.com/SkiHatDuckie)marked this pull request as ready for review

June 30, 2026 16:50

Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>

Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>

Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>

Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>


**approved these changes**

[sjmonson](https://github.com/sjmonson)Jun 30, 2026

|
Queued — the merge queue status continues in |


**approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Jun 30, 2026

## Merge Queue Status
This pull request spent ## Required conditions to merge
|


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Jun 30, 2026

[SkiHatDuckie](https://github.com/SkiHatDuckie)added a commit to SkiHatDuckie/guidellm that referenced this pull request

Jul 2, 2026

[…vllm-project#855]) ## Summary This is a separate PR for the bug fix contained in[vllm-project#829], if we instead wish to just get the bug fix in for v0.7.0. This will be closed if the trace file refactor is merged, or after the release of v0.7.0. ## Details - Fixed a bug with Mooncake format not working with multiprocessing ## Related Issues - This is also fixed with[vllm-project#829]--- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [ ] Includes code generated or substantially modified by an AI agent - [ ] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- # git log commit[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Thu Jun 25 11:54:24 2026 -0400 Hotfix: Add relative_timestamp column to output in Mooncake deserializer Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]3b89ec2[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Thu Jun 25 12:59:10 2026 -0400 Move `timestamps` outside the loop Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> --------- Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>]8d2cba0

[SkiHatDuckie](https://github.com/SkiHatDuckie)added a commit to SkiHatDuckie/guidellm that referenced this pull request

Jul 2, 2026

## Summary A refactoring of trace formats that separates format-agnostic trace replay functionality from format-specific functionality. Notably, all formats now work with the same dataset deserializer. Two abstract classes `TraceDataArgs` and `TraceFormatBase` are required to be implemented by all formats instead. Additional documentation has been added to better cover all supported trace formats and their different requirements. The unique prefixes for cache resistance found originally in `trace_synthetic.py` (now `trace_minimal.py`) was removed due to being incompatible with the new model. It may be re-added as a feature in future PRs through another means. ## Details - Added `trace_common.py` - All trace formats use the same `TraceDatasetDeserializer` - Moved commonly used functions such as `generate_token_ids` and `decode_prompt` to `trace_common.py` - Added `TraceDataArgs`: an abstract class inherited by all formats - Added `TraceFormatBase` and `TraceFormatRegistry`: defines an interface for format-specific requirements and functionality on top of `TraceExamplesIterable` - Replaced `TraceSyntheticDatasetDeserializer` and `TraceSyntheticDataArgs` with `MinimalTraceFormat` and `MinimalTraceFormatArgs` - Replaced `TraceMooncakeDatasetDeserializer` and `TraceMooncakeDataArgs` with `MooncakeTraceFormat` and `MooncakeTraceFormatArgs` - Renamed `trace_synthetic.py` -> `trace_minimal.py` - Renamed `test_trace_synthetic.py` -> `test_trace_minimal.py` - Added `test_trace_common.py`, and rearranged preexisting tests accordingly - Updated `test_replay_profile.py`, `test_trace_replay.py` and `test_trace_replay_multiprocess.py` - Fixed a bug with Mooncake format not working with multiprocessing - All trace formats now work with `IterableDataset` for streaming - Added documentation `trace_file_formats.md` to cover all trace formats supported by GuideLLM - Updated documentation in `getting_started/benchmark.md` and `guides/datasets.md` - Updated inline documentation - Updated import registry in `data/deserializers/__init__.py` - Moved common dataset validation checks to `load_trace_rows` - Removed unique prefixes for cache-resistance in `trace_minimal.py` ## Test Plan - `tox -e test-unit` - `tox -e test-integration` - `tox -e lint-check && tox -e type-check` ## Related Issues - Resolves[vllm-project#597]--- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [ ] Includes code generated or substantially modified by an AI agent - [ ] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- # git log commit[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Mon Jun 15 12:16:03 2026 -0400 Move dataset validation to load_trace_rows Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]027f439[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Mon Jun 15 13:00:51 2026 -0400 Rename `TraceColumn` in test file to `TraceColumnGenerator` Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]6ec92f5[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Mon Jun 15 15:11:25 2026 -0400 Add relative_timestamp column to deserialized dataset Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]76f43df[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Tue Jun 16 09:38:05 2026 -0400 Switch to streaming datasets for synthetic trace Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]d79be07[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Tue Jun 16 09:58:18 2026 -0400 Update docs Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]00ccea7[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Tue Jun 16 16:58:54 2026 -0400 Add trace_common.py + classes Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]7de32d6[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Wed Jun 17 10:57:16 2026 -0400 Repair broken test files Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]6f6e464[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Wed Jun 17 16:34:10 2026 -0400 Instantiate/Validate/Dispatch formats through TraceFormatArgs Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]9cd8729[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Thu Jun 18 15:09:33 2026 -0400 Rework format handling; flatten data args for CLI Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]26b740f[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Thu Jun 18 16:16:15 2026 -0400 Repair tests Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]7911a87[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Thu Jun 18 16:18:38 2026 -0400 Remove TraceDataset from __all__ Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]9aea389[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Thu Jun 18 16:25:29 2026 -0400 Move common funcs to trace_common Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]27687b2[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Mon Jun 22 11:04:41 2026 -0400 Add test_trace_common.py and rearrange tests Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]73b2eda[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Mon Jun 22 11:15:03 2026 -0400 Refactor test_trace_synthetic Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]2cdb3b8[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Mon Jun 22 11:28:35 2026 -0400 Rename trace_synthetic to trace_minimal Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]04626fe[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Mon Jun 22 11:49:30 2026 -0400 Improve text coverage Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]8f1ab50[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Mon Jun 22 12:20:30 2026 -0400 Update inline docs Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]dff58aa[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Mon Jun 22 16:12:02 2026 -0400 Update docs Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]342bd0c[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Mon Jun 22 16:17:20 2026 -0400 Cleanup linting & docs Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]37f3b10[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Wed Jun 24 10:07:04 2026 -0400 Spread `kind`ness Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]7bc2f96[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Wed Jun 24 10:47:16 2026 -0400 Update docs Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]e0fe688[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Wed Jun 24 11:31:31 2026 -0400 Fix: Register formats with deserializer Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]955a8f5[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Wed Jun 24 11:35:31 2026 -0400 Satisfy linting Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]8908132[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Thu Jun 25 13:00:26 2026 -0400 Move `timestamps` outside the loop Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]e344e80[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Mon Jun 29 17:16:23 2026 -0400 Register formats w/ deserializer outside trace_common Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]1e842a4[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Mon Jun 29 17:20:50 2026 -0400 Update TraceDataArgs Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]f68217f[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Mon Jun 29 17:50:56 2026 -0400 Move trace_io contents to trace_common Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]73617d1[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Tue Jun 30 08:59:31 2026 -0400 Fix typo Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]d6f0e67[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Tue Jun 30 10:04:58 2026 -0400 Remove TraceColumn Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]9dd48e4[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Tue Jun 30 10:17:55 2026 -0400 Specify bad path reason Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]f32a01e[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Tue Jun 30 10:29:43 2026 -0400 Add comment to create_prompt Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]5c51338[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Tue Jun 30 10:35:10 2026 -0400 Re-register trace_minimal as trace_synthetic Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]9edb490[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Tue Jun 30 12:50:13 2026 -0400 Support more filetypes + update docs Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]9a2c7c1[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Tue Jun 30 12:57:04 2026 -0400 Rename trace_file_formats.md to trace_replay.md Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]8346b53[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Tue Jun 30 13:04:58 2026 -0400 Make margin_of_safety an optional parameter Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]2741e11[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Tue Jun 30 13:07:47 2026 -0400 Update exception msgs Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]5b955d1[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Tue Jun 30 13:10:04 2026 -0400 Update exception msgs x2 Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> --------- Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>]00efe7b

[SkiHatDuckie](https://github.com/SkiHatDuckie)added a commit to SkiHatDuckie/guidellm that referenced this pull request

Jul 6, 2026

[…vllm-project#855]) ## Summary This is a separate PR for the bug fix contained in[vllm-project#829], if we instead wish to just get the bug fix in for v0.7.0. This will be closed if the trace file refactor is merged, or after the release of v0.7.0. ## Details - Fixed a bug with Mooncake format not working with multiprocessing ## Related Issues - This is also fixed with[vllm-project#829]--- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [ ] Includes code generated or substantially modified by an AI agent - [ ] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- # git log commit[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Thu Jun 25 11:54:24 2026 -0400 Hotfix: Add relative_timestamp column to output in Mooncake deserializer Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]3b89ec2[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Thu Jun 25 12:59:10 2026 -0400 Move `timestamps` outside the loop Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> --------- Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>]8d2cba0

[SkiHatDuckie](https://github.com/SkiHatDuckie)added a commit to SkiHatDuckie/guidellm that referenced this pull request

Jul 6, 2026

## Summary A refactoring of trace formats that separates format-agnostic trace replay functionality from format-specific functionality. Notably, all formats now work with the same dataset deserializer. Two abstract classes `TraceDataArgs` and `TraceFormatBase` are required to be implemented by all formats instead. Additional documentation has been added to better cover all supported trace formats and their different requirements. The unique prefixes for cache resistance found originally in `trace_synthetic.py` (now `trace_minimal.py`) was removed due to being incompatible with the new model. It may be re-added as a feature in future PRs through another means. ## Details - Added `trace_common.py` - All trace formats use the same `TraceDatasetDeserializer` - Moved commonly used functions such as `generate_token_ids` and `decode_prompt` to `trace_common.py` - Added `TraceDataArgs`: an abstract class inherited by all formats - Added `TraceFormatBase` and `TraceFormatRegistry`: defines an interface for format-specific requirements and functionality on top of `TraceExamplesIterable` - Replaced `TraceSyntheticDatasetDeserializer` and `TraceSyntheticDataArgs` with `MinimalTraceFormat` and `MinimalTraceFormatArgs` - Replaced `TraceMooncakeDatasetDeserializer` and `TraceMooncakeDataArgs` with `MooncakeTraceFormat` and `MooncakeTraceFormatArgs` - Renamed `trace_synthetic.py` -> `trace_minimal.py` - Renamed `test_trace_synthetic.py` -> `test_trace_minimal.py` - Added `test_trace_common.py`, and rearranged preexisting tests accordingly - Updated `test_replay_profile.py`, `test_trace_replay.py` and `test_trace_replay_multiprocess.py` - Fixed a bug with Mooncake format not working with multiprocessing - All trace formats now work with `IterableDataset` for streaming - Added documentation `trace_file_formats.md` to cover all trace formats supported by GuideLLM - Updated documentation in `getting_started/benchmark.md` and `guides/datasets.md` - Updated inline documentation - Updated import registry in `data/deserializers/__init__.py` - Moved common dataset validation checks to `load_trace_rows` - Removed unique prefixes for cache-resistance in `trace_minimal.py` ## Test Plan - `tox -e test-unit` - `tox -e test-integration` - `tox -e lint-check && tox -e type-check` ## Related Issues - Resolves[vllm-project#597]--- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [ ] Includes code generated or substantially modified by an AI agent - [ ] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- # git log commit[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Mon Jun 15 12:16:03 2026 -0400 Move dataset validation to load_trace_rows Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]027f439[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Mon Jun 15 13:00:51 2026 -0400 Rename `TraceColumn` in test file to `TraceColumnGenerator` Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]6ec92f5[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Mon Jun 15 15:11:25 2026 -0400 Add relative_timestamp column to deserialized dataset Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]76f43df[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Tue Jun 16 09:38:05 2026 -0400 Switch to streaming datasets for synthetic trace Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]d79be07[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Tue Jun 16 09:58:18 2026 -0400 Update docs Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]00ccea7[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Tue Jun 16 16:58:54 2026 -0400 Add trace_common.py + classes Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]7de32d6[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Wed Jun 17 10:57:16 2026 -0400 Repair broken test files Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]6f6e464[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Wed Jun 17 16:34:10 2026 -0400 Instantiate/Validate/Dispatch formats through TraceFormatArgs Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]9cd8729[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Thu Jun 18 15:09:33 2026 -0400 Rework format handling; flatten data args for CLI Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]26b740f[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Thu Jun 18 16:16:15 2026 -0400 Repair tests Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]7911a87[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Thu Jun 18 16:18:38 2026 -0400 Remove TraceDataset from __all__ Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]9aea389[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Thu Jun 18 16:25:29 2026 -0400 Move common funcs to trace_common Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]27687b2[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Mon Jun 22 11:04:41 2026 -0400 Add test_trace_common.py and rearrange tests Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]73b2eda[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Mon Jun 22 11:15:03 2026 -0400 Refactor test_trace_synthetic Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]2cdb3b8[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Mon Jun 22 11:28:35 2026 -0400 Rename trace_synthetic to trace_minimal Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]04626fe[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Mon Jun 22 11:49:30 2026 -0400 Improve text coverage Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]8f1ab50[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Mon Jun 22 12:20:30 2026 -0400 Update inline docs Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]dff58aa[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Mon Jun 22 16:12:02 2026 -0400 Update docs Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]342bd0c[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Mon Jun 22 16:17:20 2026 -0400 Cleanup linting & docs Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]37f3b10[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Wed Jun 24 10:07:04 2026 -0400 Spread `kind`ness Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]7bc2f96[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Wed Jun 24 10:47:16 2026 -0400 Update docs Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]e0fe688[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Wed Jun 24 11:31:31 2026 -0400 Fix: Register formats with deserializer Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]955a8f5[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Wed Jun 24 11:35:31 2026 -0400 Satisfy linting Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]8908132[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Thu Jun 25 13:00:26 2026 -0400 Move `timestamps` outside the loop Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]e344e80[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Mon Jun 29 17:16:23 2026 -0400 Register formats w/ deserializer outside trace_common Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]1e842a4[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Mon Jun 29 17:20:50 2026 -0400 Update TraceDataArgs Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]f68217f[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Mon Jun 29 17:50:56 2026 -0400 Move trace_io contents to trace_common Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]73617d1[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Tue Jun 30 08:59:31 2026 -0400 Fix typo Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]d6f0e67[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Tue Jun 30 10:04:58 2026 -0400 Remove TraceColumn Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]9dd48e4[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Tue Jun 30 10:17:55 2026 -0400 Specify bad path reason Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]f32a01e[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Tue Jun 30 10:29:43 2026 -0400 Add comment to create_prompt Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]5c51338[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Tue Jun 30 10:35:10 2026 -0400 Re-register trace_minimal as trace_synthetic Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]9edb490[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Tue Jun 30 12:50:13 2026 -0400 Support more filetypes + update docs Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]9a2c7c1[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Tue Jun 30 12:57:04 2026 -0400 Rename trace_file_formats.md to trace_replay.md Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]8346b53[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Tue Jun 30 13:04:58 2026 -0400 Make margin_of_safety an optional parameter Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]2741e11[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Tue Jun 30 13:07:47 2026 -0400 Update exception msgs Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> commit]5b955d1[Author: SkiHatDuckie <SkiHatDuckie@gmail.com> Date: Tue Jun 30 13:10:04 2026 -0400 Update exception msgs x2 Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com> --------- Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>]00efe7b

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

## Summary

A refactoring of trace formats that separates format-agnostic trace replay functionality from format-specific functionality. Notably, all formats now work with the same dataset deserializer. Two abstract classes

`TraceDataArgs`

and`TraceFormatBase`

are required to be implemented by all formats instead.Additional documentation has been added to better cover all supported trace formats and their different requirements.

The unique prefixes for cache resistance found originally in

`trace_synthetic.py`

(now`trace_minimal.py`

) was removed due to being incompatible with the new model. It may be re-added as a feature in future PRs through another means.## Details

`trace_common.py`

`TraceDatasetDeserializer`

`generate_token_ids`

and`decode_prompt`

to`trace_common.py`

`TraceDataArgs`

: an abstract class inherited by all formats`TraceFormatBase`

and`TraceFormatRegistry`

: defines an interface for format-specific requirements and functionality on top of`TraceExamplesIterable`

`TraceSyntheticDatasetDeserializer`

and`TraceSyntheticDataArgs`

with`MinimalTraceFormat`

and`MinimalTraceFormatArgs`

`TraceMooncakeDatasetDeserializer`

and`TraceMooncakeDataArgs`

with`MooncakeTraceFormat`

and`MooncakeTraceFormatArgs`

`trace_synthetic.py`

->`trace_minimal.py`

`test_trace_synthetic.py`

->`test_trace_minimal.py`

`test_trace_common.py`

, and rearranged preexisting tests accordingly`test_replay_profile.py`

,`test_trace_replay.py`

and`test_trace_replay_multiprocess.py`

`IterableDataset`

for streaming`trace_file_formats.md`

to cover all trace formats supported by GuideLLM`getting_started/benchmark.md`

and`guides/datasets.md`

`data/deserializers/__init__.py`

`load_trace_rows`

`trace_minimal.py`

## Test Plan

`tox -e test-unit`

`tox -e test-integration`

`tox -e lint-check && tox -e type-check`

## Related Issues

## Use of AI

## git log

commit

027f439Author: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Mon Jun 15 12:16:03 2026 -0400

commit

6ec92f5Author: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Mon Jun 15 13:00:51 2026 -0400

commit

76f43dfAuthor: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Mon Jun 15 15:11:25 2026 -0400

commit

d79be07Author: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Tue Jun 16 09:38:05 2026 -0400

commit

00ccea7Author: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Tue Jun 16 09:58:18 2026 -0400

commit

7de32d6Author: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Tue Jun 16 16:58:54 2026 -0400

commit

6f6e464Author: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Wed Jun 17 10:57:16 2026 -0400

commit

9cd8729Author: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Wed Jun 17 16:34:10 2026 -0400

commit

26b740fAuthor: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Thu Jun 18 15:09:33 2026 -0400

commit

7911a87Author: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Thu Jun 18 16:16:15 2026 -0400

commit

9aea389Author: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Thu Jun 18 16:18:38 2026 -0400

commit

27687b2Author: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Thu Jun 18 16:25:29 2026 -0400

commit

73b2edaAuthor: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Mon Jun 22 11:04:41 2026 -0400

commit

2cdb3b8Author: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Mon Jun 22 11:15:03 2026 -0400

commit

04626feAuthor: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Mon Jun 22 11:28:35 2026 -0400

commit

8f1ab50Author: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Mon Jun 22 11:49:30 2026 -0400

commit

dff58aaAuthor: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Mon Jun 22 12:20:30 2026 -0400

commit

342bd0cAuthor: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Mon Jun 22 16:12:02 2026 -0400

commit

37f3b10Author: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Mon Jun 22 16:17:20 2026 -0400

commit

7bc2f96Author: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Wed Jun 24 10:07:04 2026 -0400

commit

e0fe688Author: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Wed Jun 24 10:47:16 2026 -0400

commit

955a8f5Author: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Wed Jun 24 11:31:31 2026 -0400

commit

8908132Author: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Wed Jun 24 11:35:31 2026 -0400

commit

e344e80Author: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Thu Jun 25 13:00:26 2026 -0400

commit

1e842a4Author: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Mon Jun 29 17:16:23 2026 -0400

commit

f68217fAuthor: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Mon Jun 29 17:20:50 2026 -0400

commit

73617d1Author: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Mon Jun 29 17:50:56 2026 -0400

commit

d6f0e67Author: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Tue Jun 30 08:59:31 2026 -0400

commit

9dd48e4Author: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Tue Jun 30 10:04:58 2026 -0400

commit

f32a01eAuthor: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Tue Jun 30 10:17:55 2026 -0400

commit

5c51338Author: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Tue Jun 30 10:29:43 2026 -0400

commit

9edb490Author: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Tue Jun 30 10:35:10 2026 -0400

commit

9a2c7c1Author: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Tue Jun 30 12:50:13 2026 -0400

commit

8346b53Author: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Tue Jun 30 12:57:04 2026 -0400

commit

2741e11Author: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Tue Jun 30 13:04:58 2026 -0400

commit

5b955d1Author: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Tue Jun 30 13:07:47 2026 -0400

commit

00efe7bAuthor: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Tue Jun 30 13:10:04 2026 -0400

Signed-off-by: SkiHatDuckie SkiHatDuckie@gmail.com