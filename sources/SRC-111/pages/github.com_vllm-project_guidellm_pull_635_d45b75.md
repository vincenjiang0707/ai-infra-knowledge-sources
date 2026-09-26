source: https://github.com/vllm-project/guidellm/pull/635

# Drop vLLM extras group - #635

Merged

Merged

## Conversation

Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/f339b31d2a1aaa64da0f4388c633569d0607fcbb..59e4971541728502bee7e78d513bc6cda81b71b8)the fix/drop_vllm_extra branch from

[to](https://github.com/vllm-project/guidellm/commit/f339b31d2a1aaa64da0f4388c633569d0607fcbb)

`f339b31`


`59e4971`

[Compare](https://github.com/vllm-project/guidellm/compare/f339b31d2a1aaa64da0f4388c633569d0607fcbb..59e4971541728502bee7e78d513bc6cda81b71b8)

March 13, 2026 21:06


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Mar 13, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)
Collaborator


There was a problem hiding this comment.

Looks OK. The disadvantage of not doing this in the context of [#596](https://github.com/vllm-project/guidellm/pull/596) is that I had to jump back there to verify the `pyproject.toml`

reversions. But it looks good... even if the CI doesn't actually do anything to verify that it *works*.


**approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Mar 16, 2026

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)
Collaborator


There was a problem hiding this comment.

This change is a totally valid direction to go. vLLM is so heavy of a dependency, and I made it so that the tests don't depend on it.

[docs/guides/vllm-python-backend.md](https://github.com/vllm-project/guidellm/pull/635/files/59e4971541728502bee7e78d513bc6cda81b71b8#diff-6cdb6702b7bb7de58196447a0dab973c99c7d8ac23f82e4a56c791181748ab3d)

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

Drop vLLM extras group and instruct users to install vLLM separately.

## Details

Had planned to put this in #596 but wanted to give @jaredoconnell a chance to respond. The main reasons to have an

`extras`

group is if multiple packages are needed to make an optional feature work or a specific version is needed. vLLM is neither of those things. Not having a vLLM extras group will simplify a lot of things on the locking side for the low cost of asking a user to do`pip install vllm guidellm`

instead of`pip install guidellm[vllm]`

. In fact, the vLLM backend container image does not even use the extras group since it is easier to just install GuideLLM into an existing vLLM image.## Related Issues

## Use of AI

`## WRITTEN BY AI ##`

)