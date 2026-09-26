# [Issue #2729] [FA4/B200] return_lse=True makes D64 forward about 19% faster

source: https://github.com/Dao-AILab/flash-attention/issues/2729
state: open | updated: 2026-09-06T17:28:25Z
labels: 

## 正文

I had my agent create this reproducer while doing some heuristic tuning. This is quite strange, and I wanted to track it.

On B200, the FA4 CuTe forward kernel for dense BF16 attention with `(B, S, H, D) = (2, 16384, 16, 64)` is consistently faster when `return_lse=True`, even though that specialization calculates and writes the additional LSE output.


### Agent notes

## Environment

- GPU: NVIDIA B200 (SM100)
- PyTorch: `2.14.0.dev20260722+cu132`
- PyTorch CUDA runtime: 13.2
- NVIDIA CuTe DSL: `4.6.0.dev0`
- FlashAttention commit: `00756db9d921da0846453283ddfbeb7457abd09b`
- Dtype: BF16
- Causal: false
- Measurement: fixed-pointer CUDA graph replay, 25 warmups and 100 measured replays per round, five alternating A/B rounds

## Result

```text
GPU: NVIDIA B200
Torch: 2.14.0.dev20260722+cu132 (CUDA 13.2)
CuTe DSL: 4.6.0.dev0
FA4 commit: 00756db9d921da0846453283ddfbeb7457abd09b
no-LSE: median=3.0018 ms rounds=[3.007457275390625, 3.0017739868164064, 3.001456604003906, 3.0028912353515627, 3.0008636474609376]
with-LSE: median=2.5281 ms rounds=[2.5091484069824217, 2.545796203613281, 2.512978210449219, 2.5281126403808596, 2.532301177978516]
with-LSE speedup: 1.187x
```

Both paths pass a correctness check against PyTorch SDPA.

A focused Nsight Compute comparison showed the same launch topology and resource limits for both specializations (148 blocks, 512 threads, 128 registers/thread, and approximately 232 KB dynamic shared memory). The no-LSE specialization had substantially fewer eligible/issued warps and more samples around the pipeline synchronization path. This looks more like a compiler scheduling/code-generation cliff than an inherent benefit from calculating LSE.

I have only established this behavior on B200; this report does not claim the same result on GB300.

## Minimal reproducer

Run with:

```bash
python repro_fa4_lse_b200.py /path/to/flash-attention
```

```python
"""Reproduce the FA4 D64 B200 performance inversion caused by returning LSE."""

import argparse
import importlib
import importlib.metadata
import statistics
import subprocess
import sys
import time
from pathlib import Path
from types import ModuleType
from typing import Callable

import torch
import torch.nn.functional as F


def load_fa4_interface(fa4_root: Path) -> ModuleType:
    """Load the CuTe FA4 interface without requiring the FA2 extension."""
    package = ModuleType("flash_attn")
    package.__path__ = [str(fa4_root / "flash_attn")]
    sys.modules["flash_attn"] = package
    return importlib.import_module("flash_attn.cute.interface")


def make_call(
    interface: ModuleType,
    q: torch.Tensor,
    k: torch.Tensor,
    v: torch.Tensor,
    return_lse: bool,
) -> Callable[[], torch.Tensor]:
    """Create one allocation-free FA4 forward specialization."""
    out = torch.empty_like(q)
    lse = (
        torch.empty(q.shape[0], q.shape[2], q.shape[1], device=q.device)
        if return_lse
        else None
    )

    def run() -> torch.Tensor:
        return interface._flash_attn_fwd(
            q, k, v, out=out, lse=lse, return_lse=return_lse
        )[0]

    return run


def capture(function: Callable[[], torch.Tensor]) -> torch.cuda.CUDAGraph:
    """Capture a warmed FA4 call into a fixed-pointer CUDA graph."""
    stream = torch.cuda.Stream()
    stream.wait_stream(torch.cuda.current_stream())
    with torch.cuda.stream(stream):
        for _ in range(3):
            function()
    stream.synchronize()
    graph = torch.cuda.CUDAGraph()
    with torch.cuda.graph(graph, stream=stream):
        function()
    return graph


def warm_gpu(seconds: float = 1.0) -> None:
    """Warm the GPU long enough to avoid measuring initial idle clocks."""
    x = torch.randn(4096, 4096, device="cuda", dtype=torch.bfloat16)
    deadline = time.perf_counter() + seconds
    while time.perf_counter() < deadline:
        torch.mm(x, x)
    torch.cuda.synchronize()


def time_graph(graph: torch.cuda.CUDAGraph, iterations: int) -> float:
    """Return mean fixed-pointer graph replay latency in milliseconds."""
    for _ in range(25):
        graph.replay()
    start = torch.cuda.Event(enable_timing=True)
    end = torch.cuda.Event(enable_timing=True)
    start.record()
    for _ in range(iterations):
        graph.replay()
    end.record()
    end.synchronize()
    return start.elapsed_time(end) / iterations


def main() -> None:
    """Compile, validate, and compare no-LSE and with-LSE FA4 kernels."""
    parser = argparse.ArgumentParser()
    parser.add_argument("fa4_root", type=Path)
    parser.add_argument("--iterations", type=int, default=100)
    parser.add_argument("--rounds", type=int, default=5)
    args = parser.parse_args()

    torch.manual_seed(0)
    torch.cuda.manual_seed_all(0)
    interface = load_fa4_interface(args.fa4_root.resolve())
    shape = (2, 16384, 16, 64)
    q, k, v = (
        torch.randn(shape, device="cuda", dtype=torch.bfloat16) for _ in range(3)
    )
    no_lse = make_call(interface, q, k, v, False)
    with_lse = make_call(interface, q, k, v, True)

    expected = F.scaled_dot_product_attention(
        q.transpose(1, 2), k.transpose(1, 2), v.transpose(1, 2)
    ).transpose(1, 2)
    torch.testing.assert_close(no_lse().float(), expected.float(), atol=5e-2, rtol=2e-2)
    torch.testing.assert_close(
        with_lse().float(), expected.float(), atol=5e-2, rtol=2e-2
    )
    torch.cuda.synchronize()

    graphs = {"no-LSE": capture(no_lse), "with-LSE": capture(with_lse)}
    samples = {name: [] for name in graphs}
    warm_gpu()
    for round_index in range(args.rounds):
        order = tuple(graphs) if round_index % 2 == 0 else tuple(reversed(graphs))
        for name in order:
            samples[name].append(time_graph(graphs[name], args.iterations))

    commit = subprocess.check_output(
        ["git", "-C", str(args.fa4_root), "rev-parse", "HEAD"], text=True
    ).strip()
    medians = {name: statistics.median(values) for name, values in samples.items()}
    print(f"GPU: {torch.cuda.get_device_name()}")
    print(f"Torch: {torch.__version__} (CUDA {torch.version.cuda})")
    print(f"CuTe DSL: {importlib.metadata.version('nvidia-cutlass-dsl')}")
    print(f"FA4 commit: {commit}")
    for name, values in samples.items():
        print(f"{name}: median={medians[name]:.4f} ms rounds={values}")
    print(f"with-LSE speedup: {medians['no-LSE'] / medians['with-LSE']:.3f}x")


if __name__ == "__main__":
    main()
```

Expected behavior: omitting the extra LSE output should be at least as fast as returning it, absent a documented specialization tradeoff.


## 评论 (1)

### IaroslavElistratov · 2026-09-06

@drisspg 

As I understand, in March you guys tuned the register budgets on cutlass-dsl 4.4.2, then moved to newer DSL version (>= 4.5.2, now 4.6.2) and the budgets were not re-tuned for the new compiler. The new DSL emits about 1.1k extra register moves in the softmax role, so the same code no longer fits in 176 registers and spills, which costs about 25% on B200. The same source on 4.4.2 is spill free and gets 96-97% of paper, and on 4.6.2 a larger sofmax budget removes the spill.

––––––––

Agent notes:

FA4 on B200 runs well below the paper numbers when installed from pip, and it looks like a toolchain interaction rather than a kernel problem. Environment: B200 (sm_100a), CUDA 13.0.2, torch 2.9.1+cu130.

in March (b2176fd3, "[Fwd,Sm100] Tune ex2 frequency and registers") the hd128 non-causal 2-CTA entry got 176 registers for the softmax warps, tuned on cutlass-dsl 4.4.2, where it compiles spill-free (REG 128, STACK 0). Since beta16 the package requires cutlass-dsl >= 4.5.2, and today a plain install resolves to 4.6.2. On every newer DSL we tried (4.5.2, 4.6.2, 4.7.1, 4.8.0.dev0) the same source with the same budget compiles with a 112-byte stack frame, 55-73 spill sites, about 30 of them inside the exp2 loop of the softmax role. The output is bit-identical, so nothing in the tests catches it, and the CI benchmark job prints numbers without a threshold. With your own benchmark_attn.py (fwd, non-causal, hd128, 4k/8k/16k, cold GPU) we get 1180/1213/1236 TFLOPS as installed versus 1479/1528/1553 with the same beta29 source on DSL 4.4.2. That is 77% versus 96.5-97% of the paper.

What changed in the generated code: the arithmetic is identical (same counts of ex2, max, packed f32x2, cvt), but the newer DSL emits extra register-to-register moves. On 4.5.2 that is about 1,100 extra mov.b32, 849 of them in the softmax role; on 4.6.2 the pattern differs (about 320 extra mov.b64 pack/unpack pairs and a different lowering of the ex2 sites) with the same 112-byte frame. It is the DSL's PTX generator, not ptxas: recompiling the 4.6.2 PTX with other ptxas versions gives the same frame. And it is register pressure: the softmax role fits again at 184 registers on 4.6.2.

A one-line fix that works today: on 4.6.2 the old 192/80/48 split (softmax/correction/other) is spill-free and was the fastest of the spill-free splits we measured (beats 184/88/56 and 184/80/64 by 0.2-2.3%, outputs bit-identical). On 4.4.2 that split measured 3.4-4.3% behind the March tune, so it recovers most but probably not all of the loss; re-running tune_ex2_emu.py on the DSL the package pins would find the rest. A STACK == 0 check on the SM100 forward cubin in CI would catch this class of regression.

Reproducer: flash-attn-4==4.0.0b15 (the last beta that still allows 4.4.2) with nvidia-cutlass-dsl[cu13]==4.4.2 quack-kernels==0.4.1 versus nvidia-cutlass-dsl[cu13]==4.5.2, run _flash_attn_fwd once on randn (8, 4096, 16, 128) bf16 with CUTE_DSL_KEEP_CUBIN=1, then cuobjdump --dump-resource-usage on the cubins. Same result with beta29 installed without its dependency pin.

We suspect #2729 (return_lse making hd64 19% faster) is the same thing from the other side: the extra LSE code shifts the allocation enough that the role happens to fit again.
