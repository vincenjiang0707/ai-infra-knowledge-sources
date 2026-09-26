# [Issue #2011] Offer to help improve the MPS backend fallbacks

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/2011
state: open | updated: 2026-09-23T21:39:55Z
labels: 

## 正文

I'd like to help push the MPS backend off the 🐢 status in the README, and I'm set up to work on it directly (Apple Silicon, can build and test locally). I've contributed on the MPS side before (#1994) and on optimizers (#1998), so I'm somewhat familiar with the layout.

From reading the current backend (#1983, #2004), my understanding of the design is: try the `kernels-community/bitsandbytes-mps` Hub kernels when available, and fall back to pure PyTorch otherwise, with those fallbacks being what the 🐢 reflects. I don't want to cut across your in-flight work, so rather than guess, I wanted to ask where contributions would be most useful.

A few directions I could take on, if any are helpful:
- Profiling and speeding up specific PyTorch fallbacks in `backends/mps/ops.py`, in the spirit of #1960.
- Filling in MPS-specific fallbacks for ops that currently only hit the generic slow path.
- Extending MPS test coverage and correctness for the fallback paths.

If the 8-bit optimizer path (the 🚧) is something you'd want help with, I'm glad to look at that too, though I'd want to check it fits your plans first. Let me know what would be most useful, or if you'd rather I stay in the smaller correctness and coverage lane for now.


## 评论 (5)

### matthewdouglas · 2026-07-17

Hi @egeozkoc,

Thanks for asking!

The README's 🐢 is a little out of date. With the newer Hub kernels the 4bit quantize/dequantize/gemv ops are in a much better place. I plan to release what we have in v0.50.0 very soon, so will likely be updating this in the README even if best performance needs macOS 26 + `kernels`.

I do have a plan already for the optimizers, which will be part of a future v0.51.0 release. I would ask for now that you hold off on that. Correctness is going to come first, then further perf if needed. I'll be implementing it similar to the CPU backend, which will rely on the separate `quantize_blockwise`, `dequantize_blockwise` ops, and do the rest in PyTorch. I think this will be good enough to start before jumping further to e.g. a fully fused kernel like we have on the CUDA side.

I did spend some time benchmarking as part of #1960 and #1983. But if you want to share any benchmarks, profile data, etc, then that could be useful. Especially if you've got different hardware than I do (M4, 10-core). 

One obvious area that underperforms is the LLM.int8() ops. It's not exactly a priority, but there's opportunity there I'm sure. Another op that I know has room for improvement is `quantize_blockwise`.

I have not quite figured out exactly how I want to bring additional Metal kernels to the project in the future. I'm leaning on using `torch.mps.compile_shader` for this and doing JIT. But I want to avoid doing things like linking to libtorch without a stable ABI (makes build/dist more complex) or taking performance hits from not being able to access PyTorch's command buffer. The `compile_shader` approach avoids all of that. The other direction of course is to publish to the Hub separately, but right now it's kind of a stop-gap; we don't actually participate in maintaining anything in kernels-community at the moment.

With that said, if there's correctness fixes or similar well-isolated improvements to make, I'd be welcoming of that.


### egeozkoc · 2026-09-03

Thanks for the detailed reply, and apologies for the silence, I was away for a month. Understood on the 8-bit optimizers, I'll stay out of that.

I took your `compile_shader` lean and the `quantize_blockwise` note as the starting point and have some numbers from an M5 (10-core GPU, macOS 26, torch 2.12.1, no `kernels` package installed so this is purely the fallback path). Input is a 4096x4096 fp32 tensor, blocksize 256, dynamic map, 20 timed iterations after warmup with `torch.mps.synchronize()`.

| `quantize_blockwise` variant | time |
|---|---|
| current MPS fallback (binary search over bounds) | 6.9 ms |
| same, with `torch.compile` | 6.9 ms |
| `torch.bucketize` (default backend path) | 2488 ms |
| `torch.searchsorted` | 2283 ms |
| fused Metal kernel via `torch.mps.compile_shader` | 1.6 ms |

Two takeaways from that:

1. The binary search you have now is already the best pure-PyTorch option on this torch version; `bucketize`/`searchsorted` on MPS are unusable at this size, and `torch.compile` gives nothing. The one cheap win inside the existing fallback is the absmax reduction: `A_com.abs().max(dim=-1)` is 3.4 ms of the 6.9 ms, while `torch.aminmax(A_com, dim=-1)` followed by `maximum(max, -min)` is 1.1 ms for the same result. That alone takes the fallback to roughly 4.7 ms with no design implications, so I'd like to open that as a small PR regardless of what you decide on the next point.

2. The Metal kernel is a single `compile_shader` source, no libtorch linkage, no build changes. One threadgroup of 256 threads per block: `simd_max` reduction for the block absmax, then each thread scales its elements and does the same binary search over `(code[i] + code[i+1]) / 2` bounds that the fallback does, so it reproduces `bucketize` semantics exactly. On the 4096x4096 input the output bytes and absmax match the current fallback bit for bit. The shader is compiled once and cached at module level, so the JIT cost is paid on first call only. I've only run it at blocksize 256 so far; other blocksizes need a small loop change and I would guard the whole thing on `hasattr(torch.mps, "compile_shader")` so torch 2.4 through 2.6 keep the current fallback.

If you're open to it, I'd propose this as the first `compile_shader` kernel in `backends/mps/ops.py`, kept behind the same "try kernel, else fallback" shape you already use for the Hub kernels, and with the fallback path left intact. Since you mentioned you hadn't settled how you want to bring Metal kernels into the project, I'd rather hear how you want it structured (separate module for shader sources, blocksize coverage, dtype coverage) before opening the PR. Happy to just share the prototype as a gist if that's more useful for deciding.

Separately, while running the suite on MPS I hit one small correctness item outside the optimizer work you're reserving: every `paged_*` optimizer crashes on MPS with "Method 'cget_managed_ptr' not available in CPU-only version", because `get_state_buffer` only falls back to non-paged for `device.type == "cpu"`. Extending that guard to any non-CUDA device (same warning, same fallback) and skipping the paged tests on non-CUDA devices seems well-isolated. Shall I file it, or just open the PR?


### egeozkoc · 2026-09-03

Correction to my comment above, on the `aminmax` point (item 1): I'm withdrawing that. I had timed the absmax reduction in eager mode, but `_quantize_blockwise_compute` is already wrapped in `_try_torch_compile`, and on this setup the compile succeeds and inductor fuses the abs and the max. Measured end to end through `torch.ops.bitsandbytes.quantize_blockwise`, the `aminmax` version is 7.1 ms vs 6.9 ms for the current code, so it's a no-op and I won't open that PR. For reference, the eager path is ~80 ms on the same input (the binary search dominates), so the existing compile wrapper is doing most of the work.

The rest of the table stands: the Metal `compile_shader` kernel at 1.6 ms was compared against the compiled fallback, and `bucketize` is 2.3 s eager or compiled. Sorry for the noise.


### egeozkoc · 2026-09-04

I went ahead and built the `compile_shader` kernel for `quantize_blockwise` as a prototype so the discussion has something concrete behind it. It's on a branch, not a PR, since you said you hadn't settled how you want Metal kernels brought in: [egeozkoc/bitsandbytes@feature/mps-metal-quantize-blockwise](https://github.com/egeozkoc/bitsandbytes/tree/feature/mps-metal-quantize-blockwise).

One threadgroup per block, simdgroup reduction for the block absmax, then the same binary search over code midpoints the current fallback does. Measured on an M5 (10-core GPU, macOS 26, torch 2.12.1), against current `main`, times per call:

| dtype | shape | blocksize | main | kernel | |
|---|---|---|---|---|---|
| fp32 | 4096² | 64 | 7.63 ms | 1.98 ms | 3.9x |
| fp32 | 4096² | 256 | 6.94 ms | 1.66 ms | 4.2x |
| fp32 | 4096² | 4096 | 5.59 ms | 1.16 ms | 4.8x |
| fp32 | 1024² | 256 | 0.41 ms | 0.13 ms | 3.2x |
| fp16 | 4096² | 256 | 7.67 ms | 2.39 ms | 3.2x |
| fp16 | 4096² | 4096 | 6.31 ms | 1.91 ms | 3.3x |
| fp16 | 1024² | 256 | 0.40 ms | 0.14 ms | 2.9x |

Shader compilation is lazy and cached; it adds ~2.5 ms to the first call in a process and nothing after.

Correctness: bit-exact against the existing fallback across blocksizes 16/32/64/128/256/512/1024/4096 and sizes that exercise partial trailing blocks (48/48 configurations), plus constant, all-zero, subnormal, and large-outlier blocks. `test_ops.py` and `test_functional.py` pass with `BNB_TEST_DEVICE=mps` (1807 passed). The fallback is kept and used whenever `compile_shader` is missing (torch < 2.7) or compilation throws, so nothing regresses on older torch.

Two things worth flagging:

- There is one intentional difference. For an all-zero *partial trailing* block the current MPS fallback stores `absmax = 1e-38`, because it clamps before storing in the remainder branch, while full blocks store the unclamped value. The kernel stores `0.0`, which is what the CPU backend does for the same input. Dequantized output is identical either way, but the stored statistic differs, so I wanted it on the record rather than buried.
- Unrelated but might save someone time: `torch.equal` on MPS returned `True` for float32 tensors differing by a subnormal (`[0.0, 0.0]` vs `[0.0, 9.999999e-39]`) on torch 2.12.1. My first correctness sweep passed for that reason and was meaningless. Comparing on CPU, ideally through an int32 view, is what I ended up doing.

I've deliberately not opened a PR. The open question is still how you want this structured: I put the shader source in a separate `backends/mps/shaders.py` with a lazily compiled, process-cached library, but if you'd rather have the source inline in `ops.py`, or a different caching or fallback policy, or want it to cover `quantize_4bit` and `dequantize_blockwise` in the same pass, say which and I'll reshape it. Equally happy to leave it as a reference branch if you'd rather do this yourself when you get to it.


### natsu-git-hub · 2026-09-23

Hi @matthewdouglas and @egeozkoc, is this still open? I want to pick it up as i have some time free on my hands.
