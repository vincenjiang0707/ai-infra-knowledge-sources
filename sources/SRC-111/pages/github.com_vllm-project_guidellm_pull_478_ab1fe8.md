source: https://github.com/vllm-project/guidellm/pull/478

# Move request formatting to backend - #478

## Conversation

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/1e802377978259a89b4d35947247c16365845e77..687f702c83a1dfa992d19264ca5aa4be481248c2)the feat/split_formatter branch from

[to](https://github.com/vllm-project/guidellm/commit/1e802377978259a89b4d35947247c16365845e77)

`1e80237`


`687f702`

[Compare](https://github.com/vllm-project/guidellm/compare/1e802377978259a89b4d35947247c16365845e77..687f702c83a1dfa992d19264ca5aa4be481248c2)

November 21, 2025 23:11

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/8dbc7f57cc6d8fa5eef488ae0365d5fe7a01c0dc..cef2e60f82243abc146fef243f3846a727b390b5)the feat/split_formatter branch from

[to](https://github.com/vllm-project/guidellm/commit/8dbc7f57cc6d8fa5eef488ae0365d5fe7a01c0dc)

`8dbc7f5`


`cef2e60`

[Compare](https://github.com/vllm-project/guidellm/compare/8dbc7f57cc6d8fa5eef488ae0365d5fe7a01c0dc..cef2e60f82243abc146fef243f3846a727b390b5)

December 9, 2025 18:23

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/c98234b53ec83658fbf4e4c1b35b9b3224859d0a..28ece4555d1002765156c85d8371388b9627df80)the feat/split_formatter branch 2 times, most recently from

[to](https://github.com/vllm-project/guidellm/commit/c98234b53ec83658fbf4e4c1b35b9b3224859d0a)

`c98234b`


`28ece45`

[Compare](https://github.com/vllm-project/guidellm/compare/c98234b53ec83658fbf4e4c1b35b9b3224859d0a..28ece4555d1002765156c85d8371388b9627df80)

January 26, 2026 16:43

|
A note on |

[sjmonson](https://github.com/sjmonson)marked this pull request as ready for review

January 27, 2026 20:18

[src/guidellm/backends/openai/http.py](https://github.com/vllm-project/guidellm/pull/478/files#diff-6a56e17b4a9b1b702100f54acf336f97d4de6346ea9f696bb23602d12c1f0002)Outdated

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/01c2dce2d5b3cc45c2fb1b1380d475baea36f0d4..dbbd18afad89fc49c46f1488f048b066c0d42dfb)the feat/split_formatter branch from

[to](https://github.com/vllm-project/guidellm/commit/01c2dce2d5b3cc45c2fb1b1380d475baea36f0d4)

`01c2dce`


`dbbd18a`

[Compare](https://github.com/vllm-project/guidellm/compare/01c2dce2d5b3cc45c2fb1b1380d475baea36f0d4..dbbd18afad89fc49c46f1488f048b066c0d42dfb)

January 28, 2026 18:20

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)

There was a problem hiding this comment.

Looks good so far. I tested the default paths with a simple local benchmark, and that didn't break anything.

I have a few minor comments.

I'll give a final approving review once the tests are passing.

[src/guidellm/data/loaders.py](https://github.com/vllm-project/guidellm/pull/478/files#diff-9a029d8206d05720b0684bf0abd33ddee8e35225688fc46495bb0c2297fdca45)

[src/guidellm/__main__.py](https://github.com/vllm-project/guidellm/pull/478/files#diff-62e0a62289c938a74b026dbce7a0f95f26893e0aa9feedb81349e658db8af7bf)

[src/guidellm/settings.py](https://github.com/vllm-project/guidellm/pull/478/files#diff-9e53343eb57495c8164a5448c076b7f3504c652e3e11188963e5b6d8d3a58405)Outdated

[src/guidellm/backends/openai/request_formatter.py](https://github.com/vllm-project/guidellm/pull/478/files#diff-fa41eeb04fdf99e90f466933a5e961fa8e363623e6a7dd1d92c5b95d430ebb59)Outdated


[sjmonson](https://github.com/sjmonson)changed the title

Jan 29, 2026

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/1ecb2a120e746e0279a04a243e036a5ab73ef069..3f052117962428241d74d0910ebc50e7f0ad4fc8)the feat/split_formatter branch 3 times, most recently from

[to](https://github.com/vllm-project/guidellm/commit/1ecb2a120e746e0279a04a243e036a5ab73ef069)

`1ecb2a1`


`3f05211`

[Compare](https://github.com/vllm-project/guidellm/compare/1ecb2a120e746e0279a04a243e036a5ab73ef069..3f052117962428241d74d0910ebc50e7f0ad4fc8)

January 29, 2026 19:46


**previously approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Jan 30, 2026

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)

There was a problem hiding this comment.

The code looks good, and I tested the happy path. I didn't test edge cases or more advanced usage of the backend features.

We may want to wait for Mark's approval, too, before merging.

[src/guidellm/backends/openai/http.py](https://github.com/vllm-project/guidellm/pull/478/files#diff-6a56e17b4a9b1b702100f54acf336f97d4de6346ea9f696bb23602d12c1f0002)Outdated

[src/guidellm/data/preprocessors/encoders.py](https://github.com/vllm-project/guidellm/pull/478/files#diff-c0c08cde544025934be8a7f25d58ecb52ddf010ed3e7c7da3c88e0cf4f1ed679)

[src/guidellm/backends/openai/http.py](https://github.com/vllm-project/guidellm/pull/478/files#diff-6a56e17b4a9b1b702100f54acf336f97d4de6346ea9f696bb23602d12c1f0002)Outdated


**previously approved these changes**

[markurtz](https://github.com/markurtz)Feb 3, 2026

###
**
**[markurtz](https://github.com/markurtz)
left a comment

**left a comment**

[markurtz](https://github.com/markurtz)

There was a problem hiding this comment.

I think this all loks reasonable to move towards. There are a few things I'd like to do a pass over / discuss in a follow up, will connect later on that

Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>

Fix schema tests Drop unused backend mock Move openai tests to match new structure Rewrite OpenAI backend tests Drop HuggingFace test that relies on network Fix failing backend tests Remove remaining references to request_type in tests Unify request_formatter and response_handler tests More unit test fixes Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/6dab76f17905a6b12f7be4b187060d239fdfd658..efa02cf76dcf5183afad03f0238051ab1788a821)the feat/split_formatter branch from

[to](https://github.com/vllm-project/guidellm/commit/6dab76f17905a6b12f7be4b187060d239fdfd658)

`6dab76f`


`efa02cf`

[Compare](https://github.com/vllm-project/guidellm/compare/6dab76f17905a6b12f7be4b187060d239fdfd658..efa02cf76dcf5183afad03f0238051ab1788a821)

February 3, 2026 15:18

Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>


**approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Feb 3, 2026

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)

There was a problem hiding this comment.

I have no blocking comments. It looks good and I re-tested a simple benchmark.

[src/guidellm/data/preprocessors/encoders.py](https://github.com/vllm-project/guidellm/pull/478/files#diff-c0c08cde544025934be8a7f25d58ecb52ddf010ed3e7c7da3c88e0cf4f1ed679)

[src/guidellm/__main__.py](https://github.com/vllm-project/guidellm/pull/478/files/974ba77f8551f0656f7d6c983286aa65ba0f0a98#diff-62e0a62289c938a74b026dbce7a0f95f26893e0aa9feedb81349e658db8af7bf)

[src/guidellm/__main__.py](https://github.com/vllm-project/guidellm/pull/478/files/974ba77f8551f0656f7d6c983286aa65ba0f0a98#diff-62e0a62289c938a74b026dbce7a0f95f26893e0aa9feedb81349e658db8af7bf)

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

## Summary

Splits the

`RequestFormatter`

into multiple separate components across data loading, data preprocessing, and the backend. Necessary step for next attempt at multi-turn.## Details

`RequestFormatter`

preprocessor## Test Plan

## Related Issues

## Use of AI

`## WRITTEN BY AI ##`

)