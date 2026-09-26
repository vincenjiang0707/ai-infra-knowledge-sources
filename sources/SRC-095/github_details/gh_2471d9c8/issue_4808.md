# [Issue #4808] [Feature] Add AGENTS.md for AI coding agent context

source: https://github.com/ray-project/kuberay/issues/4808
state: open | updated: 2026-09-23T04:42:57Z
labels: enhancement, stale

## 正文

### Search before asking

- [x] I had searched in the [issues](https://github.com/ray-project/kuberay/issues) and found no similar feature requirement.


### Description

I'd like to propose adding an `AGENTS.md` file to the repository root, along with a `CLAUDE.md` symlink pointing to it.
   This follows the emerging best practice of providing AI coding agents (Claude Code, Codex, Cursor, GitHub Copilot,
  etc.) with repository context so they can work more effectively.                                                       
                  
  The file would document:                                                                                               
   
  * **Repository structure**: The monorepo layout (`ray-operator/`, `apiserver/`, `kubectl-plugin/`, `helm-chart/`,  `dashboard/`, `clients/`) and that `ray-operator/` is the primary component.
                                                                                                                         
  * **Build and test commands**: Key `make` targets (`make build`, `make test`, `make lint`, `make manifests`, `make  generate`, `make helm`) and where to run them from.
                                                                                                                         
  * **Single-file commands**: How to lint or format individual files (`golangci-lint run ./path/to/file.go`, `gofumpt -w  path/to/file.go`).
 
 * **Code generation workflow**: The sequence to follow after modifying API types (`make generate && make manifests &&  make helm`).                                                                                                           
                                                                                                                         
  * **Coding conventions**: Import ordering, formatting (gofumpt), line length (120), nolint directive requirements, and pre-commit hook details.                                                                                               
                                                                                                                         
  Using `AGENTS.md` as the source of truth (cross-tool convention) with a `CLAUDE.md` symlink keeps a single file to maintain while ensuring compatibility with Claude Code, which auto-discovers `CLAUDE.md`.                              
                                                                                                                         
  This is a docs-only change — no code is modified. The file would be kept under 150 lines to stay concise.      

### Use case

AI coding agents are increasingly used for development tasks across open source projects. Without a context file,  agents must rediscover the repo layout, build commands, and conventions from scratch each session — leading to slower iteration, incorrect commands, and style violations. A lightweight context file eliminates this friction and makes the project more accessible to AI-assisted contributors.

### Related issues

no related issues

### Are you willing to submit a PR?

- [x] Yes I am willing to submit a PR!

## 评论 (2)

### abiazett · 2026-05-07

PR created: https://github.com/ray-project/kuberay/pull/4809                                                           


### github-actions[bot] · 2026-09-23

This issue has been automatically marked as stale because it has not had
any activity for 120 days. It will be closed in 14 days if no further activity occurs.

If you'd like to keep this issue open, just leave any comment, and the stale label will be removed.
If you'd like to get more attention on this issue, please tag one of the KubeRay maintainers.

You can always ask for help on [Ray's public Slack channel](https://github.com/ray-project/kuberay#getting-involved).
