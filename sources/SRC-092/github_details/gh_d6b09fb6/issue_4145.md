# [Issue #4145] Nightly build/test failure - 2026-09-15

source: https://github.com/kvcache-ai/Mooncake/issues/4145
state: open | updated: 2026-09-16T02:06:57Z
labels: nightly-failure

## 正文

## Nightly Failure Report

**Run**: https://github.com/kvcache-ai/Mooncake/actions/runs/34867094698
**Branch**: refs/heads/main
**Timestamp**: 2026-09-15T17:19:20.246Z

Please investigate the failed jobs in the workflow run linked above.

## 评论 (1)

### he-yufeng · 2026-09-16

Root-caused the Go store part of this nightly in #4150. It is three independent breakages stacked in one job, and the visible link error is only the first:

1. The OSS adapter (#3714) signs requests with OpenSSL HMAC, so `libmooncake_store.a` now references `EVP_sha256` and the Go link needs `-lcrypto` (static archives carry no transitive deps). This is the failure the run shows.
2. With crypto linked, `master_service.cpp` pulls `LocalSsdManager` from `local_ssd/libmooncake_local_ssd.a`, which the link line never named.
3. With both linked, the test binary runs but the client cannot publish `rpc_meta`: it PUTs to `http://127.0.0.1:8080/metadata` and gets connection refused. The 09-04 green run only worked because a shared `nightly_test_cluster` master with `enable_http_metadata_server=1` from an earlier step was still serving 8080 when the Go step ran; in this job that master is gone (09-15 logs show no http-enabled master at all), while `integration_test.go` documents `mooncake_master --enable_http_metadata_server=true` as the run requirement.

#4150 fixes all three (CMake-cache-gated `-lcrypto`, group-internal `local_ssd` link when the archive exists, and the script's own master serving http metadata), verified red/green in the dev container: unpatched reproduces the exact link error, patched runs the suite green (`ok ... go/tests 13.395s`).

The other two failures in that run are already covered elsewhere: `ShmTransportTest.RelocateCopySurvivesConcurrentCap` was the scheduling race fixed by #4121 (merged after that run, and the failing `while` shape matches `'\0' vs 0x5a` exactly), and `MasterServiceSSDSnapshotTest.EvictObject` is the 4s-margin flake tracked in #4136 (it flaked twice more on unrelated branches the same day).

