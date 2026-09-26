# [Issue #2625] [BUG][Fuzzer][wrong-code] `T.rng_init()` default `seq` is x-dim-only, silently giving y/z-differing threads one RNG stream

source: https://github.com/tile-ai/tilelang/issues/2625
state: open | updated: 2026-09-17T10:13:50Z
labels: 

## 正文

### Required prerequisites

- [x] I have read the documentation <https://tilelang.com>.
- [x] I have searched the [Issue Tracker](https://github.com/tile-ai/tilelang/issues) that this hasn't already been reported. (comment there if it has.)

### What version of TileLang are you using?

0.1.11 (source at `cd37ed5fc35ae7a60a1277c8eb49028174ac51e6`).

### System information

Reproduced on NVIDIA L40S (sm_89), CUDA 13.0, PyTorch 2.11.0, tilelang 0.1.11 (dev wheel, byte-identical to the source tag above). The defect is in the arch-independent Python frontend id-computation (the codegen simply forwards `seq` to `curand_init` on every CUDA target), so it is expected on all arches; I tested sm_89.

### Problem description

`T.rng_init(seed, seq=None, off=0)` initializes a per-thread curand stream for "parallel random number generation". When `seq` is omitted (the default), the per-thread sequence number is auto-derived from **only the x dimension** of the thread and block indices:

```python
# tilelang/language/random.py  (the `seq is None` branch)
if seq is None:
    bx = T.get_block_binding()          # blockIdx.x only  (dim=0)
    ex = T.kernel.get_thread_extent()   # blockDim.x only  (dim=0)
    tx = T.get_thread_binding()         # threadIdx.x only (dim=0)
    id = tx + bx * ex
    seq = tirx.convert(id)
```

`seq` is passed straight through to `curand_init(seed, seq, offset, &state)` — it is the subsequence key that decorrelates parallel streams. Because `threadIdx.y`, `threadIdx.z`, `blockIdx.y`, and `blockIdx.z` are all dropped from `id`, any two threads that differ **only** in one of those dimensions receive the **same `seq`** and therefore the **same random stream**. The kernel compiles and runs with no diagnostic; the outputs are silently identical. This bites any kernel that uses a 2-D/3-D thread block (`threads=(x,y[,z])`) or a multi-dimensional grid with the default `seq`.

### Reproducible example code

```python
import torch, tilelang, tilelang.language as T
tilelang.disable_cache()

def build(explicit_seq):
    @tilelang.jit
    def kf():
        @T.prim_func
        def main(Out: T.Tensor((2, 2), "int32")):     # int32 buffer; uint32 is not torch-feedable
            with T.Kernel(1, threads=(2, 2)):
                tx = T.get_thread_binding(0); ty = T.get_thread_binding(1)
                if explicit_seq:
                    T.rng_init(seed=1234, seq=tx * 2 + ty)   # CONTROL: unique per (tx,ty)
                else:
                    T.rng_init(seed=1234)                    # seq=None default (drops threadIdx.y)
                Out[tx, ty] = T.reinterpret(T.rng_rand(), dtype="int32")
        return main
    return kf()

for label, ex in [("default seq=None", False), ("explicit seq (control)", True)]:
    out = torch.zeros((2, 2), device="cuda", dtype=torch.int32); build(ex)(out)
    a = out.cpu().numpy()
    print(f"{label}: distinct={len(set(a.flatten().tolist()))}/4  Out[tx,0]==Out[tx,1]: "
          f"{bool(a[0,0]==a[0,1])},{bool(a[1,0]==a[1,1])}\n{a}")
# default seq=None      : distinct=2/4  Out[tx,0]==Out[tx,1]: True,True   <-- threadIdx.y dropped
# explicit seq (control): distinct=4/4  Out[tx,0]==Out[tx,1]: False,False
```

Same collision with a 2-D grid `T.Kernel(2, 2, threads=1)` (drops `blockIdx.y`): `Out[bx,0] == Out[bx,1]`.

### Traceback

No traceback — the kernel compiles and runs to completion. The random outputs are silently identical across the dropped dimensions.

### Expected behavior

With the default `seq`, distinct threads/blocks should get distinct curand streams — that is the purpose of the `seq` argument (see the [curand device API](https://docs.nvidia.com/cuda/curand/device-api-overview.html#device-api-overview), cited in the source itself). The control (a `seq` folding in all thread/block dimensions) gives four distinct values, which is the correct output the default should also produce.

### Additional context

**Root cause.** The default sequence-id derivation collapses the thread/block index to its x component only, so it is not unique across a multi-dimensional launch and hands colliding `seq` values to `curand_init`. Concretely, [`tilelang/language/random.py` L28–L33](https://github.com/tile-ai/tilelang/blob/cd37ed5fc35ae7a60a1277c8eb49028174ac51e6/tilelang/language/random.py#L28-L33) builds `id` from only the x components of the bindings (`get_thread_binding()`/`get_block_binding()`/`get_thread_extent()` all default to `dim=0`), dropping `threadIdx.y/z` and `blockIdx.y/z`. That `seq` is forwarded to `curand_init` as arg[1] at [`src/cuda/codegen/codegen_cuda.cc` L4298](https://github.com/tile-ai/tilelang/blob/cd37ed5fc35ae7a60a1277c8eb49028174ac51e6/src/cuda/codegen/codegen_cuda.cc#L4298).

**Suggested fix.** Fold in the remaining dimensions — a row-major flatten over `get_thread_bindings()` / `get_block_bindings()` weighted by the corresponding extents — so the default id is unique across the full launch grid. (Minimally: document that the default `seq` is x-dimension-only and require an explicit `seq` for multi-dimensional launches — but silent correlation is a poor default for an RNG.)

**Provenance.** Added in PR [#1582](https://github.com/tile-ai/tilelang/pull/1582) ("Add more curand operations"); current form last touched by `b939fa01` (#2216, tirx rename). The x-only derivation has been present since the feature landed — not a regression.

**Dedup.** Searched the open and closed tracker (`rng_init`, `curand`, `rng_rand`, `sequence`) and FILED_ISSUES.md — no existing report.

The `seq is None` default branch appears to have no test coverage — the tests/examples pass an explicit `seq`, so the x-only default is never exercised against a multi-dimensional launch.


## 评论 (2)

### 0z5a · 2026-09-17

I would like to take this. ^^

### 0z5a · 2026-09-17

I'd like to take this together with #2625, #3029 and #3034 as one focused CUDA RNG hardening PR.

Planned scope:

1. make the `rng_init` API contract consistent with its actual hidden-state implementation,
2. reject `rng_rand` / `rng_rand_float` cleanly when no `rng_init` exists in the function,
3. make `rng_init(seq=None)` derive a unique default sequence across all launch dimensions,
4. add regression coverage for all three cases.

I'll keep the patch limited to the RNG frontend/codegen/tests. If you would prefer #2625 to be split from the state-lifecycle/API fixes, I can separate it.

The patch is up as #3239 (Fixes #2625, #3029, #3034). The PR description has the baseline-vs-patched reproducer output, an end-to-end stream-quality measurement (16/256 distinct per-thread streams before, 256/256 after), and the test results (8 failed/13 passed on baseline, 21 passed with the patch).

---

For #3029 specifically: my current interpretation is to preserve TileLang's existing hidden RNG-state model and make `rng_init` explicitly side-effect-only, rather than introducing a new public state-handle API. `rng_rand` / `rng_rand_float` do not consume an explicit handle today. If an explicit state handle is the intended API direction, please let me know before I lock this in.

