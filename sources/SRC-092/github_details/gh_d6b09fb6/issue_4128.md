# [Issue #4128] [Feature Request]: Support GPU buffers in Mooncake Store NOF reads and writes

source: https://github.com/kvcache-ai/Mooncake/issues/4128
state: open | updated: 2026-09-16T02:49:13Z
labels: 

## 正文

### Describe your feature request

Clients such as vLLM keep KV cache data in GPU memory and pass GPU buffers to Mooncake Store Client. The existing NOF path uses SPDK for I/O and requires contiguous CPU DMA buffers, so it cannot directly handle these GPU pointers.

Add CPU staging in Store Client to support the following data paths:

- PUT: Gather GPU slices into a contiguous CPU DMA buffer, then write it to NOF.
- GET: Read NOF data into a CPU DMA buffer, then scatter it into the destination GPU slices.

The client should select staging automatically when a NOF replica is used with GPU buffers, and support non-contiguous GPU slices and batched reads and writes.

This would allow clients such as vLLM to use the NOF backend through the native Mooncake Store PUT/GET APIs.

### Before submitting a new issue...

- [x] Make sure you already searched for relevant issues and read the [documentation](https://kvcache-ai.github.io/Mooncake/)

## 评论 (2)

### github-actions[bot] · 2026-09-15

Thanks for opening this issue, @cage-goat!

| Field | Value |
|-------|-------|
| **Issue** | #4128 |
| **GitHub user ID** | `318081269` |
| **Reporter** | @cage-goat |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.

### cage-goat · 2026-09-15

I have a local commit implementing CPU staging for GPU buffer reads and writes through the NOF backend. I'll open a PR with the implementation.
