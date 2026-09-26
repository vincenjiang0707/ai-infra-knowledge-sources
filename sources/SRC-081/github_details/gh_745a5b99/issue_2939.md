# [Issue #2939] GPTQ silently corrupts fused-expert MoE (Qwen3.6-A3B) on 0.12.0 — fixed on main by #2847/#2848, please cut a release

source: https://github.com/vllm-project/llm-compressor/issues/2939
state: closed | updated: 2026-08-21T10:03:20Z
labels: 

## 正文

**Summary**: Running `GPTQModifier(targets="Linear", scheme="W4A16")` on `Qwen/Qwen3.6-35B-A3B` (fused-expert MoE: routed experts stored as 3D fused tensors `mlp.experts.gate_up_proj`) with **llm-compressor 0.12.0** completes without error and produces a compressed-tensors checkpoint that vLLM loads successfully — but the model output is completely corrupted (benchmark scores at random-choice level: MMLU 82.2→24.7, KMMLU 62.6→26.5; generated text is garbage). The checkpoint contains `experts.gate_up_proj_packed/_scale/_shape` tensors that neither vLLM nor transformers can map.

**Environment**: llm-compressor 0.12.0 (PyPI latest as of 2026-07), compressed-tensors 0.17.1, transformers 5.10.1, vllm 0.24.0, 4×L40S.

**Repro (0.12.0)**:
1. `oneshot(model=Qwen3.6-35B-A3B, recipe=[GPTQModifier(targets="Linear", scheme="W4A16", ignore=["lm_head","re:.*visual.*"], kv_cache_scheme={per-tensor fp8})], dataset=ultrachat 512×2048)` — GPTQ error metrics look normal during calibration.
2. Serve with vLLM → generations are garbage; loglikelihood benchmarks at chance level.
3. Standard `nn.Linear` modules (attention, `shared_expert`) are unaffected — the same pipeline on dense Qwen3.5-4B/9B produces high-quality checkpoints (≤2.5pt degradation).

**Resolution verified on main**: we re-quantized with `0.12.1.dev64+` (includes #2848 — linearize up/down name swap fix — and #2847 — `qwen3_5_moe` conversion mapping), loading the model inside `load_context()`. The output layout became per-expert 2D (`experts.{i}.gate_proj.weight_packed`), vLLM 0.24.0 serves it as-is, and quality is at BF16 parity (KMMLU 62.42 vs 62.58, MMLU 82.37 vs 82.17).

**Requests**:
1. Please cut a release including these fixes — every 0.12.0 user quantizing fused-expert MoE currently gets a silently-corrupted checkpoint.
2. Consider a hard error (instead of silent success) when fused 3D expert tensors reach the packing path without linearization.

## 评论 (5)

### brian-dellabetta · 2026-07-21

Hi @narfian , can you install from main in the meantime?

### titanium-temu · 2026-07-22

I found that all the moe models of qwen3 and qwen3.5, when quantized use llm-compressor-0.12.0, output garbled characters.

### brian-dellabetta · 2026-07-22

@titanium-temu is it working for you on main?

### titanium-temu · 2026-07-23

> [@titanium-temu](https://github.com/titanium-temu) is it working for you on main?

yes, it works

### dsikka · 2026-08-21

Should be resolved as of v0.13. Closing off
