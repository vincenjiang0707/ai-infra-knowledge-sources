# [Issue #4228] [RFC][PD] Two-tier PD receiver staging: GPU fast path with CPU spillover

source: https://github.com/LMCache/LMCache/issues/4228
state: open | updated: 2026-09-27T01:56:03Z
labels: stale

## 正文

## 1. Problem

The PD receiver stages incoming KV in a **single fixed-size buffer** whose device
is chosen once by `pd_buffer_device` (`pd_backend_async.py:450-453`, `:557`). That
buffer must hold the *entire* KV of every request that has been prefilled-and-
transferred but not yet consumed by decode (the reservation is all-or-nothing by
design, to avoid the partial-allocation deadlock). Today an operator gets exactly
two operating points, and both have a sharp edge:

- **`pd_buffer_device=cuda` — fast, but a hard capacity wall.** Staging lives in
  GPU HBM, contending with vLLM's paged decode KV pool for the same leftover HBM.
  You cannot size it for concurrency without starving decode. When concurrent
  prefills exceed capacity, admission correctly serializes or times out, and the
  transfer is torn down mid-flight.

- **`pd_buffer_device=cpu` — robust, but pays H2D on every request.** Staging in
  host RAM removes the HBM contention entirely (host RAM is plentiful and
  uncontended), so it absorbs bursts. But *every* transfer now costs a
  host→device copy on the decode-side read, adding TTFT latency even to the 99%
  of requests that never needed the extra capacity.

Concrete numbers from a real run (Qwen3-32B, TP=1, bf16; `262144` B/token →
`64 MiB` per 256-token chunk):

- `pd_buffer_size = 8 GiB` = 128 chunks; a 16 384-token prefill = 65 chunks.
- The GPU staging pool admits only `floor(128 / 65) = 1` concurrent 16k prefill.
- At `CON=4`, three requests wait for a reservation, hit
  `pd_allocation_timeout_sec`, and the decoder resets the connections
  (`ServerDisconnectedError` / `Not enough data to satisfy transfer length header`).
- Sizing the GPU pool for `CON=4` would need `260` chunks ≈ `17 GiB`, which would
  starve the ~16 GiB decode KV pool sharing the same HBM.

So the fast mode has no burst headroom, and the robust mode taxes steady-state
latency. There is no operating point that is *fast in the common case and robust
under bursts*.

## 2. Non-goals

- **No vLLM / SGLang changes.** This is entirely receiver-side; the sender→receiver
  transfer contract is extended, not the engine hooks.
- **The deadlock-free reservation property is preserved.** Admission stays
  all-or-nothing *per tier*; we do not reintroduce partial-allocation deadlock.
- **No change to the prefill/decode compute or scheduling policy.**
- **Not auto-sizing.** Choosing the GPU vs CPU pool sizes stays the operator's
  job (though a follow-up capacity advisor is noted in Open Questions).

## 3. Proposal

Keep the **GPU staging buffer small and fast** (low HBM, doesn't fight decode).
When it is saturated, instead of waiting out `pd_allocation_timeout_sec` and
resetting, **admit the overflow request into a CPU staging pool**. The decoder
reads each chunk from whichever tier holds it. Bursts degrade to *slower*, not
*broken*.

```text
                    receiver admission (per request)
                                |
                 try reserve on GPU tier (fast path)
                    |                         |
              fits (common)              full (burst)
                    |                         |
        GPU staging (VRAM)          CPU staging (host RAM)
        GPU->GPU RDMA write          GPU->host RDMA write
                    |                         |
        read: scatter to KV          read: H2D then scatter to KV
                    \_________________________/
                                |
                        vLLM paged decode KV
```

Crucially, **this is orchestration of two already-shipping, individually proven
paths** — `pd_buffer_device=cuda` and `pd_buffer_device=cpu` both work today. The
new work is doing both, per request, in one receiver. Three changes:

1. **Init both pools.** `PagedCpuGpuMemoryAllocator` is *already* dual-pool — it
   holds a `gpu_allocator` and a `cpu_allocator` and routes on
   `allocator_type` (`paged_cpu_gpu_memory_allocator.py:113-116`). Today the PD
   backend initializes only one (`pd_backend_async.py:450-453`). Init both: GPU at
   `pd_buffer_size`, CPU at a new `pd_buffer_overflow_size`.

2. **Two-tier reservation.** `ReservationManager` tracks reserved/total per tier.
   `async_try_admit` tries the GPU tier first; on insufficient GPU chunks it admits
   against the CPU tier (and tags the reservation's tier) rather than returning
   `False`. A request is admitted wholly to one tier (keeps reads simple, keeps the
   deadlock-free property). The fail-fast from #4209 generalizes to "exceeds *both*
   tiers combined."

3. **Tier-tagged transfer.** `AllocResponse` carries a per-chunk (or per-request)
   tier tag so the sender's RDMA write targets the correct registered region. This
   is the one change that reaches beyond the PD backend — see §5.

## 4. Why this over what LMCache already supports

Honest framing, because `pd_buffer_device=cpu` already solves *robustness*:

| Mode | Robust under bursts | Steady-state latency | Exists today |
|---|---|---|---|
| `pd_buffer_device=cuda` | no (HBM wall) | fast (no H2D) | yes |
| `pd_buffer_device=cpu` | yes (host RAM) | slower (H2D every request) | yes |
| **two-tier spillover** | yes | fast common case; H2D only on overflow | **no** |

The unique thing two-tier buys is **decoupling steady-state latency from burst
capacity** — p50 TTFT stays at GPU-fast-path levels while p99/burst behavior
degrades gracefully instead of failing. For bursty PD serving that is a real
Pareto improvement. It is *not* a new capability for the robust case (CPU mode
already covers that); it is a latency optimization for the common case. Whether
that optimization is worth the complexity below is the central question this RFC
asks maintainers to weigh — see §7.

## 5. The hard part (design decisions for reviewers)

- **NIXL multi-region registration.** `NixlChannel.__init__` today registers a
  *single* region: one `buffer_ptr` + `buffer_size` + `device`
  (`nixl_channel.py:70-93`). NIXL itself supports registering multiple regions
  (VRAM + DRAM), but LMCache's wrapper does not expose it. Two-tier needs the
  channel to register **both** the GPU and CPU pools and select the right one per
  transfer. This channel is a **shared abstraction other backends use**, so this
  is the change most likely to ripple beyond PD — the blast radius maintainers
  most need to weigh in on.
- **Protocol tier tag.** `AllocResponse` gains a tier field. Small, backward-
  compatible (absent = GPU), but it is a wire-format change.
- **Admit-to-one-tier vs split.** Proposal keeps each request wholly in one tier
  to keep the read path and reservation accounting simple; splitting a single
  request across tiers is possible but adds mixed-tier reads for little gain.
- **Promotion.** When GPU frees up, do CPU-staged requests migrate to GPU?
  Proposed: no — they are simply read from CPU. Migration is not worth the churn.

## 6. Open questions

1. **Is the win real?** How much does the CPU-tier H2D actually add to TTFT, and
   how bursty are target workloads? A three-way benchmark (`cuda` failing
   baseline, `cpu`, two-tier) on the `CON=4 / 16k` shape bounds the prize. If CPU
   mode's latency is already acceptable, this RFC may not be worth building.
2. **How far does the NIXL multi-region change ripple?** Does exposing dual
   registration in the channel touch P2P / NIXL-storage backends, or can it be
   additive?
3. **Config surface.** `pd_buffer_overflow_size` + `pd_buffer_overflow_device`,
   or fold into a list-valued `pd_buffer_tiers`? Should overflow default off
   (opt-in) for a first landing?
4. **Interaction with the capacity fail-fast (#4209).** The fail-fast should
   trigger only when a request exceeds *combined* tier capacity.

## 7. Scope / rollout

- **v1:** async receiver + NIXL channel + vLLM; behind a config flag, overflow
  off by default. The reservation/routing/accounting core is unit-testable
  without a GPU (same harness as #4210); the NIXL multi-region path needs the real
  stack to validate.
- Sync backend and SGLang are follow-ups.

## Relationship to existing work

Builds directly on the receiver reservation/admission control and the capacity
fail-fast (#4209 / PR #4210). Independent of the MP-mode PD orchestration RFC
(#4085), which concerns the control plane (routing/completion signaling); this RFC
concerns the receiver-side data-plane staging tier.


## 评论 (3)

### ApostaC · 2026-07-27

Hi @ardecode , thanks for your RFC! I think this is mainly for the non-MP mode. However, the community's focus has already shifted to MP mode, and we will have a different PD solution in MP mode.

### ardecode · 2026-07-28

Thanks @ApostaC. That's good to know. Happy to close this as not-planned. Two questions first, so I can point my effort at the right
place:
1. Is the MP-mode PD design tracked publicly anywhere yet - #4085, or something new? I'd rather
   contribute there than keep iterating on the non-MP path.
2. Does the MP-mode design have a story for receiver-side staging capacity? The failure mode
   inverts rather than disappearing: with an eviction-based pool and no reservation, a burst can
   evict KV that decode hasn't consumed yet, which surfaces as a silent miss and recompute
   instead of a timeout. If that's already covered (pinning until read, or per-in-flight-request
   quota), then this is a non-issue. I just couldn't find where it's handled.

### github-actions[bot] · 2026-09-27

This issue has been automatically marked as stale because it has not had activity within 60 days. It will be automatically closed if no further activity occurs within 30 days.
