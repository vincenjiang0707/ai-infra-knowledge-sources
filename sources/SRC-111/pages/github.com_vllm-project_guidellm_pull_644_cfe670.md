source: https://github.com/vllm-project/guidellm/pull/644

# Import utils from sub-submodules - #644

Merged

Merged

## Conversation

Signed-off-by: Samuel Monson <smonson@redhat.com>


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Mar 18, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)
Collaborator


There was a problem hiding this comment.

That looks straightforward!

Collaborator
Author

|
Tangential to this I've noticed in a few PRs that people don't quite understand the import hierarchy. Probably should codify it in the documentation somewhere, but for now here is a rough draft of what I think we are aiming for: ```
graph TD
subgraph "Utils"
Util[Messaging<br/>...]
end
subgraph "Extras"
Extra[vLLM<br/>vision<br/>audio]
end
Schema
Data
Scheduler
Backends
subgraph "Benchmark"
Benchmarker[Benchmarker<br/>...]
end
Benchmark --> Data
Benchmark --> Scheduler
Benchmark --> Backends
Benchmark --> Schema
Benchmark --> Util
Data --> Schema
Data --> Extra
Data --> Util
Scheduler --> Util
Scheduler --> Schema
Backends --> Util
Backends --> Schema
Extra --> Util
```
|


[dbutenhof](https://github.com/dbutenhof)added the

[cleanup](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Acleanup)

Apr 10, 2026

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

Prereq for some work on deferring imports.

`utils`

are designed to be self-contained anyways so this is a small lift.## Test Plan

As long as all tests pass I think we should be good.

## Use of AI

`## WRITTEN BY AI ##`

)