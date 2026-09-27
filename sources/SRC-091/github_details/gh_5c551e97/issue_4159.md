# [Issue #4159] [RFC][P2P] Coordinator-aware CUDA DMA-BUF destination for native RDMA L1

source: https://github.com/LMCache/LMCache/issues/4159
state: open | updated: 2026-09-24T01:48:26Z
labels: 

## 正文

**Summary**

Track a phased follow-up to the native `libibverbs` host-L1 P2P transport:
integrate distributed host-L1 placement and lease metadata with the LMCache coordinator, following the control-plane direction proposed in [#4065](https://github.com/LMCache/LMCache/issues/4065), and add an optional requester-local CUDA DMA-BUF destination for eligible remote demand reads.

The owner and capacity source remain host DRAM. The optimization changes the requester's destination from host L1 to a registered GPU staging buffer:

```text
Current:
owner host L1
  -> one-sided RDMA READ
  -> requester host L1
  -> H2D
  -> requester GPU staging
  -> scatter
  -> paged vLLM KV

Proposed:
coordinator directory / placement / distributed source lease
  -> owner host L1
  -> one-sided RDMA READ
  -> requester GPU staging registered through CUDA DMA-BUF
  -> scatter
  -> paged vLLM KV
```

CUDA DMA-BUF remains a requester-local memory-registration mechanism used through `libibverbs`. No DMA-BUF file descriptor, requester GPU address, local memory key, or local region ID is sent to the coordinator or advertised to a peer.

**Details**

The native host-L1 transport currently keeps the existing LMCache P2P lookup/lock/lifecycle flow and uses the coordinator for membership and peer endpoint discovery. A peer-owned host-L1 object is read into requester host L1, followed by the existing host-to-device copy and scatter into the paged vLLM KV cache.

This issue proposes two related but distinct extensions:

1. Align distributed host-L1 discovery and lifetime metadata with #4065. The proposed coordinator model records owner, tier/backend, placement, generation, and distributed lease/routing information. MP servers continue to own local allocation, source locking, eviction execution, and memory safety.
2. For an eligible LMCache-driven, single-consumer remote demand read, register the requester's existing temporary GPU staging allocation with `ibv_reg_dmabuf_mr()` and read the peer's host-owned bytes directly into that staging slot.

The coordinator is not part of the KV data path:

```text
                         CONTROL PLANE

                  +--------------------------+
                  | LMCache coordinator      |
                  | ObjectKey -> placement   |
                  | owner + tier + generation|
                  | distributed source lease |
                  +------------+-------------+
                               |
                     route / lease metadata
                               |
          +--------------------+--------------------+
          |                                         |
          v                                         v
+-------------------------+              +--------------------------+
| owner MP server         |              | requester MP server      |
| local source lock       |              | local DirectReadLease    |
| host-DRAM L1 owner      |              | GPU staging-slot owner   |
| ibv_reg_mr()            |              | CUDA DMA-BUF FD          |
| remote-read rkey        |              | ibv_reg_dmabuf_mr()      |
+------------+------------+              +-------------+------------+
             |                                             ^
             |          DATA PLANE: RDMA READ              |
             +=============================================+
                                                           |
                                                 CQ + CUDA visibility
                                                           |
                                                           v
                                                  existing scatter kernel
```

The design uses two nested lifetime mechanisms rather than two competing
authorities:

- The coordinator is authoritative for distributed placement and lease metadata once the #4065 schema is agreed. Proposed fields include owner, generation/epoch, and expiry.
- Before posting RDMA, the owner MP server atomically validates the coordinator-provided owner, generation, and lease token and acquires its local source lock. A mismatch invalidates the placement and causes a new lookup or host-path fallback before a direct hit is reported.
- The requester MP server's **`DirectReadLease`** owns the local QP operation, GPU staging slot, CUDA scatter event, cancellation, and release of the owner MP server's local source lock.

Local unlock and coordinator lease release must both be idempotent: retries may occur, but each release has one logical effect. Lease expiry and reconciliation must recover abandoned requests without leaving an indefinite distributed pin.

The coordinator must not directly mutate local memory, manage QPs, or own CUDA allocations. The owner MP server remains the final authority for whether the source bytes are locally safe to read.

The same native QPs, CQs, work requests, and remote host-L1 registration remain in use. DMA-BUF changes only how the requester-local destination memory region is registered. It does not replace `libibverbs` or make the network link itself faster.

The default must remain the current host-destination path. The proposed configuration is:

```text
--p2p-rdma-gpudirect {off,auto,required}
```

- `off`: preserve existing host-L1 behavior and remain the default.
- `auto`: use GPU staging only when the request, CUDA device, HCA provider, and topology are eligible; otherwise choose the host path before reporting a hit.
- `required`: fail setup or reject an ineligible lookup rather than silently selecting the host path.

Initial direct-mode eligibility is intentionally narrow:

- LMCache-driven GPU retrieval only;
- remote demand reads only;
- one consumer (`extra_count == 0`);
- an exportable, page-aligned GPU staging allocation;
- a qualified GPU/HCA topology; and
- successful registration on every selected HCA rail.

Local-L1 hits, warm/speculative prefetch, CPU consumers, and TP/MLA or other multi-consumer requests continue to use requester host L1.

### Proposed PR phases

Contributors should claim one phase rather than implementing the entire issue in one PR:

1. **Design, capability probe, and instrumentation**
   - Report CUDA device DMA-BUF support, `ibv_reg_dmabuf_mr` availability,
     provider registration result, and GPU/HCA topology.
   - Measure current RDMA wait, requester-host destination, H2D staging,
     scatter, and total remote-hit time.

2. **Native registered-local-region support**
   - Add an RAII DMA-BUF local-region type and per-rail region mapping.
   - Preserve host L1 as the remotely advertised region.
   - Add atomic multi-rail registration rollback and lifecycle tests.
   - Do not change LMCache lookup or retrieval routing.

3. **Exportable per-GPU temporary-buffer backing**
   - Reuse the existing temporary GPU staging abstraction; do not create a
     second independent staging pool.
   - Add bounded slot states, CUDA visibility handling, and event-safe reuse.
   - Register once per GPU context and selected HCA, not per request.

4. **Typed direct-demand integration in the MP server**
   - Add a typed direct-demand result and explicit local lease state table.
   - Keep the generic "loaded into requester L1" result unchanged.
   - Add cancellation, expiry, worker-reaping, peer-removal, and shutdown
     handling with an idempotent source unlock that has one logical effect.
   - Keep the current peer lookup path initially so transport and lifetime
     correctness can be reviewed independently.

5. **Coordinator directory and distributed-lease integration**
   - This phase is blocked on the directory and lease decision in #4065.
   - Split it into separate child tasks/PRs for:
     1. L1 placement schema and lifecycle-event ingestion;
     2. lookup routing plus owner/generation/lease-token validation;
     3. idempotent lease release, expiry, and stale-placement cleanup; and
     4. coordinator epoch change, restart, and resync behavior.
   - Retain owner-side local locking and requester-side `DirectReadLease`
     safety throughout; do not pass a GPU-memory descriptor through the
     coordinator.

6. **Qualification and observability**
   - Add direct/host byte counters, fallback reasons, slot occupancy,
     registration time, visibility-fence time, CQ errors, and quiescence
     counters.
   - Run matched correctness, stability, low-batch, and performance tests.

Phases 1-4 do not require a coordinator protocol change. DMA-BUF registration and the first typed direct-demand path are local/peer plumbing. Phase 5 is where the data path becomes coordinator-aware and depends on the distributed directory/lease semantics agreed in #4065.

**Steps / Reproduction (if applicable)**

Current baseline, once the native host-L1 transport PR is available:

The steps below define the intended logical baseline. Before this issue is published, replace the generic launch/populate/request actions with a public base PR or commit, exact two-server commands or a checked-in harness, and the expected LMCache/HCA counters. Until those artifacts exist, this section is not an independently executable reproduction.

1. Build the optional native extension in the runtime environment:

   ```bash
   BUILD_WITH_RDMA_L1=1 uv pip install -e . --no-build-isolation
   ```

2. Start the coordinator and two LMCache MP servers with native verbs enabled, lazy L1 allocation disabled, and the intended HCA device, port, GID, and queue-depth settings.

3. Populate an object in server A's host L1, wait for pending store work to finish, and clear or miss only server B's L1.

4. Request the same KV prefix through server B and collect LMCache traces, allocation counters, and HCA counters.

5. Confirm the current behavior: server B issues an RDMA READ from server A, receives the bytes into requester host L1, and then performs H2D staging and the existing GPU scatter. No DMA-BUF region participates.

**Expected Outcome / Goal**

- The coordinator can represent host-L1 owner, placement, generation, and distributed lease/routing metadata consistently with #4065.
- MP servers retain authority over local memory mutation, local locks, QPs, GPU slots, and lifetime safety.
- Eligible remote demand reads can terminate directly in requester GPU staging through a requester-local CUDA DMA-BUF memory region.
- The existing scatter kernel remains responsible for placing contiguous staging data into final paged vLLM KV allocations.
- `off` preserves the current native host-L1 behavior.
- `auto` falls back before hit reporting when capability or eligibility checks fail.
- After a direct hit has been reported, transfer failure fails closed and lets the serving engine recompute; partially written GPU data is never treated as a cache hit.
- NIXL and other transfer engines retain their existing contracts and default behavior.
- Performance conclusions are based on topology-, rail-, concurrency-, and capacity-matched repeated tests.


## 评论 (4)

### sbates130272 · 2026-07-24

@DongDongJu what advantages do you see to this approach above and beyond using the dma-buf approach in NIXL (which we already use for p2p). I'm keen to avoid duplication of code that's already in NIXL being added to lmcache. It leads to bloat. 

Thanks!

### DongDongJu · 2026-07-24

> [@DongDongJu](https://github.com/DongDongJu) what advantages do you see to this approach above and beyond using the dma-buf approach in NIXL (which we already use for p2p). I'm keen to avoid duplication of code that's already in NIXL being added to lmcache. It leads to bloat.
> 
> Thanks!

Hello @sbates130272, Thanks for the interest. I will reply at the same question you had in the #4161.

### github-actions[bot] · 2026-09-23

This issue has been automatically marked as stale because it has not had activity within 60 days. It will be automatically closed if no further activity occurs within 30 days.

### sbates130272 · 2026-09-23

Can I request we use CUDA/ROCm since AMD is also a target GPU? 😃. 
