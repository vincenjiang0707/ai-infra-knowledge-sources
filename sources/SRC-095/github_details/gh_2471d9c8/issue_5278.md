# [Issue #5278] [CI][History Server] Remove the gosec G110 lint exclusion by deleting the unused DecompressStream helper

source: https://github.com/ray-project/kuberay/issues/5278
state: open | updated: 2026-09-24T02:00:19Z
labels: enhancement, good-first-issue

## 正文

### Search before asking

- [x] I had searched in the [issues](https://github.com/ray-project/kuberay/issues) and found no similar feature requirement.


### KubeRay Component

historyserver

### Description

#5247 silences `gosec` G110 for the compression helper with this rule in `.golangci.yml`:

```yaml
- linters: [gosec]
  path: '^historyserver/pkg/compression/compression\.go$'
  text: '^G110:'
```

### Use case

_No response_

### Related issues

_No response_

### Are you willing to submit a PR?

- [ ] Yes I am willing to submit a PR!


## 评论 (2)

### kevinzeroCode · 2026-09-23

@CheyuWu Would like to take it up.

### kevinzeroCode · 2026-09-24

Ah, I see #5286 already covers this (pending #5247). I'll go find a different issue to work on instead — thanks!
