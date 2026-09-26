# [Issue #647] [RFC]: Agent-assisted RFC implementation via @claude in issue comments

source: https://github.com/vllm-project/speculators/issues/647
state: open | updated: 2026-09-22T19:56:10Z
labels: stale, RFC

## 正文

### Motivation.

The RFC-to-PR cycle involves manual effort that an agent could accelerate. vllm already uses Copilot SWE Agent; all four repos have Copilot code review. We'd like to add agent-assisted implementation to speculators, triggered by a human in issue comments — not autonomously.

### Proposed Change.

Add a GitHub Actions workflow so a maintainer can invoke an agent from an RFC issue comment (e.g. `@claude implement this` or `@copilot`). The agent reads the RFC, implements, runs `make quality` + `pytest`, and opens a **draft** PR linking the issue. A human reviews and checks the "I (a human) have reviewed the code" box before marking ready.

**Two options:**

| | Claude Code Action | Copilot SWE Agent |
|---|---|---|
| Trigger | `@claude` in comments | Assign to Copilot / `@copilot` |
| Config | Custom system prompts, MCP tools | Minimal |
| Precedent | Not yet used in our repos | Already in vllm |
| Setup | Workflow file + API key | Toggle in repo settings |

**Scope:** Pilot in speculators, expand later if it works.

### Any Other Things.

1. Is Copilot SWE Agent the team-wide standard, or can repos choose their own tooling?
2. Any preference between the two options?
3. Comfortable with agent-generated draft PRs given the human-review checkbox?

## 评论 (2)

### dsikka · 2026-06-24

This is a good idea but is limited in the tooling we currently have available:
1. `claude` isn't fully enabled for `speculators` as of yet
2. `copilot` isn't very good
3. `coderabbit` has some of this capability already (you can get it to open a PR based on another PR comment but it may not work with issue)

Ideally we can just use claude which I am trying to enable so assigning to myself

### github-actions[bot] · 2026-09-22

This issue has been automatically marked as stale because it has not had any activity within 90 days. It will be automatically closed if no further activity occurs within 30 days. Leave a comment if you feel this issue should remain open. Thank you!
