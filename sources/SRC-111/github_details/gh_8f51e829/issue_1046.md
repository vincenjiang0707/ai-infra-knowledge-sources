# [Issue #1046] Lazy load major submodules

source: https://github.com/vllm-project/guidellm/issues/1046
state: closed | updated: 2026-08-27T20:38:39Z
labels: priority-high, internal

## 正文

### Problem Statement

The data submodule contains a lot of expensive startup requirements, like `datasets` and `torch`. Since we currently eagerly load all submodules in GuideLLM except for the shims in `guidellm.extras`, all dependencies are loaded in workers which leads to very slow `spawn` startups.

### Proposed Solution

Importing major submodules (data/scheduler/backend) should be deferred until they are actually needed. This will require some refactoring to move things like the `*Args` classes out of each submodule since they are needed on launch in the CLI.

### Alternatives Considered

_No response_

### Usage Examples

```markdown

```

### Additional Context

_No response_

## 评论 (1)

### sjmonson · 2026-08-27

Completed by #1058 
