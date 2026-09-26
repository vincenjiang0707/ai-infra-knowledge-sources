# [Issue #3736] [Bug]: NoF zero-copy transfer fails with "No translation for ptr" when using MooncakeHostTensorAllocator in SGLang

source: https://github.com/kvcache-ai/Mooncake/issues/3736
state: closed | updated: 2026-09-17T02:50:51Z
labels: bug

## 正文

### Bug Report

When using MooncakeStore as the L3 storage backend for SGLang HiCache with NoF (NVMe-oF) zero-copy transfer enabled, KV cache transfer fails with the following error:

<img width="1892" height="452" alt="Image" src="https://github.com/user-attachments/assets/d2d6da37-99c9-4f21-bb73-52667ab36356" />

Root Cause
SGLang's MooncakeHostTensorAllocator uses MooncakeHostMemAllocator → ShmHelper (memfd + mmap) to allocate host memory. However, this memory is never registered with SPDK via spdk_mem_register(). SPDK's RDMA transport requires all DMA-capable memory to be pre-registered; otherwise, spdk_rdma_get_translation() fails with No translation for ptr.



### Before submitting...

- [ ] Ensure you searched for relevant issues and read the [documentation]

## 评论 (2)

### NUABO · 2026-08-27

fix in https://github.com/kvcache-ai/Mooncake/pull/3717

### github-actions[bot] · 2026-08-27

Thanks for opening this issue, @NUABO!

| Field | Value |
|-------|-------|
| **Issue** | #3736 |
| **GitHub user ID** | `29769310` |
| **Reporter** | @NUABO |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.
