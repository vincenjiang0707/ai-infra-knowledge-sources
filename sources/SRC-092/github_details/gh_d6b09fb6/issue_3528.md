# [Issue #3528] [Bug&RFC] Bucket LOCAL_DISK: clients sharing a `storage_path` collide on bucket ids → L3 cache broken

source: https://github.com/kvcache-ai/Mooncake/issues/3528
state: closed | updated: 2026-09-24T07:36:07Z
labels: bug

## 正文

### Bug Report

**Summary.** When multiple clients share one `storage_path` (e.g. SGLang embeds one Mooncake client per TP rank on the same `ssd_offload_path`), the bucket `LOCAL_DISK` backend has no per-client namespacing and no stable identity. This causes three coupled problems: silent collision, ambiguous recovery ownership, and per-client accounting that can neither be attributed nor survive restart. Existing issues cover pieces; none covers the **"N clients, one `storage_path`"** case.

**Environment.** Mooncake bucket `LOCAL_DISK` backend (`main`). Occurs whenever multiple clients share one `storage_path` — e.g. SGLang embeds one Mooncake client per TP rank on the same `ssd_offload_path` (sgl-project/sglang#31926).

**Three coupled problems** (`mooncake-store/src/storage_backend.cpp` unless noted):
1. **Silent collision.** `BucketIdGenerator` seeds `(time_gen() << 12) | 0` (whole-second) then only `fetch_add`s; filename `<storage_path>/<bucket_id>.bucket` has no client tag; opened `O_CREAT|O_TRUNC`, no `O_EXCL`. Same-second construction → identical ids → silent overwrite. The backend struct holds only `storage_path_` — no `client_id`/pid to disambiguate.
2. **Ambiguous recovery.** `Init()` scans the whole dir and adopts every `.meta`, keyed by numeric `bucket_id`; `MasterService::AddReplica` (`master_service.cpp`) keeps one LOCAL_DISK replica per key with no `client_id` check (see #3052). Shared dir → every client claims every file → arbitrary first-claim → dangling refs when the "owner" evicts.
3. **No stable, attributable identity.** `client_id` is a random UUID minted per `Client` ctor (`client_service.cpp`, boost random), not stable across restart, and never assigned by the master. So a client cannot be recognized as the same logical owner after a restart, and its on-disk data cannot be attributed to it — which is what makes per-client, layout-independent accounting impossible today.

**Related.** #3052 (client-restart / `client_id` validation), #2306 + #2777 (marker re-adoption — marker is per-directory), #3030 (replica-id validation), #3220 + #3221 (per-object delete + GC), #2721 (SSD-capacity report), SGLang sgl-project/sglang#31926.

**The gap.** All of the above assume **one client per `storage_path`**. "N clients, one directory" is unsupported, and even the identity primitives that exist (RFC #2306's marker) are per-directory.

**Proposal** (we prefer B; A is a stopgap):
- **(A) Stopgap** — enforce one-dir-per-client (via SGLang #31926), document the contract, and fail fast on a shared directory. Leaves accounting bound to the directory layout.
- **(B) Preferred — directory-independent, Mooncake-side.** Embed a durable `owner_id` in each bucket's `.meta` (not the filename or directory). Per-client accounting and `Init()` recovery then filter by `owner_id`, so both work for **any** layout — shared dir, per-client dirs, or multiple disks. Master re-adopts by matching the in-metadata `owner_id` (not #2306's per-directory marker). Per-client bytes are reported to the master (cf. #2721); a node/disk cap is enforced by master-side aggregation, not a shared-dir scan.
  - Open design point: the durable anchor by which a restarted process recovers its own `owner_id` — a master-side registry keyed by a stable client handle, or a minimal persisted id decoupled from the offload directory.

**Ask.** Decide the ownership model for a shared `storage_path`. We advocate (B) so per-client identity and accounting become layout-independent; (A)/#31926 is a stopgap. This should be coordinated with the warm re-adoption work (#2306). Willing to contribute the PR once the direction is agreed.

### Before submitting...

- [x] Ensure you searched for relevant issues and read the [documentation]

## 评论 (5)

### Morpheus799 · 2026-08-19

Independent reproduction. We reproduced this on DeepSeek-V4-Flash (MLA), TP8, 8 ranks per pod sharing one ssd_offload_path, on the current bucket backend. The collision precondition is deterministic: all 8 ranks in a pod seed their BucketIdGenerator to the identical value (observed 7320020267008 ×8; a separate earlier run showed 7319298519040 ×8) — time_gen() is whole-second, the TP ranks initialize within the same second, and NextId() never re-reads time, so the sequences stay identical for the whole run. Under load this surfaces as read failures carrying the truncation fingerprint storage_backend.cpp: Read size mismatch for key ..., expected: N, got: 0 (a bucket that existed and was O_TRUNC-overwritten by a colliding rank), and these appear before any eviction runs — so they are the collision itself, not an eviction/read race. Requests still succeed because HiCache treats the failed read as a miss and recomputes; the corruption is therefore silent at the API level, but the L3 cache is effectively unusable under this configuration.

### github-actions[bot] · 2026-08-19

Thanks for opening this issue, @Morpheus799!

| Field | Value |
|-------|-------|
| **Issue** | #3528 |
| **GitHub user ID** | `92247184` |
| **Reporter** | @Morpheus799 |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.

### LujhCoconut · 2026-08-21

Thanks for the thorough report. I checked the code paths on `main` and agree the problem is real: the `(time_gen() << 12)` seed carries no client tag, bucket files open with `O_CREAT|O_TRUNC` (no `O_EXCL`), and `Init()` adopts every `.meta` in the directory.

From my understanding, the recommended way to run SSD offload today is **standalone mode**: start a dedicated store service to own the KV-cache pool (and the SSD tier), with the inference ranks as pure requesters. That keeps one client per `storage_path`, so this class of collision doesn't arise.

I'm not familiar with SGLang's code, but on the vLLM side there's an extra reason this fits naturally. vLLM dedups TP-rank keys *before* they reach the store: each cache group's key namespace is `tp_rank // tp_replication_factor` (`_spec_tp_replication_factor` in `worker.py` — `tp_size` for pure MLA, `max(1, tp_size // num_kv_head)` for GQA), so all TP ranks holding identical KV collapse into the same key namespace, `put_step` (the same factor) stripes their PUTs across that one shared key space, and a `batch_is_exist` check dedups before every put. In other words, the logical cache is already "one shared pool" — standalone mode just gives that shared pool a single concrete owner, which is exactly the shape the dedup assumes. Running N embedded clients against one shared offload dir works against that shape.

Happy to help push the fix (fail-fast / owner enforcement) along.

### rishabhsinha17 · 2026-08-25

+1 on (B), with a concrete shape for the open design point (the durable anchor), from the SGLang embedded-client side.

Standalone mode avoids the collision, but the embedded shape is real and staying: SGLang embeds one client per scheduler rank, and per sgl-project/sglang#31926 dp-attention reports the attention-group-local tp_rank (0 on every DP rank when attn_tp_size == 1), so "one client per `storage_path`" cannot be assumed by construction. The per-rank subdir there is the right stopgap, but it keeps identity bound to directory layout, which is exactly what (B) removes.

Anchor proposal: let the client pass an optional stable logical handle at construction (SGLang would pass `engine_id:dp:tp:pp`; no handle keeps today's random UUID and behavior). The master persists a handle -> owner_id mapping and returns the owner_id at registration; the backend stamps it into every `.meta`. `Init()` adoption and byte accounting then filter by owner_id, layout-independent, and #3052 gets a stable identity to validate restarts against.

Migration: version the `.meta`. Legacy metas (no owner_id) are adopted only when the directory is detected single-owner; in a shared dir they are quarantined for GC instead of first-claim adopted. Independent hardening worth landing under either option: salt the `BucketIdGenerator` seed with the client id, and open bucket files with `O_EXCL` plus retry-on-collision; today the seed is whole-second (`storage_backend.cpp:1689`), `NextId()` never re-reads time, and the data file opens `O_CREAT|O_TRUNC` (line 3912), so same-second clients collide for the entire run and the loser is silently truncated.

Guard for existing deployments: on `Init()`, take a lock/marker in `storage_path` and fail fast if another live client owns it, so today's shared-dir setups fail loudly at startup instead of corrupting L3.

Happy to implement once the direction is agreed: the owner_id path including the guard, or the guard plus id hardening alone as a first PR.


### quantz8a · 2026-09-24

Fixed by #4172 (merged `c30f983`). LOCAL_DISK now fail-fasts when a second live client shares `storage_path` (`.mooncake_local_disk.lock` + docs for per-rank dirs).

Closing as completed.
