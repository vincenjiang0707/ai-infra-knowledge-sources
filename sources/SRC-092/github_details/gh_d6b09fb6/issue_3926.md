# [Issue #3926] [Bug] mooncake-store no longer builds on macOS: utils.h includes linux/memfd.h unconditionally since #3789

source: https://github.com/kvcache-ai/Mooncake/issues/3926
state: closed | updated: 2026-09-23T08:02:10Z
labels: 

## 正文

## What

`mooncake-store/include/utils.h:8-9` includes `<linux/memfd.h>` and `<linux/mman.h>` unconditionally since #3789 (512MB hugepage support). On macOS neither header exists, so every TU that includes `utils.h` stops at configure-time-include resolution:

```
mooncake-store/include/utils.h:8:10: fatal error: 'linux/memfd.h' file not found
    8 | #include <linux/memfd.h>
      |         ^
```

First failing target on a clean `cmake -DWITH_STORE=ON -DWITH_TE=OFF -DBUILD_UNIT_TESTS=ON` build: `mooncake_store_shared_objects.dir/mmap_arena.cpp.o` (also `utils.cpp.o`, `local_ssd/manager.cpp.o`, ...), macOS arm64, Apple Clang, SDK 15.x.

## Why it matters

The store still builds and ships a macOS wheel, and there is no macOS store-build lane in CI, so this slipped through silently. Local store development on Mac is broken on current main (`1caf8f8f9`).

## Suggested fix

Guard the Linux headers and the memfd flag path with `#ifdef __linux__` (the hugepage env query degrades to the default page size elsewhere; `utils.cpp`'s memfd use sites need the same guard). Happy to send that PR, it is small.

Found while building `master_service_test` locally for #3806; verified the failure reproduces on unmodified main.


## 评论 (2)

### github-actions[bot] · 2026-09-07

Thanks for opening this issue, @he-yufeng!

| Field | Value |
|-------|-------|
| **Issue** | #3926 |
| **GitHub user ID** | `40085740` |
| **Reporter** | @he-yufeng |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.

### he-yufeng · 2026-09-07

One more build-config finding from the same session, adjacent but distinct: with `WITH_TE=OFF` on Linux, `mooncake-store/src/utils.cpp:4` does `#include "common.h"`, which only exists under `mooncake-transfer-engine/include/` (and tests), so a TE-less store build fails too. TE=ON is the only working store configuration on main right now. If the store-only build is meant to stay supported, the hugepage helpers need their TE dependency declared or the include moved.
