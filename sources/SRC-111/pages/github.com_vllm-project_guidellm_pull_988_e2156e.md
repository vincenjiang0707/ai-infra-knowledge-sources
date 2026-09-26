source: https://github.com/vllm-project/guidellm/pull/988

## Conversation

Signed-off-by: Fedir Zadniprovskyi <github.g1k56@simplelogin.com>

Contributor

|
Hi |

[fedirz](https://github.com/fedirz)

[force-pushed](https://github.com/vllm-project/guidellm/compare/3e838395caf56082e2ceb0332acb38084a96c50c..3257aaa0ee302406d2854b79ec060e83ace3a93d)the fix/984-redact-media-payloads branch from

[to](https://github.com/vllm-project/guidellm/commit/3e838395caf56082e2ceb0332acb38084a96c50c)

`3e83839`


`3257aaa`

[Compare](https://github.com/vllm-project/guidellm/compare/3e838395caf56082e2ceb0332acb38084a96c50c..3257aaa0ee302406d2854b79ec060e83ace3a93d)

August 3, 2026 17:39

Collaborator

|
I would rather see this done at output with a configurable toggle, at least for the lossless outputs (json/yaml). Having this data available can be necessary for replaying benchmarks. |

2 tasks

### This branch has not been deployed

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

Central sanitization keeps HTML request samples bounded for media workloads without separately truncating useful request metadata.

## Tests

Fixes #984

## git log

commit

3257aaaAuthor: Fedir Zadniprovskyi github.g1k56@simplelogin.com

Date: Mon Aug 3 10:38:41 2026 -0700

Signed-off-by: Fedir Zadniprovskyi github.g1k56@simplelogin.com