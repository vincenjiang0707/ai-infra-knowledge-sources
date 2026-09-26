# [Issue #1696] POSIX backend (libaio & io_uring): ENOSPC short writes silently reported as DONE (data loss)

source: https://github.com/ai-dynamo/nixl/issues/1696
state: closed | updated: 2026-09-02T10:27:56Z
labels: 

## 正文

## Summary

The POSIX backend's libaio (`AIO`, the Linux default) and io_uring (`URING`) I/O queues treat any **non-negative** AIO completion result as a fully successful transfer. When a write runs out of space, the kernel commonly returns a **short write** -- a positive byte count smaller than the requested length -- rather than a negative errno. That short count slips past the error check, so NIXL reports the transfer as `DONE` even though only part of the buffer reached disk. The caller never learns ENOSPC occurred, and data is silently lost.

`POSIXAIO` (`posix_aio_io_queue.cpp`) does **not** have this bug -- it compares the completed byte count against the requested length -- so it can serve as the reference for a fix.

## Affected code

`src/plugins/posix/linux_aio_io_queue.cpp`, `doCheckCompleted()`:

```cpp
for (int i = 0; i < rc; i++) {
    struct iocb *iocb = events[i].obj;
    nixlPosixLinuxAioIO *io = (nixlPosixLinuxAioIO *)iocb->data;

    if (events[i].res < 0) {                 // only catches whole-op failure (e.g. res == -ENOSPC)
        NIXL_ERROR << "AIO operation failed: " << events[i].res;
        return NIXL_ERR_BACKEND;
    }
    if (io->clb_) io->clb_(io->ctx_, events[i].res, 0);   // short write (0 <= res < len) => "success"
    completed_ios.push_back(io);
}
```

The completion callback in `src/plugins/posix/posix_backend.cpp` then discards the byte count and error entirely:

```cpp
void nixlPosixBackendReqH::ioDone(uint32_t data_size, int error) {
    num_confirmed_ios_++;     // data_size and error are ignored
    logOnPercentStep(num_confirmed_ios_, queue_depth_);
}
```

Once `num_confirmed_ios_ == queue_depth_`, `checkXfer()` returns `NIXL_SUCCESS` and the caller sees `DONE`.

`src/plugins/posix/io_uring_io_queue.cpp` has the same pattern (only `res < 0` is checked). For contrast, `src/plugins/posix/posix_aio_io_queue.cpp` does it correctly:

```cpp
ssize_t ret = aio_return(&io->aio_);
if (ret < 0 || ret != static_cast<ssize_t>(io->aio_.aio_nbytes)) {   // short write IS flagged
    NIXL_ERROR << "aio_return failed: " << nixl_strerror(-ret);
    ...
    return NIXL_ERR_BACKEND;
}
```

| Queue | Completion check | Short write |
|-------|------------------|-------------|
| libaio (`AIO`, Linux default) | `events[i].res < 0` only | silently lost |
| io_uring (`URING`) | `res < 0` only | silently lost |
| posix aio (`POSIXAIO`) | `ret < 0 \|\| ret != aio_nbytes` | correctly flagged |

Note the fully-failed case (`res == -ENOSPC`, 0 bytes written) *is* caught by the `res < 0` check. But on a filesystem with a little free space remaining, ENOSPC manifests as a short write, not a negative result -- so the common real-world case is the silent one.

## Reproduction

A single NIXL `WRITE` of a 1 MiB DRAM buffer into a `FILE_SEG` target, forcing the libaio queue (`use_aio=true`), against a nearly-full filesystem.

Filling a tmpfs (`/dev/shm`) to leave ~32 KiB free, then writing 1 MiB:

```
[xfer] check_xfer_state final state = DONE
[result] requested write = 1048576 bytes
[result] bytes on disk   = 32768
```

NIXL reports `DONE`; only 32768 of 1048576 bytes were written. The same result is obtained by capping `RLIMIT_FSIZE` (e.g. to 64 KiB) before the transfer, which forces the kernel to short-complete the write.

Minimal reproducer:

```python
import os, resource
import nixl._utils as nixl_utils
from nixl._api import nixl_agent, nixl_agent_config

resource.setrlimit(resource.RLIMIT_FSIZE, (65536, 65536))  # cap file size -> short write
agent = nixl_agent("enospc", nixl_agent_config(backends=[]))
agent.create_backend("POSIX", {"use_aio": "true"})

size = 1 << 20
src = nixl_utils.malloc_passthru(size)
nixl_utils.ba_buf(src, size)
agent.register_memory(agent.get_reg_descs([(src, size, 0, "src")], "DRAM"))
xfer_src = agent.get_xfer_descs([(src, size, 0)], "DRAM")

fd = os.open("/tmp/out.bin", os.O_WRONLY | os.O_CREAT, 0o644)
file_descs = agent.register_memory([(0, size, fd, "dst")], "FILE")
h = agent.initialize_xfer("WRITE", xfer_src, file_descs.trim(), "enospc")
agent.transfer(h)
while agent.check_xfer_state(h) not in ("DONE", "ERR"):
    pass
print("state:", agent.check_xfer_state(h), "on disk:", os.fstat(fd).st_size, "requested:", size)
# -> state: DONE  on disk: 65536  requested: 1048576
```

## Environment

- NIXL commit `4916701629f39f0469a4c1071bf2dbc3052212e6`
- Python wheel `nixl_cu13` 1.1.0, POSIX plugin, Linux x86_64
- IO queue type `AIO` (libaio), which is the default on Linux

## Suggested fix

In `linux_aio_io_queue.cpp` and `io_uring_io_queue.cpp`, track the requested length per IO and treat `res != len` (for a non-negative `res`) as a failure, mirroring `posix_aio_io_queue.cpp`. Additionally, `nixlPosixBackendReqH::ioDone` should propagate the byte count / error rather than discarding them, so a short write can be surfaced as `NIXL_ERR_BACKEND` (or a dedicated partial-write status) from `checkXfer()`.


## 评论 (1)

### lluki · 2026-08-26

uring fix was merged #1942, AIO fix still pending #2085
