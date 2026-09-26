# [Issue #3451] [Usage]: AscendDirectTransport fails with “ctx js NULL” on CANN 9.1.0 and Mooncake 0.3.12

source: https://github.com/kvcache-ai/Mooncake/issues/3451
state: closed | updated: 2026-09-22T01:09:26Z
labels: 

## 正文

### Describe your usage question

Environment
•Hardware: Ascend 910B4
•HDK: 25.5.1
•CANN Docker Image: cann:9.1.0-910b-openeuler24.03-py3.12-devel
•Mooncake Version: 0.3.12.post1 (installed via pip install mooncake-transfer-engine-npu)

Questions
It seems the mooncake_store process did not properly initialize the ACL device context(aclrtSetDevice/aclrtCreateContext) or select the correct device before allocating the local segment under CANN 9.1.0.
Could you please confirm if this version combination is officially supported, or if there is any workaround/fix required? Thanks!

### Before submitting a new issue...

- [x] Make sure you already searched for relevant issues and read the [documentation](https://kvcache-ai.github.io/Mooncake/)

## 评论 (2)

### github-actions[bot] · 2026-08-15

Thanks for opening this issue, @biosyxh!

| Field | Value |
|-------|-------|
| **Issue** | #3451 |
| **GitHub user ID** | `38521349` |
| **Reporter** | @biosyxh |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.

### ascend-direct-dev · 2026-08-17

Please make sure the inference framework has called set_device, not mooncake store
