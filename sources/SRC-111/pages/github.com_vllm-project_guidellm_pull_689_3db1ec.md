source: https://github.com/vllm-project/guidellm/pull/689

# Fix long import times due to processing all pydantic subclasses - #689

Merged

[jaredoconnell](https://github.com/jaredoconnell)merged 3 commits into

Merged

## Conversation

Other libraries that use pydantic could end up being processed by GuideLLM, significantly increasing the number of classes processed, noticeably increasing import times for GuideLLM. Assisted-by: Cursor AI Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Signed-off-by: Jared O'Connell <joconnel@redhat.com>


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Apr 10, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)
Collaborator


There was a problem hiding this comment.

Excellent! But, as Webb might say, just a few nits ...

[src/guidellm/schemas/base.py](https://github.com/vllm-project/guidellm/pull/689/files/31f92a9e75c1131abc266cea8daeca25a9222a58#diff-708f149be065456469b7819b56d3e258168ab1f0f167bbd6d8795143ea224da8)

[src/guidellm/schemas/base.py](https://github.com/vllm-project/guidellm/pull/689/files/31f92a9e75c1131abc266cea8daeca25a9222a58#diff-708f149be065456469b7819b56d3e258168ab1f0f167bbd6d8795143ea224da8)

Collaborator

|
Ha -- you might consider modifying the PR title: it's an incomplete sentence, and it displays as "Fix long import times due to |


[jaredoconnell](https://github.com/jaredoconnell)changed the title

Apr 10, 2026


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Apr 13, 2026

[src/guidellm/schemas/base.py](https://github.com/vllm-project/guidellm/pull/689/files/31f92a9e75c1131abc266cea8daeca25a9222a58#diff-708f149be065456469b7819b56d3e258168ab1f0f167bbd6d8795143ea224da8)

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

Other libraries that use pydantic could end up being processed by GuideLLM, significantly increasing the number of classes processed, noticeably increasing import times for GuideLLM.

Also, in my testing, it makes it so the startup times are less than half of what they were before.

## Details

`BenchmarkConfig`

,`BenchmarkGenerativeTextArgs`

, and`Profile`

,## Test Plan

## Related Issues

`import guidellm`

can take a very long time in some environments #688## Use of AI

`## WRITTEN BY AI ##`

)