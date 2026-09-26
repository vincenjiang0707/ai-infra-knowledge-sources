source: https://github.com/vllm-project/guidellm/pull/777

# Add Mooncake trace format support - #777

[mergify[bot]](https://github.com/mergify[bot])merged 23 commits into

## Conversation

|
Hi |

[SkiHatDuckie](https://github.com/SkiHatDuckie)

[force-pushed](https://github.com/vllm-project/guidellm/compare/9797113ecfc45d608fc08d2ffa33cceaf5b13157..4563c7287100cc89fef0168570fd791bd0e4a093)the mooncake-create-prompt branch from

[to](https://github.com/vllm-project/guidellm/commit/9797113ecfc45d608fc08d2ffa33cceaf5b13157)

`9797113`


`4563c72`

[Compare](https://github.com/vllm-project/guidellm/compare/9797113ecfc45d608fc08d2ffa33cceaf5b13157..4563c7287100cc89fef0168570fd791bd0e4a093)

June 5, 2026 20:16

|
Hi |

[SkiHatDuckie](https://github.com/SkiHatDuckie)

[force-pushed](https://github.com/vllm-project/guidellm/compare/c02b367b066f135698aaecf1b2fe5f06a5fe5265..e6ecdd65d1b7eccd0ee32bf0526b3bd81a9850e0)the mooncake-create-prompt branch 2 times, most recently from

[to](https://github.com/vllm-project/guidellm/commit/c02b367b066f135698aaecf1b2fe5f06a5fe5265)

`c02b367`


`e6ecdd6`

[Compare](https://github.com/vllm-project/guidellm/compare/c02b367b066f135698aaecf1b2fe5f06a5fe5265..e6ecdd65d1b7eccd0ee32bf0526b3bd81a9850e0)

June 8, 2026 17:05

|
Hello, thanks for working on this. It looks like the branch may have been merged with main instead of rebased on top of it. The current diff contains many unrelated commits/changes, which makes the Mooncake-specific changes difficult to review. Would it be possible to rebase or clean the branch so the PR only contains the trace_mooncake changes? I also tried the PR locally before the merge and hit the following validation error: ```
guidellm benchmark run \
--profile kind=replay \
--data "kind=trace_mooncake,path=trace.jsonl" \
--target http://<url of your endpoint> \
--model <model-name>
``` Error:
It looks like |

Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>

Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>

Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>

Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>

Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>

Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>

Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>

Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>

Signed-off-by: SkiHatDuckie <63932363+SkiHatDuckie@users.noreply.github.com> Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>

Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>

[SkiHatDuckie](https://github.com/SkiHatDuckie)

[force-pushed](https://github.com/vllm-project/guidellm/compare/4545c8e44a72372798facdb5c70a403ca1f823fc..b26e3d702fd011d303dc446b6b845573f2acd5d0)the mooncake-create-prompt branch from

[to](https://github.com/vllm-project/guidellm/commit/4545c8e44a72372798facdb5c70a403ca1f823fc)

`4545c8e`


`b26e3d7`

[Compare](https://github.com/vllm-project/guidellm/compare/4545c8e44a72372798facdb5c70a403ca1f823fc..b26e3d702fd011d303dc446b6b845573f2acd5d0)

June 8, 2026 20:08

|
Branch has now been cleaned up. I was still working on getting guidellm/vllm to run on my current machine, so the initial commits were only tested via unit tests. I'll get to work on fixing the validation shortly. |


**reviewed**

[dbutenhof](https://github.com/dbutenhof)Jun 9, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

A few minor comments to start with (which I realize I've had pending for several days after a first scan, and might as well post!)

[src/guidellm/data/deserializers/trace_mooncake.py](https://github.com/vllm-project/guidellm/pull/777/files/2b602143791c26c2cff4921567b306860b47c166#diff-8f8663ec474630bb9a8cee957c838109b834c91e3cd3cf13c2e9514a009077e8)Outdated

[src/guidellm/data/deserializers/trace_mooncake.py](https://github.com/vllm-project/guidellm/pull/777/files/2b602143791c26c2cff4921567b306860b47c166#diff-8f8663ec474630bb9a8cee957c838109b834c91e3cd3cf13c2e9514a009077e8)Outdated

[src/guidellm/data/deserializers/trace_mooncake.py](https://github.com/vllm-project/guidellm/pull/777/files/2b602143791c26c2cff4921567b306860b47c166#diff-8f8663ec474630bb9a8cee957c838109b834c91e3cd3cf13c2e9514a009077e8)Outdated

Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>

Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>


**requested changes**

[sjmonson](https://github.com/sjmonson)Jun 9, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)

There was a problem hiding this comment.

Some nits, we also discussed merging this with "trace_synthetic" since they are mostly the same. Lets do that in a followup after this merges.

[src/guidellm/data/deserializers/trace_mooncake.py](https://github.com/vllm-project/guidellm/pull/777/files/2a9811029f395571714a7f83d12c3061cad3dd26#diff-8f8663ec474630bb9a8cee957c838109b834c91e3cd3cf13c2e9514a009077e8)Outdated

[src/guidellm/data/deserializers/trace_mooncake.py](https://github.com/vllm-project/guidellm/pull/777/files/2a9811029f395571714a7f83d12c3061cad3dd26#diff-8f8663ec474630bb9a8cee957c838109b834c91e3cd3cf13c2e9514a009077e8)Outdated

[src/guidellm/data/deserializers/trace_mooncake.py](https://github.com/vllm-project/guidellm/pull/777/files/2a9811029f395571714a7f83d12c3061cad3dd26#diff-8f8663ec474630bb9a8cee957c838109b834c91e3cd3cf13c2e9514a009077e8)

[src/guidellm/data/deserializers/trace_mooncake.py](https://github.com/vllm-project/guidellm/pull/777/files/2a9811029f395571714a7f83d12c3061cad3dd26#diff-8f8663ec474630bb9a8cee957c838109b834c91e3cd3cf13c2e9514a009077e8)

[src/guidellm/data/deserializers/trace_mooncake.py](https://github.com/vllm-project/guidellm/pull/777/files/2a9811029f395571714a7f83d12c3061cad3dd26#diff-8f8663ec474630bb9a8cee957c838109b834c91e3cd3cf13c2e9514a009077e8)Outdated

Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>

Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>

Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>

Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>


**requested changes**

[sjmonson](https://github.com/sjmonson)Jun 11, 2026

[src/guidellm/data/deserializers/trace_mooncake.py](https://github.com/vllm-project/guidellm/pull/777/files/ca85a658573040d6000282ec4654d03d7224656c#diff-8f8663ec474630bb9a8cee957c838109b834c91e3cd3cf13c2e9514a009077e8)Outdated

[src/guidellm/data/deserializers/trace_mooncake.py](https://github.com/vllm-project/guidellm/pull/777/files/ca85a658573040d6000282ec4654d03d7224656c#diff-8f8663ec474630bb9a8cee957c838109b834c91e3cd3cf13c2e9514a009077e8)

Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>

Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>

Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>

Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>


**requested changes**

[sjmonson](https://github.com/sjmonson)Jun 11, 2026

[src/guidellm/data/deserializers/trace_mooncake.py](https://github.com/vllm-project/guidellm/pull/777/files/7c7d1e499ef1431d1c0e18f657167877e46fedec#diff-8f8663ec474630bb9a8cee957c838109b834c91e3cd3cf13c2e9514a009077e8)Outdated

Co-authored-by: Samuel Monson <smonson@irbash.net> Signed-off-by: SkiHatDuckie <63932363+SkiHatDuckie@users.noreply.github.com>


**requested changes**

[sjmonson](https://github.com/sjmonson)Jun 11, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)

There was a problem hiding this comment.

Still seeing failures:

```
Skipping data row due to error: <class 'guidellm.data.deserializers.trace_mooncake._TraceMooncakeExamplesIterable'> doesn't implement shard_data_sources yet.
```


Might be a good idea to write an integration test that loads a 5ish row dataset and tries to iterate through it.

Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>

Should be fixed with the latest commit. I'm thinking of adding the integration tests during the refactoring/merging together of TraceSynthetic and TraceMooncake (separate PR), as I fear adding the tests now will lead to them being immediately obsoleted. |


**previously approved these changes**

[sjmonson](https://github.com/sjmonson)Jun 11, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)

There was a problem hiding this comment.

Needs a linting fix but otherwise looks good.


**previously approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Jun 12, 2026

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)

There was a problem hiding this comment.

Looks good to me, except we could use some documentation for this format in docs/guides/datasets.md. I also added a few comments that are not blockers.

[src/guidellm/data/deserializers/trace_mooncake.py](https://github.com/vllm-project/guidellm/pull/777/files/2100dbd78f76b3fc41a98bf5e969b2dfd8cd87ef#diff-8f8663ec474630bb9a8cee957c838109b834c91e3cd3cf13c2e9514a009077e8)

[src/guidellm/data/deserializers/trace_mooncake.py](https://github.com/vllm-project/guidellm/pull/777/files/2100dbd78f76b3fc41a98bf5e969b2dfd8cd87ef#diff-8f8663ec474630bb9a8cee957c838109b834c91e3cd3cf13c2e9514a009077e8)

## Merge Queue Status
This pull request spent
|


**previously approved these changes**

[dbutenhof](https://github.com/dbutenhof)Jun 12, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

The CI is unhappy with your imports, so you're going to need one more commit.

[src/guidellm/data/deserializers/trace_mooncake.py](https://github.com/vllm-project/guidellm/pull/777/files/2100dbd78f76b3fc41a98bf5e969b2dfd8cd87ef#diff-8f8663ec474630bb9a8cee957c838109b834c91e3cd3cf13c2e9514a009077e8)

Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>

[SkiHatDuckie](https://github.com/SkiHatDuckie)dismissed stale reviews from

[dbutenhof](https://github.com/dbutenhof),

[jaredoconnell](https://github.com/jaredoconnell), and

[sjmonson](https://github.com/sjmonson)via

```
```[6472f55](https://github.com/vllm-project/guidellm/commit/6472f554bbd03992cb6c9760f44e4ea6c39ba466)

June 12, 2026 13:16


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Jun 12, 2026


**approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Jun 12, 2026

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

## Summary

Add support for generating synthetic prompts from a Mooncake formatted trace file. This involves handling the

hash_idscolumn, as well as validating that two different hash IDs do not represent the exact same sequence of tokens if they share the same previous ID (parent node).Future PRs should create a common file/class for the similar functionality of

`TraceMooncakeDatasetDeserializer`

and`TraceSyntheticDatasetDeserializer`

, as well as to make adding support for additional trace formats easier.## Details

`src/guidellm/data/deserializers/trace_mooncake.py`

`TraceMooncakeDataArgs`

: Adds two new fields`hash_ids_column`

and`hash_id_block_size`

`TraceMooncakeDatasetDeserializer`

: Takes a processor, and a path to a .jsonl file, and returns a`datasets.Dataset`

with the columns("prompt", "prompt_token_count", "output_token_count", "hash_ids")`DataArgs`

and`DatasetDeserializerFactory`

`test_trace_mooncake.py`

## Test Plan

`tox -e test-unit -- tests/unit/data/deserializers/test_trace_mooncake.py`

`tox -e lint-check && tox -e type-check`

## Related Issues

## Use of AI

## git log

commit

de90d40Author: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Wed Jun 3 15:10:36 2026 -0400

commit

a58605eAuthor: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Wed Jun 3 16:59:02 2026 -0400

commit

fe5a3f6Author: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Thu Jun 4 09:52:27 2026 -0400

commit

d770bfaAuthor: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Fri Jun 5 13:33:27 2026 -0400

commit

b2f0cdeAuthor: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Fri Jun 5 15:02:30 2026 -0400

commit

214fcefAuthor: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Fri Jun 5 15:03:26 2026 -0400

commit

b9ffd89Author: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Fri Jun 5 15:24:01 2026 -0400

commit

68c530fAuthor: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Fri Jun 5 15:32:41 2026 -0400

commit

a38db63Author: SkiHatDuckie 63932363+SkiHatDuckie@users.noreply.github.com

Date: Sat Jun 6 21:36:22 2026 -0400

commit

b26e3d7Author: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Mon Jun 8 13:12:37 2026 -0400

commit

3f67e46Author: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Tue Jun 9 12:41:59 2026 -0400

commit

2a98110Author: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Tue Jun 9 13:33:57 2026 -0400

commit

3021f8bAuthor: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Tue Jun 9 15:31:12 2026 -0400

commit

8954956Author: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Tue Jun 9 16:57:39 2026 -0400

commit

a6bfb8bAuthor: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Wed Jun 10 11:53:04 2026 -0400

commit

ca85a65Author: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Wed Jun 10 17:05:08 2026 -0400

commit

b1b85e5Author: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Thu Jun 11 12:20:39 2026 -0400

commit

f7ab87eAuthor: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Thu Jun 11 12:25:10 2026 -0400

commit

ac9233fAuthor: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Thu Jun 11 13:21:17 2026 -0400

commit

7c7d1e4Author: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Thu Jun 11 13:33:11 2026 -0400

commit

903a443Author: SkiHatDuckie 63932363+SkiHatDuckie@users.noreply.github.com

Date: Thu Jun 11 14:26:04 2026 -0400

commit

2100dbdAuthor: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Thu Jun 11 15:50:27 2026 -0400

commit

6472f55Author: SkiHatDuckie SkiHatDuckie@gmail.com

Date: Fri Jun 12 09:15:58 2026 -0400

Co-authored-by: Samuel Monson smonson@irbash.net

Signed-off-by: SkiHatDuckie SkiHatDuckie@gmail.com

Signed-off-by: SkiHatDuckie 63932363+SkiHatDuckie@users.noreply.github.com