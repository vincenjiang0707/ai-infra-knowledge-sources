# [Issue #2714] Improve issue and PR label automation

source: https://github.com/vllm-project/aibrix/issues/2714
state: closed | updated: 2026-09-16T05:58:50Z
labels: good first issue, help wanted, kind/misc, area/cicd

## 正文

## Background

AIBrix currently uses automation to label Issues and Pull Requests.

Related work:

- #2696 [Add local AIBrix workflow bot](https://github.com/vllm-project/aibrix/pull/2696)
- #2711 [Add path-based PR labeler](https://github.com/vllm-project/aibrix/pull/2711)

These two PRs improved the labeling workflow, but the problem is not fully resolved.

## Problem

Issue labeling can still assign unrelated `area/*` labels because the bot matches broad keywords across the entire Issue body.

PR and Issue labeling also need a clearer separation. PR area labels should reflect the files changed by the PR, rather than keywords in the PR title or description.

## Proposed direction

Use repository templates as the primary source of label intent:

- Add default `kind/*` labels to Issue Forms where appropriate.
- Add an explicit `Area` field to Issue Forms.
- Add an `Area` selection section to the Pull Request template.
- Use changed file paths as the fallback for PR area labels.
- Use keyword matching only as a fallback for Issues.
- Avoid assigning multiple unrelated area labels automatically.
- Keep PR title/description validation separate from area labeling.
- Handle labels produced by previous bot versions consistently.

The previous two PRs made useful improvements, but did not fully solve the classification and ownership problem.

## 评论 (3)

### github-actions[bot] · 2026-09-12

<!-- aibrix-bot-guide -->
Thanks for contributing to AIBrix! Please review the [contribution guide](https://github.com/vllm-project/aibrix/blob/main/CONTRIBUTING.md) and make sure this issue contains enough context for maintainers to reproduce or evaluate it.


### Bryandero98 · 2026-09-14

Hi! I'd like to take this on — could I get it assigned to me?

### Bryandero98 · 2026-09-14

Opened #2729 for the Issue-labeling half of this (explicit Area field + keyword matching as fallback only). Scoped it separately from the PR-side labeling (already covered by #2711) and the remaining kind/* + PR-template bullets, since those are independent follow-ups rather than one large redesign. Happy to take those on too if that's the right scope - let me know.
