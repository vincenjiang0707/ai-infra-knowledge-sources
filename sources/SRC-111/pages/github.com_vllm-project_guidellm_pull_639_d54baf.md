source: https://github.com/vllm-project/guidellm/pull/639

# Fix file extension not being sent to output handler - #639

Merged

Merged

## Conversation

This fixes YAML outputs. Generated-by: Cursor AI Signed-off-by: Jared O'Connell <joconnel@redhat.com>

[jaredoconnell](https://github.com/jaredoconnell)

[force-pushed](https://github.com/vllm-project/guidellm/compare/1bcedc80a05403d0485cd7e70f021370d785b21a..df012d800774a31a6176da6f1d05f89051b8548f)the fix/yaml-output branch from

[to](https://github.com/vllm-project/guidellm/commit/1bcedc80a05403d0485cd7e70f021370d785b21a)

`1bcedc8`


`df012d8`

[Compare](https://github.com/vllm-project/guidellm/compare/1bcedc80a05403d0485cd7e70f021370d785b21a..df012d800774a31a6176da6f1d05f89051b8548f)

March 17, 2026 18:46


**previously approved these changes**

[sjmonson](https://github.com/sjmonson)Mar 17, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)
Collaborator


There was a problem hiding this comment.

As long as CI passes LGTM


**previously approved these changes**

[dbutenhof](https://github.com/dbutenhof)Mar 17, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)
Collaborator


There was a problem hiding this comment.

Yeah; functionally this looks good. My only minor concern is that the regression tests aren't really testing what you think they're testing ... that is, the ones that read in the generated report would pass with the *current* code as well as your fix since JSON *is* valid YAML ...

[tests/unit/benchmark/test_serialized_output.py](https://github.com/vllm-project/guidellm/pull/639/files/df012d800774a31a6176da6f1d05f89051b8548f#diff-fd5dd36bab301a010e127888d0e78d7a5f07b94ee3e1f2c8a539fc954155bdf8)

Generated-by: Cursor AI Signed-off-by: Jared O'Connell <joconnel@redhat.com>


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Mar 17, 2026

[tests/unit/benchmark/test_serialized_output.py](https://github.com/vllm-project/guidellm/pull/639/files/df012d800774a31a6176da6f1d05f89051b8548f#diff-fd5dd36bab301a010e127888d0e78d7a5f07b94ee3e1f2c8a539fc954155bdf8)


[dbutenhof](https://github.com/dbutenhof)added

[bug](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Abug)

[escape](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Aescape)

Apr 10, 2026

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

Fixes YAML output when specified with --outputs yaml

## Details

Previously, when you did not specify a file name, and just "yaml", it didn't specify a file name to the handler, resulting in it just using the default file name, which is

`benchmarks.json`

, resulting in JSON.It now specifies the file extension and properly uses that.

## Test Plan

There are now dedicated tests for this, and you can manually test it with

`--outputs yaml`

## Related Issues

## Use of AI

`## WRITTEN BY AI ##`

)