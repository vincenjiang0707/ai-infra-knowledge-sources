# [Issue #3573] [BUG] CuTeDSL >= 4.6 cannot compile NCCL GIN device ops — ptxas rejects the generated PTX (4.5.2 works)

source: https://github.com/NVIDIA/cutlass/issues/3573
state: open | updated: 2026-09-02T06:14:10Z
labels: CuTe DSL

## 正文

### Summary

Compiling any NCCL **GIN remote operation** (`Gin.put` / `Gin.signal` from
`nccl4py`'s `nccl.core.device.cute`) with `nvidia-cutlass-dsl >= 4.6` fails in
`ptxas`. The same kernels compile successfully with `nvidia-cutlass-dsl == 4.5.2`.

Two distinct `ptxas` errors appear, and **which one you get is selected by the
NCCL device-bitcode version**, while **whether it fails at all is selected by the
CuTeDSL version**:

| nvidia-cutlass-dsl | nccl4py | nvidia-nccl-cu12 | result |
|---|---|---|---|
| 4.5.2 | 0.3.1 | 2.30.7 | **compiles** |
| 4.5.2 | 0.3.1 | 2.31.2 | fails — `Parsing error near '.nvvm'` |
| 4.7.1 | 0.4.1 | 2.30.7 | fails — `Modifier '.volatile' cannot be applied to '.local' space` |
| 4.7.1 | 0.4.1 | 2.31.2 | fails — `Parsing error near '.nvvm'` |

`Gin.wait_counter` / `Gin.wait_signal` / `Gin.read_signal` / `Gin.read_counter`
(the local-poll operations, which do not issue a network operation) compile fine
in **every** combination above. Only the operations that post a remote action fail.

### Defect 1 — unlowered `llvm.nvvm.activemask` leaks into the PTX (NCCL 2.31.2 bitcode)

```
ptxas application ptx input, line 47; fatal : Parsing error near '.nvvm': syntax error
ptxas fatal   : Ptx assembly aborted due to errors
```

The generated PTX contains:

```ptx
.extern .func  (.param .b32 func_retval0) llvm.nvvm.activemask
()
;
```

The `llvm.nvvm.activemask` intrinsic is emitted as an external function
declaration rather than being lowered to `activemask.b32`, and `ptxas` rejects
it because `.` is not legal in a PTX identifier. It is the only leaked intrinsic
in the module (7 references).

This one reproduces on **4.5.2 as well as 4.7.1**, so it looks independent of
the DSL version. Note CuTeDSL's own `cutlass.cute.arch.activemask` is implemented
as inline PTX asm rather than via this intrinsic, so the intrinsic may simply
have no lowering path in the LLVM→NVVM import.

### Defect 2 — `.volatile` applied to `.local` space (NCCL 2.30.7 bitcode)

```
ptxas application ptx input, line 479; error : Modifier '.volatile' cannot be applied to '.local' space
ptxas application ptx input, line 481; error : Modifier '.volatile' cannot be applied to '.local' space
ptxas fatal   : Ptx assembly aborted due to errors
```

This is the interesting one: **the identical bitcode compiles cleanly under
4.5.2 and fails under 4.6.3 / 4.7.1 / 4.8.0.dev0**, which makes it look like a
CuTeDSL codegen regression introduced in 4.6.

### Not architecture specific

Reproduced with `CUTE_DSL_ARCH` set to `sm_90a`, `sm_100a` and `sm_120a` — same
failures. The measurements above were taken on a Blackwell sm_120 (cc 12.0) part,
CUDA driver 580.x.

### Not specific to the `_v2` entry points

`nccl4py` 0.4.1 calls `ncclGinPut_v2` / `ncclGinSignal_v2`, while 0.3.1 calls the
v1 `ncclGinPut`. Declaring the v1 symbols by hand with
`@cute.extern(name="ncclGinPut", source=BitCode(...))` and calling those instead
produces the **same** error for a given NCCL version, so the entry point makes no
difference.

### Reproducer

Single rank, any CUDA GPU; nothing is transferred, both failures are at compile
time.

```bash
pip install 'nvidia-nccl-cu12==2.31.2' 'nccl4py[cu12]==0.4.1' \
            'nvidia-cutlass-dsl==4.7.1' 'cuda-python==12.9.7'

python nvidia_issue_repro.py --case control   # Gin.wait_counter -> COMPILED_OK
python nvidia_issue_repro.py --case v2        # Gin.put / Gin.signal -> fails
python nvidia_issue_repro.py --case v1        # hand-declared v1 externs -> fails
```

Then swap `nvidia-nccl-cu12==2.30.7` to see defect 2 instead of defect 1, and
`nvidia-cutlass-dsl==4.5.2` + `nccl4py[cu12]==0.3.1` for the combination that
works. (0.3.1 and >= 4.6 cannot be mixed: 0.3.1 imports
`cutlass.base_dsl._mlir_helpers.op`, which 4.6.0 removed, and 0.4.1 requires
`~= 4.6`.)

The three cases must be run in **separate processes** — declaring the case `v1`
externs in the same module changes which error the stock path reports.

<details>
<summary>nvidia_issue_repro.py</summary>

```python
#!/usr/bin/env python3
"""Minimal reproducer: CuTeDSL >= 4.6 cannot compile any NCCL GIN *remote*
operation, while local-poll operations compile fine.

Two independent defects, so the script runs ONE case per process -- declaring
the case B externs in the same module changes the failure reported for case A,
so they must not share a process:

    python nvidia_issue_repro.py --case control   # gin.wait_counter  -> OK
    python nvidia_issue_repro.py --case v2        # gin.put/signal    -> defect 1
    python nvidia_issue_repro.py --case v1        # v1 externs        -> defect 2

Dependencies are three public wheels, nothing else:

    pip install 'nvidia-nccl-cu12==2.30.7' 'nccl4py[cu12]==0.4.1' \
                'nvidia-cutlass-dsl==4.7.1' 'cuda-python==12.9.7'

A single rank on any CUDA GPU is enough; nothing is transferred, both failures
are at compile time.
"""
import argparse

import torch
import cutlass
import cutlass.cute as cute
import cutlass.torch as cutlass_torch
import cuda.bindings.driver as cuda

import nccl.core as nccl
import nccl.core.device.cute as nccl_cute
import nccl.core.interop.torch as nccl_torch
from nccl.core.device.cute._helpers import _to_ptr, _to_coop_value, _to_value
from nccl.core.device.cute._structs import _LLVMPtrType, ncclTeam, ncclCoopAny

SLOT = 1 << 20


def make_v1_externs():
    """Declared lazily: the mere presence of these stubs in the module changes
    which error the stock (_v2) path reports, so case A must never see them."""
    from nccl.core.device.cute._bindings import _BC

    # Same signatures as nccl4py 0.4.1's ncclGinPut_v2 / ncclGinSignal_v2 stubs
    # minus the trailing opt_flags parameter, i.e. the v1 C-ABI still exported
    # by libnccl_device.bc.
    @cute.extern(name="ncclGinPut", source=_BC)
    def put_v1(
        gin: _LLVMPtrType, team: ncclTeam, peer: cutlass.Int32,
        dst_win: _LLVMPtrType, dst_offset: cutlass.Int64,
        src_win: _LLVMPtrType, src_offset: cutlass.Int64,
        size: cutlass.Int64,
        is_signal: cutlass.Boolean, signal_id: cutlass.Int32,
        signal_op: cutlass.Int32, signal_op_arg: cutlass.Int64,
        is_counter: cutlass.Boolean, counter_id: cutlass.Int32,
        coop: ncclCoopAny,
        is_descriptor: cutlass.Boolean, descriptor_ptr: _LLVMPtrType,
        given_release: cutlass.Int32, required_release: cutlass.Int32,
    ) -> None: ...

    @cute.extern(name="ncclGinSignal", source=_BC)
    def signal_v1(
        gin: _LLVMPtrType, team: ncclTeam, peer: cutlass.Int32,
        is_signal: cutlass.Boolean, signal_id: cutlass.Int32,
        signal_op: cutlass.Int32, signal_op_arg: cutlass.Int64,
        coop: ncclCoopAny,
        is_descriptor: cutlass.Boolean, descriptor_ptr: _LLVMPtrType,
        given_release: cutlass.Int32, required_release: cutlass.Int32,
    ) -> None: ...

    return put_v1, signal_v1


def build(case, op):
    class K:
        @cute.jit
        def run(self, dev_comm, win, stream: cuda.CUstream):
            self.kern(dev_comm, win).launch(
                grid=[1, 1, 1], block=[128, 1, 1], stream=stream)

        @cute.kernel
        def kern(self, dev_comm, win):
            team = dev_comm.team_world
            coop = nccl_cute.cta()
            gin = dev_comm.gin(nccl_cute.GinBackendMask.PROXY, 0)
            st = win.tensor(cutlass.Int8, cute.make_layout(SLOT), 0)
            dt = win.tensor(cutlass.Int8, cute.make_layout(SLOT), cutlass.Int64(SLOT))

            if cutlass.const_expr(case == "control"):
                gin.wait_counter(coop, counter=0, least=1)

            elif cutlass.const_expr(case == "v2"):
                if cutlass.const_expr(op == "put"):
                    gin.put(team, 0, win, dt, win, st, coop,
                            is_signal=True, signal_id=0, signal_op=1,
                            signal_op_arg=1, is_counter=True, counter_id=0)
                else:
                    gin.signal(team, 0, True, 0, 1, 1, coop)

            else:  # v1 externs
                put_v1, signal_v1 = K._externs
                if cutlass.const_expr(op == "put"):
                    put_v1(gin.ptr, _to_value(team), cutlass.Int32(0),
                           win.ptr, cutlass.Int64(SLOT),
                           win.ptr, cutlass.Int64(0),
                           cutlass.Int64(SLOT),
                           cutlass.Boolean(True), cutlass.Int32(0),
                           cutlass.Int32(1), cutlass.Int64(1),
                           cutlass.Boolean(True), cutlass.Int32(0),
                           _to_coop_value(coop),
                           cutlass.Boolean(False), _to_ptr(0),
                           cutlass.Int32(0), cutlass.Int32(2))
                else:
                    signal_v1(gin.ptr, _to_value(team), cutlass.Int32(0),
                              cutlass.Boolean(True), cutlass.Int32(0),
                              cutlass.Int32(1), cutlass.Int64(1),
                              _to_coop_value(coop),
                              cutlass.Boolean(False), _to_ptr(0),
                              cutlass.Int32(0), cutlass.Int32(2))

    if case == "v1":
        K._externs = make_v1_externs()
    return K()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--case", default="control", choices=["control", "v2", "v1"])
    a = ap.parse_args()

    import importlib.metadata as md
    for p in ("nvidia-cutlass-dsl", "nccl4py", "nvidia-nccl-cu12", "cuda-python"):
        try:
            print(f"{p:22s} {md.version(p)}")
        except Exception:
            print(f"{p:22s} <not installed>")
    print(f"{'gpu':22s} {torch.cuda.get_device_name(0)}")
    print(f"{'case':22s} {a.case}\n")

    torch.cuda.set_device(0)
    dev = torch.device("cuda", 0)
    comm = nccl.Communicator.init(nranks=1, rank=0, unique_id=nccl.get_unique_id())
    reqs = nccl.NCCLDevCommRequirements(
        gin_connection_type=nccl.NcclGinConnectionType.FULL,
        gin_context_count=1, gin_signal_count=8, gin_counter_count=1)
    devcomm = comm.create_dev_comm(requirements=reqs)
    buf = nccl_torch.empty(SLOT * 2, dtype=torch.uint8, device=dev)
    win = comm.register_window(buf)
    stream = cutlass_torch.current_stream()

    ops = ["put"] if a.case == "control" else ["put", "signal"]
    for op in ops:
        label = "wait_counter" if a.case == "control" else f"{op} ({a.case})"
        try:
            cute.compile(build(a.case, op).run, devcomm, win, stream)
            print(f"{label:20s} COMPILED_OK")
        except BaseException as e:
            s = str(e)
            # the distinguishing line is inside the quoted ptxas log, not the
            # generic "ptxas rejected the PTX ..." wrapper
            hit = next((ln.strip() for ln in s.splitlines()
                        if "Parsing error near" in ln or "Modifier" in ln), None)
            print(f"{label:20s} FAILED: {hit or s.splitlines()[0][:120]}")


if __name__ == "__main__":
    main()
```

</details>

### Impact

`nvidia-cutlass-dsl` and `nccl4py` at their current released versions
(4.7.1 + 0.4.1, on either NCCL) cannot compile any GIN remote operation, so the
NCCL Device API is unusable from CuTeDSL unless one pins back to
`nvidia-cutlass-dsl == 4.5.2` + `nccl4py == 0.3.1` + `nvidia-nccl-cu12 == 2.30.7`.
That pin is not always available, since 4.5.x lacks other features — in our case
the `sm120_*` block-scaled helpers (`blockscaled_layout.sm120_make_smem_layout_sfa`,
`blackwell_helpers.partition_fragment_SFA`, `get_layoutSFA_TV`,
`sm120_get_smem_store_op`), so a process cannot use both GIN and an sm_120
block-scaled GEMM.

### Environment

```
nvidia-cutlass-dsl   4.5.2 / 4.6.3 / 4.7.1 / 4.8.0.dev0  (all tested)
nccl4py              0.3.1 / 0.4.1
nvidia-nccl-cu12     2.30.7 / 2.31.2
cuda-python          12.9.7
python               3.12
GPU                  Blackwell sm_120 (cc 12.0); also reproduced targeting
                     sm_90a / sm_100a via CUTE_DSL_ARCH
driver               580.x
```

## 评论 (2)

### jackyangNJ · 2026-09-02

Defect 1 (llvm.nvvm.activemask) is fixed in 4.8.  you can try 4.8 dev0. 
Defect 2, we're working on the fix for cu12. as the WAR, could you try cu13 package? 

### xiakun-lu · 2026-09-02

Defect 1 was introduced in NCCL 2.31.2 as `__activemask()` is called on the code path of GIN API when the EFA GDA backend is enabled. There are two workarounds, both need to re-build `libnccl_device.bc`. option 1: apply the inline ASM, see this [commit](https://github.com/NVIDIA/nccl/commit/60ffa5cdd047b517e1818e0d011e48a52fd43c7e). option 2: rebuild `libnccl_device.bc` with `NCCL_GIN_EFA_GDA_ENABLE=0` . 

The upcoming nccl 2.32 package will ship with inline ASM fix.

Defect 2 is a known issue, see [nccl4py 0.4.1 release note](https://github.com/NVIDIA/nccl/releases/tag/nccl4py-v0.4.1) . there is no workaround for cuda 12 , waiting fixes from cuteDSL.
