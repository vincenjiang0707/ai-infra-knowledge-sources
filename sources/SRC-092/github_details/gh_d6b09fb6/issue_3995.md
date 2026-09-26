# [Issue #3995] [RFC] Review MC_USE_TENT=1 gaps for classic TE callers

source: https://github.com/kvcache-ai/Mooncake/issues/3995
state: open | updated: 2026-09-22T15:10:19Z
labels: help wanted, Transfer Engine, RFC

## 正文

## How this list was produced

Started as a static pass over:

- the C++ shim (`mooncake-transfer-engine/src/transfer_engine.cpp`, `use_tent_` branches)
- the Python wrapper (`mooncake-integration/transfer_engine/transfer_engine_py.cpp`)
- inference-engine call sites that use `mooncake.engine.TransferEngine`

Local runtime (2026-09-10, installed TENT wheel, 1P1D PD) then confirmed
some items and left others unverified. Status below is as of **2026-09-17**
(`origin/main` `c4d632888b`). Please still reproduce on your tree before
treating a remaining item as confirmed.

## Why the compatibility layer

We are wiring inference engines to TENT's **native** APIs, but that work is
not finished. Until it is, we use the classic TE compatibility layer
(`MC_USE_TENT=1`) to validate TENT **runtime** stability against existing
callers (PD disaggregation and others). This RFC tracks gaps in that layer.
It is not the native-API migration itself.

## Summary

`MC_USE_TENT=1` (and `MC_USE_TEV1=1`) is meant to run existing
`mooncake::TransferEngine` / `mooncake.engine.TransferEngine` code on the TENT
runtime. Register + sync submit/poll are wired up enough for PD KV transfer.

PD happy path **works** under `MC_USE_TENT=1` (local 1P1D Qwen3-4B
`/generate` 200). This RFC is not a claim that PD is broken today.

Most of the original P0/P1/P2 shim holes now have merged PRs. What is still
open is protocol pinning for `efa`/`ascend`, Python sync/poll semantics, and
`installTransport()` returning `nullptr` for classic C/Go/EFA callers.

If you find a **new** compatibility-layer issue, please report it on this
issue. We will add it to the work-item list.

## Non-goals

- Landing inference-engine (or Mooncake Store) native-API migration in this RFC
  (that work is separate and in progress, e.g. #4070).
- Teaching applications to `installTransport` under TENT. Making the shim
  honor the classic `Transport*` contract so existing callers do not treat a
  successful TENT init as failure **is** in scope (`P1-install-transport`).
- Changing TENT runtime scheduling / failover policy.

## Work items

Priority is "if the reading holds, impact is high" — not "already on fire".

| ID | Problem | Difficulty | PR | Status |
|---|---|---|---|---|
| P0-send_probe | Python `send_probe` SIGSEGV (`getMetadata()` is null) | M | #4081, follow-up #4115 | **done** |
| P0-stale-handle | Transfer failure may keep a dead peer's cached handle (`CheckSegmentStatus` was always OK) | M | #4109 | **partial** |
| P0-device-filter | `initialize(device=...)` still opened all HCAs | M | #4028 | **done** |
| P0-force-tcp | `MC_FORCE_TCP=1` / `protocol=tcp` may still select RDMA | M | #4027, follow-up #4113 | **done** |
| P0-efa-ascend | `protocol=efa\|ascend` may no-op or look successful without that transport | H | — | **open** |
| P1-sync-status | Python `transferSync` retry / `CANCELED` handling may not match TENT failover | S–M | — | **open** |
| P1-error-codes | Shim returned TENT `Status::Code` (non-negative); classic callers expect `ERR_*` | M | #4139 | **done** |
| P1-request-options | `priority` / `remote_accessible` were dropped at the shim | M | #4114 | **done** |
| P2-first-buffer | `getFirstBufferAddress` also called `getMetadata()` (same null deref as `send_probe`) | S | #4138 | **done** |
| P1-install-transport | TENT `installTransport()` returns `nullptr`; classic C/Go/EFA callers treat that as install failure | M | — | **open** |

### Residuals on landed items

These do not reopen the row, but they are not "the original hole is gone with no leftover":

- **P0-send_probe.** Python no longer dereferences `getMetadata()`. #4081 closed the segment after probing, which invalidated a handle already stored in Python `handle_map_`; #4115 stopped closing it. C++ `getMetadata()` is still `nullptr` under TENT — any remaining `getMetadata()->sendProbe` caller will still crash.
- **P0-stale-handle.** `CheckSegmentStatus` now probes via `probePeerAliveByID`. Python only calls it when **`submitTransfer` fails**. Peer death that shows up as `getTransferStatus` `FAILED` / `TIMEOUT` still leaves `handle_map_` intact. That leftover belongs with **P1-sync-status**. The unit test covers an never-opened handle, not a still-mapped handle whose RPC probe fails.
- **P0-force-tcp.** #4113 makes `forceTcp()` disable HP TCP so a config with both enabled does not fail init.
- **P1-error-codes.** Integer-returning APIs go through `tentToClassicError()`. `submitTransfer` still wraps TENT failures as `Status::Context(...)`. No in-tree test that failed on main and passed after (#4139 checklist).
- **P1-request-options.** Shim forwards `remote_accessible` → TENT perms and `TransferRequest::priority` on submit. Python `transferSync` does not set `priority` (default MEDIUM). No in-tree red/green test (#4114 checklist).

### Still open

- **P0-efa-ascend.** `init(..., protocol)` is now forwarded, but the TENT branch only special-cases `"tcp"`. `"efa"` / `"ascend"` do not pin those transports. On `USE_EFA` / `USE_CXI` Python builds, `initialize` still calls `installTransport()` after init; under TENT that returns `nullptr` and `initialize` returns `-1`. #4122 is classic TE Ascend Direct selection, not this shim item.
- **P1-sync-status.** `transferSync` still retries `numContexts()+1` times; under TENT `numContexts()` is hardcoded `1`. The poll loop handles `COMPLETED` / `FAILED` / `TIMEOUT` only — not `CANCELED` — and does not evict the cached handle on poll failure.
- **P1-install-transport.** Added from @chlins (2026-09-14). The TENT branch logs `"installTransport not used by TENT"` and returns `nullptr`. Classic contract: `nullptr` means install failed. Store already skips this via `isUsingTent()` (#2596). C / Go (`transfer_engine_c.h`) and EFA/CXI Python do not. Proposed fix A (TENT returns a non-null sentinel; in-tree callers only null-check) is preferred over gating every caller (B) or fixing only the C shim (C). Waiting on TENT owners (@alogfans) before a PR. Related leftover from the same comment, not yet a row: `freeBatchID` on a busy batch (`BatchBusy` vs TENT lazy sweep).

## Claiming

Open a PR for **one open or partial** work item and link it here (`Refs #3995`).
No maintainer ACK needed.

Please comment on this issue before you start (optional, but helps avoid
duplicate work). Done/partial rows should not grow a second overlapping PR
unless it is a documented residual.

PR title: `[TENT] ...` or `[Bugfix] ...`. The PR should explain **how you
verified the problem is real** (repro steps, logs, or why the path is
unreachable / already safe). Include a test that failed on main under
`MC_USE_TENT=1` and passes after.


## 评论 (8)

### github-actions[bot] · 2026-09-10

Thanks for opening this issue, @staryxchen!

| Field | Value |
|-------|-------|
| **Issue** | #3995 |
| **GitHub user ID** | `151037142` |
| **Reporter** | @staryxchen |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.

### chlins · 2026-09-14

One more `use_tent_` branch worth a row, found by running a classic C-API caller rather than the Python wrapper.

**`installTransport()` returns `nullptr` on TENT, and every classic caller that installs explicitly reads that as failure.**

`transfer_engine.cpp:505-515`: the TENT branch logs "installTransport not used by TENT" and returns `nullptr` by design. Classic callers only know the classic contract, where `nullptr` means the transport failed to install:

- Store client, `!auto_discover` branch (`client_service.cpp:830-900`): `if (!transport) return INTERNAL_ERROR`
- Python wrapper, EFA and CXI builds (`transfer_engine_py.cpp:287-291, 319-323`): `if (!transport) return -1`
- C shim (`transfer_engine_c.cpp:55-59`) passes the pointer through unchanged, so any C or Go caller that checks it fails the same way

The Python happy path only survives because it relies on auto-discovery and never calls `installTransport` on this build. Repro on current `main` (28b2355, TCP-only host): a Go caller over `transfer_engine_c.h` gets `Transfer Engine 127.0.0.1:13001 started successfully` followed immediately by the install failure, before any register or transfer. #2596 already worked around this once for the Store client by gating on `isUsingTent()`.

Options, would like the TENT owners' preference before a PR:

- A. Have the TENT branch return a non-null sentinel meaning "handled by TENT". I grepped the in-tree callers: all of them null-check the result, none dereference it. One change covers Store, Python, C and Go.
- B. Gate each explicit caller on `isUsingTent()`, as #2596 did. Correct, but every future caller has to know to do it.
- C. Fix it in the C shim only.

I lean A and can send it with a runtime check on a C-API caller under `MC_USE_TENT=1` as the test. Not yet verified, blocked on the above: `freeBatchID` on a busy batch (classic returns `BatchBusy`, TENT's `freeBatch` defers to a lazy sweep; callers that drain-then-free may behave differently).

### 0z5a · 2026-09-15

Hi @TTThanos , I'd like to take P2-first-buffer if it is still available.

### staryxchen · 2026-09-15

> One more `use_tent_` branch worth a row, found by running a classic C-API caller rather than the Python wrapper.
> 
> **`installTransport()` returns `nullptr` on TENT, and every classic caller that installs explicitly reads that as failure.**
> 
> `transfer_engine.cpp:505-515`: the TENT branch logs "installTransport not used by TENT" and returns `nullptr` by design. Classic callers only know the classic contract, where `nullptr` means the transport failed to install:
> 
> * Store client, `!auto_discover` branch (`client_service.cpp:830-900`): `if (!transport) return INTERNAL_ERROR`
> * Python wrapper, EFA and CXI builds (`transfer_engine_py.cpp:287-291, 319-323`): `if (!transport) return -1`
> * C shim (`transfer_engine_c.cpp:55-59`) passes the pointer through unchanged, so any C or Go caller that checks it fails the same way
> 
> The Python happy path only survives because it relies on auto-discovery and never calls `installTransport` on this build. Repro on current `main` ([28b2355](https://github.com/kvcache-ai/Mooncake/commit/28b235565bc7eafc514f92bdc4461d290943d239), TCP-only host): a Go caller over `transfer_engine_c.h` gets `Transfer Engine 127.0.0.1:13001 started successfully` followed immediately by the install failure, before any register or transfer. [#2596](https://github.com/kvcache-ai/Mooncake/pull/2596) already worked around this once for the Store client by gating on `isUsingTent()`.
> 
> Options, would like the TENT owners' preference before a PR:
> 
> * A. Have the TENT branch return a non-null sentinel meaning "handled by TENT". I grepped the in-tree callers: all of them null-check the result, none dereference it. One change covers Store, Python, C and Go.
> * B. Gate each explicit caller on `isUsingTent()`, as [[Store][Bugfix]:Fix SGLang fails to start with MC_USE_TENT=1 when built without USE_TENT #2596](https://github.com/kvcache-ai/Mooncake/pull/2596) did. Correct, but every future caller has to know to do it.
> * C. Fix it in the C shim only.
> 
> I lean A and can send it with a runtime check on a C-API caller under `MC_USE_TENT=1` as the test. Not yet verified, blocked on the above: `freeBatchID` on a busy batch (classic returns `BatchBusy`, TENT's `freeBatch` defers to a lazy sweep; callers that drain-then-free may behave differently).

@alogfans What do you think?

### 0z5a · 2026-09-15

> Hi [@TTThanos](https://github.com/TTThanos) , I'd like to take P2-first-buffer if it is still available.

it seems that p2-frist-buffer has already taken by @anranxia .

### RuixiangMa · 2026-09-21

@staryxchen @TTThanos I’d like to take ownership of P1-sync-status

### staryxchen · 2026-09-22

> [@staryxchen](https://github.com/staryxchen) [@TTThanos](https://github.com/TTThanos) I’d like to take ownership of P1-sync-status

 @RuixiangMa Thanks. `P1-sync-status` is already split across open PRs, all touching `transfer_engine_py.cpp`:
  - #4228: TENT sync should not resubmit (retry)
  - #4241: treat `CANCELED` as terminal
  - #4264 (yours): retry + terminal states + stale-handle eviction on poll failure
  Please align with #4228 / #4241. The remaining gap from this RFC is poll-failure eviction (`FAILED` / `TIMEOUT` still keep `handle_map_`); #4109 only covers `submitTransfer` failure. If #4264 is only that leftover, please say so and drop the overlapping retry/`CANCELED` bits.

### RuixiangMa · 2026-09-22

> > [@staryxchen](https://github.com/staryxchen) [@TTThanos](https://github.com/TTThanos) I’d like to take ownership of P1-sync-status
> 
> [@RuixiangMa](https://github.com/RuixiangMa) Thanks. `P1-sync-status` is already split across open PRs, all touching `transfer_engine_py.cpp`:
> 
> * [[Bugfix][Python] Preserve TENT failure decisions in synchronous transfers #4228](https://github.com/kvcache-ai/Mooncake/pull/4228): TENT sync should not resubmit (retry)
> * [[TENT] Handle canceled synchronous transfers in the Python compatibility API #4241](https://github.com/kvcache-ai/Mooncake/pull/4241): treat `CANCELED` as terminal
> * [[Bugfix] Fix TENT sync transfer status handling #4264](https://github.com/kvcache-ai/Mooncake/pull/4264) (yours): retry + terminal states + stale-handle eviction on poll failure
>   Please align with [[Bugfix][Python] Preserve TENT failure decisions in synchronous transfers #4228](https://github.com/kvcache-ai/Mooncake/pull/4228) / [[TENT] Handle canceled synchronous transfers in the Python compatibility API #4241](https://github.com/kvcache-ai/Mooncake/pull/4241). The remaining gap from this RFC is poll-failure eviction (`FAILED` / `TIMEOUT` still keep `handle_map_`); [[Bugfix][TENT] Detect dead peers in CheckSegmentStatus under MC_USE_TENT #4109](https://github.com/kvcache-ai/Mooncake/pull/4109) only covers `submitTransfer` failure. If [[Bugfix] Fix TENT sync transfer status handling #4264](https://github.com/kvcache-ai/Mooncake/pull/4264) is only that leftover, please say so and drop the overlapping retry/`CANCELED` bits.

thx, I will remove the overlapping retry, CANCELED, async-status, and retry-hint changes from #4264. The remaining scope is only cached Segment eviction after synchronous poll failure (`get*TransferStatus()` error, `FAILED`, or `TIMEOUT`). This must be rebased on #4228 first: current TENT sync paths still retry once after the first attempt, so closing an evicted Segment before #4228 could leave that retry using the local stale handle. After #4228 lands, I will rebase and submit only the narrow poll-failure eviction plus its regression test. #4241 remains the owner of CANCELED handling.
