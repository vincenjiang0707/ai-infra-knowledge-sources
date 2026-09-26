# [Issue #4202] Nightly build/test failure - 2026-09-17

source: https://github.com/kvcache-ai/Mooncake/issues/4202
state: open | updated: 2026-09-18T00:37:56Z
labels: nightly-failure

## 正文

## Nightly Failure Report

**Run**: https://github.com/kvcache-ai/Mooncake/actions/runs/35120471779
**Branch**: refs/heads/main
**Timestamp**: 2026-09-17T16:18:47.701Z

Please investigate the failed jobs in the workflow run linked above.

## 评论 (1)

### he-yufeng · 2026-09-18

Root cause from the run logs, and it is already fixed on main.

Both failing lanes (`nightly-test` job 104876827469, `nightly-coverage` job 104876759343) die at the same step, and it is not a test: the C++ suite is 202/202 green, then `run_store_go_integration.sh` fails linking the Go test binary:

```
/usr/bin/ld: build/mooncake-store/src/libmooncake_store.a(oss_adapter.cpp.o): undefined reference to symbol 'EVP_sha256@@OPENSSL_3.0.0'
/lib/x86_64-linux-gnu/libcrypto.so.3: error adding symbols: DSO missing from command line
```

The OSS adapter was enabled at CMake time (`-- Alibaba Cloud OSS adapter: Enabled` in the same log), so `oss_adapter.cpp.o` lands in the static `libmooncake_store.a`, and its OpenSSL HMAC calls need `-lcrypto` on the Go link line. The link line in the log does not have it.

The run built `ffe0135`, which predates `c57745c3` (#4150, "[CI] Make the Go store integration link self-contained again", merged 09-17): that change makes the Go link append `-lcrypto` exactly when `MOONCAKE_OSS_ADAPTER_ENABLED:INTERNAL=TRUE` is in the build's CMakeCache, which is the case here. `git show ffe0135:scripts/ci/run_store_go_integration.sh | grep -c lcrypto` is 0.

So this specific failure should be gone in the next nightly on any sha containing `c57745c3`. Suggest leaving this open until one nightly on main runs green past the Go integration step, then closing.

