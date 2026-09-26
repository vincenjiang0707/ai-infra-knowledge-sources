# [Issue #3463] [BUG] v4.7.0 regression: bf16 tile stores scalarized to `st.global.b16` (was `st.global.v4.b32` in 4.5.3)

source: https://github.com/NVIDIA/cutlass/issues/3463
state: closed | updated: 2026-09-01T07:04:44Z
labels: bug, ? - Needs Triage, CuTe DSL

## 正文

### Which component has the problem?

CuTe DSL

### Bug Report

## Summary

A common epilogue store pattern: per-row `f32 -> bf16` conversion into rmem followed by `autovec_copy` 
to gmem fail to vectorize in cutlassv4.7.0/NVVM 23.0.0 bundle. 

Back in cutlass4.5.3/NVVM 23.0.0 both conversion & store are vectorized. 

| | 4.5.3 (CUDA 12.9 NVVM) | 4.7.0 (CUDA 13.3 NVVM) |
|---|---|---|
| conversion | `cvt.rn.bf16x2.f32` (paired) | `cvt.rn.bf16.f32` (per element) |
| store | **`st.global.v4.b32` x 8** | **`st.global.b16` x 64** |


## Impact
4-5x slow down in some memory bounded kernels. 

## Reproducer

Trivial reproducer kernel -- load a per-thread `[8, 8]` bf16 tile, multiply in f32, convert back
to bf16 row by row, `autovec_copy` the tile out — dumps the PTX, and prints
the `st.global.*`

```
$ uv run --with nvidia-cutlass-dsl==4.5.3 python nvvm_bf16_store_scalarization_repro.py
nvidia-cutlass-dsl 4.5.3
store histogram: {'st.global.v4.b32': 8}
PASS: bf16 tile stores vectorized

$ uv run --with nvidia-cutlass-dsl==4.7.0 python nvvm_bf16_store_scalarization_repro.py
nvidia-cutlass-dsl 4.7.0
store histogram: {'st.global.b16': 64}
FAIL: 64 scalar st.global.b16 stores (expected st.global.v4.b32)
```

```python
import os
import re
import sys
import tempfile

_DUMP_DIR = tempfile.mkdtemp(prefix="cute_ptx_")
# The DSL reads these at import time.
os.environ["CUTE_DSL_KEEP"] = "ptx"
os.environ["CUTE_DSL_DUMP_DIR"] = _DUMP_DIR

import cutlass  # noqa: E402
import cutlass.cute as cute  # noqa: E402
from cutlass import Float32  # noqa: E402

CHUNKS, ELTS, THREADS = 8, 8, 32  # per-thread bf16 tile: 8 rows x 8 elts (16B rows)
N = THREADS * ELTS


class Bf16TileStore:
    @cute.jit
    def __call__(self, mX, mY, stream):
        self.kernel(mX, mY).launch(grid=[1, 1, 1], block=[THREADS, 1, 1], stream=stream)

    @cute.kernel
    def kernel(self, mX: cute.Tensor, mY: cute.Tensor):
        tidx, _, _ = cute.arch.thread_idx()
        gX = cute.local_tile(mX, (CHUNKS, ELTS), (0, tidx))
        rX = cute.make_rmem_tensor_like(gX)
        cute.autovec_copy(gX, rX)
        # f32 math per row, then convert back to bf16 per row: the pattern
        # whose stores NVVM 13.3 fails to re-vectorize.
        acc = cute.make_rmem_tensor_like(rX, Float32)
        for c in cutlass.range_constexpr(CHUNKS):
            acc[c, None].store(rX[c, None].load().to(Float32) * 2.0)
        rY = cute.make_rmem_tensor_like(gX)
        for c in cutlass.range_constexpr(CHUNKS):
            rY[c, None].store(acc[c, None].load().to(mY.element_type))
        gY = cute.local_tile(mY, (CHUNKS, ELTS), (0, tidx))
        cute.autovec_copy(rY, gY)


def _fake_2d(n: int) -> cute.Tensor:
    m_sym = cute.sym_int64()
    stride = (cute.sym_int64(divisibility=n), 1)
    return cute.runtime.make_fake_tensor(
        cute.BFloat16, (m_sym, n), stride=stride, assumed_align=16
    )


def main() -> int:
    import importlib.metadata as im

    version = im.version("nvidia-cutlass-dsl")
    stream = cute.runtime.make_fake_stream(use_tvm_ffi_env_stream=True)
    cute.compile(Bf16TileStore(), _fake_2d(N), _fake_2d(N), stream, options="--enable-tvm-ffi")

    ptx_files = [f for f in os.listdir(_DUMP_DIR) if f.endswith(".ptx")]
    assert ptx_files, f"no PTX dumped to {_DUMP_DIR}"
    # The dump can contain stray non-UTF8 bytes; read permissively.
    with open(os.path.join(_DUMP_DIR, ptx_files[0]), encoding="latin-1") as f:
        ptx = f.read()
    stores = re.findall(r"st\.global[.a-z0-9]*", ptx)
    hist = {op: stores.count(op) for op in sorted(set(stores))}
    scalar = hist.get("st.global.b16", 0)

    print(f"nvidia-cutlass-dsl {version}")
    print(f"store histogram: {hist}")
    if scalar:
        print(f"FAIL: {scalar} scalar st.global.b16 stores (expected st.global.v4.b32)")
        return 1
    print("PASS: bf16 tile stores vectorized")
    return 0


if __name__ == "__main__":
    sys.exit(main())

```

Fake tensors declare 16 B pointer alignment and row-stride divisibility, so
provable alignment is not the issue (we also tested align=128 declarations —
no change). Both compiles use `options="--enable-tvm-ffi"`; target sm_103a.

## Environment

|                                | Before (PASS)                 | After (FAIL)                  |
|--------------------------------|-------------------------------|-------------------------------|
| `nvidia-cutlass-dsl`           | **4.5.3**                     | **4.7.0**                     |
| Embedded NVVM (from PTX header)| NVVM 20.0.0 (`Cuda compilation tools, release 12.9, V12.9.83`) | NVVM 23.0.0 (`Cuda compilation tools, release 13.3, V13.3.27`) |
| PTX `st.global` histogram      | `{'st.global.v4.b32': 8}`     | `{'st.global.b16': 64}`       |

Constant across both runs:

- GPU: NVIDIA GB300 (sm_103a)
- Driver: 580.126.20
- System CUDA toolkit: 13.2 (V13.2.51)
- PyTorch: 2.11.0+cu130
- OS / arch: Linux aarch64
- Python: 3.13

## 评论 (3)

### anakinxc · 2026-08-17

Thanks for reporting. @yiwangchunyu is taking a look on this one

### manishucsd · 2026-08-17

Please have MLIR LIT tests. 

### brandon-yujie-sun · 2026-08-30

@joydddd this is fixed in 4.6.3 and 4.7.1
