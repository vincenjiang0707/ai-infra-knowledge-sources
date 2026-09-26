source: https://github.com/vllm-project/guidellm/pull/619

# Add detail in benchmark profile documentation - #619

Merged

Merged

## Conversation

[dbutenhof](https://github.com/dbutenhof)

[force-pushed](https://github.com/vllm-project/guidellm/compare/de714247a1655596b190e7717260498aae513a08..4db0c590f5af61e47456961e563355f1d3aa0623)the feature/ratedoc branch from

[to](https://github.com/vllm-project/guidellm/commit/de714247a1655596b190e7717260498aae513a08)

`de71424`


`4db0c59`

[Compare](https://github.com/vllm-project/guidellm/compare/de714247a1655596b190e7717260498aae513a08..4db0c590f5af61e47456961e563355f1d3aa0623)

March 3, 2026 17:44

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)
Collaborator


There was a problem hiding this comment.

Looks good so far. I have a few comments.

[docs/getting-started/benchmark.md](https://github.com/vllm-project/guidellm/pull/619/files#diff-814d89ed16bd4644a4a05515d85d58e412ef428e6611c8e4fff8c3b667947dc2)Outdated

[docs/getting-started/benchmark.md](https://github.com/vllm-project/guidellm/pull/619/files#diff-814d89ed16bd4644a4a05515d85d58e412ef428e6611c8e4fff8c3b667947dc2)Outdated

[docs/getting-started/benchmark.md](https://github.com/vllm-project/guidellm/pull/619/files#diff-814d89ed16bd4644a4a05515d85d58e412ef428e6611c8e4fff8c3b667947dc2)Outdated

[docs/getting-started/benchmark.md](https://github.com/vllm-project/guidellm/pull/619/files#diff-814d89ed16bd4644a4a05515d85d58e412ef428e6611c8e4fff8c3b667947dc2)Outdated

[docs/getting-started/benchmark.md](https://github.com/vllm-project/guidellm/pull/619/files#diff-814d89ed16bd4644a4a05515d85d58e412ef428e6611c8e4fff8c3b667947dc2)Outdated

[dbutenhof](https://github.com/dbutenhof)

[force-pushed](https://github.com/vllm-project/guidellm/compare/4db0c590f5af61e47456961e563355f1d3aa0623..478729df755612a03ecd0e375336e42622e0453b)the feature/ratedoc branch from

[to](https://github.com/vllm-project/guidellm/commit/4db0c590f5af61e47456961e563355f1d3aa0623)

`4db0c59`


`478729d`

[Compare](https://github.com/vllm-project/guidellm/compare/4db0c590f5af61e47456961e563355f1d3aa0623..478729df755612a03ecd0e375336e42622e0453b)

March 4, 2026 20:50


**requested changes**

[sjmonson](https://github.com/sjmonson)Mar 5, 2026

[docs/getting-started/benchmark.md](https://github.com/vllm-project/guidellm/pull/619/files#diff-814d89ed16bd4644a4a05515d85d58e412ef428e6611c8e4fff8c3b667947dc2)Outdated


**previously approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Mar 6, 2026


**previously approved these changes**

[sjmonson](https://github.com/sjmonson)Mar 10, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)
Collaborator


There was a problem hiding this comment.

New docs looks good but one minor change to existing docs.

[docs/getting-started/benchmark.md](https://github.com/vllm-project/guidellm/pull/619/files#diff-814d89ed16bd4644a4a05515d85d58e412ef428e6611c8e4fff8c3b667947dc2)Outdated

Attempt to clarify the interactions of `--rate` and the count and time-based constraints with the various benchmarking profiles; especially sweep, which presents effects that aren't obvious at first glance. This is a first attempt to mitigate the implications of[vllm-project#588]with a clear warning that the global constraints are implemented separately for each strategy, and that sweep especially includes multiple strategies. Signed-off-by: David Butenhof <dbutenho@redhat.com>

Signed-off-by: David Butenhof <dbutenho@redhat.com>

I've always been bugged by the small "Data options" subsection followed by the "Working with real data" section; I reorganized a bit more radically... Signed-off-by: David Butenhof <dbutenho@redhat.com>

[dbutenhof](https://github.com/dbutenhof)

[force-pushed](https://github.com/vllm-project/guidellm/compare/433157e4fec43f082ec52b10200d27b1e0fc924c..23c51ef18d329d6c3d2af030348416024e7ca99f)the feature/ratedoc branch from

[to](https://github.com/vllm-project/guidellm/commit/433157e4fec43f082ec52b10200d27b1e0fc924c)

`433157e`


`23c51ef`

[Compare](https://github.com/vllm-project/guidellm/compare/433157e4fec43f082ec52b10200d27b1e0fc924c..23c51ef18d329d6c3d2af030348416024e7ca99f)

March 10, 2026 19:33


**approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Mar 10, 2026

Collaborator

|
Looks good except you need to fix the signoff. |

Signed-off-by: David Butenhof <dbutenho@redhat.com>

[dbutenhof](https://github.com/dbutenhof)

[force-pushed](https://github.com/vllm-project/guidellm/compare/23c51ef18d329d6c3d2af030348416024e7ca99f..ae52be603c222123b2e83a5b043ba976203f465f)the feature/ratedoc branch from

[to](https://github.com/vllm-project/guidellm/commit/23c51ef18d329d6c3d2af030348416024e7ca99f)

`23c51ef`


`ae52be6`

[Compare](https://github.com/vllm-project/guidellm/compare/23c51ef18d329d6c3d2af030348416024e7ca99f..ae52be603c222123b2e83a5b043ba976203f465f)

March 11, 2026 11:30

Collaborator
Author

Ouch ... I keep just pushing "Commit" in Cursor, which, despite following all the instructions I'd found, still fails to sign by default. But on a whim I searched through the Cursor settings and found a checkbox ... hopefully it'll work next time. (And at least I aspire to remember to confirm with |


**approved these changes**

[sjmonson](https://github.com/sjmonson)Mar 11, 2026

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

Attempt to clarify the interactions of

`--rate`

and the count and time-based constraints with the various benchmarking profiles; especially sweep, which presents effects that aren't obvious at first glance.## Details

The simple list of profiles is broken up into sub-sections with more detail on behavior and interactions to, hopefully, aid in understanding.

## Test Plan

N/A

## Related Issues

This is a first attempt to mitigate the implications of #588 with a clear warning that the global constraints are implemented separately for each strategy, and that sweep especially includes multiple strategies. We expect that future work will allow specifying separate constraints for each strategy.

## Use of AI

`## WRITTEN BY AI ##`

)