# [Issue #4224] Enable GitHub Discussions for threaded, async project conversations

source: https://github.com/LMCache/LMCache/issues/4224
state: open | updated: 2026-09-26T01:45:59Z
labels: stale

## 正文

**Label**

This is a `new feature` request (leaving labeling to maintainers per the board conventions).

**Is your feature request related to a problem? Please describe.**

Issues are the right home for *tracked, actionable* work, but the project has no dedicated space for open-ended, threaded, asynchronous conversation about changes and needs — design proposals/RFCs, "should we do X?" questions, community Q&A, and direction-setting discussion. Today these either get filed as Issues (cluttering the actionable backlog and lacking threading) or happen in Slack (ephemeral, not searchable/indexed, and not linkable to the code or to future work). This sort of community-wide asynchronous and threaded discussion doesn't fit well on Slack or in PRs, yet it's a key part of the communication triangle of an Open Source project.

**Describe the solution you'd like**

Enable **GitHub Discussions** (repo Settings → Features → Discussions) as the home for async, threaded conversation directly relevant to project changes and needs. Suggested starting categories: *Announcements*, *Ideas / RFCs*, *Q&A*, *Design & direction*, and *Show and tell*.

The key benefit is a clean lifecycle from conversation to shipped change, keeping a single, stable reference thread:

1. **Discussion → issue.** When a discussion matures into concrete, actionable work, GitHub can *create an issue from the discussion*, moving it onto the tracked backlog while keeping a link back to the originating discussion.
2. **Issue → pull request, same number.** Because issues and pull requests share **one numbering sequence** in a repo, that issue can then be converted into a pull request that **keeps the same number** — GitHub's "create a PR from an issue" (REST `POST /repos/{owner}/{repo}/pulls` with the `issue` parameter, also exposed by `gh`/`hub`) turns issue `#N` into PR `#N`.

So the artifact number stays stable across the actionable phase — **issue `#N` becomes PR `#N`** — giving reviewers one durable reference from tracked work through merge, with the original discussion linked for context.

**Describe alternatives you've considered**

- **Slack** — great for real-time chat, but ephemeral, not indexed/searchable long-term, and not linkable to issues/PRs/commits.
- **Using Issues for open-ended discussion** — clutters the actionable backlog, has no threading, and makes triage of "real" work harder.
- **External forums** — fragments the community off-platform and away from the code.

**Additional context**

Discussions are free for public repositories, moderated with the repo's existing permission model, and share the same @mentions and cross-references as Issues/PRs. They're widely used across the PyTorch and CNCF ecosystems for RFCs and Q&A, although they have broader discussions on mailing lists (groups.google.com), which is a discussion to have in the future. Enabling is a one-time repo setting; categories can be curated afterward.

## 评论 (2)

### ApostaC · 2026-07-27

Nice suggestion! Enabled it (see #4272 )

Should we broadcast it in the slack channel as well?

### github-actions[bot] · 2026-09-26

This issue has been automatically marked as stale because it has not had activity within 60 days. It will be automatically closed if no further activity occurs within 30 days.
