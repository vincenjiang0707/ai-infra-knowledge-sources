# [Issue #2566] [BUG][Fuzzer][ice-on-valid-code] Single-iteration warp-specialized pipelined loop deadlocks at runtime on Hopper (sm_90) instead of completing

source: https://github.com/tile-ai/tilelang/issues/2566
state: open | updated: 2026-09-08T09:26:03Z
labels: bug

## 正文

### Required prerequisites

- [x] I have read the documentation <https://tilelang.com>.
- [x] I have searched the [Issue Tracker](https://github.com/tile-ai/tilelang/issues) that this hasn't already been reported. (comment there if it has.)

### What version of TileLang are you using?

0.1.11

### System information


- Installed from the `0.1.11` wheel; source pinned to tag `v0.1.11` (commit `cd37ed5fc35ae7a60a1277c8eb49028174ac51e6`).
- Python 3.12.3, Linux; PyTorch 2.12.1+cu130 (CUDA 13.0).
- GPU: **NVIDIA H100 80GB HBM3** (compute capability 9.0, sm_90). Reproduced on this H100; the defect is on the warp-specialized TMA producer/consumer path, which is the default on sm_90, so it is expected to be sm_90-gated (not tested on other architectures).

```python
import sys, tilelang, torch
print(sys.version.split()[0], sys.platform)   # 3.12.3 linux
print(tilelang.__version__)                    # 0.1.11
print(torch.__version__)                        # 2.12.1+cu130, CUDA 13.0
print(torch.cuda.get_device_name(), torch.cuda.get_device_capability())  # NVIDIA H100 80GB HBM3 (9, 0)
```


### Problem description


A well-formed kernel that compiles cleanly (no error, no warning) **hangs forever** when launched on Hopper.

The trigger is a warp-specialized pipelined loop that **executes exactly one iteration** — e.g. `for k in T.Pipelined(1, num_stages=S)`. The launch never returns: the kernel dispatches, `torch.cuda.synchronize()` blocks forever, and the GPU sits pinned on an unsatisfiable barrier wait until the process is killed. There is no traceback and no compile diagnostic.

The trigger is **exactly `trip_count == 1`, independent of `num_stages`**. Compiling the identical kernel with `pass_configs={"tl.disable_warp_specialized": True}` runs to completion and returns the correct result, which isolates the defect to the Hopper warp-specialization path.

### Observed (H100, TileLang 0.1.11, default warp-spec on; each cell run in isolation under a 120 s timeout)

| `num_stages` | trip count | result |
|---|---|---|
| 1 | 1 | **HANG** (timeout, no return) |
| 2 | 1 | **HANG** (timeout, no return) |
| 3 | 1 | **HANG** (timeout, no return) |
| 1 | 2 | returns (~9 s) |
| 1 | 3 | returns (~9 s) |
| 2 | 2 | returns (~9 s) |
| 2 | 3 | returns (~9 s) |
| 3 | 2 | returns (~9 s) |
| 3 | 3 | returns (~9 s) |
| 4 | 2 | returns (~9 s) |
| 4 | 3 | returns (~9 s) |

The 11 cells partition cleanly: **`trip == 1` → HANG (3/3), `trip >= 2` → returns (8/8)**, for every `num_stages` tested. In particular `num_stages=4, trip=2` and `num_stages=4, trip=3` return normally even though `trip < num_stages`, and `num_stages=1, trip=1` hangs with a single stage. `num_stages` plays no role in whether the kernel hangs; only the single-iteration trip count does.


### Reproducible example code


```python
import tilelang
import tilelang.language as T
import torch

STAGES = 2
NTILES = 1          # trip count == 1  =>  HANG with warp-spec; correct when disabled
bM, bN = 64, 128
THREADS = 256


def make(M, N, T_):
    dt = "float16"

    @T.prim_func
    def main(A: T.Tensor((T_, M, N), dt), C: T.Tensor((M, N), "float32")):
        with T.Kernel(T.ceildiv(N, bN), T.ceildiv(M, bM), threads=THREADS) as (bx, by):
            As = T.alloc_shared((bM, bN), dt)
            Cf = T.alloc_fragment((bM, bN), "float32")
            T.clear(Cf)
            for k in T.Pipelined(T_, num_stages=STAGES):
                T.copy(A[k, by * bM, bx * bN], As)
                for i, j in T.Parallel(bM, bN):
                    Cf[i, j] += As[i, j]
            T.copy(Cf, C[by * bM, bx * bN])
    return main


def run(ws, A, ref, M, N, T_):
    f = make(M, N, T_)
    k = tilelang.compile(f, pass_configs={"tl.disable_warp_specialized": (not ws)})
    C = torch.zeros(M, N, device="cuda", dtype=torch.float32)
    print(f"launching {'WS' if ws else 'NOWS'} kernel...", flush=True)
    k(A, C)
    torch.cuda.synchronize()
    print(f"{'WS' if ws else 'NOWS'} RETURNED err={(C - ref).abs().max().item()}", flush=True)


def main():
    M = N = 128
    T_ = NTILES
    torch.manual_seed(0)
    A = torch.randint(0, 4, (T_, M, N), device="cuda").to(torch.float16)
    ref = A.float().sum(0)
    run(False, A, ref, M, N, T_)   # control: disable_warp_specialized -> returns
    run(True, A, ref, M, N, T_)    # warp-spec default: HANGS (never reaches RETURNED)


if __name__ == "__main__":
    main()
```

Output (deterministic; warp-spec branch never returns, killed by the timeout — `exit 124`):

```
launching NOWS kernel...
NOWS RETURNED err=0.0
launching WS kernel...
<hangs forever — no further output; GPU pinned at 100% util on the unsatisfiable barrier wait>
```

Setting `NTILES = 2` (or larger) makes the warp-spec build return as well.


### Traceback

```pytb
There is **no traceback** — the kernel compiles cleanly (no compile error, no warning) and the launch hangs. The process must be killed (`timeout`/SIGKILL); the GPU is at 100% utilization for the duration of the hang. The behavior is deterministic across repeated runs.
```

### Expected behavior

A warp-specialized pipelined loop with a single iteration should run to completion (and return the same result as the non-warp-specialized path, which already computes it correctly — see the control), rather than emitting a kernel that deadlocks. The single-iteration TMA copy must emit a complete producer/consumer mbarrier handshake (both the transaction-bytes count *and* the arrival) so the consumer's data-ready wait can complete.


### Additional context


**Root cause — the single-iteration TMA load is lowered through a 1D bulk-copy path that drops the forward-barrier `mbarrier.arrive`.**

When the pipelined loop has exactly one iteration, the global slice `A[k=0, ...]` folds to a fully-contiguous constant-offset region and the shared destination `As` keeps a plain (non-swizzled) linear layout, so the copy is classified as a **1D bulk copy** (`kBulkLoad1D`) and lowered by `LowerBulk1D`. In that function's TMA-copy branch the forward barrier gets a bare `mbarrier.expect_tx` and **no `mbarrier.arrive`** — the `emit_arrive` annotation that the warp-spec pass sets is ignored there. The forward barrier is `init(1)`, so its phase-0 completion needs **both** the transaction bytes (delivered by `cp.async.bulk...complete_tx::bytes`) *and* one arrival. The bytes arrive; the arrival never does, so the consumer's data-ready `mbarrier.wait(0)` blocks forever.

For `trip >= 2` the `k`-varying global slice needs a multidimensional `CUtensorMap` descriptor and `As` is swizzled, so the 1D path is rejected and the descriptor path `LowerBulk` — which *does* honor `emit_arrive` and emits `arrive_and_expect_tx` — is used, so the handshake closes. That is why only the single-iteration case hangs.

<details>
<summary>Source trace (verified against two generated-CUDA dumps, trip=1 vs trip=2, on H100 @ <code>cd37ed5f</code>)</summary>

1. The warp-spec pass sets `is_tma_copy=1` and `emit_arrive=1` on the TMA copy ([`producer_consumer_ws.cc#L792`](https://github.com/tile-ai/tilelang/blob/cd37ed5fc35ae7a60a1277c8eb49028174ac51e6/src/cuda/transform/producer_consumer_ws.cc#L792), [`#L1739-L1742`](https://github.com/tile-ai/tilelang/blob/cd37ed5fc35ae7a60a1277c8eb49028174ac51e6/src/cuda/transform/producer_consumer_ws.cc#L1739-L1742)), so a downstream arrive is expected on the forward barrier.

2. Copy classification: for `trip==1`, `CheckBulkCopy1D` is true (`shared_is_contiguous && global_is_contiguous && element_match`, [`copy_analysis.cc#L268-L309`](https://github.com/tile-ai/tilelang/blob/cd37ed5fc35ae7a60a1277c8eb49028174ac51e6/src/cuda/op/copy_analysis.cc#L268-L309)). `SelectTmaInst` checks `can_bulk_load_1d` **before** `can_bulk_load` ([`copy_analysis.cc#L505-L521`](https://github.com/tile-ai/tilelang/blob/cd37ed5fc35ae7a60a1277c8eb49028174ac51e6/src/cuda/op/copy_analysis.cc#L505-L521)), so `kBulkLoad1D` wins and dispatch routes to `LowerBulk1D` ([`copy.cc#L690-L694`](https://github.com/tile-ai/tilelang/blob/cd37ed5fc35ae7a60a1277c8eb49028174ac51e6/src/cuda/op/copy.cc#L690-L694)). This selects the raw-pointer `tma_load(void* smem, void const* gmem, ...)` overload (`cp.async.bulk.shared::cta.global.mbarrier::complete_tx::bytes`, [`copy_sm90.h#L18-L26`](https://github.com/tile-ai/tilelang/blob/cd37ed5fc35ae7a60a1277c8eb49028174ac51e6/src/tl_templates/cuda/copy_sm90.h#L18-L26)), not a `CUtensorMap` descriptor TMA.

3. Bug site: `LowerBulk1D`, the `is_load && barrier_base_id >= 0` block ([`copy.cc#L2064-L2090`](https://github.com/tile-ai/tilelang/blob/cd37ed5fc35ae7a60a1277c8eb49028174ac51e6/src/cuda/op/copy.cc#L2064-L2090)). In the `GetIsTmaCopy(op)==true` branch it emits **only** `mbarrier_expect_tx` and leaves `barrier_after_tma_stmt = std::nullopt` — it never emits `ptx_arrive_barrier` and it ignores `emit_arrive` entirely; then at `#L2088` `if (GetIsTmaCopy(op)) return producer;` returns the expect_tx-only sequence. Contrast the descriptor path `LowerBulk`, whose TMA branch honors `emit_arrive` and emits `ptx_arrive_barrier` ([`copy.cc#L1757-L1762`](https://github.com/tile-ai/tilelang/blob/cd37ed5fc35ae7a60a1277c8eb49028174ac51e6/src/cuda/op/copy.cc#L1757-L1762)).

4. Generated CUDA, **trip=1 (HANG):** `mbarrier[0].init(1); ... mbarrier[0].expect_transaction(16384); tl::tma_load((&As[0]), (&A[...]), mbarrier[0], 16384); ... mbarrier[0].wait(0);` — the raw-pointer overload, **no arrive** between the copy and the wait. `expect_transaction` maps to the cutlass `mbarrier.expect_tx` (no arrive). Phase 0 never flips → `wait(0)` blocks forever.

5. Generated CUDA, **trip=2 (returns):** `mbarrier[k].arrive_and_expect_tx(16384); tl::tma_load(A_desc, mbarrier[k], ...); ... mbarrier[k].wait(0);` — the `CUtensorMap` descriptor overload with `arrive_and_expect_tx` (cutlass `mbarrier.arrive.expect_tx`), so phase 0 completes.

The distinction is confirmed in the vendored cutlass barrier API: `expect_transaction` → `mbarrier.expect_tx` (tx-count only, no arrive), `arrive_and_expect_tx` → `mbarrier.arrive.expect_tx` (arrive + tx-count).
</details>

**Provenance.** Introduced in the `0.1.9 → 0.1.10` release window: an earlier build (0.1.9) ran the same single-iteration repro to completion, and the deadlock is present on 0.1.10, 0.1.11, and 0.1.12. The exact introducing commit has not been re-bisected for this write-up, so treat the `0.1.9 → 0.1.10` window as approximate. Verification: the trigger boundary was established by an 11-cell `num_stages × trip` sweep on H100 (0.1.11), each cell run in isolation with a 120 s timeout, with HANG confirmed by three signals (exit 124, ~120 s wall, success line absent); the mechanism was verified by two compile-time CUDA dumps (trip=1 vs trip=2) on H100 at commit `cd37ed5f`, cross-checked against the cutlass mbarrier API. The fix below is **read-verified against source but not built or run** (it lands in compiled C++).

<details>
<summary>Suggested fix (proposed; read-verified, not built)</summary>

Make `LowerBulk1D`'s TMA-copy branch emit the paired `mbarrier.arrive` for the forward barrier, honoring `emit_arrive` exactly like the descriptor path `LowerBulk` does. In [`copy.cc#L2064-L2090`](https://github.com/tile-ai/tilelang/blob/cd37ed5fc35ae7a60a1277c8eb49028174ac51e6/src/cuda/op/copy.cc#L2064-L2090), inside the `GetIsTmaCopy(op)` true-branch, after emitting `mbarrier_expect_tx`, mirror [`copy.cc#L1757-L1762`](https://github.com/tile-ai/tilelang/blob/cd37ed5fc35ae7a60a1277c8eb49028174ac51e6/src/cuda/op/copy.cc#L1757-L1762):

```cpp
if (auto emit_arrive_val = annotations.Get("emit_arrive")) {
  if (Downcast<IntImm>(emit_arrive_val.value())->value != 0) {
    barrier_after_tma_stmt =
        Evaluate(Call(DataType::Handle(), builtin::ptx_arrive_barrier(),
                      {mbar_handle}));
  }
}
```

`barrier_after_tma_stmt` is already appended to the producer sequence when defined ([`copy.cc#L2080-L2082`](https://github.com/tile-ai/tilelang/blob/cd37ed5fc35ae7a60a1277c8eb49028174ac51e6/src/cuda/op/copy.cc#L2080-L2082)), and the arrive is fused downstream into `arrive_and_expect_tx`, so this makes the 1D warp-spec producer satisfy the forward barrier's `init(1)` arrival count and the consumer's `wait(0)` completes — matching the working descriptor path.

Defensive alternative: in `SelectTmaInst`/`SelectCopyInstForLowering`, do not prefer `kBulkLoad1D` for a warp-spec producer copy (i.e. when `emit_arrive`/`is_tma_copy` is set with an attached barrier), so the single-iteration copy takes the same descriptor path (`LowerBulk`) as the multi-iteration case. Either way, the targeted arrive-emission fix is minimal and behavior-preserving for the existing (correct) non-warp-spec 1D path, which manages `mbarrier_expect_tx`/`wait` itself.

Note: clamping `num_stages` to the trip count does **not** fix this — the `num_stages=1, trip=1` cell still hangs, so `num_stages` is not on the causal path.
</details>

<details>
<summary>Distinct from previously reported issues</summary>

Not a duplicate of the nearby Hopper warp-spec reports:

- **#2559** — closest sibling: a warp-specialized GEMM that hangs forever at launch (also silent, also H100/sm_90). But its trigger is adding `T.annotate_min_blocks_per_sm(2)`, and its root cause is a register-budget reconciliation failure: `min_blocks_per_sm` halves the `__launch_bounds__` register ceiling while `AnnotateWarpGroupRegAlloc`'s `setmaxnreg` counts are unchanged (never read `min_blocks_per_sm`). That is a different pass, a different trigger (an occupancy annotation, not the trip count), and a different mechanism (inconsistent `setmaxnreg`, not a dropped `mbarrier.arrive`). This report needs **no** annotation and fires on a bare single-iteration loop.
- **#2547** — two `T.gemm` into one fragment fail `LayoutInference` under default WS: a **compile-time abort**, not a runtime deadlock; unrelated trigger.
- **#2548** — WS pass hard-aborts (internal `ICHECK`) on a `T.Pipelined` inside a `while`: a **compile-time crash**, not a silent runtime hang; different trigger.
- **#2556** — `tl.ThreadSync` drops a `__syncthreads()` for non-32-multiple thread counts: a synchronization race in a different pass, unrelated.
- **#2346** (`Producer-Consumer TMA + Thread ID and Hangs`) and **#2192** (unexpected CTA-wide `__syncthreads()` between WS scopes) are also WS-path issues but with distinct triggers — absolute-vs-relative thread-ID use inside a pipeline, and a serializing barrier between producer/consumer scopes (a performance defect, not a hang), respectively. Neither involves the single-iteration `LowerBulk1D` arrive-drop.

This report is a **silent runtime deadlock** whose sole trigger is a single-iteration (`trip==1`) warp-specialized pipelined loop, rooted in the dropped `mbarrier.arrive` in `LowerBulk1D`. No open or closed issue covers this specific trigger + root cause.
</details>


## 评论 (2)

### xiaguan · 2026-08-12

Confirming this is **not sm_90-gated**: reproduced on **sm_103 (NVIDIA GB300, Blackwell Ultra)** with tilelang **0.1.12**, PyTorch 2.13.0+cu130 (CUDA 13.0), Python 3.12.3.

We hit it in real code rather than a fuzzer: a split-K GEMV where one projection's shape worked out to `K=512, SK=8, BK=64` → `KS // BK = 1` pipelined iteration. The kernel compiles cleanly, launches, and never returns — GPU pinned at 100%, `torch.cuda.synchronize()` blocks forever. `num_stages=3` and `num_stages=1` both deadlock; the same body with `T.serial` in place of `T.Pipelined` completes in milliseconds with correct results.

Minimal repro on sm_103 (hangs at the marked line):

```python
import tilelang
import tilelang.language as T
import torch

tilelang.disable_cache()
N, BK, BN = 4096, 64, 256

@T.prim_func
def gemv_1iter(
    X: T.Tensor((BK,), "bfloat16"),
    W: T.Tensor((BK, N), "bfloat16"),
    P: T.Tensor((N,), "float32"),
):
    with T.Kernel(T.ceildiv(N, BN), threads=256) as bx:
        Ws = T.alloc_shared((BK, BN), "bfloat16")
        Xs = T.alloc_shared((BK,), "bfloat16")
        acc = T.alloc_fragment((BN,), "float32")
        T.clear(acc)
        for ko in T.Pipelined(1, num_stages=1):   # trip count 1 -> hang
            T.copy(W[ko * BK:(ko + 1) * BK, bx * BN:(bx + 1) * BN], Ws)
            T.copy(X[ko * BK:(ko + 1) * BK], Xs)
            for j in T.Parallel(BN):
                for kk in T.serial(BK):
                    acc[j] += Xs[kk].astype("float32") * Ws[kk, j].astype("float32")
        for j in T.Parallel(BN):
            P[bx * BN + j] = acc[j]

k = tilelang.compile(gemv_1iter)
x = torch.randn(BK, device="cuda", dtype=torch.bfloat16)
w = torch.randn(BK, N, device="cuda", dtype=torch.bfloat16)
p = torch.empty(N, device="cuda", dtype=torch.float32)
k(x, w, p)                  # hangs here
torch.cuda.synchronize()
```

Workaround that unblocked us: pick the loop construct at build time — `T.Pipelined(iters, num_stages=min(stages, iters))` when `iters >= 2`, else a plain `T.serial(iters)` loop with the identical body. Until the producer/consumer path handles trip count 1, it might be worth either lowering single-iteration `T.Pipelined` to the non-pipelined path automatically or rejecting it at compile time — a clean error would have saved a long debugging session (the hang presents as a 100%-utilization GPU with no output, indistinguishable from slow work).


### cklxx · 2026-09-08

Not reproducing on tilelang 0.1.14 / H20 (sm_90) / CUDA 12.9 / torch 2.11.

Both repros in this thread return with `err=0.0`: the original `num_stages=2, trip=1` case and the `num_stages=1` split-K GEMV from the sm_103 report.

Sweeping the reported trigger more widely — block `{64,128} x {128,256}`, threads `{128,256,384}`, `trip {1,2}`, `num_stages {1,2,3,4}`, `{float16, bfloat16}` — 120 of the 192 combinations are legal on this GPU and all 120 complete with exact results. The remaining 72 fail at compile time for reasons unrelated to this issue (threads=384 has no valid layout for these tiles; `num_stages=4` on 128x256 needs 256KB of shared memory). Nothing hangs, and `trip==1` passes exactly as often as `trip==2` (60/96 each), which is the split this issue is about.

Warp specialization is confirmed active in the generated code, so this is not a case of the WS path silently being skipped — for `num_stages=2, trip=1`:

```
if (((int)threadIdx.x) < 128) {          // producer
  tl::warpgroup_reg_dealloc<24>();
  mbarrier[2].wait(1);
  if (tl::tl_shuffle_elect<128>()) {
    mbarrier[0].arrive_and_expect_tx(16384);
    tl::tma_load((&(As[0])), ..., mbarrier[0], 16384);
  }
} else {                                  // consumer
  tl::warpgroup_reg_alloc<240>();
  ...
  mbarrier[0].wait(0);
  ...
  mbarrier[2].arrive();
}
```

Every wait is paired: producer `mbarrier[2].wait(1)` against consumer `mbarrier[2].arrive()`, consumer `mbarrier[0].wait(0)` against producer `mbarrier[0].arrive_and_expect_tx`. No unsatisfiable wait remains at trip count 1.

I could not bisect to a fixing commit — installing 0.1.11 alongside for an A/B on this machine fails on an ABI clash between its `libtvm_compiler.so` and the installed torch (`undefined symbol: tvm::ffi::ReprPrint`), and pinning a matching torch was out of scope. So this is evidence that the symptom is gone on current main for sm_90, not proof of which change fixed it.

@xiaguan, since you hit it on sm_103 (GB300) with real code rather than a fuzzer, could you re-run your GEMV repro on 0.1.14? If it still deadlocks there, the remaining defect is Blackwell-specific and worth keeping open with that narrower scope.

