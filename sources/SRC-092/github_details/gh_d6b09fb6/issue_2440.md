# [Issue #2440] [Bug]: Execute mooncake+hixl, final destruction phase core

source: https://github.com/kvcache-ai/Mooncake/issues/2440
state: closed | updated: 2026-09-23T03:15:50Z
labels: bug, stale, auto-closed

## 正文

### Bug Report

#0  xxx in ?? () from /usr/lib64/libc.so.6
#1  xxx in raise () from /usr/lib64/libc.so.6
#2  xxx in abort () from /usr/lib64/libc.so.6
#3  xxx in ?? () from /usr/lib64/libc.so.6
#4  xxx in ?? () from /usr/lib64/libc.so.6
#5  xxx in ?? () from /usr/lib64/libc.so.6
#6  xxx  in ?? () from /usr/lib64/libc.so.6
#7  xxx in ?? () from /usr/lib64/libc.so.6
#8  xxx in ?? () from /usr/lib64/libc.so.6
#9  xxx in free () from /usr/lib64/libc.so.6
#10 xxx in ?? () from /home/xxx/run/master_0611/cann-9.1.0/lib64/libascend_trace.so
#11 xxx in ?? () from /home/xxx/run/master_0611/cann-9.1.0/lib64/libascend_trace.so
#12 xxx  in ?? () from /home/xxx/run/master_0611/cann-9.1.0/lib64/libascend_trace.so
#13 xxx in ?? () from /lib/ld-linux-aarch64.so.1
#14 xxx in ?? () from /lib/ld-linux-aarch64.so.1
#15 xxx  in ?? () from /usr/lib64/libc.so.6
#16 xxx in exit () from /usr/lib64/libc.so.6
#17 xxx in ?? () from /usr/lib64/libc.so.6
#18 xxx in __libc_start_main () from /usr/lib64/libc.so.6
#19 xxx in _start ()


### Before submitting...

- [x] Ensure you searched for relevant issues and read the [documentation]

## 评论 (5)

### github-actions[bot] · 2026-06-12

Thanks for opening this issue, @CherryHuhu!

| Field | Value |
|-------|-------|
| **Issue** | #2440 |
| **GitHub user ID** | `43200950` |
| **Reporter** | @CherryHuhu |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.

### ykwd · 2026-06-15

@JieTang66  Could you kindly take a look when you have time? Thanks

### VNightMare · 2026-06-16

Thank you for reporting this issue, we need more details to trace it. Would you please provide:
1. Hixl or CANN version.
2. Mooncake version or commit SHA.
3. Detailed core dump and Mooncake logs.
> Notes: I previously encountered a similar problem , but I'm not sure if it's the same one. In my case, I solved it by changing the memory allocator to jemalloc, maybe you can have a try.


### github-actions[bot] · 2026-09-15

This issue has had no activity for 90 days and will be closed in 7 days if there is no further activity. Please comment or react if it should stay open.

### github-actions[bot] · 2026-09-23

Closing due to 3 months of inactivity. If this is still relevant, please comment and we can reopen.
