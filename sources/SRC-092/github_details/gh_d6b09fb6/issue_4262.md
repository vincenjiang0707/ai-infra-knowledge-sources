# [Issue #4262] [Store] BatchReplicaClear RPC drops the caller's tenant and silently no-ops for other tenants

source: https://github.com/kvcache-ai/Mooncake/issues/4262
state: closed | updated: 2026-09-23T03:32:35Z
labels: 

## 正文

With multi-tenancy enabled, `BatchReplicaClear` can only ever clear default-tenant objects: the RPC never carries the caller's tenant, and the server-side fallback hardcodes `"default"`.

Call chain:

- `Client::BatchReplicaClear` has no tenant parameter, and the `MasterClient` RPC sends `(object_keys, client_id, segment_name)` only.
- `WrappedMasterService::BatchReplicaClear` forwards to the 3-arg `MasterService::BatchReplicaClear`, which delegates with a literal `"default"`.
- The 4-arg tenant-aware overload exists on `MasterService` but is not reachable over RPC.

A tenant-a client clearing its own replica therefore resolves the object identity under `"default"`, lands in the "not found, skipping" branch, and gets an empty cleared list back with no error. The object stays fully replicated and the caller cannot tell why.

`GetReplicaListByRegex` already sends `tenant_id` over the same RPC layer, so the pattern exists. Could `BatchReplicaClear` take the caller's tenant the same way and forward to the 4-arg overload? Happy to prepare the change with a multi-tenancy regression test.

I hit this while building a cross-tenant test for #3889: the test object had to stay on the default tenant precisely because its memory replica could not be cleared otherwise.


## 评论 (3)

### github-actions[bot] · 2026-09-21

Thanks for opening this issue, @he-yufeng!

| Field | Value |
|-------|-------|
| **Issue** | #4262 |
| **GitHub user ID** | `40085740` |
| **Reporter** | @he-yufeng |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.

### XFDG · 2026-09-22

Hi, I've submitted a fix in https://github.com/kvcache-ai/Mooncake/pull/4278.

### he-yufeng · 2026-09-22

#4278 covers this: it carries the client tenant through the same call chain and resolves it through the existing WithRequestTenant pattern, with a regression test that puts the same key under two tenants, clears one, and proves the other survives. I had the same fix staged locally with a multi-tenancy regression; theirs is complete and idiomatic, so nothing left to do from my side except the review I just left (rolling-upgrade wire-shape note).

