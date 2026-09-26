source: https://github.com/vllm-project/guidellm/pull/875

# Fix for being unable to specify "benchmarks" in a config - #875

Merged

Merged

## Conversation

When the config and CLI arguments were merged the default list of benchmarks from the CLI was `[]` which alawys overrode the config since we do not merge lists. Here we add a special sentinel value that is used by the CLI to indicate no input. Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)
Collaborator


There was a problem hiding this comment.

This needs tests to prevent this from happening again.


**previously approved these changes**

[dbutenhof](https://github.com/dbutenhof)Jul 1, 2026

Contributor

|
Queued — the merge queue status continues in |

Assisted-by: GitHub Copilot GPT-4.1 Signed-off-by: Samuel Monson <smonson@redhat.com>


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Jul 1, 2026

Contributor

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

[SkiHatDuckie](https://github.com/SkiHatDuckie)pushed a commit to SkiHatDuckie/guidellm that referenced this pull request

Jul 2, 2026

[…t#875]) ## Summary The CLI was overriding a configs "benchmarks" with an empty list. This PR fixes it. Also restores the ability to provide a `benchmarks.json` to the config option. --- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [ ] Includes code generated or substantially modified by an AI agent - [ ] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- # git log commit[Author: Samuel Monson <smonson@redhat.com> Date: Wed Jul 1 11:37:28 2026 -0400 Fix specifying `benchmarks` in config When the config and CLI arguments were merged the default list of benchmarks from the CLI was `[]` which alawys overrode the config since we do not merge lists. Here we add a special sentinel value that is used by the CLI to indicate no input. Signed-off-by: Samuel Monson <smonson@redhat.com> commit]744dc9f[Author: Samuel Monson <smonson@redhat.com> Date: Wed Jul 1 11:50:50 2026 -0400 Fix running a json output as a benchmark Signed-off-by: Samuel Monson <smonson@redhat.com> commit]229d80b[Author: Samuel Monson <smonson@redhat.com> Date: Wed Jul 1 14:10:57 2026 -0400 Add some regression tests Assisted-by: GitHub Copilot GPT-4.1 Signed-off-by: Samuel Monson <smonson@redhat.com> --------- Assisted-by: GitHub Copilot GPT-4.1 Signed-off-by: Samuel Monson <smonson@redhat.com>]726d2ce

[SkiHatDuckie](https://github.com/SkiHatDuckie)pushed a commit to SkiHatDuckie/guidellm that referenced this pull request

Jul 6, 2026

[…t#875]) ## Summary The CLI was overriding a configs "benchmarks" with an empty list. This PR fixes it. Also restores the ability to provide a `benchmarks.json` to the config option. --- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [ ] Includes code generated or substantially modified by an AI agent - [ ] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- # git log commit[Author: Samuel Monson <smonson@redhat.com> Date: Wed Jul 1 11:37:28 2026 -0400 Fix specifying `benchmarks` in config When the config and CLI arguments were merged the default list of benchmarks from the CLI was `[]` which alawys overrode the config since we do not merge lists. Here we add a special sentinel value that is used by the CLI to indicate no input. Signed-off-by: Samuel Monson <smonson@redhat.com> commit]744dc9f[Author: Samuel Monson <smonson@redhat.com> Date: Wed Jul 1 11:50:50 2026 -0400 Fix running a json output as a benchmark Signed-off-by: Samuel Monson <smonson@redhat.com> commit]229d80b[Author: Samuel Monson <smonson@redhat.com> Date: Wed Jul 1 14:10:57 2026 -0400 Add some regression tests Assisted-by: GitHub Copilot GPT-4.1 Signed-off-by: Samuel Monson <smonson@redhat.com> --------- Assisted-by: GitHub Copilot GPT-4.1 Signed-off-by: Samuel Monson <smonson@redhat.com>]726d2ce

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

The CLI was overriding a configs "benchmarks" with an empty list. This PR fixes it. Also restores the ability to provide a

`benchmarks.json`

to the config option.## Use of AI

## git log

commit

744dc9fAuthor: Samuel Monson smonson@redhat.com

Date: Wed Jul 1 11:37:28 2026 -0400

commit

229d80bAuthor: Samuel Monson smonson@redhat.com

Date: Wed Jul 1 11:50:50 2026 -0400

commit

726d2ceAuthor: Samuel Monson smonson@redhat.com

Date: Wed Jul 1 14:10:57 2026 -0400

Assisted-by: GitHub Copilot GPT-4.1

Signed-off-by: Samuel Monson smonson@redhat.com