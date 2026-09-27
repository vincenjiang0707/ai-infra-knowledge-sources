# [Issue #4328] [Feature Request]:  support arm64 in `mooncake-transfer-engine-efa` python wheel

source: https://github.com/kvcache-ai/Mooncake/issues/4328
state: open | updated: 2026-09-25T20:35:30Z
labels: 

## 正文

### Describe your feature request

`mooncake-transfer-engine-efa` wheel supports only `x86_64` architecture but not `arm64`.
since AWS EFA supports `arm64` architecture already the effort needed here might be the validation and packaging multiarch wheel.

### Before submitting a new issue...

- [ ] Make sure you already searched for relevant issues and read the [documentation](https://kvcache-ai.github.io/Mooncake/)

## 评论 (1)

### github-actions[bot] · 2026-09-25

Thanks for opening this issue, @snadampal!

| Field | Value |
|-------|-------|
| **Issue** | #4328 |
| **GitHub user ID** | `87143774` |
| **Reporter** | @snadampal |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.
