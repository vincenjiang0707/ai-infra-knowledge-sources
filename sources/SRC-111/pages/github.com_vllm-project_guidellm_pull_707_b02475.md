source: https://github.com/vllm-project/guidellm/pull/707

# Fix CSV column misalignment across multiple benchmarks - #707

Merged

[dbutenhof](https://github.com/dbutenhof)merged 3 commits into

Merged

## Conversation

[leehyeoklee](https://github.com/leehyeoklee)

[force-pushed](https://github.com/vllm-project/guidellm/compare/2ac74142955d2ff66e8cb4bb450a6e0fbb3527b5..a9548f7f6f6f4ab33dfd11b496818dd99dfefc9e)the feature/csv-column-alignment branch 2 times, most recently from

[to](https://github.com/vllm-project/guidellm/commit/2ac74142955d2ff66e8cb4bb450a6e0fbb3527b5)

`2ac7414`


`a9548f7`

[Compare](https://github.com/vllm-project/guidellm/compare/2ac74142955d2ff66e8cb4bb450a6e0fbb3527b5..a9548f7f6f6f4ab33dfd11b496818dd99dfefc9e)

April 24, 2026 21:28


[leehyeoklee](https://github.com/leehyeoklee)changed the title

Apr 24, 2026


[sjmonson](https://github.com/sjmonson)added

[bug](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Abug)

[escape](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Aescape)

Apr 27, 2026


**previously approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Apr 30, 2026

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)
Collaborator


There was a problem hiding this comment.

Looks good to me. If you have a chance, this does expose a gap in our unit tests, so if you could add tests that would be great, too.

Contributor

|
You can do this by running: |

[leehyeoklee](https://github.com/leehyeoklee)

[force-pushed](https://github.com/vllm-project/guidellm/compare/59275270f2e41e26f285674a839912fc83989e32..e257bcc0f1e41a6280c9413338bf510a4a765e45)the feature/csv-column-alignment branch from

[to](https://github.com/vllm-project/guidellm/commit/59275270f2e41e26f285674a839912fc83989e32)

`5927527`


`e257bcc`

[Compare](https://github.com/vllm-project/guidellm/compare/59275270f2e41e26f285674a839912fc83989e32..e257bcc0f1e41a6280c9413338bf510a4a765e45)

May 3, 2026 11:22

[leehyeoklee](https://github.com/leehyeoklee)

[force-pushed](https://github.com/vllm-project/guidellm/compare/e257bcc0f1e41a6280c9413338bf510a4a765e45..84ba01f293e5c97d0b635b0079cf12869138262b)the feature/csv-column-alignment branch from

[to](https://github.com/vllm-project/guidellm/commit/e257bcc0f1e41a6280c9413338bf510a4a765e45)

`e257bcc`


`84ba01f`

[Compare](https://github.com/vllm-project/guidellm/compare/e257bcc0f1e41a6280c9413338bf510a4a765e45..84ba01f293e5c97d0b635b0079cf12869138262b)

May 3, 2026 11:25

Contributor
Author

|
|

Collaborator

|
I pushed a commit to fix a missing case and follow project requirements. |


**approved these changes**

[sjmonson](https://github.com/sjmonson)May 4, 2026

Signed-off-by: leehyeoklee <dlgur123456789@gmail.com>

Signed-off-by: leehyeoklee <dlgur123456789@gmail.com>

Assisted-by: Cursor AI Claude 4.6 Opus High Thinking Signed-off-by: Jared O'Connell <joconnel@redhat.com>

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/83981299f56e08333ab3292c6ecaa40099c76df0..6e6d3e1031295ecc6861870f8e88fb39b388ef1a)the feature/csv-column-alignment branch from

[to](https://github.com/vllm-project/guidellm/commit/83981299f56e08333ab3292c6ecaa40099c76df0)

`8398129`


`6e6d3e1`

[Compare](https://github.com/vllm-project/guidellm/compare/83981299f56e08333ab3292c6ecaa40099c76df0..6e6d3e1031295ecc6861870f8e88fb39b388ef1a)

May 4, 2026 18:21


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)May 4, 2026

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary:

Improve the CSV output formatter to dynamically construct a unified master header when running multiple benchmark profiles sequentially, preventing column misalignment by safely padding missing metrics.

## Details:

Currently, the CSV output formatter (

`GenerativeBenchmarkerCSV`

) locks the header structure of the entire result to the first executed benchmark when multiple benchmark profiles are run sequentially (sweep profile).As a result, if subsequent benchmarks measure new metrics or different modalities, it causes the data columns to misalign or break against the headers.

To resolve this, the logic was improved to dynamically construct a superset (master header) of all benchmark result headers and safely pad any missing metrics with empty strings.

## Test Plan:

## Before

## After

## Related Issues

## Use of AI

`## WRITTEN BY AI ##`

)