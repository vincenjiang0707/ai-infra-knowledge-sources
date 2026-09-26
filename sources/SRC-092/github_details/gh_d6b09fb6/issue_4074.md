# [Issue #4074] [Bug]: NoF e2e script aborts from a source build (libasio.so not found)

source: https://github.com/kvcache-ai/Mooncake/issues/4074
state: closed | updated: 2026-09-13T06:41:31Z
labels: 

## 正文

## Summary

`mooncake-store/tests/e2e/run_nof_heartbeat_tcp_e2e.sh` cannot be run against a source build. It aborts before any test logic executes:

```
$ BUILD_DIR=$PWD/build bash mooncake-store/tests/e2e/run_nof_heartbeat_tcp_e2e.sh
rc=1

$ cat /tmp/mooncake_nof_heartbeat_e2e/register.log
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: libasio.so: cannot open shared object file: No such file or directory
```

## Root cause

The `store` pybind module built under `build/mooncake-integration` links `libasio.so`, which the build places in `build/mooncake-common`:

```
$ readelf -d build/mooncake-integration/store.cpython-310-x86_64-linux-gnu.so | grep -E "RUNPATH|NEEDED.*asio"
 0x0000000000000001 (NEEDED)             Shared library: [libasio.so]
 0x000000000000001d (RUNPATH)            Library runpath: [$ORIGIN]
```

`$ORIGIN` is `build/mooncake-integration`, so the library resolves only in the installed layout, where both files end up in the same directory. The script exports `PYTHONPATH="$BUILD_DIR/mooncake-integration"` but nothing for the dynamic loader, and `set -euo pipefail` turns the failed import into an immediate exit — the register step, the client and the fault injection are never reached.

## Verification

With the build-tree directory on the loader path the script runs to completion and passes its assertions:

```
$ LD_LIBRARY_PATH=$PWD/build/mooncake-common CLIENT_GLOBAL_SEGMENT_SIZE=0 \
  CLIENT_MEMORY_REPLICA_NUM=0 BUILD_DIR=$PWD/build \
  bash mooncake-store/tests/e2e/run_nof_heartbeat_tcp_e2e.sh; echo rc=$?

=== verdict ===
post_fault_successes=2
post_fault_failures=35
post_unmount_successes=0
post_unmount_failures=5
pre_fault_put_ok=4
pre_fault_get_ok=4
rc=0
```

The master log confirms the control path is exercised:

```
master_service.cpp:1030]  NoF segment mount: action=mount_segment, segment_name=traddr:127.0.0.1 trsvcid:4420 subnqn:nqn.2016-06.io.spdk:cnode1 trtype:TCP adrfam:IPv4 ns:1
master_service.cpp:12465] action=unmount_nof_segment_by_heartbeat, last_error_reason=open_fail
```

## Notes

Two unrelated behaviours surfaced while testing this, not addressed here:

- NoF-only mode needs `CLIENT_MEMORY_REPLICA_NUM=0` in addition to `CLIENT_GLOBAL_SEGMENT_SIZE=0`. With only the latter the client still requests one memory replica, each `PutStart` becomes a partial allocation (`allocated_memory_replicas=0`) and `PutEnd` fails with `no_primary_write_in_progress`, so no I/O ever succeeds.
- The default memory + NoF invocation currently fails its post-unmount assertion (`post_unmount_successes = 0`), which may be an expectation drift in the script since it is not wired into CI.

## Proposed fix

Export `$BUILD_DIR/mooncake-common` on `LD_LIBRARY_PATH` in the script, or give the build tree a `$ORIGIN/../mooncake-common` RUNPATH for the pybind module.


## 评论 (1)

### github-actions[bot] · 2026-09-13

Thanks for opening this issue, @Ziy1-Tan!

| Field | Value |
|-------|-------|
| **Issue** | #4074 |
| **GitHub user ID** | `49604965` |
| **Reporter** | @Ziy1-Tan |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.
