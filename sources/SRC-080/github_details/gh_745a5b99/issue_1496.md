# [Issue #1496] Use torch.compile to speed up GPTQ algorithm

source: https://github.com/vllm-project/llm-compressor/issues/1496
state: closed | updated: 2026-09-14T19:04:52Z
labels: enhancement, good first issue, keep-open

## 正文

The bulk of the runtime associated with the GPTQ algorithm is implemented in this helpers file [src/llmcompressor/modifiers/quantization/gptq/gptq_quantize.py](https://github.com/vllm-project/llm-compressor/blob/main/src/llmcompressor/modifiers/quantization/gptq/gptq_quantize.py)

Maybe there are some opportunities to compile portions of this code?

Please include some runtime benchmarks to validate the changes

## 评论 (7)

### dsikka · 2025-06-01

@ved1beta 

### colldata79 · 2026-01-22

 can i look at this ? 

@ved1beta  is this back to active or can i pick this up?

### kylesayrs · 2026-01-24

@colldata79 Please see #1561 thread

Getting torch compile to work consistently across all users has been difficult. If you have an interest/experience with torch.compile, I can assign this ticket to you!

### colldata79 · 2026-01-24

yes please assign it to me 

### colldata79 · 2026-01-26

@kylesayrs  i have a couple of quick questions before i jump onto this week

“What performance bar makes this worth merging? (e.g., ≥1.3× on A100? measured on which model sizes?)”
“What correctness bar? (bitwise match, or ‘no meaningful perplexity regression’?)”
“Which CI/tests should cover it—unit tests only, or an E2E perf test?”

and please can you or @dsikka  please assign this to me 

### HDCharles · 2026-01-29

good questions:

we landed an [AWQ PR](https://github.com/vllm-project/llm-compressor/pull/2265) for performance improvements and that may be a good idea to compare with

The speedups were relatively small, though consistently better than before across architectures and settings. If some models do better and others worse, it'll likely require a larger average speedup to land.

I would look at examples like https://github.com/vllm-project/llm-compressor/blob/main/examples/quantization_w4a16/llama3_example.py and https://github.com/vllm-project/llm-compressor/blob/main/examples/quantizing_moe/qwen_example.py and do similar tests, you can see how i modified them in https://github.com/vllm-project/llm-compressor/pull/2265/changes/d1347840586ccbe6cb9b017cfbb719937136e542

As far as correctness i think I would probably compare compiled and uncompiled outputs, though if e2e to easier then that seems fine too.

other notes: I tried using torch.compile for the AWQ speedup and ran into issues with device on/offloading so watch out for that.
I'd also mention that compile can have a lot of overhead and it may be possible to set things up so that models with consistent sizes/shapes can use the traces from other layers.




### colldata79 · 2026-01-30



Update on #1496 — torch.compile for GPTQ quantization + benchmarks + validation

This addresses the request in #1496 to revive the idea of compiling GPTQ helpers (e.g. gptq_quantize.py hot path) and include runtime benchmarks to validate it.

What I changed
- Added an **opt-in** switch on GPTQModifier: `enable_torch_compile=...`
- When enabled, compile the GPTQ inner-loop helper `_process_block` with:
  - `torch.compile(dynamic=True)` (inductor backend)
- Default remains **disabled** to avoid changing behavior for existing users.

Why this helps
GPTQ quantization spends most of its time in the repeated per-block processing loop. Compiling that loop significantly reduces Python overhead and fuses/optimizes the hot path.

Environment (repro)
- Python: 3.10.12
- PyTorch: 2.9.1+cu128 (CUDA 12.8)
- GPU: Tesla V100-SXM2-16GB
- Driver: 535.288.01
- Setup details + env capture are included in the attached artifacts.

Benchmark setup
- Model: Qwen/Qwen2.5-3B (W4A16 GPTQ)
- Calibration: 256 samples, max seq len 512 (open_platypus)
- Block size: 128
- Measured baseline vs compiled over multiple runs; also included tiny model (TinyLlama) and block-size stress tests in the suite.

Results (Qwen2.5-3B)
Wall time
- Baseline mean: 879.3s (14m39s)
- Compiled warm mean: 477.6s (7m58s)
- Compiled cold (includes compilation): 512.5s (8m32s)
- Speedup (warm): **1.84×**
- Estimated one-time compile overhead: **~34.9s** (cold − warm_mean)

Stability / dynamo behavior
- Unique graphs compiled: 2
- Graph breaks: 0
- Calls captured: 6,406
=> No evidence of recompilation churn for this setup.

GPU memory
- Peak allocated: unchanged (2.361 GB baseline → 2.361 GB compiled)
- Peak reserved: small increase (2.961 GB → 3.049 GB, ~+3%)

Validation / sanity checks included
1) Memory instrumentation sanity (“memory sentinel”)
   - Expected 953.67 MB vs measured 954.00 MB (delta 0.33 MB) and freed correctly
   - Intended to increase confidence in the memory measurements.

2) Storage-size proof (view/inflated-storage detection when saving weights)
   - Both TinyLlama and Qwen runs show total logical == total storage for baseline vs compiled
   - No views / no inflated storage detected in these runs.
   - Note: this does NOT disprove historical memory-spike reports; it just means this implementation/run does not reproduce view-based storage inflation.

3) Numerical/output check (behavioral check)
   - Fixed prompts + greedy decoding (do_sample=False) to make comparisons consistent.
   - Outputs are **not bitwise identical** (token match ~68–69% on a small prompt set; strict “equivalent” flag is false),
     but generations remain sensible. Differences are consistent with FP nondeterminism + sensitivity of greedy argmax.

Repro commands
- Qwen baseline + compiled:
  `python benchmark_gptq_compile.py --scenario qwen3b --mode both --num_runs 2`
- TinyLlama baseline + compiled:
  `python benchmark_gptq_compile.py --scenario tinyllama --mode both --num_runs 3`
- Numerical check:
  `python benchmark_gptq_compile.py --scenario qwen3b --mode numerical_check`
- Full suite:
  `bash run_benchmark.sh` (runs tinyllama, qwen3b, and blocksize stress tests and generates a summary)


Please can someone look at this and provide some needed followup/feedback 


@HDCharles ,Thanks for the information  i will review your recommendations 
