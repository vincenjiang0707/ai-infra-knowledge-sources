# [Issue #4055] [Bug]: Default transfer-engine allocator is not 64KB-aligned, breaking Ascend SVM

source: https://github.com/kvcache-ai/Mooncake/issues/4055
state: closed | updated: 2026-09-14T06:45:46Z
labels: 

## 正文

### Environment

- Hardware: Ascend 910B (NPU)
- Mooncake: `kvcache-ai/Mooncake` `main` (`mooncake-transfer-engine-npu` wheel / source build)
- Protocol: `rdma` / `tcp` / `ascend`

### Description

`initMemoryAllocator()` in
`mooncake-integration/transfer_engine/transfer_engine_py.cpp` falls back to plain `malloc` for
protocols such as `rdma`/`tcp`/`ascend`. Ascend SVM (`_devmm_mem_remote_map`) requires a 64KB
page-aligned `src_va` (`page_size == 65536`); an unaligned `malloc` address makes
`aclrtHostRegister` fail with EINVAL ("Src_va is zero or not page alignment"), cascading into
`HCCL HcclMemRegRoce` / `GE channel` errors (e.g. 503900).

### Steps to reproduce

1. Use a protocol that falls back to the default allocator (`rdma`/`tcp`/`ascend`).
2. Allocate a large buffer; the returned address is not 64KB-aligned.
3. On the cross-card SVM path, `aclrtHostRegister` fails with EINVAL.

### Expected behavior

The default allocator should return 64KB-aligned memory so Ascend SVM can map it.

### Proposed fix

Use `posix_memalign(64 * 1024, ...)` instead of `malloc` in the fallback path. See the linked
PR.


## 评论 (1)

### github-actions[bot] · 2026-09-11

Thanks for opening this issue, @gygdh-001!

| Field | Value |
|-------|-------|
| **Issue** | #4055 |
| **GitHub user ID** | `43057576` |
| **Reporter** | @gygdh-001 |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.
