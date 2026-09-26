# [Issue #4239] [RFC]: Reclaimed-Payload Exposure (RPE): measuring the gap between TTL-lease protection and in-flight transfers in Mooncake Store

source: https://github.com/kvcache-ai/Mooncake/issues/4239
state: closed | updated: 2026-09-23T03:24:10Z
labels: RFC

## 正文

### Changes proposed

[0001-Store-Bugfix-add-missing-lease-expiry-check-to-BatchGet.patch](https://github.com/user-attachments/files/32430216/0001-Store-Bugfix-add-missing-lease-expiry-check-to-BatchGet.patch)
[issue_rpe_rfc.md](https://github.com/user-attachments/files/32430218/issue_rpe_rfc.md)
[PR_body_batchget_lease.md](https://github.com/user-attachments/files/32430217/PR_body_batchget_lease.md)


### Before submitting a new issue...

- [x] Make sure you already searched for relevant issues and read the [documentation](https://kvcache-ai.github.io/Mooncake/)

## 评论 (4)

### github-actions[bot] · 2026-09-20

Thanks for opening this issue, @binxuwang2002-lang!

| Field | Value |
|-------|-------|
| **Issue** | #4239 |
| **GitHub user ID** | `232507676` |
| **Reporter** | @binxuwang2002-lang |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.

### binxuwang2002-lang · 2026-09-20

Mooncake version: commit f20b7061097e4e2fda825f4106f215c71f13274a (main, 2026-07-17)

Environment> - OS: Ubuntu 24.04.3 LTS (WSL2, kernel 6.6.87.2), gcc 13.3.0

No GPU, no RDMA NIC; protocol=tcp, metadata P2PHANDSHAKE
Topology: 1 mooncake_master + 2 client processes on one host
Steps to reproduce:

Start mooncake_master --default_kv_lease_ttl=500 (small TTL for a fast repro).
Put two objects (replica_num=1). 3.Query` each key (grants a fresh lease), then sleep past the TTL.
Call BatchGet(keys, query_results, slices, /*prefer_same_node=*/true).
Expected: every entry fails with LEASE_EXPI — the same as Client::Get and the general Client::BatchGet, which discard the data when the lease expires before the transfer completes (lease_expired_before_data_transfer_completed).

Actual: all entries return success with the data, because Client::BatchGetWhenPreferSameNode never performs the lease-expiry check. The bytes handed back may come from a slot already reclaimed by BatchEvict and rewritten by another object.

A regression test (BatchGetPreferSameNodeLeaseExpired) that fails on the unpatched code and passes with a minimal fix mirroring the sibling paths is ready — happy to open a PR.

### ykwd · 2026-09-23

Thanks for catching this issue and for the detailed report. We appreciate it and will get it fixed.

### Aionw · 2026-09-23

This was fixed in https://github.com/kvcache-ai/Mooncake/pull/3996
