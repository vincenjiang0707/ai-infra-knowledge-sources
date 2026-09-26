# [Issue #3611] [Bug]: Store's OffsetAllocatorStorageBackend: use_direct_io=true is misleading dead code

source: https://github.com/kvcache-ai/Mooncake/issues/3611
state: closed | updated: 2026-09-15T06:52:04Z
labels: bug

## 正文

## Description

`OffsetAllocatorStorageBackend` constructs its `UringFile` with `use_direct_io = true`, and the log line `[UringFile] O_DIRECT mode enabled for <file>` is printed. However, **O_DIRECT is never actually enabled on the file descriptor**, and the I/O hot path (`vector_read`/`vector_write`) contains **no alignment handling whatsoever**. This makes `use_direct_io=true` deceptive dead code in this backend.

There are two distinct problems:

### Problem 1: `open()` does not set `O_DIRECT`

In `mooncake-store/src/storage_backend.cpp`, `OffsetAllocatorStorageBackend::Init()` opens the data file with:

```cpp
// storage_backend.cpp:3912-3913
int flags = O_CLOEXEC | O_RDWR | O_CREAT | O_TRUNC;   // no O_DIRECT
int raw_fd = open(data_file_path_.c_str(), flags, 0644);
```

then passes `use_direct_io = true` to `UringFile`:

```cpp
// storage_backend.cpp:3934-3935
data_file_ = std::make_shared<UringFile>(
    data_file_path_, fd_guard.release(), 32, true);
```

But the `UringFile` constructor (`mooncake-store/src/uring_file.cpp:414-428`) **only stores the flag and prints the log** — it does not call `fcntl(fd, F_SETFL, flags | O_DIRECT)`:

```cpp
// uring_file.cpp:578-590
UringFile::UringFile(const std::string& filename, int fd,
                     unsigned /*queue_depth*/, bool use_direct_io)
    : StorageFile(filename, fd), use_direct_io_(use_direct_io) {
    ...
    if (use_direct_io_) {
        LOG(INFO) << "[UringFile] O_DIRECT mode enabled for " << filename;  // misleading!
    }
}
```

As a result, all I/O on this fd goes through the **page cache (buffered I/O)**, not direct I/O. The log message is misleading — it suggests O_DIRECT is active when it is not.

For comparison, `BucketStorageBackend::OpenFile` (`storage_backend.cpp:2604-2617`) does this correctly by **both** adding `O_DIRECT` to the `open()` flags **and** passing `use_direct_io = true`:

```cpp
// storage_backend.cpp:3570-3590 & 932-963  (BucketStorageBackend — correct)
if (file_storage_config_.use_uring && mode == FileMode::Read) {
    flags |= O_DIRECT;                    // <-- fd gets O_DIRECT
}
int fd = open(path.c_str(), flags | access_mode, 0644);
...
if (file_storage_config_.use_uring && mode == FileMode::Read) {
    return std::make_unique<UringFile>(path, fd, 32, true);
}
```

### Problem 2: `vector_read`/`vector_write` ignore `use_direct_io_` entirely

The `use_direct_io_` flag only affects the scalar methods `read()` / `write()` / `read_aligned()` / `write_aligned()` (which allocate 4096-aligned bounce buffers and validate alignment).

However, `vector_read` and `vector_write` (`uring_file.cpp:623-671`) **do not check `use_direct_io_` at all** — no alignment validation, no bounce buffer:

```cpp
// uring_file.cpp:791-805
tl::expected<size_t, ErrorCode> UringFile::vector_write(const iovec* iov,
                                                        int iovcnt,
                                                        off_t offset) {
    if (fd_ < 0) return make_error<size_t>(ErrorCode::FILE_NOT_FOUND);
    // no use_direct_io_ check, no alignment handling
    auto res = SharedUringRing::instance().vector_write(fd_, iov, iovcnt, offset);
    ...
}

// uring_file.cpp:807-839  (same pattern for vector_read)
```

Critically, **`OffsetAllocatorStorageBackend` exclusively uses the vector I/O path**:

- `BatchOffload` calls `data_file->vector_write(iovs.data(), iovs.size(), offset)` (`storage_backend.cpp:5178`)
- `BatchLoad` calls `plan.data_file->vector_read(...)` **three times per key** (`storage_backend.cpp:5418`, `5442`, `5463`)

The scalar methods that *would* respect `use_direct_io_` are never called by this backend.

Furthermore, the `iovec`s constructed in `BatchOffload` (`storage_backend.cpp:~5150-5175`) are **completely unaligned**:

- `&header.key_len` / `&header.value_len` — 4-byte stack variables, not 4096-aligned
- `key.data()` — `std::string` internal buffer, not guaranteed aligned
- `slice.ptr` — caller-provided, not guaranteed aligned
- `offset` — from `OffsetAllocator::allocate()`, arbitrary offset, not 4096-aligned
- `iov_len` values — 4, key length, value length, etc., not 4096-aligned

## Expected behavior

Either:
- O_DIRECT should be genuinely enabled (via `open()` flags or `fcntl(F_SETFL)`) **and** the vector I/O path should enforce 4096 alignment on buffers, lengths, and offsets; **or**
- the `use_direct_io = true` argument and the misleading "O_DIRECT mode enabled" log should be removed/changed to reflect that this backend uses buffered I/O.

## Actual behavior

- `use_direct_io = true` is passed to `UringFile`, the log prints "O_DIRECT mode enabled", but the fd is opened without `O_DIRECT` — all I/O is buffered (page cache).
- The vector I/O hot path has no alignment handling, so the `use_direct_io_` flag is completely bypassed.
- If someone were to "fix" Problem 1 by adding `O_DIRECT` to `open()` **without also fixing** Problem 2, `vector_read`/`vector_write` would immediately fail with `EINVAL` due to unaligned buffers/offsets/lengths.

## Environment

- Component: `mooncake-store`
- Relevant files:
  - `mooncake-store/src/storage_backend.cpp` (`OffsetAllocatorStorageBackend::Init`, `BatchOffload`, `BatchLoad`)
  - `mooncake-store/src/uring_file.cpp` (`UringFile` constructor, `vector_read`, `vector_write`)
  - `mooncake-store/include/file_interface.h` (`UringFile` declaration, `use_direct_io` parameter)

## Checklist

- [x] I have reviewed the changed code end-to-end and can defend the change.
- [x] AI assistance disclosure: This issue was drafted with AI assistance; the findings have been verified against the source code.


### Before submitting...

- [x] Ensure you searched for relevant issues and read the [documentation]

## 评论 (2)

### github-actions[bot] · 2026-08-24

Thanks for opening this issue, @mzygQAQ!

| Field | Value |
|-------|-------|
| **Issue** | #3611 |
| **GitHub user ID** | `30590325` |
| **Reporter** | @mzygQAQ |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.

### huangxiaobai-ydmy · 2026-08-24

I'd like to take this. Planning to fix the misleading `use_direct_io`/log path first (not full O_DIRECT). Will open a PR soon.
