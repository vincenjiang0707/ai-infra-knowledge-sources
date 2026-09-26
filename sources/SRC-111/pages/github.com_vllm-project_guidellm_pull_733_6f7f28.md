source: https://github.com/vllm-project/guidellm/pull/733

# [v0.7 CLI Refactor] Rework Data Deserialization Config - #733

## Conversation


**reviewed**

[dbutenhof](https://github.com/dbutenhof)May 19, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

Wow. Lots of changes, but a few repeating patterns. I think the new patterns are great, and the "tragic" loss of `_deserialize_with_registered_deserializers`

made me want to cheer.

I should probably pull this and experiment a bit before hitting "Approve".

[docs/guides/datasets.md](https://github.com/vllm-project/guidellm/pull/733/files#diff-25d387359ef26d847e440becb4ffc0825e3dbf562df2d7e5b3cc1d49b1e6a43e)Outdated


**reviewed**

[dbutenhof](https://github.com/dbutenhof)May 19, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

Interesting. Previously, if I included an unrecognized data option or excluded a "required" like `output_tokens`

, the test run just went ahead without complaint.

With the new code, in either case, I get unhelpful errors. An unrecognized (e.g., misspelled) parameter gets "Error: Invalid value for --data: Extra inputs are not permitted", while a missing expected parameter (e.g., our friend "output_tokens") fails with "Error: Invalid value for --data: Field required".

Yeah the validation error is translated here:
Lines 427 to 432
in
But it does not handle nested args yet. Just needs some adjustments. It will be easier to do after the CLI is redone since there will be less conditional cases. |

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/a867e01115732c332d7885b5ab4c1211a6e9305d..77a0cdd3e5d2fa9a2992bfacfe8738bbc976e7f9)the refactor/schema/data branch from

[to](https://github.com/vllm-project/guidellm/commit/a867e01115732c332d7885b5ab4c1211a6e9305d)

`a867e01`


`77a0cdd`

[Compare](https://github.com/vllm-project/guidellm/compare/a867e01115732c332d7885b5ab4c1211a6e9305d..77a0cdd3e5d2fa9a2992bfacfe8738bbc976e7f9)

May 19, 2026 20:27

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)

There was a problem hiding this comment.

This is a large improvement. I just have a few comments.

[src/guidellm/data/deserializers/huggingface.py](https://github.com/vllm-project/guidellm/pull/733/files#diff-4f57b5f7882a123a186fbd822bc3bc1560860e07a731d4171463502e48bda97a)Outdated

[src/guidellm/benchmark/profiles.py](https://github.com/vllm-project/guidellm/pull/733/files#diff-abcf32987c69e483665371f42096bf49b8d65cf4651c5c95cccac96684119f10)

[src/guidellm/cli/benchmark/run.py](https://github.com/vllm-project/guidellm/pull/733/files#diff-310250441381ed1c3efd1052124a9ab915eb1ec368404345bc7037069660a46a)

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/6dacbafc8f5d497d6be2aa6e8012d218b8f1fc5c..47ade3a7747c8c5ae96f9b4ca7e31fb96b3050bc)the refactor/schema/data branch from

[to](https://github.com/vllm-project/guidellm/commit/6dacbafc8f5d497d6be2aa6e8012d218b8f1fc5c)

`6dacbaf`


`47ade3a`

[Compare](https://github.com/vllm-project/guidellm/compare/6dacbafc8f5d497d6be2aa6e8012d218b8f1fc5c..47ade3a7747c8c5ae96f9b4ca7e31fb96b3050bc)

May 21, 2026 21:14

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)

There was a problem hiding this comment.

In several places the markdown shows the old arg for huggingface inputs "data".

[src/guidellm/data/deserializers/huggingface.py](https://github.com/vllm-project/guidellm/pull/733/files#diff-4f57b5f7882a123a186fbd822bc3bc1560860e07a731d4171463502e48bda97a)


**previously approved these changes**

[dbutenhof](https://github.com/dbutenhof)May 22, 2026

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/984e75513790f7f10243e7ff4c405491289e8492..fa01ffdbf0dc0601cf58a3b15c5458bbe26448cd)the refactor/schema/data branch 2 times, most recently from

[to](https://github.com/vllm-project/guidellm/commit/984e75513790f7f10243e7ff4c405491289e8492)

`984e755`


`fa01ffd`

[Compare](https://github.com/vllm-project/guidellm/compare/984e75513790f7f10243e7ff4c405491289e8492..fa01ffdbf0dc0601cf58a3b15c5458bbe26448cd)

May 26, 2026 17:28


**approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)May 26, 2026

Generated-by: claude-code Sonnet 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com>

Assisted-by: GitHub Copilot GPT-4.1 Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>

Assisted-by: GitHub Copilot GPT-4.1 Signed-off-by: Samuel Monson <smonson@redhat.com>

Assisted-by: GitHub Copilot GPT-4.1 Signed-off-by: Samuel Monson <smonson@redhat.com>

Assisted-by: GitHub Copilot GPT-4.1 Signed-off-by: Samuel Monson <smonson@redhat.com>

Generated-by: claude-code Sonnet 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com>

Generated-by: claude-code Sonnet 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com>

Generated-by: claude-code Sonnet 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com>

Generated-by: claude-code Sonnet 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com>

Generated-by: claude-code Sonnet 4.6 Signed-off-by: Samuel Monson <smonson@redhat.com>

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/fa01ffdbf0dc0601cf58a3b15c5458bbe26448cd..89e8951bdbc40087a0818b011d31dd394f3bf834)the refactor/schema/data branch from

[to](https://github.com/vllm-project/guidellm/commit/fa01ffdbf0dc0601cf58a3b15c5458bbe26448cd)

`fa01ffd`


`89e8951`

[Compare](https://github.com/vllm-project/guidellm/compare/fa01ffdbf0dc0601cf58a3b15c5458bbe26448cd..89e8951bdbc40087a0818b011d31dd394f3bf834)

May 26, 2026 18:31


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)May 26, 2026

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

## Summary

First set of changes to

`data`

creation and configuration. Most changes are hidden interally but does break`--data`

usage by requiring the new format (e.g.`kind=sythetic_text,prompt_tokens=32,...`

).## Details

This is missing some key pieces like how

`random_seed`

and`processor`

will be configured. Also currently everything is configured in the dataloader, that may move to some nice helper function under`src/data/entrypoints.py`

.Updated docs changes are generated and mostly untested since they we need to be adjusted again after the full CLI refactor.

## Test Plan

Run any existing workloads. Everything should be the same except for the format of

`--data`

.## Related Issues

## Use of AI