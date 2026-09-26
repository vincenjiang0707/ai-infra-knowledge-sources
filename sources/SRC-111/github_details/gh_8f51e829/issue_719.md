# [Issue #719] --output-extras arg documented, but not implemented?

source: https://github.com/vllm-project/guidellm/issues/719
state: closed | updated: 2026-07-25T12:58:00Z
labels: documentation

## 正文

### Location

https://github.com/vllm-project/guidellm/blob/main/docs/guides/outputs.md#output-types

### Issue Type

Typo/Grammar

### Proposed Changes

```markdown
actually it's a useful flag, would be nice to have it
```

### Additional Context

_No response_

## 评论 (2)

### sjmonson · 2026-05-12

This is a flag we lost in v0.4.0. Scoping this under the new CLI refactor. Should probably be called something like `--metadata` or `--labels` since `--output-extras` is not very descriptive.

### dbutenhof · 2026-07-25

Resolved by the addition of `--label` in 0.7.1.
