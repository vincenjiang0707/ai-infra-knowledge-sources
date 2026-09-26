source: https://github.com/vllm-project/guidellm/pull/590

# Multiturn Benchmarking - #590

## Conversation

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/a68179f61f069a251016b272f875d6a5f2b7f755..ea34af199d74cead125018fbd094b3b74de956ba)the feat/multiturn branch 7 times, most recently from

[to](https://github.com/vllm-project/guidellm/commit/a68179f61f069a251016b272f875d6a5f2b7f755)

`a68179f`


`ea34af1`

[Compare](https://github.com/vllm-project/guidellm/compare/a68179f61f069a251016b272f875d6a5f2b7f755..ea34af199d74cead125018fbd094b3b74de956ba)

February 11, 2026 19:19

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/870a46edd921cc9d8a86157753ef07a036f93e1e..b039b6abd28657517d5ab341c4610ca957aedf73)the feat/multiturn branch 3 times, most recently from

[to](https://github.com/vllm-project/guidellm/commit/870a46edd921cc9d8a86157753ef07a036f93e1e)

`870a46e`


`b039b6a`

[Compare](https://github.com/vllm-project/guidellm/compare/870a46edd921cc9d8a86157753ef07a036f93e1e..b039b6abd28657517d5ab341c4610ca957aedf73)

February 11, 2026 21:44


**reviewed**

[dbutenhof](https://github.com/dbutenhof)Feb 18, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

A first pass to try to grok the landscape ... one comment; feel free to dismiss it if it's impractical for "reasons" not obvious to me from the context.

[src/guidellm/data/deserializers/synthetic.py](https://github.com/vllm-project/guidellm/pull/590/files#diff-4b48dc7631c1a28d1f1b7ca179feb42d01378082bc7c9b97bf3cd4bcc2c58a94)

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/1c95100f5dede20209f14b6422146d46417ed6c7..06a25f846eb8cb132ae52a7648bbbae54189392f)the feat/multiturn branch 4 times, most recently from

[to](https://github.com/vllm-project/guidellm/commit/1c95100f5dede20209f14b6422146d46417ed6c7)

`1c95100`


`06a25f8`

[Compare](https://github.com/vllm-project/guidellm/compare/1c95100f5dede20209f14b6422146d46417ed6c7..06a25f846eb8cb132ae52a7648bbbae54189392f)

March 3, 2026 22:10

[sjmonson](https://github.com/sjmonson)marked this pull request as ready for review

March 3, 2026 22:28


**commented**

[sjmonson](https://github.com/sjmonson)Mar 3, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)

There was a problem hiding this comment.

Note to reviewers: I tried pretty hard to keep each commit very focused and atomic so it may be helpful to review commit-by-commit.


**reviewed**

[dbutenhof](https://github.com/dbutenhof)Mar 4, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

I don't see anything that looks obviously broken (though I only skimmed the AI unit tests), so I'm approving ... but with some suggestions, a few questions, and an exasperated gripe or two about "Python and Python IDE support ... 😦"

[src/guidellm/data/preprocessors/mappers.py](https://github.com/vllm-project/guidellm/pull/590/files#diff-2099c62bd0e1315d94f5ca565b50198a0507b9f2818feba33fd14d29641e6deb)Outdated

[src/guidellm/data/builders.py](https://github.com/vllm-project/guidellm/pull/590/files#diff-3bd4f8c1ae0238fa5be2b89b1b443383bffd1da6f969a07543a04bd4fdc52a69)

[src/guidellm/scheduler/worker.py](https://github.com/vllm-project/guidellm/pull/590/files#diff-a2646f8d413b5691fb552d608e2f652695326bc23ea881bc9ab2f3ce666dc857)Outdated

[src/guidellm/scheduler/worker_group.py](https://github.com/vllm-project/guidellm/pull/590/files#diff-d97e4fc87c1fc2179794b3e877ce25caee6e903da76a77650ac1c75915c521c8)

[src/guidellm/schemas/info.py](https://github.com/vllm-project/guidellm/pull/590/files#diff-179053f40e2947d9c41d6c3d78a225bdb58b06d99bc62c0a3bcad6e15c19adda)Outdated

[src/guidellm/backends/openai/request_handlers.py](https://github.com/vllm-project/guidellm/pull/590/files#diff-60cfc62dcd68426ebab8f6d637eba19d6423ac6fe297be59efdfb943b9f0d79f)

[docs/guides/multiturn.md](https://github.com/vllm-project/guidellm/pull/590/files#diff-b8c613ed380ab7cd9bd8b09b3ba7f883c2f7233af1f1a5b79bcef3c14c2ef903)Outdated

[docs/guides/multiturn.md](https://github.com/vllm-project/guidellm/pull/590/files#diff-b8c613ed380ab7cd9bd8b09b3ba7f883c2f7233af1f1a5b79bcef3c14c2ef903)Outdated

[docs/guides/multiturn.md](https://github.com/vllm-project/guidellm/pull/590/files#diff-b8c613ed380ab7cd9bd8b09b3ba7f883c2f7233af1f1a5b79bcef3c14c2ef903)Outdated


**previously approved these changes**

[dbutenhof](https://github.com/dbutenhof)Mar 5, 2026

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)

There was a problem hiding this comment.

Looks good so far. I will continue reviewing on Monday.

[docs/guides/multiturn.md](https://github.com/vllm-project/guidellm/pull/590/files#diff-b8c613ed380ab7cd9bd8b09b3ba7f883c2f7233af1f1a5b79bcef3c14c2ef903)Outdated

[src/guidellm/backends/openai/request_handlers.py](https://github.com/vllm-project/guidellm/pull/590/files#diff-60cfc62dcd68426ebab8f6d637eba19d6423ac6fe297be59efdfb943b9f0d79f)Outdated


**previously approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Mar 9, 2026

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)

There was a problem hiding this comment.

Looks good to me. I tested it and inspected the output, and can confirm that the conversation history is included as expected. And I like that the request typing has been simplified compared to what was added in preparation for multi-turn during the recent refactor.

[src/guidellm/scheduler/worker_group.py](https://github.com/vllm-project/guidellm/pull/590/files#diff-d97e4fc87c1fc2179794b3e877ce25caee6e903da76a77650ac1c75915c521c8)

[sjmonson](https://github.com/sjmonson)added a commit that referenced this pull request

Mar 13, 2026

## Summary Adds formatting check to CI jobs and runs formatting against all files to ensure CI passes. ## Related Issues - Blocked by[#596]- Blocked by[#590]--- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [ ] Includes AI-assisted code completion - [ ] Includes code generated by an AI application - [ ] Includes AI-generated tests (NOTE: AI written tests should have a docstring that includes `## WRITTEN BY AI ##`)

|
This pull request has merge conflicts that must be resolved before it can be |

Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>

This reverts commit[. Signed-off-by: Samuel Monson <smonson@redhat.com>]1a1bddd

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

Signed-off-by: Samuel Monson <smonson@redhat.com>

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/c72e2b776600add13f5d626bb4dd8541d163a007..2bf1e4de59d3735d1f216cdc81952fda61b94de9)the feat/multiturn branch from

[to](https://github.com/vllm-project/guidellm/commit/c72e2b776600add13f5d626bb4dd8541d163a007)

`c72e2b7`


`2bf1e4d`

[Compare](https://github.com/vllm-project/guidellm/compare/c72e2b776600add13f5d626bb4dd8541d163a007..2bf1e4de59d3735d1f216cdc81952fda61b94de9)

March 13, 2026 18:17


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Mar 13, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

Looks good. And I watched the "needs rebase" label come and go, which was cool...

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

## Summary

Adds support for multiturn benchmarking. This is required for emulating advanced application flows such as agentic solutions.

## Details

Implements multiturn support in three areas:

`data`

for creating synthetic multiturn dataset as well as parsing user-provided datasets`scheduler`

for handling requests in turn groups and persisting history across requests`backends/http`

for formatting requests with history and responsesSome things missing from this PR that may be in a followup:

`turns_stdev`

,`turns_min`

, and`turns_max`

.`concurrent`

profile where conversations hold on to the concurrency semaphore (only truly useful when combined with delay)## Test Plan

See

`docs/guides/multiturn.md`

for some good examples.## Related Issues

## Use of AI

`## WRITTEN BY AI ##`

)