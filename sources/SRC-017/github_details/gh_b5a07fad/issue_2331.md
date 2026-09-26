# [Issue #2331] [Issue]: Symmetric VA exhaustion in `symMemoryObtain` when registering multiple windows on the same memory allocation.

source: https://github.com/NVIDIA/nccl/issues/2331
state: closed | updated: 2026-09-14T04:50:30Z
labels: 

## 正文

### How is this issue impacting you?

Application crash

### Share Your Debug Logs

_No response_

### Steps to Reproduce the Issue

_No response_

### NCCL Version

2.30.7-1

### Your platform details

_No response_

### Error Message & Behavior

**Problem:**
Calling `ncclCommWindowRegister` multiple times on the same underlying memory allocation (`memAddr`, `size`, `winFlags`) causes `symMemoryObtain()` in `src/dev_runtime.cc` to treat each call as a brand-new allocation:

- It repeatedly allocates chunks from `devr->bigSpace` via `ncclSpaceAlloc()`.
- Once `devr->bigSpace` is full, `ncclSpaceAlloc()` fails.
- Subsequent registrations fail with `ncclSystemError` / `ncclUnhandledCudaError`.
- struct `ncclDevrMemory` lacks reference counting, preventing deduplication and safe sharing.

**Error message:**
```
Allocation failed. No suitable space found to accommodate size=0x2171600000 within limit=0x2d00000000
```
```
[0] nccl/src/allocator.cc:229 (ncclSpaceAlloc) NCCL WARN Allocation failed. No suitable space found to accommodate size=0x2171600000 within limit=0x2d00000000
[0] NCCL INFO nccl/src/dev_runtime.cc:602 (symMemoryObtain) -> 3
[0] NCCL INFO nccl/src/dev_runtime.cc:901 (ncclDevrWindowRegisterInGroup) -> 3
[0] NCCL INFO nccl/src/group.cc:265 (ncclCommGroupRegisterSymmetric) -> 3
[0] NCCL INFO nccl/src/group.cc:79 (ncclAsyncJobMain) -> 3 [Async thread]
[0] NCCL INFO nccl/src/group.cc:654 (groupLaunch) -> 3
[0] NCCL INFO nccl/src/group.cc:866 (ncclGroupEndInternal) -> 3
[0] NCCL INFO nccl/src/dev_runtime.cc:1370 (ncclCommWindowRegister) -> 3
```

   
**Proposed Fix:**
In `symMemoryObtain()`, check `devr->memHead` for an existing matching `ncclDevrMemory` entry. If found:

- Increment `refCount`.
- Release redundant `memHandles` via `cuMemRelease()`.
- Participate in `bootstrapAllGather()` to maintain collective rank synchronization.
- Return the existing memory object early instead of consuming more `devr->bigSpace`.
- In `symMemoryDestroy()`, only free resources when `refCount == 0`.

## 评论 (3)

### xiaofanl-nvidia · 2026-08-09

++ @bhramesh-nvidia @KaimingOuyang please take a look at this. If this is reasonable, please file an internal bug to track. 

### bhramesh-nvidia · 2026-08-19

@thearusable Thanks for reporting this. This should be fixed in in the dev branch (https://github.com/NVIDIA/nccl/commit/8b6b8b6dbd441a1021158d88af2a3f35eac2d4cb). The code needed additional handling to ensure correctness, but it should fix whatever is reported here.

### xiaofanl-nvidia · 2026-09-14

Closing this issue since it should have been fixed. Please let us know if this is still a problem by opening a new issue. Thanks! 
