# [Issue #4073] [Bug]: -DUSE_NOF=ON fails to link mooncake_master (undefined SpdkWrapper symbols)

source: https://github.com/kvcache-ai/Mooncake/issues/4073
state: closed | updated: 2026-09-13T06:41:21Z
labels: 

## 正文

## Summary

With `-DUSE_NOF=ON`, building the Store master target fails to link:

```
$ make mooncake_master
/usr/bin/ld: libmooncake_store_master.a(master_service.cpp.o): in function `mooncake::MasterService::MasterService(...)::{lambda(...)}':
    undefined reference to `mooncake::SpdkWrapper::GetInstance()'
    undefined reference to `mooncake::SpdkWrapper::ProbeNofSegment(std::string const&, unsigned int, std::string*)'
/usr/bin/ld: libmooncake_store_master.a(spdk_wrapper.cpp.o): undefined reference to `mooncake::SpdkControllerConfig::FromEnvironment()'
collect2: error: ld returned 1 exit status
```

## Root cause

`master_service.cpp` installs the NoF heartbeat probe through `SpdkWrapper`:

```cpp
nof_probe_fn_ = [](const std::string& te_endpoint, uint32_t timeout_ms,
                   std::string* error_reason) {
    return SpdkWrapper::GetInstance().ProbeNofSegment(
        te_endpoint, timeout_ms, error_reason);
};
```

but `mooncake-store/src/CMakeLists.txt` only wires the SPDK bits into the client side:

- `${SPDK_WRAPPER_SOURCES}` is appended to `MOONCAKE_STORE_CLIENT_SOURCES` (inside `if(USE_NOF)`).
- `${SPDK_STATIC_LIBS}` is linked into the full `mooncake_store` target only.
- The reduced `mooncake_store_master` library is built from `mooncake_store_shared_objects` + `mooncake_store_master_objects`, so it has neither.

## Impact

The documented NoF end-to-end test cannot run from a clean tree: `mooncake-store/tests/e2e/run_nof_heartbeat_tcp_e2e.sh` executes

```bash
"$BUILD_DIR/mooncake-store/src/mooncake_master" --rpc_address=... --nof_heartbeat_interval_sec=...
```

so a `USE_NOF` build that cannot produce `mooncake_master` cannot run the NoF e2e at all.

## Verification

Adding the wrapper sources and `${SPDK_STATIC_LIBS}` to the reduced master library makes both targets link on commit `6ae74b3` (Ubuntu 22.04, SPDK v23.01.1):

```
[100%] Built target mooncake_master
[100%] Built target nof_worker_pool_bench
-rwxrwxr-x 6248792 mooncake-store/src/mooncake_master
-rwxrwxr-x 68923912 mooncake-store/benchmarks/nof_worker_pool_bench
```

`config/spdk_controller_config.cpp` is the only config file the master needs; `config/nof_register_config.cpp` is not referenced from the master translation units.


## 评论 (1)

### github-actions[bot] · 2026-09-13

Thanks for opening this issue, @Ziy1-Tan!

| Field | Value |
|-------|-------|
| **Issue** | #4073 |
| **GitHub user ID** | `49604965` |
| **Reporter** | @Ziy1-Tan |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.
