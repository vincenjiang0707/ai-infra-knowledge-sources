# [Issue #2324] [Issue]: Memory leak risk of function allocateSpilled

source: https://github.com/NVIDIA/nccl/issues/2324
state: open | updated: 2026-08-09T23:42:42Z
labels: 

## 正文

### How is this issue impacting you?

Lower performance than expected

### Share Your Debug Logs

In function allocateSpilled, if the following code does not hit `goto unhunked`:

```c++
size_t nextSize = (top ? top->size : 0) + (64 << 10);
    constexpr size_t maxAlign = 64;
    if (nextSize < sizeof(struct Hunk) + maxAlign + size) {
      uintptr_t uproxy = (me->topFrame.bumper + alignof(Unhunk) - 1) & -uintptr_t(alignof(Unhunk));
      if (uproxy + sizeof(struct Unhunk) <= me->topFrame.end) goto unhunked;
    }
```

then a new Hunk will be allocated:

```c++
    // At this point we must need another hunk, either to fit the object
    // itself or its Unhunk proxy.
    mallocSize = nextSize;
    INFO_LOC(NCCL_ALLOC_HOST, "memory stack hunk malloc(%llu)", (unsigned long long)mallocSize);
    struct Hunk* top1 = (struct Hunk*)malloc(mallocSize);
    ...
```

The above logic miss a special case, for example:

<img width="3475" height="1469" alt="Image" src="https://github.com/user-attachments/assets/5823cc70-8476-4653-b943-96517dd543d4" />

This caused the 128KB Hunk to be broken out of the Hunk list, leading to a memory leak.

### Steps to Reproduce the Issue

_No response_

### NCCL Version

2.30.7

### Your platform details

_No response_

### Error Message & Behavior

Memory leak(Hunk list is broken).

## 评论 (2)

### lennyJL · 2026-08-06

This issue is based on static code review. Since I am less familiar with the codebase than the maintainers, if the maintainers believe that this edge case has zero probability of occurring in real-world usage, please feel free to close this issue and the corresponding PR.

### xiaofanl-nvidia · 2026-08-09

++ @bhramesh-nvidia to help take a look and bring in the PR if this is a good fix. 
