source: https://github.com/vllm-project/guidellm/pull/1105

# feat: rotate API keys across benchmark requests - #1105

[PatilHrushikesh](https://github.com/PatilHrushikesh)wants to merge 4 commits into

[PatilHrushikesh](https://github.com/PatilHrushikesh) wants to merge 4 commits into

[PatilHrushikesh](https://github.com/PatilHrushikesh)wants to merge 4 commits into

## Conversation

[PatilHrushikesh](https://github.com/PatilHrushikesh)

[force-pushed](https://github.com/vllm-project/guidellm/compare/97eaa62f552ed5e09153e5bd06f6a98dbfe3a1a8..8632f1322c6056e30f49d24c0d254bbb6757dd29)the feature/multi-api-key-rotation branch from

[to](https://github.com/vllm-project/guidellm/commit/97eaa62f552ed5e09153e5bd06f6a98dbfe3a1a8)

`97eaa62`


`8632f13`

[Compare](https://github.com/vllm-project/guidellm/compare/97eaa62f552ed5e09153e5bd06f6a98dbfe3a1a8..8632f1322c6056e30f49d24c0d254bbb6757dd29)

September 9, 2026 05:09

[PatilHrushikesh](https://github.com/PatilHrushikesh)marked this pull request as ready for review

September 10, 2026 05:16

|
Hi |

Add inline and file-backed API key sources for the OpenAI HTTP backend and coordinate round-robin allocation across worker processes. Generated-by: Cursor GPT-5.6 Terra Co-authored-by: Cursor <cursoragent@cursor.com> Signed-off-by: Hrushikesh Patil <hrushi2900@gmail.com>

Signed-off-by: Hrushikesh Patil <hrushi2900@gmail.com>

Use worker-specific offsets, separate API credential validation, and load key files in the HTTP backend. Co-authored-by: Cursor <cursoragent@cursor.com> Signed-off-by: Hrushikesh Patil <hrushi2900@gmail.com>

[PatilHrushikesh](https://github.com/PatilHrushikesh)

[force-pushed](https://github.com/vllm-project/guidellm/compare/004ea61f05b7b56af711b6a1a34865324c5d4822..6dd730328290a0d3c633ee686eae64012b175e31)the feature/multi-api-key-rotation branch from

[to](https://github.com/vllm-project/guidellm/commit/004ea61f05b7b56af711b6a1a34865324c5d4822)

`004ea61`


`6dd7303`

[Compare](https://github.com/vllm-project/guidellm/compare/004ea61f05b7b56af711b6a1a34865324c5d4822..6dd730328290a0d3c633ee686eae64012b175e31)

September 21, 2026 08:21

|
Hey sorry for the delay. We have a release planned on the 30th so we are trying to slow down the inclusion of unplanned features until after that release. I have glanced over your code and here is a couple high-level notes in the meantime: One problem I have with the current implementation is that its unpredictable which key gets assigned to which request. Workers do not get the same requests assigned to them every time so you really should not depend on specific worker indexing. Another issue is that this is not at all multi-turn compatible, each turn could end up with completely different API keys. Something we have had on our TODO list for a long time is allowing headers (and also the body) of the request to be specifiable in the dataset. So I would prefer to see this PR move that direction. Basically add a new |

### This branch has not been deployed

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

## Summary

Add multi-key authentication for the

`openai_http`

backend. Keys can be supplied inline or from a newline-delimited file and rotate independently from worker-specific offsets.## Details

`api_keys`

and`api_key_file`

options while preserving`api_key`

.`main`

and resolve overlapping test/backend changes.## Test Plan

`tox -e lint-check`

passed.`tox -e type-check`

passed.## Related Issues

## Use of AI

Generated-by: Cursor GPT-5.6 Terra

## git log

commit

9bf9eadAuthor: Hrushikesh Patil hrushi2900@gmail.com

Date: Wed Sep 16 05:15:15 2026 +0000

commit

a224a86Author: Hrushikesh Patil hrushi2900@gmail.com

Date: Wed Sep 16 05:15:34 2026 +0000

commit

6dd7303Author: Hrushikesh Patil hrushi2900@gmail.com

Date: Wed Sep 16 05:17:22 2026 +0000

Co-authored-by: Cursor cursoragent@cursor.com

Generated-by: Cursor GPT-5.6 Terra

Signed-off-by: Hrushikesh Patil hrushi2900@gmail.com