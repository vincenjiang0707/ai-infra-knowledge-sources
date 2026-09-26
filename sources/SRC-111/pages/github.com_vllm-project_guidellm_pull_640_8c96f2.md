source: https://github.com/vllm-project/guidellm/pull/640

# Fix and improve the mock server - #640

Merged

Merged

## Conversation

[jaredoconnell](https://github.com/jaredoconnell)

[force-pushed](https://github.com/vllm-project/guidellm/compare/31ebecb79c3972a2c22fccb6e0bf1e07f6f0d836..9959e34513f0a830def874c101a4a61782514aa5)the fix/mock-server branch from

[to](https://github.com/vllm-project/guidellm/commit/31ebecb79c3972a2c22fccb6e0bf1e07f6f0d836)

`31ebecb`


`9959e34`

[Compare](https://github.com/vllm-project/guidellm/compare/31ebecb79c3972a2c22fccb6e0bf1e07f6f0d836..9959e34513f0a830def874c101a4a61782514aa5)

March 17, 2026 20:12

Collaborator

|
|

Contributor

## ✅ Branch has been successfully rebased |

[dbutenhof](https://github.com/dbutenhof)

[force-pushed](https://github.com/vllm-project/guidellm/compare/9959e34513f0a830def874c101a4a61782514aa5..54f9cfbf8ac4331c1db34505e3df341b7a9e5e21)the fix/mock-server branch from

[to](https://github.com/vllm-project/guidellm/commit/9959e34513f0a830def874c101a4a61782514aa5)

`9959e34`


`54f9cfb`

[Compare](https://github.com/vllm-project/guidellm/compare/9959e34513f0a830def874c101a4a61782514aa5..54f9cfbf8ac4331c1db34505e3df341b7a9e5e21)

March 18, 2026 13:11


**previously approved these changes**

[dbutenhof](https://github.com/dbutenhof)Mar 18, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)
Collaborator


There was a problem hiding this comment.

Looks fine -- one question to clarify the motivation behind the logging change, but I don't object to the change.

[src/guidellm/mock_server/server.py](https://github.com/vllm-project/guidellm/pull/640/files#diff-f8bc55166ebb7c30251f1e2d9adf35e9bebb2673c42f31beff3adb7dc636710c)

[src/guidellm/mock_server/server.py](https://github.com/vllm-project/guidellm/pull/640/files#diff-f8bc55166ebb7c30251f1e2d9adf35e9bebb2673c42f31beff3adb7dc636710c)Outdated

This matches the format that GuideLLM uses for chat completions. Generated-by: Cursor AI Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Generated-by: Cursor AI Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Signed-off-by: Jared O'Connell <joconnel@redhat.com>

[jaredoconnell](https://github.com/jaredoconnell)

[force-pushed](https://github.com/vllm-project/guidellm/compare/5028e88bc2f6db5c85f0483b66b54323b2ed043a..a937a12261a3f338748861d064bbdf9db715a22b)the fix/mock-server branch from

[to](https://github.com/vllm-project/guidellm/commit/5028e88bc2f6db5c85f0483b66b54323b2ed043a)

`5028e88`


`a937a12`

[Compare](https://github.com/vllm-project/guidellm/compare/5028e88bc2f6db5c85f0483b66b54323b2ed043a..a937a12261a3f338748861d064bbdf9db715a22b)

March 18, 2026 15:17


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Mar 18, 2026

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

This fixes a few issues with the mock server, each in their own commits:

~~All logs were duplicated. Now they're not.~~## Test Plan

You can use the mock server to verify that it works.

There is also now a test for the list format requests.

## Use of AI

`## WRITTEN BY AI ##`

)