source: https://github.com/vllm-project/guidellm/pull/714

# Add AGENTS.md - #714

[Add AGENTS.md](https://github.com#top)#714

[Add AGENTS.md](https://github.com#top)#714

## Conversation

###
**
**[Copilot](https://github.com/apps/copilot-pull-request-reviewer)
AI
left a comment

**left a comment**

[Copilot](https://github.com/apps/copilot-pull-request-reviewer)AI

There was a problem hiding this comment.

## Pull request overview

Adds repository-level guidance for AI agents/external contributors by introducing an `AGENTS.md`

with development commands and quality standards, plus a `.gitignore`

update to avoid committing local Claude-related files.

**Changes:**

- Add
`AGENTS.md`

describing tox-based workflows, pytest markers, and quality/style expectations. - Update
`.gitignore`

to ignore`CLAUDE.*`

files.

### Reviewed changes

Copilot reviewed 1 out of 2 changed files in this pull request and generated 5 comments.

| File | Description |
|---|---|
| AGENTS.md | New contributor/agent guidance for running tests, linting/type checks, and repository standards. |
| .gitignore | Adds an ignore rule for local Claude-related files (`CLAUDE.*` ). |

💡 [Add Copilot custom instructions](https://github.com/vllm-project/guidellm/new/main?filename=.github/instructions/*.instructions.md) for smarter, more guided reviews. [Learn how to get started](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot).


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)May 4, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

👍🏻 -- this is a great start. Locking out CLAUDE<.md> is not a bad choice, but there are "implications" for generalization of this (e.g., `.claude`

& `.cursor`

directories, etc.). Not really sure how far we want to take this out of the gate, but "discriminating" against just the base `CLAUDE.md`

sticks a big warning sign in the road... maybe that's good, maybe that's bad...

[.gitignore](https://github.com/vllm-project/guidellm/pull/714/files#diff-bc37d034bad564583790a46f19d807abfe519c5671395fd494d8cce506c42947)


**previously approved these changes**

[dbutenhof](https://github.com/dbutenhof)May 4, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

👍🏻 -- great start. Ignoring CLAUDE-specific agent files isn't a bad choice, but there are "implications" for generalization of this (e.g., `.claude`

& `.cursor`

directories).

I'm not sure how far we want to take this out of the gate, but "discriminating" against just the one prototypical file seems to raise a bit of a red flag... maybe that's good, maybe that's bad...

|
Weird -- GitHub rejected several attempt to submit my review with weird messages, but posted copies of the summary comment anyway. |

Another one of those days... |


**previously approved these changes**

[dbutenhof](https://github.com/dbutenhof)May 4, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

We should probably consider adding something to the CONTRIBUTING readme along the lines "don't add any agent skill or rule files without prior consultation with the team" ... but we always have the PR process as protection so it's not a big deal.

Signed-off-by: Samuel Monson <smonson@redhat.com>

Co-authored-by: Copilot Autofix powered by AI <175728472+Copilot@users.noreply.github.com> Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>


**previously approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)May 4, 2026

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)

There was a problem hiding this comment.

Looks good. I just have one question.

[AGENTS.md](https://github.com/vllm-project/guidellm/pull/714/files/284d2d05c25ced02de1bfd2d5336c4e4b3fca27d#diff-a54ff182c7e8acf56acfd6e4b9c3ff41e2c41a31c9b211b2deb9df75d9a478f9)Outdated

|
Oh yeah, and one more thing that should likely be done is update the PR template to specify the same quantity of # around the WRITTEN BY AI message. |

Signed-off-by: Samuel Monson <smonson@redhat.com>

Changing it was an accident in the PR which I originally deemed unimportant to fix. Since you mentioned it I have pushed up a fix. |


**approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)May 4, 2026

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

## Summary

Adds an

`AGENTS.md`

to codify some of our common development practices.## Details

This PR adds a simple

`AGENTS.md`

in the hope that we will save some back-and-forth with external contributors in the future. I went with`AGENTS.md`

rather then`CLAUDE.md`

because (a) it is a standard and (b) I prefer to maintain my`CLAUDE.md`

with hints to my local environment.Some follow-up is needed after this PR to address other common pain points such as sloppy code commenting, bad filenames, and duplicative code but those will require a lot more trial and error to find what prompting works.

## Use of AI

`## WRITTEN BY AI ##`

)