# MoonshotAI/minitriton

source: https://github.com/MoonshotAI/minitriton

<p align="center">
  <img src="assets/logo.svg" alt="MiniTriton" width="420">
</p>

MiniTriton is a teaching-grade but production-minded tile compiler. You
write kernels in a small Python-embedded tile DSL; they lower through
upstream [MLIR](https://mlir.llvm.org) dialects to PTX and run on NVIDIA GPUs. On top of that sits
an eager tensor library (eager execution and tile-level compilation, one
API). **All application kernels — [flash
attention](https://arxiv.org/abs/2205.14135), [KDA (Kimi Delta
Attention)](https://arxiv.org/abs/2510.26692), and friends — are
written in the DSL itself**; the compiler
contains only tile-level vocabulary primitives and general passes — no
application-specific intrinsics (the one expressibility exception is a
generic linear-algebra primitive, `tl.solve_tril`; see `Limitations`). Known gaps are documented in
`Limitations` below. The tile programming model deliberately follows
[Triton](https://github.com/openai/triton)'s — a familiar,
well-specified target to validate an agent-built compiler against;
upstream triton appears here only as a benchmark baseline.

> **Built by [Kimi K3](https://www.moonshot.cn) (Moonshot AI).** The
> whole stack — the DSL frontend, the MLIR compiler, CUDA kernels,
> autograd/nn, benchmarks, figures and documentation — was designed,
> implemented, measured and written by Moonshot AI's K3 model, with
> engineering direction and review by the maintainer.
>
> **Disclaimer: this is a demonstration of K3's capability on compiler
> design — not a Moonshot product, and not for production use.**

## Start here

- **Use the tensor library**: `examples/vecadd.py` → `examples/matmul.py`
  → `examples/train_gpt.py` — same API as the package
  (`minitriton.tensor` / `minitriton.nn` / `minitriton.autograd`)
- **Write a GPU kernel**: the tile DSL in `examples/vecadd.py`
  (`@tl.kernel`); the kernel corpus to learn from lives in
  `minitriton/device/cuda/kernels/` — pure DSL, no compiler intrinsics
- **See the numbers**: the figures below regenerate from
  `benchmarks/roofline/` (performance, incl. baselines) and
  `benchmarks/training/` (convergence & correctness evidence)
- **Hack the compiler**: `minitriton/frontend/` (DSL → AST) →
  `minitriton/compiler/` (builder → passes → lowering to PTX), with
  `tests/` as the executable specification

## Headline results

| CUDA-core roofline (fp32) | Tensor-core roofline (tf32/bf16) | train_gpt convergence (default fp32 path) |
|---|---|---|
| ![cuda-core](assets/roofline_cuda_core.png) | ![tensor-core](assets/roofline_tensor_core.png) | ![convergence](assets/train_gpt_convergence.png) |

How to read a roofline: the x-axis is arithmetic intensity (FLOPs per
DRAM byte), the y-axis is measured GFLOP/s. The solid line is the
measured limit, the dashed line is the
vendor spec sheet. Red is minitriton, blue is torch (eager or cuBLAS),
green is torch.compile, purple is triton. Implementations that share a
shape sit at the same point; the baseline series are drawn larger and
lighter, so an overlap shows as a faint halo around the red marker.
Points below the roofline's rivals are published too, on purpose. The
star marker is the full gpt50m train step measured end to end
(steady-state ms/step, identical accounting on every stack; gpt50m is
the benchmark's ~50M config, L10/D640/H10 — 49.4M at T128 to 50.0M at
T1024 via the positional table; the torch baseline uses
explicit-eager attention below block 512 and SDPA at block 512+) — read the red stars against the torch ones directly
(eager and compile; the fp32 panel shows eager only): that is the
current, honest state of the library, wins and losses alike. The third
figure trains the same small GPT in default fp32 on both stacks — the
curves overlap. It is an L20 measurement snapshot captured at
vocab=204 (the figure's own ln(vocab) annotation is self-consistent
with that); the train corpus is the source tree itself, so the runtime
vocab moves as the code changes — 103 at this writing, and the scripts
always use the runtime value.

## Quick start

Requirements: NVIDIA GPU (sm_89 verified; sm_80+ in principle), system
CUDA ≥ 12 (`ptxas`), Python ≥ 3.10. Toolchain via conda-forge:

```bash
conda create -p ./.conda-env -c conda-forge python=3.10 mlir=22.1.0 mlir-python-bindings=22.1.0 llvm-tools=22.1.0
./.conda-env/bin/pip install "cuda-python>=12,<13" numpy pytest pytest-xdist pytest-rerunfailures matplotlib   # torch/triton: benchmark baselines only; matplotlib: example loss plots
./.conda-env/bin/pip install torch==2.6.0   # benchmark baselines only (pulls triton==3.2.0)
PY=./.conda-env/bin/python

$PY examples/vecadd.py                  # DSL → MLIR → PTX → GPU end to end
$PY -m pytest tests/ -q                 # numpy/fp64 oracles only, no torch import
```

Or **install as a git package** (MLIR toolchain via the pip mlir-wheels index —
note the wheel is ~1.3 GB and the index tracks 22.x snapshots; the
conda-forge route above gives the exact 22.1.0 toolchain this repo was
verified with):

```bash
pip install "mlir>=22" -f https://github.com/makslevental/mlir-wheels/releases/expanded_assets/latest
pip install "cuda-python>=12,<13" numpy
pip install .            # from the repository checkout
python -c "import minitriton; print(minitriton.__version__)"
```

The pip package contains only the library; the examples and benchmarks
below assume a source checkout with the conda-route `$PY` defined above.

## Examples and usage guide

Everyday tasks, one command each (torch/triton are comparison baselines
only, never runtime dependencies):

```bash
# 1. write a kernel: @tl.kernel DSL → MLIR → PTX (examples/vecadd.py, matmul.py)
$PY examples/vecadd.py

# 2. fuse eager code: @tl.compile + the fusion rule engine (R1-R4/R8 + R2'/R2V)
$PY -m pytest tests/test_fusion.py -q          # 20+ runnable fusion examples

# 3. train a model end to end (corpus = the repo's own source, zero external data)
CUDA_VISIBLE_DEVICES=0 $PY examples/train_gpt.py --steps 200   # ~85M char-GPT (12L/12H/768 default)

# 4. mixed precision: bf16 training path
#    (bf16 params + fp32 master weights + dynamic loss scaling, CUDA-graphed step)
$PY benchmarks/training/train_gpt_precision_bench.py --steps 60 --impls tl_bf16_graph

# 5. streams: overlap independent kernels on side streams (opt-in)
MT_STREAM_OVERLAP=1 $PY benchmarks/training/train_gpt_precision_bench.py --steps 60 --impls tl_bf16

# 6. benchmarks + CI gate (core suite vs torch eager and torch.compile)
CUDA_VISIBLE_DEVICES=0 $PY benchmarks/roofline/ce_report.py
CUDA_VISIBLE_DEVICES=0 $PY benchmarks/roofline/ci_report.py   # rc=0 means PASS

# 7. scheduling helpers: canonical pipeline skeletons and composed
#    row-op reference forms live in minitriton/sched/ (import and reuse)
```

Distributed ([NCCL](https://github.com/NVIDIA/nccl) data-parallel, gradients all-reduced once per step):

```bash
CUDA_VISIBLE_DEVICES=0,1 $PY examples/train_gpt.py --ddp --steps 120 --loss-csv /tmp/ddp.csv
```

![single GPU vs 2-GPU DDP loss curves — near-identical (per-step diff annotated in the figure; benchmarks/training/plot_ddp_overlay.py)](assets/train_gpt_ddp_overlay.png)

Graphics / physics (`minitriton.viz`, window or headless PNG frames):

```bash
$PY examples/rigid_demo.py --steps 240 --frames /tmp/rigid_frames   # rigid-body particles
$PY examples/sph_demo.py   --steps 240 --frames /tmp/sph_frames     # SPH fluid
$PY examples/mpm_demo.py   --stats 50                               # MPM continuum (console stats)
```

<video src="assets/gallery_water.mp4" poster="assets/gallery_water.png" controls muted loop width="720"></video>

*SPH dam-break, 50k particles: field-sampled water (navy background,
cyan surface, white compressed foam), 480 steps @ 48 fps; regenerate
with `examples/render_gallery.py` (extra deps: `pip install pillow`
plus a system `ffmpeg`).
[Static contact sheet](assets/gallery_water.png) ·
[PDF](assets/gallery_water.pdf) for print.*

## Limitations

- **Hardware**: verified on NVIDIA L20 (sm_89) only; sm_80+ in principle
  but untested; no AMD/ROCm; the CPU backend is a numpy *oracle* for
  tests, not a usable runtime.
- **Dtypes**: fp32 and bf16 are first-class, tf32 is opt-in; fp16 works
  for elementwise, cast and norm/CE paths (16-bit norms compute in f32
  internally and cast back on store); fp16 matmul runs through f32
  compute with a cast back (numerically correct — there is no fp16
  tensor-core path); no fp8/quantized paths. The default path is not
  bit-identical to torch (different reduction order, `ex2.approx`).
- **Operator coverage**: the op set is what the benchmarks and examples
  exercise — not a torch replacement (no conv/pool/recurrent ops; most
  ops assume contiguous inputs; new shape/stride keys trigger a fresh
  compile + autotune pass). `@tl.compile` fuses forward-only: gradients
  do not flow through a compiled graph (backward on its output raises —
  compute the loss/backward outside it, unlike torch.compile). The
  layer_norm/rms_norm/softmax row kernels (forward and backward) cap
  the reduced row width at C ≤ 8192 and raise `NotImplementedError`
  above it; cross_entropy covers wider rows through its split route.
  KDA is forward-only (no tape — backward is not implemented), and
  in-place indexed assignment (`t[i] = v`) raises `NotImplementedError`.
- **Autograd**: the tape is single-use — `backward()` frees it and a
  second backward through the same graph raises (there is no
  `retain_graph`); with several losses, sum them first and backprop
  the sum (`(l1 + l2).backward()`). There is no version counter on
  in-place writes: mutating a non-requiring-grad tensor in place
  (`x += d`) after the graph saved it but before `backward()` yields
  silently wrong gradients, where torch raises (in-place writes on
  requiring-grad tensors are rejected).
- **Performance ceilings are documented, not hidden**: some kernel
  families sit below torch/cuBLAS (see the rooflines; the evidence
  regenerates with the scripts in `benchmarks/roofline/`). Cold-start
  compilation is serial per
  process (the test gate parallelizes at process level with
  pytest-xdist).
- **Distributed**: NCCL data-parallel only, tested at 2 GPUs
  single-node. `sparse/` and `distributed/` are the youngest packages.
- **Recorded non-fixes** (evaluated and deliberately left as-is):
  `sparse.spmm_csr`/`segment_reduce` indices are not range-checked
  (the embedding-family ops above are); `gather`/`scatter_add` inside
  `@tl.compile` fails with a bare `AttributeError` (no trace nodes);
  `tl.pipelined` on an empty trip count still stages one tile;
  `file://` rendezvous files are not cleaned up on reuse; `_dep`
  overlap loops with `iv > 0` get no automatic sync; one_bar /
  one_shot mma schedules have a theoretical tail-barrier race window
  (never reproduced); `viz.mesh` edge indices and
  `sparse.coo_sort_by_key`'s i64→i32 truncation are unchecked (caller
  contract).
- **Ecosystem & maturity**: torch-*like* API, not torch-*compatible*;
  no HuggingFace/ONNX bridges. Teaching-grade but measurement-honest —
  every claim has a re-runnable script; known gaps are listed in this
  section.
- **Compiler vocabulary exceptions**: `tl.solve_tril` (a batched
  triangular solve, used by KDA's factor kernel) is implemented in the
  compiler rather than the DSL — a warp-role-specialized row solve that
  does not express well in the tile vocabulary. It is a generic
  linear-algebra primitive, not an application kernel; everything
  application-level (flash attention, KDA) is pure DSL.
- **Input validation is deliberately thin**: embedding, cross-entropy,
  gather and scatter_add indices ARE bounds-checked at the op entry
  (`IndexError`); each guarded call pays two device reduces plus host
  syncs (safety over speed, a teaching-grade trade-off). Inside
  `@tl.compile` the check is skipped — a traced graph caches by shape
  and cannot replay data-dependent asserts. Beyond those,
  validation stays thin — tensor-tensor
  `pow` with a negative base returns NaN (integer scalar exponents like
  `x ** 3` work).
- **Single tensors are limited to 2³¹ − 1 elements**: kernel address
  arithmetic is i32, so the elementwise/matmul/attention entry points
  reject larger tensors loudly — including small strided views whose
  reachable address range crosses the limit; the norm/misc/cross-entropy
  row kernels row-chunk bigger inputs and keep working. A few entry points
  (`l2norm_rows`, `adamw_step`, gather/sparse) are not yet guarded, and
  a matmul/bmm whose *output* crosses the limit surfaces a misleading
  `autotune: no valid config` — split the tensor instead.
- **No middle-layer optimizer**: the DSL lowers to *hand-scheduled* MLIR
  (pipelining, smem swizzles, ldmatrix/mma orchestration and 23 inline
  PTX hotspots in `compiler/builder.py` and `passes.py`), with only
  three small general W-IR passes on
  top. This is a teaching-grade hand-scheduled tile DSL, not an
  optimizing compiler — a new kernel family costs a few hundred lines of
  hand-written schedule code, not a new pass.

## Repository layout

```
├── minitriton/          # the package
│   ├── frontend/        # @tl.kernel AST frontend (types/code_generator/semantics)
│   ├── compiler/        # builder (tile→MLIR) layout (layout algebra)
│   │                    #   wir/passes (general passes) lowering (→PTX→cubin)
│   ├── fusion.py        # graph-level fusion rule engine (registry + arbitration)
│   ├── compile.py       # @tl.compile (trace + executor)
│   ├── sched/           # scheduling choreography skeletons + row-op reference forms
│   ├── runtime/         # cuda_driver / buffer / cache / autotune / allocator / streams
│   ├── device/
│   │   ├── cuda/        # ops.py (routing shells) elementwise.py (generator + expr vocab)
│   │   │   └── kernels/ # the single kernel library (matmul/attention/norm/ce/misc/kda, pure DSL)
│   │   └── cpu/         # numpy oracle
│   ├── ops/             # eager op shared semantics (broadcast/promotion/dispatch)
│   ├── nn/  autograd/  distributed/  sparse/  precision.py (precision switches)
├── examples/            # vecadd → matmul → train_gpt (~85M char-GPT, self-contained corpus)
├── benchmarks/
│   ├── roofline/        # all performance measurement: kernel reports (matmul/
│   │                    #   attention/kda/ce/rowfam), dual rooflines + solve_tril,
│   │                    #   ci_report.py (CI performance gate)
│   └── training/        # convergence figures, precision bench, DDP, grad check
├── tests/               # pytest (numpy/fp64 oracles; no torch imports)
├── assets/              # logos + tracked figures/media
└── build/               # compile intermediates (gitignored, local debugging)
```

## Engineering rules

- **Every performance comparison ships with a figure + baseline
  implementation** (torch eager / torch.compile / triton, same
  methodology; the CSV data behind each figure is regenerated by the
  script, not committed); figures go through the
  `benchmarks/roofline/plot_style.py`
  style family ((dark, light) × (png, svg, pdf); light PDFs for print/LaTeX)
- Negative results and unmet targets are recorded in `Limitations`,
  not hidden
- DSL first: application kernels are written in the Python DSL and lowered
  through the generic pipeline; compiler intrinsics are limited to the
  tile-vocabulary set (general primitives like load/store/dot/mma/reduce),
  case-by-case justified expressibility exceptions, and explicit
  scheduling constructs; application-level kernels never enter the
  compiler
- Every kernel has a numpy/fp64 oracle test;
  `benchmarks/training/grad_check.py` (vs torch autograd, atol 1e-4) must
  not regress

