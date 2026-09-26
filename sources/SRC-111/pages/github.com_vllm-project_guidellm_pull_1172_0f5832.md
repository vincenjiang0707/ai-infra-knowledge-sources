source: https://github.com/vllm-project/guidellm/pull/1172

## Conversation

[git-jxj](https://github.com/git-jxj)requested review from

[dbutenhof](https://github.com/dbutenhof),

[dfeddema](https://github.com/dfeddema),

[jaredoconnell](https://github.com/jaredoconnell)and

[sjmonson](https://github.com/sjmonson)as

[code owners](https://github.com/vllm-project/guidellm/blob/148c3bab4f75fe9f64fb15520d7d64fa08914a90/CODEOWNERS#L2)

September 22, 2026 09:16

|
Hi |

Generated-by: OpenAI Codex Signed-off-by: git-jxj <65210887+git-jxj@users.noreply.github.com>

[git-jxj](https://github.com/git-jxj)

[force-pushed](https://github.com/vllm-project/guidellm/compare/6486e748c35173137029e0a7fe5d812f4a1813fb..82cdb1230afbb7a95dea2d2cb19fd319b1f7e717)the git-jxj/fix-url-image-resize branch from

[to](https://github.com/vllm-project/guidellm/commit/6486e748c35173137029e0a7fe5d812f4a1813fb)

`6486e74`


`82cdb12`

[Compare](https://github.com/vllm-project/guidellm/compare/6486e748c35173137029e0a7fe5d812f4a1813fb..82cdb1230afbb7a95dea2d2cb19fd319b1f7e717)

September 22, 2026 09:31


**previously approved these changes**

[dbutenhof](https://github.com/dbutenhof)Sep 22, 2026

[src/guidellm/utils/vision.py](https://github.com/vllm-project/guidellm/pull/1172/files/82cdb1230afbb7a95dea2d2cb19fd319b1f7e717#diff-de60595dd945e059db8e43d6d0e30808769c92f7f6999ea56b7dd18c2c664dd6)Outdated

|
Tick the box to add this pull request to the merge queue (same as
|

|
Received a single approval. Will automatically queue for merge once two maintainers approve, all change requests are resolved, and DCO passes. |


**previously approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Sep 23, 2026

Document each image encoding parameter in the repository's reStructuredText style and clarify the return value and error conditions. Generated-by: OpenAI Codex Signed-off-by: git-jxj <65210887+git-jxj@users.noreply.github.com>

[git-jxj](https://github.com/git-jxj)dismissed stale reviews from

[jaredoconnell](https://github.com/jaredoconnell)and

[dbutenhof](https://github.com/dbutenhof)via

```
```[a29f5eb](https://github.com/vllm-project/guidellm/commit/a29f5eb77f6b2db57baa45e3099b653fd0ddc9d5)

September 23, 2026 07:52


**requested changes**

[dbutenhof](https://github.com/dbutenhof)Sep 23, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

My apologies.

I think I'm sorry for making the comment about the docstring, because once a PR touches human-targeted text, it's hard not to devolve into nit-picking.

But, with that said, since you took up the challenge (thanks for that), I think a few details should be clarified...

[src/guidellm/utils/vision.py](https://github.com/vllm-project/guidellm/pull/1172/files/a29f5eb77f6b2db57baa45e3099b653fd0ddc9d5#diff-de60595dd945e059db8e43d6d0e30808769c92f7f6999ea56b7dd18c2c664dd6)Outdated

[src/guidellm/utils/vision.py](https://github.com/vllm-project/guidellm/pull/1172/files/a29f5eb77f6b2db57baa45e3099b653fd0ddc9d5#diff-de60595dd945e059db8e43d6d0e30808769c92f7f6999ea56b7dd18c2c664dd6)

Describe URL handling for encode_type and clarify when image pixel and byte counts are available. Generated-by: OpenAI Codex Signed-off-by: git-jxj <65210887+git-jxj@users.noreply.github.com>


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Sep 24, 2026

|
Received a single approval. Will automatically queue for merge once two maintainers approve, all change requests are resolved, and DCO passes. |

### This branch has not been deployed

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

## Summary

Image URLs encoded as base64 silently ignored explicit

`width`

and`height`

options. For example, an 80×40 image requested with`width=40`

stayed 80×40, while the same image supplied as bytes became 40×20. Forward both dimensions after downloading the image so URL and local inputs use the same resizing behavior.## Details

## Test Plan

`tox -e tests -- tests/unit`

: 3,273 passed, 31 skipped, 163 xfailed.`tox -e tests -- tests/integration tests/e2e`

: 42 passed, 25 xfailed, using the in-tree mock server.`tox -e lint-check`

and`tox -e type-check`

: passed.## Related Issues

Independent code inspection; no associated issue.

## Use of AI

Code and regression tests were generated with OpenAI Codex.

## git log

commit

82cdb12Author: git-jxj 65210887+git-jxj@users.noreply.github.com

Date: Tue Sep 22 17:09:01 2026 +0800

commit

a29f5ebAuthor: git-jxj 65210887+git-jxj@users.noreply.github.com

Date: Wed Sep 23 15:52:21 2026 +0800

commit

9b1a8c0Author: git-jxj 65210887+git-jxj@users.noreply.github.com

Date: Thu Sep 24 09:27:03 2026 +0800

Generated-by: OpenAI Codex

Signed-off-by: git-jxj 65210887+git-jxj@users.noreply.github.com