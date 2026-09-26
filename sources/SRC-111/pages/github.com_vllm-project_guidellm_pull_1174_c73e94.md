source: https://github.com/vllm-project/guidellm/pull/1174

# Bump pygments v2.19.2 -> v2.21.0 - #1174

Merged

Merged

## Conversation

Signed-off-by: Samuel Monson <smonson@redhat.com>

[sjmonson](https://github.com/sjmonson)requested review from

[dbutenhof](https://github.com/dbutenhof),

[dfeddema](https://github.com/dfeddema)and

[jaredoconnell](https://github.com/jaredoconnell)as

[code owners](https://github.com/vllm-project/guidellm/blob/9d4fe2ff043c87fe906afec82cc65fc22b13972e/CODEOWNERS#L2)

September 22, 2026 17:56

Signed-off-by: Samuel Monson <smonson@redhat.com>


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Sep 22, 2026

Contributor

|
Received a single approval. Will automatically queue for merge once two maintainers approve, all change requests are resolved, and DCO passes. |

Contributor

|
Queued — the merge queue status continues in |

Contributor

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

35 tasks

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

A while back dependabot opened a PR to bump

`pygments`

due to a CVE. That PR broke due to changes on main and dependabot has been complaining since. I can't seem to get it to open a new PR so here is a manual fix.Also bump idna for similar reasons.

## Related Issues

## Use of AI

## git log

commit

9ba6074Author: Samuel Monson smonson@redhat.com

Date: Tue Sep 22 13:51:47 2026 -0400

commit

7baa71bAuthor: Samuel Monson smonson@redhat.com

Date: Tue Sep 22 14:01:32 2026 -0400

Signed-off-by: Samuel Monson smonson@redhat.com