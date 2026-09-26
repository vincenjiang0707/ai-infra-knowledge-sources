source: https://github.com/vllm-project/guidellm/pull/1001

## Conversation

Contributor

|
Hi |

[cmiyai](https://github.com/cmiyai)

[force-pushed](https://github.com/vllm-project/guidellm/compare/a91bdca87bd4873f45ff5044808feac2348acecf..bd8d2ce961756eda7dd23bc4209504dbe107f2ad)the docs/e2e-use-case-examples branch from

[to](https://github.com/vllm-project/guidellm/commit/a91bdca87bd4873f45ff5044808feac2348acecf)

`a91bdca`


`bd8d2ce`

[Compare](https://github.com/vllm-project/guidellm/compare/a91bdca87bd4873f45ff5044808feac2348acecf..bd8d2ce961756eda7dd23bc4209504dbe107f2ad)

August 6, 2026 21:05

Contributor

|
Hi |

[cmiyai](https://github.com/cmiyai)

[force-pushed](https://github.com/vllm-project/guidellm/compare/85be37fbdd0f038f76244ca2a5e4c2dc2d27bbc6..45cba09397b221c6a6777cb91473fa139271a2a8)the docs/e2e-use-case-examples branch from

[to](https://github.com/vllm-project/guidellm/commit/85be37fbdd0f038f76244ca2a5e4c2dc2d27bbc6)

`85be37f`


`45cba09`

[Compare](https://github.com/vllm-project/guidellm/compare/85be37fbdd0f038f76244ca2a5e4c2dc2d27bbc6..45cba09397b221c6a6777cb91473fa139271a2a8)

August 12, 2026 03:28


**requested changes**

[sjmonson](https://github.com/sjmonson)Aug 13, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)
Collaborator


There was a problem hiding this comment.

Overall these guides are great. Just a few minor nits.

[docs/examples/custom_workloads.md](https://github.com/vllm-project/guidellm/pull/1001/files#diff-08dfb2c31d806945574f00d8e8bb4cb1414a823a168b3bfaf0a0c1a101f0509d)

[docs/examples/optimal_concurrency.md](https://github.com/vllm-project/guidellm/pull/1001/files#diff-c4b3a2b1b20427968653d67bcf02d2845636b85640cce4a343a52680e0a9c67c)

[docs/examples/optimal_concurrency.md](https://github.com/vllm-project/guidellm/pull/1001/files#diff-c4b3a2b1b20427968653d67bcf02d2845636b85640cce4a343a52680e0a9c67c)Outdated

Contributor

|
Hi |

[cmiyai](https://github.com/cmiyai)

[force-pushed](https://github.com/vllm-project/guidellm/compare/8ca15383c2987946a3192562fb7390c61ad29fea..1ee5a53357479337543cf75fa0a017b4527d3d20)the docs/e2e-use-case-examples branch 2 times, most recently from

[to](https://github.com/vllm-project/guidellm/commit/8ca15383c2987946a3192562fb7390c61ad29fea)

`8ca1538`


`1ee5a53`

[Compare](https://github.com/vllm-project/guidellm/compare/8ca15383c2987946a3192562fb7390c61ad29fea..1ee5a53357479337543cf75fa0a017b4527d3d20)

August 14, 2026 16:37

Contributor

|
Hi |

Collaborator

|
|

…m workloads) Signed-off-by: cmiyai <cmiyai@bu.edu>

Signed-off-by: cmiyai <cmiyai@bu.edu>

Signed-off-by: cmiyai <cmiyai@bu.edu>

[cmiyai](https://github.com/cmiyai)

[force-pushed](https://github.com/vllm-project/guidellm/compare/1ee5a53357479337543cf75fa0a017b4527d3d20..e38467ecec711ebc2e2fd3b0de1c6777c881a1ec)the docs/e2e-use-case-examples branch from

[to](https://github.com/vllm-project/guidellm/commit/1ee5a53357479337543cf75fa0a017b4527d3d20)

`1ee5a53`


`e38467e`

[Compare](https://github.com/vllm-project/guidellm/compare/1ee5a53357479337543cf75fa0a017b4527d3d20..e38467ecec711ebc2e2fd3b0de1c6777c881a1ec)

August 17, 2026 19:08

### This branch has not been deployed

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

Adds documentation for end to end use cases for usershere. Introduced a clear structured template for others to follow, so they can add documentation for other guidellm users as well.

## Details

example_template.md: Template for user guidesoptimal_concurrency.md: How to find your server's concurrency limit using sweep, with real benchmark data from Llama-3.1-8B on A100custom_workloads.md: Configuring benchmarks for different workload shapes (chat, summarization, code gen)## Related Issues

## Use of AI

## git log

commit

de05b26Author: cmiyai cmiyai@bu.edu

Date: Thu Aug 6 16:56:34 2026 -0400

commit

fe9d3baAuthor: cmiyai cmiyai@bu.edu

Date: Fri Aug 7 15:13:26 2026 -0400

commit

e38467eAuthor: cmiyai cmiyai@bu.edu

Date: Fri Aug 14 09:27:55 2026 -0700

Signed-off-by: cmiyai cmiyai@bu.edu