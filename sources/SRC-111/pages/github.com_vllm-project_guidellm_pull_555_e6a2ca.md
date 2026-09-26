source: https://github.com/vllm-project/guidellm/pull/555

# Drop pylock - #555

Merged

Merged

[Drop pylock](https://github.com#top)#555

[Drop pylock](https://github.com#top)#555

## Conversation


**previously approved these changes**

[dbutenhof](https://github.com/dbutenhof)Jan 23, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)
Collaborator


There was a problem hiding this comment.

I think it's a little odd that you just commented out the lines in `lock.sh`

but removed them in `.pre-commit-config.yaml`

. Sure, they can be uncommented later to restore the export ... but the git history will always be here if we need it. Nevertheless, fine ...

Signed-off-by: Samuel Monson <smonson@redhat.com>

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/19b5b0536428bd0340192f4a9d6fd9d61792bd66..08523c6eea66b349f87e9560912d8e4e4efc67e2)the feat/drop_pylock branch from

[to](https://github.com/vllm-project/guidellm/commit/19b5b0536428bd0340192f4a9d6fd9d61792bd66)

`19b5b05`


`08523c6`

[Compare](https://github.com/vllm-project/guidellm/compare/19b5b0536428bd0340192f4a9d6fd9d61792bd66..08523c6eea66b349f87e9560912d8e4e4efc67e2)

January 23, 2026 21:38


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Jan 23, 2026

Collaborator
Author

|
I commented them out because I am a code hoarder and needed someone to gently remind me its ok to let go. |

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

The workflow in #553 is failing due to lack of permissions. Rather than spend more time on this fragile hack. Drop the pylock for now. If we see a need later we can revive support.

## Details

See #553 (comment)

## Use of AI

`## WRITTEN BY AI ##`

)